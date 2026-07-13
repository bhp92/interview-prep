# 08 Python Basics – Literals

## Introduction

Whenever we create a variable, we usually assign a value to it.

Example:

```python
age = 25

name = "Bharatish"

price = 99.99
```

The values assigned to these variables:

* `25`
* `"Bharatish"`
* `99.99`

are called **literals**.

In every programming language, literals represent **fixed values** written directly into the source code.

---

## Definition

> A **literal** is a fixed value written directly in the source code to represent data.

Another way to think about it is:

> A literal is the actual value assigned to a variable or used directly in an expression.

Example:

```python
age = 25
```

Here:

* Variable → `age`
* Literal → `25`

Similarly,

```python
name = "Alice"
```

* Variable → `name`
* Literal → `"Alice"`

---

## Why Are Literals Important?

Variables store data, but **literals provide the initial data**.

Without literals, variables would have no values to store.

Example:

```python
salary = 75000
```

Here,

* `salary` is the variable.
* `75000` is the literal.

---

# Types of Literals in Python

Python provides four major categories of literals.

1. Numeric Literals
2. String Literals
3. Boolean Literals
4. Special Literal (`None`)

---

# Numeric Literals

## Definition

> Numeric literals represent numbers written directly in the source code.

Python supports three primary numeric data types:

* Integer (`int`)
* Floating-point (`float`)
* Complex (`complex`)

Each of these can be written in different formats.

---

# Integer Literals

The most common integer format is **decimal (base 10)**.

Example:

```python
age = 25

marks = 90

temperature = -5
```

These are all decimal integer literals.

---

## Decimal Literals

Decimal numbers use digits:

```text
0 1 2 3 4 5 6 7 8 9
```

Example:

```python
number = 100
```

Output:

```python
print(number)
```

```text
100
```

This is the format you will use **most of the time**.

# Comment:

# Around 95% of everyday Python programs use decimal integer literals.

---

# Binary Literals

Computers internally work with binary numbers.

Python allows you to directly write binary values using the prefix:

```text
0b
```

or

```text
0B
```

Syntax:

```python
0b1010
```

Example:

```python
number = 0b1010

print(number)
```

Output

```text
10
```

Although you wrote the number in binary, Python prints its decimal equivalent.

---

### Understanding the Conversion

Binary:

```text
1010
```

means

```text
1×2³ + 0×2² + 1×2¹ + 0×2⁰

= 8 + 2

= 10
```

Therefore,

```python
0b1010
```

is equivalent to

```python
10
```

---

### More Examples

```python
print(0b1)
```

Output

```text
1
```

```python
print(0b11)
```

Output

```text
3
```

```python
print(0b100)
```

Output

```text
4
```

---

## When Are Binary Literals Used?

Most application developers rarely write binary literals.

However, they are useful in areas such as:

* Embedded systems
* Raspberry Pi programming
* Microcontrollers
* Hardware programming
* Bit manipulation
* Device registers

# Comment:

# Even if you rarely write binary literals yourself, understanding them is valuable because computers store all data internally in binary.

---

# Octal Literals

Python also supports octal (base 8) numbers.

Octal literals begin with:

```text
0o
```

or

```text
0O
```

Example:

```python
number = 0o12

print(number)
```

Output

```text
10
```

Explanation

```text
1×8¹ + 2×8⁰

= 8 + 2

= 10
```

---

## Digits Allowed in Octal

Only these digits are valid:

```text
0 1 2 3 4 5 6 7
```

Using `8` or `9` produces an error.

---

# Hexadecimal Literals

Python supports hexadecimal (base 16) numbers.

Hexadecimal literals begin with:

```text
0x
```

or

```text
0X
```

Example:

```python
number = 0xA

print(number)
```

Output

```text
10
```

Here,

```text
A = 10
```

Similarly,

```python
print(0xF)
```

Output

```text
15
```

---

## Digits Used in Hexadecimal

Hexadecimal uses

```text
0 1 2 3 4 5 6 7 8 9 A B C D E F
```

where

```text
A = 10
B = 11
C = 12
D = 13
E = 14
F = 15
```

---

## Comparing Integer Literal Formats

| Format      | Prefix | Example  | Decimal Value |
| ----------- | ------ | -------- | ------------: |
| Decimal     | None   | `10`     |            10 |
| Binary      | `0b`   | `0b1010` |            10 |
| Octal       | `0o`   | `0o12`   |            10 |
| Hexadecimal | `0x`   | `0xA`    |            10 |

---

# Floating-Point Literals

## Definition

Floating-point literals represent numbers containing a decimal point.

Example:

```python
price = 99.99

temperature = -12.5

pi = 3.14159
```

---

## Scientific Notation

Very large and very small numbers can be written using scientific notation.

Python uses

```text
e
```

or

```text
E
```

to represent

```text
× 10^
```

---

### Large Numbers

Example

```python
distance = 1.5e3

print(distance)
```

Output

```text
1500.0
```

because

```text
1.5 × 10³ = 1500
```

---

Another example

```python
print(2e6)
```

Output

```text
2000000.0
```

---

### Small Numbers

Example

```python
value = 1.5e-3

print(value)
```

Output

```text
0.0015
```

because

```text
1.5 × 10⁻³
```

means

```text
1.5 / 1000
```

---

## When Is Scientific Notation Useful?

Scientific notation is commonly used in:

* Astronomy
* Physics
* Chemistry
* Biology
* Finance
* Machine Learning

Example:

```python
speed_of_light = 3e8

electron_charge = 1.602e-19
```

# Comment:

# Scientific notation improves readability when working with extremely large or extremely small numbers.

---

# Complex Literals

Python has built-in support for complex numbers.

A complex number consists of:

```text
Real Part + Imaginary Part
```

Example:

```python
number = 3 + 4j
```

where

* Real part → `3`
* Imaginary part → `4j`

---

Python also allows purely imaginary numbers.

Example

```python
number = 5j
```

This is equivalent to

```text
0 + 5j
```

---

## Accessing the Real Part

Use the `.real` attribute.

Example

```python
number = 3 + 4j

print(number.real)
```

Output

```text
3.0
```

---

## Accessing the Imaginary Part

Use the `.imag` attribute.

Example

```python
number = 3 + 4j

print(number.imag)
```

Output

```text
4.0
```

---

# Summary – Numeric Literals

Python supports several ways to represent numbers.

| Type                | Example  |
| ------------------- | -------- |
| Decimal             | `100`    |
| Binary              | `0b1010` |
| Octal               | `0o12`   |
| Hexadecimal         | `0xA`    |
| Float               | `3.14`   |
| Scientific Notation | `2e5`    |
| Complex             | `3+4j`   |

---

*(Continued in the next response with **String Literals**, **Boolean Literals**, **Special Literal (`None`)**, **Unicode Strings**, **Raw Strings**, and the full chapter summary.)*

Continuing **Chapter 08**.

---

# String Literals

## Definition

> A **string literal** is a sequence of characters enclosed within quotation marks.

Strings are used to represent textual data such as:

* Names
* Addresses
* Email IDs
* Passwords
* Messages
* Sentences
* File paths

Examples:

```python
name = "Alice"

city = "Pune"

language = "Python"
```

---

## Single Quotes

Strings may be enclosed using single quotes.

Example:

```python
name = 'Alice'

city = 'Pune'
```

Output:

```python
print(name)

print(city)
```

```text
Alice
Pune
```

---

## Double Quotes

Strings may also be enclosed using double quotes.

Example:

```python
name = "Alice"

city = "Pune"
```

Output:

```text
Alice
Pune
```

Both are completely valid.

```python
name1 = "Python"

name2 = 'Python'
```

Both create exactly the same string.

# Comment:

# Use whichever style improves readability. A common convention is:

# - Single quotes for short strings.

# - Double quotes when the string contains an apostrophe.

Example:

```python
message = "It's a beautiful day."
```

instead of

```python
message = 'It's a beautiful day.'
```

which produces a syntax error.

---

## Triple Quotes

Triple quotes allow strings to span multiple lines.

Syntax:

```python
'''...'''
```

or

```python
"""..."""
```

Example:

```python
address = """
Flat No. 302
Sunrise Apartments
Pune
India
"""

print(address)
```

Output

```text
Flat No. 302
Sunrise Apartments
Pune
India
```

---

### When Are Triple Quotes Useful?

Triple-quoted strings are commonly used for:

* Multi-line text
* SQL queries
* HTML templates
* Long messages
* Documentation strings (Docstrings)

Example:

```python
html = """
<html>
    <body>
        <h1>Hello</h1>
    </body>
</html>
"""
```

# Comment:

# Triple quotes preserve line breaks exactly as written.

---

# Unicode String Literals

Python supports Unicode.

This means Python can store text from almost every language in the world.

Examples:

```python
english = "Hello"

hindi = "नमस्ते"

japanese = "こんにちは"

emoji = "😀"
```

Python 3 stores strings as Unicode by default.

---

## Unicode Escape Sequences

Unicode characters may also be written using escape sequences.

Example:

```python
smiley = "\U0001F600"

print(smiley)
```

Output

```text
😀
```

Another example:

```python
heart = "\u2764"

print(heart)
```

Output

```text
❤
```

# Comment:

# The transcript prefixes Unicode strings with `u`.

# In Python 2, `u"Hello"` indicated a Unicode string.

# In Python 3, every normal string is already Unicode, so the `u` prefix is optional.

Example:

```python
text = "Python"

text = u"Python"
```

Both are identical in Python 3.

---

# Raw Strings

Sometimes a string contains many backslashes.

Example:

```text
C:\Users\Bharatish\Documents
```

Normally,

```python
path = "C:\new"
```

does **not** mean what it appears to mean.

Python interprets

```text
\n
```

as a newline character.

Instead of:

```text
C:\new
```

Python sees:

```text
C:
ew
```

---

## Raw String Syntax

Prefix the string with:

```python
r
```

Example:

```python
path = r"C:\Users\Bharatish\Documents"

print(path)
```

Output

```text
C:\Users\Bharatish\Documents
```

Python treats every character literally.

---

### Raw Strings Are Commonly Used For

* Windows file paths

```python
path = r"C:\Program Files\Python"
```

* Regular Expressions (Regex)

```python
pattern = r"\d+"
```

* Escape-heavy strings

# Comment:

# Raw strings prevent Python from interpreting escape sequences like

# \n, \t, \, etc.

---

# Boolean Literals

## Definition

Boolean literals represent truth values.

Python has only two Boolean literals:

```python
True

False
```

Notice the capitalization.

Correct:

```python
True

False
```

Incorrect:

```python
true

false
```

Python is case-sensitive.

---

Example

```python
is_logged_in = True

is_admin = False
```

---

## Boolean Values Behave Like Integers

Internally,

```python
True
```

behaves like

```python
1
```

and

```python
False
```

behaves like

```python
0
```

Example

```python
print(True + 4)
```

Output

```text
5
```

because Python performs:

```text
1 + 4
```

---

Another example

```python
print(False + 10)
```

Output

```text
10
```

because

```text
0 + 10
```

equals

```text
10
```

---

You can verify this yourself.

```python
print(int(True))
```

Output

```text
1
```

```python
print(int(False))
```

Output

```text
0
```

# Comment:

# Although Booleans behave like integers internally,

# conceptually they represent logical truth values,

# not numbers.

---

# Special Literal — `None`

## Definition

`None` is a special literal that represents the absence of a value.

It means:

* No value
* Nothing
* Empty reference
* Value not assigned yet

Example:

```python
result = None

print(result)
```

Output

```text
None
```

---

## Why Do We Use `None`?

Sometimes we want to create a variable before we know its value.

Example:

```python
employee_name = None
```

Later,

```python
employee_name = "Alice"
```

The variable now stores a real value.

---

Another example:

```python
selected_file = None
```

Later,

```python
selected_file = "report.pdf"
```

---

## Why Not Use Zero?

Suppose we write:

```python
marks = 0
```

Does it mean

* the student scored zero?

or

* the marks have not been entered yet?

We cannot tell.

Instead,

```python
marks = None
```

clearly means

> "No marks have been assigned yet."

Later,

```python
marks = 87
```

Now the meaning is clear.

---

## Variable Declaration Using `None`

Unlike C or Java, Python does not require variable declarations.

Normally,

you simply write

```python
age = 25
```

Python automatically creates the variable.

However, sometimes you may want to reserve a variable for future use.

Example:

```python
customer = None
```

Later,

```python
customer = "Bharatish"
```

This is a common and Pythonic way to indicate that a variable exists but does not yet have a meaningful value.

# Comment:

# `None` is not the same as:

#

# 0

# False

# ""

# []

#

# All of these are actual values.

# `None` specifically means "no value".

---

# Summary

## Literals

A literal is a fixed value written directly into the source code.

Example:

```python
age = 25

name = "Alice"
```

Here,

* `25`
* `"Alice"`

are literals.

---

## Types of Literals

Python provides four major categories.

### Numeric Literals

* Decimal
* Binary (`0b`)
* Octal (`0o`)
* Hexadecimal (`0x`)
* Floating-point
* Scientific notation (`e`)
* Complex numbers (`j`)

Examples:

```python
100

0b1010

0o12

0xA

3.14

2e5

3+4j
```

---

### String Literals

Python supports:

```python
'Hello'

"Hello"

"""Hello"""

'''Hello'''
```

It also supports:

* Unicode strings
* Raw strings

---

### Boolean Literals

Python has only two Boolean literals.

```python
True

False
```

Internally,

```python
True == 1

False == 0
```

for arithmetic operations.

---

### Special Literal

Python provides one special literal:

```python
None
```

It represents the absence of a value.

---

# Comment

Remember the distinction:

* **Literal** → The actual value written in the program.

```python
age = 25
```

`25` is the literal.

* **Variable** → The name that stores the value.

```python
age
```

is the variable.

* **Object** → The actual data created in memory.

```python
age = 25
```

creates an integer object (`25`) in memory, and the variable `age` refers to it.

This distinction becomes increasingly important as you learn about Python's memory model and object references in later chapters.

---