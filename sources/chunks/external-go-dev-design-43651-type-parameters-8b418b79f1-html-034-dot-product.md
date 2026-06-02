---
source_name: "External Linked Documentation"
source_url: "https://go.dev/design/43651-type-parameters"
source_path: "sources/raw/external/go-dev-design-43651-type-parameters-8b418b79f1.html"
license_ref: ""
---

## Examples

### Dot product

A generic dot product implementation that works for slices of any numeric type.

```go
// Numeric is a constraint that matches any numeric type.
// It would likely be in a constraints package in the standard library.
type Numeric interface {
	~int | ~int8 | ~int16 | ~int32 | ~int64 |
		~uint | ~uint8 | ~uint16 | ~uint32 | ~uint64 | ~uintptr |
		~float32 | ~float64 |
		~complex64 | ~complex128
}

// DotProduct returns the dot product of two slices.
// This panics if the two slices are not the same length.
func DotProduct[T Numeric](s1, s2 []T) T {
	if len(s1) != len(s2) {
		panic("DotProduct: slices of unequal length")
	}
	var r T
	for i := range s1 {
		r += s1[i] * s2[i]
	}
	return r
}

```

(Note: the generics implementation approach may affect whether `DotProduct` uses FMA, and thus what the exact results are when using floating point types. It's not clear how much of a problem this is, or whether there is any way to fix it.)
