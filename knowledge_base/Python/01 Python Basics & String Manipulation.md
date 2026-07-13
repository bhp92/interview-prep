## 1. Control Flow & Loops

Python has only **two** loops:

1. **`for` loop**
2. **`while` loop**


### Loop Choice Strategy

* Use a **`for` loop** when you know the range or the exact number of iterations beforehand.
* Use a **`while` loop** when you do not know how long the loop is required to run (such as when a condition needs to be operated for a validation).

### The `range()` Function

* **Syntax:** `range(start, stop, step)`
* **Example:** `range(1, 101)` generates a sequence containing `1, 2, 3, 4, 5` up to `100`.

#### Decrementing Range Question

> **What does `range(8, -1, -1)` do?**

* **`8`** is the starting point.
* **`-1`** is the ending point (exclusive, so it stops at `0`).
* **`-1`** is the step size.
* **Output Sequence:** `8, 7, 6, 5, 4, 3, 2, 1, 0`

---

## 2. Code Snippets & Case Studies

### Number Guessing Game

```python
import random #

def guess_number(): #
    n = random.randint(1, 100) #
    i = int(input("Guess a number: ")) #
    
    while i != n: #
        if i < n: #
            i = int(input("Higher: ")) #
        else: #
            i = int(input("Lower: ")) #
            
    print("Guessed correctly!") #

guess_number() #

```

# Comment: Fixed the spelling errors from the original text (`gues-number`, `conile`, `imighuang`, `lowed`, `guesed forrect`).

### Linear Search & Loop Control

```python
# The break statement can be used in a linear search
for name in names: #
    if name == "Bharati": #
        break

```

* **`continue` statement:** Used for skipping a particular iteration.
* **`pass` statement:** A statement which can be used as a placeholder for code you may write later, but want to write the container function beforehand.

### Python Expressions & Formatting

* **Generator Expression Example:**
```python
has_upper = any(c.isupper() for c in string) #

```


# Comment: Corrected from `hosupper =any (cisuppere) forcing)`.


* **String Float Formatting:**
```python
average = 84.3333 #
print(f"Average: {average:.1f}")  # Output: 84.3
print(f"Average: {average:.2f}")  # Output: 84.33

```



---

## 3. Core Built-in Functions

| Function | Description / Example |
| --- | --- |
| **`print()`** | Outputs data to the screen. |
| **`input()`** | Takes input from the user. |
| **`type()`** | Returns the data type of a variable (`int`, `float`, `str`). |
| **`abs()`** | Absolute value (Modulus): `abs(4) = 4` and `abs(-4) = 4`. |
| **`pow()`** | Power function: `pow(2, 3) = 2³ = 8` and `pow(2, -3) = 2⁻³ = 0.125`. |
| **`min()` / `max()**` | Returns the minimum or maximum: `min([2, 2, 3, 0, 5]) = 0`. `max("kolkata") = 't'` because the ASCII value of 't' is higher than the other characters. |
| **`round()`** | Rounds a number to given decimals: `c = 22/7 = 3.14285714...`, `round(c, 2) = 3.14`. |
| **`divmod()`** | Returns the quotient and remainder `(//, %)`: `divmod(5, 2) = (2, 1)`. |
| **`bin()` / `oct()` / `hex()**` | Converts to binary, octal, or hexadecimal: `bin(4) = 0b100`, `oct(4) = 0o4`, `hex(4) = 0x4`. |
| **`id()`** | Returns the unique memory address of a variable: `a = 3`, `id(a) = 140727404847984`. |
| **`ord()`** | Returns the ASCII value of a character: `ord('c') = 99` (lowercase), `ord('C') = 67` (uppercase). |
| **`len()`** | Gives the length of iterables like lists, dictionaries, sets, and strings. |
| **`sum()`** | Performs a sum operation on elements of an iterable, provided the elements are numerical: `sum([1, 2, 3]) = 6`. |
| **`help()`** | Gives documentation on methods: `help('print')`. |

---

## 4. Built-in Modules

* Using `help('modules')` gives a list of all built-in modules.
* **Definition:** A module is a Python file full of functions that can be imported into another Python file.

### `random` Module

```python
random.randint(1, 100) # Returns a random integer (e.g., 54)
a = [1, 2, 3, 4, 5]    #
random.shuffle(a)      # Shuffles the list in place (e.g., [2, 3, 4, 1, 5])

```

### `time` Module

```python
time.time()   # Returns seconds elapsed since Jan 1st, 1970 midnight
time.sleep(1) # Introduces a 1-second delay

```

### `os` Module

```python
os.getcwd()   # Gets the current working directory
os.listdir()  # Lists files in the current directory

```

---

## 5. Strings & Memory Encoding

### Machine Interpretation

For machines, characters are processed as Unicode characters. In order to understand a character, a machine first converts it to ASCII, and then converts it to binary.

$$\text{Character} \rightarrow \text{ASCII} \rightarrow \text{Unicode} \rightarrow \text{Binary}$$

### Encoding Standard Differences

| Feature | ASCII | Unicode |
| --- | --- | --- |
| **Bit Depth** | 8-bit | 16-bit |
| **Capacity** | Supported only 255 characters total | Supports characters of different global languages |

> **Resource:** Read the official documentation blog at `docs.python.org/3/howto/unicode.html`. Strings are sequences of Unicode characters.

---

## 6. Advanced String Slicing Rules

* **Syntax Pattern:** `[start:end:step]`
* A `step = 2` value means every 2nd element counting from zero.
* **Negative Indexing:** Slicing using `[-1:-5:-1]` moves in reverse order from the last element towards the 5th-last element.
* **Validity Constraints:** Slicing like `[-5:2:2]` is allowed, but slicing like `[1:5:-1]` is **not allowed** (returns an empty string).

### Directional Traversal Rule

Consider the start element, then consider the element right before the end element. Based on the sign of the step number, you either go from left to right or from right to left.

#### Example String Evaluation

Given: `s = "Hello"`

```python
s[-4:]    # Evaluates to "ello"
s[-4::1]  # Evaluates to "ello"
s[-4::-1] # Evaluates to "eH"   #

```

#### Slicing Index Combinations

* `[- : - : -]` $\rightarrow$ **Allowed**
* `[- : - : +]` $\rightarrow$ **Allowed**
* `[+ : + : -]` $\rightarrow$ **Not Allowed**
* `[+ : - : -]` $\rightarrow$ **Not Allowed**
* `[+ : + : +]` $\rightarrow$ **Allowed**

### Editing & Deletion

* When manipulating types, `del c` deletes the list container or string variable reference completely.

# Comment: Strings are immutable in Python. You can delete the entire string variable using `del`, but you cannot edit individual characters in place.

---

## 7. Comparative Expressions & Logic Evaluation

### Lexicographical Comparisons

String comparisons utilize alphabetical precedence sorting logic:

```python
"Mumbai" > "Pune"  # False (P comes after M alphabetically)
"Goa" < "Kolkata"  # True

```

Lowercase letters come after capital letters in the ASCII table (hence they have higher numerical values):

```python
"kol" < "Kol"      # False

```

### Short-Circuit Logic Evaluation Order

* `True or False` $\rightarrow$ Evaluates to `True`.
* `True or True` $\rightarrow$ Evaluates to `True` (stops evaluation at the first term).
* `True and True` $\rightarrow$ Evaluates to `True` (checks the second term).

---

## 8. Epilogue Script Notations

* जय श्रीराम
* ॥ ॐ श्री हनुमते नमः ॥