---
source_name: "External Linked Documentation"
source_url: "https://go.dev/design/43651-type-parameters"
source_path: "sources/raw/external/go-dev-design-43651-type-parameters-8b418b79f1.html"
license_ref: ""
---

## Design

### Using types that refer to themselves in constraints

It can be useful for a generic function to require a type argument with a method whose argument is the type itself. For example, this arises naturally in comparison methods. (Note that we are talking about methods here, not operators.) Suppose we want to write an `Index` method that uses an `Equal` method to check whether it has found the desired value. We would like to write that like this:

```go
// Index returns the index of e in s, or -1 if not found.
func Index[T Equaler](s []T, e T) int {
	for i, v := range s {
		if e.Equal(v) {
			return i
		}
	}
	return -1
}

```

In order to write the `Equaler` constraint, we have to write a constraint that can refer to the type argument being passed in. The easiest way to do this is to take advantage of the fact that a constraint does not have to be a defined type, it can simply be an interface type literal. This interface type literal can then refer to the type parameter.

```go
// Index returns the index of e in s, or -1 if not found.
func Index[T interface { Equal(T) bool }](s []T, e T) int {
	// same as above
}

```

This version of `Index` would be used with a type like `equalInt` defined here:

```go
// equalInt is a version of int that implements Equaler.
type equalInt int

// The Equal method lets equalInt implement the Equaler constraint.
func (a equalInt) Equal(b equalInt) bool { return a == b }

// indexEqualInts returns the index of e in s, or -1 if not found.
func indexEqualInt(s []equalInt, e equalInt) int {
	// The type argument equalInt is shown here for clarity.
	// Function argument type inference would permit omitting it.
	return Index[equalInt](s, e)
}

```

In this example, when we pass `equalInt` to `Index`, we check whether `equalInt` implements the constraint `interface { Equal(T) bool }`. The constraint has a type parameter, so we replace the type parameter with the type argument, which is `equalInt` itself. That gives us `interface { Equal(equalInt) bool }`. The `equalInt` type has an `Equal` method with that signature, so all is well, and the compilation succeeds.
