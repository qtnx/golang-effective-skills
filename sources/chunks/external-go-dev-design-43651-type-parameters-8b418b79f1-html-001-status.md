---
source_name: "External Linked Documentation"
source_url: "https://go.dev/design/43651-type-parameters"
source_path: "sources/raw/external/go-dev-design-43651-type-parameters-8b418b79f1.html"
license_ref: ""
---

# Type Parameters Proposal

Type Parameters Proposal
# Type Parameters Proposal
Ian Lance Taylor
Robert Griesemer
August 20, 2021
## Status

This is the design for adding generic programming using type parameters to the Go language. This design has been proposed and accepted <https://golang.org/issue/43651> as a future language change. We currently expect that this change will be available in the Go 1.18 release in early 2022.

# Type Parameters Proposal

## Abstract

We suggest extending the Go language to add optional type parameters to type and function declarations. Type parameters are constrained by interface types. Interface types, when used as type constraints, support embedding additional elements that may be used to limit the set of types that satisfy the constraint. Parameterized types and functions may use operators with type parameters, but only when permitted by all types that satisfy the parameter's constraint. Type inference via a unification algorithm permits omitting type arguments from function calls in many cases. The design is fully backward compatible with Go 1.
