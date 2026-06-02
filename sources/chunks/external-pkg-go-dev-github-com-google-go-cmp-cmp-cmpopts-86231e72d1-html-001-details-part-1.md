---
source_name: "External Linked Documentation"
source_url: "https://pkg.go.dev/github.com/google/go-cmp/cmp/cmpopts"
source_path: "sources/raw/external/pkg-go-dev-github-com-google-go-cmp-cmp-cmpopts-86231e72d1.html"
license_ref: ""
---

cmpopts package - github.com/google/go-cmp/cmp/cmpopts - Go Packages
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

Package cmpopts provides common options for the cmp package.

- Variables
-  func AcyclicTransformer(name string, xformFunc interface{}) cmp.Option
-  func EquateApprox(fraction, margin float64) cmp.Option
-  func EquateApproxTime(margin time.Duration) cmp.Option
-  func EquateComparable(typs ...interface{}) cmp.Option
-  func EquateEmpty() cmp.Option
-  func EquateErrors() cmp.Option
-  func EquateNaNs() cmp.Option
-  func IgnoreFields(typ interface{}, names ...string) cmp.Option
-  func IgnoreInterfaces(ifaces interface{}) cmp.Option
-  func IgnoreMapEntries(discardFunc interface{}) cmp.Option
-  func IgnoreSliceElements(discardFunc interface{}) cmp.Option
-  func IgnoreTypes(typs ...interface{}) cmp.Option
-  func IgnoreUnexported(typs ...interface{}) cmp.Option
-  func SortMaps(lessOrCompareFunc interface{}) cmp.Option
-  func SortSlices(lessOrCompareFunc interface{}) cmp.Option

- IgnoreFields (Testing)

This section is empty.

View Source <https://github.com/google/go-cmp/blob/v0.7.0/cmp/cmpopts/equate.go#L128>
```go
var AnyError anyError
```

AnyError is an error that matches any non-nil error.

```go
func AcyclicTransformer(name string, xformFunc interface{}) cmp.Option
```

AcyclicTransformer returns a cmp.Transformer with a filter applied that ensures that the transformer cannot be recursively applied upon its own output.

An example use case is a transformer that splits a string by lines:

```go
AcyclicTransformer("SplitLines", func(s string) []string{
	return strings.Split(s, "\n")
})

```

Had this been an unfiltered cmp.Transformer instead, this would result in an infinite cycle converting a string to []string to [][]string and so on.

```go
func EquateApprox(fraction, margin float64) cmp.Option
```

EquateApprox returns a cmp.Comparer option that determines float32 or float64 values to be equal if they are within a relative fraction or absolute margin. This option is not used when either x or y is NaN or infinite.

The fraction determines that the difference of two values must be within the smaller fraction of the two values, while the margin determines that the two values must be within some absolute margin. To express only a fraction or only a margin, use 0 for the other parameter. The fraction and margin must be non-negative.

The mathematical expression used is equivalent to:

```go
|x-y| ≤ max(fraction*min(|x|, |y|), margin)

```

EquateApprox can be used in conjunction with EquateNaNs.

```go
func EquateApproxTime(margin time.Duration) cmp.Option
```

EquateApproxTime returns a cmp.Comparer option that determines two non-zero time.Time values to be equal if they are within some margin of one another. If both times have a monotonic clock reading, then the monotonic time difference will be used. The margin must be non-negative.

```go
func EquateComparable(typs ...interface{}) cmp.Option
```

EquateComparable returns a cmp.Option that determines equality of comparable types by directly comparing them using the == operator in Go. The types to compare are specified by passing a value of that type. This option should only be used on types that are documented as being safe for direct == comparison. For example, net/netip.Addr is documented as being semantically safe to use with ==, while time.Time is documented to discourage the use of == on time values.

```go
func EquateEmpty() cmp.Option
```

EquateEmpty returns a cmp.Comparer option that determines all maps and slices with a length of zero to be equal, regardless of whether they are nil.

EquateEmpty can be used in conjunction with SortSlices and SortMaps.

```go
func EquateErrors() cmp.Option
```

EquateErrors returns a cmp.Comparer option that determines errors to be equal if errors.Is reports them to match. The AnyError error can be used to match any non-nil error.

```go
func EquateNaNs() cmp.Option
```

EquateNaNs returns a cmp.Comparer option that determines float32 and float64 NaN values to be equal.

EquateNaNs can be used in conjunction with EquateApprox.

```go
func IgnoreFields(typ interface{}, names ...string) cmp.Option
```

IgnoreFields returns an cmp.Option that ignores fields of the given names on a single struct type. It respects the names of exported fields that are forwarded due to struct embedding. The struct type is specified by passing in a value of that type.

The name may be a dot-delimited string (e.g., "Foo.Bar") to ignore a specific sub-field that is embedded or nested within the parent struct.

Use IgnoreFields to ignore fields on a struct type when comparing by providing a value of the type and the field names to ignore. Typically, a zero value of the type is used (e.g., foo.MyStruct{}).

```go

package main

import (
	"fmt"
	"net"
	"time"

"github.com/google/go-cmp/cmp"
	"github.com/google/go-cmp/cmp/cmpopts"
	"github.com/google/go-cmp/cmp/internal/flags"
)

func init() {
	flags.Deterministic = true
}

// Use IgnoreFields to ignore fields on a struct type when comparing
// by providing a value of the type and the field names to ignore.
// Typically, a zero value of the type is used (e.g., foo.MyStruct{}).
func main() {
	// Let got be the hypothetical value obtained from some logic under test
	// and want be the expected golden data.
	got, want := MakeGatewayInfo()

// While the specified fields will be semantically ignored for the comparison,
	// the fields may be printed in the diff when displaying entire values
	// that are already determined to be different.
	if diff := cmp.Diff(want, got, cmpopts.IgnoreFields(Client{}, "IPAddress")); diff != "" {
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
  cmpopts_test.Gateway{
  	SSID:      "CoffeeShopWiFi",
- 	IPAddress: s"192.168.0.2",
+ 	IPAddress: s"192.168.0.1",
  	NetMask:   s"ffff0000",
  	Clients: []cmpopts_test.Client{
  		... // 3 identical elements
  		{Hostname: "espresso", ...},
  		{Hostname: "latte", LastSeen: s"2009-11-10 23:00:23 +0000 UTC", ...},
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
func IgnoreInterfaces(ifaces interface{}) cmp.Option
```

IgnoreInterfaces returns an cmp.Option that ignores all values or references of values assignable to certain interface types. These interfaces are specified by passing in an anonymous struct with the interface types embedded in it. For example, to ignore sync.Locker, pass in struct{sync.Locker}{}.

```go
func IgnoreMapEntries(discardFunc interface{}) cmp.Option
```

IgnoreMapEntries returns an cmp.Option that ignores entries of map[K]V. The discard function must be of the form "func(T, R) bool" which is used to ignore map entries of type K and V, where K and V are assignable to T and R. Entries are ignored if the function reports true.

```go
func IgnoreSliceElements(discardFunc interface{}) cmp.Option
```

IgnoreSliceElements returns an cmp.Option that ignores elements of []V. The discard function must be of the form "func(T) bool" which is used to ignore slice elements of type V, where V is assignable to T. Elements are ignored if the function reports true.

```go
func IgnoreTypes(typs ...interface{}) cmp.Option
```

IgnoreTypes returns an cmp.Option that ignores all values assignable to certain types, which are specified by passing in a value of each type.

```go
func IgnoreUnexported(typs ...interface{}) cmp.Option
```

IgnoreUnexported returns an cmp.Option that only ignores the immediate unexported fields of a struct, including anonymous fields of unexported types. In particular, unexported fields within the struct's exported fields of struct types, including anonymous fields, will not be ignored unless the type of the field itself is also passed to IgnoreUnexported.

Avoid ignoring unexported fields of a type which you do not control (i.e. a type from another repository), as changes to the implementation of such types may change how the comparison behaves. Prefer a custom cmp.Comparer instead.

```go
func SortMaps(lessOrCompareFunc interface{}) cmp.Option
```

SortMaps returns a cmp.Transformer option that flattens map[K]V types to be a sorted []struct{K, V}. The lessOrCompareFunc function must be either a less function of the form "func(T, T) bool" or a compare function of the format "func(T, T) int" which is used to sort any map with key K that is assignable to T.

Flattening the map into a slice has the property that cmp.Equal is able to use cmp.Comparer options on K or the K.Equal method if it exists.

A less function must be:

- Deterministic: less(x, y) == less(x, y)
- Irreflexive: !less(x, x)
- Transitive: if !less(x, y) and !less(y, z), then !less(x, z)
- Total: if x != y, then either less(x, y) or less(y, x)

A compare function must be:
