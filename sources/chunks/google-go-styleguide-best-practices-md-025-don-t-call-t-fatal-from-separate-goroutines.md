---
source_name: "Google Go Style Guide"
source_url: "https://google.github.io/styleguide/go/"
source_path: "sources/raw/google-go-styleguide/best-practices.md"
license_ref: "sources/licenses/google-styleguide-LICENSE.txt"
---

## Tests

### Don't call `t.Fatal` from separate goroutines

As [documented in package testing](https://pkg.go.dev/testing#T), it is
incorrect to call `t.FailNow`, `t.Fatal`, etc. from any goroutine but the one
running the Test function (or the subtest). If your test starts new goroutines,
they must not call these functions from inside these goroutines.

[Test helpers](#test-functions) usually don't signal failure from new
goroutines, and therefore it is all right for them to use `t.Fatal`. If in
doubt, call `t.Error` and return instead.

```go
// Good:
func TestRevEngine(t *testing.T) {
    engine, err := Start()
    if err != nil {
        t.Fatalf("Engine failed to start: %v", err)
    }

    num := 11
    var wg sync.WaitGroup
    wg.Add(num)
    for i := 0; i < num; i++ {
        go func() {
            defer wg.Done()
            if err := engine.Vroom(); err != nil {
                // This cannot be t.Fatalf.
                t.Errorf("No vroom left on engine: %v", err)
                return
            }
            if rpm := engine.Tachometer(); rpm > 1e6 {
                t.Errorf("Inconceivable engine rate: %d", rpm)
            }
        }()
    }
    wg.Wait()

    if seen := engine.NumVrooms(); seen != num {
        t.Errorf("engine.NumVrooms() = %d, want %d", seen, num)
    }
}
```

Adding `t.Parallel` to a test or subtest does not make it unsafe to call
`t.Fatal`.

When all calls to the `testing` API are in the [test function](#test-functions),
it is usually easy to spot incorrect usage because the `go` keyword is plain to
see. Passing `testing.T` arguments around makes tracking such usage harder.
Typically, the reason for passing these arguments is to introduce a test helper,
and those should not depend on the system under test. Therefore, if a test
helper [registers a fatal test failure](#test-helper-error-handling), it can and
should do so from the test's goroutine.

<a id="t-field-names"></a>
