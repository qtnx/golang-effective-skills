---
source_name: "External Linked Documentation"
source_url: "https://go.dev/design/43651-type-parameters"
source_path: "sources/raw/external/go-dev-design-43651-type-parameters-8b418b79f1.html"
license_ref: ""
---

## Design

### Generic types

We want more than just generic functions: we also want generic types. We suggest that types be extended to take type parameters.

```go
// Vector is a name for a slice of any element type.
type Vector[T any] []T

```

A type‘s type parameters are just like a function’s type parameters.

Within the type definition, the type parameters may be used like any other type.

To use a generic type, you must supply type arguments. This is called _instantiation_. The type arguments appear in square brackets, as usual. When we instantiate a type by supplying type arguments for the type parameters, we produce a type in which each use of a type parameter in the type definition is replaced by the corresponding type argument.

```go
// v is a Vector of int values.
//
// This is similar to pretending that "Vector[int]" is a valid identifier,
// and writing
//   type "Vector[int]" []int
//   var v "Vector[int]"
// All uses of Vector[int] will refer to the same "Vector[int]" type.
//
var v Vector[int]

```

Generic types can have methods. The receiver type of a method must declare the same number of type parameters as are declared in the receiver type's definition. They are declared without any constraint.

```go
// Push adds a value to the end of a vector.
func (v *Vector[T]) Push(x T) { *v = append(*v, x) }

```

The type parameters listed in a method declaration need not have the same names as the type parameters in the type declaration. In particular, if they are not used by the method, they can be `_`.

A generic type can refer to itself in cases where a type can ordinarily refer to itself, but when it does so the type arguments must be the type parameters, listed in the same order. This restriction prevents infinite recursion of type instantiation.

```go
// List is a linked list of values of type T.
type List[T any] struct {
	next *List[T] // this reference to List[T] is OK
	val  T
}

// This type is INVALID.
type P[T1, T2 any] struct {
	F *P[T2, T1] // INVALID; must be [T1, T2]
}

```

This restriction applies to both direct and indirect references.

```go
// ListHead is the head of a linked list.
type ListHead[T any] struct {
	head *ListElement[T]
}

// ListElement is an element in a linked list with a head.
// Each element points back to the head.
type ListElement[T any] struct {
	next *ListElement[T]
	val  T
	// Using ListHead[T] here is OK.
	// ListHead[T] refers to ListElement[T] refers to ListHead[T].
	// Using ListHead[int] would not be OK, as ListHead[T]
	// would have an indirect reference to ListHead[int].
	head *ListHead[T]
}

```

(Note: with more understanding of how people want to write code, it may be possible to relax this rule to permit some cases that use different type arguments.)

The type parameter of a generic type may have constraints other than `any`.

```go
// StringableVector is a slice of some type, where the type
// must have a String method.
type StringableVector[T Stringer] []T

func (s StringableVector[T]) String() string {
	var sb strings.Builder
	for i, v := range s {
		if i > 0 {
			sb.WriteString(", ")
		}
		// It's OK to call v.String here because v is of type T
		// and T's constraint is Stringer.
		sb.WriteString(v.String())
	}
	return sb.String()
}

```
