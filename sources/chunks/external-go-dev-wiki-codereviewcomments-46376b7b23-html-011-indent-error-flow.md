---
source_name: "External Linked Documentation"
source_url: "https://go.dev/wiki/CodeReviewComments"
source_path: "sources/raw/external/go-dev-wiki-codereviewcomments-46376b7b23.html"
license_ref: ""
---

# Go Wiki: Go Code Review Comments

## Indent Error Flow

Try to keep the normal code path at a minimal indentation, and indent the error handling, dealing with it first. This improves the readability of the code by permitting visually scanning the normal path quickly. For instance, don’t write:

```go
if err != nil {
    // error handling
} else {
    // normal code
}

```

Instead, write:

```go
if err != nil {
    // error handling
    return // or continue, etc.
}
// normal code

```

If the `if` statement has an initialization statement, such as:

```go
if x, err := f(); err != nil {
    // error handling
    return
} else {
    // use x
}

```

then this may require moving the short variable declaration to its own line:

```go
x, err := f()
if err != nil {
    // error handling
    return
}
// use x

```
