---
source_name: "External Linked Documentation"
source_url: "https://go.dev/doc/comment"
source_path: "sources/raw/external/go-dev-doc-comment-d01a1d6946.html"
license_ref: ""
---

## Syntax

### Doc links

Doc links are links of the form “[Name1]” or “[Name1.Name2]” to refer to exported identifiers in the current package, or “[pkg]”, “[pkg.Name1]”, or “[pkg.Name1.Name2]” to refer to identifiers in other packages.

For example:

```go
package bytes

// ReadFrom reads data from r until EOF and appends it to the buffer, growing
// the buffer as needed. The return value n is the number of bytes read. Any
// error except [io.EOF] encountered during the read is also returned. If the
// buffer becomes too large, ReadFrom will panic with [ErrTooLarge].
func (b *Buffer) ReadFrom(r io.Reader) (n int64, err error) {
    ...
}

```

The bracketed text for a symbol link can include an optional leading star, making it easy to refer to pointer types, such as [*bytes.Buffer].

When referring to other packages, “pkg” can be either a full import path or the assumed package name of an existing import. The assumed package name is either the identifier in a renamed import or else the name assumed by goimports <https://pkg.go.dev/golang.org/x/tools/internal/imports#ImportPathToAssumedName>. (Goimports inserts renamings when that assumption is not correct, so this rule should work for essentially all Go code.) For example, if the current package imports encoding/json, then “[json.Decoder]” can be written in place of “[encoding/json.Decoder]” to link to the docs for encoding/json’s Decoder. If different source files in a package import different packages using the same name, then the shorthand is ambiguous and cannot be used.

A “pkg” is only assumed to be a full import path if it starts with a domain name (a path element with a dot) or is one of the packages from the standard library (“[os]”, “[encoding/json]”, and so on). For example, `[os.File]` and `[example.com/sys.File]` are documentation links (the latter will be a broken link), but `[os/sys.File]` is not, because there is no os/sys package in the standard library.

To avoid problems with maps, generics, and array types, doc links must be both preceded and followed by punctuation, spaces, tabs, or the start or end of a line. For example, the text “map[ast.Expr]TypeAndValue” does not contain a doc link.
