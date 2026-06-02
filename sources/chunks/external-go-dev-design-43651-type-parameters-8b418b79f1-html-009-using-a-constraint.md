---
source_name: "External Linked Documentation"
source_url: "https://go.dev/design/43651-type-parameters"
source_path: "sources/raw/external/go-dev-design-43651-type-parameters-8b418b79f1.html"
license_ref: ""
---

## Design

### Using a constraint

For a generic function, a constraint can be thought of as the type of the type argument: a meta-type. As shown above, constraints appear in the type parameter list as the meta-type of a type parameter.

```go
// Stringify calls the String method on each element of s,
// and returns the results.
func Stringify[T Stringer](s []T) (ret []string) {
	for _, v := range s {
		ret = append(ret, v.String())
	}
	return ret
}

```

The single type parameter `T` is followed by the constraint that applies to `T`, in this case `Stringer`.

## Design

### Multiple type parameters

Although the `Stringify` example uses only a single type parameter, functions may have multiple type parameters.

```go
// Print2 has two type parameters and two non-type parameters.
func Print2[T1, T2 any](s1 []T1, s2 []T2) { ... }

```

Compare this to

```go
// Print2Same has one type parameter and two non-type parameters.
func Print2Same[T any](s1 []T, s2 []T) { ... }

```

In `Print2` `s1` and `s2` may be slices of different types. In `Print2Same` `s1` and `s2` must be slices of the same element type.

Just as each ordinary parameter may have its own type, each type parameter may have its own constraint.

```go
// Stringer is a type constraint that requires a String method.
// The String method should return a string representation of the value.
type Stringer interface {
	String() string
}

// Plusser is a type constraint that requires a Plus method.
// The Plus method is expected to add the argument to an internal
// string and return the result.
type Plusser interface {
	Plus(string) string
}

// ConcatTo takes a slice of elements with a String method and a slice
// of elements with a Plus method. The slices should have the same
// number of elements. This will convert each element of s to a string,
// pass it to the Plus method of the corresponding element of p,
// and return a slice of the resulting strings.
func ConcatTo[S Stringer, P Plusser](s []S, p []P) []string {
	r := make([]string, len(s))
	for i, v := range s {
		r[i] = p[i].Plus(v.String())
	}
	return r
}

```

A single constraint can be used for multiple type parameters, just as a single type can be used for multiple non-type function parameters. The constraint applies to each type parameter separately.

```go
// Stringify2 converts two slices of different types to strings,
// and returns the concatenation of all the strings.
func Stringify2[T1, T2 Stringer](s1 []T1, s2 []T2) string {
	r := ""
	for _, v1 := range s1 {
		r += v1.String()
	}
	for _, v2 := range s2 {
		r += v2.String()
	}
	return r
}

```
