---
source_name: "External Linked Documentation"
source_url: "https://pkg.go.dev/builtin"
source_path: "sources/raw/external/pkg-go-dev-builtin-4f137aa946.html"
license_ref: ""
---

Starting in Go 1.21, calling panic with a nil interface value or an untyped nil causes a run-time error (a different panic). The GODEBUG setting panicnil=1 disables the run-time error.

```go
func print(args ...Type)
```

The print built-in function formats its arguments in an implementation-specific way and writes the result to standard error. Print is useful for bootstrapping and debugging; it is not guaranteed to stay in the language.

```go
func println(args ...Type)
```

The println built-in function formats its arguments in an implementation-specific way and writes the result to standard error. Spaces are always added between arguments and a newline is appended. Println is useful for bootstrapping and debugging; it is not guaranteed to stay in the language.

```go
func real(c ComplexType) FloatType
```

The real built-in function returns the real part of the complex number c. The return value will be floating point type corresponding to the type of c.

```go
func recover() any
```

The recover built-in function allows a program to manage behavior of a panicking goroutine. Executing a call to recover inside a deferred function (but not any function called by it) stops the panicking sequence by restoring normal execution and retrieves the error value passed to the call of panic. If recover is called outside the deferred function it will not stop a panicking sequence. In this case, or when the goroutine is not panicking, recover returns nil.

Prior to Go 1.21, recover would also return nil if panic is called with a nil argument. See [panic] for details.

```go
type ComplexType complex64
```

ComplexType is here for the purposes of documentation only. It is a stand-in for either complex type: complex64 or complex128.

```go
type FloatType float32
```

FloatType is here for the purposes of documentation only. It is a stand-in for either float type: float32 or float64.

```go
type IntegerType int
```

IntegerType is here for the purposes of documentation only. It is a stand-in for any integer type: int, uint, int8 etc.

```go
type Type int
```

Type is here for the purposes of documentation only. It is a stand-in for any Go type, but represents the same type for any given function invocation.

```go
type Type1 int
```

Type1 is here for the purposes of documentation only. It is a stand-in for any Go type, but represents the same type for any given function invocation.

```go
type TypeOrExpr int
```

TypeOrExpr is here for the purposes of documentation only. It is a stand-in for either a Go type or an expression.

```go
type any = interface{}
```

any is an alias for interface{} and is equivalent to interface{} in all ways.

```go
type bool bool
```

bool is the set of boolean values, true and false.

```go
type byte = uint8
```

byte is an alias for uint8 and is equivalent to uint8 in all ways. It is used, by convention, to distinguish byte values from 8-bit unsigned integer values.

```go
type comparable interface{ comparable }
```

comparable is an interface that is implemented by all comparable types (booleans, numbers, strings, pointers, channels, arrays of comparable types, structs whose fields are all comparable types). The comparable interface may only be used as a type parameter constraint, not as the type of a variable.

```go
type complex64 complex64
```

complex64 is the set of all complex numbers with float32 real and imaginary parts.

```go
type complex128 complex128
```

complex128 is the set of all complex numbers with float64 real and imaginary parts.

```go
type error interface {
	Error() string
}
```

The error built-in interface type is the conventional interface for representing an error condition, with the nil value representing no error.

```go
type float32 float32
```

float32 is the set of all IEEE 754 32-bit floating-point numbers.

```go
type float64 float64
```

float64 is the set of all IEEE 754 64-bit floating-point numbers.

```go
type int int
```

int is a signed integer type that is at least 32 bits in size. It is a distinct type, however, and not an alias for, say, int32.

```go
type int8 int8
```

int8 is the set of all signed 8-bit integers. Range: -128 through 127.

```go
type int16 int16
```

int16 is the set of all signed 16-bit integers. Range: -32768 through 32767.

```go
type int32 int32
```

int32 is the set of all signed 32-bit integers. Range: -2147483648 through 2147483647.

```go
type int64 int64
```

int64 is the set of all signed 64-bit integers. Range: -9223372036854775808 through 9223372036854775807.

```go
type rune = int32
```

rune is an alias for int32 and is equivalent to int32 in all ways. It is used, by convention, to distinguish character values from integer values.

```go
type string string
```

string is the set of all strings of 8-bit bytes, conventionally but not necessarily representing UTF-8-encoded text. A string may be empty, but not nil. Values of string type are immutable.

```go
type uint uint
```

uint is an unsigned integer type that is at least 32 bits in size. It is a distinct type, however, and not an alias for, say, uint32.

```go
type uint8 uint8
```

uint8 is the set of all unsigned 8-bit integers. Range: 0 through 255.

```go
type uint16 uint16
```

uint16 is the set of all unsigned 16-bit integers. Range: 0 through 65535.

```go
type uint32 uint32
```

uint32 is the set of all unsigned 32-bit integers. Range: 0 through 4294967295.

```go
type uint64 uint64
```

uint64 is the set of all unsigned 64-bit integers. Range: 0 through 18446744073709551615.

```go
type uintptr uintptr
```

uintptr is an integer type that is large enough to hold the bit pattern of any pointer.

##   Source Files ¶
 View all Source files <https://cs.opensource.google/go/go/+/go1.26.3:src/builtin>

- builtin.go <https://cs.opensource.google/go/go/+/go1.26.3:src/builtin/builtin.go>

Click to show internal directories.
  Click to hide internal directories.

Close

**?** : This menu   **/** : Search site   **f** or **F** : Jump to   **y** or **Y**  : Canonical URL
  Close
