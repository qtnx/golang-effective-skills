---
source_name: "External Linked Documentation"
source_url: "https://go.dev/doc/devel/release"
source_path: "sources/raw/external/go-dev-doc-devel-release-d3e2273091.html"
license_ref: ""
---

# Release History

## go1.1 (released 2013-05-13)

 Go 1.1 is a major release of Go. Read the Go 1.1 Release Notes for more information.

### Minor revisions

 go1.1.1 (released 2013-06-13) includes a security fix to the compiler and several bug fixes to the compiler and runtime. See the change history <https://github.com/golang/go/commits/go1.1.1> for details.

 go1.1.2 (released 2013-08-13) includes fixes to the `gc` compiler and `cgo`, and the `bufio`, `runtime`, `syscall`, and `time` packages. See the change history <https://github.com/golang/go/commits/go1.1.2> for details. If you use package syscall's `Getrlimit` and `Setrlimit` functions under Linux on the ARM or 386 architectures, please note change 11803043 that fixes issue 5949.

# Release History

## go1 (released 2012-03-28)

 Go 1 is a major release of Go that will be stable in the long term. Read the Go 1 Release Notes for more information.

 It is intended that programs written for Go 1 will continue to compile and run correctly, unchanged, under future versions of Go 1. Read the Go 1 compatibility document for more about the future of Go 1.

 The go1 release corresponds to `weekly.2012-03-27`.

### Minor revisions

 go1.0.1 (released 2012-04-25) was issued to fix an escape analysis bug that can lead to memory corruption. It also includes several minor code and documentation fixes.

 go1.0.2 (released 2012-06-13) was issued to fix two bugs in the implementation of maps using struct or array keys: issue 3695 and issue 3573. It also includes many minor code and documentation fixes.

 go1.0.3 (released 2012-09-21) includes minor code and documentation fixes.

 See the go1 release branch history <https://github.com/golang/go/commits/release-branch.go1> for the complete list of changes.

# Release History

## Older releases

 See the Pre-Go 1 Release History page for notes on earlier releases.
