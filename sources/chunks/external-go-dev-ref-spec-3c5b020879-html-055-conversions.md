---
source_name: "External Linked Documentation"
source_url: "https://go.dev/ref/spec"
source_path: "sources/raw/external/go-dev-ref-spec-3c5b020879.html"
license_ref: ""
---

## Expressions

### Conversions

 A conversion changes the type of an expression to the type specified by the conversion. A conversion may appear literally in the source, or it may be _implied_ by the context in which an expression appears.

 An _explicit_ conversion is an expression of the form `T(x)` where `T` is a type and `x` is an expression that can be converted to type `T`.

```go

Conversion = Type "(" Expression [ "," ] ")" .

```

 If the type starts with the operator `*` or `<-`, or if the type starts with the keyword `func` and has no result list, it must be parenthesized when necessary to avoid ambiguity:

```go

*Point(p)        // same as *(Point(p))
(*Point)(p)      // p is converted to *Point
<-chan int(c)    // same as <-(chan int(c))
(<-chan int)(c)  // c is converted to <-chan int
func()(x)        // function signature func() x
(func())(x)      // x is converted to func()
(func() int)(x)  // x is converted to func() int
func() int(x)    // x is converted to func() int (unambiguous)

```

 A constant value `x` can be converted to type `T` if `x` is representable by a value of `T`. As a special case, an integer constant `x` can be explicitly converted to a string type using the same rule as for non-constant `x`.

 Converting a constant to a type that is not a type parameter yields a typed constant.

```go

uint(iota)               // iota value of type uint
float32(2.718281828)     // 2.718281828 of type float32
complex128(1)            // 1.0 + 0.0i of type complex128
float32(0.49999999)      // 0.5 of type float32
float64(-1e-1000)        // 0.0 of type float64
string('x')              // "x" of type string
string(0x266c)           // "♬" of type string
myString("foo" + "bar")  // "foobar" of type myString
string([]byte{'a'})      // not a constant: []byte{'a'} is not a constant
(*int)(nil)              // not a constant: nil is not a constant, *int is not a boolean, numeric, or string type
int(1.2)                 // illegal: 1.2 cannot be represented as an int
string(65.0)             // illegal: 65.0 is not an integer constant

```

 Converting a constant to a type parameter yields a _non-constant_ value of that type, with the value represented as a value of the type argument that the type parameter is instantiated with. For example, given the function:

```go

func f[P ~float32|~float64]() {
	… P(1.1) …
}

```

 the conversion `P(1.1)` results in a non-constant value of type `P` and the value `1.1` is represented as a `float32` or a `float64` depending on the type argument for `f`. Accordingly, if `f` is instantiated with a `float32` type, the numeric value of the expression `P(1.1) + 1.2` will be computed with the same precision as the corresponding non-constant `float32` addition.

 A non-constant value `x` can be converted to type `T` in any of these cases:

-  `x` is assignable to `T`.
-  ignoring struct tags (see below), `x`'s type and `T` are not type parameters but have identical underlying types.
-  ignoring struct tags (see below), `x`'s type and `T` are pointer types that are not named types, and their pointer base types are not type parameters but have identical underlying types.
-  `x`'s type and `T` are both integer or floating point types.
-  `x`'s type and `T` are both complex types.
-  `x` is an integer or a slice of bytes or runes and `T` is a string type.
-  `x` is a string and `T` is a slice of bytes or runes.
-  `x` is a slice, `T` is an array [Go 1.20] or a pointer to an array [Go 1.17], and the slice and array types have identical element types.

 Additionally, if `T` or `x`'s type `V` are type parameters, `x` can also be converted to type `T` if one of the following conditions applies:

-  Both `V` and `T` are type parameters and a value of each type in `V`'s type set can be converted to each type in `T`'s type set.
-  Only `V` is a type parameter and a value of each type in `V`'s type set can be converted to `T`.
-  Only `T` is a type parameter and `x` can be converted to each type in `T`'s type set.

 Struct tags are ignored when comparing struct types for identity for the purpose of conversion:

```go

type Person struct {
	Name    string
	Address *struct {
		Street string
		City   string
	}
}

var data *struct {
	Name    string `json:"name"`
	Address *struct {
		Street string `json:"street"`
		City   string `json:"city"`
	} `json:"address"`
}

var person = (*Person)(data)  // ignoring tags, the underlying types are identical

```

 Specific rules apply to (non-constant) conversions between numeric types or to and from a string type. These conversions may change the representation of `x` and incur a run-time cost. All other conversions only change the type but not the representation of `x`.

 There is no linguistic mechanism to convert between pointers and integers. The package `unsafe` implements this functionality under restricted circumstances.

#### Conversions between numeric types

 For the conversion of non-constant numeric values, the following rules apply:

-  When converting between integer types, if the value is a signed integer, it is sign extended to implicit infinite precision; otherwise it is zero extended. It is then truncated to fit in the result type's size. For example, if `v := uint16(0x10F0)`, then `uint32(int8(v)) == 0xFFFFFFF0`. The conversion always yields a valid value; there is no indication of overflow.
-  When converting a floating-point number to an integer, the fraction is discarded (truncation towards zero).
-  When converting an integer or floating-point number to a floating-point type, or a complex number to another complex type, the result value is rounded to the precision specified by the destination type. For instance, the value of a variable `x` of type `float32` may be stored using additional precision beyond that of an IEEE 754 32-bit number, but float32(x) represents the result of rounding `x`'s value to 32-bit precision. Similarly, `x + 0.1` may use more than 32 bits of precision, but `float32(x + 0.1)` does not.

 In all non-constant conversions involving floating-point or complex values, if the result type cannot represent the value the conversion succeeds but the result value is implementation-dependent.

#### Conversions to and from a string type

-  Converting a slice of bytes to a string type yields a string whose successive bytes are the elements of the slice.
```go

string([]byte{'h', 'e', 'l', 'l', '\xc3', '\xb8'})   // "hellø"
string([]byte{})                                     // ""
string([]byte(nil))                                  // ""

type bytes []byte
string(bytes{'h', 'e', 'l', 'l', '\xc3', '\xb8'})    // "hellø"

type myByte byte
string([]myByte{'w', 'o', 'r', 'l', 'd', '!'})       // "world!"
myString([]myByte{'\xf0', '\x9f', '\x8c', '\x8d'})   // "🌍"

```

-  Converting a slice of runes to a string type yields a string that is the concatenation of the individual rune values converted to strings.
```go

string([]rune{0x767d, 0x9d6c, 0x7fd4})   // "\u767d\u9d6c\u7fd4" == "白鵬翔"
string([]rune{})                         // ""
string([]rune(nil))                      // ""

type runes []rune
string(runes{0x767d, 0x9d6c, 0x7fd4})    // "\u767d\u9d6c\u7fd4" == "白鵬翔"

type myRune rune
string([]myRune{0x266b, 0x266c})         // "\u266b\u266c" == "♫♬"
myString([]myRune{0x1f30e})              // "\U0001f30e" == "🌎"

```

-  Converting a value of a string type to a slice of bytes type yields a non-nil slice whose successive elements are the bytes of the string. The capacity of the resulting slice is implementation-specific and may be larger than the slice length.
```go

[]byte("hellø")             // []byte{'h', 'e', 'l', 'l', '\xc3', '\xb8'}
[]byte("")                  // []byte{}

bytes("hellø")              // []byte{'h', 'e', 'l', 'l', '\xc3', '\xb8'}

[]myByte("world!")          // []myByte{'w', 'o', 'r', 'l', 'd', '!'}
[]myByte(myString("🌏"))    // []myByte{'\xf0', '\x9f', '\x8c', '\x8f'}

```

-  Converting a value of a string type to a slice of runes type yields a slice containing the individual Unicode code points of the string. The capacity of the resulting slice is implementation-specific and may be larger than the slice length.
```go

[]rune(myString("白鵬翔"))   // []rune{0x767d, 0x9d6c, 0x7fd4}
[]rune("")                  // []rune{}

runes("白鵬翔")              // []rune{0x767d, 0x9d6c, 0x7fd4}

[]myRune("♫♬")              // []myRune{0x266b, 0x266c}
[]myRune(myString("🌐"))    // []myRune{0x1f310}

```

-  Finally, for historical reasons, an integer value may be converted to a string type. This form of conversion yields a string containing the (possibly multi-byte) UTF-8 representation of the Unicode code point with the given integer value. Values outside the range of valid Unicode code points are converted to `"\uFFFD"`.
```go

string('a')          // "a"
string(65)           // "A"
string('\xf8')       // "\u00f8" == "ø" == "\xc3\xb8"
string(-1)           // "\ufffd" == "\xef\xbf\xbd"

type myString string
myString('\u65e5')   // "\u65e5" == "日" == "\xe6\x97\xa5"

```
 Note: This form of conversion may eventually be removed from the language. The `go vet` tool flags certain integer-to-string conversions as potential errors. Library functions such as `utf8.AppendRune` or `utf8.EncodeRune` should be used instead.

#### Conversions from slice to array or array pointer

 Converting a slice to an array yields an array containing the elements of the underlying array of the slice. Similarly, converting a slice to an array pointer yields a pointer to the underlying array of the slice. In both cases, if the length of the slice is less than the length of the array, a run-time panic occurs.

```go

s := make([]byte, 2, 4)

a0 := [0]byte(s)
a1 := [1]byte(s[1:])     // a1[0] == s[1]
a2 := [2]byte(s)         // a2[0] == s[0]
a4 := [4]byte(s)         // panics: len([4]byte) > len(s)

s0 := (*[0]byte)(s)      // s0 != nil
s1 := (*[1]byte)(s[1:])  // &s1[0] == &s[1]
s2 := (*[2]byte)(s)      // &s2[0] == &s[0]
s4 := (*[4]byte)(s)      // panics: len([4]byte) > len(s)

var t []string
t0 := [0]string(t)       // ok for nil slice t
t1 := (*[0]string)(t)    // t1 == nil
t2 := (*[1]string)(t)    // panics: len([1]string) > len(t)

u := make([]byte, 0)
u0 := (*[0]byte)(u)      // u0 != nil

```
