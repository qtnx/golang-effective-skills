---
source_name: "Google Go Style Guide"
source_url: "https://google.github.io/styleguide/go/"
source_path: "sources/raw/google-go-styleguide/decisions.md"
license_ref: "sources/licenses/google-styleguide-LICENSE.txt"
---

## Language

### Use %q

<a id="TOC-UsePercentQ"></a>

Go's format functions (`fmt.Printf` etc.) have a `%q` verb which prints strings
inside double-quotation marks.

```go
// Good:
fmt.Printf("value %q looks like English text", someText)
```

Prefer using `%q` over doing the equivalent manually, using `%s`:

```go
// Bad:
fmt.Printf("value \"%s\" looks like English text", someText)
// Avoid manually wrapping strings with single-quotes too:
fmt.Printf("value '%s' looks like English text", someText)
```

Using `%q` is recommended in output intended for humans where the input value
could possibly be empty or contain control characters. It can be very hard to
notice a silent empty string, but `""` stands out clearly as such.

<a id="use-any"></a>

## Language

### Use any

Go 1.18 introduces an `any` type as an [alias] to `interface{}`. Because it is
an alias, `any` is equivalent to `interface{}` in many situations and in others
it is easily interchangeable via an explicit conversion. Prefer to use `any` in
new code.

[alias]: https://go.googlesource.com/proposal/+/master/design/18130-type-alias.md
