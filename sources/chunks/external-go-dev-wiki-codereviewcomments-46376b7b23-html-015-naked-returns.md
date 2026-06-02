---
source_name: "External Linked Documentation"
source_url: "https://go.dev/wiki/CodeReviewComments"
source_path: "sources/raw/external/go-dev-wiki-codereviewcomments-46376b7b23.html"
license_ref: ""
---

# Go Wiki: Go Code Review Comments

## Naked Returns

A `return` statement without arguments returns the named return values. This is known as a “naked” return.

```go
func split(sum int) (x, y int) {
    x = sum * 4 / 9
    y = sum - x
    return
}

```

See Named Result Parameters.

# Go Wiki: Go Code Review Comments

## Package Comments

Package comments, like all comments to be presented by godoc, must appear adjacent to the package clause, with no blank line.

```go
// Package math provides basic constants and mathematical functions.
package math

```

```go
/*
Package template implements data-driven templates for generating textual
output such as HTML.
....
*/
package template

```

For “package main” comments, other styles of comment are fine after the binary name (and it may be capitalized if it comes first), For example, for a `package main` in the directory `seedgen` you could write:

```go
// Binary seedgen ...
package main

```

or

```go
// Command seedgen ...
package main

```

or

```go
// Program seedgen ...
package main

```

or

```go
// The seedgen command ...
package main

```

or

```go
// The seedgen program ...
package main

```

or

```go
// Seedgen ..
package main

```

These are examples, and sensible variants of these are acceptable.

Note that starting the sentence with a lower-case word is not among the acceptable options for package comments, as these are publicly-visible and should be written in proper English, including capitalizing the first word of the sentence. When the binary name is the first word, capitalizing it is required even though it does not strictly match the spelling of the command-line invocation.

See https://go.dev/doc/effective_go#commentary <https://go.dev/doc/effective_go#commentary> for more information about commentary conventions.
