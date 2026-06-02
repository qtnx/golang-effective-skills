---
source_name: "External Linked Documentation"
source_url: "https://go.dev/ref/spec"
source_path: "sources/raw/external/go-dev-ref-spec-3c5b020879.html"
license_ref: ""
---

## Types

### Slice types

 A slice is a descriptor for a contiguous segment of an _underlying array_ and provides access to a numbered sequence of elements from that array. A slice type denotes the set of all slices of arrays of its element type. The number of elements is called the length of the slice and is never negative. The value of an uninitialized slice is `nil`.

```go

SliceType = "[" "]" ElementType .

```

 The length of a slice `s` can be discovered by the built-in function `len`; unlike with arrays it may change during execution. The elements can be addressed by integer indices 0 through `len(s)-1`. The slice index of a given element may be less than the index of the same element in the underlying array.

 A slice, once initialized, is always associated with an underlying array that holds its elements. A slice therefore shares storage with its array and with other slices of the same array; by contrast, distinct arrays always represent distinct storage.

 The array underlying a slice may extend past the end of the slice. The _capacity_ is a measure of that extent: it is the sum of the length of the slice and the length of the array beyond the slice; a slice of length up to that capacity can be created by _slicing_ a new one from the original slice. The capacity of a slice `a` can be discovered using the built-in function `cap(a)`.

 A new, initialized slice value for a given element type `T` may be made using the built-in function `make`, which takes a slice type and parameters specifying the length and optionally the capacity. A slice created with `make` always allocates a new, hidden array to which the returned slice value refers. That is, executing

```go

make([]T, length, capacity)

```

 produces the same slice as allocating an array and slicing it, so these two expressions are equivalent:

```go

make([]int, 50, 100)
new([100]int)[0:50]

```

 Like arrays, slices are always one-dimensional but may be composed to construct higher-dimensional objects. With arrays of arrays, the inner arrays are, by construction, always the same length; however with slices of slices (or arrays of slices), the inner lengths may vary dynamically. Moreover, the inner slices must be initialized individually.
