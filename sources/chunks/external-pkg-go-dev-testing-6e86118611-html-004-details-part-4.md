---
source_name: "External Linked Documentation"
source_url: "https://pkg.go.dev/testing"
source_path: "sources/raw/external/pkg-go-dev-testing-6e86118611.html"
license_ref: ""
---

```go
func (b *B) ReportMetric(n float64, unit string)
```

ReportMetric adds "n unit" to the reported benchmark results. If the metric is per-iteration, the caller should divide by b.N, and by convention units should end in "/op". ReportMetric overrides any previously reported value for the same unit. ReportMetric panics if unit is the empty string or if unit contains any whitespace. If unit is a unit normally reported by the benchmark framework itself (such as "allocs/op"), ReportMetric will override that metric. Setting "ns/op" to 0 will suppress that built-in metric.

```go

package main

import (
	"cmp"
	"slices"
	"testing"
)

func main() {
	// This reports a custom benchmark metric relevant to a
	// specific algorithm (in this case, sorting).
	testing.Benchmark(func(b *testing.B) {
		var compares int64
		for b.Loop() {
			s := []int{5, 4, 3, 2, 1}
			slices.SortFunc(s, func(a, b int) int {
				compares++
				return cmp.Compare(a, b)
			})
		}
		// This metric is per-operation, so divide by b.N and
		// report it as a "/op" unit.
		b.ReportMetric(float64(compares)/float64(b.N), "compares/op")
		// This metric is per-time, so divide by b.Elapsed and
		// report it as a "/ns" unit.
		b.ReportMetric(float64(compares)/float64(b.Elapsed().Nanoseconds()), "compares/ns")
	})
}

```

```go
Output:

```

Share Format Run

```go

package main

import (
	"cmp"
	"slices"
	"sync/atomic"
	"testing"
)

func main() {
	// This reports a custom benchmark metric relevant to a
	// specific algorithm (in this case, sorting) in parallel.
	testing.Benchmark(func(b *testing.B) {
		var compares atomic.Int64
		b.RunParallel(func(pb *testing.PB) {
			for pb.Next() {
				s := []int{5, 4, 3, 2, 1}
				slices.SortFunc(s, func(a, b int) int {
					// Because RunParallel runs the function many
					// times in parallel, we must increment the
					// counter atomically to avoid racing writes.
					compares.Add(1)
					return cmp.Compare(a, b)
				})
			}
		})

// NOTE: Report each metric once, after all of the parallel
		// calls have completed.

// This metric is per-operation, so divide by b.N and
		// report it as a "/op" unit.
		b.ReportMetric(float64(compares.Load())/float64(b.N), "compares/op")
		// This metric is per-time, so divide by b.Elapsed and
		// report it as a "/ns" unit.
		b.ReportMetric(float64(compares.Load())/float64(b.Elapsed().Nanoseconds()), "compares/ns")
	})
}

```

```go
Output:

```

Share Format Run

```go
func (b *B) ResetTimer()
```

ResetTimer zeroes the elapsed benchmark time and memory allocation counters and deletes user-reported metrics. It does not affect whether the timer is running.

```go
func (b *B) Run(name string, f func(b *B)) bool
```

Run benchmarks f as a subbenchmark with the given name. It reports whether there were any failures.

A subbenchmark is like any other benchmark. A benchmark that calls Run at least once will not be measured itself and will be called once with N=1.

```go
func (b *B) RunParallel(body func(*PB))
```

RunParallel runs a benchmark in parallel. It creates multiple goroutines and distributes b.N iterations among them. The number of goroutines defaults to GOMAXPROCS. To increase parallelism for non-CPU-bound benchmarks, call B.SetParallelism before RunParallel. RunParallel is usually used with the go test -cpu flag.

The body function will be run in each goroutine. It should set up any goroutine-local state and then iterate until pb.Next returns false. It should not use the B.StartTimer, B.StopTimer, or B.ResetTimer functions, because they have global effect. It should also not call B.Run.

RunParallel reports ns/op values as wall time for the benchmark as a whole, not the sum of wall time or CPU time over each parallel goroutine.

```go

package main

import (
	"bytes"
	"testing"
	"text/template"
)

func main() {
	// Parallel benchmark for text/template.Template.Execute on a single object.
	testing.Benchmark(func(b *testing.B) {
		templ := template.Must(template.New("test").Parse("Hello, {{.}}!"))
		// RunParallel will create GOMAXPROCS goroutines
		// and distribute work among them.
		b.RunParallel(func(pb *testing.PB) {
			// Each goroutine has its own bytes.Buffer.
			var buf bytes.Buffer
			for pb.Next() {
				// The loop body is executed b.N times total across all goroutines.
				buf.Reset()
				templ.Execute(&buf, "World")
			}
		})
	})
}

```

```go
Output:

```

Share Format Run

```go
func (b *B) SetBytes(n int64)
```

SetBytes records the number of bytes processed in a single operation. If this is called, the benchmark will report ns/op and MB/s.

```go
func (b *B) SetParallelism(p int)
```

SetParallelism sets the number of goroutines used by B.RunParallel to p*GOMAXPROCS. There is usually no need to call SetParallelism for CPU-bound benchmarks. If p is less than 1, this call will have no effect.

```go
func (c *B) Setenv(key, value string)
```

Setenv calls os.Setenv and uses Cleanup to restore the environment variable to its original value after the test.

Because Setenv affects the whole process, it cannot be used in parallel tests or tests with parallel ancestors.

```go
func (c *B) Skip(args ...any)
```

Skip is equivalent to Log followed by SkipNow.

```go
func (c *B) SkipNow()
```

SkipNow marks the test as having been skipped and stops its execution by calling runtime.Goexit. If a test fails (see Error, Errorf, Fail) and is then skipped, it is still considered to have failed. Execution will continue at the next test or benchmark. See also FailNow. SkipNow must be called from the goroutine running the test, not from other goroutines created during the test. Calling SkipNow does not stop those other goroutines.

```go
func (c *B) Skipf(format string, args ...any)
```

Skipf is equivalent to Logf followed by SkipNow.

```go
func (c *B) Skipped() bool
```

Skipped reports whether the test was skipped.

```go
func (b *B) StartTimer()
```

StartTimer starts timing a test. This function is called automatically before a benchmark starts, but it can also be used to resume timing after a call to B.StopTimer.

```go
func (b *B) StopTimer()
```

StopTimer stops timing a test. This can be used to pause the timer while performing steps that you don't want to measure.

```go
func (c *B) TempDir() string
```

TempDir returns a temporary directory for the test to use. The directory is automatically removed when the test and all its subtests complete. Each subsequent call to TempDir returns a unique directory; if the directory creation fails, TempDir terminates the test by calling Fatal. If the environment variable GOTMPDIR is set, the temporary directory will be created somewhere beneath it.

```go
type BenchmarkResult struct {
	N         int           // The number of iterations.
	T         time.Duration // The total time taken.
	Bytes     int64         // Bytes processed in one iteration.
	MemAllocs uint64        // The total number of memory allocations.
	MemBytes  uint64        // The total number of bytes allocated.

// Extra records additional metrics reported by ReportMetric.
	Extra map[string]float64
}
```

BenchmarkResult contains the results of a benchmark run.

```go
func Benchmark(f func(b *B)) BenchmarkResult
```

Benchmark benchmarks a single function. It is useful for creating custom benchmarks that do not use the "go test" command.

If f depends on testing flags, then Init must be used to register those flags before calling Benchmark and before calling flag.Parse.

If f calls Run, the result will be an estimate of running all its subbenchmarks that don't call Run in sequence in a single benchmark.

```go
func (r BenchmarkResult) AllocedBytesPerOp() int64
```

AllocedBytesPerOp returns the "B/op" metric, which is calculated as r.MemBytes / r.N.

```go
func (r BenchmarkResult) AllocsPerOp() int64
```

AllocsPerOp returns the "allocs/op" metric, which is calculated as r.MemAllocs / r.N.

```go
func (r BenchmarkResult) MemString() string
```

MemString returns r.AllocedBytesPerOp and r.AllocsPerOp in the same format as 'go test'.

```go
func (r BenchmarkResult) NsPerOp() int64
```

NsPerOp returns the "ns/op" metric.

```go
func (r BenchmarkResult) String() string
```

String returns a summary of the benchmark results. It follows the benchmark result line format from https://golang.org/design/14313-benchmark-format <https://golang.org/design/14313-benchmark-format>, not including the benchmark name. Extra metrics override built-in metrics of the same name. String does not include allocs/op or B/op, since those are reported by BenchmarkResult.MemString.

```go
type Cover struct {
	Mode            string
	Counters        map[string][]uint32
	Blocks          map[string][]CoverBlock
	CoveredPackages string
}
```

Cover records information about test coverage checking. NOTE: This struct is internal to the testing infrastructure and may change. It is not covered (yet) by the Go 1 compatibility guidelines.

```go
type CoverBlock struct {
	Line0 uint32 // Line number for block start.
	Col0  uint16 // Column number for block start.
	Line1 uint32 // Line number for block end.
	Col1  uint16 // Column number for block end.
	Stmts uint16 // Number of statements included in this block.
}
```

CoverBlock records the coverage data for a single basic block. The fields are 1-indexed, as in an editor: The opening line of the file is number 1, for example. Columns are measured in bytes. NOTE: This struct is internal to the testing infrastructure and may change. It is not covered (yet) by the Go 1 compatibility guidelines.

```go
type F struct {
	// contains filtered or unexported fields
}
```

F is a type passed to fuzz tests.

Fuzz tests run generated inputs against a provided fuzz target, which can find and report potential bugs in the code being tested.

A fuzz test runs the seed corpus by default, which includes entries provided by F.Add and entries in the testdata/fuzz/<FuzzTestName> directory. After any necessary setup and calls to F.Add, the fuzz test must then call F.Fuzz to provide the fuzz target. See the testing package documentation for an example, and see the F.Fuzz and F.Add method documentation for details.

*F methods can only be called before F.Fuzz. Once the test is executing the fuzz target, only *T methods can be used. The only *F methods that are allowed in the F.Fuzz function are F.Failed and F.Name.

```go
func (f *F) Add(args ...any)
```

Add will add the arguments to the seed corpus for the fuzz test. This will be a no-op if called after or within the fuzz target, and args must match the arguments for the fuzz target.

```go
func (c *F) ArtifactDir() string
```
