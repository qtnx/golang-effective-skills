---
source_name: "External Linked Documentation"
source_url: "https://docs.python.org/3/glossary.html"
source_path: "sources/raw/external/docs-python-org-3-glossary-html-f05d926bb6.html"
license_ref: ""
---

# Glossary

In a multi-threaded environment, the LBYL approach can risk introducing a race condition between “the looking” and “the leaping”. For example, the code, `if key in mapping: return mapping[key]` can fail if another thread removes _key_ from _mapping_ after the test, but before the lookup. This issue can be solved with locks or by using the EAFP approach. See also thread-safe.
  lexical analyzer
Formal name for the _tokenizer_; see token.
  list
A built-in Python sequence. Despite its name it is more akin to an array in other languages than to a linked list since access to elements is _O_(1).
  list comprehension
A compact way to process all or part of the elements in a sequence and return a list with the results. `result = ['{:#04x}'.format(x) for x in range(256) if x % 2 == 0]` generates a list of strings containing even hex numbers (0x..) in the range from 0 to 255. The `if` clause is optional. If omitted, all elements in `range(256)` are processed.
  lock
A synchronization primitive that allows only one thread at a time to access a shared resource. A thread must acquire a lock before accessing the protected resource and release it afterward. If a thread attempts to acquire a lock that is already held by another thread, it will block until the lock becomes available. Python’s `threading` module provides `Lock` (a basic lock) and `RLock` (a reentrant lock). Locks are used to prevent race conditions and ensure thread-safe access to shared data. Alternative design patterns to locks exist such as queues, producer/consumer patterns, and thread-local state. See also deadlock, and reentrant.
  lock-free
An operation that does not acquire any lock and uses atomic CPU instructions to ensure correctness. Lock-free operations can execute concurrently without blocking each other and cannot be blocked by operations that hold locks. In free-threaded Python, built-in types like `dict` and `list` provide lock-free read operations, which means other threads may observe intermediate states during multi-step modifications even when those modifications hold the per-object lock.
  loader
An object that loads a module. It must define the `exec_module()` and `create_module()` methods to implement the `Loader` interface. A loader is typically returned by a finder. See also:

-
Finders and loaders

-
`importlib.abc.Loader`

-
**PEP 302** <https://peps.python.org/pep-0302/>

locale encoding
On Unix, it is the encoding of the LC_CTYPE locale. It can be set with `locale.setlocale(locale.LC_CTYPE, new_locale)`.

On Windows, it is the ANSI code page (ex: `"cp1252"`).

On Android and VxWorks, Python uses `"utf-8"` as the locale encoding.

`locale.getencoding()` can be used to get the locale encoding.

See also the filesystem encoding and error handler.
  magic method
An informal synonym for special method.
  mapping
A container object that supports arbitrary key lookups and implements the methods specified in the `collections.abc.Mapping` or `collections.abc.MutableMapping` abstract base classes. Examples include `dict`, `collections.defaultdict`, `collections.OrderedDict` and `collections.Counter`.
  meta path finder
A finder returned by a search of `sys.meta_path`. Meta path finders are related to, but different from path entry finders.

See `importlib.abc.MetaPathFinder` for the methods that meta path finders implement.
  metaclass
The class of a class. Class definitions create a class name, a class dictionary, and a list of base classes. The metaclass is responsible for taking those three arguments and creating the class. Most object oriented programming languages provide a default implementation. What makes Python special is that it is possible to create custom metaclasses. Most users never need this tool, but when the need arises, metaclasses can provide powerful, elegant solutions. They have been used for logging attribute access, adding thread-safety, tracking object creation, implementing singletons, and many other tasks.

More information can be found in Metaclasses.
  method
A function which is defined inside a class body. If called as an attribute of an instance of that class, the method will get the instance object as its first argument (which is usually called `self`). See function and nested scope.
  method resolution order
Method Resolution Order is the order in which base classes are searched for a member during lookup. See The Python 2.3 Method Resolution Order for details of the algorithm used by the Python interpreter since the 2.3 release.
  module
An object that serves as an organizational unit of Python code. Modules have a namespace containing arbitrary Python objects. Modules are loaded into Python by the process of importing.

See also package.
  module spec
A namespace containing the import-related information used to load a module. An instance of `importlib.machinery.ModuleSpec`.

See also Module specs.
  MRO
See method resolution order.
  mutable
An object with state that is allowed to change during the course of the program. In multi-threaded programs, mutable objects that are shared between threads require careful synchronization to avoid race conditions. See also immutable, thread-safe, and concurrent modification.
  named tuple
The term “named tuple” applies to any type or class that inherits from tuple and whose indexable elements are also accessible using named attributes. The type or class may have other features as well.

Several built-in types are named tuples, including the values returned by `time.localtime()` and `os.stat()`. Another example is `sys.float_info`:

```go
>>> sys.float_info[1]                   # indexed access
1024
>>> sys.float_info.max_exp              # named field access
1024
>>> isinstance(sys.float_info, tuple)   # kind of tuple
True

```

Some named tuples are built-in types (such as the above examples). Alternatively, a named tuple can be created from a regular class definition that inherits from `tuple` and that defines named fields. Such a class can be written by hand, or it can be created by inheriting `typing.NamedTuple`, or with the factory function `collections.namedtuple()`. The latter techniques also add some extra methods that may not be found in hand-written or built-in named tuples.
  namespace
The place where a variable is stored. Namespaces are implemented as dictionaries. There are the local, global and built-in namespaces as well as nested namespaces in objects (in methods). Namespaces support modularity by preventing naming conflicts. For instance, the functions `builtins.open` and `os.open()` are distinguished by their namespaces. Namespaces also aid readability and maintainability by making it clear which module implements a function. For instance, writing `random.seed()` or `itertools.islice()` makes it clear that those functions are implemented by the `random` and `itertools` modules, respectively.
  namespace package
A package which serves only as a container for subpackages. Namespace packages may have no physical representation, and specifically are not like a regular package because they have no `__init__.py` file.

Namespace packages allow several individually installable packages to have a common parent package. Otherwise, it is recommended to use a regular package.

For more information, see **PEP 420** <https://peps.python.org/pep-0420/> and Namespace packages.

See also module.
  native code
Code that is compiled to machine instructions and runs directly on the processor, as opposed to code that is interpreted or runs in a virtual machine. In the context of Python, native code typically refers to C, C++, Rust or Fortran code in extension modules that can be called from Python. See also extension module.
  nested scope
The ability to refer to a variable in an enclosing definition. For instance, a function defined inside another function can refer to variables in the outer function. Note that nested scopes by default work only for reference and not for assignment. Local variables both read and write in the innermost scope. Likewise, global variables read and write to the global namespace. The `nonlocal` allows writing to outer scopes.
  new-style class
Old name for the flavor of classes now used for all class objects. In earlier Python versions, only new-style classes could use Python’s newer, versatile features like `__slots__`, descriptors, properties, `__getattribute__()`, class methods, and static methods.
  non-deterministic
Behavior where the outcome of a program can vary between executions with the same inputs. In multi-threaded programs, non-deterministic behavior often results from race conditions where the relative timing or interleaving of threads affects the result. Proper synchronization using locks and other synchronization primitives helps ensure deterministic behavior.
  object
Any data with state (attributes or value) and defined behavior (methods). Also the ultimate base class of any new-style class.
  optimized scope
A scope where target local variable names are reliably known to the compiler when the code is compiled, allowing optimization of read and write access to these names. The local namespaces for functions, generators, coroutines, comprehensions, and generator expressions are optimized in this fashion. Note: most interpreter optimizations are applied to all scopes, only those relying on a known set of local and nonlocal variable names are restricted to optimized scopes.
  optional module
An extension module that is part of the standard library, but may be absent in some builds of CPython, usually due to missing third-party libraries or because the module is not available for a given platform.

See Requirements for optional modules for a list of optional modules that require third-party libraries.
  package
A Python module which can contain submodules or recursively, subpackages. Technically, a package is a Python module with a `__path__` attribute.

See also regular package and namespace package.
  parallelism
Executing multiple operations at the same time (e.g. on multiple CPU cores). In Python builds with the global interpreter lock (GIL), only one thread runs Python bytecode at a time, so taking advantage of multiple CPU cores typically involves multiple processes (e.g. `multiprocessing`) or native extensions that release the GIL. In free-threaded Python, multiple Python threads can run Python code simultaneously on different cores.
  parameter
A named entity in a function (or method) definition that specifies an argument (or in some cases, arguments) that the function can accept. There are five kinds of parameter:
