# InfoBeans — Theory Questions: Answers & Revision Notes

| # | Question | Outcome |
|---|----------|---------|
| t1 | Difference between list, set and dictionary |
| t2 | Give an example of inheritance |
| t3 | Give an example of super() |

---

## t1 — list vs set vs dictionary

| # | list | tuple | set | dictionary |
|------------|----------|---------|---------|---------|
| Syntax | [1, 2, 3] | (1, 2, 3) | {1, 2, 3} | {"a": 1} |
| Ordered | Yes | Yes | No | Not necessary but Yes(3.7+) |
| Duplicates | Allowed | Allowed | Removed | Keys unique, values may repeat |
| Indexing | x[0] | x[0] | Not Subscriptable | By Key - x["a"] |
| Mutable | Yes | No | Yes | Yes |
| Hashable | No | Only if all it's items are | No(Frozenset is) | No
| Membership Test | O(n) | O(n) | O(1) | O(1) on keys |
| Typical Use | Ordered Sequence | Fixed record, dict key | dedupe, fast lookup | Key to Value mapping |

### Mutability - What can each one hold?

The important point and the one interviewrs push on: Immutable does not mean "can only contain immutable things". Those are two separate questions.
`list, tuple and dict values accept anything` - mutable or immutable, mixed freely.

```python
mixed = [1, "a", [2, 3], ["k": "v"], (4, 5)]            # Fine
record = (1, "a", [2, 3])                               # Tuple holding a mutable list - fine
d = {"key": [1, 2, 3]}                                  # dict value is mutable list - fine
```

set elements and dict keys must be hashable, which in practise means immutable:

```python
{(1, 2)}                # OK - tuple is hashable
{[1, 2]}                # TypeError - unhashable type: list
{[1, 2]: "x"}           # TypeError - unhashable type: list
{(1, 2): [1, 2]}        # OK -  key hashable, value need not to be
```

A tuple freezes which object it points to, not the object themselves. If one of them is a list, that list is still mutable:

```python
t=(1, [2, 3])
t[1].append(4)
print(t)                # (1, [2, 3, 4]) -- the tuple change

t[0] = 99               #TypeError: 'tuple' object does not support item assignmet
```

Both are consistent: rebinding a slot is forbidden, mutataing the object is a slot is not.
This has direct consquence - such tuple is no longer hashable, so it can not be a set element or dict key:

```python
hash((1, 2))            # fine
hash((1, [2]))          # TypeError: unhashable type: 'list'
```

A tuple is hashable if only every item inside it is hashable.

### fronzenset - the immutable set

```python
fs = frozenset([1, 2, 3])
print({frozenset([1, 2]), frozenset([3])})      # a set of sets, only possible via frozenset
```

Because a normal `set` is mutable, it is unhashable, so it can not be nested inside another set or used as dict key. `frozenset` exists only for exactly that case.

### Order preserving dedupe

`set` drops duplicates, but looses ordering, so the two are combined:

```python
nums = [3, 1, 3, 2]
print(set(nums))                    # {1, 2, 3} - order gone
print(list(dict.fromkeys(nums)))    # [3, 1, 2] - duplicates gone, order preserved.
```

## t2 — Inheritance

Inheritance lets a chile clss aquire the attributes and methods of a parent class, so shared behavior is written once and specialised where it differs

```python
class Employee:
    def __init__(self, name, emp_id):
        self.name = name
        self.emp_id = emp_id

    def describe(self):
        return f"{self.name} ({self.emp_id})"

    def access_level(self):
        return "Standad"

class Manager(Employee):                        # Manager inherits from Employee
    def access_level(self):                     # Overrides the parent method           
        return "Elevated"

e = Employee("Asha", "E101")
m = Manager("Ravi", "E102")

print(e.describe())                             # Asha (E101)
print(m.describe())                             # Ravi (E102)
print(e.access_level())                         # Standard
print(m.access_level())                         Elevated
```

Manager never defines `describe()`; it comes from `Employee`. Only the behavior that actually differs (`access_level`) is redefined.
Types: Single, Multiple (`class C(A, B)`), Multilevel, hierarchical

## t3 — super()

`super()` returns the proxy object that delegates to the parent class. It is used when a child overrides a method but still wants the parent's logic to run as part of it. Most commonly used in __init__

```python
class Employee:
    def __init__(self, name, emp_id):
        self.name = name
        self.emp_id = emp_id

class Manager(Employee):
    def __init__(self, name, emp_id, team_size):
        super().__init__(name, emp_id)              # Parent sets name and emp_id
        self.team_size = team_size                  # child adds it's own

m = Manager("Ravi", "E102", 6)
print(m.name, m.emp_id, m.team_size)                # Ravi E102 6
```