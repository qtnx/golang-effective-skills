---
source_name: "Google Go Style Guide"
source_url: "https://google.github.io/styleguide/go/"
source_path: "sources/raw/google-go-styleguide/best-practices.md"
license_ref: "sources/licenses/google-styleguide-LICENSE.txt"
---

### `t.Error` vs. `t.Fatal`

As discussed in [decisions](decisions#keep-going), tests should generally not
abort at the first encountered problem.

However, some situations require that the test not proceed. Calling `t.Fatal` is
appropriate when some piece of test setup fails, especially in
[test setup helpers], without which you cannot run the rest of the test. In a
table-driven test, `t.Fatal` is appropriate for failures that set up the whole
test function before the test loop. Failures that affect a single entry in the
test table, which make it impossible to continue with that entry, should be
reported as follows:

*   If you're not using `t.Run` subtests, use `t.Error` followed by a `continue`
    statement to move on to the next table entry.
*   If you're using subtests (and you're inside a call to `t.Run`), use
    `t.Fatal`, which ends the current subtest and allows your test case to
    progress to the next subtest.

**Warning:** It is not always safe to call `t.Fatal` and similar functions.
[More details here](#t-fatal-goroutine).

[test setup helpers]: #test-helper-error-handling

<a id="test-helper-error-handling"></a>
