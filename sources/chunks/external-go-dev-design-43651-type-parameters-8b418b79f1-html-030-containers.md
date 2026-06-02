---
source_name: "External Linked Documentation"
source_url: "https://go.dev/design/43651-type-parameters"
source_path: "sources/raw/external/go-dev-design-43651-type-parameters-8b418b79f1.html"
license_ref: ""
---

## Examples

### Containers

One of the frequent requests for generics in Go is the ability to write compile-time type-safe containers. This design makes it easy to write a compile-time type-safe wrapper around an existing container; we won't write out an example for that. This design also makes it easy to write a compile-time type-safe container that does not use boxing.

Here is an example of an ordered map implemented as a binary tree. The details of how it works are not too important. The important points are:

- The code is written in a natural Go style, using the key and value types where needed.
- The keys and values are stored directly in the nodes of the tree, not using pointers and not boxed as interface values.

```go
// Package orderedmaps provides an ordered map, implemented as a binary tree.
package orderedmaps

import "chans"

// Map is an ordered map.
type Map[K, V any] struct {
	root    *node[K, V]
	compare func(K, K) int
}

// node is the type of a node in the binary tree.
type node[K, V any] struct {
	k           K
	v           V
	left, right *node[K, V]
}

// New returns a new map.
// Since the type parameter V is only used for the result,
// type inference does not work, and calls to New must always
// pass explicit type arguments.
func New[K, V any](compare func(K, K) int) *Map[K, V] {
	return &Map[K, V]{compare: compare}
}

// find looks up k in the map, and returns either a pointer
// to the node holding k, or a pointer to the location where
// such a node would go.
func (m *Map[K, V]) find(k K) **node[K, V] {
	pn := &m.root
	for *pn != nil {
		switch cmp := m.compare(k, (*pn).k); {
		case cmp < 0:
			pn = &(*pn).left
		case cmp > 0:
			pn = &(*pn).right
		default:
			return pn
		}
	}
	return pn
}

// Insert inserts a new key/value into the map.
// If the key is already present, the value is replaced.
// Reports whether this is a new key.
func (m *Map[K, V]) Insert(k K, v V) bool {
	pn := m.find(k)
	if *pn != nil {
		(*pn).v = v
		return false
	}
	*pn = &node[K, V]{k: k, v: v}
	return true
}

// Find returns the value associated with a key, or zero if not present.
// The bool result reports whether the key was found.
func (m *Map[K, V]) Find(k K) (V, bool) {
	pn := m.find(k)
	if *pn == nil {
		var zero V // see the discussion of zero values, above
		return zero, false
	}
	return (*pn).v, true
}

// keyValue is a pair of key and value used when iterating.
type keyValue[K, V any] struct {
	k K
	v V
}

// InOrder returns an iterator that does an in-order traversal of the map.
func (m *Map[K, V]) InOrder() *Iterator[K, V] {
	type kv = keyValue[K, V] // convenient shorthand
	sender, receiver := chans.Ranger[kv]()
	var f func(*node[K, V]) bool
	f = func(n *node[K, V]) bool {
		if n == nil {
			return true
		}
		// Stop sending values if sender.Send returns false,
		// meaning that nothing is listening at the receiver end.
		return f(n.left) &&
			sender.Send(kv{n.k, n.v}) &&
			f(n.right)
	}
	go func() {
		f(m.root)
		sender.Close()
	}()
	return &Iterator[K, V]{receiver}
}

// Iterator is used to iterate over the map.
type Iterator[K, V any] struct {
	r *chans.Receiver[keyValue[K, V]]
}

// Next returns the next key and value pair. The bool result reports
// whether the values are valid. If the values are not valid, we have
// reached the end.
func (it *Iterator[K, V]) Next() (K, V, bool) {
	kv, ok := it.r.Next()
	return kv.k, kv.v, ok
}

```

This is what it looks like to use this package:

```go
import "container/orderedmaps"

// Set m to an ordered map from string to string,
// using strings.Compare as the comparison function.
var m = orderedmaps.New[string, string](strings.Compare)

// Add adds the pair a, b to m.
func Add(a, b string) {
	m.Insert(a, b)
}

```
