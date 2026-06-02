---
source_name: "Google Go Style Guide"
source_url: "https://google.github.io/styleguide/go/"
source_path: "sources/raw/google-go-styleguide/decisions.html"
license_ref: "sources/licenses/google-styleguide-LICENSE.txt"
---

### Keep going

Tests should keep going for as long as possible, even after a failure, in order to print out all of the failed checks in a single run. This way, a developer who is fixing the failing test doesn’t have to re-run the test after fixing each bug to find the next bug.

Prefer calling `t.Error` over `t.Fatal` for reporting a mismatch. When comparing several different properties of a function’s output, use `t.Error` for each of those comparisons.

```go
// Good:
gotMean, gotVariance, err := MyDistribution(input)
if err != nil {
  t.Fatalf("MyDistribution(%v) returned unexpected error: %v", input, err)
}
if diff := cmp.Diff(wantMean, gotMean); diff != "" {
  t.Errorf("MyDistribution(%v) returned unexpected difference in mean value (-want +got):\n%s", input, diff)
}
if diff := cmp.Diff(wantVariance, gotVariance); diff != "" {
  t.Errorf("MyDistribution(%v) returned unexpected difference in variance value (-want +got):\n%s", input, diff)
}

```

Calling `t.Fatal` is primarily useful for reporting an unexpected condition (such as an error or output mismatch) when subsequent failures would be meaningless or even mislead the investigator. Note how the code below calls `t.Fatalf` and _then_ `t.Errorf`:

```go
// Good:
gotEncoded := Encode(input)
if gotEncoded != wantEncoded {
  t.Fatalf("Encode(%q) = %q, want %q", input, gotEncoded, wantEncoded)
  // It doesn't make sense to decode from unexpected encoded input.
}
gotDecoded, err := Decode(gotEncoded)
if err != nil {
  t.Fatalf("Decode(%q) returned unexpected error: %v", gotEncoded, err)
}
if gotDecoded != input {
  t.Errorf("Decode(%q) = %q, want %q", gotEncoded, gotDecoded, input)
}

```

For table-driven test, consider using subtests and use `t.Fatal` rather than `t.Error` and `continue`. See also GoTip #25: Subtests: Making Your Tests Lean.

**Best practice:** For more discussion about when `t.Fatal` should be used, see best practices.
