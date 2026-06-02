---
source_name: "External Linked Documentation"
source_url: "https://go.dev/cmd/go/"
source_path: "sources/raw/external/go-dev-cmd-go-8fc4a393a0.html"
license_ref: ""
---

# golang.org/x/text/language

- the target operating system, as spelled by runtime.GOOS, set with the GOOS environment variable.
- the target architecture, as spelled by runtime.GOARCH, set with the GOARCH environment variable.
- any architecture features, in the form GOARCH.feature (for example, "amd64.v2"), as detailed below.
- "unix", if GOOS is a Unix or Unix-like system.
- the compiler being used, either "gc" or "gccgo"
- "cgo", if the cgo command is supported (see CGO_ENABLED in 'go help environment').
- a term for each Go major release, through the current version: "go1.1" from Go version 1.1 onward, "go1.12" from Go 1.12, and so on.
- any additional tags given by the -tags flag (see 'go help build').

There are no separate build tags for beta or minor releases.

If a file's name, after stripping the extension and a possible _test suffix, matches any of the following patterns:

```go
*_GOOS
*_GOARCH
*_GOOS_GOARCH

```

(example: source_windows_amd64.go) where GOOS and GOARCH represent any known operating system and architecture values respectively, then the file is considered to have an implicit build constraint requiring those terms (in addition to any explicit constraints in the file).

Using GOOS=android matches build tags and files as for GOOS=linux in addition to android tags and files.

Using GOOS=illumos matches build tags and files as for GOOS=solaris in addition to illumos tags and files.

Using GOOS=ios matches build tags and files as for GOOS=darwin in addition to ios tags and files.

The defined architecture feature build tags are:

- For GOARCH=386, GO386=387 and GO386=sse2 set the 386.387 and 386.sse2 build tags, respectively.
- For GOARCH=amd64, GOAMD64=v1, v2, and v3 correspond to the amd64.v1, amd64.v2, and amd64.v3 feature build tags.
- For GOARCH=arm, GOARM=5, 6, and 7 correspond to the arm.5, arm.6, and arm.7 feature build tags.
- For GOARCH=arm64, GOARM64=v8.{0-9} and v9.{0-5} correspond to the arm64.v8.{0-9} and arm64.v9.{0-5} feature build tags.
- For GOARCH=mips or mipsle, GOMIPS=hardfloat and softfloat correspond to the mips.hardfloat and mips.softfloat (or mipsle.hardfloat and mipsle.softfloat) feature build tags.
- For GOARCH=mips64 or mips64le, GOMIPS64=hardfloat and softfloat correspond to the mips64.hardfloat and mips64.softfloat (or mips64le.hardfloat and mips64le.softfloat) feature build tags.
- For GOARCH=ppc64 or ppc64le, GOPPC64=power8, power9, and power10 correspond to the ppc64.power8, ppc64.power9, and ppc64.power10 (or ppc64le.power8, ppc64le.power9, and ppc64le.power10) feature build tags.
- For GOARCH=riscv64, GORISCV64=rva20u64, rva22u64 and rva23u64 correspond to the riscv64.rva20u64, riscv64.rva22u64 and riscv64.rva23u64 build tags.
- For GOARCH=wasm, GOWASM=satconv and signext correspond to the wasm.satconv and wasm.signext feature build tags.

For GOARCH=amd64, arm, ppc64, ppc64le, and riscv64, a particular feature level sets the feature build tags for all previous levels as well. For example, GOAMD64=v2 sets the amd64.v1 and amd64.v2 feature flags. This ensures that code making use of v2 features continues to compile when, say, GOAMD64=v4 is introduced. Code handling the absence of a particular feature level should use a negation:

```go
//go:build !amd64.v2

```

To keep a file from being considered for any build:

```go
//go:build ignore

```

(Any other unsatisfied word will work as well, but "ignore" is conventional.)

To build a file only when using cgo, and only on Linux and OS X:

```go
//go:build cgo && (linux || darwin)

```

Such a file is usually paired with another file implementing the default functionality for other systems, which in this case would carry the constraint:

```go
//go:build !(cgo && (linux || darwin))

```

Naming a file dns_windows.go will cause it to be included only when building the package for Windows; similarly, math_386.s will be included only when building the package for 32-bit x86.

By convention, packages with assembly implementations may provide a go-only version under the "purego" build constraint. This does not limit the use of cgo (use the "cgo" build constraint) or unsafe. For example:

```go
//go:build purego

```

Go versions 1.16 and earlier used a different syntax for build constraints, with a "// +build" prefix. The gofmt command will add an equivalent //go:build constraint when encountering the older syntax.

In modules with a Go version of 1.21 or later, if a file's build constraint has a term for a Go major release, the language version used when compiling the file will be the minimum version implied by the build constraint.

#### Build -json encoding ¶

The 'go build', 'go install', and 'go test' commands take a -json flag that reports build output and failures as structured JSON output on standard output.

The JSON stream is a newline-separated sequence of BuildEvent objects corresponding to the Go struct:

```go
type BuildEvent struct {
	ImportPath string
	Action     string
	Output     string
}

```

The ImportPath field gives the package ID of the package being built. This matches the Package.ImportPath field of go list -json and the TestEvent.FailedBuild field of go test -json. Note that it does not match TestEvent.Package.

The Action field is one of the following:

```go
build-output - The toolchain printed output
build-fail - The build failed

```

The Output field is set for Action == "build-output" and is a portion of the build's output. The concatenation of the Output fields of all output events is the exact output of the build. A single event may contain one or more lines of output and there may be more than one output event for a given ImportPath. This matches the definition of the TestEvent.Output field produced by go test -json.

For go test -json, this struct is designed so that parsers can distinguish interleaved TestEvents and BuildEvents by inspecting the Action field. Furthermore, as with TestEvent, parsers can simply concatenate the Output fields of all events to reconstruct the text format output, as it would have appeared from go build without the -json flag.

Note that there may also be non-JSON error text on standard error, even with the -json flag. Typically, this indicates an early, serious error. Consumers should be robust to this.

#### Build modes ¶

The 'go build' and 'go install' commands take a -buildmode argument which indicates which kind of object file is to be built. Currently supported values are:

```go
-buildmode=archive
	Build the listed non-main packages into .a files. Packages named
	main are ignored.

-buildmode=c-archive
	Build the listed main package, plus all packages it imports,
	into a C archive file. The only callable symbols will be those
	functions exported using a cgo //export comment. Requires
	exactly one main package to be listed.

-buildmode=c-shared
	Build the listed main package, plus all packages it imports,
	into a C shared library. The only callable symbols will
	be those functions exported using a cgo //export comment.
	On wasip1, this mode builds it to a WASI reactor/library,
	of which the callable symbols are those functions exported
	using a //go:wasmexport directive. Requires exactly one
	main package to be listed.

-buildmode=default
	Listed main packages are built into executables and listed
	non-main packages are built into .a files (the default
	behavior).

-buildmode=shared
	Combine all the listed non-main packages into a single shared
	library that will be used when building with the -linkshared
	option. Packages named main are ignored.

-buildmode=exe
	Build the listed main packages and everything they import into
	executables. Packages not named main are ignored.

-buildmode=pie
	Build the listed main packages and everything they import into
	position independent executables (PIE). Packages not named
	main are ignored.

-buildmode=plugin
	Build the listed main packages, plus all packages that they
	import, into a Go plugin. Packages not named main are ignored.

```

On AIX, when linking a C program that uses a Go archive built with -buildmode=c-archive, you must pass -Wl,-bnoobjreorder to the C compiler.

#### Calling between Go and C ¶

There are two different ways to call between Go and C/C++ code.

The first is the cgo tool, which is part of the Go distribution. For information on how to use it see the cgo documentation (go doc cmd/cgo).

The second is the SWIG program, which is a general tool for interfacing between languages. For information on SWIG see https://swig.org/ <https://swig.org/>. When running go build, any file with a .swig extension will be passed to SWIG. Any file with a .swigcxx extension will be passed to SWIG with the -c++ option. A package can't be just a .swig or .swigcxx file; there must be at least one .go file, even if it has just a package clause.

When either cgo or SWIG is used, go build will pass any .c, .m, .s, .S or .sx files to the C compiler, and any .cc, .cpp, .cxx files to the C++ compiler. The CC or CXX environment variables may be set to determine the C or C++ compiler, respectively, to use.

#### Build and test caching ¶

The go command caches build outputs for reuse in future builds. The default location for cache data is a subdirectory named go-build in the standard user cache directory for the current operating system. The cache is safe for concurrent invocations of the go command. Setting the GOCACHE environment variable overrides this default, and running 'go env GOCACHE' prints the current cache directory.

The go command periodically deletes cached data that has not been used recently. Running 'go clean -cache' deletes all cached data.

The build cache correctly accounts for changes to Go source files, compilers, compiler options, and so on: cleaning the cache explicitly should not be necessary in typical use. However, the build cache does not detect changes to C libraries imported with cgo. If you have made changes to the C libraries on your system, you will need to clean the cache explicitly or else use the -a build flag (see 'go help build') to force rebuilding of packages that depend on the updated C libraries.
