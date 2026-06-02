---
source_name: "Google Go Style Guide"
source_url: "https://google.github.io/styleguide/go/"
source_path: "sources/raw/google-go-styleguide/decisions.html"
license_ref: "sources/licenses/google-styleguide-LICENSE.txt"
---

### Must functions

Setup helper functions that stop the program on failure follow the naming convention `MustXYZ` (or `mustXYZ`). In general, they should only be called early on program startup, not on things like user input where normal Go error handling is preferred.

This often comes up for functions called to initialize package-level variables exclusively at package initialization time (e.g. template.Must and regexp.MustCompile).

```go
// Good:
func MustParse(version string) *Version {
    v, err := Parse(version)
    if err != nil {
        panic(fmt.Sprintf("MustParse(%q) = _, %v", version, err))
    }
    return v
}

// Package level "constant". If we wanted to use `Parse`, we would have had to
// set the value in `init`.
var DefaultVersion = MustParse("1.2.3")

```

The same convention may be used in test helpers that only stop the current test (using `t.Fatal`). Such helpers are often convenient in creating test values, for example in struct fields of table driven tests, as functions that return errors cannot be directly assigned to a struct field.

```go
// Good:
func mustMarshalAny(t *testing.T, m proto.Message) *anypb.Any {
  t.Helper()
  any, err := anypb.New(m)
  if err != nil {
    t.Fatalf("mustMarshalAny(t, m) = %v; want %v", err, nil)
  }
  return any
}

func TestCreateObject(t *testing.T) {
  tests := []struct{
    desc string
    data *anypb.Any
  }{
    {
      desc: "my test case",
      // Creating values directly within table driven test cases.
      data: mustMarshalAny(t, mypb.Object{}),
    },
    // ...
  }
  // ...
}

```

In both of these cases, the value of this pattern is that the helpers can be called in a “value” context. These helpers should not be called in places where it’s difficult to ensure an error would be caught or in a context where an error should be checked (e.g., in many request handlers). For constant inputs, this allows tests to easily ensure that the `Must` arguments are well-formed, and for non-constant inputs it permits tests to validate that errors are properly handled or propagated.

Where `Must` functions are used in a test, they should generally be marked as a test helper and call `t.Fatal` on error (see error handling in test helpers for more considerations of using that).

They should not be used when ordinary error handling is possible (including with some refactoring):

```go
// Bad:
func Version(o *servicepb.Object) (*version.Version, error) {
    // Return error instead of using Must functions.
    v := version.MustParse(o.GetVersionString())
    return dealiasVersion(v)
}

```
