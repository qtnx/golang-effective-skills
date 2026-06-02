---
source_name: "External Linked Documentation"
source_url: "https://go.dev/doc/faq"
source_path: "sources/raw/external/go-dev-doc-faq-c6a034d6a5.html"
license_ref: ""
---

## Design

### Why does Go not have feature X?

Every language contains novel features and omits someone’s favorite feature. Go was designed with an eye on felicity of programming, speed of compilation, orthogonality of concepts, and the need to support features such as concurrency and garbage collection. Your favorite feature may be missing because it doesn’t fit, because it affects compilation speed or clarity of design, or because it would make the fundamental system model too difficult.

If it bothers you that Go is missing feature _X_, please forgive us and investigate the features that Go does have. You might find that they compensate in interesting ways for the lack of _X_.

## Design

### When did Go get generic types?

The Go 1.18 release added type parameters to the language. This permits a form of polymorphic or generic programming. See the language spec and the proposal for details.
