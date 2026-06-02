---
source_name: "Google Go Style Guide"
source_url: "https://google.github.io/styleguide/go/"
source_path: "sources/raw/google-go-styleguide/decisions.md"
license_ref: "sources/licenses/google-styleguide-LICENSE.txt"
---

## Test structure

### Use package `testing`

The Go standard library provides the [`testing` package]. This is the only
testing framework permitted for Go code in the Google codebase. In particular,
[assertion libraries](#assert) and third-party testing frameworks are not
allowed.

The `testing` package provides a minimal but complete set of functionality for
writing good tests:

*   Top-level tests
*   Benchmarks
*   [Runnable examples](https://blog.golang.org/examples)
*   Subtests
*   Logging
*   Failures and fatal failures

These are designed to work cohesively with core language features like
[composite literal] and [if-with-initializer] syntax to enable test authors to
write [clear, readable, and maintainable tests].

[`testing` package]: https://pkg.go.dev/testing
[composite literal]: https://go.dev/ref/spec#Composite_literals
[if-with-initializer]: https://go.dev/ref/spec#If_statements

<a id="non-decisions"></a>

# Go Style Decisions

## Non-decisions

A style guide cannot enumerate positive prescriptions for all matters, nor can
it enumerate all matters about which it does not offer an opinion. That said,
here are a few things where the readability community has previously debated and
has not achieved consensus about.

*   **Local variable initialization with zero value**. `var i int` and `i := 0`
    are equivalent. See also [initialization best practices].
*   **Empty composite literal vs. `new` or `make`**. `&File{}` and `new(File)`
    are equivalent. So are `map[string]bool{}` and `make(map[string]bool)`. See
    also [composite declaration best practices].
*   **got, want argument ordering in cmp.Diff calls**. Be locally consistent,
    and [include a legend](#print-diffs) in your failure message.
*   **`errors.New` vs `fmt.Errorf` on non-formatted strings**.
    `errors.New("foo")` and `fmt.Errorf("foo")` may be used interchangeably.

If there are special circumstances where they come up again, the readability
mentor might make an optional comment, but in general the author is free to pick
the style they prefer in the given situation.

Naturally, if anything not covered by the style guide does need more discussion,
authors are welcome to ask -- either in the specific review, or on internal
message boards.

[composite declaration best practices]: https://google.github.io/styleguide/go/best-practices#vardeclcomposite
[initialization best practices]: https://google.github.io/styleguide/go/best-practices#vardeclinitialization
