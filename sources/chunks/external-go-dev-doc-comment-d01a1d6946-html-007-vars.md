---
source_name: "External Linked Documentation"
source_url: "https://go.dev/doc/comment"
source_path: "sources/raw/external/go-dev-doc-comment-d01a1d6946.html"
license_ref: ""
---

# Go Doc Comments

## Vars

The conventions for variables are the same as those for constants. For example, here is a set of grouped variables:

```go
package fs

// Generic file system errors.
// Errors returned by file systems can be tested against these errors
// using errors.Is.
var (
    ErrInvalid    = errInvalid()    // "invalid argument"
    ErrPermission = errPermission() // "permission denied"
    ErrExist      = errExist()      // "file already exists"
    ErrNotExist   = errNotExist()   // "file does not exist"
    ErrClosed     = errClosed()     // "file already closed"
)

```

And a single variable:

```go
package unicode

// Scripts is the set of Unicode script tables.
var Scripts = map[string]*RangeTable{
    "Adlam":                  Adlam,
    "Ahom":                   Ahom,
    "Anatolian_Hieroglyphs":  Anatolian_Hieroglyphs,
    "Arabic":                 Arabic,
    "Armenian":               Armenian,
    ...
}

```
