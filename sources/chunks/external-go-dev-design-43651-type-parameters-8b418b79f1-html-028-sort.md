---
source_name: "External Linked Documentation"
source_url: "https://go.dev/design/43651-type-parameters"
source_path: "sources/raw/external/go-dev-design-43651-type-parameters-8b418b79f1.html"
license_ref: ""
---

## Examples

### Sort

Before the introduction of `sort.Slice`, a common complaint was the need for boilerplate definitions in order to use `sort.Sort`. With this design, we can add to the sort package as follows:

```go
// Ordered is a type constraint that matches all ordered types.
// (An ordered type is one that supports the < <= >= > operators.)
// In practice this type constraint would likely be defined in
// a standard library package.
type Ordered interface {
	~int | ~int8 | ~int16 | ~int32 | ~int64 |
		~uint | ~uint8 | ~uint16 | ~uint32 | ~uint64 | ~uintptr |
		~float32 | ~float64 |
		~string
}

// orderedSlice is an internal type that implements sort.Interface.
// The Less method uses the < operator. The Ordered type constraint
// ensures that T has a < operator.
type orderedSlice[T Ordered] []T

func (s orderedSlice[T]) Len() int           { return len(s) }
func (s orderedSlice[T]) Less(i, j int) bool { return s[i] < s[j] }
func (s orderedSlice[T]) Swap(i, j int)      { s[i], s[j] = s[j], s[i] }

// OrderedSlice sorts the slice s in ascending order.
// The elements of s must be ordered using the < operator.
func OrderedSlice[T Ordered](s []T) {
	// Convert s to the type orderedSlice[T].
	// As s is []T, and orderedSlice[T] is defined as []T,
	// this conversion is permitted.
	// orderedSlice[T] implements sort.Interface,
	// so can pass the result to sort.Sort.
	// The elements will be sorted using the < operator.
	sort.Sort(orderedSlice[T](s))
}

```

Now we can write:

```go
	s1 := []int32{3, 5, 2}
	sort.OrderedSlice(s1)
	// Now s1 is []int32{2, 3, 5}

	s2 := []string{"a", "c", "b"})
	sort.OrderedSlice(s2)
	// Now s2 is []string{"a", "b", "c"}

```

Along the same lines, we can add a function for sorting using a comparison function, similar to `sort.Slice` but writing the function to take values rather than slice indexes.

```go
// sliceFn is an internal type that implements sort.Interface.
// The Less method calls the cmp field.
type sliceFn[T any] struct {
	s   []T
	cmp func(T, T) bool
}

func (s sliceFn[T]) Len() int           { return len(s.s) }
func (s sliceFn[T]) Less(i, j int) bool { return s.cmp(s.s[i], s.s[j]) }
func (s sliceFn[T]) Swap(i, j int)      { s.s[i], s.s[j] = s.s[j], s.s[i] }

// SliceFn sorts the slice s according to the function cmp.
func SliceFn[T any](s []T, cmp func(T, T) bool) {
	sort.Sort(sliceFn[T]{s, cmp})
}

```

An example of calling this might be:

```go
	var s []*Person
	// ...
	sort.SliceFn(s, func(p1, p2 *Person) bool { return p1.Name < p2.Name })

```
