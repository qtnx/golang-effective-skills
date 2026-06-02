---
source_name: "External Linked Documentation"
source_url: "https://pkg.go.dev/testing"
source_path: "sources/raw/external/pkg-go-dev-testing-6e86118611.html"
license_ref: ""
---

ArtifactDir returns a directory in which the test should store output files. When the -artifacts flag is provided, this directory is located under the output directory. Otherwise, ArtifactDir returns a temporary directory that is removed after the test completes.

Each test or subtest within each test package has a unique artifact directory. Repeated calls to ArtifactDir in the same test or subtest return the same directory. Subtest outputs are not located under the parent test's output directory.

```go
func (c *F) Attr(key, value string)
```

Attr emits a test attribute associated with this test.

The key must not contain whitespace. The value must not contain newlines or carriage returns.

The meaning of different attribute keys is left up to continuous integration systems and test frameworks.

Test attributes are emitted immediately in the test log, but they are intended to be treated as unordered.

```go
func (c *F) Chdir(dir string)
```

Chdir calls os.Chdir and uses Cleanup to restore the current working directory to its original value after the test. On Unix, it also sets PWD environment variable for the duration of the test.

Because Chdir affects the whole process, it cannot be used in parallel tests or tests with parallel ancestors.

```go
func (c *F) Cleanup(f func())
```

Cleanup registers a function to be called when the test (or subtest) and all its subtests complete. Cleanup functions will be called in last added, first called order.

```go
func (c *F) Context() context.Context
```

Context returns a context that is canceled just before Cleanup-registered functions are called.

Cleanup functions can wait for any resources that shut down on context.Context.Done before the test or benchmark completes.

```go
func (c *F) Error(args ...any)
```

Error is equivalent to Log followed by Fail.

```go
func (c *F) Errorf(format string, args ...any)
```

Errorf is equivalent to Logf followed by Fail.

```go
func (f *F) Fail()
```

Fail marks the function as having failed but continues execution.

```go
func (c *F) FailNow()
```

FailNow marks the function as having failed and stops its execution by calling runtime.Goexit (which then runs all deferred calls in the current goroutine). Execution will continue at the next test or benchmark. FailNow must be called from the goroutine running the test or benchmark function, not from other goroutines created during the test. Calling FailNow does not stop those other goroutines.

```go
func (c *F) Failed() bool
```

Failed reports whether the function has failed.

```go
func (c *F) Fatal(args ...any)
```

Fatal is equivalent to Log followed by FailNow.

```go
func (c *F) Fatalf(format string, args ...any)
```

Fatalf is equivalent to Logf followed by FailNow.

```go
func (f *F) Fuzz(ff any)
```

Fuzz runs the fuzz function, ff, for fuzz testing. If ff fails for a set of arguments, those arguments will be added to the seed corpus.

ff must be a function with no return value whose first argument is *T and whose remaining arguments are the types to be fuzzed. For example:

```go
f.Fuzz(func(t *testing.T, b []byte, i int) { ... })

```

The following types are allowed: []byte, string, bool, byte, rune, float32, float64, int, int8, int16, int32, int64, uint, uint8, uint16, uint32, uint64. More types may be supported in the future.

ff must not call any *F methods, e.g. F.Log, F.Error, F.Skip. Use the corresponding *T method instead. The only *F methods that are allowed in the F.Fuzz function are F.Failed and F.Name.

This function should be fast and deterministic, and its behavior should not depend on shared state. No mutable input arguments, or pointers to them, should be retained between executions of the fuzz function, as the memory backing them may be mutated during a subsequent invocation. ff must not modify the underlying data of the arguments provided by the fuzzing engine.

When fuzzing, F.Fuzz does not return until a problem is found, time runs out (set with -fuzztime), or the test process is interrupted by a signal. F.Fuzz should be called exactly once, unless F.Skip or F.Fail is called beforehand.

```go
func (f *F) Helper()
```

Helper marks the calling function as a test helper function. When printing file and line information, that function will be skipped. Helper may be called simultaneously from multiple goroutines.

```go
func (c *F) Log(args ...any)
```

Log formats its arguments using default formatting, analogous to fmt.Println, and records the text in the error log. For tests, the text will be printed only if the test fails or the -test.v flag is set. For benchmarks, the text is always printed to avoid having performance depend on the value of the -test.v flag. It is an error to call Log after a test or benchmark returns.

```go
func (c *F) Logf(format string, args ...any)
```

Logf formats its arguments according to the format, analogous to fmt.Printf, and records the text in the error log. A final newline is added if not provided. For tests, the text will be printed only if the test fails or the -test.v flag is set. For benchmarks, the text is always printed to avoid having performance depend on the value of the -test.v flag. It is an error to call Logf after a test or benchmark returns.

```go
func (c *F) Name() string
```

Name returns the name of the running (sub-) test or benchmark.

The name will include the name of the test along with the names of any nested sub-tests. If two sibling sub-tests have the same name, Name will append a suffix to guarantee the returned name is unique.

```go
func (c *F) Output() io.Writer
```

Output returns a Writer that writes to the same test output stream as TB.Log. The output is indented like TB.Log lines, but Output does not add source locations or newlines. The output is internally line buffered, and a call to TB.Log or the end of the test will implicitly flush the buffer, followed by a newline. After a test function and all its parents return, neither Output nor the Write method may be called.

```go
func (c *F) Setenv(key, value string)
```

Setenv calls os.Setenv and uses Cleanup to restore the environment variable to its original value after the test.

Because Setenv affects the whole process, it cannot be used in parallel tests or tests with parallel ancestors.

```go
func (c *F) Skip(args ...any)
```

Skip is equivalent to Log followed by SkipNow.

```go
func (c *F) SkipNow()
```

SkipNow marks the test as having been skipped and stops its execution by calling runtime.Goexit. If a test fails (see Error, Errorf, Fail) and is then skipped, it is still considered to have failed. Execution will continue at the next test or benchmark. See also FailNow. SkipNow must be called from the goroutine running the test, not from other goroutines created during the test. Calling SkipNow does not stop those other goroutines.

```go
func (c *F) Skipf(format string, args ...any)
```

Skipf is equivalent to Logf followed by SkipNow.

```go
func (f *F) Skipped() bool
```

Skipped reports whether the test was skipped.

```go
func (c *F) TempDir() string
```

TempDir returns a temporary directory for the test to use. The directory is automatically removed when the test and all its subtests complete. Each subsequent call to TempDir returns a unique directory; if the directory creation fails, TempDir terminates the test by calling Fatal. If the environment variable GOTMPDIR is set, the temporary directory will be created somewhere beneath it.

```go
type InternalBenchmark struct {
	Name string
	F    func(b *B)
}
```

InternalBenchmark is an internal type but exported because it is cross-package; it is part of the implementation of the "go test" command.

```go
type InternalExample struct {
	Name      string
	F         func()
	Output    string
	Unordered bool
}
```

```go
type InternalFuzzTarget struct {
	Name string
	Fn   func(f *F)
}
```

InternalFuzzTarget is an internal type but exported because it is cross-package; it is part of the implementation of the "go test" command.

```go
type InternalTest struct {
	Name string
	F    func(*T)
}
```

InternalTest is an internal type but exported because it is cross-package; it is part of the implementation of the "go test" command.

```go
type M struct {
	// contains filtered or unexported fields
}
```

M is a type passed to a TestMain function to run the actual tests.

```go
func MainStart(deps testDeps, tests []InternalTest, benchmarks []InternalBenchmark, fuzzTargets []InternalFuzzTarget, examples []InternalExample) *M
```

MainStart is meant for use by tests generated by 'go test'. It is not meant to be called directly and is not subject to the Go 1 compatibility document. It may change signature from release to release.

```go
func (m *M) Run() (code int)
```

Run runs the tests. It returns an exit code to pass to os.Exit. The exit code is zero when all tests pass, and non-zero for any kind of failure. For machine readable test results, parse the output of 'go test -json'.

```go
type PB struct {
	// contains filtered or unexported fields
}
```

A PB is used by RunParallel for running parallel benchmarks.

```go
func (pb *PB) Next() bool
```

Next reports whether there are more iterations to execute.

```go
type T struct {
	// contains filtered or unexported fields
}
```

T is a type passed to Test functions to manage test state and support formatted test logs.

A test ends when its Test function returns or calls any of the methods T.FailNow, T.Fatal, T.Fatalf, T.SkipNow, T.Skip, or T.Skipf. Those methods, as well as the T.Parallel method, must be called only from the goroutine running the Test function.
