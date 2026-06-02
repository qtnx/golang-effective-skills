---
source_name: "External Linked Documentation"
source_url: "https://go.dev/design/43651-type-parameters"
source_path: "sources/raw/external/go-dev-design-43651-type-parameters-8b418b79f1.html"
license_ref: ""
---

## Examples

### Map keys

Here is how to get a slice of the keys of any map.

```go
// Package maps provides general functions that work for all map types.
package maps

// Keys returns the keys of the map m in a slice.
// The keys will be returned in an unpredictable order.
// This function has two type parameters, K and V.
// Map keys must be comparable, so key has the predeclared
// constraint comparable. Map values can be any type.
func Keys[K comparable, V any](m map[K]V) []K {
	r := make([]K, 0, len(m))
	for k := range m {
		r = append(r, k)
	}
	return r
}

```

In typical use the map key and val types will be inferred.

```go
	k := maps.Keys(map[int]int{1:2, 2:4})
	// Now k is either []int{1, 2} or []int{2, 1}.

```
