---
source_name: "Google Go Style Guide"
source_url: "https://google.github.io/styleguide/go/"
source_path: "sources/raw/google-go-styleguide/decisions.html"
license_ref: "sources/licenses/google-styleguide-LICENSE.txt"
---

#### Matching braces

The closing half of a brace pair should always appear on a line with the same amount of indentation as the opening brace. One-line literals necessarily have this property. When the literal spans multiple lines, maintaining this property keeps the brace matching for literals the same as brace matching for common Go syntactic constructs like functions and `if` statements.

The most common mistake in this area is putting the closing brace on the same line as a value in a multi-line struct literal. In these cases, the line should end with a comma and the closing brace should appear on the next line.

```go
// Good:
good := []*Type{{Key: "value"}}

```

```go
// Good:
good := []*Type{
    {Key: "multi"},
    {Key: "line"},
}

```

```go
// Bad:
bad := []*Type{
    {Key: "multi"},
    {Key: "line"}}

```

```go
// Bad:
bad := []*Type{
    {
        Key: "value"},
}

```
