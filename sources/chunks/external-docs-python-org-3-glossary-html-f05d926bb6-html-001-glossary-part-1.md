---
source_name: "External Linked Documentation"
source_url: "https://docs.python.org/3/glossary.html"
source_path: "sources/raw/external/docs-python-org-3-glossary-html-f05d926bb6.html"
license_ref: ""
---

# Glossary

Glossary — Python 3.14.5 documentation
# Glossary
  `>>>`
The default Python prompt of the interactive shell. Often seen for code examples which can be executed interactively in the interpreter.
  `...`
Can refer to:

-
The default Python prompt of the interactive shell when entering the code for an indented code block, when within a pair of matching left and right delimiters (parentheses, square brackets, curly braces or triple quotes), or after specifying a decorator.

-
The three dots form of the Ellipsis object.

abstract base class
Abstract base classes complement duck-typing by providing a way to define interfaces when other techniques like `hasattr()` would be clumsy or subtly wrong (for example with magic methods). ABCs introduce virtual subclasses, which are classes that don’t inherit from a class but are still recognized by `isinstance()` and `issubclass()`; see the `abc` module documentation. Python comes with many built-in ABCs for data structures (in the `collections.abc` module), numbers (in the `numbers` module), streams (in the `io` module), import finders and loaders (in the `importlib.abc` module). You can create your own ABCs with the `abc` module.
  annotate function
A callable that can be called to retrieve the annotations of an object. Annotate functions are usually functions, automatically generated as the `__annotate__` attribute of functions, classes, and modules. Annotate functions are a subset of evaluate functions.
  annotation
A label associated with a variable, a class attribute or a function parameter or return value, used by convention as a type hint.

Annotations of local variables cannot be accessed at runtime, but annotations of global variables, class attributes, and functions can be retrieved by calling `annotationlib.get_annotations()` on modules, classes, and functions, respectively.

See variable annotation, function annotation, **PEP 484** <https://peps.python.org/pep-0484/>, **PEP 526** <https://peps.python.org/pep-0526/>, and **PEP 649** <https://peps.python.org/pep-0649/>, which describe this functionality. Also see Annotations Best Practices for best practices on working with annotations.
  argument
A value passed to a function (or method) when calling the function. There are two kinds of argument:

-
_keyword argument_: an argument preceded by an identifier (e.g. `name=`) in a function call or passed as a value in a dictionary preceded by `**`. For example, `3` and `5` are both keyword arguments in the following calls to `complex()`:

```go
complex(real=3, imag=5)
complex(**{'real': 3, 'imag': 5})

```

-
_positional argument_: an argument that is not a keyword argument. Positional arguments can appear at the beginning of an argument list and/or be passed as elements of an iterable preceded by `*`. For example, `3` and `5` are both positional arguments in the following calls:

```go
complex(3, 5)
complex(*(3, 5))

```

Arguments are assigned to the named local variables in a function body. See the Calls section for the rules governing this assignment. Syntactically, any expression can be used to represent an argument; the evaluated value is assigned to the local variable.

See also the parameter glossary entry, the FAQ question on the difference between arguments and parameters, and **PEP 362** <https://peps.python.org/pep-0362/>.
  asynchronous context manager
An object which controls the environment seen in an `async with` statement by defining `__aenter__()` and `__aexit__()` methods. Introduced by **PEP 492** <https://peps.python.org/pep-0492/>.
  asynchronous generator
A function which returns an asynchronous generator iterator. It looks like a coroutine function defined with `async def` except that it contains `yield` expressions for producing a series of values usable in an `async for` loop.

Usually refers to an asynchronous generator function, but may refer to an _asynchronous generator iterator_ in some contexts. In cases where the intended meaning isn’t clear, using the full terms avoids ambiguity.

An asynchronous generator function may contain `await` expressions as well as `async for`, and `async with` statements.
  asynchronous generator iterator
An object created by an asynchronous generator function.

This is an asynchronous iterator which when called using the `__anext__()` method returns an awaitable object which will execute the body of the asynchronous generator function until the next `yield` expression.

Each `yield` temporarily suspends processing, remembering the execution state (including local variables and pending try-statements). When the _asynchronous generator iterator_ effectively resumes with another awaitable returned by `__anext__()`, it picks up where it left off. See **PEP 492** <https://peps.python.org/pep-0492/> and **PEP 525** <https://peps.python.org/pep-0525/>.
  asynchronous iterable
An object, that can be used in an `async for` statement. Must return an asynchronous iterator from its `__aiter__()` method. Introduced by **PEP 492** <https://peps.python.org/pep-0492/>.
  asynchronous iterator
An object that implements the `__aiter__()` and `__anext__()` methods. `__anext__()` must return an awaitable object. `async for` resolves the awaitables returned by an asynchronous iterator’s `__anext__()` method until it raises a `StopAsyncIteration` exception. Introduced by **PEP 492** <https://peps.python.org/pep-0492/>.
  atomic operation
An operation that appears to execute as a single, indivisible step: no other thread can observe it half-done, and its effects become visible all at once. Python does not guarantee that high-level statements are atomic (for example, `x += 1` performs multiple bytecode operations and is not atomic). Atomicity is only guaranteed where explicitly documented. See also race condition and data race.
  attached thread state
A thread state that is active for the current OS thread.

When a thread state is attached, the OS thread has access to the full Python C API and can safely invoke the bytecode interpreter.

Unless a function explicitly notes otherwise, attempting to call the C API without an attached thread state will result in a fatal error or undefined behavior. A thread state can be attached and detached explicitly by the user through the C API, or implicitly by the runtime, including during blocking C calls and by the bytecode interpreter in between calls.

On most builds of Python, having an attached thread state implies that the caller holds the GIL for the current interpreter, so only one OS thread can have an attached thread state at a given moment. In free-threaded builds of Python, threads can concurrently hold an attached thread state, allowing for true parallelism of the bytecode interpreter.
  attribute
A value associated with an object which is usually referenced by name using dotted expressions. For example, if an object _o_ has an attribute _a_ it would be referenced as _o.a_.

It is possible to give an object an attribute whose name is not an identifier as defined by Names (identifiers and keywords), for example using `setattr()`, if the object allows it. Such an attribute will not be accessible using a dotted expression, and would instead need to be retrieved with `getattr()`.
  awaitable
An object that can be used in an `await` expression. Can be a coroutine or an object with an `__await__()` method. See also **PEP 492** <https://peps.python.org/pep-0492/>.
  BDFL
Benevolent Dictator For Life, a.k.a. Guido van Rossum <https://gvanrossum.github.io/>, Python’s creator.
  binary file
A file object able to read and write bytes-like objects. Examples of binary files are files opened in binary mode (`'rb'`, `'wb'` or `'rb+'`), `sys.stdin.buffer`, `sys.stdout.buffer`, and instances of `io.BytesIO` and `gzip.GzipFile`.

See also text file for a file object able to read and write `str` objects.
  borrowed reference
In Python’s C API, a borrowed reference is a reference to an object, where the code using the object does not own the reference. It becomes a dangling pointer if the object is destroyed. For example, a garbage collection can remove the last strong reference to the object and so destroy it.

Calling `Py_INCREF()` on the borrowed reference is recommended to convert it to a strong reference in-place, except when the object cannot be destroyed before the last usage of the borrowed reference. The `Py_NewRef()` function can be used to create a new strong reference.
  bytes-like object
An object that supports the Buffer Protocol and can export a C-contiguous buffer. This includes all `bytes`, `bytearray`, and `array.array` objects, as well as many common `memoryview` objects. Bytes-like objects can be used for various operations that work with binary data; these include compression, saving to a binary file, and sending over a socket.

Some operations need the binary data to be mutable. The documentation often refers to these as “read-write bytes-like objects”. Example mutable buffer objects include `bytearray` and a `memoryview` of a `bytearray`. Other operations require the binary data to be stored in immutable objects (“read-only bytes-like objects”); examples of these include `bytes` and a `memoryview` of a `bytes` object.
  bytecode
Python source code is compiled into bytecode, the internal representation of a Python program in the CPython interpreter. The bytecode is also cached in `.pyc` files so that executing the same file is faster the second time (recompilation from source to bytecode can be avoided). This “intermediate language” is said to run on a virtual machine that executes the machine code corresponding to each bytecode. Do note that bytecodes are not expected to work between different Python virtual machines, nor to be stable between Python releases.

A list of bytecode instructions can be found in the documentation for the dis module.
  callable
A callable is an object that can be called, possibly with a set of arguments (see argument), with the following syntax:

```go
callable(argument1, argument2, argumentN)

```
