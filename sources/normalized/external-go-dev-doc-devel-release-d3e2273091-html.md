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

## go1.26.0 (released 2026-02-10)

 Go 1.26.0 is a major release of Go. Read the Go 1.26 Release Notes for more information.

### Minor revisions

 go1.26.1 (released 2026-03-05) includes security fixes to the `crypto/x509`, `html/template`, `net/url`, and `os` packages, as well as bug fixes to the `go` command, the `go fix` command, the compiler, and the `os` and `reflect` packages. See the Go 1.26.1 milestone <https://github.com/golang/go/issues?q=milestone%3AGo1.26.1+label%3ACherryPickApproved> on our issue tracker for details.

 go1.26.2 (released 2026-04-07) includes security fixes to the `go` command, the compiler, and the `archive/tar`, `crypto/tls`, `crypto/x509`, `html/template`, and `os` packages, as well as bug fixes to the `go` command, the `go fix` command, the compiler, the linker, the runtime, and the `net`, `net/http`, and `net/url` packages. See the Go 1.26.2 milestone <https://github.com/golang/go/issues?q=milestone%3AGo1.26.2+label%3ACherryPickApproved> on our issue tracker for details.

 go1.26.3 (released 2026-05-07) includes security fixes to the `go` command, the `pack` tool, and the `html/template`, `net`, `net/http`, `net/http/httputil`, `net/mail`, and `syscall` packages, as well as bug fixes to the `go` command, the `go fix` command, the compiler, the linker, the runtime, and the `crypto/fips140`, `crypto/tls`, `go/types`, and `os` packages. See the Go 1.26.3 milestone <https://github.com/golang/go/issues?q=milestone%3AGo1.26.3+label%3ACherryPickApproved> on our issue tracker for details.

## go1.25.0 (released 2025-08-12)

 Go 1.25.0 is a major release of Go. Read the Go 1.25 Release Notes for more information.

### Minor revisions

 go1.25.1 (released 2025-09-03) includes security fixes to the `net/http` package, as well as bug fixes to the `go` command, and the `net`, `os`, `os/exec`, and `testing/synctest` packages. See the Go 1.25.1 milestone <https://github.com/golang/go/issues?q=milestone%3AGo1.25.1+label%3ACherryPickApproved> on our issue tracker for details.

 go1.25.2 (released 2025-10-07) includes security fixes to the `archive/tar`, `crypto/tls`, `crypto/x509`, `encoding/asn1`, `encoding/pem`, `net/http`, `net/mail`, `net/textproto`, and `net/url` packages, as well as bug fixes to the compiler, the runtime, and the `context`, `debug/pe`, `net/http`, `os`, and `sync/atomic` packages. See the Go 1.25.2 milestone <https://github.com/golang/go/issues?q=milestone%3AGo1.25.2+label%3ACherryPickApproved> on our issue tracker for details.

 go1.25.3 (released 2025-10-13) includes fixes to the `crypto/x509` package. See the Go 1.25.3 milestone <https://github.com/golang/go/issues?q=milestone%3AGo1.25.3+label%3ACherryPickApproved> on our issue tracker for details.

 go1.25.4 (released 2025-11-05) includes fixes to the compiler, the runtime, and the `crypto/subtle`, `encoding/pem`, `net/url`, and `os` packages. See the Go 1.25.4 milestone <https://github.com/golang/go/issues?q=milestone%3AGo1.25.4+label%3ACherryPickApproved> on our issue tracker for details.

 go1.25.5 (released 2025-12-02) includes two security fixes to the `crypto/x509` package, as well as bug fixes to the `mime` and `os` packages. See the Go 1.25.5 milestone <https://github.com/golang/go/issues?q=milestone%3AGo1.25.5+label%3ACherryPickApproved> on our issue tracker for details.

 go1.25.6 (released 2026-01-15) includes security fixes to the `go` command, and the `archive/zip`, `crypto/tls`, and `net/url` packages, as well as bug fixes to the compiler, the runtime, and the `crypto/tls`, `errors`, and `os` packages. See the Go 1.25.6 milestone <https://github.com/golang/go/issues?q=milestone%3AGo1.25.6+label%3ACherryPickApproved> on our issue tracker for details.

 go1.25.7 (released 2026-02-04) includes security fixes to the `go` command and the `crypto/tls` package, as well as bug fixes to the compiler and the `crypto/x509` package. See the Go 1.25.7 milestone <https://github.com/golang/go/issues?q=milestone%3AGo1.25.7+label%3ACherryPickApproved> on our issue tracker for details.

 go1.25.8 (released 2026-03-05) includes security fixes to the `html/template`, `net/url`, and `os` packages, as well as bug fixes to the `go` command, the compiler, and the `os` package. See the Go 1.25.8 milestone <https://github.com/golang/go/issues?q=milestone%3AGo1.25.8+label%3ACherryPickApproved> on our issue tracker for details.

 go1.25.9 (released 2026-04-07) includes security fixes to the `go` command, the compiler, and the `archive/tar`, `crypto/tls`, `crypto/x509`, `html/template`, and `os` packages, as well as bug fixes to the `go` command, the compiler, and the runtime. See the Go 1.25.9 milestone <https://github.com/golang/go/issues?q=milestone%3AGo1.25.9+label%3ACherryPickApproved> on our issue tracker for details.

 go1.25.10 (released 2026-05-07) includes security fixes to the `go` command, the `pack` tool, and the `html/template`, `net`, `net/http`, `net/http/httputil`, `net/mail`, and `syscall` packages, as well as bug fixes to the `go` command, the compiler, the linker, the runtime, and the `crypto/fips140`, `go/types`, and `os` packages. See the Go 1.25.10 milestone <https://github.com/golang/go/issues?q=milestone%3AGo1.25.10+label%3ACherryPickApproved> on our issue tracker for details.

## go1.24.0 (released 2025-02-11)

 Go 1.24.0 is a major release of Go. Read the Go 1.24 Release Notes for more information.

### Minor revisions

 go1.24.1 (released 2025-03-04) includes security fixes to the `net/http` package, as well as bug fixes to cgo, the compiler, the `go` command, and the `reflect`, `runtime`, and `syscall` packages. See the Go 1.24.1 milestone <https://github.com/golang/go/issues?q=milestone%3AGo1.24.1+label%3ACherryPickApproved> on our issue tracker for details.

 go1.24.2 (released 2025-04-01) includes security fixes to the `net/http` package, as well as bug fixes to the compiler, the runtime, the `go` command, and the `crypto/tls`, `go/types`, `net/http`, and `testing` packages. See the Go 1.24.2 milestone <https://github.com/golang/go/issues?q=milestone%3AGo1.24.2+label%3ACherryPickApproved> on our issue tracker for details.

 go1.24.3 (released 2025-05-06) includes security fixes to the `os` package, as well as bug fixes to the runtime, the compiler, the linker, the `go` command, and the `crypto/tls` and `os` packages. See the Go 1.24.3 milestone <https://github.com/golang/go/issues?q=milestone%3AGo1.24.3+label%3ACherryPickApproved> on our issue tracker for details.

 go1.24.4 (released 2025-06-05) includes security fixes to the `crypto/x509`, `net/http`, and `os` packages, as well as bug fixes to the linker, the `go` command, and the `hash/maphash` and `os` packages. See the Go 1.24.4 milestone <https://github.com/golang/go/issues?q=milestone%3AGo1.24.4+label%3ACherryPickApproved> on our issue tracker for details.

 go1.24.5 (released 2025-07-08) includes security fixes to the `go` command, as well as bug fixes to the compiler, the linker, the runtime, and the `go` command. See the Go 1.24.5 milestone <https://github.com/golang/go/issues?q=milestone%3AGo1.24.5+label%3ACherryPickApproved> on our issue tracker for details.

 go1.24.6 (released 2025-08-06) includes security fixes to the `database/sql` and `os/exec` packages, as well as bug fixes to the runtime. See the Go 1.24.6 milestone <https://github.com/golang/go/issues?q=milestone%3AGo1.24.6+label%3ACherryPickApproved> on our issue tracker for details.

 go1.24.7 (released 2025-09-03) includes fixes to the `go` command, and the `net` and `os/exec` packages. See the Go 1.24.7 milestone <https://github.com/golang/go/issues?q=milestone%3AGo1.24.7+label%3ACherryPickApproved> on our issue tracker for details.

 go1.24.8 (released 2025-10-07) includes security fixes to the `archive/tar`, `crypto/tls`, `crypto/x509`, `encoding/asn1`, `encoding/pem`, `net/http`, `net/mail`, `net/textproto`, and `net/url` packages, as well as bug fixes to the compiler, the linker, and the `debug/pe`, `net/http`, `os`, and `sync/atomic` packages. See the Go 1.24.8 milestone <https://github.com/golang/go/issues?q=milestone%3AGo1.24.8+label%3ACherryPickApproved> on our issue tracker for details.

 go1.24.9 (released 2025-10-13) includes fixes to the `crypto/x509` package. See the Go 1.24.9 milestone <https://github.com/golang/go/issues?q=milestone%3AGo1.24.9+label%3ACherryPickApproved> on our issue tracker for details.

 go1.24.10 (released 2025-11-05) includes fixes to the `encoding/pem` and `net/url` packages. See the Go 1.24.10 milestone <https://github.com/golang/go/issues?q=milestone%3AGo1.24.10+label%3ACherryPickApproved> on our issue tracker for details.

 go1.24.11 (released 2025-12-02) includes two security fixes to the `crypto/x509` package, as well as bug fixes to the runtime. See the Go 1.24.11 milestone <https://github.com/golang/go/issues?q=milestone%3AGo1.24.11+label%3ACherryPickApproved> on our issue tracker for details.

 go1.24.12 (released 2026-01-15) includes security fixes to the `go` command, and the `archive/zip`, `crypto/tls`, and `net/url` packages, as well as bug fixes to the compiler, the runtime, and the `crypto/tls` and `os` packages. See the Go 1.24.12 milestone <https://github.com/golang/go/issues?q=milestone%3AGo1.24.12+label%3ACherryPickApproved> on our issue tracker for details.

 go1.24.13 (released 2026-02-04) includes security fixes to the `go` command and the `crypto/tls` package, as well as bug fixes to the `crypto/x509` package. See the Go 1.24.13 milestone <https://github.com/golang/go/issues?q=milestone%3AGo1.24.13+label%3ACherryPickApproved> on our issue tracker for details.

## go1.23.0 (released 2024-08-13)

 Go 1.23.0 is a major release of Go. Read the Go 1.23 Release Notes for more information.

### Minor revisions

 go1.23.1 (released 2024-09-05) includes security fixes to the `encoding/gob`, `go/build/constraint`, and `go/parser` packages, as well as bug fixes to the compiler, the `go` command, the runtime, and the `database/sql`, `go/types`, `os`, `runtime/trace`, and `unique` packages. See the Go 1.23.1 milestone <https://github.com/golang/go/issues?q=milestone%3AGo1.23.1+label%3ACherryPickApproved> on our issue tracker for details.

 go1.23.2 (released 2024-10-01) includes fixes to the compiler, cgo, the runtime, and the `maps`, `os`, `os/exec`, `time`, and `unique` packages. See the Go 1.23.2 milestone <https://github.com/golang/go/issues?q=milestone%3AGo1.23.2+label%3ACherryPickApproved> on our issue tracker for details.

 go1.23.3 (released 2024-11-06) includes fixes to the linker, the runtime, and the `net/http`, `os`, and `syscall` packages. See the Go 1.23.3 milestone <https://github.com/golang/go/issues?q=milestone%3AGo1.23.3+label%3ACherryPickApproved> on our issue tracker for details.

 go1.23.4 (released 2024-12-03) includes fixes to the compiler, the runtime, the `trace` command, and the `syscall` package. See the Go 1.23.4 milestone <https://github.com/golang/go/issues?q=milestone%3AGo1.23.4+label%3ACherryPickApproved> on our issue tracker for details.

 go1.23.5 (released 2025-01-16) includes security fixes to the `crypto/x509` and `net/http` packages, as well as bug fixes to the compiler, the runtime, and the `net` package. See the Go 1.23.5 milestone <https://github.com/golang/go/issues?q=milestone%3AGo1.23.5+label%3ACherryPickApproved> on our issue tracker for details.

 go1.23.6 (released 2025-02-04) includes security fixes to the `crypto/elliptic` package, as well as bug fixes to the compiler and the `go` command. See the Go 1.23.6 milestone <https://github.com/golang/go/issues?q=milestone%3AGo1.23.6+label%3ACherryPickApproved> on our issue tracker for details.

 go1.23.7 (released 2025-03-04) includes security fixes to the `net/http` package, as well as bug fixes to cgo, the compiler, and the `reflect`, `runtime`, and `syscall` packages. See the Go 1.23.7 milestone <https://github.com/golang/go/issues?q=milestone%3AGo1.23.7+label%3ACherryPickApproved> on our issue tracker for details.

 go1.23.8 (released 2025-04-01) includes security fixes to the `net/http` package, as well as bug fixes to the runtime and the `go` command. See the Go 1.23.8 milestone <https://github.com/golang/go/issues?q=milestone%3AGo1.23.8+label%3ACherryPickApproved> on our issue tracker for details.

 go1.23.9 (released 2025-05-06) includes fixes to the runtime and the linker. See the Go 1.23.9 milestone <https://github.com/golang/go/issues?q=milestone%3AGo1.23.9+label%3ACherryPickApproved> on our issue tracker for details.

 go1.23.10 (released 2025-06-05) includes security fixes to the `net/http` and `os` packages, as well as bug fixes to the linker. See the Go 1.23.10 milestone <https://github.com/golang/go/issues?q=milestone%3AGo1.23.10+label%3ACherryPickApproved> on our issue tracker for details.

 go1.23.11 (released 2025-07-08) includes security fixes to the `go` command, as well as bug fixes to the compiler, the linker, and the runtime. See the Go 1.23.11 milestone <https://github.com/golang/go/issues?q=milestone%3AGo1.23.11+label%3ACherryPickApproved> on our issue tracker for details.

 go1.23.12 (released 2025-08-06) includes security fixes to the `database/sql` and `os/exec` packages, as well as bug fixes to the runtime. See the Go 1.23.12 milestone <https://github.com/golang/go/issues?q=milestone%3AGo1.23.12+label%3ACherryPickApproved> on our issue tracker for details.

## go1.22.0 (released 2024-02-06)

 Go 1.22.0 is a major release of Go. Read the Go 1.22 Release Notes for more information.

### Minor revisions

 go1.22.1 (released 2024-03-05) includes security fixes to the `crypto/x509`, `html/template`, `net/http`, `net/http/cookiejar`, and `net/mail` packages, as well as bug fixes to the compiler, the `go` command, the runtime, the `trace` command, and the `go/types` and `net/http` packages. See the Go 1.22.1 milestone <https://github.com/golang/go/issues?q=milestone%3AGo1.22.1+label%3ACherryPickApproved> on our issue tracker for details.

 go1.22.2 (released 2024-04-03) includes a security fix to the `net/http` package, as well as bug fixes to the compiler, the `go` command, the linker, and the `encoding/gob`, `go/types`, `net/http`, and `runtime/trace` packages. See the Go 1.22.2 milestone <https://github.com/golang/go/issues?q=milestone%3AGo1.22.2+label%3ACherryPickApproved> on our issue tracker for details.

 go1.22.3 (released 2024-05-07) includes security fixes to the `go` command and the `net` package, as well as bug fixes to the compiler, the runtime, and the `net/http` package. See the Go 1.22.3 milestone <https://github.com/golang/go/issues?q=milestone%3AGo1.22.3+label%3ACherryPickApproved> on our issue tracker for details.

 go1.22.4 (released 2024-06-04) includes security fixes to the `archive/zip` and `net/netip` packages, as well as bug fixes to the compiler, the `go` command, the linker, the runtime, and the `os` package. See the Go 1.22.4 milestone <https://github.com/golang/go/issues?q=milestone%3AGo1.22.4+label%3ACherryPickApproved> on our issue tracker for details.

 go1.22.5 (released 2024-07-02) includes security fixes to the `net/http` package, as well as bug fixes to the compiler, cgo, the `go` command, the linker, the runtime, and the `crypto/tls`, `go/types`, `net`, `net/http`, and `os/exec` packages. See the Go 1.22.5 milestone <https://github.com/golang/go/issues?q=milestone%3AGo1.22.5+label%3ACherryPickApproved> on our issue tracker for details.

 go1.22.6 (released 2024-08-06) includes fixes to the `go` command, the compiler, the linker, the `trace` command, the `covdata` command, and the `bytes`, `go/types`, and `os/exec` packages. See the Go 1.22.6 milestone <https://github.com/golang/go/issues?q=milestone%3AGo1.22.6+label%3ACherryPickApproved> on our issue tracker for details.

 go1.22.7 (released 2024-09-05) includes security fixes to the `encoding/gob`, `go/build/constraint`, and `go/parser` packages, as well as bug fixes to the `fix` command and the runtime. See the Go 1.22.7 milestone <https://github.com/golang/go/issues?q=milestone%3AGo1.22.7+label%3ACherryPickApproved> on our issue tracker for details.

 go1.22.8 (released 2024-10-01) includes fixes to cgo, and the `maps` and `syscall` packages. See the Go 1.22.8 milestone <https://github.com/golang/go/issues?q=milestone%3AGo1.22.8+label%3ACherryPickApproved> on our issue tracker for details.

 go1.22.9 (released 2024-11-06) includes fixes to the linker. See the Go 1.22.9 milestone <https://github.com/golang/go/issues?q=milestone%3AGo1.22.9+label%3ACherryPickApproved> on our issue tracker for details.

 go1.22.10 (released 2024-12-03) includes fixes to the runtime and the `syscall` package. See the Go 1.22.10 milestone <https://github.com/golang/go/issues?q=milestone%3AGo1.22.10+label%3ACherryPickApproved> on our issue tracker for details.

 go1.22.11 (released 2025-01-16) includes security fixes to the `crypto/x509` and `net/http` packages, as well as bug fixes to the runtime. See the Go 1.22.11 milestone <https://github.com/golang/go/issues?q=milestone%3AGo1.22.11+label%3ACherryPickApproved> on our issue tracker for details.

 go1.22.12 (released 2025-02-04) includes security fixes to the `crypto/elliptic` package, as well as bug fixes to the compiler and the `go` command. See the Go 1.22.12 milestone <https://github.com/golang/go/issues?q=milestone%3AGo1.22.12+label%3ACherryPickApproved> on our issue tracker for details.

## go1.21.0 (released 2023-08-08)

 Go 1.21.0 is a major release of Go. Read the Go 1.21 Release Notes for more information.

### Minor revisions

 go1.21.1 (released 2023-09-06) includes four security fixes to the `cmd/go`, `crypto/tls`, and `html/template` packages, as well as bug fixes to the compiler, the `go` command, the linker, the runtime, and the `context`, `crypto/tls`, `encoding/gob`, `encoding/xml`, `go/types`, `net/http`, `os`, and `path/filepath` packages. See the Go 1.21.1 milestone <https://github.com/golang/go/issues?q=milestone%3AGo1.21.1+label%3ACherryPickApproved> on our issue tracker for details.

 go1.21.2 (released 2023-10-05) includes one security fix to the `cmd/go` package, as well as bug fixes to the compiler, the `go` command, the linker, the runtime, and the `runtime/metrics` package. See the Go 1.21.2 milestone <https://github.com/golang/go/issues?q=milestone%3AGo1.21.2+label%3ACherryPickApproved> on our issue tracker for details.

 go1.21.3 (released 2023-10-10) includes a security fix to the `net/http` package. See the Go 1.21.3 milestone <https://github.com/golang/go/issues?q=milestone%3AGo1.21.3+label%3ACherryPickApproved> on our issue tracker for details.

 go1.21.4 (released 2023-11-07) includes security fixes to the `path/filepath` package, as well as bug fixes to the linker, the runtime, the compiler, and the `go/types`, `net/http`, and `runtime/cgo` packages. See the Go 1.21.4 milestone <https://github.com/golang/go/issues?q=milestone%3AGo1.21.4+label%3ACherryPickApproved> on our issue tracker for details.

 go1.21.5 (released 2023-12-05) includes security fixes to the `go` command, and the `net/http` and `path/filepath` packages, as well as bug fixes to the compiler, the `go` command, the runtime, and the `crypto/rand`, `net`, `os`, and `syscall` packages. See the Go 1.21.5 milestone <https://github.com/golang/go/issues?q=milestone%3AGo1.21.5+label%3ACherryPickApproved> on our issue tracker for details.

 go1.21.6 (released 2024-01-09) includes fixes to the compiler, the runtime, and the `crypto/tls`, `maps`, and `runtime/pprof` packages. See the Go 1.21.6 milestone <https://github.com/golang/go/issues?q=milestone%3AGo1.21.6+label%3ACherryPickApproved> on our issue tracker for details.

 go1.21.7 (released 2024-02-06) includes fixes to the compiler, the `go` command, the runtime, and the `crypto/x509` package. See the Go 1.21.7 milestone <https://github.com/golang/go/issues?q=milestone%3AGo1.21.7+label%3ACherryPickApproved> on our issue tracker for details.

 go1.21.8 (released 2024-03-05) includes security fixes to the `crypto/x509`, `html/template`, `net/http`, `net/http/cookiejar`, and `net/mail` packages, as well as bug fixes to the `go` command and the runtime. See the Go 1.21.8 milestone <https://github.com/golang/go/issues?q=milestone%3AGo1.21.8+label%3ACherryPickApproved> on our issue tracker for details.

 go1.21.9 (released 2024-04-03) includes a security fix to the `net/http` package, as well as bug fixes to the linker, and the `go/types` and `net/http` packages. See the Go 1.21.9 milestone <https://github.com/golang/go/issues?q=milestone%3AGo1.21.9+label%3ACherryPickApproved> on our issue tracker for details.

 go1.21.10 (released 2024-05-07) includes security fixes to the `go` command, as well as bug fixes to the `net/http` package. See the Go 1.21.10 milestone <https://github.com/golang/go/issues?q=milestone%3AGo1.21.10+label%3ACherryPickApproved> on our issue tracker for details.

 go1.21.11 (released 2024-06-04) includes security fixes to the `archive/zip` and `net/netip` packages, as well as bug fixes to the compiler, the `go` command, the runtime, and the `os` package. See the Go 1.21.11 milestone <https://github.com/golang/go/issues?q=milestone%3AGo1.21.11+label%3ACherryPickApproved> on our issue tracker for details.

 go1.21.12 (released 2024-07-02) includes security fixes to the `net/http` package, as well as bug fixes to the compiler, the `go` command, the runtime, and the `crypto/x509`, `net/http`, `net/netip`, and `os` packages. See the Go 1.21.12 milestone <https://github.com/golang/go/issues?q=milestone%3AGo1.21.12+label%3ACherryPickApproved> on our issue tracker for details.

 go1.21.13 (released 2024-08-06) includes fixes to the `go` command, the `covdata` command, and the `bytes` package. See the Go 1.21.13 milestone <https://github.com/golang/go/issues?q=milestone%3AGo1.21.13+label%3ACherryPickApproved> on our issue tracker for details.

## go1.20 (released 2023-02-01)

 Go 1.20 is a major release of Go. Read the Go 1.20 Release Notes for more information.

### Minor revisions

 go1.20.1 (released 2023-02-14) includes security fixes to the `crypto/tls`, `mime/multipart`, `net/http`, and `path/filepath` packages, as well as bug fixes to the compiler, the `go` command, the linker, the runtime, and the `time` package. See the Go 1.20.1 milestone <https://github.com/golang/go/issues?q=milestone%3AGo1.20.1+label%3ACherryPickApproved> on our issue tracker for details.

 go1.20.2 (released 2023-03-07) includes a security fix to the `crypto/elliptic` package, as well as bug fixes to the compiler, the `covdata` command, the linker, the runtime, and the `crypto/ecdh`, `crypto/rsa`, `crypto/x509`, `os`, and `syscall` packages. See the Go 1.20.2 milestone <https://github.com/golang/go/issues?q=milestone%3AGo1.20.2+label%3ACherryPickApproved> on our issue tracker for details.

 go1.20.3 (released 2023-04-04) includes security fixes to the `go/parser`, `html/template`, `mime/multipart`, `net/http`, and `net/textproto` packages, as well as bug fixes to the compiler, the linker, the runtime, and the `time` package. See the Go 1.20.3 milestone <https://github.com/golang/go/issues?q=milestone%3AGo1.20.3+label%3ACherryPickApproved> on our issue tracker for details.

 go1.20.4 (released 2023-05-02) includes three security fixes to the `html/template` package, as well as bug fixes to the compiler, the runtime, and the `crypto/subtle`, `crypto/tls`, `net/http`, and `syscall` packages. See the Go 1.20.4 milestone <https://github.com/golang/go/issues?q=milestone%3AGo1.20.4+label%3ACherryPickApproved> on our issue tracker for details.

 go1.20.5 (released 2023-06-06) includes four security fixes to the `cmd/go` and `runtime` packages, as well as bug fixes to the compiler, the `go` command, the runtime, and the `crypto/rsa`, `net`, and `os` packages. See the Go 1.20.5 milestone <https://github.com/golang/go/issues?q=milestone%3AGo1.20.5+label%3ACherryPickApproved> on our issue tracker for details.

 go1.20.6 (released 2023-07-11) includes a security fix to the `net/http` package, as well as bug fixes to the compiler, cgo, the `cover` tool, the `go` command, the runtime, and the `crypto/ecdsa`, `go/build`, `go/printer`, `net/mail`, and `text/template` packages. See the Go 1.20.6 milestone <https://github.com/golang/go/issues?q=milestone%3AGo1.20.6+label%3ACherryPickApproved> on our issue tracker for details.

 go1.20.7 (released 2023-08-01) includes a security fix to the `crypto/tls` package, as well as bug fixes to the assembler and the compiler. See the Go 1.20.7 milestone <https://github.com/golang/go/issues?q=milestone%3AGo1.20.7+label%3ACherryPickApproved> on our issue tracker for details.

 go1.20.8 (released 2023-09-06) includes two security fixes to the `html/template` package, as well as bug fixes to the compiler, the `go` command, the runtime, and the `crypto/tls`, `go/types`, `net/http`, and `path/filepath` packages. See the Go 1.20.8 milestone <https://github.com/golang/go/issues?q=milestone%3AGo1.20.8+label%3ACherryPickApproved> on our issue tracker for details.

 go1.20.9 (released 2023-10-05) includes one security fix to the `cmd/go` package, as well as bug fixes to the `go` command and the linker. See the Go 1.20.9 milestone <https://github.com/golang/go/issues?q=milestone%3AGo1.20.9+label%3ACherryPickApproved> on our issue tracker for details.

 go1.20.10 (released 2023-10-10) includes a security fix to the `net/http` package. See the Go 1.20.10 milestone <https://github.com/golang/go/issues?q=milestone%3AGo1.20.10+label%3ACherryPickApproved> on our issue tracker for details.

 go1.20.11 (released 2023-11-07) includes security fixes to the `path/filepath` package, as well as bug fixes to the linker and the `net/http` package. See the Go 1.20.11 milestone <https://github.com/golang/go/issues?q=milestone%3AGo1.20.11+label%3ACherryPickApproved> on our issue tracker for details.

 go1.20.12 (released 2023-12-05) includes security fixes to the `go` command, and the `net/http` and `path/filepath` packages, as well as bug fixes to the compiler and the `go` command. See the Go 1.20.12 milestone <https://github.com/golang/go/issues?q=milestone%3AGo1.20.12+label%3ACherryPickApproved> on our issue tracker for details.

 go1.20.13 (released 2024-01-09) includes fixes to the runtime and the `crypto/tls` package. See the Go 1.20.13 milestone <https://github.com/golang/go/issues?q=milestone%3AGo1.20.13+label%3ACherryPickApproved> on our issue tracker for details.

 go1.20.14 (released 2024-02-06) includes fixes to the `crypto/x509` package. See the Go 1.20.14 milestone <https://github.com/golang/go/issues?q=milestone%3AGo1.20.14+label%3ACherryPickApproved> on our issue tracker for details.

## go1.19 (released 2022-08-02)

 Go 1.19 is a major release of Go. Read the Go 1.19 Release Notes for more information.

### Minor revisions

 go1.19.1 (released 2022-09-06) includes security fixes to the `net/http` and `net/url` packages, as well as bug fixes to the compiler, the `go` command, the `pprof` command, the linker, the runtime, and the `crypto/tls` and `crypto/x509` packages. See the Go 1.19.1 milestone <https://github.com/golang/go/issues?q=milestone%3AGo1.19.1+label%3ACherryPickApproved> on our issue tracker for details.

 go1.19.2 (released 2022-10-04) includes security fixes to the `archive/tar`, `net/http/httputil`, and `regexp` packages, as well as bug fixes to the compiler, the linker, the runtime, and the `go/types` package. See the Go 1.19.2 milestone <https://github.com/golang/go/issues?q=milestone%3AGo1.19.2+label%3ACherryPickApproved> on our issue tracker for details.

 go1.19.3 (released 2022-11-01) includes security fixes to the `os/exec` and `syscall` packages, as well as bug fixes to the compiler and the runtime. See the Go 1.19.3 milestone <https://github.com/golang/go/issues?q=milestone%3AGo1.19.3+label%3ACherryPickApproved> on our issue tracker for details.

 go1.19.4 (released 2022-12-06) includes security fixes to the `net/http` and `os` packages, as well as bug fixes to the compiler, the runtime, and the `crypto/x509`, `os/exec`, and `sync/atomic` packages. See the Go 1.19.4 milestone <https://github.com/golang/go/issues?q=milestone%3AGo1.19.4+label%3ACherryPickApproved> on our issue tracker for details.

 go1.19.5 (released 2023-01-10) includes fixes to the compiler, the linker, and the `crypto/x509`, `net/http`, `sync/atomic`, and `syscall` packages. See the Go 1.19.5 milestone <https://github.com/golang/go/issues?q=milestone%3AGo1.19.5+label%3ACherryPickApproved> on our issue tracker for details.

 go1.19.6 (released 2023-02-14) includes security fixes to the `crypto/tls`, `mime/multipart`, `net/http`, and `path/filepath` packages, as well as bug fixes to the `go` command, the linker, the runtime, and the `crypto/x509`, `net/http`, and `time` packages. See the Go 1.19.6 milestone <https://github.com/golang/go/issues?q=milestone%3AGo1.19.6+label%3ACherryPickApproved> on our issue tracker for details.

 go1.19.7 (released 2023-03-07) includes a security fix to the `crypto/elliptic` package, as well as bug fixes to the linker, the runtime, and the `crypto/x509` and `syscall` packages. See the Go 1.19.7 milestone <https://github.com/golang/go/issues?q=milestone%3AGo1.19.7+label%3ACherryPickApproved> on our issue tracker for details.

 go1.19.8 (released 2023-04-04) includes security fixes to the `go/parser`, `html/template`, `mime/multipart`, `net/http`, and `net/textproto` packages, as well as bug fixes to the linker, the runtime, and the `time` package. See the Go 1.19.8 milestone <https://github.com/golang/go/issues?q=milestone%3AGo1.19.8+label%3ACherryPickApproved> on our issue tracker for details.

 go1.19.9 (released 2023-05-02) includes three security fixes to the `html/template` package, as well as bug fixes to the compiler, the runtime, and the `crypto/tls` and `syscall` packages. See the Go 1.19.9 milestone <https://github.com/golang/go/issues?q=milestone%3AGo1.19.9+label%3ACherryPickApproved> on our issue tracker for details.

 go1.19.10 (released 2023-06-06) includes four security fixes to the `cmd/go` and `runtime` packages, as well as bug fixes to the compiler, the `go` command, and the runtime. See the Go 1.19.10 milestone <https://github.com/golang/go/issues?q=milestone%3AGo1.19.10+label%3ACherryPickApproved> on our issue tracker for details.

 go1.19.11 (released 2023-07-11) includes a security fix to the `net/http` package, as well as bug fixes to cgo, the `cover` tool, the `go` command, the runtime, and the `go/printer` package. See the Go 1.19.11 milestone <https://github.com/golang/go/issues?q=milestone%3AGo1.19.11+label%3ACherryPickApproved> on our issue tracker for details.

 go1.19.12 (released 2023-08-01) includes a security fix to the `crypto/tls` package, as well as bug fixes to the assembler and the compiler. See the Go 1.19.12 milestone <https://github.com/golang/go/issues?q=milestone%3AGo1.19.12+label%3ACherryPickApproved> on our issue tracker for details.

 go1.19.13 (released 2023-09-06) includes fixes to the `go` command, and the `crypto/tls` and `net/http` packages. See the Go 1.19.13 milestone <https://github.com/golang/go/issues?q=milestone%3AGo1.19.13+label%3ACherryPickApproved> on our issue tracker for details.

## go1.18 (released 2022-03-15)

 Go 1.18 is a major release of Go. Read the Go 1.18 Release Notes for more information.

### Minor revisions

 go1.18.1 (released 2022-04-12) includes security fixes to the `crypto/elliptic`, `crypto/x509`, and `encoding/pem` packages, as well as bug fixes to the compiler, linker, runtime, the `go` command, vet, and the `bytes`, `crypto/x509`, and `go/types` packages. See the Go 1.18.1 milestone <https://github.com/golang/go/issues?q=milestone%3AGo1.18.1+label%3ACherryPickApproved> on our issue tracker for details.

 go1.18.2 (released 2022-05-10) includes security fixes to the `syscall` package, as well as bug fixes to the compiler, runtime, the `go` command, and the `crypto/x509`, `go/types`, `net/http/httptest`, `reflect`, and `sync/atomic` packages. See the Go 1.18.2 milestone <https://github.com/golang/go/issues?q=milestone%3AGo1.18.2+label%3ACherryPickApproved> on our issue tracker for details.

 go1.18.3 (released 2022-06-01) includes security fixes to the `crypto/rand`, `crypto/tls`, `os/exec`, and `path/filepath` packages, as well as bug fixes to the compiler, and the `crypto/tls` and `text/template/parse` packages. See the Go 1.18.3 milestone <https://github.com/golang/go/issues?q=milestone%3AGo1.18.3+label%3ACherryPickApproved> on our issue tracker for details.

 go1.18.4 (released 2022-07-12) includes security fixes to the `compress/gzip`, `encoding/gob`, `encoding/xml`, `go/parser`, `io/fs`, `net/http`, and `path/filepath` packages, as well as bug fixes to the compiler, the `go` command, the linker, the runtime, and the `runtime/metrics` package. See the Go 1.18.4 milestone <https://github.com/golang/go/issues?q=milestone%3AGo1.18.4+label%3ACherryPickApproved> on our issue tracker for details.

 go1.18.5 (released 2022-08-01) includes security fixes to the `encoding/gob` and `math/big` packages, as well as bug fixes to the compiler, the `go` command, the runtime, and the `testing` package. See the Go 1.18.5 milestone <https://github.com/golang/go/issues?q=milestone%3AGo1.18.5+label%3ACherryPickApproved> on our issue tracker for details.

 go1.18.6 (released 2022-09-06) includes security fixes to the `net/http` package, as well as bug fixes to the compiler, the `go` command, the `pprof` command, the runtime, and the `crypto/tls`, `encoding/xml`, and `net` packages. See the Go 1.18.6 milestone <https://github.com/golang/go/issues?q=milestone%3AGo1.18.6+label%3ACherryPickApproved> on our issue tracker for details.

 go1.18.7 (released 2022-10-04) includes security fixes to the `archive/tar`, `net/http/httputil`, and `regexp` packages, as well as bug fixes to the compiler, the linker, and the `go/types` package. See the Go 1.18.7 milestone <https://github.com/golang/go/issues?q=milestone%3AGo1.18.7+label%3ACherryPickApproved> on our issue tracker for details.

 go1.18.8 (released 2022-11-01) includes security fixes to the `os/exec` and `syscall` packages, as well as bug fixes to the runtime. See the Go 1.18.8 milestone <https://github.com/golang/go/issues?q=milestone%3AGo1.18.8+label%3ACherryPickApproved> on our issue tracker for details.

 go1.18.9 (released 2022-12-06) includes security fixes to the `net/http` and `os` packages, as well as bug fixes to cgo, the compiler, the runtime, and the `crypto/x509` and `os/exec` packages. See the Go 1.18.9 milestone <https://github.com/golang/go/issues?q=milestone%3AGo1.18.9+label%3ACherryPickApproved> on our issue tracker for details.

 go1.18.10 (released 2023-01-10) includes fixes to cgo, the compiler, the linker, and the `crypto/x509`, `net/http`, and `syscall` packages. See the Go 1.18.10 milestone <https://github.com/golang/go/issues?q=milestone%3AGo1.18.10+label%3ACherryPickApproved> on our issue tracker for details.

## go1.17 (released 2021-08-16)

 Go 1.17 is a major release of Go. Read the Go 1.17 Release Notes for more information.

### Minor revisions

 go1.17.1 (released 2021-09-09) includes a security fix to the `archive/zip` package, as well as bug fixes to the compiler, linker, the `go` command, and the `crypto/rand`, `embed`, `go/types`, `html/template`, and `net/http` packages. See the Go 1.17.1 milestone <https://github.com/golang/go/issues?q=milestone%3AGo1.17.1+label%3ACherryPickApproved> on our issue tracker for details.

 go1.17.2 (released 2021-10-07) includes security fixes to linker and the `misc/wasm` directory, as well as bug fixes to the compiler, runtime, the `go` command, and the `text/template` and `time` packages. See the Go 1.17.2 milestone <https://github.com/golang/go/issues?q=milestone%3AGo1.17.2+label%3ACherryPickApproved> on our issue tracker for details.

 go1.17.3 (released 2021-11-04) includes security fixes to the `archive/zip` and `debug/macho` packages, as well as bug fixes to the compiler, linker, runtime, the `go` command, the `misc/wasm` directory, and the `net/http` and `syscall` packages. See the Go 1.17.3 milestone <https://github.com/golang/go/issues?q=milestone%3AGo1.17.3+label%3ACherryPickApproved> on our issue tracker for details.

 go1.17.4 (released 2021-12-02) includes fixes to the compiler, linker, runtime, and the `go/types`, `net/http`, and `time` packages. See the Go 1.17.4 milestone <https://github.com/golang/go/issues?q=milestone%3AGo1.17.4+label%3ACherryPickApproved> on our issue tracker for details.

 go1.17.5 (released 2021-12-09) includes security fixes to the `net/http` and `syscall` packages. See the Go 1.17.5 milestone <https://github.com/golang/go/issues?q=milestone%3AGo1.17.5+label%3ACherryPickApproved> on our issue tracker for details.

 go1.17.6 (released 2022-01-06) includes fixes to the compiler, linker, runtime, and the `crypto/x509`, `net/http`, and `reflect` packages. See the Go 1.17.6 milestone <https://github.com/golang/go/issues?q=milestone%3AGo1.17.6+label%3ACherryPickApproved> on our issue tracker for details.

 go1.17.7 (released 2022-02-10) includes security fixes to the `go` command, and the `crypto/elliptic` and `math/big` packages, as well as bug fixes to the compiler, linker, runtime, the `go` command, and the `debug/macho`, `debug/pe`, and `net/http/httptest` packages. See the Go 1.17.7 milestone <https://github.com/golang/go/issues?q=milestone%3AGo1.17.7+label%3ACherryPickApproved> on our issue tracker for details.

 go1.17.8 (released 2022-03-03) includes a security fix to the `regexp/syntax` package, as well as bug fixes to the compiler, runtime, the `go` command, and the `crypto/x509` and `net` packages. See the Go 1.17.8 milestone <https://github.com/golang/go/issues?q=milestone%3AGo1.17.8+label%3ACherryPickApproved> on our issue tracker for details.

 go1.17.9 (released 2022-04-12) includes security fixes to the `crypto/elliptic` and `encoding/pem` packages, as well as bug fixes to the linker and runtime. See the Go 1.17.9 milestone <https://github.com/golang/go/issues?q=milestone%3AGo1.17.9+label%3ACherryPickApproved> on our issue tracker for details.

 go1.17.10 (released 2022-05-10) includes security fixes to the `syscall` package, as well as bug fixes to the compiler, runtime, and the `crypto/x509` and `net/http/httptest` packages. See the Go 1.17.10 milestone <https://github.com/golang/go/issues?q=milestone%3AGo1.17.10+label%3ACherryPickApproved> on our issue tracker for details.

 go1.17.11 (released 2022-06-01) includes security fixes to the `crypto/rand`, `crypto/tls`, `os/exec`, and `path/filepath` packages, as well as bug fixes to the `crypto/tls` package. See the Go 1.17.11 milestone <https://github.com/golang/go/issues?q=milestone%3AGo1.17.11+label%3ACherryPickApproved> on our issue tracker for details.

 go1.17.12 (released 2022-07-12) includes security fixes to the `compress/gzip`, `encoding/gob`, `encoding/xml`, `go/parser`, `io/fs`, `net/http`, and `path/filepath` packages, as well as bug fixes to the compiler, the `go` command, the runtime, and the `runtime/metrics` package. See the Go 1.17.12 milestone <https://github.com/golang/go/issues?q=milestone%3AGo1.17.12+label%3ACherryPickApproved> on our issue tracker for details.

 go1.17.13 (released 2022-08-01) includes security fixes to the `encoding/gob` and `math/big` packages, as well as bug fixes to the compiler and the runtime. See the Go 1.17.13 milestone <https://github.com/golang/go/issues?q=milestone%3AGo1.17.13+label%3ACherryPickApproved> on our issue tracker for details.

## go1.16 (released 2021-02-16)

 Go 1.16 is a major release of Go. Read the Go 1.16 Release Notes for more information.

### Minor revisions

 go1.16.1 (released 2021-03-10) includes security fixes to the `archive/zip` and `encoding/xml` packages. See the Go 1.16.1 milestone <https://github.com/golang/go/issues?q=milestone%3AGo1.16.1+label%3ACherryPickApproved> on our issue tracker for details.

 go1.16.2 (released 2021-03-11) includes fixes to cgo, the compiler, linker, the `go` command, and the `syscall` and `time` packages. See the Go 1.16.2 milestone <https://github.com/golang/go/issues?q=milestone%3AGo1.16.2+label%3ACherryPickApproved> on our issue tracker for details.

 go1.16.3 (released 2021-04-01) includes fixes to the compiler, linker, runtime, the `go` command, and the `testing` and `time` packages. See the Go 1.16.3 milestone <https://github.com/golang/go/issues?q=milestone%3AGo1.16.3+label%3ACherryPickApproved> on our issue tracker for details.

 go1.16.4 (released 2021-05-06) includes a security fix to the `net/http` package, as well as bug fixes to the compiler, runtime, and the `archive/zip`, `syscall`, and `time` packages. See the Go 1.16.4 milestone <https://github.com/golang/go/issues?q=milestone%3AGo1.16.4+label%3ACherryPickApproved> on our issue tracker for details.

 go1.16.5 (released 2021-06-03) includes security fixes to the `archive/zip`, `math/big`, `net`, and `net/http/httputil` packages, as well as bug fixes to the linker, the `go` command, and the `net/http` package. See the Go 1.16.5 milestone <https://github.com/golang/go/issues?q=milestone%3AGo1.16.5+label%3ACherryPickApproved> on our issue tracker for details.

 go1.16.6 (released 2021-07-12) includes a security fix to the `crypto/tls` package, as well as bug fixes to the compiler, and the `net` and `net/http` packages. See the Go 1.16.6 milestone <https://github.com/golang/go/issues?q=milestone%3AGo1.16.6+label%3ACherryPickApproved> on our issue tracker for details.

 go1.16.7 (released 2021-08-05) includes a security fix to the `net/http/httputil` package, as well as bug fixes to the compiler, linker, runtime, the `go` command, and the `net/http` package. See the Go 1.16.7 milestone <https://github.com/golang/go/issues?q=milestone%3AGo1.16.7+label%3ACherryPickApproved> on our issue tracker for details.

 go1.16.8 (released 2021-09-09) includes a security fix to the `archive/zip` package, as well as bug fixes to the `archive/zip`, `go/internal/gccgoimporter`, `html/template`, `net/http`, and `runtime/pprof` packages. See the Go 1.16.8 milestone <https://github.com/golang/go/issues?q=milestone%3AGo1.16.8+label%3ACherryPickApproved> on our issue tracker for details.

 go1.16.9 (released 2021-10-07) includes security fixes to linker and the `misc/wasm` directory, as well as bug fixes to runtime and the `text/template` package. See the Go 1.16.9 milestone <https://github.com/golang/go/issues?q=milestone%3AGo1.16.9+label%3ACherryPickApproved> on our issue tracker for details.

 go1.16.10 (released 2021-11-04) includes security fixes to the `archive/zip` and `debug/macho` packages, as well as bug fixes to the compiler, linker, runtime, the `misc/wasm` directory, and the `net/http` package. See the Go 1.16.10 milestone <https://github.com/golang/go/issues?q=milestone%3AGo1.16.10+label%3ACherryPickApproved> on our issue tracker for details.

 go1.16.11 (released 2021-12-02) includes fixes to the compiler, runtime, and the `net/http`, `net/http/httptest`, and `time` packages. See the Go 1.16.11 milestone <https://github.com/golang/go/issues?q=milestone%3AGo1.16.11+label%3ACherryPickApproved> on our issue tracker for details.

 go1.16.12 (released 2021-12-09) includes security fixes to the `net/http` and `syscall` packages. See the Go 1.16.12 milestone <https://github.com/golang/go/issues?q=milestone%3AGo1.16.12+label%3ACherryPickApproved> on our issue tracker for details.

 go1.16.13 (released 2022-01-06) includes fixes to the compiler, linker, runtime, and the `net/http` package. See the Go 1.16.13 milestone <https://github.com/golang/go/issues?q=milestone%3AGo1.16.13+label%3ACherryPickApproved> on our issue tracker for details.

 go1.16.14 (released 2022-02-10) includes security fixes to the `go` command, and the `crypto/elliptic` and `math/big` packages, as well as bug fixes to the compiler, linker, runtime, the `go` command, and the `debug/macho`, `debug/pe`, `net/http/httptest`, and `testing` packages. See the Go 1.16.14 milestone <https://github.com/golang/go/issues?q=milestone%3AGo1.16.14+label%3ACherryPickApproved> on our issue tracker for details.

 go1.16.15 (released 2022-03-03) includes a security fix to the `regexp/syntax` package, as well as bug fixes to the compiler, runtime, the `go` command, and the `net` package. See the Go 1.16.15 milestone <https://github.com/golang/go/issues?q=milestone%3AGo1.16.15+label%3ACherryPickApproved> on our issue tracker for details.

## go1.15 (released 2020-08-11)

 Go 1.15 is a major release of Go. Read the Go 1.15 Release Notes for more information.

### Minor revisions

 go1.15.1 (released 2020-09-01) includes security fixes to the `net/http/cgi` and `net/http/fcgi` packages. See the Go 1.15.1 milestone <https://github.com/golang/go/issues?q=milestone%3AGo1.15.1+label%3ACherryPickApproved> on our issue tracker for details.

 go1.15.2 (released 2020-09-09) includes fixes to the compiler, runtime, documentation, the `go` command, and the `net/mail`, `os`, `sync`, and `testing` packages. See the Go 1.15.2 milestone <https://github.com/golang/go/issues?q=milestone%3AGo1.15.2+label%3ACherryPickApproved> on our issue tracker for details.

 go1.15.3 (released 2020-10-14) includes fixes to cgo, the compiler, runtime, the `go` command, and the `bytes`, `plugin`, and `testing` packages. See the Go 1.15.3 milestone <https://github.com/golang/go/issues?q=milestone%3AGo1.15.3+label%3ACherryPickApproved> on our issue tracker for details.

 go1.15.4 (released 2020-11-05) includes fixes to cgo, the compiler, linker, runtime, and the `compress/flate`, `net/http`, `reflect`, and `time` packages. See the Go 1.15.4 milestone <https://github.com/golang/go/issues?q=milestone%3AGo1.15.4+label%3ACherryPickApproved> on our issue tracker for details.

 go1.15.5 (released 2020-11-12) includes security fixes to the `go` command and the `math/big` package. See the Go 1.15.5 milestone <https://github.com/golang/go/issues?q=milestone%3AGo1.15.5+label%3ACherryPickApproved> on our issue tracker for details.

 go1.15.6 (released 2020-12-03) includes fixes to the compiler, linker, runtime, the `go` command, and the `io` package. See the Go 1.15.6 milestone <https://github.com/golang/go/issues?q=milestone%3AGo1.15.6+label%3ACherryPickApproved> on our issue tracker for details.

 go1.15.7 (released 2021-01-19) includes security fixes to the `go` command and the `crypto/elliptic` package. See the Go 1.15.7 milestone <https://github.com/golang/go/issues?q=milestone%3AGo1.15.7+label%3ACherryPickApproved> on our issue tracker for details.

 go1.15.8 (released 2021-02-04) includes fixes to the compiler, linker, runtime, the `go` command, and the `net/http` package. See the Go 1.15.8 milestone <https://github.com/golang/go/issues?q=milestone%3AGo1.15.8+label%3ACherryPickApproved> on our issue tracker for details.

 go1.15.9 (released 2021-03-10) includes security fixes to the `encoding/xml` package. See the Go 1.15.9 milestone <https://github.com/golang/go/issues?q=milestone%3AGo1.15.9+label%3ACherryPickApproved> on our issue tracker for details.

 go1.15.10 (released 2021-03-11) includes fixes to the compiler, the `go` command, and the `net/http`, `os`, `syscall`, and `time` packages. See the Go 1.15.10 milestone <https://github.com/golang/go/issues?q=milestone%3AGo1.15.10+label%3ACherryPickApproved> on our issue tracker for details.

 go1.15.11 (released 2021-04-01) includes fixes to cgo, the compiler, linker, runtime, the `go` command, and the `database/sql` and `net/http` packages. See the Go 1.15.11 milestone <https://github.com/golang/go/issues?q=milestone%3AGo1.15.11+label%3ACherryPickApproved> on our issue tracker for details.

 go1.15.12 (released 2021-05-06) includes a security fix to the `net/http` package, as well as bug fixes to the compiler, runtime, and the `archive/zip`, `syscall`, and `time` packages. See the Go 1.15.12 milestone <https://github.com/golang/go/issues?q=milestone%3AGo1.15.12+label%3ACherryPickApproved> on our issue tracker for details.

 go1.15.13 (released 2021-06-03) includes security fixes to the `archive/zip`, `math/big`, `net`, and `net/http/httputil` packages, as well as bug fixes to the linker, the `go` command, and the `math/big` and `net/http` packages. See the Go 1.15.13 milestone <https://github.com/golang/go/issues?q=milestone%3AGo1.15.13+label%3ACherryPickApproved> on our issue tracker for details.

 go1.15.14 (released 2021-07-12) includes a security fix to the `crypto/tls` package, as well as bug fixes to the linker and the `net` package. See the Go 1.15.14 milestone <https://github.com/golang/go/issues?q=milestone%3AGo1.15.14+label%3ACherryPickApproved> on our issue tracker for details.

 go1.15.15 (released 2021-08-05) includes a security fix to the `net/http/httputil` package, as well as bug fixes to the compiler, runtime, the `go` command, and the `net/http` package. See the Go 1.15.15 milestone <https://github.com/golang/go/issues?q=milestone%3AGo1.15.15+label%3ACherryPickApproved> on our issue tracker for details.

## go1.14 (released 2020-02-25)

 Go 1.14 is a major release of Go. Read the Go 1.14 Release Notes for more information.

### Minor revisions

 go1.14.1 (released 2020-03-19) includes fixes to the go command, tools, and the runtime. See the Go 1.14.1 milestone <https://github.com/golang/go/issues?q=milestone%3AGo1.14.1+label%3ACherryPickApproved> on our issue tracker for details.

 go1.14.2 (released 2020-04-08) includes fixes to cgo, the go command, the runtime, and the `os/exec` and `testing` packages. See the Go 1.14.2 milestone <https://github.com/golang/go/issues?q=milestone%3AGo1.14.2+label%3ACherryPickApproved> on our issue tracker for details.

 go1.14.3 (released 2020-05-14) includes fixes to cgo, the compiler, the runtime, and the `go/doc` and `math/big` packages. See the Go 1.14.3 milestone <https://github.com/golang/go/issues?q=milestone%3AGo1.14.3+label%3ACherryPickApproved> on our issue tracker for details.

 go1.14.4 (released 2020-06-01) includes fixes to the `go` `doc` command, the runtime, and the `encoding/json` and `os` packages. See the Go 1.14.4 milestone <https://github.com/golang/go/issues?q=milestone%3AGo1.14.4+label%3ACherryPickApproved> on our issue tracker for details.

 go1.14.5 (released 2020-07-14) includes security fixes to the `crypto/x509` and `net/http` packages. See the Go 1.14.5 milestone <https://github.com/golang/go/issues?q=milestone%3AGo1.14.5+label%3ACherryPickApproved> on our issue tracker for details.

 go1.14.6 (released 2020-07-16) includes fixes to the `go` command, the compiler, the linker, vet, and the `database/sql`, `encoding/json`, `net/http`, `reflect`, and `testing` packages. See the Go 1.14.6 milestone <https://github.com/golang/go/issues?q=milestone%3AGo1.14.6+label%3ACherryPickApproved> on our issue tracker for details.

 go1.14.7 (released 2020-08-06) includes security fixes to the `encoding/binary` package. See the Go 1.14.7 milestone <https://github.com/golang/go/issues?q=milestone%3AGo1.14.7+label%3ACherryPickApproved> on our issue tracker for details.

 go1.14.8 (released 2020-09-01) includes security fixes to the `net/http/cgi` and `net/http/fcgi` packages. See the Go 1.14.8 milestone <https://github.com/golang/go/issues?q=milestone%3AGo1.14.8+label%3ACherryPickApproved> on our issue tracker for details.

 go1.14.9 (released 2020-09-09) includes fixes to the compiler, linker, runtime, documentation, and the `net/http` and `testing` packages. See the Go 1.14.9 milestone <https://github.com/golang/go/issues?q=milestone%3AGo1.14.9+label%3ACherryPickApproved> on our issue tracker for details.

 go1.14.10 (released 2020-10-14) includes fixes to the compiler, runtime, and the `plugin` and `testing` packages. See the Go 1.14.10 milestone <https://github.com/golang/go/issues?q=milestone%3AGo1.14.10+label%3ACherryPickApproved> on our issue tracker for details.

 go1.14.11 (released 2020-11-05) includes fixes to the runtime, and the `net/http` and `time` packages. See the Go 1.14.11 milestone <https://github.com/golang/go/issues?q=milestone%3AGo1.14.11+label%3ACherryPickApproved> on our issue tracker for details.

 go1.14.12 (released 2020-11-12) includes security fixes to the `go` command and the `math/big` package. See the Go 1.14.12 milestone <https://github.com/golang/go/issues?q=milestone%3AGo1.14.12+label%3ACherryPickApproved> on our issue tracker for details.

 go1.14.13 (released 2020-12-03) includes fixes to the compiler, runtime, and the `go` command. See the Go 1.14.13 milestone <https://github.com/golang/go/issues?q=milestone%3AGo1.14.13+label%3ACherryPickApproved> on our issue tracker for details.

 go1.14.14 (released 2021-01-19) includes security fixes to the `go` command and the `crypto/elliptic` package. See the Go 1.14.14 milestone <https://github.com/golang/go/issues?q=milestone%3AGo1.14.14+label%3ACherryPickApproved> on our issue tracker for details.

 go1.14.15 (released 2021-02-04) includes fixes to the compiler, runtime, the `go` command, and the `net/http` package. See the Go 1.14.15 milestone <https://github.com/golang/go/issues?q=milestone%3AGo1.14.15+label%3ACherryPickApproved> on our issue tracker for details.

## go1.13 (released 2019-09-03)

 Go 1.13 is a major release of Go. Read the Go 1.13 Release Notes for more information.

### Minor revisions

 go1.13.1 (released 2019-09-25) includes security fixes to the `net/http` and `net/textproto` packages. See the Go 1.13.1 milestone <https://github.com/golang/go/issues?q=milestone%3AGo1.13.1+label%3ACherryPickApproved> on our issue tracker for details.

 go1.13.2 (released 2019-10-17) includes security fixes to the compiler and the `crypto/dsa` package. See the Go 1.13.2 milestone <https://github.com/golang/go/issues?q=milestone%3AGo1.13.2+label%3ACherryPickApproved> on our issue tracker for details.

 go1.13.3 (released 2019-10-17) includes fixes to the go command, the toolchain, the runtime, and the `crypto/ecdsa`, `net`, `net/http`, and `syscall` packages. See the Go 1.13.3 milestone <https://github.com/golang/go/issues?q=milestone%3AGo1.13.3+label%3ACherryPickApproved> on our issue tracker for details.

 go1.13.4 (released 2019-10-31) includes fixes to the `net/http` and `syscall` packages. It also fixes an issue on macOS 10.15 Catalina where the non-notarized installer and binaries were being rejected by Gatekeeper. See the Go 1.13.4 milestone <https://github.com/golang/go/issues?q=milestone%3AGo1.13.4+label%3ACherryPickApproved> on our issue tracker for details.

 go1.13.5 (released 2019-12-04) includes fixes to the go command, the runtime, the linker, and the `net/http` package. See the Go 1.13.5 milestone <https://github.com/golang/go/issues?q=milestone%3AGo1.13.5+label%3ACherryPickApproved> on our issue tracker for details.

 go1.13.6 (released 2020-01-09) includes fixes to the runtime and the `net/http` package. See the Go 1.13.6 milestone <https://github.com/golang/go/issues?q=milestone%3AGo1.13.6+label%3ACherryPickApproved> on our issue tracker for details.

 go1.13.7 (released 2020-01-28) includes two security fixes to the `crypto/x509` package. See the Go 1.13.7 milestone <https://github.com/golang/go/issues?q=milestone%3AGo1.13.7+label%3ACherryPickApproved> on our issue tracker for details.

 go1.13.8 (released 2020-02-12) includes fixes to the runtime, and the `crypto/x509` and `net/http` packages. See the Go 1.13.8 milestone <https://github.com/golang/go/issues?q=milestone%3AGo1.13.8+label%3ACherryPickApproved> on our issue tracker for details.

 go1.13.9 (released 2020-03-19) includes fixes to the go command, tools, the runtime, the toolchain, and the `crypto/cypher` package. See the Go 1.13.9 milestone <https://github.com/golang/go/issues?q=milestone%3AGo1.13.9+label%3ACherryPickApproved> on our issue tracker for details.

 go1.13.10 (released 2020-04-08) includes fixes to the go command, the runtime, and the `os/exec` and `time` packages. See the Go 1.13.10 milestone <https://github.com/golang/go/issues?q=milestone%3AGo1.13.10+label%3ACherryPickApproved> on our issue tracker for details.

 go1.13.11 (released 2020-05-14) includes fixes to the compiler. See the Go 1.13.11 milestone <https://github.com/golang/go/issues?q=milestone%3AGo1.13.11+label%3ACherryPickApproved> on our issue tracker for details.

 go1.13.12 (released 2020-06-01) includes fixes to the runtime, and the `go/types` and `math/big` packages. See the Go 1.13.12 milestone <https://github.com/golang/go/issues?q=milestone%3AGo1.13.12+label%3ACherryPickApproved> on our issue tracker for details.

 go1.13.13 (released 2020-07-14) includes security fixes to the `crypto/x509` and `net/http` packages. See the Go 1.13.13 milestone <https://github.com/golang/go/issues?q=milestone%3AGo1.13.13+label%3ACherryPickApproved> on our issue tracker for details.

 go1.13.14 (released 2020-07-16) includes fixes to the compiler, vet, and the `database/sql`, `net/http`, and `reflect` packages. See the Go 1.13.14 milestone <https://github.com/golang/go/issues?q=milestone%3AGo1.13.14+label%3ACherryPickApproved> on our issue tracker for details.

 go1.13.15 (released 2020-08-06) includes security fixes to the `encoding/binary` package. See the Go 1.13.15 milestone <https://github.com/golang/go/issues?q=milestone%3AGo1.13.15+label%3ACherryPickApproved> on our issue tracker for details.

## go1.12 (released 2019-02-25)

 Go 1.12 is a major release of Go. Read the Go 1.12 Release Notes for more information.

### Minor revisions

 go1.12.1 (released 2019-03-14) includes fixes to cgo, the compiler, the go command, and the `fmt`, `net/smtp`, `os`, `path/filepath`, `sync`, and `text/template` packages. See the Go 1.12.1 milestone <https://github.com/golang/go/issues?q=milestone%3AGo1.12.1+label%3ACherryPickApproved> on our issue tracker for details.

 go1.12.2 (released 2019-04-05) includes security fixes to the runtime, as well as bug fixes to the compiler, the go command, and the `doc`, `net`, `net/http/httputil`, and `os` packages. See the Go 1.12.2 milestone <https://github.com/golang/go/issues?q=milestone%3AGo1.12.2+label%3ACherryPickApproved> on our issue tracker for details.

 go1.12.3 (released 2019-04-08) was accidentally released without its intended fix. It is identical to go1.12.2, except for its version number. The intended fix is in go1.12.4.

 go1.12.4 (released 2019-04-11) fixes an issue where using the prebuilt binary releases on older versions of GNU/Linux led to failures when linking programs that used cgo. Only Linux users who hit this issue need to update.

 go1.12.5 (released 2019-05-06) includes fixes to the compiler, the linker, the go command, the runtime, and the `os` package. See the Go 1.12.5 milestone <https://github.com/golang/go/issues?q=milestone%3AGo1.12.5+label%3ACherryPickApproved> on our issue tracker for details.

 go1.12.6 (released 2019-06-11) includes fixes to the compiler, the linker, the go command, and the `crypto/x509`, `net/http`, and `os` packages. See the Go 1.12.6 milestone <https://github.com/golang/go/issues?q=milestone%3AGo1.12.6+label%3ACherryPickApproved> on our issue tracker for details.

 go1.12.7 (released 2019-07-08) includes fixes to cgo, the compiler, and the linker. See the Go 1.12.7 milestone <https://github.com/golang/go/issues?q=milestone%3AGo1.12.7+label%3ACherryPickApproved> on our issue tracker for details.

 go1.12.8 (released 2019-08-13) includes security fixes to the `net/http` and `net/url` packages. See the Go 1.12.8 milestone <https://github.com/golang/go/issues?q=milestone%3AGo1.12.8+label%3ACherryPickApproved> on our issue tracker for details.

 go1.12.9 (released 2019-08-15) includes fixes to the linker, and the `math/big` and `os` packages. See the Go 1.12.9 milestone <https://github.com/golang/go/issues?q=milestone%3AGo1.12.9+label%3ACherryPickApproved> on our issue tracker for details.

 go1.12.10 (released 2019-09-25) includes security fixes to the `net/http` and `net/textproto` packages. See the Go 1.12.10 milestone <https://github.com/golang/go/issues?q=milestone%3AGo1.12.10+label%3ACherryPickApproved> on our issue tracker for details.

 go1.12.11 (released 2019-10-17) includes security fixes to the `crypto/dsa` package. See the Go 1.12.11 milestone <https://github.com/golang/go/issues?q=milestone%3AGo1.12.11+label%3ACherryPickApproved> on our issue tracker for details.

 go1.12.12 (released 2019-10-17) includes fixes to the go command, runtime, and the `net` and `syscall` packages. See the Go 1.12.12 milestone <https://github.com/golang/go/issues?q=milestone%3AGo1.12.12+label%3ACherryPickApproved> on our issue tracker for details.

 go1.12.13 (released 2019-10-31) fixes an issue on macOS 10.15 Catalina where the non-notarized installer and binaries were being rejected by Gatekeeper. Only macOS users who hit this issue need to update.

 go1.12.14 (released 2019-12-04) includes a fix to the runtime. See the Go 1.12.14 milestone <https://github.com/golang/go/issues?q=milestone%3AGo1.12.14+label%3ACherryPickApproved> on our issue tracker for details.

 go1.12.15 (released 2020-01-09) includes fixes to the runtime and the `net/http` package. See the Go 1.12.15 milestone <https://github.com/golang/go/issues?q=milestone%3AGo1.12.15+label%3ACherryPickApproved> on our issue tracker for details.

 go1.12.16 (released 2020-01-28) includes two security fixes to the `crypto/x509` package. See the Go 1.12.16 milestone <https://github.com/golang/go/issues?q=milestone%3AGo1.12.16+label%3ACherryPickApproved> on our issue tracker for details.

 go1.12.17 (released 2020-02-12) includes a fix to the runtime. See the Go 1.12.17 milestone <https://github.com/golang/go/issues?q=milestone%3AGo1.12.17+label%3ACherryPickApproved> on our issue tracker for details.

## go1.11 (released 2018-08-24)

 Go 1.11 is a major release of Go. Read the Go 1.11 Release Notes for more information.

### Minor revisions

 go1.11.1 (released 2018-10-01) includes fixes to the compiler, documentation, go command, runtime, and the `crypto/x509`, `encoding/json`, `go/types`, `net`, `net/http`, and `reflect` packages. See the Go 1.11.1 milestone <https://github.com/golang/go/issues?q=milestone%3AGo1.11.1+label%3ACherryPickApproved> on our issue tracker for details.

 go1.11.2 (released 2018-11-02) includes fixes to the compiler, linker, documentation, go command, and the `database/sql` and `go/types` packages. See the Go 1.11.2 milestone <https://github.com/golang/go/issues?q=milestone%3AGo1.11.2+label%3ACherryPickApproved> on our issue tracker for details.

 go1.11.3 (released 2018-12-12) includes three security fixes to "go get" and the `crypto/x509` package. See the Go 1.11.3 milestone <https://github.com/golang/go/issues?q=milestone%3AGo1.11.3+label%3ACherryPickApproved> on our issue tracker for details.

 go1.11.4 (released 2018-12-14) includes fixes to cgo, the compiler, linker, runtime, documentation, go command, and the `go/types` and `net/http` packages. It includes a fix to a bug introduced in Go 1.11.3 that broke `go` `get` for import path patterns containing "`...`". See the Go 1.11.4 milestone <https://github.com/golang/go/issues?q=milestone%3AGo1.11.4+label%3ACherryPickApproved> on our issue tracker for details.

 go1.11.5 (released 2019-01-23) includes a security fix to the `crypto/elliptic` package. See the Go 1.11.5 milestone <https://github.com/golang/go/issues?q=milestone%3AGo1.11.5+label%3ACherryPickApproved> on our issue tracker for details.

 go1.11.6 (released 2019-03-14) includes fixes to cgo, the compiler, linker, runtime, go command, and the `crypto/x509`, `encoding/json`, `net`, and `net/url` packages. See the Go 1.11.6 milestone <https://github.com/golang/go/issues?q=milestone%3AGo1.11.6+label%3ACherryPickApproved> on our issue tracker for details.

 go1.11.7 (released 2019-04-05) includes fixes to the runtime and the `net` package. See the Go 1.11.7 milestone <https://github.com/golang/go/issues?q=milestone%3AGo1.11.7+label%3ACherryPickApproved> on our issue tracker for details.

 go1.11.8 (released 2019-04-08) was accidentally released without its intended fix. It is identical to go1.11.7, except for its version number. The intended fix is in go1.11.9.

 go1.11.9 (released 2019-04-11) fixes an issue where using the prebuilt binary releases on older versions of GNU/Linux led to failures when linking programs that used cgo. Only Linux users who hit this issue need to update.

 go1.11.10 (released 2019-05-06) includes security fixes to the runtime, as well as bug fixes to the linker. See the Go 1.11.10 milestone <https://github.com/golang/go/issues?q=milestone%3AGo1.11.10+label%3ACherryPickApproved> on our issue tracker for details.

 go1.11.11 (released 2019-06-11) includes a fix to the `crypto/x509` package. See the Go 1.11.11 milestone <https://github.com/golang/go/issues?q=milestone%3AGo1.11.11+label%3ACherryPickApproved> on our issue tracker for details.

 go1.11.12 (released 2019-07-08) includes fixes to the compiler and the linker. See the Go 1.11.12 milestone <https://github.com/golang/go/issues?q=milestone%3AGo1.11.12+label%3ACherryPickApproved> on our issue tracker for details.

 go1.11.13 (released 2019-08-13) includes security fixes to the `net/http` and `net/url` packages. See the Go 1.11.13 milestone <https://github.com/golang/go/issues?q=milestone%3AGo1.11.13+label%3ACherryPickApproved> on our issue tracker for details.

## go1.10 (released 2018-02-16)

 Go 1.10 is a major release of Go. Read the Go 1.10 Release Notes for more information.

### Minor revisions

 go1.10.1 (released 2018-03-28) includes security fixes to the go command, as well as bug fixes to the compiler, runtime, and the `archive/zip`, `crypto/tls`, `crypto/x509`, `encoding/json`, `net`, `net/http`, and `net/http/pprof` packages. See the Go 1.10.1 milestone <https://github.com/golang/go/issues?q=milestone%3AGo1.10.1+label%3ACherryPickApproved> on our issue tracker for details.

 go1.10.2 (released 2018-05-01) includes fixes to the compiler, linker, and go command. See the Go 1.10.2 milestone <https://github.com/golang/go/issues?q=milestone%3AGo1.10.2+label%3ACherryPickApproved> on our issue tracker for details.

 go1.10.3 (released 2018-06-05) includes fixes to the go command, and the `crypto/tls`, `crypto/x509`, and `strings` packages. In particular, it adds  minimal support to the go command for the vgo transition <https://go.googlesource.com/go/+/d4e21288e444d3ffd30d1a0737f15ea3fc3b8ad9>. See the Go 1.10.3 milestone <https://github.com/golang/go/issues?q=milestone%3AGo1.10.3+label%3ACherryPickApproved> on our issue tracker for details.

 go1.10.4 (released 2018-08-24) includes fixes to the go command, linker, and the `bytes`, `mime/multipart`, `net/http`, and `strings` packages. See the Go 1.10.4 milestone <https://github.com/golang/go/issues?q=milestone%3AGo1.10.4+label%3ACherryPickApproved> on our issue tracker for details.

 go1.10.5 (released 2018-11-02) includes fixes to the go command, linker, runtime, and the `database/sql` package. See the Go 1.10.5 milestone <https://github.com/golang/go/issues?q=milestone%3AGo1.10.5+label%3ACherryPickApproved> on our issue tracker for details.

 go1.10.6 (released 2018-12-12) includes three security fixes to "go get" and the `crypto/x509` package. It contains the same fixes as Go 1.11.3 and was released at the same time. See the Go 1.10.6 milestone <https://github.com/golang/go/issues?q=milestone%3AGo1.10.6+label%3ACherryPickApproved> on our issue tracker for details.

 go1.10.7 (released 2018-12-14) includes a fix to a bug introduced in Go 1.10.6 that broke `go` `get` for import path patterns containing "`...`". See the  Go 1.10.7 milestone <https://github.com/golang/go/issues?q=milestone%3AGo1.10.7+label%3ACherryPickApproved> on our issue tracker for details.

 go1.10.8 (released 2019-01-23) includes a security fix to the `crypto/elliptic` package. See the Go 1.10.8 milestone <https://github.com/golang/go/issues?q=milestone%3AGo1.10.8+label%3ACherryPickApproved> on our issue tracker for details.

## go1.9 (released 2017-08-24)

 Go 1.9 is a major release of Go. Read the Go 1.9 Release Notes for more information.

### Minor revisions

 go1.9.1 (released 2017-10-04) includes two security fixes. See the Go 1.9.1 milestone <https://github.com/golang/go/issues?q=milestone%3AGo1.9.1+label%3ACherryPickApproved> on our issue tracker for details.

 go1.9.2 (released 2017-10-25) includes fixes to the compiler, linker, runtime, documentation, `go` command, and the `crypto/x509`, `database/sql`, `log`, and `net/smtp` packages. It includes a fix to a bug introduced in Go 1.9.1 that broke `go` `get` of non-Git repositories under certain conditions. See the Go 1.9.2 milestone <https://github.com/golang/go/issues?q=milestone%3AGo1.9.2+label%3ACherryPickApproved> on our issue tracker for details.

 go1.9.3 (released 2018-01-22) includes security fixes to the `net/url` package, as well as bug fixes to the compiler, runtime, and the `database/sql`, `math/big`, and `net/http` packages. See the Go 1.9.3 milestone <https://github.com/golang/go/issues?q=milestone%3AGo1.9.3+label%3ACherryPickApproved> on our issue tracker for details.

 go1.9.4 (released 2018-02-07) includes a security fix to "go get". See the Go 1.9.4 milestone <https://github.com/golang/go/issues?q=milestone%3AGo1.9.4+label%3ACherryPickApproved> on our issue tracker for details.

 go1.9.5 (released 2018-03-28) includes security fixes to the go command, as well as bug fixes to the compiler, go command, and the `net/http/pprof` package. See the Go 1.9.5 milestone <https://github.com/golang/go/issues?q=milestone%3AGo1.9.5+label%3ACherryPickApproved> on our issue tracker for details.

 go1.9.6 (released 2018-05-01) includes fixes to the compiler and go command. See the Go 1.9.6 milestone <https://github.com/golang/go/issues?q=milestone%3AGo1.9.6+label%3ACherryPickApproved> on our issue tracker for details.

 go1.9.7 (released 2018-06-05) includes fixes to the go command, and the `crypto/x509` and `strings` packages. In particular, it adds  minimal support to the go command for the vgo transition <https://go.googlesource.com/go/+/d4e21288e444d3ffd30d1a0737f15ea3fc3b8ad9>. See the Go 1.9.7 milestone <https://github.com/golang/go/issues?q=milestone%3AGo1.9.7+label%3ACherryPickApproved> on our issue tracker for details.

## go1.8 (released 2017-02-16)

 Go 1.8 is a major release of Go. Read the Go 1.8 Release Notes for more information.

### Minor revisions

 go1.8.1 (released 2017-04-07) includes fixes to the compiler, linker, runtime, documentation, `go` command and the `crypto/tls`, `encoding/xml`, `image/png`, `net`, `net/http`, `reflect`, `text/template`, and `time` packages. See the Go 1.8.1 milestone <https://github.com/golang/go/issues?q=milestone%3AGo1.8.1> on our issue tracker for details.

 go1.8.2 (released 2017-05-23) includes a security fix to the `crypto/elliptic` package. See the Go 1.8.2 milestone <https://github.com/golang/go/issues?q=milestone%3AGo1.8.2> on our issue tracker for details.

 go1.8.3 (released 2017-05-24) includes fixes to the compiler, runtime, documentation, and the `database/sql` package. See the Go 1.8.3 milestone <https://github.com/golang/go/issues?q=milestone%3AGo1.8.3> on our issue tracker for details.

 go1.8.4 (released 2017-10-04) includes two security fixes. It contains the same fixes as Go 1.9.1 and was released at the same time. See the Go 1.8.4 milestone <https://github.com/golang/go/issues?q=milestone%3AGo1.8.4> on our issue tracker for details.

 go1.8.5 (released 2017-10-25) includes fixes to the compiler, linker, runtime, documentation, `go` command, and the `crypto/x509` and `net/smtp` packages. It includes a fix to a bug introduced in Go 1.8.4 that broke `go` `get` of non-Git repositories under certain conditions. See the Go 1.8.5 milestone <https://github.com/golang/go/issues?q=milestone%3AGo1.8.5> on our issue tracker for details.

 go1.8.6 (released 2018-01-22) includes the same fix in `math/big` as Go 1.9.3 and was released at the same time. See the Go 1.8.6 milestone <https://github.com/golang/go/issues?q=milestone%3AGo1.8.6> on our issue tracker for details.

 go1.8.7 (released 2018-02-07) includes a security fix to "go get". It contains the same fix as Go 1.9.4 and was released at the same time. See the Go 1.8.7 <https://github.com/golang/go/issues?q=milestone%3AGo1.8.7> milestone on our issue tracker for details.

## go1.7 (released 2016-08-15)

 Go 1.7 is a major release of Go. Read the Go 1.7 Release Notes for more information.

### Minor revisions

 go1.7.1 (released 2016-09-07) includes fixes to the compiler, runtime, documentation, and the `compress/flate`, `hash/crc32`, `io`, `net`, `net/http`, `path/filepath`, `reflect`, and `syscall` packages. See the Go 1.7.1 milestone <https://github.com/golang/go/issues?q=milestone%3AGo1.7.1> on our issue tracker for details.

 go1.7.2 should not be used. It was tagged but not fully released. The release was deferred due to a last minute bug report. Use go1.7.3 instead, and refer to the summary of changes below.

 go1.7.3 (released 2016-10-19) includes fixes to the compiler, runtime, and the `crypto/cipher`, `crypto/tls`, `net/http`, and `strings` packages. See the Go 1.7.3 milestone <https://github.com/golang/go/issues?q=milestone%3AGo1.7.3> on our issue tracker for details.

 go1.7.4 (released 2016-12-01) includes two security fixes. See the Go 1.7.4 milestone <https://github.com/golang/go/issues?q=milestone%3AGo1.7.4> on our issue tracker for details.

 go1.7.5 (released 2017-01-26) includes fixes to the compiler, runtime, and the `crypto/x509` and `time` packages. See the Go 1.7.5 milestone <https://github.com/golang/go/issues?q=milestone%3AGo1.7.5> on our issue tracker for details.

 go1.7.6 (released 2017-05-23) includes the same security fix as Go 1.8.2 and was released at the same time. See the Go 1.8.2 milestone <https://github.com/golang/go/issues?q=milestone%3AGo1.8.2> on our issue tracker for details.

## go1.6 (released 2016-02-17)

 Go 1.6 is a major release of Go. Read the Go 1.6 Release Notes for more information.

### Minor revisions

 go1.6.1 (released 2016-04-12) includes two security fixes. See the Go 1.6.1 milestone <https://github.com/golang/go/issues?q=milestone%3AGo1.6.1> on our issue tracker for details.

 go1.6.2 (released 2016-04-20) includes fixes to the compiler, runtime, tools, documentation, and the `mime/multipart`, `net/http`, and `sort` packages. See the Go 1.6.2 milestone <https://github.com/golang/go/issues?q=milestone%3AGo1.6.2> on our issue tracker for details.

 go1.6.3 (released 2016-07-17) includes security fixes to the `net/http/cgi` package and `net/http` package when used in a CGI environment. See the Go 1.6.3 milestone <https://github.com/golang/go/issues?q=milestone%3AGo1.6.3> on our issue tracker for details.

 go1.6.4 (released 2016-12-01) includes two security fixes. It contains the same fixes as Go 1.7.4 and was released at the same time. See the Go 1.7.4 milestone <https://github.com/golang/go/issues?q=milestone%3AGo1.7.4> on our issue tracker for details.

## go1.5 (released 2015-08-19)

 Go 1.5 is a major release of Go. Read the Go 1.5 Release Notes for more information.

### Minor revisions

 go1.5.1 (released 2015-09-08) includes bug fixes to the compiler, assembler, and the `fmt`, `net/textproto`, `net/http`, and `runtime` packages. See the Go 1.5.1 milestone <https://github.com/golang/go/issues?q=milestone%3AGo1.5.1> on our issue tracker for details.

 go1.5.2 (released 2015-12-02) includes bug fixes to the compiler, linker, and the `mime/multipart`, `net`, and `runtime` packages. See the Go 1.5.2 milestone <https://github.com/golang/go/issues?q=milestone%3AGo1.5.2> on our issue tracker for details.

 go1.5.3 (released 2016-01-13) includes a security fix to the `math/big` package affecting the `crypto/tls` package. See the release announcement for details.

 go1.5.4 (released 2016-04-12) includes two security fixes. It contains the same fixes as Go 1.6.1 and was released at the same time. See the Go 1.6.1 milestone <https://github.com/golang/go/issues?q=milestone%3AGo1.6.1> on our issue tracker for details.

## go1.4 (released 2014-12-10)

 Go 1.4 is a major release of Go. Read the Go 1.4 Release Notes for more information.

### Minor revisions

 go1.4.1 (released 2015-01-15) includes bug fixes to the linker and the `log`, `syscall`, and `runtime` packages. See the Go 1.4.1 milestone on our issue tracker <https://github.com/golang/go/issues?q=milestone%3AGo1.4.1> for details.

 go1.4.2 (released 2015-02-17) includes security fixes to the compiler, and bug fixes to the `go` command, the compiler and linker, and the `runtime`, `syscall`, `reflect`, and `math/big` packages. See the Go 1.4.2 milestone on our issue tracker <https://github.com/golang/go/issues?q=milestone%3AGo1.4.2> for details.

 go1.4.3 (released 2015-09-22) includes security fixes to the `net/http` package and bug fixes to the `runtime` package. See the Go 1.4.3 milestone on our issue tracker <https://github.com/golang/go/issues?q=milestone%3AGo1.4.3> for details.

## go1.3 (released 2014-06-18)

 Go 1.3 is a major release of Go. Read the Go 1.3 Release Notes for more information.

### Minor revisions

 go1.3.1 (released 2014-08-13) includes bug fixes to the compiler and the `runtime`, `net`, and `crypto/rsa` packages. See the change history <https://github.com/golang/go/commits/go1.3.1> for details.

 go1.3.2 (released 2014-09-25) includes security fixes to the `crypto/tls` package and bug fixes to cgo. See the change history <https://github.com/golang/go/commits/go1.3.2> for details.

 go1.3.3 (released 2014-09-30) includes further bug fixes to cgo, the runtime package, and the nacl port. See the change history <https://github.com/golang/go/commits/go1.3.3> for details.

## go1.2 (released 2013-12-01)

 Go 1.2 is a major release of Go. Read the Go 1.2 Release Notes for more information.

### Minor revisions

 go1.2.1 (released 2014-03-02) includes bug fixes to the `runtime`, `net`, and `database/sql` packages. See the change history <https://github.com/golang/go/commits/go1.2.1> for details.

 go1.2.2 (released 2014-05-05) includes a security fix <https://github.com/golang/go/commits/go1.2.2> that affects the tour binary included in the binary distributions (thanks to Guillaume T).

## go1.1 (released 2013-05-13)

 Go 1.1 is a major release of Go. Read the Go 1.1 Release Notes for more information.

### Minor revisions

 go1.1.1 (released 2013-06-13) includes a security fix to the compiler and several bug fixes to the compiler and runtime. See the change history <https://github.com/golang/go/commits/go1.1.1> for details.

 go1.1.2 (released 2013-08-13) includes fixes to the `gc` compiler and `cgo`, and the `bufio`, `runtime`, `syscall`, and `time` packages. See the change history <https://github.com/golang/go/commits/go1.1.2> for details. If you use package syscall's `Getrlimit` and `Setrlimit` functions under Linux on the ARM or 386 architectures, please note change 11803043 that fixes issue 5949.

## go1 (released 2012-03-28)

 Go 1 is a major release of Go that will be stable in the long term. Read the Go 1 Release Notes for more information.

 It is intended that programs written for Go 1 will continue to compile and run correctly, unchanged, under future versions of Go 1. Read the Go 1 compatibility document for more about the future of Go 1.

 The go1 release corresponds to `weekly.2012-03-27`.

### Minor revisions

 go1.0.1 (released 2012-04-25) was issued to fix an escape analysis bug that can lead to memory corruption. It also includes several minor code and documentation fixes.

 go1.0.2 (released 2012-06-13) was issued to fix two bugs in the implementation of maps using struct or array keys: issue 3695 and issue 3573. It also includes many minor code and documentation fixes.

 go1.0.3 (released 2012-09-21) includes minor code and documentation fixes.

 See the go1 release branch history <https://github.com/golang/go/commits/release-branch.go1> for the complete list of changes.

## Older releases

 See the Pre-Go 1 Release History page for notes on earlier releases.
