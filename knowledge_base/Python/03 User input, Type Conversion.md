# 06 Python Basics – User Input

## Introduction

Until now, we have assigned values directly in our programs.

Example:

```python
name = "Bharatish"
age = 25
```

However, most real-world programs do **not** know these values in advance.

Instead, they ask the **user** to provide them during program execution.

Examples:

* Login forms
* Search boxes
* ATM machines
* Banking applications
* Shopping websites
* Calculator applications

These applications need **user input** to perform their tasks.

---

## Static Software vs Dynamic Software

Software can be broadly categorized into two types.

### Static Software

Static software mainly displays information to the user.

Communication is mostly **one-way**.

Examples:

* Calendar
* Clock
* Blog websites
* Government information websites
* College notice boards

The software provides information, but the user usually does not interact with it.

---

### Dynamic Software

Dynamic software allows **two-way communication**.

The user provides information, and the software responds accordingly.

Examples:

* YouTube (Search, Comments, Likes)
* WhatsApp
* Amazon
* Swiggy
* Zomato
* Online Banking
* Chat Applications

Nearly all modern applications are dynamic because they rely on user input.

---

## Why User Input is Important

Without user input, many applications cannot function.

Imagine writing a calculator.

While writing the code, you **do not know** which numbers the user will enter.

Instead, your program asks the user for values.

This is why every programming language provides a mechanism to receive user input.

Examples:

| Language | User Input              |
| -------- | ----------------------- |
| C        | `scanf()`               |
| C++      | `cin`                   |
| Java     | `Scanner` / `System.in` |
| Python   | `input()`               |

---

# The `input()` Function

## Definition

> `input()` is a built-in Python function used to receive input from the user during program execution.

### Syntax

```python
input()
```

Example:

```python
input()
```

When executed, Python waits until the user types something and presses **Enter**.

---

## Storing User Input

Usually, we store the entered value in a variable.

Example:

```python
name = input()
```

Now whatever the user types is stored in `name`.

---

## Providing a Prompt

Calling `input()` without any message can confuse the user.

Example:

```python
name = input()
```

The user sees an empty input prompt and may not know what to enter.

Instead, provide a helpful message.

Syntax:

```python
input("Prompt Message")
```

Example:

```python
name = input("Enter your name: ")
```

Output:

```text
Enter your name: Bharatish
```

Now the user clearly knows what information is expected.

> **Good Practice:** Always provide a descriptive prompt when using `input()`.

```python
age = input("Enter your age: ")

city = input("Enter your city: ")

salary = input("Enter your salary: ")
```

# Comment:

# Good prompts improve the user experience and make programs easier to use.

---

# Example – Reading Two Numbers

```python
first_number = input("Enter the first number: ")

second_number = input("Enter the second number: ")

print(first_number)

print(second_number)
```

Sample Output:

```text
Enter the first number: 56
Enter the second number: 76

56
76
```

---

# Important Property of `input()`

## Definition

> **The `input()` function always returns the user's input as a string (`str`).**

This is one of the most important facts to remember.

Example:

```python
number = input("Enter a number: ")

print(type(number))
```

Output:

```text
<class 'str'>
```

Even if the user enters:

```text
25
```

Python stores:

```python
"25"
```

which is a string, **not** an integer.

---

## Why Does `input()` Always Return a String?

Strings are a **universal representation** of user input.

A string can represent:

* Numbers
* Names
* Email addresses
* Phone numbers
* Addresses
* Sentences

If Python always assumed the input was an integer, it would fail whenever the user entered text.

Therefore, Python safely returns everything as a string and lets the programmer convert it later if needed.

# Comment:

# Think of `input()` as reading keyboard characters. Everything typed on a keyboard initially arrives as text.

---

# Demonstrating the Problem

Suppose we write:

```python
first_number = input("Enter first number: ")

second_number = input("Enter second number: ")

result = first_number + second_number

print(result)
```

Input:

```text
56
76
```

Output:

```text
5676
```

Instead of mathematical addition, Python joins the two strings together.

This operation is called **string concatenation**.

---

# Checking the Data Type

Python provides the built-in `type()` function.

## Definition

> `type()` returns the data type of an object.

Syntax:

```python
type(object)
```

Examples:

```python
print(type(5))
```

Output:

```text
<class 'int'>
```

```python
print(type(4.5))
```

Output:

```text
<class 'float'>
```

```python
print(type("Hello"))
```

Output:

```text
<class 'str'>
```

```python
print(type(True))
```

Output:

```text
<class 'bool'>
```

```python
print(type(2 + 3j))
```

Output:

```text
<class 'complex'>
```

Lists can also be checked:

```python
print(type([1, 2, 3]))
```

Output:

```text
<class 'list'>
```

---

# 07 Python Basics – Type Conversion

## Introduction

Since `input()` always returns a string, we often need to convert that string into another data type before performing operations.

This process is called **Type Conversion**.

---

## Definition

> **Type Conversion** is the process of converting one data type into another compatible data type.

Examples:

* String → Integer
* Integer → Float
* Float → Integer
* Integer → Complex

A conversion is only possible if the value is compatible with the target type.

For example:

```python
int("123")
```

works because `"123"` represents a valid integer.

However:

```python
int("Hello")
```

produces an error because `"Hello"` is not a valid integer.

---

# Types of Type Conversion

Python supports two kinds of type conversion.

## 1. Implicit Type Conversion

## Definition

> **Implicit Type Conversion** happens automatically when Python safely converts one compatible type into another.

The programmer does not explicitly request the conversion.

Example:

```python
print(4 + 5.5)
```

Output:

```text
9.5
```

Python automatically converts:

```python
4
```

into

```python
4.0
```

before performing the addition.

Another example:

```python
print(5 + (6 + 2j))
```

Python automatically converts the integer to a compatible type before performing the operation.

# Comment:

# Python performs implicit conversion only when it is safe and unambiguous.

---

## 2. Explicit Type Conversion

## Definition

> **Explicit Type Conversion** is when the programmer manually converts a value from one data type to another.

Python provides built-in conversion functions for this purpose.

---

# Integer Conversion

```python
int(4.5)
```

Output:

```text
4
```

```python
int("25")
```

Output:

```text
25
```

Invalid:

```python
int("Hello")
```

Output:

```text
ValueError
```

---

# Float Conversion

```python
float(4)
```

Output:

```text
4.0
```

```python
float("3.14")
```

Output:

```text
3.14
```

---

# String Conversion

```python
str(100)
```

Output:

```text
'100'
```

---

# Boolean Conversion

```python
bool(1)
```

Output:

```text
True
```

```python
bool(0)
```

Output:

```text
False
```

---

# Complex Conversion

```python
complex(4)
```

Output:

```text
(4+0j)
```

---

# Other Conversion Functions

Python also provides conversion functions for many built-in data types.

Examples:

```python
list()
tuple()
set()
dict()
```

These convert compatible values into their respective data types.

# Comment:

# Not every conversion is valid. The value must be compatible with the target type.

---

# Type Conversion is Not Permanent

Type conversion creates a **new object** of the requested type.

It does **not** modify the original value unless you assign the converted value back to the variable.

Example:

```python
x = 4.5

print(int(x))

print(x)
```

Output:

```text
4
4.5
```

The original value of `x` is still `4.5`.

To permanently use the converted value:

```python
x = int(x)

print(x)
```

Output:

```text
4
```

# Comment:

# In Python, variables hold references to objects. `int(x)` creates a new integer object; it does not change the original float object.

---

# Solving the Input Problem

Incorrect:

```python
first_number = input("Enter first number: ")

second_number = input("Enter second number: ")

result = first_number + second_number

print(result)
```

Output:

```text
5676
```

Correct:

```python
first_number = int(input("Enter first number: "))

second_number = int(input("Enter second number: "))

result = first_number + second_number

print(result)
```

Output:

```text
132
```

This works because the input strings are converted to integers before addition.

---

# Best Practice

Convert user input **immediately after reading it** if you know the expected type.

Instead of:

```python
first_number = input("Enter first number: ")

second_number = input("Enter second number: ")

result = int(first_number) + int(second_number)
```

Prefer:

```python
first_number = int(input("Enter first number: "))

second_number = int(input("Enter second number: "))

result = first_number + second_number
```

This keeps the rest of the program working with the correct data type and avoids repeated conversions.

---

# Summary

## User Input

* `input()` is a built-in function used to receive user input.
* Always provide a meaningful prompt.
* `input()` always returns a **string (`str`)**.
* Use `type()` to check the data type of a value.

---

## Type Conversion

* Converts one compatible data type into another.
* Two types:

  * Implicit Type Conversion (automatic)
  * Explicit Type Conversion (manual)
* Common conversion functions:

  * `int()`
  * `float()`
  * `str()`
  * `bool()`
  * `complex()`
  * `list()`
  * `tuple()`
  * `set()`
  * `dict()`
* Type conversion is **not permanent** unless the converted value is assigned back to the variable.
* Convert user input immediately after reading it when you know the expected data type.

# Comment:

# One subtle but important distinction:

# Dynamic Typing (Chapter 04) is about Python deciding the type of a variable automatically.

# Type Conversion (Chapter 07) is about changing a value from one type to another, either automatically (implicit) or manually (explicit).
