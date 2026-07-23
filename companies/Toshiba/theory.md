# Toshiba — Theory Questions: Answers & Revision Notes

| # | Question |
|---|----------|
| t1 |	Primitive / built-in data types	|
| t2 |	Deep copy vs shallow copy (memory management) |
| t3 |	What is OOP and what is it all about |
| t4 |	Multithreading vs multiprocessing |
| t5 |	What makes a REST API RESTful |
| t6 |	Firmware test pipeline design (storage scenario) |

## t1 - Primitive/Built-in data types

Python does not have "primitives" in the Java sense. There is no int vs Integer split, no stack-allocated raw values. Everything is an object - an int, a bool, even a function - so every value has a type, an id, and methods.

```python
print(type(5))                  # <class 'int'>
print((5).bit_length())         # 3 - as int has methods, it is an object
print(type(True))               # <class 'bool'>

The built-in typesworth naming:

| Category | Types |
|----------|-------|
| Numeric | int, float, complex |
| Boolean | bool (a subclass of int - True == 1) |
| Text | str |
| None | NoneType (the single value None)
| Sequence | list, tuple, range |
| Mapping | dict |
| set | set, frozenset |

```python
print(isinstance(True, int))    # True - bool subclass int
print(True + True)              # 2
```

The interview framing was "primitive data types" - the strong answer is to name the built-ins and make the point that python has no primitive/wrapper distinction at all. (Likeliy a tricky question probing wheather you'd blindly map Java's 8 primitives onto Python)

---

## t2 - Deep copy vs Shallow copy

### Shallow Copy
A shallow copy creates a new outer object, but the objects contained inside it are not copied; their references are copied instead. As a result, the original and the copy share the same nested objects.

### Deep Copy
A deep copy recursively copied the object and every nested objectinside it, making the entire structure completely independent of the original. Since nested object is duplicated, a deep copy uses more memory.

```python
import copy

o = [[1, 2], [3, 4]]

s = copy.copy(o)
d = copy.deepcopy(o)

s.append(5)
s[1].append(6)
d.append(7)
d.append(8)

print(o)                        # [[1, 2], [3, 4, 6]] - changes to s does not change the o. A newer copy of outer object is created in shallow copy.
print(s)                        # [[1, 2], [3, 4, 6], 5] - changes to s.
print(d)                        # [[1, 2], [3, 4, 8], 7] - deep copy created a separate copy of objects and it's nested objects.
```

`s` is a new outer list but `s[0]` is `o[0]` - The same inner lisst object in memory. Mutating it shows up in both. `deepcopy` built it's own inner lists, so it is fully independent.

Rebinding a whole element `s[0] = [9]` affexts only the copy - that swaps reference rather than mutating the shared object. The trap is only in-place mutation of a shared inner object.

The distinction only matters for nested/compound objects. It is about how many levels of the structures get duplicated versus shared by reference.

- Assignment (b = a) — not a copy at all. Both names point at the same object.
- Shallow copy — a new outer object, but the inner objects are shared references.
- Deep copy — recursively copies everything; no references shared with the original.

## t3 - What is OOP and what it's all about

OOP models a programme or piece of code as objects. OOP is about bundling data (attributes) and behavior that acts on that data (methods) instead of loose functions and free floating state. It's four pillars are as below,
- `Encapsullation`: Keep data and the methods that operate on it together in once object, and control access to internal state (in python by convention: `_protected`, `__private` name-mangled)
- `Abstraction`: Expose what object does, hide how. A caller called `drive.flash()` without knowing the internals. Abstract base classes `ABC` formalise this.
- `Inheritance`: A child classs reuses and specialises a parent's behavior, so shared logic is written once.
- `Polymorphism`: The same call works across different types. In python this is usually `duck typing`: if a object has the method, it works, no shared base class required.

```python
class StorageDevice:
    def read(self):
        raise NotImplementedError

class SSD(StorageDevice):
    def read(self):
        return "fast read"

class HDD(StorageDevice):
    def read(self):
        return "spinning read"

# Polymorphism: same loop, different concrete behavior

for device in (SSD(), HDD()):
    print(device.read())
```

It keeps large systems maintainable, related state and behavior stay together, changes stay local and shared logic is't copy-pasted.

## t4 - Multithreading vs Multiprocessing

### Multithreading
Multithreading is the splitting the process in multiple threads, execution of these threads within the same process. All threads share the process's resources, including the code segment, heap, global variables, open files, network sockets and other operating system resources. But each thread has it's own stack, cpu registers and execution state. Because the threads share the same memory, communication between them is fast,but access to shared data must be synchronised to avoid race conditions.

```
                 Process
+--------------------------------------------------+
| Code (Shared)                                    |
| Heap / Python Objects (Shared)                   |
| Global Variables (Shared)                        |
| Open Files (Shared)                              |
| Network Sockets (Shared)                         |
| Python Interpreter (Shared)                      |
| GIL (Shared)                                     |
|                                                  |
| Thread 1 → Stack + Registers                     |
| Thread 2 → Stack + Registers                     |
| Thread 3 → Stack + Registers                     |
+--------------------------------------------------+
```

Multithreading is best suited for I/O - bound workloads because while one thread waits for I/O (disk, network, devices, etc.), another thread can aquire the GIL and continue executing the python code.

### Global Interpreter Lock (GIL)
CPython, the reference implementation of python written in C (just as Jython is implmented in Java and runs on JVM) uses a Global Interpreter Lock (GIL). Each CPython interpreter has one GIL. In the common case one python process contains one interpreter, so that process has one GIL. All threads in that interpreter must aquire the GIL before they can execute python bytecode. The GIL is periodically released and reaquired, allowing threads to take turns executing. This creates concurrency (multiple task making progress over time), but not parallel execution of python bytecode.

### Race Condition
A race condition occurs when multiple threads or processes access the same shared data concurrently, and the final result depends on the unpredictable order in which their operations occur. Because the shared memory is modified without proper synchronization, the programme may produce incorrect or inconsistent reuslts
A race condition occurs when two or more threads (or processes) compete to read or write the same shared memory, making the program's result depend on the order in which they execute.

### Multiprocessing
Multiprocessing is execution of multiple independent processes, where each process has it's own address space, memory, Python interpreter and Global Interpreter Lock (GIL). Since processes do not share memory by default, they can execute Python bytecode truley in prallel on multiple CPU cores.
Multiprocessing solves the limitation of multithreading in CPython, where multiple threads cannot execute Python bytecode simultaneously because they compete for a single GIL within the same interpreter. By giving such process it's own interpreter and GIL, multiprocessing enables true CPU parallelism for computationally intensive workloads.

```
+--------------------------------------------------+
Process A                                          |
-------------------------                          |
Code                                               |
Heap                                               |
Globals                                            |
Interpreter                                        |
GIL                                                |
Stack(s)                                           |
                                                   | 
=========================                          |
                                                   |
Process B                                          |
-------------------------                          |
Code                                               |
Heap                                               |
Globals                                            |
Interpreter                                        |
GIL                                                |
Stack(s)                                           |
+--------------------------------------------------+
```

Each process owns a completely separate address space. Changing memory in one process has no effect on another unless the processes explicitly communicate (for example, usng pipes, queues, sockets, or shared-memory mechanisms).

### Python & CPython
- Python - The language rules with which you write the code. The programming language; it defines the syntax, semantics, and rules you follow when writing Python code.
- CPython - The official program written in C that turns the code into computer instructions. The reference implementation of the Python language, written in C. It reads, compiles, and executes Python code by translating it into Python bytecode and interpreting that bytecode.
- Python Bytecode = The instructions generated by CPython from your python source code. These instructions are executed by the CPython interpreter, which translates them into machine instructions that are untimately executed by the CPU.

```
Python Source Code (.py)
        │
        ▼
CPython Compiler
        │
        ▼
Python Bytecode
        │
        ▼
CPython Virtual Machine (Interpreter)
        │
        ▼
Machine Instructions
        │
        ▼
CPU
```