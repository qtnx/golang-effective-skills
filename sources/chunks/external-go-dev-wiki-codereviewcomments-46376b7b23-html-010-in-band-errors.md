---
source_name: "External Linked Documentation"
source_url: "https://go.dev/wiki/CodeReviewComments"
source_path: "sources/raw/external/go-dev-wiki-codereviewcomments-46376b7b23.html"
license_ref: ""
---

# Go Wiki: Go Code Review Comments

## In-Band Errors

In C and similar languages, it’s common for functions to return values like -1 or null to signal errors or missing results:

```go
// Lookup returns the value for key or "" if there is no mapping for key.
func Lookup(key string) string

// Failing to check for an in-band error value can lead to bugs:
Parse(Lookup(key))  // returns "parse failure for value" instead of "no value for key"

```

Go’s support for multiple return values provides a better solution. Instead of requiring clients to check for an in-band error value, a function should return an additional value to indicate whether its other return values are valid. This return value may be an error, or a boolean when no explanation is needed. It should be the final return value.

```go
// Lookup returns the value for key or ok=false if there is no mapping for key.
func Lookup(key string) (value string, ok bool)

```

This prevents the caller from using the result incorrectly:

```go
Parse(Lookup(key))  // compile-time error

```

And encourages more robust and readable code:

```go
value, ok := Lookup(key)
if !ok {
    return fmt.Errorf("no value for %q", key)
}
return Parse(value)

```

This rule applies to exported functions but is also useful for unexported functions.

Return values like nil, “”, 0, and -1 are fine when they are valid results for a function, that is, when the caller need not handle them differently from other values.

Some standard library functions, like those in package “strings”, return in-band error values. This greatly simplifies string-manipulation code at the cost of requiring more diligence from the programmer. In general, Go code should return additional values for errors.
