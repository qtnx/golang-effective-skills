---
source_name: "Google Go Style Guide"
source_url: "https://google.github.io/styleguide/go/"
source_path: "sources/raw/google-go-styleguide/decisions.md"
license_ref: "sources/licenses/google-styleguide-LICENSE.txt"
---

### Handle errors

<a id="TOC-HandleErrors"></a>

Code that encounters an error should make a deliberate choice about how to
handle it. It is not usually appropriate to discard errors using `_` variables.
If a function returns an error, do one of the following:

*   Handle and address the error immediately.
*   Return the error to the caller.
*   In exceptional situations, call [`log.Fatal`] or (if absolutely necessary)
    `panic`.

**Note:** `log.Fatalf` is not the standard library log. See [#logging].

In the rare circumstance where it is appropriate to ignore or discard an error
(for example a call to [`(*bytes.Buffer).Write`] that is documented to never
fail), an accompanying comment should explain why this is safe.

```go
// Good:
var b *bytes.Buffer

n, _ := b.Write(p) // never returns a non-nil error
```

For more discussion and examples of error handling, see
[Effective Go](http://golang.org/doc/effective_go.html#errors) and
[best practices](best-practices.md#error-handling).

[`(*bytes.Buffer).Write`]: https://pkg.go.dev/bytes#Buffer.Write

<a id="in-band-errors"></a>
