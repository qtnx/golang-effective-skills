---
source_name: "External Linked Documentation"
source_url: "https://go.dev/doc/faq"
source_path: "sources/raw/external/go-dev-doc-faq-c6a034d6a5.html"
license_ref: ""
---

## Type Parameters

### Why does Go use square brackets for type parameter lists?

Java and C++ use angle brackets for type parameter lists, as in Java `List<Integer>` and C++ `std::vector<int>`. However, that option was not available for Go, because it leads to a syntactic problem: when parsing code within a function, such as `v := F<T>`, at the point of seeing the `<` it’s ambiguous whether we are seeing an instantiation or an expression using the `<` operator. This is very difficult to resolve without type information.

For example, consider a statement like

```go

    a, b = w < x, y > (z)

```

Without type information, it is impossible to decide whether the right hand side of the assignment is a pair of expressions (`w < x` and `y > z`), or whether it is a generic function instantiation and call that returns two result values (`(w<x, y>)(z)`).

It is a key design decision of Go that parsing be possible without type information, which seems impossible when using angle brackets for generics.

Go is not unique or original in using square brackets; there are other languages such as Scala that also use square brackets for generic code.
