---
source_name: "Google Go Style Guide"
source_url: "https://google.github.io/styleguide/go/"
source_path: "sources/raw/google-go-styleguide/decisions.md"
license_ref: "sources/licenses/google-styleguide-LICENSE.txt"
---

#### Cuddled braces

Dropping whitespace between braces (aka "cuddling" them) for slice and array
literals is only permitted when both of the following are true.

*   The [indentation matches](#literal-matching-braces)
*   The inner values are also literals or proto builders (i.e. not a variable or
    other expression)

```go
// Good:
good := []*Type{
    { // Not cuddled
        Field: "value",
    },
    {
        Field: "value",
    },
}
```

```go
// Good:
good := []*Type{{ // Cuddled correctly
    Field: "value",
}, {
    Field: "value",
}}
```

```go
// Good:
good := []*Type{
    first, // Can't be cuddled
    {Field: "second"},
}
```

```go
// Good:
okay := []*pb.Type{pb.Type_builder{
    Field: "first", // Proto Builders may be cuddled to save vertical space
}.Build(), pb.Type_builder{
    Field: "second",
}.Build()}
```

```go
// Bad:
bad := []*Type{
    first,
    {
        Field: "second",
    }}
```

<a id="literal-repeated-type-names"></a>
