---
source_name: "External Linked Documentation"
source_url: "https://go.dev/cmd/go/"
source_path: "sources/raw/external/go-dev-cmd-go-8fc4a393a0.html"
license_ref: ""
---

# golang.org/x/text/language

As part of building a test binary, go test runs go vet on the package and its test source files to identify significant problems. If go vet finds any problems, go test reports those and does not run the test binary. Only a high-confidence subset of the default go vet checks are used. That subset is: atomic, bool, buildtags, directive, errorsas, ifaceassert, nilfunc, printf, stringintconv, and tests. You can see the documentation for these and other vet tests via "go doc cmd/vet". To disable the running of go vet, use the -vet=off flag. To run all checks, use the -vet=all flag.

All test output and summary lines are printed to the go command's standard output, even if the test printed them to its own standard error. (The go command's standard error is reserved for printing errors building the tests.)

The go command places $GOROOT/bin at the beginning of $PATH in the test's environment, so that tests that execute 'go' commands use the same 'go' as the parent 'go test' command.

Go test runs in two different modes:

The first, called local directory mode, occurs when go test is invoked with no package arguments (for example, 'go test' or 'go test -v'). In this mode, go test compiles the package sources and tests found in the current directory and then runs the resulting test binary. In this mode, caching (discussed below) is disabled. After the package test finishes, go test prints a summary line showing the test status ('ok' or 'FAIL'), package name, and elapsed time.

The second, called package list mode, occurs when go test is invoked with explicit package arguments (for example 'go test math', 'go test ./...', and even 'go test .'). In this mode, go test compiles and tests each of the packages listed on the command line. If a package test passes, go test prints only the final 'ok' summary line. If a package test fails, go test prints the full test output. If invoked with the -bench or -v flag, go test prints the full output even for passing package tests, in order to display the requested benchmark results or verbose logging. After the package tests for all of the listed packages finish, and their output is printed, go test prints a final 'FAIL' status if any package test has failed.

In package list mode only, go test caches successful package test results to avoid unnecessary repeated running of tests. When the result of a test can be recovered from the cache, go test will redisplay the previous output instead of running the test binary again. When this happens, go test prints '(cached)' in place of the elapsed time in the summary line.

The rule for a match in the cache is that the run involves the same test binary and the flags on the command line come entirely from a restricted set of 'cacheable' test flags, defined as -benchtime, -coverprofile, -cpu, -failfast, -fullpath, -list, -outputdir, -parallel, -run, -short, -skip, -timeout and -v. If a run of go test has any test or non-test flags outside this set, the result is not cached. To disable test caching, use any test flag or argument other than the cacheable flags. The idiomatic way to disable test caching explicitly is to use -count=1. Tests that open files within the package's module or that consult environment variables only match future runs in which the files and environment variables are unchanged. A cached test result is treated as executing in no time at all, so a successful package test result will be cached and reused regardless of -timeout setting.

In addition to the build flags, the flags handled by 'go test' itself are:

```go
-args
    Pass the remainder of the command line (everything after -args)
    to the test binary, uninterpreted and unchanged.
    Because this flag consumes the remainder of the command line,
    the package list (if present) must appear before this flag.

-c
    Compile the test binary to pkg.test in the current directory but do not run it
    (where pkg is the last element of the package's import path).
    The file name or target directory can be changed with the -o flag.

-exec xprog
    Run the test binary using xprog. The behavior is the same as
    in 'go run'. See 'go help run' for details.

-json
    Convert test output to JSON suitable for automated processing.
    See 'go doc test2json' for the encoding details.
    Also emits build output in JSON. See 'go help buildjson'.

-o file
    Save a copy of the test binary to the named file.
    The test still runs (unless -c is specified).
    If file ends in a slash or names an existing directory,
    the test is written to pkg.test in that directory.

```

The test binary also accepts flags that control execution of the test; these flags are also accessible by 'go test'. See 'go help testflag' for details.

For more about build flags, see 'go help build'. For more about specifying packages, see 'go help packages'.

See also: go build, go vet.

#### Run specified go tool ¶

Usage:

```go
go tool [-n] command [args...]

```

Tool runs the go tool command identified by the arguments.

Go ships with a number of builtin tools, and additional tools may be defined in the go.mod of the current module.

With no arguments it prints the list of known tools.

The -n flag causes tool to print the command that would be executed but not execute it.

The -modfile=file.mod build flag causes tool to use an alternate file instead of the go.mod in the module root directory.

Tool also provides the -C, -overlay, and -modcacherw build flags.

For more about build flags, see 'go help build'.

For more about each builtin tool command, see 'go doc cmd/<command>'.

#### Print Go version ¶

Usage:

```go
go version [-m] [-v] [-json] [file ...]

```

Version prints the build information for Go binary files.

Go version reports the Go version used to build each of the named files.

If no files are named on the command line, go version prints its own version information.

If a directory is named, go version walks that directory, recursively, looking for recognized Go binaries and reporting their versions. By default, go version does not report unrecognized files found during a directory scan. The -v flag causes it to report unrecognized files.

The -m flag causes go version to print each file's embedded module version information, when available. In the output, the module information consists of multiple lines following the version line, each indented by a leading tab character.

The -json flag is similar to -m but outputs the runtime/debug.BuildInfo in JSON format. If flag -json is specified without -m, go version reports an error.

See also: go doc runtime/debug.BuildInfo.

#### Report likely mistakes in packages ¶

Usage:

```go
go vet [build flags] [-vettool prog] [vet flags] [packages]

```

Vet runs the Go vet tool (cmd/vet) on the named packages and reports diagnostics.

It supports these flags:

```go
  -c int
	display offending line with this many lines of context (default -1)
  -json
	emit JSON output
  -fix
	instead of printing each diagnostic, apply its first fix (if any)
  -diff
	instead of applying each fix, print the patch as a unified diff;
	exit with a non-zero status if the diff is not empty

```

The -vettool=prog flag selects a different analysis tool with alternative or additional checks. For example, the 'shadow' analyzer can be built and run using these commands:

```go
go install golang.org/x/tools/go/analysis/passes/shadow/cmd/shadow@latest
go vet -vettool=$(which shadow)

```

Alternative vet tools should be built atop golang.org/x/tools/go/analysis/unitchecker, which handles the interaction with go vet.

The default vet tool is 'go tool vet' or cmd/vet. For help on its checkers and their flags, run 'go tool vet help'. For details of a specific checker such as 'printf', see 'go tool vet help printf'.

For more about specifying packages, see 'go help packages'.

The build flags supported by go vet are those that control package resolution and execution, such as -C, -n, -x, -v, -tags, and -toolexec. For more about these flags, see 'go help build'.

See also: go fmt, go fix.

#### Build constraints ¶

A build constraint, also known as a build tag, is a condition under which a file should be included in the package. Build constraints are given by a line comment that begins

```go
//go:build

```

Build constraints can also be used to downgrade the language version used to compile a file.

Constraints may appear in any kind of source file (not just Go), but they must appear near the top of the file, preceded only by blank lines and other comments. These rules mean that in Go files a build constraint must appear before the package clause.

To distinguish build constraints from package documentation, a build constraint should be followed by a blank line.

A build constraint comment is evaluated as an expression containing build tags combined by ||, &&, and ! operators and parentheses. Operators have the same meaning as in Go.

For example, the following build constraint constrains a file to build when the "linux" and "386" constraints are satisfied, or when "darwin" is satisfied and "cgo" is not:

```go
//go:build (linux && 386) || (darwin && !cgo)

```

It is an error for a file to have more than one //go:build line.

During a particular build, the following build tags are satisfied:
