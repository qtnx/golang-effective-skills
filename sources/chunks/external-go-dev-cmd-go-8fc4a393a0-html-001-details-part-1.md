---
source_name: "External Linked Documentation"
source_url: "https://go.dev/cmd/go/"
source_path: "sources/raw/external/go-dev-cmd-go-8fc4a393a0.html"
license_ref: ""
---

# golang.org/x/text/language

go command - cmd/go - Go Packages
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

# golang.org/x/text/language

## Repository
   cs.opensource.google/go/go  <https://cs.opensource.google/go/go>

# golang.org/x/text/language

##   Documentation ¶
   Rendered for <https://go.dev/about#build-context>  linux/amd64 windows/amd64 darwin/amd64 js/wasm

Go is a tool for managing Go source code.

Usage:

```go
go <command> [arguments]

```

The commands are:

```go
bug         start a bug report
build       compile packages and dependencies
clean       remove object files and cached files
doc         show documentation for package or symbol
env         print Go environment information
fix         apply fixes suggested by static checkers
fmt         gofmt (reformat) package sources
generate    generate Go files by processing source
get         add dependencies to current module and install them
install     compile and install packages and dependencies
list        list packages or modules
mod         module maintenance
work        workspace maintenance
run         compile and run Go program
telemetry   manage telemetry data and settings
test        test packages
tool        run specified go tool
version     print Go version
vet         report likely mistakes in packages

```

Use "go help <command>" for more information about a command.

Additional help topics:

```go
buildconstraint build constraints
buildjson       build -json encoding
buildmode       build modes
c               calling between Go and C
cache           build and test caching
environment     environment variables
filetype        file types
goauth          GOAUTH environment variable
go.mod          the go.mod file
gopath          GOPATH environment variable
goproxy         module proxy protocol
importpath      import path syntax
modules         modules, module versions, and more
module-auth     module authentication using go.sum
packages        package lists and patterns
private         configuration for downloading non-public code
testflag        testing flags
testfunc        testing functions
vcs             controlling version control with GOVCS

```

Use "go help <topic>" for more information about that topic.

#### Start a bug report ¶

Usage:

```go
go bug

```

Bug opens the default browser and starts a new bug report. The report includes useful system information.

#### Compile packages and dependencies ¶

Usage:

```go
go build [-o output] [build flags] [packages]

```

Build compiles the packages named by the import paths, along with their dependencies, but it does not install the results.

If the arguments to build are a list of .go files from a single directory, build treats them as a list of source files specifying a single package.

When compiling packages, build ignores files that end in '_test.go'.

When compiling a single main package, build writes the resulting executable to an output file named after the last non-major-version component of the package import path. The '.exe' suffix is added when writing a Windows executable. So 'go build example/sam' writes 'sam' or 'sam.exe'. 'go build example.com/foo/v2' writes 'foo' or 'foo.exe', not 'v2.exe'.

When compiling a package from a list of .go files, the executable is named after the first source file. 'go build ed.go rx.go' writes 'ed' or 'ed.exe'.

When compiling multiple packages or a single non-main package, build compiles the packages but discards the resulting object, serving only as a check that the packages can be built.

The -o flag forces build to write the resulting executable or object to the named output file or directory, instead of the default behavior described in the last two paragraphs. If the named output is an existing directory or ends with a slash or backslash, then any resulting executables will be written to that directory.

The build flags are shared by the build, clean, get, install, list, run, and test commands:
