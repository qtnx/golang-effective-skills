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

## Repository
   github.com/uber-go/goleak  <https://github.com/uber-go/goleak>

## Links

-    Open Source Insights  <https://deps.dev/go/go.uber.org%2Fgoleak/v1.3.0>

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

##   Documentation ¶

Package goleak is a Goroutine leak detector.

-  func Find(options ...Option) error
-  func VerifyNone(t TestingT, options ...Option)
-  func VerifyTestMain(m TestingM, options ...Option)
-  type Option
-
-  func Cleanup(cleanupFunc func(exitCode int)) Option
-  func IgnoreAnyFunction(f string) Option
-  func IgnoreCurrent() Option
-  func IgnoreTopFunction(f string) Option

-  type TestingM
-  type TestingT

This section is empty.

This section is empty.

```go
func Find(options ...Option) error
```

Find looks for extra goroutines, and returns a descriptive error if any are found.

```go
func VerifyNone(t TestingT, options ...Option)
```

VerifyNone marks the given TestingT as failed if any extra goroutines are found by Find. This is a helper method to make it easier to integrate in tests by doing:

```go
defer VerifyNone(t)

```

VerifyNone is currently incompatible with t.Parallel because it cannot associate specific goroutines with specific tests. Thus, non-leaking goroutines from other tests running in parallel could fail this check. If you need to run tests in parallel, use VerifyTestMain instead, which will verify that no leaking goroutines exist after ALL tests finish.

```go
func VerifyTestMain(m TestingM, options ...Option)
```

VerifyTestMain can be used in a TestMain function for package tests to verify that there were no goroutine leaks. To use it, your TestMain function should look like:

```go
func TestMain(m *testing.M) {
  goleak.VerifyTestMain(m)
}

```

See https://golang.org/pkg/testing/#hdr-Main <https://golang.org/pkg/testing/#hdr-Main> for more details.

This will run all tests as per normal, and if they were successful, look for any goroutine leaks and fail the tests if any leaks were found.

```go
type Option interface {
	// contains filtered or unexported methods
}
```

Option lets users specify custom verifications.

```go
func Cleanup(cleanupFunc func(exitCode int)) Option
```

Cleanup sets up a cleanup function that will be executed at the end of the leak check. When passed to VerifyTestMain, the exit code passed to cleanupFunc will be set to the exit code of TestMain. When passed to VerifyNone, the exit code will be set to 0. This cannot be passed to Find.

```go
func IgnoreAnyFunction(f string) Option
```

IgnoreAnyFunction ignores goroutines where the specified function is present anywhere in the stack.

The function name must be fully qualified, e.g.,

```go
go.uber.org/goleak.IgnoreAnyFunction

```

For methods, the fully qualified form looks like:

```go
go.uber.org/goleak.(*MyType).MyMethod

```

```go
func IgnoreCurrent() Option
```

IgnoreCurrent records all current goroutines when the option is created, and ignores them in any future Find/Verify calls.

```go
func IgnoreTopFunction(f string) Option
```

IgnoreTopFunction ignores any goroutines where the specified function is at the top of the stack. The function name should be fully qualified, e.g., go.uber.org/goleak.IgnoreTopFunction

```go
type TestingM interface {
	Run() int
}
```

TestingM is the minimal subset of testing.M that we use.

```go
type TestingT interface {
	Error(...interface{})
}
```

TestingT is the minimal subset of testing.TB that we use.

##   Source Files ¶
 View all Source files <https://github.com/uber-go/goleak/tree/v1.3.0>

- doc.go <https://github.com/uber-go/goleak/blob/v1.3.0/doc.go>
- leaks.go <https://github.com/uber-go/goleak/blob/v1.3.0/leaks.go>
- options.go <https://github.com/uber-go/goleak/blob/v1.3.0/options.go>
- testmain.go <https://github.com/uber-go/goleak/blob/v1.3.0/testmain.go>
- tracestack_new.go <https://github.com/uber-go/goleak/blob/v1.3.0/tracestack_new.go>

##   Directories ¶
    Show internal   Expand all

        internal      stack  Package stack is used for parsing stacks from `runtime.Stack`.

  Package stack is used for parsing stacks from `runtime.Stack`.

  Click to show internal directories.
  Click to hide internal directories.

  Close

     **?** : This menu   **/** : Search site   **f** or **F** : Jump to   **y** or **Y**  : Canonical URL
  Close
