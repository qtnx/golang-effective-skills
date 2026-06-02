---
source_name: "External Linked Documentation"
source_url: "https://go.dev/doc/faq"
source_path: "sources/raw/external/go-dev-doc-faq-c6a034d6a5.html"
license_ref: ""
---

## Type Parameters

### Why can’t I use a more specific type for the receiver of a parameterized type?

The method declarations of a generic type are written with a receiver that includes the type parameter names. Perhaps because of the similarity of the syntax for specifying types at a call site, some have thought this provides a mechanism for producing a method customized for certain type arguments by naming a specific type in the receiver, such as `string`:

```go
type S[T any] struct { f T }

func (s S[string]) Add(t string) string {
    return s.f + t
}

```

This fails because the word `string` is taken by the compiler to be the name of the type argument in the method. The compiler error message will be something like “`operator + not defined on s.f (variable of type string)`”. This can be confusing because the `+` operator works fine on the predeclared type `string`, but the declaration has overwritten, for this method, the definition of `string`, and the operator does not work on that unrelated version of `string`. It’s valid to overwrite a predeclared name like this, but is an odd thing to do and often a mistake.
