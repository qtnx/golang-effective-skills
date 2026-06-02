---
source_name: "Google Go Style Guide"
source_url: "https://google.github.io/styleguide/go/"
source_path: "sources/raw/google-go-styleguide/decisions.html"
license_ref: "sources/licenses/google-styleguide-LICENSE.txt"
---

### Returning errors

Use `error` to signal that a function can fail. By convention, `error` is the last result parameter.

```go
// Good:
func Good() error { /* ... */ }

```

Returning a `nil` error is the idiomatic way to signal a successful operation that could otherwise fail. If a function returns an error, callers must treat all non-error return values as unspecified unless explicitly documented otherwise. Commonly, the non-error return values are their zero values, but this cannot be assumed.

```go
// Good:
func GoodLookup() (*Result, error) {
    // ...
    if err != nil {
        return nil, err
    }
    return res, nil
}

```

Exported functions that return errors should return them using the `error` type. Concrete error types are susceptible to subtle bugs: a concrete `nil` pointer can get wrapped into an interface and thus become a non-nil value (see the Go FAQ entry on the topic).

```go
// Bad:
func Bad() *os.PathError { /*...*/ }

```

**Tip:** A function that takes a `context.Context` argument should usually return an `error` so that the caller can determine if the context was cancelled while the function was running.
