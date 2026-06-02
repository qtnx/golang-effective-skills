---
source_name: "External Linked Documentation"
source_url: "https://go.dev/design/43651-type-parameters"
source_path: "sources/raw/external/go-dev-design-43651-type-parameters-8b418b79f1.html"
license_ref: ""
---

## Design

### The `any` constraint

Now that we know that constraints are simply interface types, we can explain what `any` means as a constraint. As shown above, the `any` constraint permits any type as a type argument and only permits the function to use the operations permitted for any type. The interface type for that is the empty interface: `interface{}`. So we could write the `Print` example as

```go
// Print prints the elements of any slice.
// Print has a type parameter T and has a single (non-type)
// parameter s which is a slice of that type parameter.
func Print[T interface{}](s []T) {
	// same as above
}

```

However, it‘s tedious to have to write `interface{}` every time you write a generic function that doesn’t impose constraints on its type parameters. So in this design we suggest a type constraint `any` that is equivalent to `interface{}`. This will be a predeclared name, implicitly declared in the universe block. It will not be valid to use `any` as anything other than a type constraint.

(Note: clearly we could make `any` generally available as an alias for `interface{}`, or as a new defined type defined as `interface{}`. However, we don't want this design, which is about generics, to lead to a possibly significant change to non-generic code. Adding `any` as a general purpose name for `interface{}` can and should be discussed separately <https://golang.org/issue/33232>).
