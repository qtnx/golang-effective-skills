---
source_name: "External Linked Documentation"
source_url: "https://docs.python.org/3/glossary.html"
source_path: "sources/raw/external/docs-python-org-3-glossary-html-f05d926bb6.html"
license_ref: ""
---

# Glossary

-
_positional-or-keyword_: specifies an argument that can be passed either positionally or as a keyword argument. This is the default kind of parameter, for example _foo_ and _bar_ in the following:

```go
def func(foo, bar=None): ...

```

-
_positional-only_: specifies an argument that can be supplied only by position. Positional-only parameters can be defined by including a `/` character in the parameter list of the function definition after them, for example _posonly1_ and _posonly2_ in the following:

```go
def func(posonly1, posonly2, /, positional_or_keyword): ...

```

-
_keyword-only_: specifies an argument that can be supplied only by keyword. Keyword-only parameters can be defined by including a single var-positional parameter or bare `*` in the parameter list of the function definition before them, for example _kw_only1_ and _kw_only2_ in the following:

```go
def func(arg, *, kw_only1, kw_only2): ...

```

-
_var-positional_: specifies that an arbitrary sequence of positional arguments can be provided (in addition to any positional arguments already accepted by other parameters). Such a parameter can be defined by prepending the parameter name with `*`, for example _args_ in the following:

```go
def func(*args, **kwargs): ...

```

-
_var-keyword_: specifies that arbitrarily many keyword arguments can be provided (in addition to any keyword arguments already accepted by other parameters). Such a parameter can be defined by prepending the parameter name with `**`, for example _kwargs_ in the example above.

Parameters can specify both optional and required arguments, as well as default values for some optional arguments.

See also the argument glossary entry, the FAQ question on the difference between arguments and parameters, the `inspect.Parameter` class, the Function definitions section, and **PEP 362** <https://peps.python.org/pep-0362/>.
  per-object lock
A lock associated with an individual object instance rather than a global lock shared across all objects. In free-threaded Python, built-in types like `dict` and `list` use per-object locks to allow concurrent operations on different objects while serializing operations on the same object. Operations that hold the per-object lock prevent other locking operations on the same object from proceeding, but do not block lock-free operations.
  path entry
A single location on the import path which the path based finder consults to find modules for importing.
  path entry finder
A finder returned by a callable on `sys.path_hooks` (i.e. a path entry hook) which knows how to locate modules given a path entry.

See `importlib.abc.PathEntryFinder` for the methods that path entry finders implement.
  path entry hook
A callable on the `sys.path_hooks` list which returns a path entry finder if it knows how to find modules on a specific path entry.
  path based finder
One of the default meta path finders which searches an import path for modules.
  path-like object
An object representing a file system path. A path-like object is either a `str` or `bytes` object representing a path, or an object implementing the `os.PathLike` protocol. An object that supports the `os.PathLike` protocol can be converted to a `str` or `bytes` file system path by calling the `os.fspath()` function; `os.fsdecode()` and `os.fsencode()` can be used to guarantee a `str` or `bytes` result instead, respectively. Introduced by **PEP 519** <https://peps.python.org/pep-0519/>.
  PEP
Python Enhancement Proposal. A PEP is a design document providing information to the Python community, or describing a new feature for Python or its processes or environment. PEPs should provide a concise technical specification and a rationale for proposed features.

PEPs are intended to be the primary mechanisms for proposing major new features, for collecting community input on an issue, and for documenting the design decisions that have gone into Python. The PEP author is responsible for building consensus within the community and documenting dissenting opinions.

See **PEP 1** <https://peps.python.org/pep-0001/>.
  portion
A set of files in a single directory (possibly stored in a zip file) that contribute to a namespace package, as defined in **PEP 420** <https://peps.python.org/pep-0420/>.
  positional argument
See argument.
  provisional API
A provisional API is one which has been deliberately excluded from the standard library’s backwards compatibility guarantees. While major changes to such interfaces are not expected, as long as they are marked provisional, backwards incompatible changes (up to and including removal of the interface) may occur if deemed necessary by core developers. Such changes will not be made gratuitously – they will occur only if serious fundamental flaws are uncovered that were missed prior to the inclusion of the API.

Even for provisional APIs, backwards incompatible changes are seen as a “solution of last resort” - every attempt will still be made to find a backwards compatible resolution to any identified problems.

This process allows the standard library to continue to evolve over time, without locking in problematic design errors for extended periods of time. See **PEP 411** <https://peps.python.org/pep-0411/> for more details.
  provisional package
See provisional API.
  Python 3000
Nickname for the Python 3.x release line (coined long ago when the release of version 3 was something in the distant future.) This is also abbreviated “Py3k”.
  Pythonic
An idea or piece of code which closely follows the most common idioms of the Python language, rather than implementing code using concepts common to other languages. For example, a common idiom in Python is to loop over all elements of an iterable using a `for` statement. Many other languages don’t have this type of construct, so people unfamiliar with Python sometimes use a numerical counter instead:

```go
for i in range(len(food)):
    print(food[i])

```

As opposed to the cleaner, Pythonic method:

```go
for piece in food:
    print(piece)

```

qualified name
A dotted name showing the “path” from a module’s global scope to a class, function or method defined in that module, as defined in **PEP 3155** <https://peps.python.org/pep-3155/>. For top-level functions and classes, the qualified name is the same as the object’s name:

```go
>>> class C:
...     class D:
...         def meth(self):
...             pass
...
>>> C.__qualname__
'C'
>>> C.D.__qualname__
'C.D'
>>> C.D.meth.__qualname__
'C.D.meth'

```

When used to refer to modules, the _fully qualified name_ means the entire dotted path to the module, including any parent packages, e.g. `email.mime.text`:

```go
>>> import email.mime.text
>>> email.mime.text.__name__
'email.mime.text'

```

race condition
A condition of a program where the behavior depends on the relative timing or ordering of events, particularly in multi-threaded programs. Race conditions can lead to non-deterministic behavior and bugs that are difficult to reproduce. A data race is a specific type of race condition involving unsynchronized access to shared memory. The LBYL coding style is particularly susceptible to race conditions in multi-threaded code. Using locks and other synchronization primitives helps prevent race conditions.
  reference count
The number of references to an object. When the reference count of an object drops to zero, it is deallocated. Some objects are immortal and have reference counts that are never modified, and therefore the objects are never deallocated. Reference counting is generally not visible to Python code, but it is a key element of the CPython implementation. Programmers can call the `sys.getrefcount()` function to return the reference count for a particular object.

In CPython, reference counts are not considered to be stable or well-defined values; the number of references to an object, and how that number is affected by Python code, may be different between versions.
  regular package
A traditional package, such as a directory containing an `__init__.py` file.

See also namespace package.
  reentrant
A property of a function or lock that allows it to be called or acquired multiple times by the same thread without causing errors or a deadlock.

For functions, reentrancy means the function can be safely called again before a previous invocation has completed, which is important when functions may be called recursively or from signal handlers. Thread-unsafe functions may be non-deterministic if they’re called reentrantly in a multithreaded program.

For locks, Python’s `threading.RLock` (reentrant lock) is reentrant, meaning a thread that already holds the lock can acquire it again without blocking. In contrast, `threading.Lock` is not reentrant - attempting to acquire it twice from the same thread will cause a deadlock.

See also lock and deadlock.
  REPL
An acronym for the “read–eval–print loop”, another name for the interactive interpreter shell.
  __slots__
A declaration inside a class that saves memory by pre-declaring space for instance attributes and eliminating instance dictionaries. Though popular, the technique is somewhat tricky to get right and is best reserved for rare cases where there are large numbers of instances in a memory-critical application.
  sequence
An iterable which supports efficient element access using integer indices via the `__getitem__()` special method and defines a `__len__()` method that returns the length of the sequence. Some built-in sequence types are `list`, `str`, `tuple`, and `bytes`. Note that `dict` also supports `__getitem__()` and `__len__()`, but is considered a mapping rather than a sequence because the lookups use arbitrary hashable keys rather than integers.
