Excellent. Let's continue with **Chapter 09 – Python Basics: Operators**.
# 09 Python Basics – Operators

## Introduction

Programs do not simply store data—they also **perform operations** on that data.

For example:

* Add two numbers
* Compare two values
* Check multiple conditions
* Assign values to variables
* Test whether an item exists in a collection

These operations are performed using **operators**.

---

## Definition

> An **operator** is a symbol or keyword that tells Python to perform a specific operation on one or more operands (values or variables).

Example:

```python
a = 10
b = 5

print(a + b)
```

Here:

* `a` and `b` are **operands**
* `+` is the **operator**

Output:

```text
15
```

---

## Operands

The values on which an operator acts are called **operands**.

Example:

```python
10 + 20
```

Here:

* `10` → Operand
* `20` → Operand
* `+` → Operator

---

# Types of Operators in Python

Python provides the following categories of operators.

| Operator Type           | Purpose                                               |
| ----------------------- | ----------------------------------------------------- |
| Arithmetic              | Mathematical calculations                             |
| Comparison (Relational) | Compare values                                        |
| Logical                 | Combine conditions                                    |
| Bitwise                 | Operate on binary bits                                |
| Assignment              | Assign or update values                               |
| Identity                | Check whether two references point to the same object |
| Membership              | Check whether an item exists in a collection          |

---

# Arithmetic Operators

## Definition

Arithmetic operators perform mathematical operations.

---

| Operator | Meaning          | Example  |
| -------- | ---------------- | -------- |
| `+`      | Addition         | `5 + 2`  |
| `-`      | Subtraction      | `5 - 2`  |
| `*`      | Multiplication   | `5 * 2`  |
| `/`      | Division         | `5 / 2`  |
| `//`     | Floor Division   | `5 // 2` |
| `%`      | Modulus          | `5 % 2`  |
| `**`     | Exponent (Power) | `5 ** 2` |

---

## Addition

```python
x = 10
y = 5

print(x + y)
```

Output

```text
15
```

---

## Subtraction

```python
print(10 - 5)
```

Output

```text
5
```

---

## Multiplication

```python
print(10 * 5)
```

Output

```text
50
```

---

## Division

```python
print(10 / 5)
```

Output

```text
2.0
```

Notice that **division always returns a float**.

```python
print(9 / 2)
```

Output

```text
4.5
```

---

## Floor Division (`//`)

## Definition

> Floor division divides two numbers and returns the integer quotient by discarding the fractional part.

Example:

```python
print(9 // 2)
```

Output

```text
4
```

Another example

```python
print(10 // 3)
```

Output

```text
3
```

---

### Difference Between `/` and `//`

| Expression | Output |
| ---------- | ------ |
| `9 / 2`    | `4.5`  |
| `9 // 2`   | `4`    |

# Comment:

# `//` is called **floor division** because it rounds the result down toward negative infinity.

---

## Modulus (`%`)

## Definition

> The modulus operator returns the **remainder** after division.

Example

```python
print(10 % 3)
```

Output

```text
1
```

because

```text
10 ÷ 3

Quotient = 3

Remainder = 1
```

Another example

```python
print(20 % 5)
```

Output

```text
0
```

---

### Common Uses

Checking even numbers

```python
number = 8

print(number % 2 == 0)
```

Output

```text
True
```

---

Checking odd numbers

```python
number = 7

print(number % 2 != 0)
```

Output

```text
True
```

---

## Exponent (`**`)

## Definition

Raises a number to a power.

Example

```python
print(2 ** 3)
```

Output

```text
8
```

because

```text
2 × 2 × 2
```

Another example

```python
print(10 ** 2)
```

Output

```text
100
```

---

# Summary – Arithmetic Operators

| Operator | Example | Result |
| -------- | ------- | -----: |
| `+`      | `5+2`   |      7 |
| `-`      | `5-2`   |      3 |
| `*`      | `5*2`   |     10 |
| `/`      | `5/2`   |    2.5 |
| `//`     | `5//2`  |      2 |
| `%`      | `5%2`   |      1 |
| `**`     | `5**2`  |     25 |

---

# Comparison (Relational) Operators

## Definition

Comparison operators compare two values and return a Boolean result.

The result is always:

```python
True
```

or

```python
False
```

---

| Operator | Meaning                  |
| -------- | ------------------------ |
| `==`     | Equal to                 |
| `!=`     | Not equal to             |
| `>`      | Greater than             |
| `<`      | Less than                |
| `>=`     | Greater than or equal to |
| `<=`     | Less than or equal to    |

---

## Equal To (`==`)

```python
print(5 == 5)
```

Output

```text
True
```

---

```python
print(5 == 10)
```

Output

```text
False
```

---

## Not Equal (`!=`)

```python
print(5 != 10)
```

Output

```text
True
```

---

```python
print(5 != 5)
```

Output

```text
False
```

---

## Greater Than (`>`)

```python
print(10 > 5)
```

Output

```text
True
```

---

## Less Than (`<`)

```python
print(10 < 5)
```

Output

```text
False
```

---

## Greater Than or Equal (`>=`)

```python
print(10 >= 10)
```

Output

```text
True
```

---

## Less Than or Equal (`<=`)

```python
print(10 <= 8)
```

Output

```text
False
```

---

## Why Are Comparison Operators Useful?

Comparison operators are used in:

* `if` statements
* loops
* searching
* validation
* filtering

Example

```python
age = 18

print(age >= 18)
```

Output

```text
True
```

---

# Logical Operators

## Definition

Logical operators combine multiple conditions.

Python provides three logical operators.

| Operator | Meaning                             |
| -------- | ----------------------------------- |
| `and`    | Both conditions must be True        |
| `or`     | At least one condition must be True |
| `not`    | Reverses a Boolean value            |

---

## Logical AND

Returns `True` only when **both** conditions are True.

Example

```python
print(True and True)
```

Output

```text
True
```

---

```python
print(True and False)
```

Output

```text
False
```

---

Example

```python
age = 20

citizen = True

print(age >= 18 and citizen)
```

Output

```text
True
```

---

## Logical OR

Returns True if **at least one** condition is True.

Example

```python
print(True or False)
```

Output

```text
True
```

---

```python
print(False or False)
```

Output

```text
False
```

---

Example

```python
is_admin = False

is_owner = True

print(is_admin or is_owner)
```

Output

```text
True
```

---

## Logical NOT

Reverses a Boolean value.

Example

```python
print(not True)
```

Output

```text
False
```

---

```python
print(not False)
```

Output

```text
True
```

---

Example

```python
logged_in = False

print(not logged_in)
```

Output

```text
True
```

---

## Truth Tables

### AND

| A     | B     | A and B |
| ----- | ----- | ------- |
| False | False | False   |
| False | True  | False   |
| True  | False | False   |
| True  | True  | True    |

---

### OR

| A     | B     | A or B |
| ----- | ----- | ------ |
| False | False | False  |
| False | True  | True   |
| True  | False | True   |
| True  | True  | True   |

---

### NOT

| A     | not A |
| ----- | ----- |
| True  | False |
| False | True  |

---

# Comment

The transcript introduces these operators before `if` statements because they are commonly used together.

Example:

```python
if age >= 18 and citizen:
    print("Eligible")
```

We'll study this in detail in **Chapter 11 – Decision Making**.

---

*(To keep the handbook complete and avoid truncation, I'll continue in the next response with **Bitwise Operators**, **Assignment Operators**, **Identity Operators (`is`, `is not`)**, **Membership Operators (`in`, `not in`)**, **Operator Precedence**, and **Common Mistakes**. I won't omit any concepts from the transcript.)*

Excellent. Let's continue and complete the remainder of **Chapter 09 – Operators**.

---

# Bitwise Operators

## Definition

> **Bitwise operators** perform operations on the binary (bit-level) representation of integers.

Unlike arithmetic operators, bitwise operators work directly on the **bits** of a number.

For example,

```python
5
```

is stored internally as:

```text
00000101
```

and

```python
3
```

is stored as:

```text
00000011
```

A bitwise operator compares these bits one by one.

# Comment:

# Bitwise operators are commonly used in embedded systems, networking,

# image processing, cryptography, operating systems, and hardware programming.

---

# Binary Representation

Before learning bitwise operators, let's understand how numbers are represented.

Example:

```python
5
```

Binary representation:

```text
00000101
```

Example:

```python
3
```

Binary representation:

```text
00000011
```

Python performs bitwise operations using these binary values.

---

# Bitwise AND (`&`)

## Definition

> The **Bitwise AND** operator compares each corresponding bit.

Rule:

```text
1 & 1 = 1

1 & 0 = 0

0 & 1 = 0

0 & 0 = 0
```

Example:

```python
print(5 & 3)
```

Binary calculation:

```text
5  → 00000101

3  → 00000011

----------------

    00000001
```

Output

```text
1
```

---

Another example

```python
print(6 & 2)
```

Binary:

```text
6 → 110

2 → 010

----------

    010
```

Output

```text
2
```

---

# Bitwise OR (`|`)

## Definition

Returns 1 if either bit is 1.

Rule:

```text
1 | 1 = 1

1 | 0 = 1

0 | 1 = 1

0 | 0 = 0
```

Example

```python
print(5 | 3)
```

Binary:

```text
5 → 101

3 → 011

---------

    111
```

Output

```text
7
```

---

# Bitwise XOR (`^`)

## Definition

Returns 1 only if the bits are different.

Rule:

```text
1 ^ 1 = 0

0 ^ 0 = 0

1 ^ 0 = 1

0 ^ 1 = 1
```

Example

```python
print(5 ^ 3)
```

Binary

```text
101

011

------

110
```

Output

```text
6
```

---

# Bitwise NOT (`~`)

Inverts every bit.

Example

```python
print(~5)
```

Output

```text
-6
```

# Comment:

# The output may look surprising because Python stores negative

# integers using two's complement representation.

# You'll study this in more detail when learning computer architecture.

---

# Left Shift (`<<`)

Moves all bits to the left.

Example

```python
print(5 << 1)
```

Binary

```text
5

00000101

↓

00001010
```

Output

```text
10
```

---

Another example

```python
print(5 << 2)
```

Output

```text
20
```

---

# Right Shift (`>>`)

Moves bits to the right.

Example

```python
print(8 >> 1)
```

Binary

```text
1000

↓

0100
```

Output

```text
4
```

---

Another example

```python
print(8 >> 2)
```

Output

```text
2
```

---

# Where Are Bitwise Operators Used?

Most application developers rarely use bitwise operators.

However, they are common in:

* Device drivers
* Operating systems
* Embedded programming
* Raspberry Pi
* Robotics
* Image processing
* Network protocols
* Compression algorithms
* Encryption

The transcript specifically mentions **image processing**.

Images are stored as numbers (pixel values), and many image filters internally use combinations of bitwise operations.

# Comment:

# Don't worry if bitwise operators feel difficult.

# Even experienced Python developers don't use them every day.

---

# Assignment Operators

## Definition

Assignment operators assign values to variables.

The simplest assignment operator is:

```python
=
```

Example

```python
x = 10
```

---

# Basic Assignment

```python
x = 5

print(x)
```

Output

```text
5
```

---

# Compound Assignment Operators

Python allows combining an arithmetic operation with assignment.

---

## Addition Assignment (`+=`)

```python
x = 5

x += 3

print(x)
```

Output

```text
8
```

Equivalent to

```python
x = x + 3
```

---

## Subtraction Assignment (`-=`)

```python
x = 10

x -= 4

print(x)
```

Output

```text
6
```

Equivalent to

```python
x = x - 4
```

---

## Multiplication Assignment (`*=`)

```python
x = 5

x *= 2

print(x)
```

Output

```text
10
```

---

## Division Assignment (`/=`)

```python
x = 10

x /= 2

print(x)
```

Output

```text
5.0
```

---

## Floor Division Assignment (`//=`)

```python
x = 9

x //= 2

print(x)
```

Output

```text
4
```

---

## Modulus Assignment (`%=`)

```python
x = 10

x %= 3

print(x)
```

Output

```text
1
```

---

## Exponent Assignment (`**=`)

```python
x = 2

x **= 3

print(x)
```

Output

```text
8
```

---

# Python Does NOT Have `++`

Unlike C, C++, or Java,

Python **does not support**

```python
x++
```

or

```python
++x
```

These are invalid.

Instead,

write

```python
x += 1
```

or

```python
x = x + 1
```

# Comment:

# Many beginners coming from C/C++ look for `++`.

# Python intentionally omits increment and decrement operators

# to keep the language simpler and more readable.

---

# Identity Operators

## Definition

Identity operators check whether **two variables refer to the same object in memory**.

They do **not** compare values.

Python provides:

| Operator | Meaning           |
| -------- | ----------------- |
| `is`     | Same object       |
| `is not` | Different objects |

---

## `is`

Example

```python
a = 10
b = a

print(a is b)
```

Output

```text
True
```

Both variables refer to the same object.

---

Example

```python
a = [1, 2, 3]

b = a

print(a is b)
```

Output

```text
True
```

---

Now compare

```python
a = [1, 2, 3]

b = [1, 2, 3]

print(a is b)
```

Output

```text
False
```

Although both lists contain identical values,

they are different objects.

---

# `==` vs `is`

This is one of the most important distinctions in Python.

Example

```python
a = [1, 2, 3]

b = [1, 2, 3]
```

```python
print(a == b)
```

Output

```text
True
```

because the values are equal.

However,

```python
print(a is b)
```

Output

```text
False
```

because they are different objects.

---

# Comment

Remember:

```text
==

↓

Same VALUE

----------------------

is

↓

Same OBJECT
```

This is more precise than the transcript and avoids a common beginner misconception.

---

# `is not`

Example

```python
a = [1]

b = [1]

print(a is not b)
```

Output

```text
True
```

because they are different objects.

---

# Membership Operators

## Definition

Membership operators check whether an element exists inside another object.

Python provides:

| Operator | Meaning     |
| -------- | ----------- |
| `in`     | Present     |
| `not in` | Not present |

---

# Using `in` with Strings

Example

```python
city = "Pune"

print("Pu" in city)
```

Output

```text
True
```

---

```python
print("Delhi" in city)
```

Output

```text
False
```

---

# Using `in` with Lists

```python
numbers = [10, 20, 30]

print(20 in numbers)
```

Output

```text
True
```

---

```python
print(40 in numbers)
```

Output

```text
False
```

---

# Using `in` with Tuples

```python
colors = ("red", "green", "blue")

print("green" in colors)
```

Output

```text
True
```

---

# Using `in` with Sets

```python
numbers = {1, 2, 3}

print(2 in numbers)
```

Output

```text
True
```

---

# Using `in` with Dictionaries

For dictionaries,

membership checks **keys**, not values.

Example

```python
student = {
    "name": "Alice",
    "age": 20
}

print("name" in student)
```

Output

```text
True
```

---

```python
print("Alice" in student)
```

Output

```text
False
```

because `"Alice"` is a value, not a key.

---

# `not in`

Example

```python
numbers = [1, 2, 3]

print(5 not in numbers)
```

Output

```text
True
```

---

# Operator Precedence

Sometimes multiple operators appear in the same expression.

Python follows precedence rules.

Example

```python
print(2 + 3 * 4)
```

Output

```text
14
```

not

```text
20
```

because multiplication happens first.

---

## Common Operator Precedence

Highest → Lowest

| Priority            | Operators                |
| ------------------- | ------------------------ |
| `()`                | Parentheses              |
| `**`                | Exponent                 |
| `+x`, `-x`, `~x`    | Unary operators          |
| `*`, `/`, `//`, `%` | Multiplication, Division |
| `+`, `-`            | Addition, Subtraction    |
| `<<`, `>>`          | Shift                    |
| `&`                 | Bitwise AND              |
| `^`                 | Bitwise XOR              |
| `\|`                | Bitwise OR               |
| Comparison          | `==`, `!=`, `<`, `>`     |
| `not`               | Logical NOT              |
| `and`               | Logical AND              |
| `or`                | Logical OR               |

---

# Best Practices

* Use parentheses to improve readability.

Instead of

```python
result = a + b * c
```

write

```python
result = a + (b * c)
```

if you want to emphasize the intended order.

---

* Use `==` to compare values.

* Use `is` only when checking object identity (especially `None`).

Example

```python
if value is None:
    ...
```

instead of

```python
if value == None:
    ...
```

---

# Summary

Python provides seven major categories of operators:

* Arithmetic
* Comparison (Relational)
* Logical
* Bitwise
* Assignment
* Identity
* Membership

Each category serves a different purpose, and together they form the foundation of expressions, conditions, and calculations in Python.

---

**Next Chapter:** **10 Python Basics – Indentation**.

This chapter will explain **why Python does not use braces (`{}`)**, **how indentation defines code blocks**, **PEP 8 recommendations**, **tabs vs spaces**, **nested blocks**, and **common beginner mistakes**, while preserving all the concepts from the transcript and adding the missing technical details.

