---
source_name: "External Linked Documentation"
source_url: "https://go.dev/doc/faq"
source_path: "sources/raw/external/go-dev-doc-faq-c6a034d6a5.html"
license_ref: ""
---

# Frequently Asked Questions (FAQ)

## Control Flow

### Why does Go not have the `?:` operator?

There is no ternary testing operation in Go. You may use the following to achieve the same result:

```go
if expr {
    n = trueVal
} else {
    n = falseVal
}

```

The reason `?:` is absent from Go is that the language’s designers had seen the operation used too often to create impenetrably complex expressions. The `if-else` form, although longer, is unquestionably clearer. A language needs only one conditional control flow construct.

## Type Parameters
### Why does Go have type parameters?

Type parameters permit what is known as generic programming, in which functions and data structures are defined in terms of types that are specified later, when those functions and data structures are used. For example, they make it possible to write a function that returns the minimum of two values of any ordered type, without having to write a separate version for each possible type. For a more in-depth explanation with examples see the blog post Why Generics?.
