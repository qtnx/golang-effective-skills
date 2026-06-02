---
source_name: "Google Go Style Guide"
source_url: "https://google.github.io/styleguide/go/"
source_path: "sources/raw/google-go-styleguide/decisions.html"
license_ref: "sources/licenses/google-styleguide-LICENSE.txt"
---

#### Repeated type names

Repeated type names may be omitted from slice and map literals. This can be helpful in reducing clutter. A reasonable occasion for repeating the type names explicitly is when dealing with a complex type that is not common in your project, when the repetitive type names are on lines that are far apart and can remind the reader of the context.

```go
// Good:
good := []*Type{
    {A: 42},
    {A: 43},
}

```

```go
// Bad:
repetitive := []*Type{
    &Type{A: 42},
    &Type{A: 43},
}

```

```go
// Good:
good := map[Type1]*Type2{
    {A: 1}: {B: 2},
    {A: 3}: {B: 4},
}

```

```go
// Bad:
repetitive := map[Type1]*Type2{
    Type1{A: 1}: &Type2{B: 2},
    Type1{A: 3}: &Type2{B: 4},
}

```

**Tip:** If you want to remove repetitive type names in struct literals, you can run `gofmt -s`.
