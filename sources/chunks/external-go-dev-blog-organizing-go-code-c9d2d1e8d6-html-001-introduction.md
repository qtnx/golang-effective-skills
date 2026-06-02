---
source_name: "External Linked Documentation"
source_url: "https://go.dev/blog/organizing-go-code"
source_path: "sources/raw/external/go-dev-blog-organizing-go-code-c9d2d1e8d6.html"
license_ref: ""
---

# The Go Blog

Organizing Go code - The Go Programming Language
# The Go Blog
# Organizing Go code
 Andrew Gerrand
 16 August 2012
## Introduction

Go code is organized differently to that of other languages. This post discusses how to name and package the elements of your Go program to best serve its users.

# The Go Blog

## Choose good names

The names you choose affect how you think about your code, so take care when naming your package and its exported identifiers.

A package’s name provides context for its contents. For instance, the bytes package from the standard library exports the `Buffer` type. On its own, the name `Buffer` isn’t very descriptive, but when combined with its package name its meaning becomes clear: `bytes.Buffer`. If the package had a less descriptive name, like `util`, the buffer would likely acquire the longer and clumsier name `util.BytesBuffer`.

Don’t be shy about renaming things as you work. As you spend time with your program you will better understand how its pieces fit together and, therefore, what their names should be. There’s no need to lock yourself into early decisions. (The gofmt command has a `-r` flag that provides a syntax-aware search and replace, making large-scale refactoring easier.)

A good name is the most important part of a software interface: the name is the first thing every client of the code will see. A well-chosen name is therefore the starting point for good documentation. Many of the following practices result organically from good naming.
