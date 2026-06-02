---
source_name: "External Linked Documentation"
source_url: "https://go.dev/ref/spec"
source_path: "sources/raw/external/go-dev-ref-spec-3c5b020879.html"
license_ref: ""
---

# The Go Programming Language Specification

## System considerations

### Package `unsafe`

 The built-in package `unsafe`, known to the compiler and accessible through the import path `"unsafe"`, provides facilities for low-level programming including operations that violate the type system. A package using `unsafe` must be vetted manually for type safety and may not be portable. The package provides the following interface:

```go

package unsafe

type ArbitraryType int  // shorthand for an arbitrary Go type; it is not a real type
type Pointer *ArbitraryType

func Alignof(variable ArbitraryType) uintptr
func Offsetof(selector ArbitraryType) uintptr
func Sizeof(variable ArbitraryType) uintptr

type IntegerType int  // shorthand for an integer type; it is not a real type
func Add(ptr Pointer, len IntegerType) Pointer
func Slice(ptr *ArbitraryType, len IntegerType) []ArbitraryType
func SliceData(slice []ArbitraryType) *ArbitraryType
func String(ptr *byte, len IntegerType) string
func StringData(str string) *byte

```

 A `Pointer` is a pointer type but a `Pointer` value may not be dereferenced. Any pointer or value of underlying type `uintptr` can be converted to a type of underlying type `Pointer` and vice versa. If the respective types are type parameters, all types in their respective type sets must have the same underlying type, which must be `uintptr` and `Pointer`, respectively. The effect of converting between `Pointer` and `uintptr` is implementation-defined.

```go

var f float64
bits = *(*uint64)(unsafe.Pointer(&f))

type ptr unsafe.Pointer
bits = *(*uint64)(ptr(&f))

func f[P ~*B, B any](p P) uintptr {
	return uintptr(unsafe.Pointer(p))
}

var p ptr = nil

```

 The functions `Alignof` and `Sizeof` take an expression `x` of any type and return the alignment or size, respectively, of a hypothetical variable `v` as if `v` were declared via `var v = x`.

 The function `Offsetof` takes a (possibly parenthesized) selector `s.f`, denoting a field `f` of the struct denoted by `s` or `*s`, and returns the field offset in bytes relative to the struct's address. If `f` is an embedded field, it must be reachable without pointer indirections through fields of the struct. For a struct `s` with field `f`:

```go

uintptr(unsafe.Pointer(&s)) + unsafe.Offsetof(s.f) == uintptr(unsafe.Pointer(&s.f))

```

 Computer architectures may require memory addresses to be _aligned_; that is, for addresses of a variable to be a multiple of a factor, the variable's type's _alignment_. The function `Alignof` takes an expression denoting a variable of any type and returns the alignment of the (type of the) variable in bytes. For a variable `x`:

```go

uintptr(unsafe.Pointer(&x)) % unsafe.Alignof(x) == 0

```

 A (variable of) type `T` has _variable size_ if `T` is a type parameter, or if it is an array or struct type containing elements or fields of variable size. Otherwise the size is _constant_. Calls to `Alignof`, `Offsetof`, and `Sizeof` are compile-time constant expressions of type `uintptr` if their arguments (or the struct `s` in the selector expression `s.f` for `Offsetof`) are types of constant size.

 The function `Add` adds `len` to `ptr` and returns the updated pointer `unsafe.Pointer(uintptr(ptr) + uintptr(len))` [Go 1.17]. The `len` argument must be of integer type or an untyped constant. A constant `len` argument must be representable by a value of type `int`; if it is an untyped constant it is given type `int`. The rules for valid uses of `Pointer` still apply.

 The function `Slice` returns a slice whose underlying array starts at `ptr` and whose length and capacity are `len`. `Slice(ptr, len)` is equivalent to

```go

(*[len]ArbitraryType)(unsafe.Pointer(ptr))[:]

```

 except that, as a special case, if `ptr` is `nil` and `len` is zero, `Slice` returns `nil` [Go 1.17].

 The `len` argument must be of integer type or an untyped constant. A constant `len` argument must be non-negative and representable by a value of type `int`; if it is an untyped constant it is given type `int`. At run time, if `len` is negative, or if `ptr` is `nil` and `len` is not zero, a run-time panic occurs [Go 1.17].

 The function `SliceData` returns a pointer to the underlying array of the `slice` argument. If the slice's capacity `cap(slice)` is not zero, that pointer is `&slice;[:1][0]`. If `slice` is `nil`, the result is `nil`. Otherwise it is a non-`nil` pointer to an unspecified memory address [Go 1.20].

 The function `String` returns a `string` value whose underlying bytes start at `ptr` and whose length is `len`. The same requirements apply to the `ptr` and `len` argument as in the function `Slice`. If `len` is zero, the result is the empty string `""`. Since Go strings are immutable, the bytes passed to `String` must not be modified afterwards. [Go 1.20]

 The function `StringData` returns a pointer to the underlying bytes of the `str` argument. For an empty string the return value is unspecified, and may be `nil`. Since Go strings are immutable, the bytes returned by `StringData` must not be modified [Go 1.20].

### Size and alignment guarantees

 For the numeric types, the following sizes are guaranteed:

```go

type                                 size in bytes

byte, uint8, int8                     1
uint16, int16                         2
uint32, int32, float32                4
uint64, int64, float64, complex64     8
complex128                           16

```

 The following minimal alignment properties are guaranteed:

- For a variable `x` of any type: `unsafe.Alignof(x)` is at least 1.
- For a variable `x` of struct type: `unsafe.Alignof(x)` is the largest of all the values `unsafe.Alignof(x.f)` for each field `f` of `x`, but at least 1.
- For a variable `x` of array type: `unsafe.Alignof(x)` is the same as the alignment of a variable of the array's element type.

 A struct or array type has size zero if it contains no fields (or elements, respectively) that have a size greater than zero. Two distinct zero-size variables may have the same address in memory.
