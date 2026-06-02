---
source_name: "External Linked Documentation"
source_url: "https://go.dev/design/43651-type-parameters"
source_path: "sources/raw/external/go-dev-design-43651-type-parameters-8b418b79f1.html"
license_ref: ""
---

## Examples

### Sets

Many people have asked for Go's builtin map type to be extended, or rather reduced, to support a set type. Here is a type-safe implementation of a set type, albeit one that uses methods rather than operators like `[]`.

```go
// Package sets implements sets of any comparable type.
package sets

// Set is a set of values.
type Set[T comparable] map[T]struct{}

// Make returns a set of some element type.
func Make[T comparable]() Set[T] {
	return make(Set[T])
}

// Add adds v to the set s.
// If v is already in s this has no effect.
func (s Set[T]) Add(v T) {
	s[v] = struct{}{}
}

// Delete removes v from the set s.
// If v is not in s this has no effect.
func (s Set[T]) Delete(v T) {
	delete(s, v)
}

// Contains reports whether v is in s.
func (s Set[T]) Contains(v T) bool {
	_, ok := s[v]
	return ok
}

// Len reports the number of elements in s.
func (s Set[T]) Len() int {
	return len(s)
}

// Iterate invokes f on each element of s.
// It's OK for f to call the Delete method.
func (s Set[T]) Iterate(f func(T)) {
	for v := range s {
		f(v)
	}
}

```

Example use:

```go
	// Create a set of ints.
	// We pass int as a type argument.
	// Then we write () because Make does not take any non-type arguments.
	// We have to pass an explicit type argument to Make.
	// Function argument type inference doesn't work because the
	// type argument to Make is only used for a result parameter type.
	s := sets.Make[int]()

	// Add the value 1 to the set s.
	s.Add(1)

	// Check that s does not contain the value 2.
	if s.Contains(2) { panic("unexpected 2") }

```

This example shows how to use this design to provide a compile-time type-safe wrapper around an existing API.
