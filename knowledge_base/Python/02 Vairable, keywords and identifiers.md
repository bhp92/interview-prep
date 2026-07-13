# 04 Python Basics – Variables (Notes)

## Introduction

Variables are one of the most fundamental concepts in programming.

A variable is used when, as a programmer, you **do not know the value in advance**. The actual value will be provided later, usually by the user or during program execution.

### Example Scenario

Suppose you are building a website with millions of users.

When writing the code, you **do not know** which user will log in.

Instead of writing a specific name, you store the future value in a variable.

Similarly, if you write a program to add two numbers, you don't know which numbers the user will enter.

You use variables to represent those future values.

---

## Definition

> A **variable** is a named container that stores a value.

More generally:

> A variable is a placeholder for data that may be assigned now or later during program execution.

---

## Creating Variables in Python

Python creates a variable simply by assigning a value.

### Syntax

```python
variable_name = value
```

### Example

```python
name = "Bharatish"
age = 25
price = 99.99
```

To access the stored value:

```python
print(name)
print(age)
```

---

## Variable Declaration

Unlike languages such as C, C++, or Java:

* You do **not** declare variables before using them.
* You do **not** specify the data type explicitly.

### C Example

```c
int age = 25;
```

### Python Example

```python
age = 25
```

Python automatically creates the variable when it sees the assignment.

---

## Variable Names vs Values

A variable has:

* a **name** (identifier)
* a **value** stored inside it

Example:

```python
city = "Pune"
```

Here:

* Variable name → `city`
* Stored value → `"Pune"`

---

# Dynamic Typing

## Definition

> **Dynamic Typing** means Python automatically determines the data type of a variable from the value assigned to it.

You do **not** tell Python whether a variable is an `int`, `str`, `float`, or `bool`.

Python figures it out automatically.

---

### Example

```python
age = 25
name = "Alice"
price = 19.99
is_admin = True
```

Python automatically treats them as:

* `age` → `int`
* `name` → `str`
* `price` → `float`
* `is_admin` → `bool`

---

## Static Typing vs Dynamic Typing

### Static Typing (C, C++, Java)

You must specify the data type.

```c
int age = 25;
```

---

### Dynamic Typing (Python)

Python determines the type automatically.

```python
age = 25
```

No type declaration is required.

---

# Dynamic Binding

## Definition

> **Dynamic Binding** means a variable can be reassigned to values of different data types during program execution.

The variable itself is **not permanently bound to one type**.

---

### Example

```python
value = "Hello"

print(value)

value = 100

print(value)

value = True

print(value)
```

**Output**

```text
Hello
100
True
```

The same variable stores:

* a string
* an integer
* a boolean

This is perfectly valid in Python.

---

## Static Binding vs Dynamic Binding

### Static Binding (C, C++, Java)

Once a variable is declared with a type, it can only store that type.

Example:

```c
int number = 5;
```

Later:

```c
number = "Hello";   // Error
```

---

### Dynamic Binding (Python)

```python
number = 5

number = "Hello"

number = True
```

All of these assignments are valid.

---

# Multiple Variable Assignment

Python provides several convenient ways to assign variables.

---

## Method 1 – Separate Assignments

```python
a = 5
b = 6
c = 7
```

---

## Method 2 – Multiple Statements on One Line

```python
a = 5; b = 6; c = 7
```

This works, but is generally less readable.

---

## Method 3 – Multiple Assignment

```python
a, b, c = 5, 6, 7
```

This is the preferred Pythonic style.

---

## Method 4 – Assign the Same Value to Multiple Variables

```python
a = b = c = 6
```

All three variables receive the same value.

---

# Summary

## Variables

* Variables store data.
* They represent values that may not be known while writing the program.
* Variables are created using the assignment operator (`=`).
* No separate declaration is required.

---

## Dynamic Typing

* Python automatically determines the variable's data type.
* No explicit type declaration is needed.

---

## Dynamic Binding

* A variable can hold different data types at different times.
* Reassigning a variable with a new type is valid.

---

## Multiple Assignment

Python supports:

```python
a = 5
```

```python
a = 5; b = 6
```

```python
a, b, c = 5, 6, 7
```

```python
a = b = c = 10
```

---

# 05 Python Basics – Keywords and Identifiers (Notes)

## Introduction

When writing Python programs, you create names for variables, functions, classes, and modules.

These names are called **identifiers**.

However, some words are **reserved by Python** for its own syntax.

These reserved words are called **keywords**.

---

## Case Sensitivity

Python is a **case-sensitive** programming language.

This means uppercase and lowercase letters are treated as different.

Example:

```python
name = "Alice"

Name = "Bob"
```

Here, `name` and `Name` are two different variables.

Similarly:

```python
True
```

is valid, but

```python
true
```

is not.

Always pay attention to letter casing.

---

# Keywords

## Definition

> **Keywords** are reserved words that have a predefined meaning in Python.

They are part of Python's syntax and **cannot be used as identifiers**.

Examples include:

* `if`
* `else`
* `for`
* `while`
* `True`
* `False`
* `None`
* `class`
* `def`
* `return`
* `import`

---

## Why Can't We Use Keywords as Variable Names?

Python's interpreter uses keywords to understand the structure of your program.

If keywords were allowed as variable names, the interpreter would become confused.

Example (Invalid):

```python
for = 10
```

This produces a syntax error because `for` is a keyword.

---

## Viewing Python Keywords

Python provides the built-in `keyword` module.

Example:

```python
import keyword

print(keyword.kwlist)
```

This prints the list of Python's reserved keywords.

> **Note:** The number of keywords may change slightly between Python versions.

---

# Identifiers

## Definition

> An **identifier** is a user-defined name given to variables, functions, classes, modules, or objects.

Examples:

```python
age = 25

student_name = "Alice"

calculate_total()

class Employee:
    pass
```

Here:

* `age`
* `student_name`
* `calculate_total`
* `Employee`

are all identifiers.

---

# Rules for Naming Identifiers

## Rule 1 – Must Start with a Letter or Underscore

Valid:

```python
name = "Alice"

_age = 25
```

Invalid:

```python
1name = "Alice"
```

Identifiers cannot begin with a digit.

---

## Rule 2 – Remaining Characters

After the first character, an identifier may contain:

* letters (`A–Z`, `a–z`)
* digits (`0–9`)
* underscore (`_`)

Example:

```python
student1

first_name

employee_2025
```

---

## Rule 3 – No Special Characters

These are invalid:

```python
first-name

salary$

user@home
```

Only the underscore (`_`) is allowed as a special character.

---

## Rule 4 – Cannot Be a Keyword

Invalid:

```python
class = "Python"
```

because `class` is a reserved keyword.

---

## Rule 5 – Case Sensitive

These are different identifiers:

```python
name

Name

NAME
```

Python treats each as a separate name.

---

# Good Naming Practices

Prefer meaningful names.

Good:

```python
student_name

total_marks

is_logged_in
```

Avoid:

```python
x

abc

temp123
```

unless their purpose is obvious.

---

# Summary

## Keywords

* Reserved words with predefined meanings.
* Used by Python's syntax.
* Cannot be used as variable names.
* View them using:

```python
import keyword

print(keyword.kwlist)
```

---

## Identifiers

Identifiers are user-defined names for:

* Variables
* Functions
* Classes
* Modules
* Objects

---

## Identifier Rules

* Must start with a letter or underscore.
* Remaining characters may contain letters, digits, and underscores.
* Cannot contain special characters (except `_`).
* Cannot be a Python keyword.
* Python identifiers are case-sensitive.
