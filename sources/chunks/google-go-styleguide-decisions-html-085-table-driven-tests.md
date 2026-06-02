---
source_name: "Google Go Style Guide"
source_url: "https://google.github.io/styleguide/go/"
source_path: "sources/raw/google-go-styleguide/decisions.html"
license_ref: "sources/licenses/google-styleguide-LICENSE.txt"
---

### Table-driven tests

Use table-driven tests when many different test cases can be tested using similar testing logic.

- When testing whether the actual output of a function is equal to the expected output. For example, the many tests of `fmt.Sprintf` or the minimal snippet below.
- When testing whether the outputs of a function always conform to the same set of invariants. For example, tests for `net.Dial`.

Here is the minimal structure of a table-driven test. If needed, you may use different names or add extra facilities such as subtests or setup and cleanup functions. Always keep useful test failures in mind.

```go
// Good:
func TestCompare(t *testing.T) {
    compareTests := []struct {
        a, b string
        want int
    }{
        {"", "", 0},
        {"a", "", 1},
        {"", "a", -1},
        {"abc", "abc", 0},
        {"ab", "abc", -1},
        {"abc", "ab", 1},
        {"x", "ab", 1},
        {"ab", "x", -1},
        {"x", "a", 1},
        {"b", "x", -1},
        // test runtime·memeq's chunked implementation
        {"abcdefgh", "abcdefgh", 0},
        {"abcdefghi", "abcdefghi", 0},
        {"abcdefghi", "abcdefghj", -1},
    }

    for _, test := range compareTests {
        got := Compare(test.a, test.b)
        if got != test.want {
            t.Errorf("Compare(%q, %q) = %v, want %v", test.a, test.b, got, test.want)
        }
    }
}

```

**Note**: The failure messages in this example above fulfill the guidance to identify the function and identify the input. There’s no need to identify the row numerically.

When some test cases need to be checked using different logic from other test cases, it is appropriate to write multiple test functions, as explained in GoTip #50: Disjoint Table Tests.

When the additional test cases are simple (e.g., basic error checking) and don’t introduce conditionalized code flow in the table test’s loop body, it’s permissible to include that case in the existing test, though be careful using logic like this. What starts simple today can organically grow into something unmaintainable.

For example:

```go
func TestDivide(t *testing.T) {
    tests := []struct {
        dividend, divisor int
        want              int
        wantErr           bool
    }{
        {
            dividend: 4,
            divisor:  2,
            want:     2,
        },
        {
            dividend: 10,
            divisor:  2,
            want:     5,
        },
        {
            dividend: 1,
            divisor:  0,
            wantErr:  true,
        },
    }

    for _, test := range tests {
        got, err := Divide(test.dividend, test.divisor)
        if (err != nil) != test.wantErr {
            t.Errorf("Divide(%d, %d) error = %v, want error presence = %t", test.dividend, test.divisor, err, test.wantErr)
        }

        // In this example, we're only testing the value result when the tested function didn't fail.
        if err != nil {
            continue
        }

        if got != test.want {
            t.Errorf("Divide(%d, %d) = %d, want %d", test.dividend, test.divisor, got, test.want)
        }
    }
}

```

More complicated logic in your test code, like complex error checking based on conditional differences in test setup (often based on table test input parameters), can be difficult to understand when each entry in a table has specialized logic based on the inputs. If test cases have different logic but identical setup, a sequence of subtests within a single test function might be more readable. A test helper may also be useful for simplifying test setup in order to maintain the readability of a test body.

You can combine table-driven tests with multiple test functions. For example, when testing that a function’s output exactly matches the expected output and that the function returns a non-nil error for an invalid input, then writing two separate table-driven test functions is the best approach: one for normal non-error outputs, and one for error outputs.
