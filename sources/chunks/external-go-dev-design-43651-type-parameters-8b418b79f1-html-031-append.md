---
source_name: "External Linked Documentation"
source_url: "https://go.dev/design/43651-type-parameters"
source_path: "sources/raw/external/go-dev-design-43651-type-parameters-8b418b79f1.html"
license_ref: ""
---

## Examples

### Append

The predeclared `append` function exists to replace the boilerplate otherwise required to grow a slice. Before `append` was added to the language, there was a function `Add` in the bytes package:

```go
// Add appends the contents of t to the end of s and returns the result.
// If s has enough capacity, it is extended in place; otherwise a
// new array is allocated and returned.
func Add(s, t []byte) []byte

```

`Add` appended two `[]byte` values together, returning a new slice. That was fine for `[]byte`, but if you had a slice of some other type, you had to write essentially the same code to append more values. If this design were available back then, perhaps we would not have added `append` to the language. Instead, we could write something like this:

```go
// Package slices implements various slice algorithms.
package slices

// Append appends the contents of t to the end of s and returns the result.
// If s has enough capacity, it is extended in place; otherwise a
// new array is allocated and returned.
func Append[T any](s []T, t ...T) []T {
	lens := len(s)
	tot := lens + len(t)
	if tot < 0 {
		panic("Append: cap out of range")
	}
	if tot > cap(s) {
		news := make([]T, tot, tot + tot/2)
		copy(news, s)
		s = news
	}
	s = s[:tot]
	copy(s[lens:], t)
	return s
}

```

That example uses the predeclared `copy` function, but that's OK, we can write that one too:

```go
// Copy copies values from t to s, stopping when either slice is
// full, returning the number of values copied.
func Copy[T any](s, t []T) int {
	i := 0
	for ; i < len(s) && i < len(t); i++ {
		s[i] = t[i]
	}
	return i
}

```

These functions can be used as one would expect:

```go
	s := slices.Append([]int{1, 2, 3}, 4, 5, 6)
	// Now s is []int{1, 2, 3, 4, 5, 6}.
	slices.Copy(s[3:], []int{7, 8, 9})
	// Now s is []int{1, 2, 3, 7, 8, 9}

```

This code doesn‘t implement the special case of appending or copying a `string` to a `[]byte`, and it’s unlikely to be as efficient as the implementation of the predeclared function. Still, this example shows that using this design would permit `append` and `copy` to be written generically, once, without requiring any additional special language features.
