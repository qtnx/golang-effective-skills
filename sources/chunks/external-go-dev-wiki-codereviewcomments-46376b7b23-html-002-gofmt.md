---
source_name: "External Linked Documentation"
source_url: "https://go.dev/wiki/CodeReviewComments"
source_path: "sources/raw/external/go-dev-wiki-codereviewcomments-46376b7b23.html"
license_ref: ""
---

# Go Wiki: Go Code Review Comments

## Gofmt

Run gofmt <https://pkg.go.dev/cmd/gofmt/> on your code to automatically fix the majority of mechanical style issues. Almost all Go code in the wild uses `gofmt`. The rest of this document addresses non-mechanical style points.

An alternative is to use goimports <https://pkg.go.dev/golang.org/x/tools/cmd/goimports>, a superset of `gofmt` which additionally adds (and removes) import lines as necessary.

# Go Wiki: Go Code Review Comments

## Comment Sentences

See https://go.dev/doc/effective_go#commentary <https://go.dev/doc/effective_go#commentary>. Comments documenting declarations should be full sentences, even if that seems a little redundant. This approach makes them format well when extracted into godoc documentation. Comments should begin with the name of the thing being described and end in a period:

```go
// Request represents a request to run a command.
type Request struct { ...

// Encode writes the JSON encoding of req to w.
func Encode(w io.Writer, req *Request) { ...

```

and so on.
