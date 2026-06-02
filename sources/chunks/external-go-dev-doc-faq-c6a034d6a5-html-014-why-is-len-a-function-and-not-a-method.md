---
source_name: "External Linked Documentation"
source_url: "https://go.dev/doc/faq"
source_path: "sources/raw/external/go-dev-doc-faq-c6a034d6a5.html"
license_ref: ""
---

## Types

### Why is `len` a function and not a method?

We debated this issue but decided implementing `len` and friends as functions was fine in practice and didn’t complicate questions about the interface (in the Go type sense) of basic types.

## Types

### Why does Go not support overloading of methods and operators?

Method dispatch is simplified if it doesn’t need to do type matching as well. Experience with other languages told us that having a variety of methods with the same name but different signatures was occasionally useful but that it could also be confusing and fragile in practice. Matching only by name and requiring consistency in the types was a major simplifying decision in Go’s type system.

Regarding operator overloading, it seems more a convenience than an absolute requirement. Again, things are simpler without it.
