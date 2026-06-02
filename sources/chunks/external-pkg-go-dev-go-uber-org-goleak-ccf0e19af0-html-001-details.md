---
source_name: "External Linked Documentation"
source_url: "https://pkg.go.dev/go.uber.org/goleak"
source_path: "sources/raw/external/pkg-go-dev-go-uber-org-goleak-ccf0e19af0.html"
license_ref: ""
---

# Create a test binary which will be used to run each test individually

goleak package - go.uber.org/goleak - Go Packages
## Details

-     Valid go.mod <https://github.com/uber-go/goleak/tree/v1.3.0/go.mod> file
 The Go module system was introduced in Go 1.11 and is the official dependency management solution for Go.

-     Redistributable license
 Redistributable licenses place minimal restrictions on how software can be used, modified, and redistributed.

-     Tagged version
Modules with tagged versions give importers more predictable builds.

-     Stable version
When a project reaches major version v1 it is considered stable.

-  Learn more about best practices

# Create a test binary which will be used to run each test individually

## Repository
   github.com/uber-go/goleak  <https://github.com/uber-go/goleak>

# Create a test binary which will be used to run each test individually

##   README ¶

### goleak  <https://godoc.org/go.uber.org/goleak>  <https://github.com/uber-go/goleak/actions/workflows/ci.yml>  <https://codecov.io/gh/uber-go/goleak>

Goroutine leak detector to help avoid Goroutine leaks.

#### Installation

You can use `go get` to get the latest version:

`go get -u go.uber.org/goleak`

`goleak` also supports semver releases.

Note that go-leak only supports <https://go.dev/doc/devel/release#policy> the two most recent minor versions of Go.

#### Quick Start

To verify that there are no unexpected goroutines running at the end of a test:

```go
func TestA(t *testing.T) {
	defer goleak.VerifyNone(t)

	// test logic here.
}

```

Instead of checking for leaks at the end of every test, `goleak` can also be run at the end of every test package by creating a `TestMain` function for your package:

```go
func TestMain(m *testing.M) {
	goleak.VerifyTestMain(m)
}

```

#### Determine Source of Package Leaks

When verifying leaks using `TestMain`, the leak test is only run once after all tests have been run. This is typically enough to ensure there's no goroutines leaked from tests, but when there are leaks, it's hard to determine which test is causing them.

You can use the following bash script to determine the source of the failing test:

```go
# Create a test binary which will be used to run each test individually
$ go test -c -o tests

# Run each test individually, printing "." for successful tests, or the test name
# for failing tests.
$ for test in $(go test -list . | grep -E "^(Test|Example)"); do ./tests -test.run "^$test\$" &>/dev/null && echo -n "." || echo -e "\n$test failed"; done

```

This will only print names of failing tests which can be investigated individually. E.g.,

```go
.....
TestLeakyTest failed
.......

```

#### Stability

goleak is v1 and follows SemVer <http://semver.org/> strictly.

No breaking changes will be made to exported APIs before 2.0.

 Expand ▾ Collapse ▴
