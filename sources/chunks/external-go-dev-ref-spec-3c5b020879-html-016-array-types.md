---
source_name: "External Linked Documentation"
source_url: "https://go.dev/ref/spec"
source_path: "sources/raw/external/go-dev-ref-spec-3c5b020879.html"
license_ref: ""
---

## Types

### Array types

 An array is a numbered sequence of elements of a single type, called the element type. The number of elements is called the length of the array and is never negative.

```go

ArrayType   = "[" ArrayLength "]" ElementType .
ArrayLength = Expression .
ElementType = Type .

```

 The length is part of the array's type; it must evaluate to a non-negative constant representable by a value of type `int`. The length of array `a` can be discovered using the built-in function `len`. The elements can be addressed by integer indices 0 through `len(a)-1`. Array types are always one-dimensional but may be composed to form multi-dimensional types.

```go

[32]byte
[2*N] struct { x, y int32 }
[1000]*float64
[3][5]int
[2][2][2]float64  // same as [2]([2]([2]float64))

```

 An array type `T` may not have an element of type `T`, or of a type containing `T` as a component, directly or indirectly, if those containing types are only array or struct types.

```go

// invalid array types
type (
	T1 [10]T1                 // element type of T1 is T1
	T2 [10]struct{ f T2 }     // T2 contains T2 as component of a struct
	T3 [10]T4                 // T3 contains T3 as component of a struct in T4
	T4 struct{ f T3 }         // T4 contains T4 as component of array T3 in a struct
)

// valid array types
type (
	T5 [10]*T5                // T5 contains T5 as component of a pointer
	T6 [10]func() T6          // T6 contains T6 as component of a function type
	T7 [10]struct{ f []T7 }   // T7 contains T7 as component of a slice in a struct
)

```
