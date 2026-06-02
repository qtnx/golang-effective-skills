---
source_name: "External Linked Documentation"
source_url: "https://go.dev/wiki/CodeReviewComments"
source_path: "sources/raw/external/go-dev-wiki-codereviewcomments-46376b7b23.html"
license_ref: ""
---

# Go Wiki: Go Code Review Comments

## Package Names

All references to names in your package will be done using the package name, so you can omit that name from the identifiers. For example, if you are in package chubby, you don’t need type ChubbyFile, which clients will write as `chubby.ChubbyFile`. Instead, name the type `File`, which clients will write as `chubby.File`. Avoid meaningless package names like util, common, misc, api, types, and interfaces. See https://go.dev/doc/effective_go#package-names <https://go.dev/doc/effective_go#package-names> and https://go.dev/blog/package-names <https://go.dev/blog/package-names> for more.

# Go Wiki: Go Code Review Comments

## Pass Values

Don’t pass pointers as function arguments just to save a few bytes. If a function refers to its argument `x` only as `*x` throughout, then the argument shouldn’t be a pointer. Common instances of this include passing a pointer to a string (`*string`) or a pointer to an interface value (`*io.Reader`). In both cases the value itself is a fixed size and can be passed directly. This advice does not apply to large structs, or even small structs that might grow.
