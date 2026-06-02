---
source_name: "External Linked Documentation"
source_url: "https://go.dev/design/43651-type-parameters"
source_path: "sources/raw/external/go-dev-design-43651-type-parameters-8b418b79f1.html"
license_ref: ""
---

## Design

When a constraint embeds another constraint, the type set of the outer constraint is the intersection of all the type sets involved. If there are multiple embedded types, intersection preserves the property that any type argument must satisfy the requirements of all constraint elements.

```go
// Addable is types that support the + operator.
type Addable interface {
	~int | ~int8 | ~int16 | ~int32 | ~int64 |
		~uint | ~uint8 | ~uint16 | ~uint32 | ~uint64 | ~uintptr |
		~float32 | ~float64 | ~complex64 | ~complex128 |
		~string
}

// Byteseq is a byte sequence: either string or []byte.
type Byteseq interface {
	~string | ~[]byte
}

// AddableByteseq is a byte sequence that supports +.
// This is every type that is both Addable and Byteseq.
// In other words, just the type set ~string.
type AddableByteseq interface {
	Addable
	Byteseq
}

```

An embedded constraint may appear in a union element. The type set of the union is, as usual, the union of the type sets of the elements listed in the union.

```go
// Signed is a constraint with a type set of all signed integer
// types.
type Signed interface {
	~int | ~int8 | ~int16 | ~int32 | ~int64
}

// Unsigned is a constraint with a type set of all unsigned integer
// types.
type Unsigned interface {
	~uint | ~uint8 | ~uint16 | ~uint32 | ~uint64 | ~uintptr
}

// Integer is a constraint with a type set of all integer types.
type Integer interface {
	Signed | Unsigned
}

```

#### Interface types in union elements

We've said that the type set of a union element is the union of the type sets of all types in the union. For most types `T` the type set of `T` is simply `T` itself. For interface types (and approximation elements), however, that is not the case.

The type set of an interface type that does not embed a non-interface element is, as we said earlier, the set of all types that declare all the methods of the interface, including the interface type itself. Using such an interface type in a union element will add that type set to the union.

```go
type Stringish interface {
	string | fmt.Stringer
}

```

The type set of `Stringish` is the type `string` and all types that implement `fmt.Stringer`. Any of those types (including `fmt.Stringer` itself) will be permitted as a type argument for this constraint. No operations will be permitted for a value of a type parameter that uses `Stringish` as a constraint (other than operations supported by all types). This is because `fmt.Stringer` is in the type set of `Stringish`, and `fmt.Stringer`, an interface type, does not support any type-specific operations. The operations permitted by `Stringish` are those operations supported by all the types in the type set, including `fmt.Stringer`, so in this case there are no operations other than those supported by all types. A parameterized function that uses this constraint will have to use type assertions or reflection in order to use the values. Still, this may be useful in some cases for stronger static type checking. The main point is that it follows directly from the definition of type sets and constraint satisfaction.

#### Empty type sets

It is possible to write a constraint with an empty type set. There is no type argument that will satisfy such a constraint, so any attempt to instantiate a function that uses constraint with an empty type set will fail. It is not possible in general for the compiler to detect all such cases. Probably the vet tool should give an error for cases that it is able to detect.

```go
// Unsatisfiable is an unsatisfiable constraint with an empty type set.
// No predeclared types have any methods.
// If this used ~int | ~float32 the type set would not be empty.
type Unsatisfiable interface {
	int | float32
	String() string
}

```

#### General notes on type sets

It may seem awkward to explicitly list types in a constraint, but it is clear both as to which type arguments are permitted at the call site, and which operations are permitted by the generic function.

If the language later changes to support operator methods (there are no such plans at present), then constraints will handle them as they do any other kind of method.

There will always be a limited number of predeclared types, and a limited number of operators that those types support. Future language changes will not fundamentally change those facts, so this approach will continue to be useful.

This approach does not attempt to handle every possible operator. The expectation is that composite types will normally be handled using composite types in generic function and type declarations, rather than putting composite types in a type set. For example, we expect functions that want to index into a slice to be parameterized on the slice element type `T`, and to use parameters or variables of type `[]T`.

As shown in the `DoubleMySlice` example above, this approach makes it awkward to declare generic functions that accept and return a composite type and want to return the same result type as their argument type. Defined composite types are not common, but they do arise. This awkwardness is a weakness of this approach. Constraint type inference can help at the call site.
