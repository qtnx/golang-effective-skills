---
source_name: "External Linked Documentation"
source_url: "https://go.dev/design/43651-type-parameters"
source_path: "sources/raw/external/go-dev-design-43651-type-parameters-8b418b79f1.html"
license_ref: ""
---

## Examples

### Metrics

In a Go experience report <https://medium.com/@sameer_74231/go-experience-report-for-generics-google-metrics-api-b019d597aaa4> Sameer Ajmani describes a metrics implementation. Each metric has a value and one or more fields. The fields have different types. Defining a metric requires specifying the types of the fields. The `Add` method takes the field types as arguments, and records an instance of that set of fields. The C++ implementation uses a variadic template. The Java implementation includes the number of fields in the name of the type. Both the C++ and Java implementations provide compile-time type-safe Add methods.

Here is how to use this design to provide similar functionality in Go with a compile-time type-safe `Add` method. Because there is no support for a variadic number of type arguments, we must use different names for a different number of arguments, as in Java. This implementation only works for comparable types. A more complex implementation could accept a comparison function to work with arbitrary types.

```go
// Package metrics provides a general mechanism for accumulating
// metrics of different values.
package metrics

import "sync"

// Metric1 accumulates metrics of a single value.
type Metric1[T comparable] struct {
	mu sync.Mutex
	m  map[T]int
}

// Add adds an instance of a value.
func (m *Metric1[T]) Add(v T) {
	m.mu.Lock()
	defer m.mu.Unlock()
	if m.m == nil {
		m.m = make(map[T]int)
	}
	m.m[v]++
}

// key2 is an internal type used by Metric2.
type key2[T1, T2 comparable] struct {
	f1 T1
	f2 T2
}

// Metric2 accumulates metrics of pairs of values.
type Metric2[T1, T2 comparable] struct {
	mu sync.Mutex
	m  map[key2[T1, T2]]int
}

// Add adds an instance of a value pair.
func (m *Metric2[T1, T2]) Add(v1 T1, v2 T2) {
	m.mu.Lock()
	defer m.mu.Unlock()
	if m.m == nil {
		m.m = make(map[key2[T1, T2]]int)
	}
	m.m[key2[T1, T2]{v1, v2}]++
}

// key3 is an internal type used by Metric3.
type key3[T1, T2, T3 comparable] struct {
	f1 T1
	f2 T2
	f3 T3
}

// Metric3 accumulates metrics of triples of values.
type Metric3[T1, T2, T3 comparable] struct {
	mu sync.Mutex
	m  map[key3[T1, T2, T3]]int
}

// Add adds an instance of a value triplet.
func (m *Metric3[T1, T2, T3]) Add(v1 T1, v2 T2, v3 T3) {
	m.mu.Lock()
	defer m.mu.Unlock()
	if m.m == nil {
		m.m = make(map[key3[T1, T2, T3]]int)
	}
	m.m[key3[T1, T2, T3]{v1, v2, v3}]++
}

// Repeat for the maximum number of permitted arguments.

```

Using this package looks like this:

```go
import "metrics"

var m = metrics.Metric2[string, int]{}

func F(s string, i int) {
	m.Add(s, i) // this call is type checked at compile time
}

```

This implementation has a certain amount of repetition due to the lack of support for variadic type parameters. Using the package, though, is easy and type safe.
