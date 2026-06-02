---
source_name: "Google Go Style Guide"
source_url: "https://google.github.io/styleguide/go/"
source_path: "sources/raw/google-go-styleguide/decisions.html"
license_ref: "sources/licenses/google-styleguide-LICENSE.txt"
---

#### Identifying the row

Do not use the index of the test in the test table as a substitute for naming your tests or printing the inputs. Nobody wants to go through your test table and count the entries in order to figure out which test case is failing.

```go
// Bad:
tests := []struct {
    input, want string
}{
    {"hello", "HELLO"},
    {"wORld", "WORLD"},
}
for i, d := range tests {
    if strings.ToUpper(d.input) != d.want {
        t.Errorf("Failed on case #%d", i)
    }
}

```

Add a test description to your test struct and print it along failure messages. When using subtests, your subtest name should be effective in identifying the row.

**Important:** Even though `t.Run` scopes the output and execution, you must always identify the input. The table test row names must follow the subtest naming guidance.
