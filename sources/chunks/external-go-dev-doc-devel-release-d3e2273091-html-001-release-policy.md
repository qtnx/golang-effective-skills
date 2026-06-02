---
source_name: "External Linked Documentation"
source_url: "https://go.dev/doc/devel/release"
source_path: "sources/raw/external/go-dev-doc-devel-release-d3e2273091.html"
license_ref: ""
---

# Release History

Release History - The Go Programming Language
# Release History
This page summarizes the changes between official stable releases of Go. The change log has the full details.
To update to a specific release, use:
```go
git fetch --tags
git checkout _goX.Y.Z_
```
## Release Policy

 Each major Go release is supported until there are two newer major releases. For example, Go 1.5 was supported until the Go 1.7 release, and Go 1.6 was supported until the Go 1.8 release. We fix critical problems, including critical security problems, in supported releases as needed by issuing minor revisions (for example, Go 1.6.1, Go 1.6.2, and so on).

# Release History

## go1.26.0 (released 2026-02-10)

 Go 1.26.0 is a major release of Go. Read the Go 1.26 Release Notes for more information.

### Minor revisions

 go1.26.1 (released 2026-03-05) includes security fixes to the `crypto/x509`, `html/template`, `net/url`, and `os` packages, as well as bug fixes to the `go` command, the `go fix` command, the compiler, and the `os` and `reflect` packages. See the Go 1.26.1 milestone <https://github.com/golang/go/issues?q=milestone%3AGo1.26.1+label%3ACherryPickApproved> on our issue tracker for details.

 go1.26.2 (released 2026-04-07) includes security fixes to the `go` command, the compiler, and the `archive/tar`, `crypto/tls`, `crypto/x509`, `html/template`, and `os` packages, as well as bug fixes to the `go` command, the `go fix` command, the compiler, the linker, the runtime, and the `net`, `net/http`, and `net/url` packages. See the Go 1.26.2 milestone <https://github.com/golang/go/issues?q=milestone%3AGo1.26.2+label%3ACherryPickApproved> on our issue tracker for details.

 go1.26.3 (released 2026-05-07) includes security fixes to the `go` command, the `pack` tool, and the `html/template`, `net`, `net/http`, `net/http/httputil`, `net/mail`, and `syscall` packages, as well as bug fixes to the `go` command, the `go fix` command, the compiler, the linker, the runtime, and the `crypto/fips140`, `crypto/tls`, `go/types`, and `os` packages. See the Go 1.26.3 milestone <https://github.com/golang/go/issues?q=milestone%3AGo1.26.3+label%3ACherryPickApproved> on our issue tracker for details.
