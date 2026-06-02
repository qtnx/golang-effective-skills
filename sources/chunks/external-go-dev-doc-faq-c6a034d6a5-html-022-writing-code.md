---
source_name: "External Linked Documentation"
source_url: "https://go.dev/doc/faq"
source_path: "sources/raw/external/go-dev-doc-faq-c6a034d6a5.html"
license_ref: ""
---

# Frequently Asked Questions (FAQ)

## Writing Code

### How are libraries documented?

For access to documentation from the command line, the go tool has a doc subcommand that provides a textual interface to the documentation for declarations, files, packages and so on.

The global package discovery page pkg.go.dev/pkg/. runs a server that extracts package documentation from Go source code anywhere on the web and serves it as HTML with links to the declarations and related elements. It is the easiest way to learn about existing Go libraries.

In the early days of the project, there was a similar program, `godoc`, that could also be run to extract documentation for files on the local machine; pkg.go.dev/pkg/ is essentially a descendant. Another descendant is the `pkgsite` <https://pkg.go.dev/golang.org/x/pkgsite/cmd/pkgsite> command that, like `godoc`, can be run locally, although it is not yet integrated into the results shown by `go` `doc`.

### Is there a Go programming style guide?

There is no explicit style guide, although there is certainly a recognizable “Go style”.

Go has established conventions to guide decisions around naming, layout, and file organization. The document Effective Go contains some advice on these topics. More directly, the program `gofmt` is a pretty-printer whose purpose is to enforce layout rules; it replaces the usual compendium of dos and don’ts that allows interpretation. All the Go code in the repository, and the vast majority in the open source world, has been run through `gofmt`.

The document titled Go Code Review Comments is a collection of very short essays about details of Go idiom that are often missed by programmers. It is a handy reference for people doing code reviews for Go projects.

### How do I submit patches to the Go libraries?

The library sources are in the `src` directory of the repository. If you want to make a significant change, please discuss on the mailing list before embarking.

See the document Contributing to the Go project for more information about how to proceed.

### Why does “go get” use HTTPS when cloning a repository?

Companies often permit outgoing traffic only on the standard TCP ports 80 (HTTP) and 443 (HTTPS), blocking outgoing traffic on other ports, including TCP port 9418 (git) and TCP port 22 (SSH). When using HTTPS instead of HTTP, `git` enforces certificate validation by default, providing protection against man-in-the-middle, eavesdropping and tampering attacks. The `go get` command therefore uses HTTPS for safety.

`Git` can be configured to authenticate over HTTPS or to use SSH in place of HTTPS. To authenticate over HTTPS, you can add a line to the `$HOME/.netrc` file that git consults:

```go
machine github.com login *USERNAME* password *APIKEY*

```

For GitHub accounts, the password can be a personal access token <https://help.github.com/articles/creating-a-personal-access-token-for-the-command-line/>.

`Git` can also be configured to use SSH in place of HTTPS for URLs matching a given prefix. For example, to use SSH for all GitHub access, add these lines to your `~/.gitconfig`:

```go
[url "ssh://git@github.com/"]
    insteadOf = https://github.com/

```

When working with private modules, but using a public module proxy for dependencies, you may need to set `GOPRIVATE`. See private modules for details and additional settings.

### How should I manage package versions using “go get”?

The Go toolchain has a built-in system for managing versioned sets of related packages, known as _modules_. Modules were introduced in Go 1.11 and have been ready for production use since 1.14.

To create a project using modules, run `go mod init`. This command creates a `go.mod` file that tracks dependency versions.

```go
go mod init example/project

```

To add, upgrade, or downgrade a dependency, run `go get`:

```go
go get golang.org/x/text@v0.3.5

```

See Tutorial: Create a module for more information on getting started.

See Developing modules for guides on managing dependencies with modules.

Packages within modules should maintain backward compatibility as they evolve, following the import compatibility rule <https://research.swtch.com/vgo-import>:

If an old package and a new package have the same import path,
 the new package must be backwards compatible with the old package.

The Go 1 compatibility guidelines are a good reference here: don’t remove exported names, encourage tagged composite literals, and so on. If different functionality is required, add a new name instead of changing an old one.

Modules codify this with semantic versioning <https://semver.org/> and semantic import versioning. If a break in compatibility is required, release a module at a new major version. Modules at major version 2 and higher require a major version suffix as part of their path (like `/v2`). This preserves the import compatibility rule: packages in different major versions of a module have distinct paths.
