Excellent. This is the last chapter from your transcripts. I'll make it significantly stronger than the transcript while preserving everything important.

---

# 11 Python Basics – Decision Making (`if`, `elif`, `else`)

## Introduction

Until now, every Python program we have written executes **from top to bottom**, one statement after another.

Example:

```python
print("Line 1")
print("Line 2")
print("Line 3")
```

Output

```text
Line 1
Line 2
Line 3
```

The execution always follows the same path.

However, real-world programs often need to **make decisions**.

Examples:

* Can a user log in?
* Is a student eligible to take an exam?
* Is a customer old enough to vote?
* Does a password match?
* Does a file exist?
* Is the bank balance sufficient?

In these situations, the program must choose between different paths.

This process is called **decision making** or **branching**.

---

# What is Branching?

## Definition

> **Branching** is the process of choosing one execution path from multiple possible paths based on a condition.

Example:

```text
           Age >= 18 ?

             True
               │
               ▼
          Allow Voting

             False
               │
               ▼
         Not Eligible
```

Instead of executing every statement, the program decides **which path** to follow.

---

# Decision Making in Python

Python provides three main statements for decision making:

* `if`
* `elif`
* `else`

These statements evaluate **conditions**.

A condition always evaluates to either:

```python
True
```

or

```python
False
```

---

# The `if` Statement

## Definition

> The `if` statement executes a block of code **only if** its condition evaluates to `True`.

---

## Syntax

```python
if condition:
    statement
```

---

### Flow

```text
Condition

    │
    ▼

Is it True?

 ┌───────────┐
 │           │
 │  True     │────► Execute block
 │
 │
 │ False
 │
 ▼

Skip block
```

---

## Example 1

```python
age = 20

if age >= 18:
    print("Adult")
```

Output

```text
Adult
```

---

## Example 2

```python
age = 15

if age >= 18:
    print("Adult")
```

Output

```text
(no output)
```

The condition is `False`, so Python skips the block.

---

# How `if` Works

Python evaluates the condition.

Example

```python
age >= 18
```

Suppose

```python
age = 20
```

Python evaluates

```python
20 >= 18
```

which becomes

```python
True
```

Therefore,

```python
print("Adult")
```

executes.

---

# Conditions

A condition is any expression that evaluates to

```python
True
```

or

```python
False
```

Examples:

```python
10 > 5
```

```python
age >= 18
```

```python
marks == 100
```

```python
name == "Alice"
```

```python
is_logged_in
```

---

# Using Logical Operators

Conditions can be combined using

* `and`
* `or`
* `not`

Example

```python
age = 20
citizen = True

if age >= 18 and citizen:
    print("Eligible")
```

Output

```text
Eligible
```

---

Another example

```python
if is_admin or is_owner:
    print("Access Granted")
```

---

# The `else` Statement

## Definition

> The `else` block executes when the `if` condition is `False`.

---

## Syntax

```python
if condition:
    statement
else:
    statement
```

---

### Flow

```text
Condition

     │
     ▼

 True ?

 ┌─────────┐
 │         │
 │ True    │────► if block
 │
 │ False
 │
 ▼
else block
```

---

## Example

```python
age = 15

if age >= 18:
    print("Adult")
else:
    print("Minor")
```

Output

```text
Minor
```

---

Another example

```python
marks = 75

if marks >= 40:
    print("Pass")
else:
    print("Fail")
```

---

# Login Example

Suppose the correct credentials are

```python
correct_email = "campusx@gmail.com"
correct_password = "1234"
```

Ask the user for input.

```python
email = input("Enter Email: ")
password = input("Enter Password: ")
```

Check both conditions.

```python
if email == correct_email and password == correct_password:
    print("Welcome")
else:
    print("Incorrect Credentials")
```

This is exactly the example discussed in the transcript.

---

# Why Use `and`?

Logging in requires

* Correct email
* Correct password

Both conditions must be true.

Therefore,

```python
if email == correct_email and password == correct_password:
```

uses the logical **AND** operator.

---

# The `elif` Statement

Sometimes there are more than two possibilities.

Example:

Suppose we want to classify marks.

```text
Marks ≥ 90

Excellent

Marks ≥ 75

Good

Marks ≥ 40

Pass

Otherwise

Fail
```

Using only `if` and `else` becomes difficult.

Python provides

```python
elif
```

which means

> **Else If**

---

## Syntax

```python
if condition1:
    ...
elif condition2:
    ...
elif condition3:
    ...
else:
    ...
```

---

## Example

```python
marks = 82

if marks >= 90:
    print("Excellent")

elif marks >= 75:
    print("Good")

elif marks >= 40:
    print("Pass")

else:
    print("Fail")
```

Output

```text
Good
```

---

# Order Matters

Python checks conditions from top to bottom.

Once a condition becomes `True`,

Python ignores the remaining conditions.

Example

```python
marks = 95

if marks >= 40:
    print("Pass")

elif marks >= 75:
    print("Good")

elif marks >= 90:
    print("Excellent")
```

Output

```text
Pass
```

This is incorrect logic because the first condition is already true.

Correct version

```python
if marks >= 90:
    print("Excellent")

elif marks >= 75:
    print("Good")

elif marks >= 40:
    print("Pass")

else:
    print("Fail")
```

Always write **more specific conditions first**.

---

# Login Example with `elif`

The transcript introduces a better login system.

Scenario

* Email correct
* Password incorrect

Instead of immediately rejecting the user,

give them another chance.

```python
correct_email = "campusx@gmail.com"
correct_password = "1234"

email = input("Enter Email: ")
password = input("Enter Password: ")

if email == correct_email and password == correct_password:
    print("Welcome")

elif email == correct_email:
    print("Incorrect Password")

    password = input("Enter Password Again: ")

    if password == correct_password:
        print("Welcome")
    else:
        print("Incorrect Password")

else:
    print("Incorrect Email")
```

This demonstrates

* `if`
* `elif`
* nested `if`

all together.

---

# Nested `if`

## Definition

> A **nested `if`** is an `if` statement inside another `if` statement.

Example

```python
age = 25

if age >= 18:

    if age >= 21:
        print("Can Enter")

    print("Adult")
```

---

Flow

```text
if

│

├── if

│      │

│      └── Code

│

└── More Code
```

---

# Email Format Validation

The transcript also introduces another useful example.

Before checking the password,

verify whether the email contains

```text
@
```

Example

```python
email = input("Enter Email: ")

if "@" not in email:
    print("Invalid Email Format")

else:
    password = input("Enter Password: ")
```

Notice the use of

```python
in
```

which we learned in the previous chapter.

---

# Multiple Levels of Decision Making

Programs can contain many levels.

Example

```python
if condition1:

    if condition2:

        if condition3:

            print("Success")
```

Each indentation level creates another decision level.

---

# Common Beginner Mistakes

## Mistake 1

Using

```python
=
```

instead of

```python
==
```

Incorrect

```python
if age = 18:
```

Correct

```python
if age == 18:
```

---

## Mistake 2

Forgetting the colon.

Incorrect

```python
if age >= 18
```

Correct

```python
if age >= 18:
```

---

## Mistake 3

Incorrect indentation.

Incorrect

```python
if age >= 18:
print("Adult")
```

Correct

```python
if age >= 18:
    print("Adult")
```

---

## Mistake 4

Writing conditions in the wrong order.

Always put the **most specific condition first**.

---

# Best Practices

✔ Keep conditions simple.

✔ Use meaningful variable names.

✔ Avoid deeply nested code when possible.

✔ Use `elif` instead of many separate `if` statements when only one branch should execute.

✔ Indent consistently.

---

# Summary

## Decision Making

Decision making allows a program to choose between different execution paths.

Python provides

* `if`
* `elif`
* `else`

---

## `if`

Executes only when the condition is `True`.

---

## `else`

Executes when the `if` condition is `False`.

---

## `elif`

Allows checking multiple conditions.

---

## Nested `if`

An `if` inside another `if`.

---

## Logical Operators

Decision making commonly uses

* `and`
* `or`
* `not`

---

## Membership Operators

Conditions often use

```python
in
```

or

```python
not in
```

for validation.

Example

```python
if "@" in email:
```

---

# Comment

A helpful mental model is:

```text
Program Starts

        │
        ▼

Evaluate Condition

        │
        ▼

True ? ───────► Execute Block A

False ───────► Execute Block B

Continue Program
```

Think of `if`, `elif`, and `else` as road intersections. At each intersection, your program decides **which path to take** based on the result of a condition. This idea of **control flow** is fundamental and will be used extensively in loops, functions, exception handling, and beyond.

---