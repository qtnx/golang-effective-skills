---
source_name: "External Linked Documentation"
source_url: "https://go.dev/cmd/go/"
source_path: "sources/raw/external/go-dev-cmd-go-8fc4a393a0.html"
license_ref: ""
---

# golang.org/x/text/language

-run regexp
    Run only those tests, examples, and fuzz tests matching the regular
    expression. For tests, the regular expression is split by unbracketed
    slash (/) characters into a sequence of regular expressions, and each
    part of a test's identifier must match the corresponding element in
    the sequence, if any. Note that possible parents of matches are
    run too, so that -run=X/Y matches and runs and reports the result
    of all tests matching X, even those without sub-tests matching Y,
    because it must run them to look for those sub-tests.
    See also -skip.

-short
    Tell long-running tests to shorten their run time.
    It is off by default but set during all.bash so that installing
    the Go tree can run a sanity check but not spend time running
    exhaustive tests.

-shuffle off,on,N
    Randomize the execution order of tests and benchmarks.
    It is off by default. If -shuffle is set to on, then it will seed
    the randomizer using the system clock. If -shuffle is set to an
    integer N, then N will be used as the seed value. In both cases,
    the seed will be reported for reproducibility.

-skip regexp
    Run only those tests, examples, fuzz tests, and benchmarks that
    do not match the regular expression. Like for -run and -bench,
    for tests and benchmarks, the regular expression is split by unbracketed
    slash (/) characters into a sequence of regular expressions, and each
    part of a test's identifier must match the corresponding element in
    the sequence, if any.

-timeout d
    If a test binary runs longer than duration d, panic.
    If d is 0, the timeout is disabled.
    The default is 10 minutes (10m).

-v
    Verbose output: log all tests as they are run. Also print all
    text from Log and Logf calls even if the test succeeds.

-vet list
    Configure the invocation of "go vet" during "go test"
    to use the comma-separated list of vet checks.
    If list is empty, "go test" runs "go vet" with a curated list of
    checks believed to be always worth addressing.
    If list is "off", "go test" does not run "go vet" at all.

```

The following flags are also recognized by 'go test' and can be used to profile the tests during execution:

```go
-benchmem
    Print memory allocation statistics for benchmarks.
    Allocations made in C or using C.malloc are not counted.

-blockprofile block.out
    Write a goroutine blocking profile to the specified file
    when all tests are complete.
    Writes test binary as -c would.

-blockprofilerate n
    Control the detail provided in goroutine blocking profiles by
    calling runtime.SetBlockProfileRate with n.
    See 'go doc runtime.SetBlockProfileRate'.
    The profiler aims to sample, on average, one blocking event every
    n nanoseconds the program spends blocked. By default,
    if -test.blockprofile is set without this flag, all blocking events
    are recorded, equivalent to -test.blockprofilerate=1.

-coverprofile cover.out
    Write a coverage profile to the file after all tests have passed.
    Sets -cover.

-cpuprofile cpu.out
    Write a CPU profile to the specified file before exiting.
    Writes test binary as -c would.

-memprofile mem.out
    Write an allocation profile to the file after all tests have passed.
    Writes test binary as -c would.

-memprofilerate n
    Enable more precise (and expensive) memory allocation profiles by
    setting runtime.MemProfileRate. See 'go doc runtime.MemProfileRate'.
    To profile all memory allocations, use -test.memprofilerate=1.

-mutexprofile mutex.out
    Write a mutex contention profile to the specified file
    when all tests are complete.
    Writes test binary as -c would.

-mutexprofilefraction n
    Sample 1 in n stack traces of goroutines holding a
    contended mutex.

-trace trace.out
    Write an execution trace to the specified file before exiting.

```

Each of these flags is also recognized with an optional 'test.' prefix, as in -test.v. When invoking the generated test binary (the result of 'go test -c') directly, however, the prefix is mandatory.

The 'go test' command rewrites or removes recognized flags, as appropriate, both before and after the optional package list, before invoking the test binary.

For instance, the command

```go
go test -v -myflag testdata -cpuprofile=prof.out -x

```

will compile the test binary and then run it as

```go
pkg.test -test.v -myflag testdata -test.cpuprofile=prof.out

```

(The -x flag is removed because it applies only to the go command's execution, not to the test itself.)

The test flags that generate profiles (other than for coverage) also leave the test binary in pkg.test for use when analyzing the profiles.

When 'go test' runs a test binary, it does so from within the corresponding package's source code directory. Depending on the test, it may be necessary to do the same when invoking a generated test binary directly. Because that directory may be located within the module cache, which may be read-only and is verified by checksums, the test must not write to it or any other directory within the module unless explicitly requested by the user (such as with the -fuzz flag, which writes failures to testdata/fuzz).

The command-line package list, if present, must appear before any flag not known to the go test command. Continuing the example above, the package list would have to appear before -myflag, but could appear on either side of -v.

When 'go test' runs in package list mode, 'go test' caches successful package test results to avoid unnecessary repeated running of tests. To disable test caching, use any test flag or argument other than the cacheable flags. The idiomatic way to disable test caching explicitly is to use -count=1.

To keep an argument for a test binary from being interpreted as a known flag or a package name, use -args (see 'go help test') which passes the remainder of the command line through to the test binary uninterpreted and unaltered.

For instance, the command

```go
go test -v -args -x -v

```

will compile the test binary and then run it as

```go
pkg.test -test.v -x -v

```

Similarly,

```go
go test -args math

```

will compile the test binary and then run it as

```go
pkg.test math

```

In the first example, the -x and the second -v are passed through to the test binary unchanged and with no effect on the go command itself. In the second example, the argument math is passed through to the test binary, instead of being interpreted as the package list.

#### Testing functions ¶

The 'go test' command expects to find test, benchmark, and example functions in the "*_test.go" files corresponding to the package under test.

A test function is one named TestXxx (where Xxx does not start with a lower case letter) and should have the signature,

```go
func TestXxx(t *testing.T) { ... }

```

A benchmark function is one named BenchmarkXxx and should have the signature,

```go
func BenchmarkXxx(b *testing.B) { ... }

```

A fuzz test is one named FuzzXxx and should have the signature,

```go
func FuzzXxx(f *testing.F) { ... }

```

An example function is similar to a test function but, instead of using *testing.T to report success or failure, prints output to os.Stdout. If the last comment in the function starts with "Output:" then the output is compared exactly against the comment (see examples below). If the last comment begins with "Unordered output:" then the output is compared to the comment, however the order of the lines is ignored. An example with no such comment is compiled but not executed. An example with no text after "Output:" is compiled, executed, and expected to produce no output.

Godoc displays the body of ExampleXxx to demonstrate the use of the function, constant, or variable Xxx. An example of a method M with receiver type T or *T is named ExampleT_M. There may be multiple examples for a given function, constant, or variable, distinguished by a trailing _xxx, where xxx is a suffix not beginning with an upper case letter.

Here is an example of an example:

```go
func ExamplePrintln() {
	Println("The output of\nthis example.")
	// Output: The output of
	// this example.
}

```

Here is another example where the ordering of the output is ignored:

```go
func ExamplePerm() {
	for _, value := range Perm(4) {
		fmt.Println(value)
	}

// Unordered output: 4
	// 2
	// 1
	// 3
	// 0
}

```

The entire test file is presented as the example when it contains a single example function, at least one other function, type, variable, or constant declaration, and no tests, benchmarks, or fuzz tests.

See the documentation of the testing package for more information.

#### Controlling version control with GOVCS ¶

The 'go get' command can run version control commands like git to download imported code. This functionality is critical to the decentralized Go package ecosystem, in which code can be imported from any server, but it is also a potential security problem, if a malicious server finds a way to cause the invoked version control command to run unintended code.

To balance the functionality and security concerns, the 'go get' command by default will only use git and hg to download code from public servers. But it will use any known version control system (bzr, fossil, git, hg, svn) to download code from private servers, defined as those hosting packages matching the GOPRIVATE variable (see 'go help private'). The rationale behind allowing only Git and Mercurial is that these two systems have had the most attention to issues of being run as clients of untrusted servers. In contrast, Bazaar, Fossil, and Subversion have primarily been used in trusted, authenticated environments and are not as well scrutinized as attack surfaces.
