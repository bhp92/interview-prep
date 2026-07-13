# 01 Python Basics – `print()` Function (Notes)

## Introduction

* Like every programming language, we start with printing output.
* Every programming language has a built-in function to print something.

  * C → `printf()`
  * C++ → `cout`
  * Java → `System.out`
  * Python → `print()`

---

- `print()` Function

**Definition**

> `print()` is a built-in function used to print anything on the screen.

* It is built into Python.
* No need to import any library.
* No need to write a `main()` function.
* Simply call `print()`.

### Example

```python
print("Hello World")
```

**Output**

```text
Hello World
```

**Note**

Unlike C/C++, Python doesn't require:

* importing any library
* writing a `main()` function

Just one line is enough.

---

## Printing Different Data Types

You are **not limited to strings**.

You can print:

* Strings
* Numbers
* Booleans
* Other data types

### Examples

```python
print("Hello World")
print(10)
print(10.5)
print(True)
```

Everything prints exactly like other programming languages.

---

## Printing Multiple Values

One of the powerful features of Python's `print()` function is that **multiple values can be printed together**.

Separate them using commas.

### Example

```python
print("India", "Pakistan", "Nepal", "Sri Lanka")
```

**Output**

```text
India Pakistan Nepal Sri Lanka
```

---

You can even mix different data types.

### Example

```python
print("India", 10, True)
```

**Output**

```text
India 10 True
```

---

There is **no practical limit** like:

* only 4 values
* only 10 values

`print()` is flexible.

You can pass as many values as you want using commas.

---

## Other Parameters

The `print()` function has some more parameters.

Two important ones mentioned are:

* `file`
* `flush`

These are related to **File Handling**.

The instructor mentions that these will be covered later when studying File Handling.

---

# 02 Python Basics – Python Data Types (Notes)

## Introduction

In Python, all data types can be divided into **three categories**:

1. **Basic Types**
2. **Container Types**
3. **User-defined Types**

```
Data Types
│
├── Basic Types
├── Container Types
└── User-defined Types
```

---

## 1. Basic Types

These are the data types you commonly see in most programming languages.

They include:

* Integer (`int`)
* Float (`float`)
* Complex (`complex`)
* Boolean (`bool`)
* String (`str`)

---

## 2. Container Types

Container types allow you to store **multiple data items inside a single container**.

Python provides four major container types:

* List
* Tuple
* Set
* Dictionary

---

## 3. User-defined Types

User-defined types are learned when studying **Object-Oriented Programming (OOP)**.

They involve:

* Classes
* Objects

This topic is **not covered now** and will be studied later.

---

## Basic Types

### Integer (`int`)

An integer represents a whole number.

Example

```python
a = 10
print(a)
```

---

### Integer Range

One good thing about Python is that integers have **very large support**.

Practically, there is **no small fixed limit** like many other programming languages.

The instructor experimented with extremely large integers and Python was able to handle them.

Example:

```python
num = 999999999999999999999999999999999999999999999999999999999999
print(num)
```

Python can directly create and print extremely large integers.

The instructor mentions that the range is extremely large and experimented with numbers around powers such as:

* around `10^307`
* `10^308`
* `10^309`

and observed how Python handled them during experimentation.

For all practical purposes:

* You can assume Python integers can store **very large numbers**.
* You are unlikely to reach this limit in normal programming.

Example use case mentioned:

* Storing the number of views on the most popular YouTube video would be trivial for Python.

---

### Float (`float`)

A float represents decimal numbers.

Example

```python
price = 12.75
print(price)
```

Float supports decimal values.

The instructor also mentions experimenting with extremely large floating-point numbers and observing values like infinity (`inf`) at very large magnitudes, while normal practical numbers display correctly.

For all practical purposes:

* Python's `float` is sufficiently large.
* You are very unlikely to need numbers larger than what it supports.

---

### Boolean (`bool`)

Boolean has only two values:

* `True`
* `False`

Example

```python
print(True)
print(False)
```

---

### Complex Numbers (`complex`)

Python has built-in support for **complex numbers**.

This is something the instructor mentions is not commonly seen in many programming languages.

If you're working in domains involving mathematics, you may need complex numbers.

Example

```python
z = 3 + 4j
print(z)
```

The instructor mentions:

* Complex numbers are usually useful in mathematical applications.
* Personally, they haven't used this type very often outside such domains.

---

### String (`str`)

Strings are one of the most useful data types.

Whenever you're developing applications for users, strings are used extensively.

Strings can be written in multiple ways.

---

#### Using Single Quotes

```python
name = 'Python'
```

---

#### Using Double Quotes

```python
name = "Python"
```

---

#### Using Triple Quotes

```python
text = """Python"""
```

---

All three are valid.

The instructor mentions:

> Which one to use and when will be discussed later when studying strings.

At this point:

* Any of these methods are acceptable.
* There is no error.

---

## Container Types

The instructor mentions that every container type will later be studied **in great detail**, with multiple dedicated videos.

For now, the goal is only to understand **how they look**.

---

### List

A list is similar to an **array** in many other programming languages.

In Python it is called a **List**.

Lists use square brackets.

Example

```python
numbers = [10, 20, 30, 40]
```

---

### Tuple

A tuple looks very similar to a list.

The major visible difference is the brackets used.

Tuple uses parentheses.

Example

```python
numbers = (10, 20, 30, 40)
```

---

### Difference Mentioned

List

Uses:

```python
[]
```

Tuple

Uses:

```python
()
```

The instructor says:

This is only the biggest **visible difference** for now.

There are many more differences, which will be studied later.

---

### Set

A set is the same concept learned in high-school mathematics.

Examples:

* Set
* Union
* Intersection

Python provides this concept as a built-in data type.

Sets use curly braces.

Example

```python
numbers = {10, 20, 30, 40}
```

---

### Dictionary (`dict`)

The instructor mentions that dictionaries are:

* Wonderful
* Very useful
* Extremely fast

They will be studied in detail later.

---

### Dictionary stores Key–Value pairs

Example

```python
student = {
    "name": "Nitesh",
    "age": 30,
    "gender": "Male"
}
```

The dictionary above contains three key–value pairs:

First pair

```
Key   -> "name"
Value -> "Nitesh"
```

Second pair

```
Key   -> "age"
Value -> 30
```

Third pair

```
Key   -> "gender"
Value -> "Male"
```

The instructor notes that dictionaries are used extensively in Python programming.

---

# Summary

## Python Data Types

### Basic Types

* Integer (`int`)
* Float (`float`)
* Complex (`complex`)
* Boolean (`bool`)
* String (`str`)

---

### Container Types

* List
* Tuple
* Set
* Dictionary

---

### User-defined Types

Will be studied later with **Object-Oriented Programming (OOP)**.

Topics include:

* Classes
* Objects

---

Here is a concise section you can append to your existing notes, keeping the same style and structure.

---

# 03 Python Basics – Comments (Notes)

## Introduction

Comments are **non-executable lines** in a Python program.

They are written for humans to read and are **ignored by the Python interpreter**.

> **Definition**
>
> A **comment** is text in the source code that is **not executed** by the Python interpreter.

---

## Why Do We Use Comments?

Comments improve the **readability** and **maintainability** of code.

There are two common reasons for writing comments.

### 1. Helping Other Programmers

Software is usually developed by a **team**.

If another programmer has to read or modify your code, comments help them understand:

* what the code does
* why a particular logic was used

Without comments, understanding complex logic can take much longer.

---

### 2. Helping Yourself

After several months, you may forget why you wrote a particular piece of code.

Comments act as **documentation**, making it easier to understand your own code later.

---

## Single-Line Comments

In Python, a single-line comment begins with the **hash (`#`)** symbol.

Everything after `#` on that line is ignored by the interpreter.

### Example

```python
# This is a comment

print("Hello World")
```

**Output**

```text
Hello World
```

The comment is ignored during execution.

---

Another example:

```python
print(10)

# Print the user's age
print(25)
```

Only the `print()` statements execute.

---

## Multi-Line Comments

Python **does not have a special syntax for multi-line comments**.

Instead, write a `#` at the beginning of **each line**.

### Example

```python
# This program
# calculates the total
# price of items.

print("Shopping Cart")
```

---

## Important Note

Some editors and IDEs provide shortcuts to comment multiple lines at once, but internally they simply add `#` to each selected line.

This is an editor feature, **not a Python language feature**.

---

# Summary

## Comments

* Comments are **ignored by the Python interpreter**.
* They make code **easier to read and understand**.
* They help:

  * other programmers working on the same project
  * your future self when revisiting the code
* Single-line comments begin with `#`.
* Python has **no dedicated multi-line comment syntax**; use `#` on every line.