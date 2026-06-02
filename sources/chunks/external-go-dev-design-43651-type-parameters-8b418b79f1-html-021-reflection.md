---
source_name: "External Linked Documentation"
source_url: "https://go.dev/design/43651-type-parameters"
source_path: "sources/raw/external/go-dev-design-43651-type-parameters-8b418b79f1.html"
license_ref: ""
---

## Design

### Reflection

We do not propose to change the reflect package in any way. When a type or function is instantiated, all of the type parameters will become ordinary non-generic types. The `String` method of a `reflect.Type` value of an instantiated type will return the name with the type arguments in square brackets. For example, `List[int]`.

It's impossible for non-generic code to refer to generic code without instantiating it, so there is no reflection information for uninstantiated generic types or functions.

## Design

### Implementation

Russ Cox famously observed <https://research.swtch.com/generic> that generics require choosing among slow programmers, slow compilers, or slow execution times.

We believe that this design permits different implementation choices. Code may be compiled separately for each set of type arguments, or it may be compiled as though each type argument is handled similarly to an interface type with method calls, or there may be some combination of the two.

In other words, this design permits people to stop choosing slow programmers, and permits the implementation to decide between slow compilers (compile each set of type arguments separately) or slow execution times (use method calls for each operation on a value of a type argument).
