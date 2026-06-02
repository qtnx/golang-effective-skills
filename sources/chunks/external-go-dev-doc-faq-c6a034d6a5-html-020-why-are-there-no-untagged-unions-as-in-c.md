---
source_name: "External Linked Documentation"
source_url: "https://go.dev/doc/faq"
source_path: "sources/raw/external/go-dev-doc-faq-c6a034d6a5.html"
license_ref: ""
---

## Types

### Why are there no untagged unions, as in C?

Untagged unions would violate Go’s memory safety guarantees.

## Types

### Why does Go not have variant types?

Variant types, also known as algebraic types, provide a way to specify that a value might take one of a set of other types, but only those types. A common example in systems programming would specify that an error is, say, a network error, a security error or an application error and allow the caller to discriminate the source of the problem by examining the type of the error. Another example is a syntax tree in which each node can be a different type: declaration, statement, assignment and so on.

We considered adding variant types to Go, but after discussion decided to leave them out because they overlap in confusing ways with interfaces. What would happen if the elements of a variant type were themselves interfaces?

Also, some of what variant types address is already covered by the language. The error example is easy to express using an interface value to hold the error and a type switch to discriminate cases. The syntax tree example is also doable, although not as elegantly.
