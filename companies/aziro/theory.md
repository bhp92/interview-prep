# Aziro — Theory Questions: Answers & Revision Notes

| # | Question | Outcome |
|---|----------|---------|
| Q3 | What are Decorators? | ✅ Answered |
| Q4 | What are Generators? | ❌ Could not answer |
| Q5 | What is an abstract method? | ✅ Answered |
| Q6 | What is a class method? | ❌ Could not answer |
| Q7 | What is the super() method? | ✅ Answered |
| Q8 | What is inheritance? | ✅ Answered |

---

## Q3 — Decorators ✅

A decorator is a function that wraps another function to extend its behaviour without modifying it directly.
A decorator is a tool that lets you add new behavior to an existing function without changing the actual code.

```python
def logger(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        return func(*args, **kwargs) # return Redundant for greet() (returns None), but keeps the decorator safe for functions that return values
    return wrapper

@logger
def greet(name):
    print(f"Hello, {name}")

greet("Alice")
# Calling greet
# Hello, Alice
```

---

## Q4 — Generators ❌

A generator is a function that uses `yield` instead of `return`. It returns a **generator object** that produces values one at a time (lazy evaluation) — memory efficient for large sequences.
A generator returns an iterator object, allowing it to produce a sequence of values one at a time only when req uested.

```python
def count_up(n):
    for i in range(n):
        yield i

gen = count_up(3)
print(next(gen))  # 0
print(next(gen))  # 1
print(next(gen))  # 2
```

Key differences vs a regular function:
- Pauses at each `yield`, resumes from same point on next `next()` call
- Does not hold all values in memory at once
- `list(count_up(3))` → `[0, 1, 2]` to materialise all values

---

## Q5 — Abstract Method ✅

An abstract method is a method declared in a base class with no implementation, forcing subclasses to provide one. Defined using `@abstractmethod` from the `abc` module.
Abstract method is used to make a method mandatory for use in child class.

```python
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof"
```

Instantiating `Animal` directly raises `TypeError`.

---

## Q6 — Class Method ❌

A class method is decorated with `@classmethod` and receives `cls` (the class itself) as its first argument instead of `self` (the instance). Can be called on the class directly.
A class method allows function to access and modify class attributes using cls

```python
class Dog:
    species = "Canis familiaris"

    def __init__(self, name):
        self.name = name

    @classmethod
    def get_species(cls):
        return cls.species

    @classmethod
    def from_string(cls, name_string):
        # Alternative constructor pattern
        name = name_string.upper()
        return cls(name)

print(Dog.get_species())          # Canis familiaris
d = Dog.from_string("buddy")
print(d.name)                     # BUDDY
```

Comparison:
| | `self` | `cls` | neither |
|---|---|---|---|
| Instance method | ✅ | — | — |
| Class method (`@classmethod`) | — | ✅ | — |
| Static method (`@staticmethod`) | — | — | ✅ |

---

## Q7 — super() ✅

`super()` returns a proxy object that delegates method calls to a parent class. Used to call the parent's `__init__` or any overridden method.
`super()` is used in a child class to access methods or constructor of a parent class. It is useful when a child class overrides a parent method but still wants to execute the parent class logic for some part of the functionality.

```python
class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)   # calls Animal.__init__
        self.breed = breed
```

---

## Q8 — Inheritance ✅

Inheritance allows a class (child) to acquire attributes and methods of another class (parent), enabling code reuse and hierarchy.

```python
class Animal:
    def speak(self):
        return "..."

class Dog(Animal):
    def speak(self):       # overrides parent
        return "Woof"

class Cat(Animal):
    def speak(self):
        return "Meow"
```

Types: single, multiple (`class C(A, B)`), multilevel, hierarchical.