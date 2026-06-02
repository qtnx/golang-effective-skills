---
source_name: "External Linked Documentation"
source_url: "https://go.dev/ref/spec"
source_path: "sources/raw/external/go-dev-ref-spec-3c5b020879.html"
license_ref: ""
---

## Types

### Boolean types

 A _boolean type_ represents the set of Boolean truth values denoted by the predeclared constants `true` and `false`. The predeclared boolean type is `bool`; it is a defined type.

## Types

### Numeric types

 An _integer_, _floating-point_, or _complex_ type represents the set of integer, floating-point, or complex values, respectively. They are collectively called _numeric types_. The predeclared architecture-independent numeric types are:

```go

uint8       the set of all unsigned  8-bit integers (0 to 255)
uint16      the set of all unsigned 16-bit integers (0 to 65535)
uint32      the set of all unsigned 32-bit integers (0 to 4294967295)
uint64      the set of all unsigned 64-bit integers (0 to 18446744073709551615)

int8        the set of all signed  8-bit integers (-128 to 127)
int16       the set of all signed 16-bit integers (-32768 to 32767)
int32       the set of all signed 32-bit integers (-2147483648 to 2147483647)
int64       the set of all signed 64-bit integers (-9223372036854775808 to 9223372036854775807)

float32     the set of all IEEE 754 32-bit floating-point numbers
float64     the set of all IEEE 754 64-bit floating-point numbers

complex64   the set of all complex numbers with float32 real and imaginary parts
complex128  the set of all complex numbers with float64 real and imaginary parts

byte        alias for uint8
rune        alias for int32

```

 The value of an _n_-bit integer is _n_ bits wide and represented using two's complement arithmetic <https://en.wikipedia.org/wiki/Two's_complement>.

 There is also a set of predeclared integer types with implementation-specific sizes:

```go

uint     either 32 or 64 bits
int      same size as uint
uintptr  an unsigned integer large enough to store the uninterpreted bits of a pointer value

```

 To avoid portability issues all numeric types are defined types and thus distinct except `byte`, which is an alias for `uint8`, and `rune`, which is an alias for `int32`. Explicit conversions are required when different numeric types are mixed in an expression or assignment. For instance, `int32` and `int` are not the same type even though they may have the same size on a particular architecture.
