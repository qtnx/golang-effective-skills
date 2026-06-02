---
source_name: "External Linked Documentation"
source_url: "https://pkg.go.dev/github.com/google/go-cmp/cmp"
source_path: "sources/raw/external/pkg-go-dev-github-com-google-go-cmp-cmp-5b1469c340.html"
license_ref: ""
---

Pointers and interfaces are equal if they are both nil or both non-nil, where they have the same underlying concrete type and recursively calling Equal on the underlying values reports equal.

Before recursing into a pointer, slice element, or map, the current path is checked to detect whether the address has already been visited. If there is a cycle, then the pointed at values are considered equal only if both addresses were previously visited in the same path step.

```go
type Indirect struct {
	// contains filtered or unexported fields
}
```

Indirect is a PathStep that represents pointer indirection on the parent type.

```go
func (in Indirect) String() string
```

```go
func (in Indirect) Type() reflect.Type
```

```go
func (in Indirect) Values() (vx, vy reflect.Value)
```

```go
type MapIndex struct {
	// contains filtered or unexported fields
}
```

MapIndex is a PathStep that represents an index operation on a map at some index Key.

```go
func (mi MapIndex) Key() reflect.Value
```

Key is the value of the map key.

```go
func (mi MapIndex) String() string
```

```go
func (mi MapIndex) Type() reflect.Type
```

```go
func (mi MapIndex) Values() (vx, vy reflect.Value)
```

```go
type Option interface {
	// contains filtered or unexported methods
}
```

Option configures for specific behavior of Equal and Diff. In particular, the fundamental Option functions (Ignore, Transformer, and Comparer), configure how equality is determined.

The fundamental options may be composed with filters (FilterPath and FilterValues) to control the scope over which they are applied.

The github.com/google/go-cmp/cmp/cmpopts package provides helper functions for creating options that may be used with Equal and Diff.

Approximate equality for floats can be handled by defining a custom comparer on floats that determines two values to be equal if they are within some range of each other.

This example is for demonstrative purposes; use github.com/google/go-cmp/cmp/cmpopts.EquateApprox instead.

```go

package main

import (
	"fmt"
	"math"

"github.com/google/go-cmp/cmp"
)

func main() {
	// This Comparer only operates on float64.
	// To handle float32s, either define a similar function for that type
	// or use a Transformer to convert float32s into float64s.
	opt := cmp.Comparer(func(x, y float64) bool {
		delta := math.Abs(x - y)
		mean := math.Abs(x+y) / 2.0
		return delta/mean < 0.00001
	})

x := []float64{1.0, 1.1, 1.2, math.Pi}
	y := []float64{1.0, 1.1, 1.2, 3.14159265359} // Accurate enough to Pi
	z := []float64{1.0, 1.1, 1.2, 3.1415}        // Diverges too far from Pi

fmt.Println(cmp.Equal(x, y, opt))
	fmt.Println(cmp.Equal(y, z, opt))
	fmt.Println(cmp.Equal(z, x, opt))

}

```

```go
Output:
true
false
false

```

Share Format Run

If the Equal method defined on a type is not suitable, the type can be dynamically transformed to be stripped of the Equal method (or any method for that matter).

```go

package main

import (
	"fmt"
	"strings"

"github.com/google/go-cmp/cmp"
)

type otherString string

func (x otherString) Equal(y otherString) bool {
	return strings.EqualFold(string(x), string(y))
}

func main() {
	// Suppose otherString.Equal performs a case-insensitive equality,
	// which is too loose for our needs.
	// We can avoid the methods of otherString by declaring a new type.
	type myString otherString

// This transformer converts otherString to myString, allowing Equal to use
	// other Options to determine equality.
	trans := cmp.Transformer("", func(in otherString) myString {
		return myString(in)
	})

x := []otherString{"foo", "bar", "baz"}
	y := []otherString{"fOO", "bAr", "Baz"} // Same as before, but with different case

fmt.Println(cmp.Equal(x, y))        // Equal because of case-insensitivity
	fmt.Println(cmp.Equal(x, y, trans)) // Not equal because of more exact equality

}

```

```go
Output:
true
false

```

Share Format Run

Sometimes, an empty map or slice is considered equal to an allocated one of zero length.

This example is for demonstrative purposes; use github.com/google/go-cmp/cmp/cmpopts.EquateEmpty instead.

```go

package main

import (
	"fmt"
	"reflect"

"github.com/google/go-cmp/cmp"
)

func main() {
	alwaysEqual := cmp.Comparer(func(_, _ interface{}) bool { return true })

// This option handles slices and maps of any type.
	opt := cmp.FilterValues(func(x, y interface{}) bool {
		vx, vy := reflect.ValueOf(x), reflect.ValueOf(y)
		return (vx.IsValid() && vy.IsValid() && vx.Type() == vy.Type()) &&
			(vx.Kind() == reflect.Slice || vx.Kind() == reflect.Map) &&
			(vx.Len() == 0 && vy.Len() == 0)
	}, alwaysEqual)

type S struct {
		A []int
		B map[string]bool
	}
	x := S{nil, make(map[string]bool, 100)}
	y := S{make([]int, 0, 200), nil}
	z := S{[]int{0}, nil} // []int has a single element (i.e., not empty)

fmt.Println(cmp.Equal(x, y, opt))
	fmt.Println(cmp.Equal(y, z, opt))
	fmt.Println(cmp.Equal(z, x, opt))

}

```

```go
Output:
true
false
false

```

Share Format Run

Normal floating-point arithmetic defines == to be false when comparing NaN with itself. In certain cases, this is not the desired property.

This example is for demonstrative purposes; use github.com/google/go-cmp/cmp/cmpopts.EquateNaNs instead.

```go

package main

import (
	"fmt"
	"math"

"github.com/google/go-cmp/cmp"
)

func main() {
	// This Comparer only operates on float64.
	// To handle float32s, either define a similar function for that type
	// or use a Transformer to convert float32s into float64s.
	opt := cmp.Comparer(func(x, y float64) bool {
		return (math.IsNaN(x) && math.IsNaN(y)) || x == y
	})

x := []float64{1.0, math.NaN(), math.E, 0.0}
	y := []float64{1.0, math.NaN(), math.E, 0.0}
	z := []float64{1.0, math.NaN(), math.Pi, 0.0} // Pi constant instead of E

fmt.Println(cmp.Equal(x, y, opt))
	fmt.Println(cmp.Equal(y, z, opt))
	fmt.Println(cmp.Equal(z, x, opt))

}

```

```go
Output:
true
false
false

```

Share Format Run

To have floating-point comparisons combine both properties of NaN being equal to itself and also approximate equality of values, filters are needed to restrict the scope of the comparison so that they are composable.

This example is for demonstrative purposes; use github.com/google/go-cmp/cmp/cmpopts.EquateApprox instead.

```go

package main

import (
	"fmt"
	"math"

"github.com/google/go-cmp/cmp"
)

func main() {
	alwaysEqual := cmp.Comparer(func(_, _ interface{}) bool { return true })

opts := cmp.Options{
		// This option declares that a float64 comparison is equal only if
		// both inputs are NaN.
		cmp.FilterValues(func(x, y float64) bool {
			return math.IsNaN(x) && math.IsNaN(y)
		}, alwaysEqual),

// This option declares approximate equality on float64s only if
		// both inputs are not NaN.
		cmp.FilterValues(func(x, y float64) bool {
			return !math.IsNaN(x) && !math.IsNaN(y)
		}, cmp.Comparer(func(x, y float64) bool {
			delta := math.Abs(x - y)
			mean := math.Abs(x+y) / 2.0
			return delta/mean < 0.00001
		})),
	}

x := []float64{math.NaN(), 1.0, 1.1, 1.2, math.Pi}
	y := []float64{math.NaN(), 1.0, 1.1, 1.2, 3.14159265359} // Accurate enough to Pi
	z := []float64{math.NaN(), 1.0, 1.1, 1.2, 3.1415}        // Diverges too far from Pi

fmt.Println(cmp.Equal(x, y, opts))
	fmt.Println(cmp.Equal(y, z, opts))
	fmt.Println(cmp.Equal(z, x, opts))

}

```

```go
Output:
true
false
false

```

Share Format Run

Two slices may be considered equal if they have the same elements, regardless of the order that they appear in. Transformations can be used to sort the slice.

This example is for demonstrative purposes; use github.com/google/go-cmp/cmp/cmpopts.SortSlices instead.

```go

package main

import (
	"fmt"
	"sort"

"github.com/google/go-cmp/cmp"
)

func main() {
	// This Transformer sorts a []int.
	trans := cmp.Transformer("Sort", func(in []int) []int {
		out := append([]int(nil), in...) // Copy input to avoid mutating it
		sort.Ints(out)
		return out
	})

x := struct{ Ints []int }{[]int{0, 1, 2, 3, 4, 5, 6, 7, 8, 9}}
	y := struct{ Ints []int }{[]int{2, 8, 0, 9, 6, 1, 4, 7, 3, 5}}
	z := struct{ Ints []int }{[]int{0, 0, 1, 2, 3, 4, 5, 6, 7, 8}}

fmt.Println(cmp.Equal(x, y, trans))
	fmt.Println(cmp.Equal(y, z, trans))
	fmt.Println(cmp.Equal(z, x, trans))

}

```

```go
Output:
true
false
false

```

Share Format Run

The complex numbers complex64 and complex128 can really just be decomposed into a pair of float32 or float64 values. It would be convenient to be able define only a single comparator on float64 and have float32, complex64, and complex128 all be able to use that comparator. Transformations can be used to handle this.

```go

package main

import (
	"fmt"
	"math"

"github.com/google/go-cmp/cmp"
)

func roundF64(z float64) float64 {
	if z < 0 {
		return math.Ceil(z - 0.5)
	}
	return math.Floor(z + 0.5)
}

func main() {
	opts := []cmp.Option{
		// This transformer decomposes complex128 into a pair of float64s.
		cmp.Transformer("T1", func(in complex128) (out struct{ Real, Imag float64 }) {
			out.Real, out.Imag = real(in), imag(in)
			return out
		}),
		// This transformer converts complex64 to complex128 to allow the
		// above transform to take effect.
		cmp.Transformer("T2", func(in complex64) complex128 {
			return complex128(in)
		}),
		// This transformer converts float32 to float64.
		cmp.Transformer("T3", func(in float32) float64 {
			return float64(in)
		}),
		// This equality function compares float64s as rounded integers.
		cmp.Comparer(func(x, y float64) bool {
			return roundF64(x) == roundF64(y)
		}),
	}

x := []interface{}{
		complex128(3.0), complex64(5.1 + 2.9i), float32(-1.2), float64(12.3),
	}
	y := []interface{}{
		complex128(3.1), complex64(4.9 + 3.1i), float32(-1.3), float64(11.7),
	}
	z := []interface{}{
		complex128(3.8), complex64(4.9 + 3.1i), float32(-1.3), float64(11.7),
	}

fmt.Println(cmp.Equal(x, y, opts...))
	fmt.Println(cmp.Equal(y, z, opts...))
	fmt.Println(cmp.Equal(z, x, opts...))

}

```

```go
Output:
true
false
false

```

Share Format Run

```go
func AllowUnexported(types ...interface{}) Option
```

AllowUnexported returns an Option that allows Equal to forcibly introspect unexported fields of the specified struct types.

See Exporter for the proper use of this option.

```go
func Comparer(f interface{}) Option
```

Comparer returns an Option that determines whether two values are equal to each other.

The comparer f must be a function "func(T, T) bool" and is implicitly filtered to input values assignable to T. If T is an interface, it is possible that f is called with two values of different concrete types that both implement T.

The equality function must be:

- Symmetric: equal(x, y) == equal(y, x)
- Deterministic: equal(x, y) == equal(x, y)
- Pure: equal(x, y) does not modify x or y

```go
func Exporter(f func(reflect.Type) bool) Option
```

Exporter returns an Option that specifies whether Equal is allowed to introspect into the unexported fields of certain struct types.
