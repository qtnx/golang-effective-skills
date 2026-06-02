---
source_name: "Google Go Style Guide"
source_url: "https://google.github.io/styleguide/go/"
source_path: "sources/raw/google-go-styleguide/decisions.md"
license_ref: "sources/licenses/google-styleguide-LICENSE.txt"
---

### In-band errors

<a id="TOC-In-Band-Errors"></a>

In C and similar languages, it is common for functions to return values like -1,
null, or the empty string to signal errors or missing results. This is known as
in-band error handling.

```go
// Bad:
// Lookup returns the value for key or -1 if there is no mapping for key.
func Lookup(key string) int
```

Failing to check for an in-band error value can lead to bugs and can attribute
errors to the wrong function.

```go
// Bad:
// The following line returns an error that Parse failed for the input value,
// whereas the failure was that there is no mapping for missingKey.
return Parse(Lookup(missingKey))
```

Go's support for multiple return values provides a better solution (see the
[Effective Go section on multiple returns]). Instead of requiring clients to
check for an in-band error value, a function should return an additional value
to indicate whether its other return values are valid. This return value may be
an error or a boolean when no explanation is needed, and should be the final
return value.

```go
// Good:
// Lookup returns the value for key or ok=false if there is no mapping for key.
func Lookup(key string) (value string, ok bool)
```

This API prevents the caller from incorrectly writing `Parse(Lookup(key))` which
causes a compile-time error, since `Lookup(key)` has 2 outputs.

Returning errors in this way encourages more robust and explicit error handling:

```go
// Good:
value, ok := Lookup(key)
if !ok {
    return fmt.Errorf("no value for %q", key)
}
return Parse(value)
```

Some standard library functions, like those in package `strings`, return in-band
error values. This greatly simplifies string-manipulation code at the cost of
requiring more diligence from the programmer. In general, Go code in the Google
codebase should return additional values for errors.

[Effective Go section on multiple returns]: http://golang.org/doc/effective_go.html#multiple-returns

<a id="indent-error-flow"></a>
