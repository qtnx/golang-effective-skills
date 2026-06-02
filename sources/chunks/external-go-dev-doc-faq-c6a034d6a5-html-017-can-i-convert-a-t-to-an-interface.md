---
source_name: "External Linked Documentation"
source_url: "https://go.dev/doc/faq"
source_path: "sources/raw/external/go-dev-doc-faq-c6a034d6a5.html"
license_ref: ""
---

## Types

### Can I convert a []T to an []interface{}?

Not directly. It is disallowed by the language specification because the two types do not have the same representation in memory. It is necessary to copy the elements individually to the destination slice. This example converts a slice of `int` to a slice of `interface{}`:

```go
t := []int{1, 2, 3, 4}
s := make([]interface{}, len(t))
for i, v := range t {
    s[i] = v
}

```

## Types

### Can I convert []T1 to []T2 if T1 and T2 have the same underlying type?

This last line of this code sample does not compile.

```go
type T1 int
type T2 int
var t1 T1
var x = T2(t1) // OK
var st1 []T1
var sx = ([]T2)(st1) // NOT OK

```

In Go, types are closely tied to methods, in that every named type has a (possibly empty) method set. The general rule is that you can change the name of the type being converted (and thus possibly change its method set) but you can’t change the name (and method set) of elements of a composite type. Go requires you to be explicit about type conversions.
