---
source_name: "External Linked Documentation"
source_url: "https://pkg.go.dev/builtin"
source_path: "sources/raw/external/pkg-go-dev-builtin-4f137aa946.html"
license_ref: ""
---

builtin package - builtin - Go Packages
## Details

-     Valid go.mod <https://cs.opensource.google/go/go/+/go1.26.3:src/go.mod> file
 The Go module system was introduced in Go 1.11 and is the official dependency management solution for Go.

-     Redistributable license
 Redistributable licenses place minimal restrictions on how software can be used, modified, and redistributed.

-     Tagged version
Modules with tagged versions give importers more predictable builds.

-     Stable version
When a project reaches major version v1 it is considered stable.

-  Learn more about best practices

## Repository
   cs.opensource.google/go/go  <https://cs.opensource.google/go/go>

##   Documentation ¶

Package builtin provides documentation for Go's predeclared identifiers. The items documented here are not actually in package builtin but their descriptions here allow godoc to present documentation for the language's special identifiers.

- Constants
- Variables
-  func append(slice []Type, elems ...Type) []Type
-  func cap(v Type) int
-  func clear[T ~[]Type | ~map[Type]Type1](t T)
-  func close(c chan<- Type)
-  func complex(r, i FloatType) ComplexType
-  func copy(dst, src []Type) int
-  func delete(m map[Type]Type1, key Type)
-  func imag(c ComplexType) FloatType
-  func len(v Type) int
-  func make(t Type, size ...IntegerType) Type
-  func max[T cmp.Ordered](x T, y ...T) T
-  func min[T cmp.Ordered](x T, y ...T) T
-  func new(TypeOrExpr) *Type
-  func panic(v any)
-  func print(args ...Type)
-  func println(args ...Type)
-  func real(c ComplexType) FloatType
-  func recover() any
-  type ComplexType
-  type FloatType
-  type IntegerType
-  type Type
-  type Type1
-  type TypeOrExpr
-  type any
-  type bool
-  type byte
-  type comparable
-  type complex64
-  type complex128
-  type error
-  type float32
-  type float64
-  type int
-  type int8
-  type int16
-  type int32
-  type int64
-  type rune
-  type string
-  type uint
-  type uint8
-  type uint16
-  type uint32
-  type uint64
-  type uintptr

View Source <https://cs.opensource.google/go/go/+/go1.26.3:src/builtin/builtin.go;l=19>
```go
const (
	true  = 0 == 0 // Untyped bool.
	false = 0 != 0 // Untyped bool.
)
```

true and false are the two untyped boolean values.
  View Source <https://cs.opensource.google/go/go/+/go1.26.3:src/builtin/builtin.go;l=109>
```go
const iota = 0 // Untyped int.

```

iota is a predeclared identifier representing the untyped integer ordinal number of the current const specification in a (usually parenthesized) const declaration. It is zero-indexed.

View Source <https://cs.opensource.google/go/go/+/go1.26.3:src/builtin/builtin.go;l=113>
```go
var nil Type // Type must be a pointer, channel, func, interface, map, or slice type

```

nil is a predeclared identifier representing the zero value for a pointer, channel, func, interface, map, or slice type.

```go
func append(slice []Type, elems ...Type) []Type
```

The append built-in function appends elements to the end of a slice. If it has sufficient capacity, the destination is resliced to accommodate the new elements. If it does not, a new underlying array will be allocated. Append returns the updated slice. It is therefore necessary to store the result of append, often in the variable holding the slice itself:

```go
slice = append(slice, elem1, elem2)
slice = append(slice, anotherSlice...)

```

As a special case, it is legal to append a string to a byte slice, like this:

```go
slice = append([]byte("hello "), "world"...)

```

```go
func cap(v Type) int
```

The cap built-in function returns the capacity of v, according to its type:

- Array: the number of elements in v (same as len(v)).
- Pointer to array: the number of elements in *v (same as len(v)).
- Slice: the maximum length the slice can reach when resliced; if v is nil, cap(v) is zero.
- Channel: the channel buffer capacity, in units of elements; if v is nil, cap(v) is zero.

For some arguments, such as a simple array expression, the result can be a constant. See the Go language specification's "Length and capacity" section for details.

```go
func clear[T ~[]Type | ~map[Type]Type1](t T)
```

The clear built-in function clears maps and slices. For maps, clear deletes all entries, resulting in an empty map. For slices, clear sets all elements up to the length of the slice to the zero value of the respective element type. If the argument type is a type parameter, the type parameter's type set must contain only map or slice types, and clear performs the operation implied by the type argument. If t is nil, clear is a no-op.

```go
func close(c chan<- Type)
```

The close built-in function closes a channel, which must be either bidirectional or send-only. It should be executed only by the sender, never the receiver, and has the effect of shutting down the channel after the last sent value is received. After the last value has been received from a closed channel c, any receive from c will succeed without blocking, returning the zero value for the channel element. The form

```go
x, ok := <-c

```

will also set ok to false for a closed and empty channel.

```go
func complex(r, i FloatType) ComplexType
```

The complex built-in function constructs a complex value from two floating-point values. The real and imaginary parts must be of the same size, either float32 or float64 (or assignable to them), and the return value will be the corresponding complex type (complex64 for float32, complex128 for float64).

```go
func copy(dst, src []Type) int
```

The copy built-in function copies elements from a source slice into a destination slice. (As a special case, it also will copy bytes from a string to a slice of bytes.) The source and destination may overlap. Copy returns the number of elements copied, which will be the minimum of len(src) and len(dst).

```go
func delete(m map[Type]Type1, key Type)
```

The delete built-in function deletes the element with the specified key (m[key]) from the map. If m is nil or there is no such element, delete is a no-op.

```go
func imag(c ComplexType) FloatType
```

The imag built-in function returns the imaginary part of the complex number c. The return value will be floating point type corresponding to the type of c.

```go
func len(v Type) int
```

The len built-in function returns the length of v, according to its type:

- Array: the number of elements in v.
- Pointer to array: the number of elements in *v (even if v is nil).
- Slice, or map: the number of elements in v; if v is nil, len(v) is zero.
- String: the number of bytes in v.
- Channel: the number of elements queued (unread) in the channel buffer; if v is nil, len(v) is zero.

For some arguments, such as a string literal or a simple array expression, the result can be a constant. See the Go language specification's "Length and capacity" section for details.

```go
func make(t Type, size ...IntegerType) Type
```

The make built-in function allocates and initializes an object of type slice, map, or chan (only). Like new, the first argument is a type, not a value. Unlike new, make's return type is the same as the type of its argument, not a pointer to it. The specification of the result depends on the type:

- Slice: The size specifies the length. The capacity of the slice is equal to its length. A second integer argument may be provided to specify a different capacity; it must be no smaller than the length. For example, make([]int, 0, 10) allocates an underlying array of size 10 and returns a slice of length 0 and capacity 10 that is backed by this underlying array.
- Map: An empty map is allocated with enough space to hold the specified number of elements. The size may be omitted, in which case a small starting size is allocated.
- Channel: The channel's buffer is initialized with the specified buffer capacity. If zero, or the size is omitted, the channel is unbuffered.

```go
func max[T cmp.Ordered](x T, y ...T) T
```

The max built-in function returns the largest value of a fixed number of arguments of cmp.Ordered types. There must be at least one argument. If T is a floating-point type and any of the arguments are NaNs, max will return NaN.

```go
func min[T cmp.Ordered](x T, y ...T) T
```

The min built-in function returns the smallest value of a fixed number of arguments of cmp.Ordered types. There must be at least one argument. If T is a floating-point type and any of the arguments are NaNs, min will return NaN.

```go
func new(TypeOrExpr) *Type
```

The built-in function new allocates a new, initialized variable and returns a pointer to it. It accepts a single argument, which may be either a type or an expression. If the argument is a type T, then new(T) allocates a variable of type T initialized to its zero value. Otherwise, the argument is an expression x and new(x) allocates a variable of the type of x initialized to the value of x. If that value is an untyped constant, it is first implicitly converted to its default type.

```go
func panic(v any)
```

The panic built-in function stops normal execution of the current goroutine. When a function F calls panic, normal execution of F stops immediately. Any functions whose execution was deferred by F are run in the usual way, and then F returns to its caller. To the caller G, the invocation of F then behaves like a call to panic, terminating G's execution and running any deferred functions. This continues until all functions in the executing goroutine have stopped, in reverse order. At that point, the program is terminated with a non-zero exit code. This termination sequence is called panicking and can be controlled by the built-in function recover.
