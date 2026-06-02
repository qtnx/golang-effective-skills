cmp package - github.com/google/go-cmp/cmp - Go Packages

## Details

-     Valid go.mod <https://github.com/google/go-cmp/tree/v0.7.0/go.mod> file
 The Go module system was introduced in Go 1.11 and is the official dependency management solution for Go.

-     Redistributable license
 Redistributable licenses place minimal restrictions on how software can be used, modified, and redistributed.

-     Tagged version
Modules with tagged versions give importers more predictable builds.

-     Stable version
When a project reaches major version v1 it is considered stable.

-  Learn more about best practices

## Repository
   github.com/google/go-cmp  <https://github.com/google/go-cmp>

## Links

-    Open Source Insights  <https://deps.dev/go/github.com%2Fgoogle%2Fgo-cmp/v0.7.0>
-    Code Wiki

##   Documentation ¶

Package cmp determines equality of values.

This package is intended to be a more powerful and safer alternative to reflect.DeepEqual for comparing whether two values are semantically equal. It is intended to only be used in tests, as performance is not a goal and it may panic if it cannot compare the values. Its propensity towards panicking means that its unsuitable for production environments where a spurious panic may be fatal.

The primary features of cmp are:

-
When the default behavior of equality does not suit the test's needs, custom equality functions can override the equality operation. For example, an equality function may report floats as equal so long as they are within some tolerance of each other.

-
Types with an Equal method (e.g., time.Time.Equal) may use that method to determine equality. This allows package authors to determine the equality operation for the types that they define.

-
If no custom equality functions are used and no Equal method is defined, equality is determined by recursively comparing the primitive kinds on both values, much like reflect.DeepEqual. Unlike reflect.DeepEqual, unexported fields are not compared by default; they result in panics unless suppressed by using an Ignore option (see github.com/google/go-cmp/cmp/cmpopts.IgnoreUnexported) or explicitly compared using the Exporter option.

-  func Diff(x, y interface{}, opts ...Option) string
-  func Equal(x, y interface{}, opts ...Option) bool
-  type Indirect
-
-  func (in Indirect) String() string
-  func (in Indirect) Type() reflect.Type
-  func (in Indirect) Values() (vx, vy reflect.Value)

-  type MapIndex
-
-  func (mi MapIndex) Key() reflect.Value
-  func (mi MapIndex) String() string
-  func (mi MapIndex) Type() reflect.Type
-  func (mi MapIndex) Values() (vx, vy reflect.Value)

-  type Option
-
-  func AllowUnexported(types ...interface{}) Option
-  func Comparer(f interface{}) Option
-  func Exporter(f func(reflect.Type) bool) Option
-  func FilterPath(f func(Path) bool, opt Option) Option
-  func FilterValues(f interface{}, opt Option) Option
-  func Ignore() Option
-  func Reporter(r interface{ ... }) Option
-  func Transformer(name string, f interface{}) Option

-  type Options
-
-  func (opts Options) String() string

-  type Path
-
-  func (pa Path) GoString() string
-  func (pa Path) Index(i int) PathStep
-  func (pa Path) Last() PathStep
-  func (pa Path) String() string

-  type PathStep
-  type Result
-
-  func (r Result) ByCycle() bool
-  func (r Result) ByFunc() bool
-  func (r Result) ByIgnore() bool
-  func (r Result) ByMethod() bool
-  func (r Result) Equal() bool

-  type SliceIndex
-
-  func (si SliceIndex) Key() int
-  func (si SliceIndex) SplitKeys() (ix, iy int)
-  func (si SliceIndex) String() string
-  func (si SliceIndex) Type() reflect.Type
-  func (si SliceIndex) Values() (vx, vy reflect.Value)

-  type StructField
-
-  func (sf StructField) Index() int
-  func (sf StructField) Name() string
-  func (sf StructField) String() string
-  func (sf StructField) Type() reflect.Type
-  func (sf StructField) Values() (vx, vy reflect.Value)

-  type Transform
-
-  func (tf Transform) Func() reflect.Value
-  func (tf Transform) Name() string
-  func (tf Transform) Option() Option
-  func (tf Transform) String() string
-  func (tf Transform) Type() reflect.Type
-  func (tf Transform) Values() (vx, vy reflect.Value)

-  type TypeAssertion
-
-  func (ta TypeAssertion) String() string
-  func (ta TypeAssertion) Type() reflect.Type
-  func (ta TypeAssertion) Values() (vx, vy reflect.Value)

- Diff (Testing)
- Option (ApproximateFloats)
- Option (AvoidEqualMethod)
- Option (EqualEmpty)
- Option (EqualNaNs)
- Option (EqualNaNsAndApproximateFloats)
- Option (SortedSlice)
- Option (TransformComplex)
- Reporter

This section is empty.

This section is empty.

```go
func Diff(x, y interface{}, opts ...Option) string
```

Diff returns a human-readable report of the differences between two values: y - x. It returns an empty string if and only if Equal returns true for the same input values and options.

The output is displayed as a literal in pseudo-Go syntax. At the start of each line, a "-" prefix indicates an element removed from x, a "+" prefix to indicates an element added from y, and the lack of a prefix indicates an element common to both x and y. If possible, the output uses fmt.Stringer.String or error.Error methods to produce more humanly readable outputs. In such cases, the string is prefixed with either an 's' or 'e' character, respectively, to indicate that the method was called.

Do not depend on this output being stable. If you need the ability to programmatically interpret the difference, consider using a custom Reporter.

Use Diff to print out a human-readable report of differences for tests comparing nested or structured data.

```go

package main

import (
	"fmt"
	"net"
	"time"

	"github.com/google/go-cmp/cmp"
)

func main() {
	// Let got be the hypothetical value obtained from some logic under test
	// and want be the expected golden data.
	got, want := MakeGatewayInfo()

	if diff := cmp.Diff(want, got); diff != "" {
		t.Errorf("MakeGatewayInfo() mismatch (-want +got):\n%s", diff)
	}

}

type (
	Gateway struct {
		SSID      string
		IPAddress net.IP
		NetMask   net.IPMask
		Clients   []Client
	}
	Client struct {
		Hostname  string
		IPAddress net.IP
		LastSeen  time.Time
	}
)

func MakeGatewayInfo() (x, y Gateway) {
	x = Gateway{
		SSID:      "CoffeeShopWiFi",
		IPAddress: net.IPv4(192, 168, 0, 1),
		NetMask:   net.IPv4Mask(255, 255, 0, 0),
		Clients: []Client{{
			Hostname:  "ristretto",
			IPAddress: net.IPv4(192, 168, 0, 116),
		}, {
			Hostname:  "arabica",
			IPAddress: net.IPv4(192, 168, 0, 104),
			LastSeen:  time.Date(2009, time.November, 10, 23, 6, 32, 0, time.UTC),
		}, {
			Hostname:  "macchiato",
			IPAddress: net.IPv4(192, 168, 0, 153),
			LastSeen:  time.Date(2009, time.November, 10, 23, 39, 43, 0, time.UTC),
		}, {
			Hostname:  "espresso",
			IPAddress: net.IPv4(192, 168, 0, 121),
		}, {
			Hostname:  "latte",
			IPAddress: net.IPv4(192, 168, 0, 219),
			LastSeen:  time.Date(2009, time.November, 10, 23, 0, 23, 0, time.UTC),
		}, {
			Hostname:  "americano",
			IPAddress: net.IPv4(192, 168, 0, 188),
			LastSeen:  time.Date(2009, time.November, 10, 23, 3, 5, 0, time.UTC),
		}},
	}
	y = Gateway{
		SSID:      "CoffeeShopWiFi",
		IPAddress: net.IPv4(192, 168, 0, 2),
		NetMask:   net.IPv4Mask(255, 255, 0, 0),
		Clients: []Client{{
			Hostname:  "ristretto",
			IPAddress: net.IPv4(192, 168, 0, 116),
		}, {
			Hostname:  "arabica",
			IPAddress: net.IPv4(192, 168, 0, 104),
			LastSeen:  time.Date(2009, time.November, 10, 23, 6, 32, 0, time.UTC),
		}, {
			Hostname:  "macchiato",
			IPAddress: net.IPv4(192, 168, 0, 153),
			LastSeen:  time.Date(2009, time.November, 10, 23, 39, 43, 0, time.UTC),
		}, {
			Hostname:  "espresso",
			IPAddress: net.IPv4(192, 168, 0, 121),
		}, {
			Hostname:  "latte",
			IPAddress: net.IPv4(192, 168, 0, 221),
			LastSeen:  time.Date(2009, time.November, 10, 23, 0, 23, 0, time.UTC),
		}},
	}
	return x, y
}

var t fakeT

type fakeT struct{}

func (t fakeT) Errorf(format string, args ...interface{}) { fmt.Printf(format+"\n", args...) }

```

```go
Output:
MakeGatewayInfo() mismatch (-want +got):
  cmp_test.Gateway{
  	SSID:      "CoffeeShopWiFi",
- 	IPAddress: s"192.168.0.2",
+ 	IPAddress: s"192.168.0.1",
  	NetMask:   s"ffff0000",
  	Clients: []cmp_test.Client{
  		... // 2 identical elements
  		{Hostname: "macchiato", IPAddress: s"192.168.0.153", LastSeen: s"2009-11-10 23:39:43 +0000 UTC"},
  		{Hostname: "espresso", IPAddress: s"192.168.0.121"},
  		{
  			Hostname:  "latte",
- 			IPAddress: s"192.168.0.221",
+ 			IPAddress: s"192.168.0.219",
  			LastSeen:  s"2009-11-10 23:00:23 +0000 UTC",
  		},
+ 		{
+ 			Hostname:  "americano",
+ 			IPAddress: s"192.168.0.188",
+ 			LastSeen:  s"2009-11-10 23:03:05 +0000 UTC",
+ 		},
  	},
  }

```

 Share Format Run

```go
func Equal(x, y interface{}, opts ...Option) bool
```

Equal reports whether x and y are equal by recursively applying the following rules in the given order to x and y and all of their sub-values:

-
Let S be the set of all Ignore, Transformer, and Comparer options that remain after applying all path filters, value filters, and type filters. If at least one Ignore exists in S, then the comparison is ignored. If the number of Transformer and Comparer options in S is non-zero, then Equal panics because it is ambiguous which option to use. If S contains a single Transformer, then use that to transform the current values and recursively call Equal on the output values. If S contains a single Comparer, then use that to compare the current values. Otherwise, evaluation proceeds to the next rule.

-
If the values have an Equal method of the form "(T) Equal(T) bool" or "(T) Equal(I) bool" where T is assignable to I, then use the result of x.Equal(y) even if x or y is nil. Otherwise, no such method exists and evaluation proceeds to the next rule.

-
Lastly, try to compare x and y based on their basic kinds. Simple kinds like booleans, integers, floats, complex numbers, strings, and channels are compared using the equivalent of the == operator in Go. Functions are only equal if they are both nil, otherwise they are unequal.

Structs are equal if recursively calling Equal on all fields report equal. If a struct contains unexported fields, Equal panics unless an Ignore option (e.g., github.com/google/go-cmp/cmp/cmpopts.IgnoreUnexported) ignores that field or the Exporter option explicitly permits comparing the unexported field.

Slices are equal if they are both nil or both non-nil, where recursively calling Equal on all non-ignored slice or array elements report equal. Empty non-nil slices and nil slices are not equal; to equate empty slices, consider using github.com/google/go-cmp/cmp/cmpopts.EquateEmpty.

Maps are equal if they are both nil or both non-nil, where recursively calling Equal on all non-ignored map entries report equal. Map keys are equal according to the == operator. To use custom comparisons for map keys, consider using github.com/google/go-cmp/cmp/cmpopts.SortMaps. Empty non-nil maps and nil maps are not equal; to equate empty maps, consider using github.com/google/go-cmp/cmp/cmpopts.EquateEmpty.

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

Users of this option must understand that comparing on unexported fields from external packages is not safe since changes in the internal implementation of some external package may cause the result of Equal to unexpectedly change. However, it may be valid to use this option on types defined in an internal package where the semantic meaning of an unexported field is in the control of the user.

In many cases, a custom Comparer should be used instead that defines equality as a function of the public API of a type rather than the underlying unexported implementation.

For example, the reflect.Type documentation defines equality to be determined by the == operator on the interface (essentially performing a shallow pointer comparison) and most attempts to compare *regexp.Regexp types are interested in only checking that the regular expression strings are equal. Both of these are accomplished using Comparer options:

```go
Comparer(func(x, y reflect.Type) bool { return x == y })
Comparer(func(x, y *regexp.Regexp) bool { return x.String() == y.String() })

```

In other cases, the github.com/google/go-cmp/cmp/cmpopts.IgnoreUnexported option can be used to ignore all unexported fields on specified struct types.

```go
func FilterPath(f func(Path) bool, opt Option) Option
```

FilterPath returns a new Option where opt is only evaluated if filter f returns true for the current Path in the value tree.

This filter is called even if a slice element or map entry is missing and provides an opportunity to ignore such cases. The filter function must be symmetric such that the filter result is identical regardless of whether the missing value is from x or y.

The option passed in may be an Ignore, Transformer, Comparer, Options, or a previously filtered Option.

```go
func FilterValues(f interface{}, opt Option) Option
```

FilterValues returns a new Option where opt is only evaluated if filter f, which is a function of the form "func(T, T) bool", returns true for the current pair of values being compared. If either value is invalid or the type of the values is not assignable to T, then this filter implicitly returns false.

The filter function must be symmetric (i.e., agnostic to the order of the inputs) and deterministic (i.e., produces the same result when given the same inputs). If T is an interface, it is possible that f is called with two values with different concrete types that both implement T.

The option passed in may be an Ignore, Transformer, Comparer, Options, or a previously filtered Option.

```go
func Ignore() Option
```

Ignore is an Option that causes all comparisons to be ignored. This value is intended to be combined with FilterPath or FilterValues. It is an error to pass an unfiltered Ignore option to Equal.

```go
func Reporter(r interface {
	// PushStep is called when a tree-traversal operation is performed.
	// The PathStep itself is only valid until the step is popped.
	// The PathStep.Values are valid for the duration of the entire traversal
	// and must not be mutated.
	//
	// Equal always calls PushStep at the start to provide an operation-less
	// PathStep used to report the root values.
	//
	// Within a slice, the exact set of inserted, removed, or modified elements
	// is unspecified and may change in future implementations.
	// The entries of a map are iterated through in an unspecified order.
	PushStep(PathStep)

	// Report is called exactly once on leaf nodes to report whether the
	// comparison identified the node as equal, unequal, or ignored.
	// A leaf node is one that is immediately preceded by and followed by
	// a pair of PushStep and PopStep calls.
	Report(Result)

	// PopStep ascends back up the value tree.
	// There is always a matching pop call for every push call.
	PopStep()
}) Option
```

Reporter is an Option that can be passed to Equal. When Equal traverses the value trees, it calls PushStep as it descends into each node in the tree and PopStep as it ascend out of the node. The leaves of the tree are either compared (determined to be equal or not equal) or ignored and reported as such by calling the Report method.

```go

package main

import (
	"fmt"
	"strings"

	"github.com/google/go-cmp/cmp"
)

// DiffReporter is a simple custom reporter that only records differences
// detected during comparison.
type DiffReporter struct {
	path  cmp.Path
	diffs []string
}

func (r *DiffReporter) PushStep(ps cmp.PathStep) {
	r.path = append(r.path, ps)
}

func (r *DiffReporter) Report(rs cmp.Result) {
	if !rs.Equal() {
		vx, vy := r.path.Last().Values()
		r.diffs = append(r.diffs, fmt.Sprintf("%#v:\n\t-: %+v\n\t+: %+v\n", r.path, vx, vy))
	}
}

func (r *DiffReporter) PopStep() {
	r.path = r.path[:len(r.path)-1]
}

func (r *DiffReporter) String() string {
	return strings.Join(r.diffs, "\n")
}

func main() {
	x, y := MakeGatewayInfo()

	var r DiffReporter
	cmp.Equal(x, y, cmp.Reporter(&r))
	fmt.Print(r.String())

}

```

```go
Output:
{cmp_test.Gateway}.IPAddress:
	-: 192.168.0.1
	+: 192.168.0.2

{cmp_test.Gateway}.Clients[4].IPAddress:
	-: 192.168.0.219
	+: 192.168.0.221

{cmp_test.Gateway}.Clients[5->?]:
	-: {Hostname:americano IPAddress:192.168.0.188 LastSeen:2009-11-10 23:03:05 +0000 UTC}
	+: <invalid reflect.Value>

```

 Share Format Run

```go
func Transformer(name string, f interface{}) Option
```

Transformer returns an Option that applies a transformation function that converts values of a certain type into that of another.

The transformer f must be a function "func(T) R" that converts values of type T to those of type R and is implicitly filtered to input values assignable to T. The transformer must not mutate T in any way.

To help prevent some cases of infinite recursive cycles applying the same transform to the output of itself (e.g., in the case where the input and output types are the same), an implicit filter is added such that a transformer is applicable only if that exact transformer is not already in the tail of the Path since the last non-Transform step. For situations where the implicit filter is still insufficient, consider using github.com/google/go-cmp/cmp/cmpopts.AcyclicTransformer, which adds a filter to prevent the transformer from being recursively applied upon itself.

The name is a user provided label that is used as the Transform.Name in the transformation PathStep (and eventually shown in the Diff output). The name must be a valid identifier or qualified identifier in Go syntax. If empty, an arbitrary name is used.

```go
type Options []Option
```

Options is a list of Option values that also satisfies the Option interface. Helper comparison packages may return an Options value when packing multiple Option values into a single Option. When this package processes an Options, it will be implicitly expanded into a flat list.

Applying a filter on an Options is equivalent to applying that same filter on all individual options held within.

```go
func (opts Options) String() string
```

```go
type Path []PathStep
```

Path is a list of PathStep describing the sequence of operations to get from some root type to the current position in the value tree. The first Path element is always an operation-less PathStep that exists simply to identify the initial type.

When traversing structs with embedded structs, the embedded struct will always be accessed as a field before traversing the fields of the embedded struct themselves. That is, an exported field from the embedded struct will never be accessed directly from the parent struct.

```go
func (pa Path) GoString() string
```

GoString returns the path to a specific node using Go syntax.

For example:

```go
(*root.MyMap["key"].(*mypkg.MyStruct).MySlices)[2][3].MyField

```

```go
func (pa Path) Index(i int) PathStep
```

Index returns the ith step in the Path and supports negative indexing. A negative index starts counting from the tail of the Path such that -1 refers to the last step, -2 refers to the second-to-last step, and so on. If index is invalid, this returns a non-nil PathStep that reports a nil [PathStep.Type].

```go
func (pa Path) Last() PathStep
```

Last returns the last PathStep in the Path. If the path is empty, this returns a non-nil PathStep that reports a nil [PathStep.Type].

```go
func (pa Path) String() string
```

String returns the simplified path to a node. The simplified path only contains struct field accesses.

For example:

```go
MyMap.MySlices.MyField

```

```go
type PathStep interface {
	String() string

	// Type is the resulting type after performing the path step.
	Type() reflect.Type

	// Values is the resulting values after performing the path step.
	// The type of each valid value is guaranteed to be identical to Type.
	//
	// In some cases, one or both may be invalid or have restrictions:
	//   - For StructField, both are not interface-able if the current field
	//     is unexported and the struct type is not explicitly permitted by
	//     an Exporter to traverse unexported fields.
	//   - For SliceIndex, one may be invalid if an element is missing from
	//     either the x or y slice.
	//   - For MapIndex, one may be invalid if an entry is missing from
	//     either the x or y map.
	//
	// The provided values must not be mutated.
	Values() (vx, vy reflect.Value)
}
```

PathStep is a union-type for specific operations to traverse a value's tree structure. Users of this package never need to implement these types as values of this type will be returned by this package.

Implementations of this interface:

- StructField
- SliceIndex
- MapIndex
- Indirect
- TypeAssertion
- Transform

```go
type Result struct {
	// contains filtered or unexported fields
}
```

Result represents the comparison result for a single node and is provided by cmp when calling Report (see Reporter).

```go
func (r Result) ByCycle() bool
```

ByCycle reports whether a reference cycle was detected.

```go
func (r Result) ByFunc() bool
```

ByFunc reports whether a Comparer function determined equality.

```go
func (r Result) ByIgnore() bool
```

ByIgnore reports whether the node is equal because it was ignored. This never reports true if Result.Equal reports false.

```go
func (r Result) ByMethod() bool
```

ByMethod reports whether the Equal method determined equality.

```go
func (r Result) Equal() bool
```

Equal reports whether the node was determined to be equal or not. As a special case, ignored nodes are considered equal.

```go
type SliceIndex struct {
	// contains filtered or unexported fields
}
```

SliceIndex is a PathStep that represents an index operation on a slice or array at some index SliceIndex.Key.

```go
func (si SliceIndex) Key() int
```

Key is the index key; it may return -1 if in a split state

```go
func (si SliceIndex) SplitKeys() (ix, iy int)
```

SplitKeys are the indexes for indexing into slices in the x and y values, respectively. These indexes may differ due to the insertion or removal of an element in one of the slices, causing all of the indexes to be shifted. If an index is -1, then that indicates that the element does not exist in the associated slice.

SliceIndex.Key is guaranteed to return -1 if and only if the indexes returned by SplitKeys are not the same. SplitKeys will never return -1 for both indexes.

```go
func (si SliceIndex) String() string
```

```go
func (si SliceIndex) Type() reflect.Type
```

```go
func (si SliceIndex) Values() (vx, vy reflect.Value)
```

```go
type StructField struct {
	// contains filtered or unexported fields
}
```

StructField is a PathStep that represents a struct field access on a field called StructField.Name.

```go
func (sf StructField) Index() int
```

Index is the index of the field in the parent struct type. See reflect.Type.Field.

```go
func (sf StructField) Name() string
```

Name is the field name.

```go
func (sf StructField) String() string
```

```go
func (sf StructField) Type() reflect.Type
```

```go
func (sf StructField) Values() (vx, vy reflect.Value)
```

```go
type Transform struct {
	// contains filtered or unexported fields
}
```

Transform is a PathStep that represents a transformation from the parent type to the current type.

```go
func (tf Transform) Func() reflect.Value
```

Func is the function pointer to the transformer function.

```go
func (tf Transform) Name() string
```

Name is the name of the Transformer.

```go
func (tf Transform) Option() Option
```

Option returns the originally constructed Transformer option. The == operator can be used to detect the exact option used.

```go
func (tf Transform) String() string
```

```go
func (tf Transform) Type() reflect.Type
```

```go
func (tf Transform) Values() (vx, vy reflect.Value)
```

```go
type TypeAssertion struct {
	// contains filtered or unexported fields
}
```

TypeAssertion is a PathStep that represents a type assertion on an interface.

```go
func (ta TypeAssertion) String() string
```

```go
func (ta TypeAssertion) Type() reflect.Type
```

```go
func (ta TypeAssertion) Values() (vx, vy reflect.Value)
```

##   Source Files ¶
 View all Source files <https://github.com/google/go-cmp/tree/v0.7.0/cmp>

- compare.go <https://github.com/google/go-cmp/blob/v0.7.0/cmp/compare.go>
- export.go <https://github.com/google/go-cmp/blob/v0.7.0/cmp/export.go>
- options.go <https://github.com/google/go-cmp/blob/v0.7.0/cmp/options.go>
- path.go <https://github.com/google/go-cmp/blob/v0.7.0/cmp/path.go>
- report.go <https://github.com/google/go-cmp/blob/v0.7.0/cmp/report.go>
- report_compare.go <https://github.com/google/go-cmp/blob/v0.7.0/cmp/report_compare.go>
- report_references.go <https://github.com/google/go-cmp/blob/v0.7.0/cmp/report_references.go>
- report_reflect.go <https://github.com/google/go-cmp/blob/v0.7.0/cmp/report_reflect.go>
- report_slices.go <https://github.com/google/go-cmp/blob/v0.7.0/cmp/report_slices.go>
- report_text.go <https://github.com/google/go-cmp/blob/v0.7.0/cmp/report_text.go>
- report_value.go <https://github.com/google/go-cmp/blob/v0.7.0/cmp/report_value.go>

##   Directories ¶
    Show internal   Expand all

      cmpopts
 Package cmpopts provides common options for the cmp package.

  Package cmpopts provides common options for the cmp package.      internal      diff  Package diff implements an algorithm for producing edit-scripts.

  Package diff implements an algorithm for producing edit-scripts.    flags

      function  Package function provides functionality for identifying function types.

  Package function provides functionality for identifying function types.    testprotos

      teststructs

      teststructs/foo1  Package foo is deliberately named differently than the parent directory.

  Package foo is deliberately named differently than the parent directory.    teststructs/foo2  Package foo is deliberately named differently than the parent directory.

  Package foo is deliberately named differently than the parent directory.    value

  Click to show internal directories.
  Click to hide internal directories.

  Close

     **?** : This menu   **/** : Search site   **f** or **F** : Jump to   **y** or **Y**  : Canonical URL
  Close
