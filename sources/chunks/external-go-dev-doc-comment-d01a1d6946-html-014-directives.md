---
source_name: "External Linked Documentation"
source_url: "https://go.dev/doc/comment"
source_path: "sources/raw/external/go-dev-doc-comment-d01a1d6946.html"
license_ref: ""
---

## Syntax

### Directives

Directive comments such as `//go:generate` are not considered part of a doc comment and are omitted from rendered documentation. Gofmt moves directive comments to the end of the doc comment, preceded by a blank line. For example:

```go
package regexp

// An Op is a single regular expression operator.
//
//go:generate stringer -type Op -trimprefix Op
type Op uint8

```

A directive comment is a line starting with the regular expression `//(line |extern |export |[a-z0-9]+:[a-z0-9])`.

Tools may define their own directive comments using the form `//toolname:directive arguments`. Tool directives match the regular expression `//([a-z0-9]+):([a-z0-9]\PZ*)($|\pZ+)(.*)`, where the first group is the tool name and the second group is the directive name. Optional arguments are separated from the directive name by one or more Unicode whitespace characters. Each tool may define its own argument syntax, but a common convention is a sequence of space-separated arguments, where an argument may be a bare word, or a double-quoted or backtick-quoted Go string. The tool name `go` is reserved for use by the Go toolchain.

The `go/ast.ParseDirective` function and its related types parse the tool directive syntax.
