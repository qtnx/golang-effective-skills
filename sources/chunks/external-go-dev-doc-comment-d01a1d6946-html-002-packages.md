---
source_name: "External Linked Documentation"
source_url: "https://go.dev/doc/comment"
source_path: "sources/raw/external/go-dev-doc-comment-d01a1d6946.html"
license_ref: ""
---

# Go Doc Comments

## Packages

Every package should have a package comment introducing the package. It provides information relevant to the package as a whole and generally sets expectations for the package. Especially in large packages, it can be helpful for the package comment to give a brief overview of the most important parts of the API, linking to other doc comments as needed.

If the package is simple, the package comment can be brief. For example:

```go
// Package path implements utility routines for manipulating slash-separated
// paths.
//
// The path package should only be used for paths separated by forward
// slashes, such as the paths in URLs. This package does not deal with
// Windows paths with drive letters or backslashes; to manipulate
// operating system paths, use the [path/filepath] package.
package path

```

The square brackets in `[path/filepath]` create a documentation link.

As can be seen in this example, Go doc comments use complete sentences. For a package comment, that means the first sentence begins with “Package ”.

For multi-file packages, the package comment should only be in one source file. If multiple files have package comments, they are concatenated to form one large comment for the entire package.
