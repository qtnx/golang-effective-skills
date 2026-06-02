---
source_name: "External Linked Documentation"
source_url: "https://go.dev/cmd/go/"
source_path: "sources/raw/external/go-dev-cmd-go-8fc4a393a0.html"
license_ref: ""
---

# golang.org/x/text/language

```go
$GOARCH
	The execution architecture (arm, amd64, etc.)
$GOOS
	The execution operating system (linux, windows, etc.)
$GOFILE
	The base name of the file.
$GOLINE
	The line number of the directive in the source file.
$GOPACKAGE
	The name of the package of the file containing the directive.
$GOROOT
	The GOROOT directory for the 'go' command that invoked the
	generator, containing the Go toolchain and standard library.
$DOLLAR
	A dollar sign.
$PATH
	The $PATH of the parent process, with $GOROOT/bin
	placed at the beginning. This causes generators
	that execute 'go' commands to use the same 'go'
	as the parent 'go generate' command.

```

Other than variable substitution and quoted-string evaluation, no special processing such as "globbing" is performed on the command line.

As a last step before running the command, any invocations of any environment variables with alphanumeric names, such as $GOFILE or $HOME, are expanded throughout the command line. The syntax for variable expansion is $NAME on all operating systems. Due to the order of evaluation, variables are expanded even inside quoted strings. If the variable NAME is not set, $NAME expands to the empty string.

A directive of the form,

```go
//go:generate -command xxx args...

```

specifies, for the remainder of this source file only, that the string xxx represents the command identified by the arguments. This can be used to create aliases or to handle multiword generators. For example,

```go
//go:generate -command foo go tool foo

```

specifies that the command "foo" represents the generator "go tool foo".

Generate processes packages in the order given on the command line, one at a time. If the command line lists .go files from a single directory, they are treated as a single package. Within a package, generate processes the source files in a package in file name order, one at a time. Within a source file, generate runs generators in the order they appear in the file, one at a time. The go generate tool also sets the build tag "generate" so that files may be examined by go generate but ignored during build.

For packages with invalid code, generate processes only source files with a valid package clause.

If any generator returns an error exit status, "go generate" skips all further processing for that package.

The generator is run in the package's source directory.

Go generate accepts two specific flags:

```go
-run=""
	if non-empty, specifies a regular expression to select
	directives whose full original source text (excluding
	any trailing spaces and final newline) matches the
	expression.

-skip=""
	if non-empty, specifies a regular expression to suppress
	directives whose full original source text (excluding
	any trailing spaces and final newline) matches the
	expression. If a directive matches both the -run and
	the -skip arguments, it is skipped.

```

It also accepts the standard build flags including -v, -n, and -x. The -v flag prints the names of packages and files as they are processed. The -n flag prints commands that would be executed. The -x flag prints commands as they are executed.

For more about build flags, see 'go help build'.

For more about specifying packages, see 'go help packages'.

#### Add dependencies to current module and install them ¶

Usage:

```go
go get [-t] [-u] [-tool] [build flags] [packages]

```

Get resolves its command-line arguments to packages at specific module versions, updates go.mod to require those versions, and downloads source code into the module cache.

To add a dependency for a package or upgrade it to its latest version:

```go
go get example.com/pkg

```

To upgrade or downgrade a package to a specific version:

```go
go get example.com/pkg@v1.2.3

```

To remove a dependency on a module and downgrade modules that require it:

```go
go get example.com/mod@none

```

To upgrade the minimum required Go version to the latest released Go version:

```go
go get go@latest

```

To upgrade the Go toolchain to the latest patch release of the current Go toolchain:

```go
go get toolchain@patch

```

See https://golang.org/ref/mod#go-get <https://golang.org/ref/mod#go-get> for details.

In earlier versions of Go, 'go get' was used to build and install packages. Now, 'go get' is dedicated to adjusting dependencies in go.mod. 'go install' may be used to build and install commands instead. When a version is specified, 'go install' runs in module-aware mode and ignores the go.mod file in the current directory. For example:

```go
go install example.com/pkg@v1.2.3
go install example.com/pkg@latest

```

See 'go help install' or https://golang.org/ref/mod#go-install <https://golang.org/ref/mod#go-install> for details.

'go get' accepts the following flags.

The -t flag instructs get to consider modules needed to build tests of packages specified on the command line.

The -u flag instructs get to update modules providing dependencies of packages named on the command line to use newer minor or patch releases when available.

The -u=patch flag (not -u patch) also instructs get to update dependencies, but changes the default to select patch releases.

When the -t and -u flags are used together, get will update test dependencies as well.

The -tool flag instructs go to add a matching tool line to go.mod for each listed package. If -tool is used with @none, the line will be removed.

The -x flag prints commands as they are executed. This is useful for debugging version control commands when a module is downloaded directly from a repository.

For more about build flags, see 'go help build'.

For more about modules, see https://golang.org/ref/mod <https://golang.org/ref/mod>.

For more about using 'go get' to update the minimum Go version and suggested Go toolchain, see https://go.dev/doc/toolchain <https://go.dev/doc/toolchain>.

For more about specifying packages, see 'go help packages'.

See also: go build, go install, go clean, go mod.

#### Compile and install packages and dependencies ¶

Usage:

```go
go install [build flags] [packages]

```

Install compiles and installs the packages named by the import paths.

Executables are installed in the directory named by the GOBIN environment variable, which defaults to $GOPATH/bin or $HOME/go/bin if the GOPATH environment variable is not set. Executables in $GOROOT are installed in $GOROOT/bin or $GOTOOLDIR instead of $GOBIN. Cross compiled binaries are installed in $GOOS_$GOARCH subdirectories of the above.

If the arguments have version suffixes (like @latest or @v1.0.0), "go install" builds packages in module-aware mode, ignoring the go.mod file in the current directory or any parent directory, if there is one. This is useful for installing executables without affecting the dependencies of the main module. To eliminate ambiguity about which module versions are used in the build, the arguments must satisfy the following constraints:

- Arguments must be package paths or package patterns (with "..." wildcards). They must not be standard packages (like fmt), meta-patterns (std, cmd, all), or relative or absolute file paths.

- All arguments must have the same version suffix. Different queries are not allowed, even if they refer to the same version.

- All arguments must refer to packages in the same module at the same version.

- Package path arguments must refer to main packages. Pattern arguments will only match main packages.

- No module is considered the "main" module. If the module containing packages named on the command line has a go.mod file, it must not contain directives (replace and exclude) that would cause it to be interpreted differently than if it were the main module. The module must not require a higher version of itself.

- Vendor directories are not used in any module. (Vendor directories are not included in the module zip files downloaded by 'go install'.)

If the arguments don't have version suffixes, "go install" may run in module-aware mode or GOPATH mode, depending on the GO111MODULE environment variable and the presence of a go.mod file. See 'go help modules' for details. If module-aware mode is enabled, "go install" runs in the context of the main module.

When module-aware mode is disabled, non-main packages are installed in the directory $GOPATH/pkg/$GOOS_$GOARCH. When module-aware mode is enabled, non-main packages are built and cached but not installed.

Before Go 1.20, the standard library was installed to $GOROOT/pkg/$GOOS_$GOARCH. Starting in Go 1.20, the standard library is built and cached but not installed. Setting GODEBUG=installgoroot=all restores the use of $GOROOT/pkg/$GOOS_$GOARCH.

For more about build flags, see 'go help build'.

For more about specifying packages, see 'go help packages'.

See also: go build, go get, go clean.

#### List packages or modules ¶

Usage:

```go
go list [-f format] [-json] [-m] [list flags] [build flags] [packages]

```

List lists the named packages, one per line. The most commonly-used flags are -f and -json, which control the form of the output printed for each package. Other list flags, documented below, control more specific details.

The default output shows the package import path:

```go
bytes
encoding/json
github.com/gorilla/mux
golang.org/x/net/html

```

The -f flag specifies an alternate format for the list, using the syntax of package template. The default output is equivalent to -f '{{.ImportPath}}'. The struct being passed to the template is:
