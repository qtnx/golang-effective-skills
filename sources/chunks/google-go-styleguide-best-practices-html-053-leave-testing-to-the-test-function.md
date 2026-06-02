---
source_name: "Google Go Style Guide"
source_url: "https://google.github.io/styleguide/go/"
source_path: "sources/raw/google-go-styleguide/best-practices.html"
license_ref: "sources/licenses/google-styleguide-LICENSE.txt"
---

### Leave testing to the `Test` function

Go distinguishes between “test helpers” and “assertion helpers”:

-
**Test helpers** are functions that do setup or cleanup tasks. All failures that occur in test helpers are expected to be failures of the environment (not from the code under test) — for example when a test database cannot be started because there are no more free ports on this machine. For functions like these, calling `t.Helper` is often appropriate to mark them as a test helper. See error handling in test helpers for more details.

-
**Assertion helpers** are functions that check the correctness of a system and fail the test if an expectation is not met. Assertion helpers are not considered idiomatic in Go.

The purpose of a test is to report pass/fail conditions of the code under test. The ideal place to fail a test is within the `Test` function itself, as that ensures that failure messages and the test logic are clear.

As your testing code grows, it may become necessary to factor out some functionality to separate functions. Standard software engineering considerations still apply, as _test code is still code_. If the functionality does not interact with the testing framework, then all of the usual rules apply. When the common code interacts with the framework, however, some care must be taken to avoid common pitfalls that can lead to uninformative failure messages and unmaintainable tests.

If many separate test cases require the same validation logic, arrange the test in one of the following ways instead of using assertion helpers or complex validation functions:

- Inline the logic (both the validation and the failure) in the `Test` function, even if it is repetitive. This works best in simple cases.
- If inputs are similar, consider unifying them into a table-driven test while keeping the logic inlined in the loop. This helps to avoid repetition while keeping the validation and failure in the `Test`.
- If there are multiple callers who need the same validation function but table tests are not suitable (typically because the inputs are not simple enough or the validation is required as part of a sequence of operations), arrange the validation function so that it returns a value (typically an `error`) rather than taking a `testing.T` parameter and using it to fail the test. Use logic within the `Test` to decide whether to fail, and to provide useful test failures. You can also create test helpers to factor out common boilerplate setup code.

The design outlined in the last point maintains orthogonality. For example, package `cmp` is not designed to fail tests, but rather to compare (and to diff) values. It therefore does not need to know about the context in which the comparison was made, since the caller can supply that. If your common testing code provides a `cmp.Transformer` for your data type, that can often be the simplest design. For other validations, consider returning an `error` value.

```go
// Good:
// polygonCmp returns a cmp.Option that equates s2 geometry objects up to
// some small floating-point error.
func polygonCmp() cmp.Option {
    return cmp.Options{
        cmp.Transformer("polygon", func(p *s2.Polygon) []*s2.Loop { return p.Loops() }),
        cmp.Transformer("loop", func(l *s2.Loop) []s2.Point { return l.Vertices() }),
        cmpopts.EquateApprox(0.00000001, 0),
        cmpopts.EquateEmpty(),
    }
}

func TestFenceposts(t *testing.T) {
    // This is a test for a fictional function, Fenceposts, which draws a fence
    // around some Place object. The details are not important, except that
    // the result is some object that has s2 geometry (github.com/golang/geo/s2)
    got := Fencepost(tomsDiner, 1*meter)
    if diff := cmp.Diff(want, got, polygonCmp()); diff != "" {
        t.Errorf("Fencepost(tomsDiner, 1m) returned unexpected diff (-want+got):\n%v", diff)
    }
}

func FuzzFencepost(f *testing.F) {
    // Fuzz test (https://go.dev/doc/fuzz) for the same.

    f.Add(tomsDiner, 1*meter)
    f.Add(school, 3*meter)

    f.Fuzz(func(t *testing.T, geo Place, padding Length) {
        got := Fencepost(geo, padding)
        // Simple reference implementation: not used in prod, but easy to
        // reason about and therefore useful to check against in random tests.
        reference := slowFencepost(geo, padding)

        // In the fuzz test, inputs and outputs can be large so don't
        // bother with printing a diff. cmp.Equal is enough.
        if !cmp.Equal(got, reference, polygonCmp()) {
            t.Errorf("Fencepost returned wrong placement")
        }
    })
}

```

The `polygonCmp` function is agnostic about how it’s called; it doesn’t take a concrete input type nor does it police what to do in case two objects don’t match. Therefore, more callers can make use of it.

**Note:** There is an analogy between test helpers and plain library code. Code in libraries should usually not panic except in rare circumstances; code called from a test should not stop the test unless there is no point in proceeding.
