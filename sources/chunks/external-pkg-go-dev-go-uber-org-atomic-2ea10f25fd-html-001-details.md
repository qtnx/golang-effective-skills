---
source_name: "External Linked Documentation"
source_url: "https://pkg.go.dev/go.uber.org/atomic"
source_path: "sources/raw/external/pkg-go-dev-go-uber-org-atomic-2ea10f25fd.html"
license_ref: ""
---

atomic package - go.uber.org/atomic - Go Packages
## Details

-     Valid go.mod <https://github.com/uber-go/atomic/tree/v1.11.0/go.mod> file
 The Go module system was introduced in Go 1.11 and is the official dependency management solution for Go.

-     Redistributable license
 Redistributable licenses place minimal restrictions on how software can be used, modified, and redistributed.

-     Tagged version
Modules with tagged versions give importers more predictable builds.

-     Stable version
When a project reaches major version v1 it is considered stable.

-  Learn more about best practices

## Repository
   github.com/uber-go/atomic  <https://github.com/uber-go/atomic>

##   README ¶

### atomic  <https://godoc.org/go.uber.org/atomic>  <https://github.com/uber-go/atomic/actions/workflows/go.yml>  <https://codecov.io/gh/uber-go/atomic>  <https://goreportcard.com/report/go.uber.org/atomic>

Simple wrappers for primitive types to enforce atomic access.

#### Installation

```go
$ go get -u go.uber.org/atomic@v1

```
 Legacy Import Path
As of v1.5.0, the import path `go.uber.org/atomic` is the only supported way of using this package. If you are using Go modules, this package will fail to compile with the legacy import path path `github.com/uber-go/atomic`.

We recommend migrating your code to the new import path but if you're unable to do so, or if your dependencies are still using the old import path, you will have to add a `replace` directive to your `go.mod` file downgrading the legacy import path to an older version.

```go
replace github.com/uber-go/atomic => github.com/uber-go/atomic v1.4.0

```

You can do so automatically by running the following command.

```go
$ go mod edit -replace github.com/uber-go/atomic=github.com/uber-go/atomic@v1.4.0

```

#### Usage

The standard library's `sync/atomic` is powerful, but it's easy to forget which variables must be accessed atomically. `go.uber.org/atomic` preserves all the functionality of the standard library, but wraps the primitive types to provide a safer, more convenient API.

```go
var atom atomic.Uint32
atom.Store(42)
atom.Sub(2)
atom.CAS(40, 11)

```

See the documentation <https://godoc.org/go.uber.org/atomic> for a complete API specification.

#### Development Status

Stable.

Released under the MIT License <https://github.com/uber-go/atomic/blob/v1.11.0/LICENSE.txt>.

 Expand ▾ Collapse ▴
