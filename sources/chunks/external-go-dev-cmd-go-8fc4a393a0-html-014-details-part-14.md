---
source_name: "External Linked Documentation"
source_url: "https://go.dev/cmd/go/"
source_path: "sources/raw/external/go-dev-cmd-go-8fc4a393a0.html"
license_ref: ""
---

# golang.org/x/text/language

- "cmd" expands to the Go repository's commands and their internal libraries.

- "tool" expands to the tools defined in the current module's go.mod file.

Package names match against fully-qualified import paths or patterns that match against any number of import paths. For instance, "fmt" refers to the standard library's package fmt, but "http" alone for package http would not match the import path "net/http" from the standard library. Instead, the complete import path "net/http" must be used.

Import paths beginning with "cmd/" only match source code in the Go repository.

An import path is a pattern if it includes one or more "..." wildcards, each of which can match any string, including the empty string and strings containing slashes. Such a pattern expands to all package directories found in the GOPATH trees with names matching the patterns.

To make common patterns more convenient, there are two special cases. First, /... at the end of the pattern can match an empty string, so that net/... matches both net and packages in its subdirectories, like net/http. Second, any slash-separated pattern element containing a wildcard never participates in a match of the "vendor" element in the path of a vendored package, so that ./... does not match packages in subdirectories of ./vendor or ./mycode/vendor, but ./vendor/... and ./mycode/vendor/... do. Note, however, that a directory named vendor that itself contains code is not a vendored package: cmd/vendor would be a command named vendor, and the pattern cmd/... matches it. See golang.org/s/go15vendor for more about vendoring.

An import path can also name a package to be downloaded from a remote repository. Run 'go help importpath' for details.

Every package in a program must have a unique import path. By convention, this is arranged by starting each path with a unique prefix that belongs to you. For example, paths used internally at Google all begin with 'google', and paths denoting remote repositories begin with the path to the code, such as 'github.com/user/repo'. Package patterns should include this prefix. For instance, a package called 'http' residing under 'github.com/user/repo', would be addressed with the fully-qualified pattern: 'github.com/user/repo/http'.

Packages in a program need not have unique package names, but there are two reserved package names with special meaning. The name main indicates a command, not a library. Commands are built into binaries and cannot be imported. The name documentation indicates documentation for a non-Go program in the directory. Files in package documentation are ignored by the go command.

As a special case, if the package list is a list of .go files from a single directory, the command is applied to a single synthesized package made up of exactly those files, ignoring any build constraints in those files and ignoring any other files in the directory.

Directory and file names that begin with "." or "_" are ignored by the go tool, as are directories named "testdata".

#### Configuration for downloading non-public code ¶

The go command defaults to downloading modules from the public Go module mirror at proxy.golang.org. It also defaults to validating downloaded modules, regardless of source, against the public Go checksum database at sum.golang.org. These defaults work well for publicly available source code.

The GOPRIVATE environment variable controls which modules the go command considers to be private (not available publicly) and should therefore not use the proxy or checksum database. The variable is a comma-separated list of glob patterns (in the syntax of Go's path.Match) of module path prefixes. For example,

```go
GOPRIVATE=*.corp.example.com,rsc.io/private

```

causes the go command to treat as private any module with a path prefix matching either pattern, including git.corp.example.com/xyzzy, rsc.io/private, and rsc.io/private/quux.

For fine-grained control over module download and validation, the GONOPROXY and GONOSUMDB environment variables accept the same kind of glob list and override GOPRIVATE for the specific decision of whether to use the proxy and checksum database, respectively.

For example, if a company ran a module proxy serving private modules, users would configure go using:

```go
GOPRIVATE=*.corp.example.com
GOPROXY=proxy.example.com
GONOPROXY=none

```

The GOPRIVATE variable is also used to define the "public" and "private" patterns for the GOVCS variable; see 'go help vcs'. For that usage, GOPRIVATE applies even in GOPATH mode. In that case, it matches import paths instead of module paths.

The 'go env -w' command (see 'go help env') can be used to set these variables for future go command invocations.

For more details, see https://golang.org/ref/mod#private-modules <https://golang.org/ref/mod#private-modules>.

#### Testing flags ¶

The 'go test' command takes both flags that apply to 'go test' itself and flags that apply to the resulting test binary.

Several of the flags control profiling and write an execution profile suitable for "go tool pprof"; run "go tool pprof -h" for more information. The -sample_index=alloc_space, -sample_index=alloc_objects, and -show_bytes options of pprof control how the information is presented.

The following flags are recognized by the 'go test' command and control the execution of any test:

```go
-artifacts
    Save test artifacts in the directory specified by -outputdir.
    See 'go doc testing.T.ArtifactDir'.

-bench regexp
    Run only those benchmarks matching a regular expression.
    By default, no benchmarks are run.
    To run all benchmarks, use '-bench .' or '-bench=.'.
    The regular expression is split by unbracketed slash (/)
    characters into a sequence of regular expressions, and each
    part of a benchmark's identifier must match the corresponding
    element in the sequence, if any. Possible parents of matches
    are run with b.N=1 to identify sub-benchmarks. For example,
    given -bench=X/Y, top-level benchmarks matching X are run
    with b.N=1 to find any sub-benchmarks matching Y, which are
    then run in full.

-benchtime t
    Run enough iterations of each benchmark to take t, specified
    as a time.Duration (for example, -benchtime 1h30s).
    The default is 1 second (1s).
    The special syntax Nx means to run the benchmark N times
    (for example, -benchtime 100x).

-count n
    Run each test, benchmark, and fuzz seed n times (default 1).
    If -cpu is set, run n times for each GOMAXPROCS value.
    Examples are always run once. -count does not apply to
    fuzz tests matched by -fuzz.

-cover
    Enable coverage analysis.
    Note that because coverage works by annotating the source
    code before compilation, compilation and test failures with
    coverage enabled may report line numbers that don't correspond
    to the original sources.

-covermode set,count,atomic
    Set the mode for coverage analysis for the package[s]
    being tested. The default is "set" unless -race is enabled,
    in which case it is "atomic".
    The values:
	set: bool: does this statement run?
	count: int: how many times does this statement run?
	atomic: int: count, but correct in multithreaded tests;
		significantly more expensive.
    Sets -cover.

-coverpkg pattern1,pattern2,pattern3
    Apply coverage analysis in each test to packages whose import paths
    match the patterns. The default is for each test to analyze only
    the package being tested. See 'go help packages' for a description
    of package patterns. Sets -cover.

-cpu 1,2,4
    Specify a list of GOMAXPROCS values for which the tests, benchmarks or
    fuzz tests should be executed. The default is the current value
    of GOMAXPROCS. -cpu does not apply to fuzz tests matched by -fuzz.

-failfast
    Do not start new tests after the first test failure.

-fullpath
    Show full file names in the error messages.

-fuzz regexp
    Run the fuzz test matching the regular expression. When specified,
    the command line argument must match exactly one package within the
    main module, and regexp must match exactly one fuzz test within
    that package. Fuzzing will occur after tests, benchmarks, seed corpora
    of other fuzz tests, and examples have completed. See the Fuzzing
    section of the testing package documentation for details.

-fuzztime t
    Run enough iterations of the fuzz target during fuzzing to take t,
    specified as a time.Duration (for example, -fuzztime 1h30s).
	The default is to run forever.
    The special syntax Nx means to run the fuzz target N times
    (for example, -fuzztime 1000x).

-fuzzminimizetime t
    Run enough iterations of the fuzz target during each minimization
    attempt to take t, as specified as a time.Duration (for example,
    -fuzzminimizetime 30s).
	The default is 60s.
    The special syntax Nx means to run the fuzz target N times
    (for example, -fuzzminimizetime 100x).

-json
    Log verbose output and test results in JSON. This presents the
    same information as the -v flag in a machine-readable format.

-list regexp
    List tests, benchmarks, fuzz tests, or examples matching the regular
    expression. No tests, benchmarks, fuzz tests, or examples will be run.
    This will only list top-level tests. No subtest or subbenchmarks will be
    shown.

-outputdir directory
    Place output files from profiling and test artifacts in the
    specified directory, by default the directory in which "go test" is running.

-parallel n
    Allow parallel execution of test functions that call t.Parallel, and
    fuzz targets that call t.Parallel when running the seed corpus.
    The value of this flag is the maximum number of tests to run
    simultaneously.
    While fuzzing, the value of this flag is the maximum number of
    subprocesses that may call the fuzz function simultaneously, regardless of
    whether T.Parallel is called.
    By default, -parallel is set to the value of GOMAXPROCS.
    Setting -parallel to values higher than GOMAXPROCS may cause degraded
    performance due to CPU contention, especially when fuzzing.
    Note that -parallel only applies within a single test binary.
    The 'go test' command may run tests for different packages
    in parallel as well, according to the setting of the -p flag
    (see 'go help build').
