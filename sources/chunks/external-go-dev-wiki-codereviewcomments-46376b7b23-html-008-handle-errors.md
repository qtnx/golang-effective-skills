---
source_name: "External Linked Documentation"
source_url: "https://go.dev/wiki/CodeReviewComments"
source_path: "sources/raw/external/go-dev-wiki-codereviewcomments-46376b7b23.html"
license_ref: ""
---

# Go Wiki: Go Code Review Comments

## Handle Errors

See https://go.dev/doc/effective_go#errors <https://go.dev/doc/effective_go#errors>. Do not discard errors using `_` variables. If a function returns an error, check it to make sure the function succeeded. Handle the error, return it, or, in truly exceptional situations, panic.

# Go Wiki: Go Code Review Comments

## Imports

Avoid renaming imports except to avoid a name collision; good package names should not require renaming. In the event of collision, prefer to rename the most local or project-specific import.

Imports are organized in groups, with blank lines between them. The standard library packages are always in the first group.

```go
package main

import (
    "fmt"
    "hash/adler32"
    "os"

    "github.com/foo/bar"
    "rsc.io/goversion/version"
)

```

goimports <https://pkg.go.dev/golang.org/x/tools/cmd/goimports> will do this for you.
