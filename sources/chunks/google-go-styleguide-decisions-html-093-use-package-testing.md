---
source_name: "Google Go Style Guide"
source_url: "https://google.github.io/styleguide/go/"
source_path: "sources/raw/google-go-styleguide/decisions.html"
license_ref: "sources/licenses/google-styleguide-LICENSE.txt"
---

### Use package `testing`

The Go standard library provides the `testing` package. This is the only testing framework permitted for Go code in the Google codebase. In particular, assertion libraries and third-party testing frameworks are not allowed.

The `testing` package provides a minimal but complete set of functionality for writing good tests:

- Top-level tests
- Benchmarks
- Runnable examples
- Subtests
- Logging
- Failures and fatal failures

These are designed to work cohesively with core language features like composite literal and if-with-initializer syntax to enable test authors to write [clear, readable, and maintainable tests].
