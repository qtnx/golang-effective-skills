---
source_name: "External Linked Documentation"
source_url: "https://go.dev/ref/spec"
source_path: "sources/raw/external/go-dev-ref-spec-3c5b020879.html"
license_ref: ""
---

## Types

### Map types

 A map is an unordered group of elements of one type, called the element type, indexed by a set of unique _keys_ of another type, called the key type. The value of an uninitialized map is `nil`.

```go

MapType = "map" "[" KeyType "]" ElementType .
KeyType = Type .

```

 The comparison operators `==` and `!=` must be fully defined for operands of the key type; thus the key type must not be a function, map, or slice. If the key type is an interface type, these comparison operators must be defined for the dynamic key values; failure will cause a run-time panic.

```go

map[string]int
map[*T]struct{ x, y float64 }
map[string]interface{}

```

 The number of map elements is called its length. For a map `m`, it can be discovered using the built-in function `len` and may change during execution. Elements may be added during execution using assignments and retrieved with index expressions; they may be removed with the `delete` and `clear` built-in function.

 A new, empty map value is made using the built-in function `make`, which takes the map type and an optional capacity hint as arguments:

```go

make(map[string]int)
make(map[string]int, 100)

```

 The initial capacity does not bound its size: maps grow to accommodate the number of items stored in them, with the exception of `nil` maps. A `nil` map is equivalent to an empty map except that no elements may be added.
