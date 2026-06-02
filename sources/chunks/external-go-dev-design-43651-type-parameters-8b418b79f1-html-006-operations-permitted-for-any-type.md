---
source_name: "External Linked Documentation"
source_url: "https://go.dev/design/43651-type-parameters"
source_path: "sources/raw/external/go-dev-design-43651-type-parameters-8b418b79f1.html"
license_ref: ""
---

## Design

### Operations permitted for any type

Before we discuss constraints further, let's briefly note what happens when the constraint is `any`. If a generic function uses the `any` constraint for a type parameter, as is the case for the `Print` method above, then any type argument is permitted for that parameter. The only operations that the generic function can use with values of that type parameter are those operations that are permitted for values of any type. In the example above, the `Print` function declares a variable `v` whose type is the type parameter `T`, and it passes that variable to a function.

The operations permitted for any type are:

- declare variables of those types
- assign other values of the same type to those variables
- pass those variables to functions or return them from functions
- take the address of those variables
- convert or assign values of those types to the type `interface{}`
- convert a value of type `T` to type `T` (permitted but useless)
- use a type assertion to convert an interface value to the type
- use the type as a case in a type switch
- define and use composite types that use those types, such as a slice of that type
- pass the type to some predeclared functions such as `new`

It's possible that future language changes will add other such operations, though none are currently anticipated.
