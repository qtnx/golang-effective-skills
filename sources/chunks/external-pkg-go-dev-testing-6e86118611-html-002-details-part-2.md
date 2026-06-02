---
source_name: "External Linked Documentation"
source_url: "https://pkg.go.dev/testing"
source_path: "sources/raw/external/pkg-go-dev-testing-6e86118611.html"
license_ref: ""
---

Each subtest and sub-benchmark has a unique name: the combination of the name of the top-level test and the sequence of names passed to Run, separated by slashes, with an optional trailing sequence number for disambiguation.

The argument to the -run, -bench, and -fuzz command-line flags is an unanchored regular expression that matches the test's name. For tests with multiple slash-separated elements, such as subtests, the argument is itself slash-separated, with expressions matching each name element in turn. Because it is unanchored, an empty expression matches any string. For example, using "matching" to mean "whose name contains":

```go
go test -run ''        # Run all tests.
go test -run Foo       # Run top-level tests matching "Foo", such as "TestFooBar".
go test -run Foo/A=    # For top-level tests matching "Foo", run subtests matching "A=".
go test -run /A=1      # For all top-level tests, run subtests matching "A=1".
go test -fuzz FuzzFoo  # Fuzz the target matching "FuzzFoo"

```

The -run argument can also be used to run a specific value in the seed corpus, for debugging. For example:

```go
go test -run=FuzzFoo/9ddb952d9814

```

The -fuzz and -run flags can both be set, in order to fuzz a target but skip the execution of all other tests.

Subtests can also be used to control parallelism. A parent test will only complete once all of its subtests complete. In this example, all tests are run in parallel with each other, and only with each other, regardless of other top-level tests that may be defined:

```go
func TestGroupedParallel(t *testing.T) {
    for _, tc := range tests {
        t.Run(tc.Name, func(t *testing.T) {
            t.Parallel()
            ...
        })
    }
}

```

Run does not return until parallel subtests have completed, providing a way to clean up after a group of parallel tests:

```go
func TestTeardownParallel(t *testing.T) {
    // This Run will not return until the parallel tests finish.
    t.Run("group", func(t *testing.T) {
        t.Run("Test1", parallelTest1)
        t.Run("Test2", parallelTest2)
        t.Run("Test3", parallelTest3)
    })
    // <tear-down code>
}

```

#### Main ¶

It is sometimes necessary for a test or benchmark program to do extra setup or teardown before or after it executes. It is also sometimes necessary to control which code runs on the main thread. To support these and other cases, if a test file contains a function:

```go
func TestMain(m *testing.M)

```

then the generated test will call TestMain(m) instead of running the tests or benchmarks directly. TestMain runs in the main goroutine and can do whatever setup and teardown is necessary around a call to m.Run. m.Run will return an exit code that may be passed to os.Exit. If TestMain returns, the test wrapper will pass the result of m.Run to os.Exit itself.

When TestMain is called, flag.Parse has not been run. If TestMain depends on command-line flags, including those of the testing package, it should call flag.Parse explicitly. Command line flags are always parsed by the time test or benchmark functions run.

A simple implementation of TestMain is:

```go
func TestMain(m *testing.M) {
	// call flag.Parse() here if TestMain uses flags
	m.Run()
}

```

TestMain is a low-level primitive and should not be necessary for casual testing needs, where ordinary test functions suffice.

-  func AllocsPerRun(runs int, f func()) (avg float64)
-  func CoverMode() string
-  func Coverage() float64
-  func Init()
-  func Main(matchString func(pat, str string) (bool, error), tests []InternalTest, ...)
-  func RegisterCover(c Cover)
-  func RunBenchmarks(matchString func(pat, str string) (bool, error), ...)
-  func RunExamples(matchString func(pat, str string) (bool, error), examples []InternalExample) (ok bool)
-  func RunTests(matchString func(pat, str string) (bool, error), tests []InternalTest) (ok bool)
-  func Short() bool
-  func Testing() bool
-  func Verbose() bool
-  type B
-
-  func (c *B) ArtifactDir() string
-  func (c *B) Attr(key, value string)
-  func (c *B) Chdir(dir string)
-  func (c *B) Cleanup(f func())
-  func (c *B) Context() context.Context
-  func (b *B) Elapsed() time.Duration
-  func (c *B) Error(args ...any)
-  func (c *B) Errorf(format string, args ...any)
-  func (c *B) Fail()
-  func (c *B) FailNow()
-  func (c *B) Failed() bool
-  func (c *B) Fatal(args ...any)
-  func (c *B) Fatalf(format string, args ...any)
-  func (c *B) Helper()
-  func (c *B) Log(args ...any)
-  func (c *B) Logf(format string, args ...any)
-  func (b *B) Loop() bool
-  func (c *B) Name() string
-  func (c *B) Output() io.Writer
-  func (b *B) ReportAllocs()
-  func (b *B) ReportMetric(n float64, unit string)
-  func (b *B) ResetTimer()
-  func (b *B) Run(name string, f func(b *B)) bool
-  func (b *B) RunParallel(body func(*PB))
-  func (b *B) SetBytes(n int64)
-  func (b *B) SetParallelism(p int)
-  func (c *B) Setenv(key, value string)
-  func (c *B) Skip(args ...any)
-  func (c *B) SkipNow()
-  func (c *B) Skipf(format string, args ...any)
-  func (c *B) Skipped() bool
-  func (b *B) StartTimer()
-  func (b *B) StopTimer()
-  func (c *B) TempDir() string

-  type BenchmarkResult
-
-  func Benchmark(f func(b *B)) BenchmarkResult

-
-  func (r BenchmarkResult) AllocedBytesPerOp() int64
-  func (r BenchmarkResult) AllocsPerOp() int64
-  func (r BenchmarkResult) MemString() string
-  func (r BenchmarkResult) NsPerOp() int64
-  func (r BenchmarkResult) String() string

-  type Cover
-  type CoverBlock
-  type F
-
-  func (f *F) Add(args ...any)
-  func (c *F) ArtifactDir() string
-  func (c *F) Attr(key, value string)
-  func (c *F) Chdir(dir string)
-  func (c *F) Cleanup(f func())
-  func (c *F) Context() context.Context
-  func (c *F) Error(args ...any)
-  func (c *F) Errorf(format string, args ...any)
-  func (f *F) Fail()
-  func (c *F) FailNow()
-  func (c *F) Failed() bool
-  func (c *F) Fatal(args ...any)
-  func (c *F) Fatalf(format string, args ...any)
-  func (f *F) Fuzz(ff any)
-  func (f *F) Helper()
-  func (c *F) Log(args ...any)
-  func (c *F) Logf(format string, args ...any)
-  func (c *F) Name() string
-  func (c *F) Output() io.Writer
-  func (c *F) Setenv(key, value string)
-  func (c *F) Skip(args ...any)
-  func (c *F) SkipNow()
-  func (c *F) Skipf(format string, args ...any)
-  func (f *F) Skipped() bool
-  func (c *F) TempDir() string

-  type InternalBenchmark
-  type InternalExample
-  type InternalFuzzTarget
-  type InternalTest
-  type M
-
-  func MainStart(deps testDeps, tests []InternalTest, benchmarks []InternalBenchmark, ...) *M

-
-  func (m *M) Run() (code int)

-  type PB
-
-  func (pb *PB) Next() bool

-  type T
-
-  func (c *T) ArtifactDir() string
-  func (c *T) Attr(key, value string)
-  func (t *T) Chdir(dir string)
-  func (c *T) Cleanup(f func())
-  func (c *T) Context() context.Context
-  func (t *T) Deadline() (deadline time.Time, ok bool)
-  func (c *T) Error(args ...any)
-  func (c *T) Errorf(format string, args ...any)
-  func (c *T) Fail()
-  func (c *T) FailNow()
-  func (c *T) Failed() bool
-  func (c *T) Fatal(args ...any)
-  func (c *T) Fatalf(format string, args ...any)
-  func (c *T) Helper()
-  func (c *T) Log(args ...any)
-  func (c *T) Logf(format string, args ...any)
-  func (c *T) Name() string
-  func (c *T) Output() io.Writer
-  func (t *T) Parallel()
-  func (t *T) Run(name string, f func(t *T)) bool
-  func (t *T) Setenv(key, value string)
-  func (c *T) Skip(args ...any)
-  func (c *T) SkipNow()
-  func (c *T) Skipf(format string, args ...any)
-  func (c *T) Skipped() bool
-  func (c *T) TempDir() string

-  type TB

- B.Loop
- B.ReportMetric
- B.ReportMetric (Parallel)
- B.RunParallel

This section is empty.

This section is empty.

```go
func AllocsPerRun(runs int, f func()) (avg float64)
```

AllocsPerRun returns the average number of allocations during calls to f. Although the return value has type float64, it will always be an integral value.

To compute the number of allocations, the function will first be run once as a warm-up. The average number of allocations over the specified number of runs will then be measured and returned.

AllocsPerRun sets runtime.GOMAXPROCS to 1 during its measurement and will restore it before returning.

```go
func CoverMode() string
```

CoverMode reports what the test coverage mode is set to. The values are "set", "count", or "atomic". The return value will be empty if test coverage is not enabled.

```go
func Coverage() float64
```

Coverage reports the current code coverage as a fraction in the range [0, 1]. If coverage is not enabled, Coverage returns 0.

When running a large set of sequential test cases, checking Coverage after each one can be useful for identifying which test cases exercise new code paths. It is not a replacement for the reports generated by 'go test -cover' and 'go tool cover'.

```go
func Init()
```

Init registers testing flags. These flags are automatically registered by the "go test" command before running test functions, so Init is only needed when calling functions such as Benchmark without using "go test".

Init is not safe to call concurrently. It has no effect if it was already called.

```go
func Main(matchString func(pat, str string) (bool, error), tests []InternalTest, benchmarks []InternalBenchmark, examples []InternalExample)
```

Main is an internal function, part of the implementation of the "go test" command. It was exported because it is cross-package and predates "internal" packages. It is no longer used by "go test" but preserved, as much as possible, for other systems that simulate "go test" using Main, but Main sometimes cannot be updated as new functionality is added to the testing package. Systems simulating "go test" should be updated to use MainStart.

```go
func RegisterCover(c Cover)
```
