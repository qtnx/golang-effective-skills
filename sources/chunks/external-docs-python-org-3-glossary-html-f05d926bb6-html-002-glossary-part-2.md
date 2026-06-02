---
source_name: "External Linked Documentation"
source_url: "https://docs.python.org/3/glossary.html"
source_path: "sources/raw/external/docs-python-org-3-glossary-html-f05d926bb6.html"
license_ref: ""
---

# Glossary

A function, and by extension a method, is a callable. An instance of a class that implements the `__call__()` method is also a callable.
  callback
A subroutine function which is passed as an argument to be executed at some point in the future.
  class
A template for creating user-defined objects. Class definitions normally contain method definitions which operate on instances of the class.
  class variable
A variable defined in a class and intended to be modified only at class level (i.e., not in an instance of the class).
  closure variable
A free variable referenced from a nested scope that is defined in an outer scope rather than being resolved at runtime from the globals or builtin namespaces. May be explicitly defined with the `nonlocal` keyword to allow write access, or implicitly defined if the variable is only being read.

For example, in the `inner` function in the following code, both `x` and `print` are free variables, but only `x` is a _closure variable_:

```go
def outer():
    x = 0
    def inner():
        nonlocal x
        x += 1
        print(x)
    return inner

```

Due to the `codeobject.co_freevars` attribute (which, despite its name, only includes the names of closure variables rather than listing all referenced free variables), the more general free variable term is sometimes used even when the intended meaning is to refer specifically to closure variables.
  complex number
An extension of the familiar real number system in which all numbers are expressed as a sum of a real part and an imaginary part. Imaginary numbers are real multiples of the imaginary unit (the square root of `-1`), often written `i` in mathematics or `j` in engineering. Python has built-in support for complex numbers, which are written with this latter notation; the imaginary part is written with a `j` suffix, e.g., `3+1j`. To get access to complex equivalents of the `math` module, use `cmath`. Use of complex numbers is a fairly advanced mathematical feature. If you’re not aware of a need for them, it’s almost certain you can safely ignore them.
  concurrency
The ability of a computer program to perform multiple tasks at the same time. Python provides libraries for writing programs that make use of different forms of concurrency. `asyncio` is a library for dealing with asynchronous tasks and coroutines. `threading` provides access to operating system threads and `multiprocessing` to operating system processes. Multi-core processors can execute threads and processes on different CPU cores at the same time (see parallelism).
  concurrent modification
When multiple threads modify shared data at the same time. Concurrent modification without proper synchronization can cause race conditions, and might also trigger a data race, data corruption, or both.
  context
This term has different meanings depending on where and how it is used. Some common meanings:

-
The temporary state or environment established by a context manager via a `with` statement.

-
The collection of key­value bindings associated with a particular `contextvars.Context` object and accessed via `ContextVar` objects. Also see context variable.

-
A `contextvars.Context` object. Also see current context.

context management protocol
The `__enter__()` and `__exit__()` methods called by the `with` statement. See **PEP 343** <https://peps.python.org/pep-0343/>.
  context manager
An object which implements the context management protocol and controls the environment seen in a `with` statement. See **PEP 343** <https://peps.python.org/pep-0343/>.
  context variable
A variable whose value depends on which context is the current context. Values are accessed via `contextvars.ContextVar` objects. Context variables are primarily used to isolate state between concurrent asynchronous tasks.
  contiguous
A buffer is considered contiguous exactly if it is either _C-contiguous_ or _Fortran contiguous_. Zero-dimensional buffers are C and Fortran contiguous. In one-dimensional arrays, the items must be laid out in memory next to each other, in order of increasing indexes starting from zero. In multidimensional C-contiguous arrays, the last index varies the fastest when visiting items in order of memory address. However, in Fortran contiguous arrays, the first index varies the fastest.
  coroutine
Coroutines are a more generalized form of subroutines. Subroutines are entered at one point and exited at another point. Coroutines can be entered, exited, and resumed at many different points. They can be implemented with the `async def` statement. See also **PEP 492** <https://peps.python.org/pep-0492/>.
  coroutine function
A function which returns a coroutine object. A coroutine function may be defined with the `async def` statement, and may contain `await`, `async for`, and `async with` keywords. These were introduced by **PEP 492** <https://peps.python.org/pep-0492/>.
  CPython
The canonical implementation of the Python programming language, as distributed on python.org <https://www.python.org>. The term “CPython” is used when necessary to distinguish this implementation from others such as Jython or IronPython.
  current context
The context (`contextvars.Context` object) that is currently used by `ContextVar` objects to access (get or set) the values of context variables. Each thread has its own current context. Frameworks for executing asynchronous tasks (see `asyncio`) associate each task with a context which becomes the current context whenever the task starts or resumes execution.
  cyclic isolate
A subgroup of one or more objects that reference each other in a reference cycle, but are not referenced by objects outside the group. The goal of the cyclic garbage collector is to identify these groups and break the reference cycles so that the memory can be reclaimed.
  data race
A situation where multiple threads access the same memory location concurrently, at least one of the accesses is a write, and the threads do not use any synchronization to control their access. Data races lead to non-deterministic behavior and can cause data corruption. Proper use of locks and other synchronization primitives prevents data races. Note that data races can only happen in native code, but that native code might be exposed in a Python API. See also race condition and thread-safe.
  deadlock
A situation in which two or more tasks (threads, processes, or coroutines) wait indefinitely for each other to release resources or complete actions, preventing any from making progress. For example, if thread A holds lock 1 and waits for lock 2, while thread B holds lock 2 and waits for lock 1, both threads will wait indefinitely. In Python this often arises from acquiring multiple locks in conflicting orders or from circular join/await dependencies. Deadlocks can be avoided by always acquiring multiple locks in a consistent order. See also lock and reentrant.
  decorator
A function returning another function, usually applied as a function transformation using the `@wrapper` syntax. Common examples for decorators are `classmethod()` and `staticmethod()`.

The decorator syntax is merely syntactic sugar, the following two function definitions are semantically equivalent:

```go
def f(arg):
    ...
f = staticmethod(f)

@staticmethod
def f(arg):
    ...

```

The same concept exists for classes, but is less commonly used there. See the documentation for function definitions and class definitions for more about decorators.
  descriptor
Any object which defines the methods `__get__()`, `__set__()`, or `__delete__()`. When a class attribute is a descriptor, its special binding behavior is triggered upon attribute lookup. Normally, using _a.b_ to get, set or delete an attribute looks up the object named _b_ in the class dictionary for _a_, but if _b_ is a descriptor, the respective descriptor method gets called. Understanding descriptors is a key to a deep understanding of Python because they are the basis for many features including functions, methods, properties, class methods, static methods, and reference to super classes.
