---
source_name: "Google Go Style Guide"
source_url: "https://google.github.io/styleguide/go/"
source_path: "sources/raw/google-go-styleguide/best-practices.html"
license_ref: "sources/licenses/google-styleguide-LICENSE.txt"
---

### Signal boosting

Sometimes a line of code looks like something common, but actually isn’t. One of the best examples of this is an `err == nil` check (since `err != nil` is much more common). The following two conditional checks are hard to distinguish:

```go
// Good:
if err := doSomething(); err != nil {
    // ...
}

```

```go
// Bad:
if err := doSomething(); err == nil {
    // ...
}

```

You can instead “boost” the signal of the conditional by adding a comment:

```go
// Good:
if err := doSomething(); err == nil { // if NO error
    // ...
}

```

The comment draws attention to the difference in the conditional.
