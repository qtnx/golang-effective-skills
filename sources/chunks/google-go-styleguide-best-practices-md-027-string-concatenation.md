---
source_name: "Google Go Style Guide"
source_url: "https://google.github.io/styleguide/go/"
source_path: "sources/raw/google-go-styleguide/best-practices.md"
license_ref: "sources/licenses/google-styleguide-LICENSE.txt"
---

# Go Style Best Practices

## String concatenation

There are several ways to concatenate strings in Go. Some examples include:

*   The "+" operator
*   `fmt.Sprintf`
*   `strings.Builder`
*   `text/template`
*   `safehtml/template`

Though there is no one-size-fits-all rule for which to choose, the following
guidance outlines when each method is preferred.

<a id="string-concat-simple"></a>

### Prefer "+" for simple cases

Prefer using "+" when concatenating few strings. This method is syntactically
the simplest and requires no import.

```go
// Good:
key := "projectid: " + p
```

<a id="string-concat-fmt"></a>

### Prefer `fmt.Sprintf` when formatting

Prefer using `fmt.Sprintf` when building a complex string with formatting. Using
many "+" operators may obscure the end result.

```go
// Good:
str := fmt.Sprintf("%s [%s:%d]-> %s", src, qos, mtu, dst)
```

```go
// Bad:
bad := src.String() + " [" + qos.String() + ":" + strconv.Itoa(mtu) + "]-> " + dst.String()
```

**Best Practice:** When the output of the string-building operation is an
`io.Writer`, don't construct a temporary string with `fmt.Sprintf` just to send
it to the Writer. Instead, use `fmt.Fprintf` to emit to the Writer directly.

When the formatting is even more complex, prefer [`text/template`] or
[`safehtml/template`] as appropriate.

[`text/template`]: https://pkg.go.dev/text/template
[`safehtml/template`]: https://pkg.go.dev/github.com/google/safehtml/template

<a id="string-concat-piecemeal"></a>

### Prefer `strings.Builder` for constructing a string piecemeal

Prefer using `strings.Builder` when building a string bit-by-bit.
`strings.Builder` takes amortized linear time, whereas "+" and `fmt.Sprintf`
take quadratic time when called sequentially to form a larger string.

```go
// Good:
b := new(strings.Builder)
for i, d := range digitsOfPi {
    fmt.Fprintf(b, "the %d digit of pi is: %d\n", i, d)
}
str := b.String()
```

**Note:** For more discussion, see
[GoTip #29: Building Strings Efficiently](https://google.github.io/styleguide/go/index.html#gotip).

<a id="string-constants"></a>

### Constant strings

Prefer to use backticks (\`) when constructing constant, multi-line string
literals.

```go
// Good:
usage := `Usage:

custom_tool [args]`
```

```go
// Bad:
usage := "" +
  "Usage:\n" +
  "\n" +
  "custom_tool [args]"
```

<a id="globals"></a>
