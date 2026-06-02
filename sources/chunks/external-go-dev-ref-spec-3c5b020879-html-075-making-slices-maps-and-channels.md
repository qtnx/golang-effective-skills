---
source_name: "External Linked Documentation"
source_url: "https://go.dev/ref/spec"
source_path: "sources/raw/external/go-dev-ref-spec-3c5b020879.html"
license_ref: ""
---

## Built-in functions

### Making slices, maps and channels

 The built-in function `make` takes a type `T`, which must be a slice, map or channel type, or a type parameter, optionally followed by a type-specific list of expressions. It returns a value of type `T` (not `*T`). The memory is initialized as described in the section on initial values.

```go

Call             Type T            Result

make(T, n)       slice             slice of type T with length n and capacity n
make(T, n, m)    slice             slice of type T with length n and capacity m

make(T)          map               map of type T
make(T, n)       map               map of type T with initial space for approximately n elements

make(T)          channel           unbuffered channel of type T
make(T, n)       channel           buffered channel of type T, buffer size n

make(T, n)       type parameter    see below
make(T, n, m)    type parameter    see below

```

 If the first argument is a type parameter, all types in its type set must have the same underlying type, which must be a slice or map type, or, if there are channel types, there must only be channel types, they must all have the same element type, and the channel directions must not conflict.

 Each of the size arguments `n` and `m` must be of integer type, have a type set containing only integer types, or be an untyped constant. A constant size argument must be non-negative and representable by a value of type `int`; if it is an untyped constant it is given type `int`. If both `n` and `m` are provided and are constant, then `n` must be no larger than `m`. For slices and channels, if `n` is negative or larger than `m` at run time, a run-time panic occurs.

```go

s := make([]int, 10, 100)       // slice with len(s) == 10, cap(s) == 100
s := make([]int, 1e3)           // slice with len(s) == cap(s) == 1000
s := make([]int, 1<<63)         // illegal: len(s) is not representable by a value of type int
s := make([]int, 10, 0)         // illegal: len(s) > cap(s)
c := make(chan int, 10)         // channel with a buffer size of 10
m := make(map[string]int, 100)  // map with initial space for approximately 100 elements

```

 Calling `make` with a map type and size hint `n` will create a map with initial space to hold `n` map elements. The precise behavior is implementation-dependent.
