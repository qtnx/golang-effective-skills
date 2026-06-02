---
source_name: "External Linked Documentation"
source_url: "https://pkg.go.dev/github.com/kylelemons/godebug/diff"
source_path: "sources/raw/external/pkg-go-dev-github-com-kylelemons-godebug-diff-5d0083f56a.html"
license_ref: ""
---

diff package - github.com/kylelemons/godebug/diff - Go Packages
## Details

-     Valid go.mod <https://github.com/kylelemons/godebug/tree/v1.1.0/go.mod> file
 The Go module system was introduced in Go 1.11 and is the official dependency management solution for Go.

-     Redistributable license
 Redistributable licenses place minimal restrictions on how software can be used, modified, and redistributed.

-     Tagged version
Modules with tagged versions give importers more predictable builds.

-     Stable version
When a project reaches major version v1 it is considered stable.

-  Learn more about best practices

## Repository
   github.com/kylelemons/godebug  <https://github.com/kylelemons/godebug>

##   Documentation ¶

Package diff implements a linewise diff algorithm.

-  func Diff(A, B string) string
-  type Chunk
-
-  func DiffChunks(a, b []string) []Chunk

- Diff

This section is empty.

This section is empty.

```go
func Diff(A, B string) string
```

Diff returns a string containing a line-by-line unified diff of the linewise changes required to make A into B. Each line is prefixed with '+', '-', or ' ' to indicate if it should be added, removed, or is correct respectively.

```go

constitution := strings.TrimSpace(`
We the People of the United States, in Order to form a more perfect Union,
establish Justice, insure domestic Tranquility, provide for the common defence,
promote the general Welfare, and secure the Blessings of Liberty to ourselves
and our Posterity, do ordain and establish this Constitution for the United
States of America.
`)

got := strings.TrimSpace(`
:wq
We the People of the United States, in Order to form a more perfect Union,
establish Justice, insure domestic Tranquility, provide for the common defence,
and secure the Blessings of Liberty to ourselves
and our Posterity, do ordain and establish this Constitution for the United
States of America.
`)

fmt.Println(Diff(got, constitution))

```

```go
Output:
-:wq
 We the People of the United States, in Order to form a more perfect Union,
 establish Justice, insure domestic Tranquility, provide for the common defence,
-and secure the Blessings of Liberty to ourselves
+promote the general Welfare, and secure the Blessings of Liberty to ourselves
 and our Posterity, do ordain and establish this Constitution for the United
 States of America.

```

```go
type Chunk struct {
	Added   []string
	Deleted []string
	Equal   []string
}
```

Chunk represents a piece of the diff. A chunk will not have both added and deleted lines. Equal lines are always after any added or deleted lines. A Chunk may or may not have any lines in it, especially for the first or last chunk in a computation.

```go
func DiffChunks(a, b []string) []Chunk
```

DiffChunks uses an O(D(N+M)) shortest-edit-script algorithm to compute the edits required from A to B and returns the edit chunks.

##   Source Files ¶
 View all Source files <https://github.com/kylelemons/godebug/tree/v1.1.0/diff>

- diff.go <https://github.com/kylelemons/godebug/blob/v1.1.0/diff/diff.go>

  Click to show internal directories.
  Click to hide internal directories.

  Close

     **?** : This menu   **/** : Search site   **f** or **F** : Jump to   **y** or **Y**  : Canonical URL
  Close
