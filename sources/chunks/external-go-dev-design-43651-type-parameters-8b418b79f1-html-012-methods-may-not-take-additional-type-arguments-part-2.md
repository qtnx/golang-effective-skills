---
source_name: "External Linked Documentation"
source_url: "https://go.dev/design/43651-type-parameters"
source_path: "sources/raw/external/go-dev-design-43651-type-parameters-8b418b79f1.html"
license_ref: ""
---

## Design

// ApproximateMyString is INVALID.
type ApproximateMyString interface {
	~MyString // INVALID: underlying type of MyString is not MyString
}

// ApproximateParameter is INVALID.
type ApproximateParameter[T any] interface {
	~T // INVALID: T is a type parameter
}

```
Union constraint element
The third new element we permit in a constraint is also a new syntactic construct: a union element, written as a series of constraint elements separated by vertical bars (`|`). For example: `int | float32` or `~int8 | ~int16 | ~int32 | ~int64`. The type set of a union element is the union of the type sets of each element in the sequence. The elements listed in a union must all be different. For example:

```go
// PredeclaredSignedInteger is a constraint that matches the
// five predeclared signed integer types.
type PredeclaredSignedInteger interface {
	int | int8 | int16 | int32 | int64
}

```

The type set of this union element is the set `{int, int8, int16, int32, int64}`. Since the union is the only element of `PredeclaredSignedInteger`, that is also the type set of `PredeclaredSignedInteger`. This constraint can be satisfied by any of those five types.

Here is an example using approximation elements:

```go
// SignedInteger is a constraint that matches any signed integer type.
type SignedInteger interface {
	~int | ~int8 | ~int16 | ~int32 | ~int64
}

```

The type set of this constraint is the set of all types whose underlying type is one of `int`, `int8`, `int16`, `int32`, or `int64`. Any of those types will satisfy this constraint.

The new constraint element syntax is

```go
InterfaceType  = "interface" "{" {(MethodSpec | InterfaceTypeName | ConstraintElem) ";" } "}" .
ConstraintElem = ConstraintTerm { "|" ConstraintTerm } .
ConstraintTerm = ["~"] Type .

```

#### Operations based on type sets

The purpose of type sets is to permit generic functions to use operators, such as `<`, with values whose type is a type parameter.

The rule is that a generic function may use a value whose type is a type parameter in any way that is permitted by every member of the type set of the parameter‘s constraint. This applies to operators like ‘<’ or ‘+’ or other general operators. For special purpose operators like `range` loops, we permit their use if the type parameter has a structural constraint, as defined later; the definition here is basically that the constraint has a single underlying type. If the function can be compiled successfully using each type in the constraint’s type set, or when applicable using the structural type, then the use is permitted.

For the `Smallest` example shown earlier, we could use a constraint like this:

```go
package constraints

// Ordered is a type constraint that matches any ordered type.
// An ordered type is one that supports the <, <=, >, and >= operators.
type Ordered interface {
	~int | ~int8 | ~int16 | ~int32 | ~int64 |
		~uint | ~uint8 | ~uint16 | ~uint32 | ~uint64 | ~uintptr |
		~float32 | ~float64 |
		~string
}

```

In practice this constraint would likely be defined and exported in a new standard library package, `constraints`, so that it could be used by function and type definitions.

Given that constraint, we can write this function, now valid:

```go
// Smallest returns the smallest element in a slice.
// It panics if the slice is empty.
func Smallest[T constraints.Ordered](s []T) T {
	r := s[0] // panics if slice is empty
	for _, v := range s[1:] {
		if v < r {
			r = v
		}
	}
	return r
}

```

#### Comparable types in constraints

Earlier we mentioned that there are two exceptions to the rule that operators may only be used with types that are predeclared by the language. The exceptions are `==` and `!=`, which are permitted for struct, array, and interface types. These are useful enough that we want to be able to write a constraint that accepts any comparable type.

To do this we introduce a new predeclared type constraint: `comparable`. The type set of the `comparable` constraint is the set of all comparable types. This permits the use of `==` and `!=` with values of that type parameter.

For example, this function may be instantiated with any comparable type:

```go
// Index returns the index of x in s, or -1 if not found.
func Index[T comparable](s []T, x T) int {
	for i, v := range s {
		// v and x are type T, which has the comparable
		// constraint, so we can use == here.
		if v == x {
			return i
		}
	}
	return -1
}

```

Since `comparable` is a constraint, it can be embedded in another interface type used as a constraint.

```go
// ComparableHasher is a type constraint that matches all
// comparable types with a Hash method.
type ComparableHasher interface {
	comparable
	Hash() uintptr
}

```

The constraint `ComparableHasher` is implemented by any type that is comparable and also has a `Hash() uintptr` method. A generic function that uses `ComparableHasher` as a constraint can compare values of that type and can call the `Hash` method.

It's possible to use `comparable` to produce a constraint that can not be satisfied by any type. See also the discussion of empty type sets below.

```go
// ImpossibleConstraint is a type constraint that no type can satisfy,
// because slice types are not comparable.
type ImpossibleConstraint interface {
	comparable
	[]int
}

```
