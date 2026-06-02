---
source_name: "External Linked Documentation"
source_url: "https://pkg.go.dev/testing"
source_path: "sources/raw/external/pkg-go-dev-testing-6e86118611.html"
license_ref: ""
---

RegisterCover records the coverage data accumulators for the tests. NOTE: This function is internal to the testing infrastructure and may change. It is not covered (yet) by the Go 1 compatibility guidelines.

```go
func RunBenchmarks(matchString func(pat, str string) (bool, error), benchmarks []InternalBenchmark)
```

RunBenchmarks is an internal function but exported because it is cross-package; it is part of the implementation of the "go test" command.

```go
func RunExamples(matchString func(pat, str string) (bool, error), examples []InternalExample) (ok bool)
```

RunExamples is an internal function but exported because it is cross-package; it is part of the implementation of the "go test" command.

```go
func RunTests(matchString func(pat, str string) (bool, error), tests []InternalTest) (ok bool)
```

RunTests is an internal function but exported because it is cross-package; it is part of the implementation of the "go test" command.

```go
func Short() bool
```

Short reports whether the -test.short flag is set.

```go
func Testing() bool
```

Testing reports whether the current code is being run in a test. This will report true in programs created by "go test", false in programs created by "go build".

```go
func Verbose() bool
```

Verbose reports whether the -test.v flag is set.

```go
type B struct {
	N int
	// contains filtered or unexported fields
}
```

B is a type passed to Benchmark functions to manage benchmark timing and control the number of iterations.

A benchmark ends when its Benchmark function returns or calls any of the methods B.FailNow, B.Fatal, B.Fatalf, B.SkipNow, B.Skip, or B.Skipf. Those methods must be called only from the goroutine running the Benchmark function. The other reporting methods, such as the variations of B.Log and B.Error, may be called simultaneously from multiple goroutines.

Like in tests, benchmark logs are accumulated during execution and dumped to standard output when done. Unlike in tests, benchmark logs are always printed, so as not to hide output whose existence may be affecting benchmark results.

```go
func (c *B) ArtifactDir() string
```

ArtifactDir returns a directory in which the test should store output files. When the -artifacts flag is provided, this directory is located under the output directory. Otherwise, ArtifactDir returns a temporary directory that is removed after the test completes.

Each test or subtest within each test package has a unique artifact directory. Repeated calls to ArtifactDir in the same test or subtest return the same directory. Subtest outputs are not located under the parent test's output directory.

```go
func (c *B) Attr(key, value string)
```

Attr emits a test attribute associated with this test.

The key must not contain whitespace. The value must not contain newlines or carriage returns.

The meaning of different attribute keys is left up to continuous integration systems and test frameworks.

Test attributes are emitted immediately in the test log, but they are intended to be treated as unordered.

```go
func (c *B) Chdir(dir string)
```

Chdir calls os.Chdir and uses Cleanup to restore the current working directory to its original value after the test. On Unix, it also sets PWD environment variable for the duration of the test.

Because Chdir affects the whole process, it cannot be used in parallel tests or tests with parallel ancestors.

```go
func (c *B) Cleanup(f func())
```

Cleanup registers a function to be called when the test (or subtest) and all its subtests complete. Cleanup functions will be called in last added, first called order.

```go
func (c *B) Context() context.Context
```

Context returns a context that is canceled just before Cleanup-registered functions are called.

Cleanup functions can wait for any resources that shut down on context.Context.Done before the test or benchmark completes.

```go
func (b *B) Elapsed() time.Duration
```

Elapsed returns the measured elapsed time of the benchmark. The duration reported by Elapsed matches the one measured by B.StartTimer, B.StopTimer, and B.ResetTimer.

```go
func (c *B) Error(args ...any)
```

Error is equivalent to Log followed by Fail.

```go
func (c *B) Errorf(format string, args ...any)
```

Errorf is equivalent to Logf followed by Fail.

```go
func (c *B) Fail()
```

Fail marks the function as having failed but continues execution.

```go
func (c *B) FailNow()
```

FailNow marks the function as having failed and stops its execution by calling runtime.Goexit (which then runs all deferred calls in the current goroutine). Execution will continue at the next test or benchmark. FailNow must be called from the goroutine running the test or benchmark function, not from other goroutines created during the test. Calling FailNow does not stop those other goroutines.

```go
func (c *B) Failed() bool
```

Failed reports whether the function has failed.

```go
func (c *B) Fatal(args ...any)
```

Fatal is equivalent to Log followed by FailNow.

```go
func (c *B) Fatalf(format string, args ...any)
```

Fatalf is equivalent to Logf followed by FailNow.

```go
func (c *B) Helper()
```

Helper marks the calling function as a test helper function. When printing file and line information, that function will be skipped. Helper may be called simultaneously from multiple goroutines.

```go
func (c *B) Log(args ...any)
```

Log formats its arguments using default formatting, analogous to fmt.Println, and records the text in the error log. For tests, the text will be printed only if the test fails or the -test.v flag is set. For benchmarks, the text is always printed to avoid having performance depend on the value of the -test.v flag. It is an error to call Log after a test or benchmark returns.

```go
func (c *B) Logf(format string, args ...any)
```

Logf formats its arguments according to the format, analogous to fmt.Printf, and records the text in the error log. A final newline is added if not provided. For tests, the text will be printed only if the test fails or the -test.v flag is set. For benchmarks, the text is always printed to avoid having performance depend on the value of the -test.v flag. It is an error to call Logf after a test or benchmark returns.

```go
func (b *B) Loop() bool
```

Loop returns true as long as the benchmark should continue running.

A typical benchmark is structured like:

```go
func Benchmark(b *testing.B) {
	... setup ...
	for b.Loop() {
		... code to measure ...
	}
	... cleanup ...
}

```

Loop resets the benchmark timer the first time it is called in a benchmark, so any setup performed prior to starting the benchmark loop does not count toward the benchmark measurement. Likewise, when it returns false, it stops the timer so cleanup code is not measured.

Within the body of a "for b.Loop() { ... }" loop, arguments to and results from function calls and assigned variables within the loop are kept alive, preventing the compiler from fully optimizing away the loop body. Currently, this is implemented as a compiler transformation that wraps such variables with a runtime.KeepAlive intrinsic call. This applies only to statements syntactically between the curly braces of the loop, and the loop condition must be written exactly as "b.Loop()".

After Loop returns false, b.N contains the total number of iterations that ran, so the benchmark may use b.N to compute other average metrics.

Prior to the introduction of Loop, benchmarks were expected to contain an explicit loop from 0 to b.N. Benchmarks should either use Loop or contain a loop to b.N, but not both. Loop offers more automatic management of the benchmark timer, and runs each benchmark function only once per measurement, whereas b.N-based benchmarks must run the benchmark function (and any associated setup and cleanup) several times.

```go

package main

import (
	"math/rand/v2"
	"testing"
)

// ExBenchmark shows how to use b.Loop in a benchmark.
//
// (If this were a real benchmark, not an example, this would be named
// BenchmarkSomething.)
func ExBenchmark(b *testing.B) {
	// Generate a large random slice to use as an input.
	// Since this is done before the first call to b.Loop(),
	// it doesn't count toward the benchmark time.
	input := make([]int, 128<<10)
	for i := range input {
		input[i] = rand.Int()
	}

// Perform the benchmark.
	for b.Loop() {
		// Normally, the compiler would be allowed to optimize away the call
		// to sum because it has no side effects and the result isn't used.
		// However, inside a b.Loop loop, the compiler ensures function calls
		// aren't optimized away.
		sum(input)
	}

// Outside the loop, the timer is stopped, so we could perform
	// cleanup if necessary without affecting the result.
}

func sum(data []int) int {
	total := 0
	for _, value := range data {
		total += value
	}
	return total
}

func main() {
	testing.Benchmark(ExBenchmark)
}

```

```go
Output:

```

Share Format Run

```go
func (c *B) Name() string
```

Name returns the name of the running (sub-) test or benchmark.

The name will include the name of the test along with the names of any nested sub-tests. If two sibling sub-tests have the same name, Name will append a suffix to guarantee the returned name is unique.

```go
func (c *B) Output() io.Writer
```

Output returns a Writer that writes to the same test output stream as TB.Log. The output is indented like TB.Log lines, but Output does not add source locations or newlines. The output is internally line buffered, and a call to TB.Log or the end of the test will implicitly flush the buffer, followed by a newline. After a test function and all its parents return, neither Output nor the Write method may be called.

```go
func (b *B) ReportAllocs()
```

ReportAllocs enables malloc statistics for this benchmark. It is equivalent to setting -test.benchmem, but it only affects the benchmark function that calls ReportAllocs.
