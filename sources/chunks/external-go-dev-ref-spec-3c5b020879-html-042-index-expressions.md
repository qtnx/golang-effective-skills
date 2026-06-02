---
source_name: "External Linked Documentation"
source_url: "https://go.dev/ref/spec"
source_path: "sources/raw/external/go-dev-ref-spec-3c5b020879.html"
license_ref: ""
---

## Expressions

### Index expressions

 A primary expression of the form

```go

a[x]

```

 denotes the element of the array, pointer to array, slice, string or map `a` indexed by `x`. The value `x` is called the _index_ or _map key_, respectively. The following rules apply:

 If `a` is neither a map nor a type parameter:

- the index `x` must be an untyped constant, or its type must be an integer or a type parameter whose type set contains only integer types
- a constant index must be non-negative and representable by a value of type `int`
- a constant index that is untyped is given type `int`
- the index `x` is _in range_ if `0 <= x < len(a)`, otherwise it is _out of range_

 For `a` of array type `A`:

- a constant index must be in range
- if `x` is out of range at run time, a run-time panic occurs
- `a[x]` is the array element at index `x` and the type of `a[x]` is the element type of `A`

 For `a` of pointer to array type:

- `a[x]` is shorthand for `(*a)[x]`

 For `a` of slice type `S`:

- if `x` is out of range at run time, a run-time panic occurs
- `a[x]` is the slice element at index `x` and the type of `a[x]` is the element type of `S`

 For `a` of string type:

- a constant index must be in range if the string `a` is also constant
- if `x` is out of range at run time, a run-time panic occurs
- `a[x]` is the non-constant byte value at index `x` and the type of `a[x]` is `byte`
- `a[x]` may not be assigned to

 For `a` of map type `M`:

- `x`'s type must be assignable to the key type of `M`
- if the map contains an entry with key `x`, `a[x]` is the map element with key `x` and the type of `a[x]` is the element type of `M`
- if the map is `nil` or does not contain such an entry, `a[x]` is the zero value for the element type of `M`

 For `a` of type parameter type `P`:

- The index expression `a[x]` must be valid for values of all types in `P`'s type set.
- The element types of all types in `P`'s type set must be identical. In this context, the element type of a string type is `byte`.
- If there is a map type in the type set of `P`, all types in that type set must be map types, and the respective key types must be all identical.
- `a[x]` is the array, slice, or string element at index `x`, or the map element with key `x` of the type argument that `P` is instantiated with, and the type of `a[x]` is the type of the (identical) element types.
- `a[x]` may not be assigned to if `P`'s type set includes string types.

 Otherwise `a[x]` is illegal.

 An index expression on a map `a` of type `map[K]V` used in an assignment statement or initialization of the special form

```go

v, ok = a[x]
v, ok := a[x]
var v, ok = a[x]

```

 yields an additional untyped boolean value. The value of `ok` is `true` if the key `x` is present in the map, and `false` otherwise.

 Assigning to an element of a `nil` map causes a run-time panic.
