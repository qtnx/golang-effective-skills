---
source_name: "External Linked Documentation"
source_url: "https://go.dev/blog/package-names"
source_path: "sources/raw/external/go-dev-blog-package-names-a6de1f37de.html"
license_ref: ""
---

# The Go Blog

Package names - The Go Programming Language
# The Go Blog
# Package names
 Sameer Ajmani
 4 February 2015
## Introduction

Go code is organized into packages. Within a package, code can refer to any identifier (name) defined within, while clients of the package may only reference the package’s exported types, functions, constants, and variables. Such references always include the package name as a prefix: `foo.Bar` refers to the exported name `Bar` in the imported package named `foo`.

Good package names make code better. A package’s name provides context for its contents, making it easier for clients to understand what the package is for and how to use it. The name also helps package maintainers determine what does and does not belong in the package as it evolves. Well-named packages make it easier to find the code you need.

Effective Go provides guidelines for naming packages, types, functions, and variables. This article expands on that discussion and surveys names found in the standard library. It also discusses bad package names and how to fix them.
