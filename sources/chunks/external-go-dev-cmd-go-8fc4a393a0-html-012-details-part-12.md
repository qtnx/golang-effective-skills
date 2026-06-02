---
source_name: "External Linked Documentation"
source_url: "https://go.dev/cmd/go/"
source_path: "sources/raw/external/go-dev-cmd-go-8fc4a393a0.html"
license_ref: ""
---

# golang.org/x/text/language

```go
GOEXE
	The executable file name suffix (".exe" on Windows, "" on other systems).
GOGCCFLAGS
	A space-separated list of arguments supplied to the CC command.
GOHOSTARCH
	The architecture (GOARCH) of the Go toolchain binaries.
GOHOSTOS
	The operating system (GOOS) of the Go toolchain binaries.
GOMOD
	The absolute path to the go.mod of the main module.
	If module-aware mode is enabled, but there is no go.mod, GOMOD will be
	os.DevNull ("/dev/null" on Unix-like systems, "NUL" on Windows).
	If module-aware mode is disabled, GOMOD will be the empty string.
GOTELEMETRY
	The current Go telemetry mode ("off", "local", or "on").
	See "go help telemetry" for more information.
GOTELEMETRYDIR
	The directory Go telemetry data is written is written to.
GOTOOLDIR
	The directory where the go tools (compile, cover, doc, etc...) are installed.
GOVERSION
	The version of the installed Go tree, as reported by runtime.Version.

```

#### File types ¶

The go command examines the contents of a restricted set of files in each directory. It identifies which files to examine based on the extension of the file name. These extensions are:

```go
.go
	Go source files.
.c, .h
	C source files.
	If the package uses cgo or SWIG, these will be compiled with the
	OS-native compiler (typically gcc); otherwise they will
	trigger an error.
.cc, .cpp, .cxx, .hh, .hpp, .hxx
	C++ source files. Only useful with cgo or SWIG, and always
	compiled with the OS-native compiler.
.m
	Objective-C source files. Only useful with cgo, and always
	compiled with the OS-native compiler.
.s, .S, .sx
	Assembler source files.
	If the package uses cgo or SWIG, these will be assembled with the
	OS-native assembler (typically gcc (sic)); otherwise they
	will be assembled with the Go assembler.
.swig, .swigcxx
	SWIG definition files.
.syso
	System object files.

```

Files of each of these types except .syso may contain build constraints, but the go command stops scanning for build constraints at the first item in the file that is not a blank line or //-style line comment. See the go/build package documentation for more details.

#### GOAUTH environment variable ¶

GOAUTH is a semicolon-separated list of authentication commands for go-import and HTTPS module mirror interactions. The default is netrc.

The supported authentication commands are:

off

```go
Disables authentication.

```

netrc

```go
Uses credentials from NETRC or the .netrc file in your home directory.

```

git dir

```go
Runs 'git credential fill' in dir and uses its credentials. The
go command will run 'git credential approve/reject' to update
the credential helper's cache.

```

command

```go
Executes the given command (a space-separated argument list) and attaches
the provided headers to HTTPS requests.
The command must produce output in the following format:
	Response      = { CredentialSet } .
	CredentialSet = URLLine { URLLine } BlankLine { HeaderLine } BlankLine .
	URLLine       = /* URL that starts with "https://" */ '\n' .
	HeaderLine    = /* HTTP Request header */ '\n' .
	BlankLine     = '\n' .

Example:
	https://example.com
	https://example.net/api/

Authorization: Basic <token>

https://another-example.org/

Example: Data

If the server responds with any 4xx code, the go command will write the
following to the program's stdin:
	Response      = StatusLine { HeaderLine } BlankLine .
	StatusLine    = Protocol Space Status '\n' .
	Protocol      = /* HTTP protocol */ .
	Space         = ' ' .
	Status        = /* HTTP status code */ .
	BlankLine     = '\n' .
	HeaderLine    = /* HTTP Response's header */ '\n' .

Example:
	HTTP/1.1 401 Unauthorized
	Content-Length: 19
	Content-Type: text/plain; charset=utf-8
	Date: Thu, 07 Nov 2024 18:43:09 GMT

Note: it is safe to use net/http.ReadResponse to parse this input.

```

Before the first HTTPS fetch, the go command will invoke each GOAUTH command in the list with no additional arguments and no input. If the server responds with any 4xx code, the go command will invoke the GOAUTH commands again with the URL as an additional command-line argument and the HTTP Response to the program's stdin. If the server responds with an error again, the fetch fails: a URL-specific GOAUTH will only be attempted once per fetch.

#### The go.mod file ¶

A module version is defined by a tree of source files, with a go.mod file in its root. When the go command is run, it looks in the current directory and then successive parent directories to find the go.mod marking the root of the main (current) module.

The go.mod file format is described in detail at https://golang.org/ref/mod#go-mod-file <https://golang.org/ref/mod#go-mod-file>.

To create a new go.mod file, use 'go mod init'. For details see 'go help mod init' or https://golang.org/ref/mod#go-mod-init <https://golang.org/ref/mod#go-mod-init>.

To add missing module requirements or remove unneeded requirements, use 'go mod tidy'. For details, see 'go help mod tidy' or https://golang.org/ref/mod#go-mod-tidy <https://golang.org/ref/mod#go-mod-tidy>.

To add, upgrade, downgrade, or remove a specific module requirement, use 'go get'. For details, see 'go help module-get' or https://golang.org/ref/mod#go-get <https://golang.org/ref/mod#go-get>.

To make other changes or to parse go.mod as JSON for use by other tools, use 'go mod edit'. See 'go help mod edit' or https://golang.org/ref/mod#go-mod-edit <https://golang.org/ref/mod#go-mod-edit>.

#### GOPATH environment variable ¶

The Go path is used to resolve import statements. It is implemented by and documented in the go/build package.

The GOPATH environment variable lists places to look for Go code. On Unix, the value is a colon-separated string. On Windows, the value is a semicolon-separated string. On Plan 9, the value is a list.

If the environment variable is unset, GOPATH defaults to a subdirectory named "go" in the user's home directory ($HOME/go on Unix, %USERPROFILE%\go on Windows), unless that directory holds a Go distribution. Run "go env GOPATH" to see the current GOPATH.

See https://golang.org/wiki/SettingGOPATH <https://golang.org/wiki/SettingGOPATH> to set a custom GOPATH.

Each directory listed in GOPATH must have a prescribed structure:

The src directory holds source code. The path below src determines the import path or executable name.

The pkg directory holds installed package objects. As in the Go tree, each target operating system and architecture pair has its own subdirectory of pkg (pkg/GOOS_GOARCH).

If DIR is a directory listed in the GOPATH, a package with source in DIR/src/foo/bar can be imported as "foo/bar" and has its compiled form installed to "DIR/pkg/GOOS_GOARCH/foo/bar.a".

The bin directory holds compiled commands. Each command is named for its source directory, but only the final element, not the entire path. That is, the command with source in DIR/src/foo/quux is installed into DIR/bin/quux, not DIR/bin/foo/quux. The "foo/" prefix is stripped so that you can add DIR/bin to your PATH to get at the installed commands. If the GOBIN environment variable is set, commands are installed to the directory it names instead of DIR/bin. GOBIN must be an absolute path.

Here's an example directory layout:

```go
GOPATH=/home/user/go

/home/user/go/
    src/
        foo/
            bar/               (go code in package bar)
                x.go
            quux/              (go code in package main)
                y.go
    bin/
        quux                   (installed command)
    pkg/
        linux_amd64/
            foo/
                bar.a          (installed package object)

```

Go searches each directory listed in GOPATH to find source code, but new packages are always downloaded into the first directory in the list.

See https://golang.org/doc/code.html <https://golang.org/doc/code.html> for an example.

#### GOPATH and Modules ¶

When using modules, GOPATH is no longer used for resolving imports. However, it is still used to store downloaded source code (in GOPATH/pkg/mod) and compiled commands (in GOPATH/bin).

#### Internal Directories ¶

Code in or below a directory named "internal" is importable only by code in the directory tree rooted at the parent of "internal". Here's an extended version of the directory layout above:

```go
/home/user/go/
    src/
        crash/
            bang/              (go code in package bang)
                b.go
        foo/                   (go code in package foo)
            f.go
            bar/               (go code in package bar)
                x.go
            internal/
                baz/           (go code in package baz)
                    z.go
            quux/              (go code in package main)
                y.go

```

The code in z.go is imported as "foo/internal/baz", but that import statement can only appear in source files in the subtree rooted at foo. The source files foo/f.go, foo/bar/x.go, and foo/quux/y.go can all import "foo/internal/baz", but the source file crash/bang/b.go cannot.

See https://golang.org/s/go14internal <https://golang.org/s/go14internal> for details.

#### Vendor Directories ¶

Go 1.6 includes support for using local copies of external dependencies to satisfy imports of those dependencies, often referred to as vendoring.

Code below a directory named "vendor" is importable only by code in the directory tree rooted at the parent of "vendor", and only using an import path that omits the prefix up to and including the vendor element.

Here's the example from the previous section, but with the "internal" directory renamed to "vendor" and a new foo/vendor/crash/bang directory added:

```go
/home/user/go/
    src/
        crash/
            bang/              (go code in package bang)
                b.go
        foo/                   (go code in package foo)
            f.go
            bar/               (go code in package bar)
                x.go
            vendor/
                crash/
                    bang/      (go code in package bang)
                        b.go
                baz/           (go code in package baz)
                    z.go
            quux/              (go code in package main)
                y.go

```

The same visibility rules apply as for internal, but the code in z.go is imported as "baz", not as "foo/vendor/baz".

Code in vendor directories deeper in the source tree shadows code in higher directories. Within the subtree rooted at foo, an import of "crash/bang" resolves to "foo/vendor/crash/bang", not the top-level "crash/bang".

Code in vendor directories is not subject to import path checking (see 'go help importpath').

When 'go get' checks out or updates a git repository, it now also updates submodules.

Vendor directories do not affect the placement of new repositories being checked out for the first time by 'go get': those are always placed in the main GOPATH, never in a vendor subtree.

See https://golang.org/s/go15vendor <https://golang.org/s/go15vendor> for details.

#### Module proxy protocol ¶
