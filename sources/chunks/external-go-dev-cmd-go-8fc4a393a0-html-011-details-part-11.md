---
source_name: "External Linked Documentation"
source_url: "https://go.dev/cmd/go/"
source_path: "sources/raw/external/go-dev-cmd-go-8fc4a393a0.html"
license_ref: ""
---

# golang.org/x/text/language

The go command also caches successful package test results. See 'go help test' for details. Running 'go clean -testcache' removes all cached test results (but not cached build results).

The go command also caches values used in fuzzing with 'go test -fuzz', specifically, values that expanded code coverage when passed to a fuzz function. These values are not used for regular building and testing, but they're stored in a subdirectory of the build cache. Running 'go clean -fuzzcache' removes all cached fuzzing values. This may make fuzzing less effective, temporarily.

The GODEBUG environment variable can enable printing of debugging information about the state of the cache:

GODEBUG=gocacheverify=1 causes the go command to bypass the use of any cache entries and instead rebuild everything and check that the results match existing cache entries.

GODEBUG=gocachehash=1 causes the go command to print the inputs for all of the content hashes it uses to construct cache lookup keys. The output is voluminous but can be useful for debugging the cache.

GODEBUG=gocachetest=1 causes the go command to print details of its decisions about whether to reuse a cached test result.

#### Environment variables ¶

The go command and the tools it invokes consult environment variables for configuration. If an environment variable is unset or empty, the go command uses a sensible default setting. To see the effective setting of the variable <NAME>, run 'go env <NAME>'. To change the default setting, run 'go env -w <NAME>=<VALUE>'. Defaults changed using 'go env -w' are recorded in a Go environment configuration file stored in the per-user configuration directory, as reported by os.UserConfigDir. The location of the configuration file can be changed by setting the environment variable GOENV, and 'go env GOENV' prints the effective location, but 'go env -w' cannot change the default location. See 'go help env' for details.

General-purpose environment variables:

```go
GCCGO
	The gccgo command to run for 'go build -compiler=gccgo'.
GO111MODULE
	Controls whether the go command runs in module-aware mode or GOPATH mode.
	May be "off", "on", or "auto".
	See https://golang.org/ref/mod#mod-commands.
GOARCH
	The architecture, or processor, for which to compile code.
	Examples are amd64, 386, arm, ppc64.
GOAUTH
	Controls authentication for go-import and HTTPS module mirror interactions.
	See 'go help goauth'.
GOBIN
	The directory where 'go install' will install a command.
GOCACHE
	The directory where the go command will store cached
	information for reuse in future builds. Must be an absolute path.
GOCACHEPROG
	A command (with optional space-separated flags) that implements an
	external go command build cache.
	See 'go doc cmd/go/internal/cacheprog'.
GODEBUG
	Enable various debugging facilities for programs built with Go,
	including the go command. Cannot be set using 'go env -w'.
	See https://go.dev/doc/godebug for details.
GOENV
	The location of the Go environment configuration file.
	Cannot be set using 'go env -w'.
	Setting GOENV=off in the environment disables the use of the
	default configuration file.
GOFLAGS
	A space-separated list of -flag=value settings to apply
	to go commands by default, when the given flag is known by
	the current command. Each entry must be a standalone flag.
	Because the entries are space-separated, flag values must
	not contain spaces. Flags listed on the command line
	are applied after this list and therefore override it.
GOINSECURE
	Comma-separated list of glob patterns (in the syntax of Go's path.Match)
	of module path prefixes that should always be fetched in an insecure
	manner. Only applies to dependencies that are being fetched directly.
	GOINSECURE does not disable checksum database validation. GOPRIVATE or
	GONOSUMDB may be used to achieve that.
GOMODCACHE
	The directory where the go command will store downloaded modules.
GOOS
	The operating system for which to compile code.
	Examples are linux, darwin, windows, netbsd.
GOPATH
	Controls where various files are stored. See: 'go help gopath'.
GOPRIVATE, GONOPROXY, GONOSUMDB
	Comma-separated list of glob patterns (in the syntax of Go's path.Match)
	of module path prefixes that should always be fetched directly
	or that should not be compared against the checksum database.
	See https://golang.org/ref/mod#private-modules.
GOPROXY
	URL of Go module proxy. See https://golang.org/ref/mod#environment-variables
	and https://golang.org/ref/mod#module-proxy for details.
GOROOT
	The root of the go tree.
GOSUMDB
	The name of checksum database to use and optionally its public key and
	URL. See https://golang.org/ref/mod#authenticating.
GOTMPDIR
	Temporary directory used by the go command and testing package.
	Overrides the platform-specific temporary directory such as "/tmp".
	The go command and testing package will write temporary source files,
	packages, and binaries here.
GOTOOLCHAIN
	Controls which Go toolchain is used. See https://go.dev/doc/toolchain.
GOVCS
	Lists version control commands that may be used with matching servers.
	See 'go help vcs'.
GOWORK
	In module aware mode, use the given go.work file as a workspace file.
	By default or when GOWORK is "auto", the go command searches for a
	file named go.work in the current directory and then containing directories
	until one is found. If a valid go.work file is found, the modules
	specified will collectively be used as the main modules. If GOWORK
	is "off", or a go.work file is not found in "auto" mode, workspace
	mode is disabled.

```

Environment variables for use with cgo:

```go
AR
	The command to use to manipulate library archives when
	building with the gccgo compiler.
	The default is 'ar'.
CC
	The command to use to compile C code.
CGO_CFLAGS
	Flags that cgo will pass to the compiler when compiling
	C code.
CGO_CFLAGS_ALLOW
	A regular expression specifying additional flags to allow
	to appear in #cgo CFLAGS source code directives.
	Does not apply to the CGO_CFLAGS environment variable.
CGO_CFLAGS_DISALLOW
	A regular expression specifying flags that must be disallowed
	from appearing in #cgo CFLAGS source code directives.
	Does not apply to the CGO_CFLAGS environment variable.
CGO_CPPFLAGS, CGO_CPPFLAGS_ALLOW, CGO_CPPFLAGS_DISALLOW
	Like CGO_CFLAGS, CGO_CFLAGS_ALLOW, and CGO_CFLAGS_DISALLOW,
	but for the C preprocessor.
CGO_CXXFLAGS, CGO_CXXFLAGS_ALLOW, CGO_CXXFLAGS_DISALLOW
	Like CGO_CFLAGS, CGO_CFLAGS_ALLOW, and CGO_CFLAGS_DISALLOW,
	but for the C++ compiler.
CGO_ENABLED
	Whether the cgo command is supported. Either 0 or 1.
CGO_FFLAGS, CGO_FFLAGS_ALLOW, CGO_FFLAGS_DISALLOW
	Like CGO_CFLAGS, CGO_CFLAGS_ALLOW, and CGO_CFLAGS_DISALLOW,
	but for the Fortran compiler.
CGO_LDFLAGS, CGO_LDFLAGS_ALLOW, CGO_LDFLAGS_DISALLOW
	Like CGO_CFLAGS, CGO_CFLAGS_ALLOW, and CGO_CFLAGS_DISALLOW,
	but for the linker.
CXX
	The command to use to compile C++ code.
FC
	The command to use to compile Fortran code.
PKG_CONFIG
	Path to pkg-config tool.

```

Architecture-specific environment variables:

```go
GO386
	For GOARCH=386, how to implement floating point instructions.
	Valid values are sse2 (default), softfloat.
GOAMD64
	For GOARCH=amd64, the microarchitecture level for which to compile.
	Valid values are v1 (default), v2, v3, v4.
	See https://golang.org/wiki/MinimumRequirements#amd64
GOARM
	For GOARCH=arm, the ARM architecture for which to compile.
	Valid values are 5, 6, 7.
	When the Go tools are built on an arm system,
	the default value is set based on what the build system supports.
	When the Go tools are not built on an arm system
	(that is, when building a cross-compiler),
	the default value is 7.
	The value can be followed by an option specifying how to implement floating point instructions.
	Valid options are ,softfloat (default for 5) and ,hardfloat (default for 6 and 7).
GOARM64
	For GOARCH=arm64, the ARM64 architecture for which to compile.
	Valid values are v8.0 (default), v8.{1-9}, v9.{0-5}.
	The value can be followed by an option specifying extensions implemented by target hardware.
	Valid options are ,lse and ,crypto.
	Note that some extensions are enabled by default starting from a certain GOARM64 version;
	for example, lse is enabled by default starting from v8.1.
GOMIPS
	For GOARCH=mips{,le}, whether to use floating point instructions.
	Valid values are hardfloat (default), softfloat.
GOMIPS64
	For GOARCH=mips64{,le}, whether to use floating point instructions.
	Valid values are hardfloat (default), softfloat.
GOPPC64
	For GOARCH=ppc64{,le}, the target ISA (Instruction Set Architecture).
	Valid values are power8 (default), power9, power10.
GORISCV64
	For GOARCH=riscv64, the RISC-V user-mode application profile for which
	to compile. Valid values are rva20u64 (default), rva22u64, rva23u64.
	See https://github.com/riscv/riscv-profiles/blob/main/src/profiles.adoc
	and https://github.com/riscv/riscv-profiles/blob/main/src/rva23-profile.adoc
GOWASM
	For GOARCH=wasm, comma-separated list of experimental WebAssembly features to use.
	Valid values are satconv, signext.

```

Environment variables for use with code coverage:

```go
GOCOVERDIR
	Directory into which to write code coverage data files
	generated by running a "go build -cover" binary.

```

Special-purpose environment variables:

```go
GCCGOTOOLDIR
	If set, where to find gccgo tools, such as cgo.
	The default is based on how gccgo was configured.
GOEXPERIMENT
	Comma-separated list of toolchain experiments to enable or disable.
	The list of available experiments may change arbitrarily over time.
	See GOROOT/src/internal/goexperiment/flags.go for currently valid values.
	Warning: This variable is provided for the development and testing
	of the Go toolchain itself. Use beyond that purpose is unsupported.
GOFIPS140
	The FIPS-140 cryptography mode to use when building binaries.
	The default is GOFIPS140=off, which makes no FIPS-140 changes at all.
	Other values enable FIPS-140 compliance measures and select alternate
	versions of the cryptography source code.
	See https://go.dev/doc/security/fips140 for details.
GO_EXTLINK_ENABLED
	Whether the linker should use external linking mode
	when using -linkmode=auto with code that uses cgo.
	Set to 0 to disable external linking mode, 1 to enable it.
GIT_ALLOW_PROTOCOL
	Defined by Git. A colon-separated list of schemes that are allowed
	to be used with git fetch/clone. If set, any scheme not explicitly
	mentioned will be considered insecure by 'go get'.
	Because the variable is defined by Git, the default value cannot
	be set using 'go env -w'.

```

Additional information available from 'go env' but not read from the environment:
