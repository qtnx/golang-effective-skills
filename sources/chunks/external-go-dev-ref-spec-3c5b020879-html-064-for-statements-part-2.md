---
source_name: "External Linked Documentation"
source_url: "https://go.dev/ref/spec"
source_path: "sources/raw/external/go-dev-ref-spec-3c5b020879.html"
license_ref: ""
---

## Statements

// print the Fibonacci numbers below 1000:
for x := range fibo {
	if x >= 1000 {
		break
	}
	fmt.Printf("%d ", x)
}
// output: 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987

// iteration support for a recursive tree data structure
type Tree[K cmp.Ordered, V any] struct {
	left, right *Tree[K, V]
	key         K
	value       V
}

func (t *Tree[K, V]) walk(yield func(key K, val V) bool) bool {
	return t == nil || t.left.walk(yield) && yield(t.key, t.value) && t.right.walk(yield)
}

func (t *Tree[K, V]) Walk(yield func(key K, val V) bool) {
	t.walk(yield)
}

// walk tree t in-order
var t Tree[string, int]
for k, v := range t.Walk {
	// process k, v
}

```

If the type of the range expression is a type parameter, all types in its type set must have the same underlying type and the range expression must be valid for that type, or, if the type set contains channel types, it must only contain channel types with identical element types, and all channel types must permit receive operations.
