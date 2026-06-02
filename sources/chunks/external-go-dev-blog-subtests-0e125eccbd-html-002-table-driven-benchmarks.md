---
source_name: "External Linked Documentation"
source_url: "https://go.dev/blog/subtests"
source_path: "sources/raw/external/go-dev-blog-subtests-0e125eccbd.html"
license_ref: ""
---

# The Go Blog

## Table-driven benchmarks

Before Go 1.7 it was not possible to use the same table-driven approach for benchmarks. A benchmark tests the performance of an entire function, so iterating over benchmarks would just measure all of them as a single benchmark.

A common workaround was to define separate top-level benchmarks that each call a common function with different parameters. For instance, before 1.7 the `strconv` package’s benchmarks for `AppendFloat` looked something like this:

```go
func benchmarkAppendFloat(b *testing.B, f float64, fmt byte, prec, bitSize int) {
    dst := make([]byte, 30)
    b.ResetTimer() // Overkill here, but for illustrative purposes.
    for i := 0; i < b.N; i++ {
        AppendFloat(dst[:0], f, fmt, prec, bitSize)
    }
}

func BenchmarkAppendFloatDecimal(b *testing.B) { benchmarkAppendFloat(b, 33909, 'g', -1, 64) }
func BenchmarkAppendFloat(b *testing.B)        { benchmarkAppendFloat(b, 339.7784, 'g', -1, 64) }
func BenchmarkAppendFloatExp(b *testing.B)     { benchmarkAppendFloat(b, -5.09e75, 'g', -1, 64) }
func BenchmarkAppendFloatNegExp(b *testing.B)  { benchmarkAppendFloat(b, -5.11e-95, 'g', -1, 64) }
func BenchmarkAppendFloatBig(b *testing.B)     { benchmarkAppendFloat(b, 123456789123456789123456789, 'g', -1, 64) }
...

```

Using the `Run` method available in Go 1.7, the same set of benchmarks is now expressed as a single top-level benchmark:

```go
func BenchmarkAppendFloat(b *testing.B) {
    benchmarks := []struct{
        name    string
        float   float64
        fmt     byte
        prec    int
        bitSize int
    }{
        {"Decimal", 33909, 'g', -1, 64},
        {"Float", 339.7784, 'g', -1, 64},
        {"Exp", -5.09e75, 'g', -1, 64},
        {"NegExp", -5.11e-95, 'g', -1, 64},
        {"Big", 123456789123456789123456789, 'g', -1, 64},
        ...
    }
    dst := make([]byte, 30)
    for _, bm := range benchmarks {
        b.Run(bm.name, func(b *testing.B) {
            for i := 0; i < b.N; i++ {
                AppendFloat(dst[:0], bm.float, bm.fmt, bm.prec, bm.bitSize)
            }
        })
    }
}

```

Each invocation of the `Run` method creates a separate benchmark. An enclosing benchmark function that calls a `Run` method is only run once and is not measured.

The new code has more lines of code, but is more maintainable, more readable, and consistent with the table-driven approach commonly used for testing. Moreover, common setup code is now shared between runs while eliminating the need to reset the timer.
