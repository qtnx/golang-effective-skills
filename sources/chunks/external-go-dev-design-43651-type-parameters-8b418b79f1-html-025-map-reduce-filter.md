---
source_name: "External Linked Documentation"
source_url: "https://go.dev/design/43651-type-parameters"
source_path: "sources/raw/external/go-dev-design-43651-type-parameters-8b418b79f1.html"
license_ref: ""
---

## Examples
The following sections are examples of how this design could be used. This is intended to address specific areas where people have created user experience reports concerned with Go's lack of generics.
### Map/Reduce/Filter

Here is an example of how to write map, reduce, and filter functions for slices. These functions are intended to correspond to the similar functions in Lisp, Python, Java, and so forth.

```go
// Package slices implements various slice algorithms.
package slices

// Map turns a []T1 to a []T2 using a mapping function.
// This function has two type parameters, T1 and T2.
// This works with slices of any type.
func Map[T1, T2 any](s []T1, f func(T1) T2) []T2 {
	r := make([]T2, len(s))
	for i, v := range s {
		r[i] = f(v)
	}
	return r
}

// Reduce reduces a []T1 to a single value using a reduction function.
func Reduce[T1, T2 any](s []T1, initializer T2, f func(T2, T1) T2) T2 {
	r := initializer
	for _, v := range s {
		r = f(r, v)
	}
	return r
}

// Filter filters values from a slice using a filter function.
// It returns a new slice with only the elements of s
// for which f returned true.
func Filter[T any](s []T, f func(T) bool) []T {
	var r []T
	for _, v := range s {
		if f(v) {
			r = append(r, v)
		}
	}
	return r
}

```

Here are some example calls of these functions. Type inference is used to determine the type arguments based on the types of the non-type arguments.

```go
	s := []int{1, 2, 3}

	floats := slices.Map(s, func(i int) float64 { return float64(i) })
	// Now floats is []float64{1.0, 2.0, 3.0}.

	sum := slices.Reduce(s, 0, func(i, j int) int { return i + j })
	// Now sum is 6.

	evens := slices.Filter(s, func(i int) bool { return i%2 == 0 })
	// Now evens is []int{2}.

```
