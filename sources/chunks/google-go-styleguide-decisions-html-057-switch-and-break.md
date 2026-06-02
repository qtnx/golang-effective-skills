---
source_name: "Google Go Style Guide"
source_url: "https://google.github.io/styleguide/go/"
source_path: "sources/raw/google-go-styleguide/decisions.html"
license_ref: "sources/licenses/google-styleguide-LICENSE.txt"
---

### `switch` and `break`

Do not use `break` statements without target labels at the ends of `switch` clauses; they are redundant. Unlike in C and Java, `switch` clauses in Go automatically break, and a `fallthrough` statement is needed to achieve the C-style behavior. Use a comment rather than `break` if you want to clarify the purpose of an empty clause.

```go
// Good:
switch x {
case "A", "B":
    buf.WriteString(x)
case "C":
    // handled outside of the switch statement
default:
    return fmt.Errorf("unknown value: %q", x)
}

```

```go
// Bad:
switch x {
case "A", "B":
    buf.WriteString(x)
    break // this break is redundant
case "C":
    break // this break is redundant
default:
    return fmt.Errorf("unknown value: %q", x)
}

```

**Note:** If a `switch` clause is within a `for` loop, using `break` within `switch` does not exit the enclosing `for` loop.

```go
for {
  switch x {
  case "A":
     break // exits the switch, not the loop
  }
}

```

To escape the enclosing loop, use a label on the `for` statement:

```go
loop:
  for {
    switch x {
    case "A":
       break loop // exits the loop
    }
  }

```
