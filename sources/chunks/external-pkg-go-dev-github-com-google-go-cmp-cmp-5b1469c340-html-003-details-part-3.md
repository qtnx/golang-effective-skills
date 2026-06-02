---
source_name: "External Linked Documentation"
source_url: "https://pkg.go.dev/github.com/google/go-cmp/cmp"
source_path: "sources/raw/external/pkg-go-dev-github-com-google-go-cmp-cmp-5b1469c340.html"
license_ref: ""
---

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
