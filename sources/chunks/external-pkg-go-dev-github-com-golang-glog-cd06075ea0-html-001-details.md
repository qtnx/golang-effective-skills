---
source_name: "External Linked Documentation"
source_url: "https://pkg.go.dev/github.com/golang/glog"
source_path: "sources/raw/external/pkg-go-dev-github-com-golang-glog-cd06075ea0.html"
license_ref: ""
---

glog package - github.com/golang/glog - Go Packages
## Details

-     Valid go.mod <https://github.com/golang/glog/tree/v1.2.5/go.mod> file
 The Go module system was introduced in Go 1.11 and is the official dependency management solution for Go.

-     Redistributable license
 Redistributable licenses place minimal restrictions on how software can be used, modified, and redistributed.

-     Tagged version
Modules with tagged versions give importers more predictable builds.

-     Stable version
When a project reaches major version v1 it is considered stable.

-  Learn more about best practices

## Repository
   github.com/golang/glog  <https://github.com/golang/glog>

##   README ¶

### glog

 <https://pkg.go.dev/github.com/golang/glog>

Leveled execution logs for Go.

This is an efficient pure Go implementation of leveled logs in the manner of the open source C++ package _glog_ <https://github.com/google/glog>.

By binding methods to booleans it is possible to use the log package without paying the expense of evaluating the arguments to the log. Through the `-vmodule` flag, the package also provides fine-grained control over logging at the file level.

The comment from `glog.go` introduces the ideas:

Package _glog_ implements logging analogous to the Google-internal C++ INFO/ERROR/V setup. It provides the functions Info, Warning, Error, Fatal, plus formatting variants such as Infof. It also provides V-style loggingcontrolled by the `-v` and `-vmodule=file=2` flags.

Basic examples:

```go
glog.Info("Prepare to repel boarders")

glog.Fatalf("Initialization failed: %s", err)

```

See the documentation for the V function for an explanation of these examples:

```go
if glog.V(2) {
	glog.Info("Starting transaction...")
}
glog.V(2).Infoln("Processed", nItems, "elements")

```

The repository contains an open source version of the log package used inside Google. The master copy of the source lives inside Google, not here. The code in this repo is for export only and is not itself under development. Feature requests will be ignored.

Send bug reports to golang-nuts@googlegroups.com.

 Expand ▾ Collapse ▴
