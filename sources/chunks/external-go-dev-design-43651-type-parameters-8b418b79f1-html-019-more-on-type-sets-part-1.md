---
source_name: "External Linked Documentation"
source_url: "https://go.dev/design/43651-type-parameters"
source_path: "sources/raw/external/go-dev-design-43651-type-parameters-8b418b79f1.html"
license_ref: ""
---

## Design

### More on type sets

Let's return now to type sets to cover some less important details that are still worth noting.

#### Both elements and methods in constraints

As seen earlier for `Setter2`, a constraint may use both constraint elements and methods.

```go
// StringableSignedInteger is a type constraint that matches any
// type that is both 1) defined as a signed integer type;
// 2) has a String method.
type StringableSignedInteger interface {
	~int | ~int8 | ~int16 | ~int32 | ~int64
	String() string
}

```

The rules for type sets define what this means. The type set of the union element is the set of all types whose underlying type is one of the predeclared signed integer types. The type set of `String() string` is the set of all types that define that method. The type set of `StringableSignedInteger` is the intersection of those two type sets. The result is the set of all types whose underlying type is one of the predeclared signed integer types and that defines the method `String() string`. A function that uses a parameterized type `P` that uses `StringableSignedInteger` as a constraint may use the operations permitted for any integer type (`+`, `*`, and so forth) on a value of type `P`. It may also call the `String` method on a value of type `P` to get back a `string`.

It's worth noting that the `~` is essential here. The `StringableSignedInteger` constraint uses `~int`, not `int`. The type `int` would not itself be permitted as a type argument, since `int` does not have a `String` method. An example of a type argument that would be permitted is `MyInt`, defined as:

```go
// MyInt is a stringable int.
type MyInt int

// The String method returns a string representation of mi.
func (mi MyInt) String() string {
	return fmt.Sprintf("MyInt(%d)", mi)
}

```

#### Composite types in constraints

As we've seen in some earlier examples, a constraint element may be a type literal.

```go
type byteseq interface {
	string | []byte
}

```

The usual rules apply: the type argument for this constraint may be `string` or `[]byte`; a generic function with this constraint may use any operation permitted by both `string` and `[]byte`.

The `byteseq` constraint permits writing generic functions that work for either `string` or `[]byte` types.

```go
// Join concatenates the elements of its first argument to create a
// single value. sep is placed between elements in the result.
// Join works for string and []byte types.
func Join[T byteseq](a []T, sep T) (ret T) {
	if len(a) == 0 {
		// Use the result parameter as a zero value;
		// see discussion of zero value in the Issues section.
		return ret
	}
	if len(a) == 1 {
		// We know that a[0] is either a string or a []byte.
		// We can append either a string or a []byte to a []byte,
		// producing a []byte. We can convert that []byte to
		// either a []byte (a no-op conversion) or a string.
		return T(append([]byte(nil), a[0]...))
	}
	// We can call len on sep because we can call len
	// on both string and []byte.
	n := len(sep) * (len(a) - 1)
	for _, v := range a {
		// Another case where we call len on string or []byte.
		n += len(v)
	}

b := make([]byte, n)
	// We can call copy to a []byte with an argument of
	// either string or []byte.
	bp := copy(b, a[0])
	for _, s := range a[1:] {
		bp += copy(b[bp:], sep)
		bp += copy(b[bp:], s)
	}
	// As above, we can convert b to either []byte or string.
	return T(b)
}

```

For composite types (string, pointer, array, slice, struct, function, map, channel) we impose an additional restriction: an operation may only be used if the operator accepts identical input types (if any) and produces identical result types for all of the types in the type set. To be clear, this additional restriction is only imposed when a composite type appears in a type set. It does not apply when a composite type is formed from a type parameter outside of a type set, as in `var v []T` for some type parameter `T`.

```go
// structField is a type constraint whose type set consists of some
// struct types that all have a field named x.
type structField interface {
	struct { a int; x int } |
		struct { b int; x float64 } |
		struct { c int; x uint64 }
}

// This function is INVALID.
func IncrementX[T structField](p *T) {
	v := p.x // INVALID: type of p.x is not the same for all types in set
	v++
	p.x = v
}

// sliceOrMap is a type constraint for a slice or a map.
type sliceOrMap interface {
	[]int | map[int]int
}

// Entry returns the i'th entry in a slice or the value of a map
// at key i. This is valid as the result of the operator is always int.
func Entry[T sliceOrMap](c T, i int) int {
	// This is either a slice index operation or a map key lookup.
	// Either way, the index and result types are type int.
	return c[i]
}

// sliceOrFloatMap is a type constraint for a slice or a map.
type sliceOrFloatMap interface {
	[]int | map[float64]int
}

// This function is INVALID.
// In this example the input type of the index operation is either
// int (for a slice) or float64 (for a map), so the operation is
// not permitted.
func FloatEntry[T sliceOrFloatMap](c T) int {
	return c[1.0] // INVALID: input type is either int or float64.
}

```

Imposing this restriction makes it easier to reason about the type of some operation in a generic function. It avoids introducing the notion of a value with a constructed type set based on applying some operation to each element of a type set.

(Note: with more understanding of how people want to write code, it may be possible to relax this restriction in the future.)

#### Type parameters in type sets

A type literal in a constraint element can refer to type parameters of the constraint. In this example, the generic function `Map` takes two type parameters. The first type parameter is required to have an underlying type that is a slice of the second type parameter. There are no constraints on the second type parameter.

```go
// SliceConstraint is a type constraint that matches a slice of
// the type parameter.
type SliceConstraint[T any] interface {
	~[]T
}

// Map takes a slice of some element type and a transformation function,
// and returns a slice of the function applied to each element.
// Map returns a slice that is the same type as its slice argument,
// even if that is a defined type.
func Map[S SliceConstraint[E], E any](s S, f func(E) E) S {
	r := make(S, len(s))
	for i, v := range s {
		r[i] = f(v)
	}
	return r
}

// MySlice is a simple defined type.
type MySlice []int

// DoubleMySlice takes a value of type MySlice and returns a new
// MySlice value with each element doubled in value.
func DoubleMySlice(s MySlice) MySlice {
	// The type arguments listed explicitly here could be inferred.
	v := Map[MySlice, int](s, func(e int) int { return 2 * e })
	// Here v has type MySlice, not type []int.
	return v
}

```

We showed other examples of this earlier in the discussion of constraint type inference.

#### Type conversions

In a function with two type parameters `From` and `To`, a value of type `From` may be converted to a value of type `To` if all the types in the type set of `From`'s constraint can be converted to all the types in the type set of `To`'s constraint.

This is a consequence of the general rule that a generic function may use any operation that is permitted by all types listed in the type set.

For example:

```go
type integer interface {
	~int | ~int8 | ~int16 | ~int32 | ~int64 |
		~uint | ~uint8 | ~uint16 | ~uint32 | ~uint64 | ~uintptr
}

func Convert[To, From integer](from From) To {
	to := To(from)
	if From(to) != from {
		panic("conversion out of range")
	}
	return to
}

```

The type conversions in `Convert` are permitted because Go permits every integer type to be converted to every other integer type.

#### Untyped constants

Some functions use untyped constants. An untyped constant is permitted with a value of a type parameter if it is permitted with every type in the type set of the type parameter's constraint.

As with type conversions, this is a consequence of the general rule that a generic function may use any operation that is permitted by all types in the type set.

```go
type integer interface {
	~int | ~int8 | ~int16 | ~int32 | ~int64 |
		~uint | ~uint8 | ~uint16 | ~uint32 | ~uint64 | ~uintptr
}

func Add10[T integer](s []T) {
	for i, v := range s {
		s[i] = v + 10 // OK: 10 can convert to any integer type
	}
}

// This function is INVALID.
func Add1024[T integer](s []T) {
	for i, v := range s {
		s[i] = v + 1024 // INVALID: 1024 not permitted by int8/uint8
	}
}

```

#### Type sets of embedded constraints
