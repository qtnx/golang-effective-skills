---
source_name: "External Linked Documentation"
source_url: "https://pkg.go.dev/github.com/google/go-cmp/cmp"
source_path: "sources/raw/external/pkg-go-dev-github-com-google-go-cmp-cmp-5b1469c340.html"
license_ref: ""
---

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
