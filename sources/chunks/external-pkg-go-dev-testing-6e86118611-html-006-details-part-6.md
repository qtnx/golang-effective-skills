---
source_name: "External Linked Documentation"
source_url: "https://pkg.go.dev/testing"
source_path: "sources/raw/external/pkg-go-dev-testing-6e86118611.html"
license_ref: ""
---

The other reporting methods, such as the variations of T.Log and T.Error, may be called simultaneously from multiple goroutines.

```go
func (c *T) ArtifactDir() string
```

ArtifactDir returns a directory in which the test should store output files. When the -artifacts flag is provided, this directory is located under the output directory. Otherwise, ArtifactDir returns a temporary directory that is removed after the test completes.

Each test or subtest within each test package has a unique artifact directory. Repeated calls to ArtifactDir in the same test or subtest return the same directory. Subtest outputs are not located under the parent test's output directory.

```go
func (c *T) Attr(key, value string)
```

Attr emits a test attribute associated with this test.

The key must not contain whitespace. The value must not contain newlines or carriage returns.

The meaning of different attribute keys is left up to continuous integration systems and test frameworks.

Test attributes are emitted immediately in the test log, but they are intended to be treated as unordered.

```go
func (t *T) Chdir(dir string)
```

Chdir calls os.Chdir and uses Cleanup to restore the current working directory to its original value after the test. On Unix, it also sets PWD environment variable for the duration of the test.

Because Chdir affects the whole process, it cannot be used in parallel tests or tests with parallel ancestors.

```go
func (c *T) Cleanup(f func())
```

Cleanup registers a function to be called when the test (or subtest) and all its subtests complete. Cleanup functions will be called in last added, first called order.

```go
func (c *T) Context() context.Context
```

Context returns a context that is canceled just before Cleanup-registered functions are called.

Cleanup functions can wait for any resources that shut down on context.Context.Done before the test or benchmark completes.

```go
func (t *T) Deadline() (deadline time.Time, ok bool)
```

Deadline reports the time at which the test binary will have exceeded the timeout specified by the -timeout flag.

The ok result is false if the -timeout flag indicates “no timeout” (0).

```go
func (c *T) Error(args ...any)
```

Error is equivalent to Log followed by Fail.

```go
func (c *T) Errorf(format string, args ...any)
```

Errorf is equivalent to Logf followed by Fail.

```go
func (c *T) Fail()
```

Fail marks the function as having failed but continues execution.

```go
func (c *T) FailNow()
```

FailNow marks the function as having failed and stops its execution by calling runtime.Goexit (which then runs all deferred calls in the current goroutine). Execution will continue at the next test or benchmark. FailNow must be called from the goroutine running the test or benchmark function, not from other goroutines created during the test. Calling FailNow does not stop those other goroutines.

```go
func (c *T) Failed() bool
```

Failed reports whether the function has failed.

```go
func (c *T) Fatal(args ...any)
```

Fatal is equivalent to Log followed by FailNow.

```go
func (c *T) Fatalf(format string, args ...any)
```

Fatalf is equivalent to Logf followed by FailNow.

```go
func (c *T) Helper()
```

Helper marks the calling function as a test helper function. When printing file and line information, that function will be skipped. Helper may be called simultaneously from multiple goroutines.

```go
func (c *T) Log(args ...any)
```

Log formats its arguments using default formatting, analogous to fmt.Println, and records the text in the error log. For tests, the text will be printed only if the test fails or the -test.v flag is set. For benchmarks, the text is always printed to avoid having performance depend on the value of the -test.v flag. It is an error to call Log after a test or benchmark returns.

```go
func (c *T) Logf(format string, args ...any)
```

Logf formats its arguments according to the format, analogous to fmt.Printf, and records the text in the error log. A final newline is added if not provided. For tests, the text will be printed only if the test fails or the -test.v flag is set. For benchmarks, the text is always printed to avoid having performance depend on the value of the -test.v flag. It is an error to call Logf after a test or benchmark returns.

```go
func (c *T) Name() string
```

Name returns the name of the running (sub-) test or benchmark.

The name will include the name of the test along with the names of any nested sub-tests. If two sibling sub-tests have the same name, Name will append a suffix to guarantee the returned name is unique.

```go
func (c *T) Output() io.Writer
```

Output returns a Writer that writes to the same test output stream as TB.Log. The output is indented like TB.Log lines, but Output does not add source locations or newlines. The output is internally line buffered, and a call to TB.Log or the end of the test will implicitly flush the buffer, followed by a newline. After a test function and all its parents return, neither Output nor the Write method may be called.

```go
func (t *T) Parallel()
```

Parallel signals that this test is to be run in parallel with (and only with) other parallel tests. When a test is run multiple times due to use of -test.count or -test.cpu, multiple instances of a single test never run in parallel with each other.

```go
func (t *T) Run(name string, f func(t *T)) bool
```

Run runs f as a subtest of t called name. It runs f in a separate goroutine and blocks until f returns or calls t.Parallel to become a parallel test. Run reports whether f succeeded (or at least did not fail before calling t.Parallel).

Run may be called simultaneously from multiple goroutines, but all such calls must return before the outer test function for t returns.

```go
func (t *T) Setenv(key, value string)
```

Setenv calls os.Setenv(key, value) and uses Cleanup to restore the environment variable to its original value after the test.

Because Setenv affects the whole process, it cannot be used in parallel tests or tests with parallel ancestors.

```go
func (c *T) Skip(args ...any)
```

Skip is equivalent to Log followed by SkipNow.

```go
func (c *T) SkipNow()
```

SkipNow marks the test as having been skipped and stops its execution by calling runtime.Goexit. If a test fails (see Error, Errorf, Fail) and is then skipped, it is still considered to have failed. Execution will continue at the next test or benchmark. See also FailNow. SkipNow must be called from the goroutine running the test, not from other goroutines created during the test. Calling SkipNow does not stop those other goroutines.

```go
func (c *T) Skipf(format string, args ...any)
```

Skipf is equivalent to Logf followed by SkipNow.

```go
func (c *T) Skipped() bool
```

Skipped reports whether the test was skipped.

```go
func (c *T) TempDir() string
```

TempDir returns a temporary directory for the test to use. The directory is automatically removed when the test and all its subtests complete. Each subsequent call to TempDir returns a unique directory; if the directory creation fails, TempDir terminates the test by calling Fatal. If the environment variable GOTMPDIR is set, the temporary directory will be created somewhere beneath it.

```go
type TB interface {
	ArtifactDir() string
	Attr(key, value string)
	Cleanup(func())
	Error(args ...any)
	Errorf(format string, args ...any)
	Fail()
	FailNow()
	Failed() bool
	Fatal(args ...any)
	Fatalf(format string, args ...any)
	Helper()
	Log(args ...any)
	Logf(format string, args ...any)
	Name() string
	Setenv(key, value string)
	Chdir(dir string)
	TempDir() string
	Context() context.Context
	Output() io.Writer
	// contains filtered or unexported methods
}
```

TB is the interface common to T, B, and F.
