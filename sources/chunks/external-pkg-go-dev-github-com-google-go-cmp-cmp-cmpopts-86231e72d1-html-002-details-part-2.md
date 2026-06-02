---
source_name: "External Linked Documentation"
source_url: "https://pkg.go.dev/github.com/google/go-cmp/cmp/cmpopts"
source_path: "sources/raw/external/pkg-go-dev-github-com-google-go-cmp-cmp-cmpopts-86231e72d1.html"
license_ref: ""
---

- Deterministic: compare(x, y) == compare(x, y)
- Irreflexive: compare(x, x) == 0
- Transitive: if compare(x, y) < 0 and compare(y, z) < 0, then compare(x, z) < 0
- Total: if x != y, then compare(x, y) != 0

SortMaps can be used in conjunction with EquateEmpty.

```go
func SortSlices(lessOrCompareFunc interface{}) cmp.Option
```

SortSlices returns a cmp.Transformer option that sorts all []V. The lessOrCompareFunc function must be either a less function of the form "func(T, T) bool" or a compare function of the format "func(T, T) int" which is used to sort any slice with element type V that is assignable to T.

A less function must be:

- Deterministic: less(x, y) == less(x, y)
- Irreflexive: !less(x, x)
- Transitive: if !less(x, y) and !less(y, z), then !less(x, z)

A compare function must be:

- Deterministic: compare(x, y) == compare(x, y)
- Irreflexive: compare(x, x) == 0
- Transitive: if !less(x, y) and !less(y, z), then !less(x, z)

The function does not have to be "total". That is, if x != y, but less or compare report inequality, their relative order is maintained.

SortSlices can be used in conjunction with EquateEmpty.

This section is empty.

##   Source Files ¶
 View all Source files <https://github.com/google/go-cmp/tree/v0.7.0/cmp/cmpopts>

- equate.go <https://github.com/google/go-cmp/blob/v0.7.0/cmp/cmpopts/equate.go>
- ignore.go <https://github.com/google/go-cmp/blob/v0.7.0/cmp/cmpopts/ignore.go>
- sort.go <https://github.com/google/go-cmp/blob/v0.7.0/cmp/cmpopts/sort.go>
- struct_filter.go <https://github.com/google/go-cmp/blob/v0.7.0/cmp/cmpopts/struct_filter.go>
- xform.go <https://github.com/google/go-cmp/blob/v0.7.0/cmp/cmpopts/xform.go>

Click to show internal directories.
  Click to hide internal directories.

Close

**?** : This menu   **/** : Search site   **f** or **F** : Jump to   **y** or **Y**  : Canonical URL
  Close
