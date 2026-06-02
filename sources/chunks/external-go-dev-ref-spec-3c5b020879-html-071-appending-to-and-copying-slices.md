---
source_name: "External Linked Documentation"
source_url: "https://go.dev/ref/spec"
source_path: "sources/raw/external/go-dev-ref-spec-3c5b020879.html"
license_ref: ""
---

## Built-in functions
 Built-in functions are predeclared. They are called like any other function but some of them accept a type instead of an expression as the first argument.
 The built-in functions do not have standard Go types, so they can only appear in call expressions; they cannot be used as function values.
### Appending to and copying slices

 The built-in functions `append` and `copy` assist in common slice operations. For both functions, the result is independent of whether the memory referenced by the arguments overlaps.

 The variadic function `append` appends zero or more values `x` to a slice `s` of type `S` and returns the resulting slice, also of type `S`. The values `x` are passed to a parameter of type `...E` where `E` is the element type of `S` and the respective parameter passing rules apply. As a special case, `append` also accepts a slice whose type is assignable to type `[]byte` with a second argument of `string` type followed by `...`. This form appends the bytes of the string.

```go

append(s S, x ...E) S  // E is the element type of S

```

 If `S` is a type parameter, all types in its type set must have the same underlying slice type `[]E`.

 If the capacity of `s` is not large enough to fit the additional values, `append` allocates a new, sufficiently large underlying array that fits both the existing slice elements and the additional values. Otherwise, `append` re-uses the underlying array.

```go

s0 := []int{0, 0}
s1 := append(s0, 2)                // append a single element     s1 is []int{0, 0, 2}
s2 := append(s1, 3, 5, 7)          // append multiple elements    s2 is []int{0, 0, 2, 3, 5, 7}
s3 := append(s2, s0...)            // append a slice              s3 is []int{0, 0, 2, 3, 5, 7, 0, 0}
s4 := append(s3[3:6], s3[2:]...)   // append overlapping slice    s4 is []int{3, 5, 7, 2, 3, 5, 7, 0, 0}

var t []interface{}
t = append(t, 42, 3.1415, "foo")   //                             t is []interface{}{42, 3.1415, "foo"}

var b []byte
b = append(b, "bar"...)            // append string contents      b is []byte{'b', 'a', 'r' }

```

 The function `copy` copies slice elements from a source `src` to a destination `dst` and returns the number of elements copied. Both arguments must have identical element type `E` and must be assignable to a slice of type `[]E`. The number of elements copied is the minimum of `len(src)` and `len(dst)`. As a special case, `copy` also accepts a destination argument assignable to type `[]byte` with a source argument of a `string` type. This form copies the bytes from the string into the byte slice.

```go

copy(dst, src []T) int
copy(dst []byte, src string) int

```

 If the type of one or both arguments is a type parameter, all types in their respective type sets must have the same underlying slice type `[]E`.

 Examples:

```go

var a = [...]int{0, 1, 2, 3, 4, 5, 6, 7}
var s = make([]int, 6)
var b = make([]byte, 5)
n1 := copy(s, a[0:])            // n1 == 6, s is []int{0, 1, 2, 3, 4, 5}
n2 := copy(s, s[2:])            // n2 == 4, s is []int{2, 3, 4, 5, 4, 5}
n3 := copy(b, "Hello, World!")  // n3 == 5, b is []byte("Hello")

```
