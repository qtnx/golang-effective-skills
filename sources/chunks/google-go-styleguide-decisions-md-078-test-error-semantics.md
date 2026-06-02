---
source_name: "Google Go Style Guide"
source_url: "https://google.github.io/styleguide/go/"
source_path: "sources/raw/google-go-styleguide/decisions.md"
license_ref: "sources/licenses/google-styleguide-LICENSE.txt"
---

### Test error semantics

When a unit test performs string comparisons or uses a vanilla `cmp` to check
that particular kinds of errors are returned for particular inputs, you may find
that your tests are brittle if any of those error messages are reworded in the
future. Since this has the potential to turn your unit test into a change
detector (see [TotT: Change-Detector Tests Considered Harmful][tott-350] ),
don't use string comparison to check what type of error your function returns.
However, it is permissible to use string comparisons to check that error
messages coming from the package under test satisfy certain properties, for
example, that it includes the parameter name.

Error values in Go typically have a component intended for human eyes and a
component intended for semantic control flow. Tests should seek to only test
semantic information that can be reliably observed, rather than display
information that is intended for human debugging, as this is often subject to
future changes. For guidance on constructing errors with semantic meaning see
[best-practices regarding errors](best-practices#error-handling). If an error
with insufficient semantic information is coming from a dependency outside your
control, consider filing a bug against the owner to help improve the API, rather
than relying on parsing the error message.

Within unit tests, it is common to only care whether an error occurred or not.
If so, then it is sufficient to only test whether the error was non-nil when you
expected an error. If you would like to test that the error semantically matches
some other error, then consider using [`errors.Is`] or `cmp` with
[`cmpopts.EquateErrors`].

> **Note:** If a test uses [`cmpopts.EquateErrors`] but all of its `wantErr`
> values are either `nil` or `cmpopts.AnyError`, then using `cmp` is
> [unnecessary mechanism](guide#least-mechanism). Simplify the code by making
> the want field a `bool`. You can then use a simple comparison with `!=`.
>
> ```go
> // Good:
> err := f(test.input)
> if gotErr := err != nil; gotErr != test.wantErr {
>     t.Errorf("f(%q) = %v, want error presence = %v", test.input, err, test.wantErr)
> }
> ```

See also
[GoTip #13: Designing Errors for Checking](https://google.github.io/styleguide/go/index.html#gotip).

[tott-350]: https://testing.googleblog.com/2015/01/testing-on-toilet-change-detector-tests.html
[`cmpopts.EquateErrors`]: https://pkg.go.dev/github.com/google/go-cmp/cmp/cmpopts#EquateErrors
[`errors.Is`]: https://pkg.go.dev/errors#Is

<a id="test-structure"></a>
