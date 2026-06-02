---
source_name: "Google Go Style Guide"
source_url: "https://google.github.io/styleguide/go/"
source_path: "sources/raw/google-go-styleguide/decisions.html"
license_ref: "sources/licenses/google-styleguide-LICENSE.txt"
---

#### Subtest names

Name your subtest such that it is readable in test output and useful on the command line for users of test filtering. When you use `t.Run` to create a subtest, the first argument is used as a descriptive name for the test. To ensure that test results are legible to humans reading the logs, choose subtest names that will remain useful and readable after escaping. Think of subtest names more like a function identifier than a prose description.

The test runner replaces spaces with underscores, and escapes non-printing characters. To ensure accurate correlation between test logs and source code, it is recommended to avoid using these characters in subtest names.

If your test data benefits from a longer description, consider putting the description in a separate field (perhaps to be printed using `t.Log` or alongside failure messages).

Subtests may be run individually using flags to the Go test runner or Bazel test filter, so choose descriptive names that are also easy to type.

**Warning:** Slash characters are particularly unfriendly in subtest names, since they have special meaning for test filters.

```go
