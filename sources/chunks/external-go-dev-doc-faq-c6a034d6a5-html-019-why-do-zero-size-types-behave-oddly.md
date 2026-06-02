---
source_name: "External Linked Documentation"
source_url: "https://go.dev/doc/faq"
source_path: "sources/raw/external/go-dev-doc-faq-c6a034d6a5.html"
license_ref: ""
---

## Types

### Why do zero-size types behave oddly?

Go supports zero-size types, such as a struct with no fields (`struct{}`) or an array with no elements (`[0]byte`). There is nothing you can store in a zero-size type, but these types are sometimes useful when no value is needed, as in `map[int]struct{}` or a type that has methods but no value.

Different variables with a zero-size type may be placed at the same location in memory. This is safe as no value can be stored in those variables.

Moreover, the language does not make any guarantees as to whether pointers to two different zero-size variables will compare equal or not. Such comparisons may even return `true` at one point in the program and then return `false` at a different point, depending on exactly how the program is compiled and executed.

A separate issue with zero-size types is that a pointer to a zero-size struct field must not overlap with a pointer to a different object in memory. That could cause confusion in the garbage collector. This means that if the last field in a struct is zero-size, the struct will be padded to ensure that a pointer to the last field does not overlap with memory that immediately follows the struct. Thus, this program:

```go
func main() {
    type S struct {
        f1 byte
        f2 struct{}
    }
    fmt.Println(unsafe.Sizeof(S{}))
}

```

will print `2`, not `1`, in most Go implementations.
