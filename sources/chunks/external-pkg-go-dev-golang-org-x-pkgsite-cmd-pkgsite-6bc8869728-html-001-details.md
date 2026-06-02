---
source_name: "External Linked Documentation"
source_url: "https://pkg.go.dev/golang.org/x/pkgsite/cmd/pkgsite"
source_path: "sources/raw/external/pkg-go-dev-golang-org-x-pkgsite-cmd-pkgsite-6bc8869728.html"
license_ref: ""
---

pkgsite command - golang.org/x/pkgsite/cmd/pkgsite - Go Packages
## Details

-     Valid go.mod <https://cs.opensource.google/go/x/pkgsite/+/b045357b:/go.mod> file
 The Go module system was introduced in Go 1.11 and is the official dependency management solution for Go.

-     Redistributable license
 Redistributable licenses place minimal restrictions on how software can be used, modified, and redistributed.

-     Tagged version
Modules with tagged versions give importers more predictable builds.

-     Stable version
When a project reaches major version v1 it is considered stable.

-  Learn more about best practices

## Repository
   cs.opensource.google/go/x/pkgsite  <https://cs.opensource.google/go/x/pkgsite>

##   Documentation ¶

Pkgsite extracts and generates documentation for Go programs. It runs as a web server and presents the documentation as a web page.

To install, run:

```go
go install golang.org/x/pkgsite/cmd/pkgsite@latest

```

With no arguments, pkgsite will serve docs for main modules relative to the current directory, i.e. the modules listed by `go list -m`. This is typically the module defined by the nearest go.mod file in a parent directory. However, this may include multiple main modules when using a go.work file to define a workspace <https://go.dev/ref/mod#workspaces>.

For example, both of the following forms could be used to work on the module defined in repos/cue/go.mod:

The single module form:

```go
cd repos/cue && pkgsite

```

The multiple module form:

```go
go work init repos/cue repos/other && pkgsite

```

By default, the resulting server will also serve all of the module's dependencies at their required versions. You can disable serving the required modules by passing -list=false.

You can also serve docs from your module cache, directly from the proxy (it uses the GOPROXY environment variable), or both:

```go
pkgsite -cache -proxy

```

With either -cache or -proxy, pkgsite won't look for a module in the current directory. You can still provide modules on the local filesystem by listing their paths:

```go
pkgsite -cache -proxy ~/repos/cue some/other/module

```

Although standard library packages will work by default, the docs can take a while to appear the first time because the Go repo must be cloned and processed. If you clone the repo yourself (https://go.googlesource.com/go <https://go.googlesource.com/go>), you can provide its location with the -gorepo flag to save a little time.

##   Source Files ¶
 View all Source files <https://cs.opensource.google/go/x/pkgsite/+/b045357b:cmd/pkgsite>

- main.go <https://cs.opensource.google/go/x/pkgsite/+/b045357b:cmd/pkgsite/main.go>

  Click to show internal directories.
  Click to hide internal directories.

  Close

     **?** : This menu   **/** : Search site   **f** or **F** : Jump to   **y** or **Y**  : Canonical URL
  Close
