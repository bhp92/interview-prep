# Python Practice: `map`, `filter`, and `lambda`

30 problems (10 each), difficulty increasing 1 → 10 per topic.
All solutions below have been run and verified against the expected output.

---

## MAP

### 1. Double each number
**Input:** `[1, 2, 3, 4]` → **Output:** `[2, 4, 6, 8]`
```python
def double(lst):
    return list(map(lambda x: x * 2, lst))

print(double([1, 2, 3, 4]))
```

### 2. Convert each string to its length
**Input:** `['hi', 'hello', 'hey']` → **Output:** `[2, 5, 3]`
```python
def length_of_chars(lst):
    return list(map(len, lst))

print(length_of_chars(['hi', 'hello', 'hey']))
```

### 3. Convert each int to a string
**Input:** `[1, 22, 333]` → **Output:** `['1', '22', '333']`
```python
def int_to_str(lst):
    return list(map(str, lst))

print(int_to_str([1, 22, 333]))
```

### 4. Turn each number `n` into a `(n, n**2)` tuple
**Input:** `[1, 2, 3]` → **Output:** `[(1, 1), (2, 4), (3, 9)]`
```python
def convert(lst):
    return list(map(lambda x: (x, x ** 2), lst))

print(convert([1, 2, 3]))
```

### 5. Multiply two lists element-wise
**Input:** `[1, 2, 3]`, `[4, 5, 6]` → **Output:** `[4, 10, 18]`
```python
def multiply_two_lists(lst1, lst2):
    return list(map(lambda x, y: x * y, lst1, lst2))

print(multiply_two_lists([1, 2, 3], [4, 5, 6]))
```

### 6. Capitalize the first letter of each word
**Input:** `['hello', 'world']` → **Output:** `['Hello', 'World']`
```python
def capitalize(lst):
    return list(map(lambda x: x.capitalize(), lst))

print(capitalize(['hello', 'world']))
```

### 7. Extract the `'name'` field from each dict
**Input:** `[{'name': 'Alice', 'age': 30}, {'name': 'Bob', 'age': 25}]` → **Output:** `['Alice', 'Bob']`
```python
def extract_name(lst):
    return list(map(lambda x: x['name'], lst))

print(extract_name([{'name': 'Alice', 'age': 30}, {'name': 'Bob', 'age': 25}]))
```

### 8. Round each float to 2 decimals
**Input:** `[3.14159, 2.71828, 1.61803]` → **Output:** `[3.14, 2.72, 1.62]`
```python
def round_float(lst):
    return list(map(lambda x: round(x, 2), lst))

print(round_float([3.14159, 2.71828, 1.61803]))
```

### 9. Sum three lists element-wise
**Input:** `[1, 2, 3]`, `[10, 20, 30]`, `[100, 200, 300]` → **Output:** `[111, 222, 333]`
```python
def sum_three(lst1, lst2, lst3):
    return list(map(lambda x, y, z: x + y + z, lst1, lst2, lst3))

print(sum_three([1, 2, 3], [10, 20, 30], [100, 200, 300]))
```

### 10. Convert each binary string to its integer value
**Input:** `['101', '1111', '10']` → **Output:** `[5, 15, 2]`
```python
def bin_to_int(lst):
    return list(map(lambda x: int(x, 2), lst))

print(bin_to_int(['101', '1111', '10']))
```

---

## FILTER

### 1. Keep positive numbers
**Input:** `[-3, 5, -1, 8, 0, 2]` → **Output:** `[5, 8, 2]`
```python
def positive_only(lst):
    return list(filter(lambda x: x > 0, lst))

print(positive_only([-3, 5, -1, 8, 0, 2]))
```

### 2. Keep odd numbers
**Input:** `[1, 2, 3, 4, 5, 6]` → **Output:** `[1, 3, 5]`
```python
def odd_number(lst):
    return list(filter(lambda x: x % 2 != 0, lst))

print(odd_number([1, 2, 3, 4, 5, 6]))
```

### 3. Keep non-empty strings
**Input:** `['a', '', 'b', '', 'c']` → **Output:** `['a', 'b', 'c']`
```python
def non_empty_string(lst):
    return list(filter(lambda x: x, lst))

print(non_empty_string(['a', '', 'b', '', 'c']))
```

### 4. Keep numbers divisible by 3
**Input:** `[1, 3, 5, 6, 9, 10, 12]` → **Output:** `[3, 6, 9, 12]`
```python
def divisible_by_3(lst):
    return list(filter(lambda x: x % 3 == 0, lst))

print(divisible_by_3([1, 3, 5, 6, 9, 10, 12]))
```

### 5. Keep strings longer than 4 characters
**Input:** `['cat', 'window', 'ox', 'defenestrate', 'hi']` → **Output:** `['window', 'defenestrate']`
```python
def longer_than_4(lst):
    return list(filter(lambda x: len(x) > 4, lst))

print(longer_than_4(['cat', 'window', 'ox', 'defenestrate', 'hi']))
```

### 6. Keep palindromes
**Input:** `['level', 'python', 'radar', 'hello', 'noon']` → **Output:** `['level', 'radar', 'noon']`
```python
def palindrome(lst):
    return list(filter(lambda x: x == x[::-1], lst))

print(palindrome(['level', 'python', 'radar', 'hello', 'noon']))
```

### 7. Keep numbers whose digits sum to an even number
**Input:** `[12, 22, 31, 44, 5]` → **Output:** `[22, 31, 44]`
```python
def sum_even(lst):
    return list(filter(lambda x: sum(int(d) for d in str(x)) % 2 == 0, lst))

print(sum_even([12, 22, 31, 44, 5]))
```

### 8. Keep strings containing at least one digit
**Input:** `['abc', 'a1b', 'hello', 'test9', '123']` → **Output:** `['a1b', 'test9', '123']`
```python
def digit_check(lst):
    return list(filter(lambda x: any(i.isdigit() for i in x), lst))

print(digit_check(['abc', 'a1b', 'hello', 'test9', '123']))
```

### 9. Keep prime numbers
**Input:** `[2, 3, 4, 5, 6, 7, 8, 9, 10, 11]` → **Output:** `[2, 3, 5, 7, 11]`
```python
import math

def prime(lst):
    return list(filter(
        lambda x: x >= 2 and all(x % i != 0 for i in range(2, int(math.sqrt(x)) + 1)),
        lst
    ))

print(prime([2, 3, 4, 5, 6, 7, 8, 9, 10, 11]))
```

### 10. Keep dicts where `'active'` is `True` and `'age' >= 18`
**Input:**
```python
[{'name': 'A', 'active': True,  'age': 20},
 {'name': 'B', 'active': False, 'age': 30},
 {'name': 'C', 'active': True,  'age': 15},
 {'name': 'D', 'active': True,  'age': 45}]
```
**Output:** `[{'name': 'A', 'active': True, 'age': 20}, {'name': 'D', 'active': True, 'age': 45}]`
```python
def active(lst):
    return list(filter(lambda x: x['active'] and x['age'] >= 18, lst))

print(active([
    {'name': 'A', 'active': True,  'age': 20},
    {'name': 'B', 'active': False, 'age': 30},
    {'name': 'C', 'active': True,  'age': 15},
    {'name': 'D', 'active': True,  'age': 45}
]))
```

---

## LAMBDA

### 1. A lambda that adds two numbers
`add(3, 4)` → `7`
```python
add = lambda a, b: a + b
print(add(3, 4))
```

### 2. A lambda returning the last character of a string
`last('hello')` → `'o'`
```python
last = lambda x: x[-1]
print(last('hello'))
```

### 3. Sort a list of tuples by the second element
**Input:** `[(1, 3), (2, 1), (3, 2)]` → **Output:** `[(2, 1), (3, 2), (1, 3)]`
```python
def sort_a_list(lst):
    return sorted(lst, key=lambda x: x[-1])

print(sort_a_list([(1, 3), (2, 1), (3, 2)]))
```

### 4. Sort strings by length
**Input:** `['banana', 'kiwi', 'apple', 'fig']` → **Output:** `['fig', 'kiwi', 'apple', 'banana']`
```python
def sort_by_len(lst):
    return sorted(lst, key=lambda x: len(x))

print(sort_by_len(['banana', 'kiwi', 'apple', 'fig']))
```

### 5. A lambda returning `'even'` or `'odd'`
`parity(7)` → `'odd'`
```python
parity = lambda x: 'even' if x % 2 == 0 else 'odd'
print(parity(7))
```

### 6. Use `reduce` with a lambda to compute the product of a list
**Input:** `[1, 2, 3, 4, 5]` → **Output:** `120`
```python
from functools import reduce

def product(lst):
    return reduce(lambda a, b: a * b, lst)

print(product([1, 2, 3, 4, 5]))
```

### 7. Sort a list of dicts by `'age'` descending
**Input:** `[{'name': 'A', 'age': 30}, {'name': 'B', 'age': 25}, {'name': 'C', 'age': 40}]`
**Output:** `[{'name': 'C', 'age': 40}, {'name': 'A', 'age': 30}, {'name': 'B', 'age': 25}]`
```python
def sort_by_age_desc(lst):
    return sorted(lst, key=lambda x: x['age'], reverse=True)

print(sort_by_age_desc([{'name': 'A', 'age': 30}, {'name': 'B', 'age': 25}, {'name': 'C', 'age': 40}]))
```

### 8. Sort strings by vowel count ascending (ties keep original order)
**Input:** `['sky', 'apple', 'be', 'ok']` → **Output:** `['sky', 'be', 'ok', 'apple']`
```python
def sort_by_vowels(lst):
    return sorted(lst, key=lambda x: sum(ch in 'aeiou' for ch in x))

print(sort_by_vowels(['sky', 'apple', 'be', 'ok']))
```

### 9. Use `reduce` with a lambda to find the max, without using `max()`
**Input:** `[3, 7, 2, 8, 5]` → **Output:** `8`
```python
from functools import reduce

def find_max(lst):
    return reduce(lambda a, b: a if a > b else b, lst)

print(find_max([3, 7, 2, 8, 5]))
```

### 10. Sort full names by last name, then first name
**Input:** `['John Smith', 'Jane Adams', 'Bob Smith', 'Alice Adams']`
**Output:** `['Alice Adams', 'Jane Adams', 'Bob Smith', 'John Smith']`
```python
def sort_by_last_first(lst):
    return sorted(lst, key=lambda x: (x.split()[-1], x.split()[0]))

print(sort_by_last_first(['John Smith', 'Jane Adams', 'Bob Smith', 'Alice Adams']))
```

---

## Notes from review

- **map #2, #3**: no need to wrap `len`/`str` in a lambda when passing them directly to `map` does the same job (`map(len, lst)` instead of `map(lambda x: len(x), lst)`). Use a lambda when you're doing something *around* the call, not just forwarding the argument.
- **filter #9 (primes)**: capping the divisor check at `sqrt(x) + 1` instead of `x` is the efficient version, not just a "works" version — worth keeping as the default pattern.
- **lambda #9**: the point of "without `max()`" is to hand-write the comparison logic (`a if a > b else b`), rather than calling `max(a, b)` inside the lambda — that would just be delegating back to the builtin you were told to avoid.