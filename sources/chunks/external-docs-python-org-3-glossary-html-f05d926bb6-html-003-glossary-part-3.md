---
source_name: "External Linked Documentation"
source_url: "https://docs.python.org/3/glossary.html"
source_path: "sources/raw/external/docs-python-org-3-glossary-html-f05d926bb6.html"
license_ref: ""
---

# Glossary

For more information about descriptors’ methods, see Implementing Descriptors or the Descriptor How To Guide.
  dictionary
An associative array, where arbitrary keys are mapped to values. The keys can be any object with `__hash__()` and `__eq__()` methods. Called a hash in Perl.
  dictionary comprehension
A compact way to process all or part of the elements in an iterable and return a dictionary with the results. `results = {n: n ** 2 for n in range(10)}` generates a dictionary containing key `n` mapped to value `n ** 2`. See Displays for lists, sets and dictionaries.
  dictionary view
The objects returned from `dict.keys()`, `dict.values()`, and `dict.items()` are called dictionary views. They provide a dynamic view on the dictionary’s entries, which means that when the dictionary changes, the view reflects these changes. To force the dictionary view to become a full list use `list(dictview)`. See Dictionary view objects.
  docstring
A string literal which appears as the first expression in a class, function or module. While ignored when the suite is executed, it is recognized by the compiler and put into the `__doc__` attribute of the enclosing class, function or module. Since it is available via introspection, it is the canonical place for documentation of the object.
  duck-typing
A programming style which does not look at an object’s type to determine if it has the right interface; instead, the method or attribute is simply called or used (“If it looks like a duck and quacks like a duck, it must be a duck.”) By emphasizing interfaces rather than specific types, well-designed code improves its flexibility by allowing polymorphic substitution. Duck-typing avoids tests using `type()` or `isinstance()`. (Note, however, that duck-typing can be complemented with abstract base classes.) Instead, it typically employs `hasattr()` tests or EAFP programming.
  dunder
An informal short-hand for “double underscore”, used when talking about a special method. For example, `__init__` is often pronounced “dunder init”.
  EAFP
Easier to ask for forgiveness than permission. This common Python coding style assumes the existence of valid keys or attributes and catches exceptions if the assumption proves false. This clean and fast style is characterized by the presence of many `try` and `except` statements. The technique contrasts with the LBYL style common to many other languages such as C.
  evaluate function
A function that can be called to evaluate a lazily evaluated attribute of an object, such as the value of type aliases created with the `type` statement.
  expression
A piece of syntax which can be evaluated to some value. In other words, an expression is an accumulation of expression elements like literals, names, attribute access, operators or function calls which all return a value. In contrast to many other languages, not all language constructs are expressions. There are also statements which cannot be used as expressions, such as `while`. Assignments are also statements, not expressions.
  extension module
A module written in C or C++, using Python’s C API to interact with the core and with user code.
  f-stringf-strings
String literals prefixed with `f` or `F` are commonly called “f-strings” which is short for formatted string literals. See also **PEP 498** <https://peps.python.org/pep-0498/>.
  file object
An object exposing a file-oriented API (with methods such as `read()` or `write()`) to an underlying resource. Depending on the way it was created, a file object can mediate access to a real on-disk file or to another type of storage or communication device (for example standard input/output, in-memory buffers, sockets, pipes, etc.). File objects are also called _file-like objects_ or _streams_.

There are actually three categories of file objects: raw binary files, buffered binary files and text files. Their interfaces are defined in the `io` module. The canonical way to create a file object is by using the `open()` function.
  file-like object
A synonym for file object.
  filesystem encoding and error handler
Encoding and error handler used by Python to decode bytes from the operating system and encode Unicode to the operating system.

The filesystem encoding must guarantee to successfully decode all bytes below 128. If the file system encoding fails to provide this guarantee, API functions can raise `UnicodeError`.

The `sys.getfilesystemencoding()` and `sys.getfilesystemencodeerrors()` functions can be used to get the filesystem encoding and error handler.

The filesystem encoding and error handler are configured at Python startup by the `PyConfig_Read()` function: see `filesystem_encoding` and `filesystem_errors` members of `PyConfig`.

See also the locale encoding.
  finder
An object that tries to find the loader for a module that is being imported.

There are two types of finder: meta path finders for use with `sys.meta_path`, and path entry finders for use with `sys.path_hooks`.

See Finders and loaders and `importlib` for much more detail.
  floor division
Mathematical division that rounds down to nearest integer. The floor division operator is `//`. For example, the expression `11 // 4` evaluates to `2` in contrast to the `2.75` returned by float true division. Note that `(-11) // 4` is `-3` because that is `-2.75` rounded _downward_. See **PEP 238** <https://peps.python.org/pep-0238/>.
  free threading
A threading model where multiple threads can run Python bytecode simultaneously within the same interpreter. This is in contrast to the global interpreter lock which allows only one thread to execute Python bytecode at a time. See **PEP 703** <https://peps.python.org/pep-0703/>.
  free-threaded build
A build of CPython that supports free threading, configured using the `--disable-gil` option before compilation.

See Python support for free threading.
  free variable
Formally, as defined in the language execution model, a free variable is any variable used in a namespace which is not a local variable in that namespace. See closure variable for an example. Pragmatically, due to the name of the `codeobject.co_freevars` attribute, the term is also sometimes used as a synonym for closure variable.
  function
A series of statements which returns some value to a caller. It can also be passed zero or more arguments which may be used in the execution of the body. See also parameter, method, and the Function definitions section.
  function annotation
An annotation of a function parameter or return value.

Function annotations are usually used for type hints: for example, this function is expected to take two `int` arguments and is also expected to have an `int` return value:

```go
def sum_two_numbers(a: int, b: int) -> int:
   return a + b

```

Function annotation syntax is explained in section Function definitions.

See variable annotation and **PEP 484** <https://peps.python.org/pep-0484/>, which describe this functionality. Also see Annotations Best Practices for best practices on working with annotations.
  __future__
A future statement, `from __future__ import <feature>`, directs the compiler to compile the current module using syntax or semantics that will become standard in a future release of Python. The `__future__` module documents the possible values of _feature_. By importing this module and evaluating its variables, you can see when a new feature was first added to the language and when it will (or did) become the default:

```go
>>> import __future__
>>> __future__.division
_Feature((2, 2, 0, 'alpha', 2), (3, 0, 0, 'alpha', 0), 8192)

```

garbage collection
The process of freeing memory when it is not used anymore. Python performs garbage collection via reference counting and a cyclic garbage collector that is able to detect and break reference cycles. The garbage collector can be controlled using the `gc` module.
  generator
A function which returns a generator iterator. It looks like a normal function except that it contains `yield` expressions for producing a series of values usable in a for-loop or that can be retrieved one at a time with the `next()` function.

Usually refers to a generator function, but may refer to a _generator iterator_ in some contexts. In cases where the intended meaning isn’t clear, using the full terms avoids ambiguity.
  generator iterator
An object created by a generator function.

Each `yield` temporarily suspends processing, remembering the execution state (including local variables and pending try-statements). When the _generator iterator_ resumes, it picks up where it left off (in contrast to functions which start fresh on every invocation).
  generator expression
An expression that returns an iterator. It looks like a normal expression followed by a `for` clause defining a loop variable, range, and an optional `if` clause. The combined expression generates values for an enclosing function:

```go
>>> sum(i*i for i in range(10))         # sum of squares 0, 1, 4, ... 81
285

```

generic function
A function composed of multiple functions implementing the same operation for different types. Which implementation should be used during a call is determined by the dispatch algorithm.

See also the single dispatch glossary entry, the `functools.singledispatch()` decorator, and **PEP 443** <https://peps.python.org/pep-0443/>.
  generic type
A type that can be parameterized; typically a container class such as `list` or `dict`. Used for type hints and annotations.

For more details, see generic alias types, **PEP 483** <https://peps.python.org/pep-0483/>, **PEP 484** <https://peps.python.org/pep-0484/>, **PEP 585** <https://peps.python.org/pep-0585/>, and the `typing` module.
  GIL
See global interpreter lock.
  global interpreter lock
The mechanism used by the CPython interpreter to assure that only one thread executes Python bytecode at a time. This simplifies the CPython implementation by making the object model (including critical built-in types such as `dict`) implicitly safe against concurrent access. Locking the entire interpreter makes it easier for the interpreter to be multi-threaded, at the expense of much of the parallelism afforded by multi-processor machines.

However, some extension modules, either standard or third-party, are designed so as to release the GIL when doing computationally intensive tasks such as compression or hashing. Also, the GIL is always released when doing I/O.
