---
source_name: "External Linked Documentation"
source_url: "https://docs.python.org/3/glossary.html"
source_path: "sources/raw/external/docs-python-org-3-glossary-html-f05d926bb6.html"
license_ref: ""
---

# Glossary

The `collections.abc.Sequence` abstract base class defines a much richer interface that goes beyond just `__getitem__()` and `__len__()`, adding `count()`, `index()`, `__contains__()`, and `__reversed__()`. Types that implement this expanded interface can be registered explicitly using `register()`. For more documentation on sequence methods generally, see Common Sequence Operations.
  set comprehension
A compact way to process all or part of the elements in an iterable and return a set with the results. `results = {c for c in 'abracadabra' if c not in 'abc'}` generates the set of strings `{'r', 'd'}`. See Displays for lists, sets and dictionaries.
  single dispatch
A form of generic function dispatch where the implementation is chosen based on the type of a single argument.
  slice
An object of type `slice`, used to describe a portion of a sequence. A slice object is created when using the slicing form of subscript notation, with colons inside square brackets, such as in `variable_name[1:3:5]`.
  soft deprecated
A soft deprecated API should not be used in new code, but it is safe for already existing code to use it. The API remains documented and tested, but will not be enhanced further.

Soft deprecation, unlike normal deprecation, does not plan on removing the API and will not emit warnings.

See PEP 387: Soft Deprecation <https://peps.python.org/pep-0387/#soft-deprecation>.
  special method
A method that is called implicitly by Python to execute a certain operation on a type, such as addition. Such methods have names starting and ending with double underscores. Special methods are documented in Special method names.
  standard library
The collection of packages, modules and extension modules distributed as a part of the official Python interpreter package. The exact membership of the collection may vary based on platform, available system libraries, or other criteria. Documentation can be found at The Python Standard Library.

See also `sys.stdlib_module_names` for a list of all possible standard library module names.
  statement
A statement is part of a suite (a “block” of code). A statement is either an expression or one of several constructs with a keyword, such as `if`, `while` or `for`.
  static type checker
An external tool that reads Python code and analyzes it, looking for issues such as incorrect types. See also type hints and the `typing` module.
  stdlib
An abbreviation of standard library.
  strong reference
In Python’s C API, a strong reference is a reference to an object which is owned by the code holding the reference. The strong reference is taken by calling `Py_INCREF()` when the reference is created and released with `Py_DECREF()` when the reference is deleted.

The `Py_NewRef()` function can be used to create a strong reference to an object. Usually, the `Py_DECREF()` function must be called on the strong reference before exiting the scope of the strong reference, to avoid leaking one reference.

See also borrowed reference.
  subscript
The expression in square brackets of a subscription expression, for example, the `3` in `items[3]`. Usually used to select an element of a container. Also called a key when subscripting a mapping, or an index when subscripting a sequence.
  synchronization primitive
A basic building block for coordinating (synchronizing) the execution of multiple threads to ensure thread-safe access to shared resources. Python’s `threading` module provides several synchronization primitives including `Lock`, `RLock`, `Semaphore`, `Condition`, `Event`, and `Barrier`. Additionally, the `queue` module provides multi-producer, multi-consumer queues that are especially useful in multithreaded programs. These primitives help prevent race conditions and coordinate thread execution. See also lock.
  t-stringt-strings
String literals prefixed with `t` or `T` are commonly called “t-strings” which is short for template string literals.
  text encoding
A string in Python is a sequence of Unicode code points (in range `U+0000`–`U+10FFFF`). To store or transfer a string, it needs to be serialized as a sequence of bytes.

Serializing a string into a sequence of bytes is known as “encoding”, and recreating the string from the sequence of bytes is known as “decoding”.

There are a variety of different text serialization codecs, which are collectively referred to as “text encodings”.
  text file
A file object able to read and write `str` objects. Often, a text file actually accesses a byte-oriented datastream and handles the text encoding automatically. Examples of text files are files opened in text mode (`'r'` or `'w'`), `sys.stdin`, `sys.stdout`, and instances of `io.StringIO`.

See also binary file for a file object able to read and write bytes-like objects.
  thread state
The information used by the CPython runtime to run in an OS thread. For example, this includes the current exception, if any, and the state of the bytecode interpreter.

Each thread state is bound to a single OS thread, but threads may have many thread states available. At most, one of them may be attached at once.

An attached thread state is required to call most of Python’s C API, unless a function explicitly documents otherwise. The bytecode interpreter only runs under an attached thread state.

Each thread state belongs to a single interpreter, but each interpreter may have many thread states, including multiple for the same OS thread. Thread states from multiple interpreters may be bound to the same thread, but only one can be attached in that thread at any given moment.

See Thread State and the Global Interpreter Lock for more information.
  thread-safe
A module, function, or class that behaves correctly when used by multiple threads concurrently. Thread-safe code uses appropriate synchronization primitives like locks to protect shared mutable state, or is designed to avoid shared mutable state entirely. In the free-threaded build, built-in types like `dict`, `list`, and `set` use internal locking to make many operations thread-safe, although thread safety is not necessarily guaranteed. Code that is not thread-safe may experience race conditions and data races when used in multi-threaded programs.
  token
A small unit of source code, generated by the lexical analyzer (also called the _tokenizer_). Names, numbers, strings, operators, newlines and similar are represented by tokens.

The `tokenize` module exposes Python’s lexical analyzer. The `token` module contains information on the various types of tokens.
  triple-quoted string
A string which is bound by three instances of either a quotation mark (”) or an apostrophe (‘). While they don’t provide any functionality not available with single-quoted strings, they are useful for a number of reasons. They allow you to include unescaped single and double quotes within a string and they can span multiple lines without the use of the continuation character, making them especially useful when writing docstrings.
  type
The type of a Python object determines what kind of object it is; every object has a type. An object’s type is accessible as its `__class__` attribute or can be retrieved with `type(obj)`.
  type alias
A synonym for a type, created by assigning the type to an identifier.

Type aliases are useful for simplifying type hints. For example:

```go
def remove_gray_shades(
        colors: list[tuple[int, int, int]]) -> list[tuple[int, int, int]]:
    pass

```

could be made more readable like this:

```go
Color = tuple[int, int, int]

def remove_gray_shades(colors: list[Color]) -> list[Color]:
    pass

```

See `typing` and **PEP 484** <https://peps.python.org/pep-0484/>, which describe this functionality.
  type hint
An annotation that specifies the expected type for a variable, a class attribute, or a function parameter or return value.

Type hints are optional and are not enforced by Python but they are useful to static type checkers. They can also aid IDEs with code completion and refactoring.

Type hints of global variables, class attributes, and functions, but not local variables, can be accessed using `typing.get_type_hints()`.

See `typing` and **PEP 484** <https://peps.python.org/pep-0484/>, which describe this functionality.
  universal newlines
A manner of interpreting text streams in which all of the following are recognized as ending a line: the Unix end-of-line convention `'\n'`, the Windows convention `'\r\n'`, and the old Macintosh convention `'\r'`. See **PEP 278** <https://peps.python.org/pep-0278/> and **PEP 3116** <https://peps.python.org/pep-3116/>, as well as `bytes.splitlines()` for an additional use.
  variable annotation
An annotation of a variable or a class attribute.

When annotating a variable or a class attribute, assignment is optional:

```go
class C:
    field: 'annotation'

```

Variable annotations are usually used for type hints: for example this variable is expected to take `int` values:

```go
count: int = 0

```

Variable annotation syntax is explained in section Annotated assignment statements.

See function annotation, **PEP 484** <https://peps.python.org/pep-0484/> and **PEP 526** <https://peps.python.org/pep-0526/>, which describe this functionality. Also see Annotations Best Practices for best practices on working with annotations.
  virtual environment
A cooperatively isolated runtime environment that allows Python users and applications to install and upgrade Python distribution packages without interfering with the behaviour of other Python applications running on the same system.

See also `venv`.
  virtual machine
A computer defined entirely in software. Python’s virtual machine executes the bytecode emitted by the bytecode compiler.
  walrus operator
A light-hearted way to refer to the assignment expression operator `:=` because it looks a bit like a walrus if you turn your head.
  Zen of Python
Listing of Python design principles and philosophies that are helpful in understanding and using the language. The listing can be found by typing “`import this`” at the interactive prompt.
