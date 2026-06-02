---
source_name: "Google Go Style Guide"
source_url: "https://google.github.io/styleguide/go/"
source_path: "sources/raw/google-go-styleguide/decisions.html"
license_ref: "sources/licenses/google-styleguide-LICENSE.txt"
---

### Full structure comparisons

If your function returns a struct (or any data type with multiple fields such as slices, arrays, and maps), avoid writing test code that performs a hand-coded field-by-field comparison of the struct. Instead, construct the data that you’re expecting your function to return, and compare directly using a deep comparison.

**Note:** This does not apply if your data contains irrelevant fields that obscure the intention of the test.

If your struct needs to be compared for approximate (or equivalent kind of semantic) equality or it contains fields that cannot be compared for equality (e.g., if one of the fields is an `io.Reader`), tweaking a `cmp.Diff` or `cmp.Equal` comparison with `cmpopts` options such as `cmpopts.IgnoreInterfaces` may meet your needs (example).

If your function returns multiple return values, you don’t need to wrap those in a struct before comparing them. Just compare the return values individually and print them.

```go
// Good:
val, multi, tail, err := strconv.UnquoteChar(`\"Fran & Freddie's Diner\"`, '"')
if err != nil {
  t.Fatalf(...)
}
if val != `"` {
  t.Errorf(...)
}
if multi {
  t.Errorf(...)
}
if tail != `Fran & Freddie's Diner"` {
  t.Errorf(...)
}

```
