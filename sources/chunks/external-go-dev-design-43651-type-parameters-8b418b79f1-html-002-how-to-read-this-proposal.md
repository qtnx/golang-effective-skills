---
source_name: "External Linked Documentation"
source_url: "https://go.dev/design/43651-type-parameters"
source_path: "sources/raw/external/go-dev-design-43651-type-parameters-8b418b79f1.html"
license_ref: ""
---

# Type Parameters Proposal

## How to read this proposal

This document is long. Here is some guidance on how to read it.

- We start with a high level overview, describing the concepts very briefly.
- We then explain the full design starting from scratch, introducing the details as we need them, with simple examples.
- After the design is completely described, we discuss implementation, some issues with the design, and a comparison with other approaches to generics.
- We then present several complete examples of how this design would be used in practice.
- Following the examples some minor details are discussed in an appendix.

# Type Parameters Proposal

## Very high level overview

This section explains the changes suggested by the design very briefly. This section is intended for people who are already familiar with how generics would work in a language like Go. These concepts will be explained in detail in the following sections.

- Functions can have an additional type parameter list that uses square brackets but otherwise looks like an ordinary parameter list: `func F[T any](p T) { ... }`.
- These type parameters can be used by the regular parameters and in the function body.
- Types can also have a type parameter list: `type M[T any] []T`.
- Each type parameter has a type constraint, just as each ordinary parameter has a type: `func F[T Constraint](p T) { ... }`.
- Type constraints are interface types.
- The new predeclared name `any` is a type constraint that permits any type.
- Interface types used as type constraints can embed additional elements to restrict the set of type arguments that satisfy the contraint:
- an arbitrary type `T` restricts to that type
- an approximation element `~T` restricts to all types whose underlying type is `T`
- a union element `T1 | T2 | ...` restricts to any of the listed elements

- Generic functions may only use operations supported by all the types permitted by the constraint.
- Using a generic function or type requires passing type arguments.
- Type inference permits omitting the type arguments of a function call in common cases.

In the following sections we work through each of these language changes in great detail. You may prefer to skip ahead to the examples to see what generic code written to this design will look like in practice.
