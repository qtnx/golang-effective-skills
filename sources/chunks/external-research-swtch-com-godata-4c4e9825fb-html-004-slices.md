---
source_name: "External Linked Documentation"
source_url: "https://research.swtch.com/godata"
source_path: "sources/raw/external/research-swtch-com-godata-4c4e9825fb.html"
license_ref: ""
---

# Go Data Structures   Russ Cox

## Slices

A slice <http://golang.org/doc/effective_go.html#slices> is a reference to a section of an array. In memory, it is a 3-word structure contaning a pointer to the first element, the length of the slice, and the capacity. The length is the upper bound for indexing operations like `x[i]` while the capacity is the upper bound for slice operations like `x[i:j]`.

Like slicing a string, slicing an array does not make a copy: it only creates a new structure holding a different pointer, length, and capacity. In the example, evaluating the composite literal `[]int{2, 3, 5, 7, 11}` creates a new array containing the five values and then sets the fields of the slice `x` to describe that array. The slice expression `x[1:3]` does not allocate more data: it just writes the fields of a new slice structure to refer to the same backing store. In the example, the length is 2—`y[0]` and `y[1]` are the only valid indexes—but the capacity is 4—`y[0:4]` is a valid slice expression. (See Effective Go <http://golang.org/doc/effective_go.html#slices> for more about length and capacity and how slices are used.)

 Because slices are multiword structures, not pointers, the slicing operation does not need to allocate memory, not even for the slice header, which can usually be kept on the stack. This representation makes slices about as cheap to use as passing around explicit pointer and length pairs in C. Go originally represented a slice as a pointer to the structure shown above, but doing so meant that every slice operation allocated a new memory object. Even with a fast allocator, that creates a lot of unnecessary work for the garbage collector, and we found that, as was the case with strings above, programs avoided slicing operations in favor of passing explicit indices. Removing the indirection and the allocation made slices cheap enough to avoid passing explicit indices in most cases.
