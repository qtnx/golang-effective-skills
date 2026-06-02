---
source_name: "External Linked Documentation"
source_url: "https://go.dev/doc/faq"
source_path: "sources/raw/external/go-dev-doc-faq-c6a034d6a5.html"
license_ref: ""
---

## Type Parameters

### Why can’t the compiler infer the type argument in my program?

There are many cases where a programmer can easily see what the type argument for a generic type or function must be, but the language does not permit the compiler to infer it. Type inference is intentionally limited to ensure that there is never any confusion as to which type is inferred. Experience with other languages suggests that unexpected type inference can lead to considerable confusion when reading and debugging a program. It is always possible to specify the explicit type argument to be used in the call. In the future new forms of inference may be supported, as long as the rules remain simple and clear.
