# Python Lists

> **How to read this document.** Throughout, two levels are kept deliberately separate:
>
> - **Language semantics** — what *Python the language* guarantees about lists. True for any conforming implementation (CPython, PyPy, etc.).
> - **CPython implementation** — how *the reference C implementation* actually delivers those guarantees. Version-specific; the numbers here are measured on **CPython 3.12.3, 64-bit Linux**. Check the source for your own version before quoting exact constants in an interview.
>
> Wherever a number appears (byte sizes, growth steps, timings), it was measured on this machine, not recalled from memory.

---

## 1. Definition

A **list** is Python's built-in mutable sequence type.

| Property | Meaning |
|---|---|
| **Ordered** | Elements keep insertion order; position is meaningful and stable. |
| **Mutable** | You can change contents in place after creation (add, remove, reassign). |
| **Dynamically sized** | Grows and shrinks at runtime; no fixed capacity you manage. |
| **Heterogeneous** | Elements may be of *different* types in the same list. |
| **Allows duplicates** | The same value — and even the same object — can appear many times. |

### Correction to a common belief (and to the handwritten notes)

> ❌ "A list is homogeneous — all elements must be the same type."

That describes an **array** (C array, `array` module, NumPy `ndarray`), **not** a Python list. A Python list is **heterogeneous**:

```python
lst = [10, "hello", 3.14, True, [1, 2]]
# element types: int, str, float, bool, list
```

The *why* behind this is the whole reason lists are the shape they are, and it's covered in §3.

---

## 2. Creating Lists

```python
[]                      # empty list literal (fastest, idiomatic)
[1, 2, 3]               # populated literal
list()                  # empty list via constructor
list("abc")             # from an iterable -> ['a', 'b', 'c']
list(range(5))          # -> [0, 1, 2, 3, 4]
[0] * 5                 # -> [0, 0, 0, 0, 0]  (repetition)
[x*x for x in range(5)] # comprehension (see §10)
```

**Trap — repetition of mutable elements:**

```python
grid = [[0] * 3] * 3        # THREE references to the SAME inner list
grid[0][0] = 9              # -> [[9,0,0],[9,0,0],[9,0,0]]  (all rows change)

grid = [[0] * 3 for _ in range(3)]   # correct: three distinct inner lists
```

`[x] * n` copies the **reference** `n` times, not the object. This is a direct consequence of reference semantics (§12) and a classic interview gotcha.

---

## 3. How a List Exists in Memory

This is the conceptual core. Everything else follows from it.

A Python list does **not** store raw values contiguously. It stores a **contiguous array of pointers** (references) to `PyObject`s that live elsewhere on the heap.

```
        PyListObject                     objects on the heap
        (the "list" itself)              (each a full PyObject)
        ┌───────────────────┐
ob_item │ ptr ───────────────┼────────►  int 10
        │ ptr ───────────────┼────────►  str "hello"
        │ ptr ───────────────┼────────►  float 3.14
        │ ptr ───────────────┼────────►  bool True
        │ ptr ───────────────┼────────►  list [1, 2]
        └───────────────────┘
         ▲ contiguous block          ▲ scattered, arbitrary types & sizes
           of equal-size pointers
```

**Why this design gives you heterogeneity for free:** every slot is just a pointer of the same fixed width (8 bytes on 64-bit). A pointer to an `int` and a pointer to a 10 KB `str` are the same size. The list doesn't know or care what it points at — so mixing types costs nothing structurally.

**Verified — the slot holds a reference, not a copy:**

```python
a = 10
lst = [a]
id(a) == id(lst[0])   # True  -> same object, the list stores a's address
```

**Related CPython detail — small-int cache:** CPython pre-creates and reuses the integer objects **−5 through 256**, so `a = 10; b = 10; a is b` is `True`. This is a memory optimization, *not* a language guarantee.

> ⚠️ Honesty note: `x = 1000; y = 1000; x is y` may *also* print `True`, but that's a **different** mechanism — constant deduplication within a single compiled code object — and it is **not** guaranteed. Never rely on `is` for value equality; use `==`.

---

## 4. List Growth Internals

Because a list is backed by a fixed-size array of pointers, growing past its capacity requires allocating a bigger array and copying the pointers over. To avoid doing that on every `append`, CPython **overallocates**.

Two distinct quantities:

- **length** (`ob_size`) — how many elements you actually have.
- **capacity** (`allocated`) — how many pointer slots are reserved.

### Measured overallocation (CPython 3.12.3, 64-bit)

`getsizeof(list) = 56-byte header + 8 bytes × capacity`. Reallocations happen only when length exceeds capacity:

| length at realloc | `getsizeof` (bytes) | inferred capacity (slots) |
|---:|---:|---:|
| 1 | 88 | 4 |
| 5 | 120 | 8 |
| 9 | 184 | 16 |
| 17 | 248 | 24 |
| 25 | 312 | 32 |
| 33 | 376 | 40 |

### The growth formula

In `list_resize()` (`Objects/listobject.c`), CPython 3.12 computes:

```c
new_allocated = ((size_t)newsize + (newsize >> 3) + 6) & ~(size_t)3;
```

i.e. **new capacity ≈ newsize + newsize/8 + 6, rounded down to a multiple of 4.** That reproduces the table above exactly (e.g. newsize 17 → 17 + 2 + 6 = 25 → `& ~3` → 24). The growth factor is roughly **1.125×**, not 2× as many other languages use — CPython trades a bit more copying for lower memory overhead.

> The exact constants have changed across CPython versions. The *idea* — geometric overallocation — is stable; the specific `>> 3` and `+ 6` are 3.x-era details. Verify against your version's `listobject.c`.

### Why `append()` is amortized O(1)

Most appends land in already-reserved capacity → O(1). Occasionally one triggers a resize that copies all *n* pointers → O(n). But because capacity grows geometrically, resizes become exponentially rarer, so the **average cost per append over many appends is O(1)**. That's what "amortized" means: not every call, but the running average.

---

## 5. Indexing

```python
lst[0]     # first
lst[-1]    # last (negative counts from the end)
```

**Language semantics:** indexed access is O(1).

**CPython mechanism:** `ob_item` is a contiguous C array of pointers. `lst[i]` is essentially:

```
address_of_slot = ob_item_base + i * sizeof(pointer)   # one multiply + add
value_pointer   = *address_of_slot                      # one memory read
```

A bounds check (`0 <= i < ob_size`, with negatives normalized by adding `ob_size`) plus a single pointer load. No scanning — that's the O(1). Contrast with a linked list, where reaching index *i* means walking *i* nodes (O(n)).

---

## 6. Slicing

```python
lst[start:stop:step]   # all parts optional
lst[1:4]               # indices 1,2,3
lst[:]                 # full shallow copy
lst[::-1]              # reversed copy
lst[1:3] = [9, 9, 9]   # slice assignment: can change length
```

**Slicing creates a NEW list** (a **shallow copy** — new outer list, same inner object references):

```python
orig = [1, 2, [3, 4]]
cp = orig[:]
orig is cp            # False  -> different list objects
orig[2] is cp[2]      # True   -> the nested list is SHARED
cp[2].append(99)
orig                  # [1, 2, [3, 4, 99]]  -> mutation leaks across
```

**Complexity:** building the slice is O(k) in the number of elements copied (it copies *pointers*, not the pointed-to objects).

---

## 7. Mutation (in-place methods)

All of these modify the list in place and (except where noted) return `None`.

| Method | Effect | Complexity |
|---|---|---|
| `append(x)` | Add **one** element `x` at the end | Amortized **O(1)** |
| `extend(it)` | Add each element of iterable `it` | **O(k)**, k = len(it) |
| `insert(i, x)` | Insert `x` before index `i` | **O(n)** (shifts tail) |
| `remove(x)` | Delete first element `== x` | **O(n)** (search + shift) |
| `pop()` | Remove & return **last** element | **O(1)** |
| `pop(i)` | Remove & return element at `i` | **O(n)** for non-tail |
| `clear()` | Remove all elements | O(n) (drops refs) |
| `reverse()` | Reverse in place | O(n) |
| `sort()` | Sort in place (Timsort) | O(n log n) |

### `append` vs `extend` (correction to the notes)

> ❌ Notes said: "extend allows appending multiple elements... append adds one at a time, extend adds multiple."

Half right, but the crucial distinction is *what counts as an element*:

```python
la = [1, 2, 3]; la.append([4, 5])   # -> [1, 2, 3, [4, 5]]   ONE element (a list)
le = [1, 2, 3]; le.extend([4, 5])   # -> [1, 2, 3, 4, 5]     iterates, adds each
```

`extend` accepts **any iterable**, and a string *is* an iterable of characters — so this (from the notes) is a sharp illustration:

```python
l = [1, 2, 3]; l.extend("goo")      # -> [1, 2, 3, 'g', 'o', 'o']   (iterates the str)
l = [1, 2, 3]; l.append("goo")      # -> [1, 2, 3, 'goo']           (one str element)
```

Internally:
- `append(x)` stores **one reference** to `x`.
- `extend(iterable)` runs the iterator protocol over `iterable` and stores a reference for **each** item produced. `l.extend(x)` is equivalent to `l += x`.

### Why `insert(0, x)` is O(n)

To insert at the front, every existing pointer must shift one slot right (via `memmove`) before the new pointer goes in slot 0. **Measured, 20,000 operations on this machine:**

```
append(0)    :  6.49 ms
insert(0, 0) : 39.18 ms   (~6x slower here, and the gap widens as n grows —
                            insert-at-front over a loop is O(n²) total)
```

If you need cheap insertion/removal at *both* ends, that's what `collections.deque` is for (§16).

### `del`, `remove`, `pop`, `clear` — when to use which

```python
del lst[i]        # delete by index (or `del lst[i:j]` for a slice)
del lst           # unbind the NAME entirely (list may be GC'd if no other refs)
lst.remove(v)     # delete by VALUE when you don't know the index; first match only
lst.pop()         # remove & RETURN last (use when you want the value back)
lst.pop(i)        # remove & return at index i
lst.clear()       # empty it in place; equivalent to lst[:] = []
```

Use `remove` when you know the value but not the position; use `del`/`pop` when you know the position.

> ⚠️ Correction to the notes: `remove` matches by `==` **and by type**. The notes wrote `l.remove("5")` against an int list `[1,2,3,4,5]` — that raises `ValueError`, because the string `"5"` never equals the int `5`. You want `l.remove(5)`. If the value is absent, `remove` (like `index`) raises `ValueError`, so guard with `if v in lst:` when unsure.

---

## 8. List Methods vs Python Built-ins

Two different things people lump together:

**List methods** — attached to the object, called as `lst.method(...)`:
`append`, `extend`, `insert`, `remove`, `pop`, `clear`, `index`, `count`, `sort`, `reverse`, `copy`.

**Built-in functions** — general functions that *accept* a list (or any iterable):

| Built-in | Does | Note |
|---|---|---|
| `len(lst)` | length | O(1) — reads `ob_size`, doesn't count |
| `min` / `max` | smallest / largest | O(n); needs orderable elements |
| `sum(lst)` | numeric total | O(n) |
| `sorted(lst)` | **new** sorted list | doesn't mutate; `lst.sort()` does |
| `reversed(lst)` | reverse **iterator** | lazy; wrap in `list()` to materialize |
| `any` / `all` | truthiness fold | short-circuits |
| `enumerate(lst)` | `(index, value)` pairs | lazy iterator |
| `zip(a, b)` | pair up iterables | stops at shortest |
| `map(f, lst)` | apply `f` lazily | returns iterator |
| `filter(f, lst)` | keep where `f` true | returns iterator |

### `sorted()` vs `.sort()` (a distinction the notes half-captured)

```python
new = sorted(lst)               # returns a NEW list; lst unchanged
new = sorted(lst, reverse=True) # descending
lst.sort()                      # sorts IN PLACE; returns None
lst.sort(key=len, reverse=True) # by a key, descending
```

Common bug: `lst = lst.sort()` sets `lst` to `None`, because `.sort()` returns `None`.

### `index()` — and the notes' email example

```python
lst.index(value)          # first index of value; ValueError if absent
lst.index(value, start)   # search from `start`

sample = "abc@gmail.com"
sample[:sample.find("@")] # 'abc'  -> str.find, not list.index, but same idea
```

`list.index` is O(n): it scans until it finds a match.

### Removing duplicates (from the notes)

Your notes had the classic order-preserving dedup:

```python
def dedup(lst):
    dup = []
    for i in lst:
        if i not in dup:      # <-- this membership test is the catch
            dup.append(i)
    return dup

dedup([1, 1, 2, 2, 3, 3, 4, 4])   # -> [1, 2, 3, 4]
```

It's correct and preserves order, but `i not in dup` scans the growing `dup` list every iteration → **O(n²)** overall. Two faster ways, both worth knowing for interviews:

```python
# Fastest, order NOT preserved — O(n). Only works if elements are hashable.
list(set(lst))

# O(n) AND order-preserving — the idiomatic modern answer.
# dict keys are unique and (since 3.7) insertion-ordered.
list(dict.fromkeys(lst))
```

The upgrade from your loop to `dict.fromkeys` is exactly the "replace O(n) membership on a list with O(1) membership on a hash structure" move from §13 — the kind of complexity improvement an interviewer wants you to reach for out loud.

---

## 9. Iteration Internals

A `for` loop does **not** use indices under the hood. It uses the **iterator protocol**:

```python
it = iter(lst)      # calls lst.__iter__() -> a list_iterator holding an index
next(it)            # calls it.__next__() -> next element, advances the index
# ...raises StopIteration when exhausted; the for loop catches that silently
```

So `for x in lst:` is roughly:

```python
it = iter(lst)
while True:
    try:
        x = next(it)
    except StopIteration:
        break
    ...              # loop body
```

**Iterator vs list:** the list is the container (holds the data); the iterator is a lightweight cursor over it (holds a position). An iterator is single-pass and lazy; a list is re-iterable and fully materialized.

---

## 10. List Comprehensions

```python
[expr for item in iterable]                       # map
[expr for item in iterable if cond]               # map + filter
[expr if cond else alt for item in iterable]      # conditional expression
[x for row in matrix for x in row]                # nested / flatten
```

**Execution model:** a comprehension builds a list by evaluating `expr` for each produced item, appending as it goes. In Python 3 it runs in its **own scope**, so the loop variable does **not** leak:

```python
[i for i in range(3)]
i    # NameError -> i did not escape the comprehension
```

**vs `map`/`filter`:** comprehensions are eager (return a list now); `map`/`filter` are lazy (return iterators). Comprehensions are usually more readable and, for simple bodies, about as fast — favor them unless you specifically want laziness.

---

## 11. Copying

| Technique | Depth | Notes |
|---|---|---|
| `b = a` | **no copy** | `b` is another name for the *same* list (§12) |
| `a.copy()` | shallow | new outer list, shared inner objects |
| `a[:]` | shallow | same as `.copy()` |
| `list(a)` | shallow | same effect |
| `copy.copy(a)` | shallow | explicit |
| `copy.deepcopy(a)` | **deep** | recursively copies nested objects too |

**Shallow vs deep — the difference only shows with nested mutables:**

```python
import copy
a = [1, [2, 3]]
s = a.copy()                 # shallow
s[1].append(99)              # a becomes [1, [2, 3, 99]]  -> inner list shared

d = copy.deepcopy(a)         # deep
d[1].append(0)               # a unaffected -> inner list was cloned
```

---

## 12. References and Mutability

Assignment **never copies** in Python — it binds a name to an object.

```python
p = [1, 2, 3]
q = p            # q and p point at the SAME list object
q.append(4)
p                # [1, 2, 3, 4]   -> both see it
p is q           # True
```

This is **aliasing**. Two consequences to keep straight:

- **Mutating** through any alias (`q.append`, `q[0]=...`) is visible through every alias — same object.
- **Rebinding** an alias (`q = [9]`) only redirects that one name; `p` still points at the original.

**Passing a list to a function** passes the reference, so the function can mutate the caller's list. To protect the caller, copy first (`func(lst[:])`) or don't mutate the argument.

**Mutable default argument trap:**

```python
def f(x, acc=[]):     # acc is created ONCE, at def time, and reused
    acc.append(x)
    return acc
f(1); f(2)            # -> [1, 2]  (surprise: state persists across calls)

def f(x, acc=None):   # correct idiom
    if acc is None:
        acc = []
    ...
```

---

## 13. Time Complexity (cheat sheet)

| Operation | Complexity | Why |
|---|---|---|
| Index `lst[i]` | **O(1)** | pointer arithmetic + one load |
| Store `lst[i] = x` | **O(1)** | overwrite one slot's pointer |
| `len(lst)` | **O(1)** | reads cached `ob_size` |
| `append` | **O(1)** amortized | overallocation absorbs most calls |
| `pop()` (end) | **O(1)** | just decrement size |
| `insert(0, x)` / `pop(0)` | **O(n)** | shift all trailing pointers |
| `remove(v)` | **O(n)** | search then shift |
| `x in lst` | **O(n)** | linear scan (use a `set`/`dict` for O(1)) |
| `lst.index(v)` | **O(n)** | linear scan |
| Slice `lst[a:b]` | **O(k)** | copies k pointers |
| `sort()` | **O(n log n)** | Timsort |
| `reverse()` | **O(n)** | swap ends inward |
| `min`/`max`/`sum` | **O(n)** | one pass |

**Interview reflex:** repeated membership tests or de-duplication over a list are O(n) each → O(n²) in a loop. Convert to a `set`/`dict` for O(1) lookups when the values are hashable.

---

## 14. CPU / Memory Perspective

**The array of pointers is contiguous — the objects are not.**

- Walking `ob_item` (the pointer array) is cache-friendly: the pointers sit next to each other in RAM, so the CPU's prefetcher and cache lines help.
- But each element access then **chases that pointer** to wherever the object lives — which may be a cache miss. This is **pointer chasing**, and it's why a Python `list` of ints is far slower to crunch numerically than a NumPy array, where the raw values sit packed together (great **cache locality**, no per-element pointer or object header).

**Shifting (insert/delete in the middle):** implemented with `memmove` over the pointer array — moving 8-byte pointers, not the objects. Still O(n) pointers moved.

**Resizing (§4):** allocate a larger block, `memcpy` the existing pointers across, free the old block. The *objects* aren't touched — only the pointer array is reallocated.

**Reference counting:** every `PyObject` carries `ob_refcnt`. Putting an object in a list **increments** its refcount; removing it (or clearing/deleting the list) **decrements** it. An object is freed when its count hits 0. A separate **cyclic garbage collector** handles reference cycles (e.g. a list that contains itself) that plain refcounting can't reclaim.

---

## 15. CPython Internals (`PyListObject`)

Defined in `Include/cpython/listobject.h`; operations in `Objects/listobject.c`.

```c
typedef struct {
    PyObject_VAR_HEAD        // includes ob_refcnt, ob_type, and ob_size (= length)
    PyObject **ob_item;      // pointer to the array of element pointers
    Py_ssize_t allocated;    // capacity: how many slots are reserved
} PyListObject;
```

Mapping to everything above:

- `ob_size` → **length** → makes `len()` O(1).
- `allocated` → **capacity** → the overallocation from §4; `allocated >= ob_size` always.
- `ob_item` → the **contiguous pointer array** → makes indexing O(1) and gives cache-friendly iteration over the pointers.
- Growth lives in **`list_resize()`**; the geometric policy is why `append` is amortized O(1).

On this build: empty-list header = **56 bytes**, each slot = **8 bytes**, so `getsizeof = 56 + 8 × capacity`.

---

## 16. Interview Questions (with crisp answers)

**Why is list access O(1)?**
Elements are referenced through a contiguous C array of pointers (`ob_item`). Index *i* is one multiply-add to find the slot plus one memory read — no scanning.

**Why is `append` amortized O(1)?**
The backing array is overallocated geometrically (~1.125× in CPython). Most appends use spare capacity (O(1)); the occasional resize is O(n) but rare enough that the average per append is O(1).

**Why is `insert(0, x)` O(n)?**
Every existing pointer must shift one slot to make room at the front (`memmove`), so cost scales with length. (Measured ~6× slower than `append` at 20k ops on this machine, widening with n.)

**Why are lists heterogeneous?**
Slots hold same-width pointers to `PyObject`s, not raw values. A pointer to an `int` and a pointer to a `str` are identical in size, so mixing types costs nothing structurally.

**Why can't a list be a dictionary key (or set element)?**
Keys must be **hashable**, and hashability requires immutability of the hash over the object's lifetime. Lists are mutable, so they deliberately have no `__hash__` — `{[1,2]: "x"}` raises `TypeError: unhashable type: 'list'`. Use a `tuple` (of hashable items) instead.

**list vs tuple?**
Tuple is immutable, fixed-size, hashable (if its contents are), and more memory-compact (no overallocation, smaller header) — measured **80 B vs 104 B** for five ints. Use a tuple for fixed heterogeneous records and dict keys; a list for a mutable, growable homogeneous-*or*-mixed sequence.

**list vs array (`array` module / NumPy)?**
An array stores **raw typed values** contiguously (homogeneous, compact, cache-friendly, fast numeric ops). A list stores **pointers** to boxed objects (heterogeneous, flexible, but pointer-chasing and heavier per element).

**list vs deque (`collections.deque`)?**
A list is O(1) at the *end* but O(n) at the *front*. A `deque` is a doubly-linked list of fixed-size blocks giving **O(1) append/pop at both ends** — the right choice for queues/sliding windows. Trade-off: `deque` has O(n) random indexing in the middle.

---

## Appendix — reproduce the measurements yourself

Every number in this doc came from running the following on CPython 3.12.3. Re-run it on your own interpreter; if a value differs, trust *your* output and update the doc — implementation details drift across versions.

```python
import sys, timeit

# heterogeneity
print([type(x).__name__ for x in [10, "hi", 3.14, True, [1, 2]]])

# reference held, not copied; small-int cache
a = 10; print(id(a) == id([a][0]), (10 is 10))

# overallocation growth
l, prev, empty = [], sys.getsizeof([]), sys.getsizeof([])
for i in range(33):
    l.append(i); s = sys.getsizeof(l)
    if s != prev: print(len(l), s, (s - empty)//8); prev = s

# append vs extend
la=[1,2,3]; la.append([4,5]); le=[1,2,3]; le.extend([4,5]); print(la, le)

# shallow copy shares nested objects
o=[1,2,[3,4]]; c=o[:]; c[2].append(99); print(o is c, o)

# O(1) append vs O(n) insert(0)
print(timeit.timeit("b.append(0)", "b=[]", number=20000))
print(timeit.timeit("b.insert(0,0)", "b=[]", number=20000))

# tuple lighter than list
print(sys.getsizeof([1,2,3,4,5]), sys.getsizeof((1,2,3,4,5)))
```