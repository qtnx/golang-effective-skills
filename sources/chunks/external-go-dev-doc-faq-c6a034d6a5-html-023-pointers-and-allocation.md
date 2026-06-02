---
source_name: "External Linked Documentation"
source_url: "https://go.dev/doc/faq"
source_path: "sources/raw/external/go-dev-doc-faq-c6a034d6a5.html"
license_ref: ""
---

# Frequently Asked Questions (FAQ)

## Pointers and Allocation

### When are function parameters passed by value?

As in all languages in the C family, everything in Go is passed by value. That is, a function always gets a copy of the thing being passed, as if there were an assignment statement assigning the value to the parameter. For instance, passing an `int` value to a function makes a copy of the `int`, and passing a pointer value makes a copy of the pointer, but not the data it points to. (See a later section for a discussion of how this affects method receivers.)

Map and slice values behave like pointers: they are descriptors that contain pointers to the underlying map or slice data. Copying a map or slice value doesn’t copy the data it points to. Copying an interface value makes a copy of the thing stored in the interface value. If the interface value holds a struct, copying the interface value makes a copy of the struct. If the interface value holds a pointer, copying the interface value makes a copy of the pointer, but again not the data it points to.

Note that this discussion is about the semantics of the operations. Actual implementations may apply optimizations to avoid copying as long as the optimizations do not change the semantics.

### When should I use a pointer to an interface?

Almost never. Pointers to interface values arise only in rare, tricky situations involving disguising an interface value’s type for delayed evaluation.

It is a common mistake to pass a pointer to an interface value to a function expecting an interface. The compiler will complain about this error but the situation can still be confusing, because sometimes a pointer is necessary to satisfy an interface. The insight is that although a pointer to a concrete type can satisfy an interface, with one exception _a pointer to an interface can never satisfy an interface_.

Consider the variable declaration,

```go
var w io.Writer

```

The printing function `fmt.Fprintf` takes as its first argument a value that satisfies `io.Writer`—something that implements the canonical `Write` method. Thus we can write

```go
fmt.Fprintf(w, "hello, world\n")

```

If however we pass the address of `w`, the program will not compile.

```go
fmt.Fprintf(&w, "hello, world\n") // Compile-time error.

```

The one exception is that any value, even a pointer to an interface, can be assigned to a variable of empty interface type (`interface{}`). Even so, it’s almost certainly a mistake if the value is a pointer to an interface; the result can be confusing.

### Should I define methods on values or pointers?

```go
func (s *MyStruct) pointerMethod() { } // method on pointer
func (s MyStruct)  valueMethod()   { } // method on value

```

For programmers unaccustomed to pointers, the distinction between these two examples can be confusing, but the situation is actually very simple. When defining a method on a type, the receiver (`s` in the above examples) behaves exactly as if it were an argument to the method. Whether to define the receiver as a value or as a pointer is the same question, then, as whether a function argument should be a value or a pointer. There are several considerations.

First, and most important, does the method need to modify the receiver? If it does, the receiver _must_ be a pointer. (Slices and maps act as references, so their story is a little more subtle, but for instance to change the length of a slice in a method the receiver must still be a pointer.) In the examples above, if `pointerMethod` modifies the fields of `s`, the caller will see those changes, but `valueMethod` is called with a copy of the caller’s argument (that’s the definition of passing a value), so changes it makes will be invisible to the caller.

By the way, in Java method receivers have always been pointers, although their pointer nature is somewhat disguised (and recent developments are bringing value receivers to Java). It is the value receivers in Go that are unusual.

Second is the consideration of efficiency. If the receiver is large, a big `struct` for instance, it may be cheaper to use a pointer receiver.

Next is consistency. If some of the methods of the type must have pointer receivers, the rest should too, so the method set is consistent regardless of how the type is used. See the section on method sets for details.

For types such as basic types, slices, and small `structs`, a value receiver is very cheap so unless the semantics of the method requires a pointer, a value receiver is efficient and clear.

### What’s the difference between new and make?

In short: `new` allocates memory, while `make` initializes the slice, map, and channel types.

See the relevant section of Effective Go for more details.

### What is the size of an `int` on a 64 bit machine?

The sizes of `int` and `uint` are implementation-specific but the same as each other on a given platform. For portability, code that relies on a particular size of value should use an explicitly sized type, like `int64`. On 32-bit machines the compilers use 32-bit integers by default, while on 64-bit machines integers have 64 bits. (Historically, this was not always true.)

On the other hand, floating-point scalars and complex types are always sized (there are no `float` or `complex` basic types), because programmers should be aware of precision when using floating-point numbers. The default type used for an (untyped) floating-point constant is `float64`. Thus `foo` `:=` `3.0` declares a variable `foo` of type `float64`. For a `float32` variable initialized by an (untyped) constant, the variable type must be specified explicitly in the variable declaration:

```go
var foo float32 = 3.0

```

Alternatively, the constant must be given a type with a conversion as in `foo := float32(3.0)`.

### How do I know whether a variable is allocated on the heap or the stack?

From a correctness standpoint, you don’t need to know. Each variable in Go exists as long as there are references to it. The storage location chosen by the implementation is irrelevant to the semantics of the language.

The storage location does have an effect on writing efficient programs. When possible, the Go compilers will allocate variables that are local to a function in that function’s stack frame. However, if the compiler cannot prove that the variable is not referenced after the function returns, then the compiler must allocate the variable on the garbage-collected heap to avoid dangling pointer errors. Also, if a local variable is very large, it might make more sense to store it on the heap rather than the stack.

In the current compilers, if a variable has its address taken, that variable is a candidate for allocation on the heap. However, a basic _escape analysis_ recognizes some cases when such variables will not live past the return from the function and can reside on the stack.

### Why does my Go process use so much virtual memory?

The Go memory allocator reserves a large region of virtual memory as an arena for allocations. This virtual memory is local to the specific Go process; the reservation does not deprive other processes of memory.

To find the amount of actual memory allocated to a Go process, use the Unix `top` command and consult the `RES` (Linux) or `RSIZE` (macOS) columns.
