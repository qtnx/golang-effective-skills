---
source_name: "External Linked Documentation"
source_url: "https://go.dev/doc/comment"
source_path: "sources/raw/external/go-dev-doc-comment-d01a1d6946.html"
license_ref: ""
---

# Go Doc Comments

Go Doc Comments - The Go Programming Language
# Go Doc Comments
Table of Contents:
Packages
 Commands
 Types
 Funcs
 Consts
 Vars
 Syntax
 Common mistakes and pitfalls
“Doc comments” are comments that appear immediately before top-level package, const, func, type, and var declarations with no intervening newlines. Every exported (capitalized) name should have a doc comment.
The go/doc and go/doc/comment packages provide the ability to extract documentation from Go source code, and a variety of tools make use of this functionality. The `go` `doc` command looks up and prints the doc comment for a given package or symbol. (A symbol is a top-level const, func, type, or var.) The web server pkg.go.dev <https://pkg.go.dev/> shows the documentation for public Go packages (when their licenses permit that use). The program serving that site is golang.org/x/pkgsite/cmd/pkgsite <https://pkg.go.dev/golang.org/x/pkgsite/cmd/pkgsite>, which can also be run locally to view documentation for private modules or without an internet connection. The language server gopls <https://pkg.go.dev/golang.org/x/tools/gopls> provides documentation when editing Go source files in IDEs.
The rest of this page documents how to write Go doc comments.
