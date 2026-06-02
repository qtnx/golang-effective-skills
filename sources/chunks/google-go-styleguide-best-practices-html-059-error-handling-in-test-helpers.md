---
source_name: "Google Go Style Guide"
source_url: "https://google.github.io/styleguide/go/"
source_path: "sources/raw/google-go-styleguide/best-practices.html"
license_ref: "sources/licenses/google-styleguide-LICENSE.txt"
---

### Error handling in test helpers

**Note:** This section discusses test helpers in the sense Go uses the term: functions that perform test setup and cleanup, not common assertion facilities. See the test functions section for more discussion.

Operations performed by a test helper sometimes fail. For example, setting up a directory with files involves I/O, which can fail. When test helpers fail, their failure often signifies that the test cannot continue, since a setup precondition failed. When this happens, prefer calling one of the `Fatal` functions in the helper:

```go
// Good:
func mustAddGameAssets(t *testing.T, dir string) {
    t.Helper()
    if err := os.WriteFile(path.Join(dir, "pak0.pak"), pak0, 0644); err != nil {
        t.Fatalf("Setup failed: could not write pak0 asset: %v", err)
    }
    if err := os.WriteFile(path.Join(dir, "pak1.pak"), pak1, 0644); err != nil {
        t.Fatalf("Setup failed: could not write pak1 asset: %v", err)
    }
}

```

This keeps the calling side cleaner than if the helper were to return the error to the test itself:

```go
// Bad:
func addGameAssets(t *testing.T, dir string) error {
    t.Helper()
    if err := os.WriteFile(path.Join(d, "pak0.pak"), pak0, 0644); err != nil {
        return err
    }
    if err := os.WriteFile(path.Join(d, "pak1.pak"), pak1, 0644); err != nil {
        return err
    }
    return nil
}

```

**Warning:** It is not always safe to call `t.Fatal` and similar functions. More details here.

The failure message should include a description of what happened. This is important, as you may be providing a testing API to many users, especially as the number of error-producing steps in the helper increases. When the test fails, the user should know where, and why.

**Tip:** Go 1.14 introduced a `t.Cleanup` function that can be used to register cleanup functions that run when your test completes. The function also works with test helpers. See GoTip #4: Cleaning Up Your Tests for guidance on simplifying test helpers.

The snippet below in a fictional file called `paint_test.go` demonstrates how `(*testing.T).Helper` influences failure reporting in a Go test:

```go
package paint_test

import (
    "fmt"
    "testing"
)

func paint(color string) error {
    return fmt.Errorf("no %q paint today", color)
}

func badSetup(t *testing.T) {
    // This should call t.Helper, but doesn't.
    if err := paint("taupe"); err != nil {
        t.Fatalf("Could not paint the house under test: %v", err) // line 15
    }
}

func goodSetup(t *testing.T) {
    t.Helper()
    if err := paint("lilac"); err != nil {
        t.Fatalf("Could not paint the house under test: %v", err)
    }
}

func TestBad(t *testing.T) {
    badSetup(t)
    // ...
}

func TestGood(t *testing.T) {
    goodSetup(t) // line 32
    // ...
}

```

Here is an example of this output when run. Note the highlighted text and how it differs:

```go
=== RUN   TestBad
    paint_test.go:15: Could not paint the house under test: no "taupe" paint today
--- FAIL: TestBad (0.00s)
=== RUN   TestGood
    paint_test.go:32: Could not paint the house under test: no "lilac" paint today
--- FAIL: TestGood (0.00s)
FAIL

```

The error with `paint_test.go:15` refers to the line of the setup function that failed in `badSetup`:

`t.Fatalf("Could not paint the house under test: %v", err)`

Whereas `paint_test.go:32` refers to the line of the test that failed in `TestGood`:

`goodSetup(t)`

Correctly using `(*testing.T).Helper` attributes the location of the failure much better when:

- the helper functions grow
- the helper functions call other helpers
- the amount of helper usage in the test functions grow

**Tip:** If a helper calls `(*testing.T).Error` or `(*testing.T).Fatal`, provide some context in the format string to help determine what went wrong and why.

**Tip:** If nothing a helper does can cause a test to fail, it doesn’t need to call `t.Helper`. Simplify its signature by removing `t` from the function parameter list.
