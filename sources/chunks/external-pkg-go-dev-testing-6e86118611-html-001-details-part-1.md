---
source_name: "External Linked Documentation"
source_url: "https://pkg.go.dev/testing"
source_path: "sources/raw/external/pkg-go-dev-testing-6e86118611.html"
license_ref: ""
---

testing package - testing - Go Packages
## Details

-     Valid go.mod <https://cs.opensource.google/go/go/+/go1.26.3:src/go.mod> file
 The Go module system was introduced in Go 1.11 and is the official dependency management solution for Go.

-     Redistributable license
 Redistributable licenses place minimal restrictions on how software can be used, modified, and redistributed.

-     Tagged version
Modules with tagged versions give importers more predictable builds.

-     Stable version
When a project reaches major version v1 it is considered stable.

-  Learn more about best practices

## Repository
   cs.opensource.google/go/go  <https://cs.opensource.google/go/go>

##   Documentation ¶
   Rendered for <https://go.dev/about#build-context>  linux/amd64 windows/amd64 darwin/amd64 js/wasm

Package testing provides support for automated testing of Go packages. It is intended to be used in concert with the "go test" command, which automates execution of any function of the form

```go
func TestXxx(*testing.T)

```

where Xxx does not start with a lowercase letter. The function name serves to identify the test routine.

Within these functions, use T.Error, T.Fail or related methods to signal failure.

To write a new test suite, create a file that contains the TestXxx functions as described here, and give that file a name ending in "_test.go". The file will be excluded from regular package builds but will be included when the "go test" command is run.

The test file can be in the same package as the one being tested, or in a corresponding package with the suffix "_test".

If the test file is in the same package, it may refer to unexported identifiers within the package, as in this example:

```go
package abs

import "testing"

func TestAbs(t *testing.T) {
    got := abs(-1)
    if got != 1 {
        t.Errorf("abs(-1) = %d; want 1", got)
    }
}

```

If the file is in a separate "_test" package, the package being tested must be imported explicitly and only its exported identifiers may be used. This is known as "black box" testing.

```go
package abs_test

import (
	"testing"

"path_to_pkg/abs"
)

func TestAbs(t *testing.T) {
    got := abs.Abs(-1)
    if got != 1 {
        t.Errorf("Abs(-1) = %d; want 1", got)
    }
}

```

For more detail, run go help test <https://pkg.go.dev/cmd/go#hdr-Test_packages> and go help testflag <https://pkg.go.dev/cmd/go#hdr-Testing_flags>.

#### Benchmarks ¶

Functions of the form

```go
func BenchmarkXxx(*testing.B)

```

are considered benchmarks, and are executed by the "go test" command when its -bench flag is provided. Benchmarks are run sequentially.

For a description of the testing flags, see go help testflag <https://pkg.go.dev/cmd/go#hdr-Testing_flags>.

A sample benchmark function looks like this:

```go
func BenchmarkRandInt(b *testing.B) {
    for b.Loop() {
        rand.Int()
    }
}

```

The output

```go
BenchmarkRandInt-8   	68453040	        17.8 ns/op

```

means that the body of the loop ran 68453040 times at a speed of 17.8 ns per loop.

Only the body of the loop is timed, so benchmarks may do expensive setup before calling b.Loop, which will not be counted toward the benchmark measurement:

```go
func BenchmarkBigLen(b *testing.B) {
    big := NewBig()
    for b.Loop() {
        big.Len()
    }
}

```

If a benchmark needs to test performance in a parallel setting, it may use the RunParallel helper function; such benchmarks are intended to be used with the go test -cpu flag:

```go
func BenchmarkTemplateParallel(b *testing.B) {
    templ := template.Must(template.New("test").Parse("Hello, {{.}}!"))
    b.RunParallel(func(pb *testing.PB) {
        var buf bytes.Buffer
        for pb.Next() {
            buf.Reset()
            templ.Execute(&buf, "World")
        }
    })
}

```

A detailed specification of the benchmark results format is given in https://go.dev/design/14313-benchmark-format <https://go.dev/design/14313-benchmark-format>.

There are standard tools for working with benchmark results at golang.org/x/perf/cmd. In particular, golang.org/x/perf/cmd/benchstat performs statistically robust A/B comparisons.

#### b.N-style benchmarks ¶

Prior to the introduction of B.Loop, benchmarks were written in a different style using B.N. For example:

```go
func BenchmarkRandInt(b *testing.B) {
    for range b.N {
        rand.Int()
    }
}

```

In this style of benchmark, the benchmark function must run the target code b.N times. The benchmark function is called multiple times with b.N adjusted until the benchmark function lasts long enough to be timed reliably. This also means any setup done before the loop may be run several times.

If a benchmark needs some expensive setup before running, the timer should be explicitly reset:

```go
func BenchmarkBigLen(b *testing.B) {
    big := NewBig()
    b.ResetTimer()
    for range b.N {
        big.Len()
    }
}

```

New benchmarks should prefer using B.Loop, which is more robust and more efficient.

#### Examples ¶

The package also runs and verifies example code. Example functions may include a concluding line comment that begins with "Output:" and is compared with the standard output of the function when the tests are run. (The comparison ignores leading and trailing space.) These are examples of an example:

```go
func ExampleHello() {
    fmt.Println("hello")
    // Output: hello
}

func ExampleSalutations() {
    fmt.Println("hello, and")
    fmt.Println("goodbye")
    // Output:
    // hello, and
    // goodbye
}

```

The comment prefix "Unordered output:" is like "Output:", but matches any line order:

```go
func ExamplePerm() {
    for _, value := range Perm(5) {
        fmt.Println(value)
    }
    // Unordered output: 4
    // 2
    // 1
    // 3
    // 0
}

```

Example functions without output comments are compiled but not executed.

The naming convention to declare examples for the package, a function F, a type T and method M on type T are:

```go
func Example() { ... }
func ExampleF() { ... }
func ExampleT() { ... }
func ExampleT_M() { ... }

```

Multiple example functions for a package/type/function/method may be provided by appending a distinct suffix to the name. The suffix must start with a lower-case letter.

```go
func Example_suffix() { ... }
func ExampleF_suffix() { ... }
func ExampleT_suffix() { ... }
func ExampleT_M_suffix() { ... }

```

The entire test file is presented as the example when it contains a single example function, at least one other function, type, variable, or constant declaration, and no test or benchmark functions.

#### Fuzzing ¶

'go test' and the testing package support fuzzing, a testing technique where a function is called with randomly generated inputs to find bugs not anticipated by unit tests.

Functions of the form

```go
func FuzzXxx(*testing.F)

```

are considered fuzz tests.

For example:

```go
func FuzzHex(f *testing.F) {
  for _, seed := range [][]byte{{}, {0}, {9}, {0xa}, {0xf}, {1, 2, 3, 4}} {
    f.Add(seed)
  }
  f.Fuzz(func(t *testing.T, in []byte) {
    enc := hex.EncodeToString(in)
    out, err := hex.DecodeString(enc)
    if err != nil {
      t.Fatalf("%v: decode: %v", in, err)
    }
    if !bytes.Equal(in, out) {
      t.Fatalf("%v: not equal after round trip: %v", in, out)
    }
  })
}

```

A fuzz test maintains a seed corpus, or a set of inputs which are run by default, and can seed input generation. Seed inputs may be registered by calling F.Add or by storing files in the directory testdata/fuzz/<Name> (where <Name> is the name of the fuzz test) within the package containing the fuzz test. Seed inputs are optional, but the fuzzing engine may find bugs more efficiently when provided with a set of small seed inputs with good code coverage. These seed inputs can also serve as regression tests for bugs identified through fuzzing.

The function passed to F.Fuzz within the fuzz test is considered the fuzz target. A fuzz target must accept a *T parameter, followed by one or more parameters for random inputs. The types of arguments passed to F.Add must be identical to the types of these parameters. The fuzz target may signal that it's found a problem the same way tests do: by calling T.Fail (or any method that calls it like T.Error or T.Fatal) or by panicking.

When fuzzing is enabled (by setting the -fuzz flag to a regular expression that matches a specific fuzz test), the fuzz target is called with arguments generated by repeatedly making random changes to the seed inputs. On supported platforms, 'go test' compiles the test executable with fuzzing coverage instrumentation. The fuzzing engine uses that instrumentation to find and cache inputs that expand coverage, increasing the likelihood of finding bugs. If the fuzz target fails for a given input, the fuzzing engine writes the inputs that caused the failure to a file in the directory testdata/fuzz/<Name> within the package directory. This file later serves as a seed input. If the file can't be written at that location (for example, because the directory is read-only), the fuzzing engine writes the file to the fuzz cache directory within the build cache instead.

When fuzzing is disabled, the fuzz target is called with the seed inputs registered with F.Add and seed inputs from testdata/fuzz/<Name>. In this mode, the fuzz test acts much like a regular test, with subtests started with F.Fuzz instead of T.Run.

See https://go.dev/doc/fuzz <https://go.dev/doc/fuzz> for documentation about fuzzing.

Tests or benchmarks may be skipped at run time with a call to T.Skip or B.Skip:

```go
func TestTimeConsuming(t *testing.T) {
    if testing.Short() {
        t.Skip("skipping test in short mode.")
    }
    ...
}

```

The T.Skip method can be used in a fuzz target if the input is invalid, but should not be considered a failing input. For example:

```go
func FuzzJSONMarshaling(f *testing.F) {
    f.Fuzz(func(t *testing.T, b []byte) {
        var v interface{}
        if err := json.Unmarshal(b, &v); err != nil {
            t.Skip()
        }
        if _, err := json.Marshal(v); err != nil {
            t.Errorf("Marshal: %v", err)
        }
    })
}

```

#### Subtests and Sub-benchmarks ¶

The T.Run and B.Run methods allow defining subtests and sub-benchmarks, without having to define separate functions for each. This enables uses like table-driven benchmarks and creating hierarchical tests. It also provides a way to share common setup and tear-down code:

```go
func TestFoo(t *testing.T) {
    // <setup code>
    t.Run("A=1", func(t *testing.T) { ... })
    t.Run("A=2", func(t *testing.T) { ... })
    t.Run("B=1", func(t *testing.T) { ... })
    // <tear-down code>
}

```
