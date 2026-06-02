---
source_name: "External Linked Documentation"
source_url: "https://pkg.go.dev/github.com/google/go-cmp/cmp"
source_path: "sources/raw/external/pkg-go-dev-github-com-google-go-cmp-cmp-5b1469c340.html"
license_ref: ""
---

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
