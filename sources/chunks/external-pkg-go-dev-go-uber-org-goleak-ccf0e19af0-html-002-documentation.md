---
source_name: "External Linked Documentation"
source_url: "https://pkg.go.dev/go.uber.org/goleak"
source_path: "sources/raw/external/pkg-go-dev-go-uber-org-goleak-ccf0e19af0.html"
license_ref: ""
---

# Create a test binary which will be used to run each test individually

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

# Create a test binary which will be used to run each test individually

##   Source Files ¶
 View all Source files <https://github.com/uber-go/goleak/tree/v1.3.0>

- doc.go <https://github.com/uber-go/goleak/blob/v1.3.0/doc.go>
- leaks.go <https://github.com/uber-go/goleak/blob/v1.3.0/leaks.go>
- options.go <https://github.com/uber-go/goleak/blob/v1.3.0/options.go>
- testmain.go <https://github.com/uber-go/goleak/blob/v1.3.0/testmain.go>
- tracestack_new.go <https://github.com/uber-go/goleak/blob/v1.3.0/tracestack_new.go>

# Create a test binary which will be used to run each test individually

##   Directories ¶
    Show internal   Expand all

        internal      stack  Package stack is used for parsing stacks from `runtime.Stack`.

  Package stack is used for parsing stacks from `runtime.Stack`.

  Click to show internal directories.
  Click to hide internal directories.

  Close

     **?** : This menu   **/** : Search site   **f** or **F** : Jump to   **y** or **Y**  : Canonical URL
  Close
