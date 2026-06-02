---
source_name: "External Linked Documentation"
source_url: "https://go.dev/cmd/go/"
source_path: "sources/raw/external/go-dev-cmd-go-8fc4a393a0.html"
license_ref: ""
---

# golang.org/x/text/language

The -godebug, -dropgodebug, -require, -droprequire, -exclude, -dropexclude, -replace, -dropreplace, -retract, -dropretract, -tool, -droptool, -ignore, and -dropignore editing flags may be repeated, and the changes are applied in the order given.

The -print flag prints the final go.mod in its text format instead of writing it back to go.mod.

The -json flag prints the final go.mod file in JSON format instead of writing it back to go.mod. The JSON output corresponds to these Go types:

```go
type GoMod struct {
	Module    ModPath
	Go        string
	Toolchain string
	Godebug   []Godebug
	Require   []Require
	Exclude   []Module
	Replace   []Replace
	Retract   []Retract
	Tool      []Tool
	Ignore    []Ignore
}

type Module struct {
	Path    string
	Version string
}

type ModPath struct {
	Path       string
	Deprecated string
}

type Godebug struct {
	Key   string
	Value string
}

type Require struct {
	Path     string
	Version  string
	Indirect bool
}

type Replace struct {
	Old Module
	New Module
}

type Retract struct {
	Low       string
	High      string
	Rationale string
}

type Tool struct {
	Path string
}

type Ignore struct {
	Path string
}

```

Retract entries representing a single version (not an interval) will have the "Low" and "High" fields set to the same value.

Note that this only describes the go.mod file itself, not other modules referred to indirectly. For the full set of modules available to a build, use 'go list -m -json all'.

Edit also provides the -C, -n, and -x build flags.

See https://golang.org/ref/mod#go-mod-edit <https://golang.org/ref/mod#go-mod-edit> for more about 'go mod edit'.

#### Print module requirement graph ¶

Usage:

```go
go mod graph [-go=version] [-x]

```

Graph prints the module requirement graph (with replacements applied) in text form. Each line in the output has two space-separated fields: a module and one of its requirements. Each module is identified as a string of the form path@version, except for the main module, which has no @version suffix.

The -go flag causes graph to report the module graph as loaded by the given Go version, instead of the version indicated by the 'go' directive in the go.mod file.

The -x flag causes graph to print the commands graph executes.

See https://golang.org/ref/mod#go-mod-graph <https://golang.org/ref/mod#go-mod-graph> for more about 'go mod graph'.

#### Initialize new module in current directory ¶

Usage:

```go
go mod init [module-path]

```

Init initializes and writes a new go.mod file in the current directory, in effect creating a new module rooted at the current directory. The go.mod file must not already exist.

Init accepts one optional argument, the module path for the new module. If the module path argument is omitted, init will attempt to infer the module path using import comments in .go files and the current directory (if in GOPATH).

See https://golang.org/ref/mod#go-mod-init <https://golang.org/ref/mod#go-mod-init> for more about 'go mod init'.

#### Add missing and remove unused modules ¶

Usage:

```go
go mod tidy [-e] [-v] [-x] [-diff] [-go=version] [-compat=version]

```

Tidy makes sure go.mod matches the source code in the module. It adds any missing modules necessary to build the current module's packages and dependencies, and it removes unused modules that don't provide any relevant packages. It also adds any missing entries to go.sum and removes any unnecessary ones.

The -v flag causes tidy to print information about removed modules to standard error.

The -e flag causes tidy to attempt to proceed despite errors encountered while loading packages.

The -diff flag causes tidy not to modify go.mod or go.sum but instead print the necessary changes as a unified diff. It exits with a non-zero code if the diff is not empty.

The -go flag causes tidy to update the 'go' directive in the go.mod file to the given version, which may change which module dependencies are retained as explicit requirements in the go.mod file. (Go versions 1.17 and higher retain more requirements in order to support lazy module loading.)

The -compat flag preserves any additional checksums needed for the 'go' command from the indicated major Go release to successfully load the module graph, and causes tidy to error out if that version of the 'go' command would load any imported package from a different module version. By default, tidy acts as if the -compat flag were set to the version prior to the one indicated by the 'go' directive in the go.mod file.

The -x flag causes tidy to print the commands download executes.

See https://golang.org/ref/mod#go-mod-tidy <https://golang.org/ref/mod#go-mod-tidy> for more about 'go mod tidy'.

#### Make vendored copy of dependencies ¶

Usage:

```go
go mod vendor [-e] [-v] [-o outdir]

```

Vendor resets the main module's vendor directory to include all packages needed to build and test all the main module's packages. It does not include test code for vendored packages.

The -v flag causes vendor to print the names of vendored modules and packages to standard error.

The -e flag causes vendor to attempt to proceed despite errors encountered while loading packages.

The -o flag causes vendor to create the vendor directory at the given path instead of "vendor". The go command can only use a vendor directory named "vendor" within the module root directory, so this flag is primarily useful for other tools.

See https://golang.org/ref/mod#go-mod-vendor <https://golang.org/ref/mod#go-mod-vendor> for more about 'go mod vendor'.

#### Verify dependencies have expected content ¶

Usage:

```go
go mod verify

```

Verify checks that the dependencies of the current module, which are stored in a local downloaded source cache, have not been modified since being downloaded. If all the modules are unmodified, verify prints "all modules verified." Otherwise it reports which modules have been changed and causes 'go mod' to exit with a non-zero status.

See https://golang.org/ref/mod#go-mod-verify <https://golang.org/ref/mod#go-mod-verify> for more about 'go mod verify'.

#### Explain why packages or modules are needed ¶

Usage:

```go
go mod why [-m] [-vendor] packages...

```

Why shows a shortest path in the import graph from the main module to each of the listed packages. If the -m flag is given, why treats the arguments as a list of modules and finds a path to any package in each of the modules.

By default, why queries the graph of packages matched by "go list all", which includes tests for reachable packages. The -vendor flag causes why to exclude tests of dependencies.

The output is a sequence of stanzas, one for each package or module name on the command line, separated by blank lines. Each stanza begins with a comment line "# package" or "# module" giving the target package or module. Subsequent lines give a path through the import graph, one package per line. If the package or module is not referenced from the main module, the stanza will display a single parenthesized note indicating that fact.

For example:

```go
$ go mod why golang.org/x/text/language golang.org/x/text/encoding
# golang.org/x/text/language
rsc.io/quote
rsc.io/sampler
golang.org/x/text/language

# golang.org/x/text/encoding
(main module does not need package golang.org/x/text/encoding)
$

```

See https://golang.org/ref/mod#go-mod-why <https://golang.org/ref/mod#go-mod-why> for more about 'go mod why'.

#### Workspace maintenance ¶

Work provides access to operations on workspaces.

Note that support for workspaces is built into many other commands, not just 'go work'.

See 'go help modules' for information about Go's module system of which workspaces are a part.

See https://go.dev/ref/mod#workspaces <https://go.dev/ref/mod#workspaces> for an in-depth reference on workspaces.

See https://go.dev/doc/tutorial/workspaces <https://go.dev/doc/tutorial/workspaces> for an introductory tutorial on workspaces.

A workspace is specified by a go.work file that specifies a set of module directories with the "use" directive. These modules are used as root modules by the go command for builds and related operations. A workspace that does not specify modules to be used cannot be used to do builds from local modules.

go.work files are line-oriented. Each line holds a single directive, made up of a keyword followed by arguments. For example:

```go
go 1.18

use ../foo/bar
use ./baz

replace example.com/foo v1.2.3 => example.com/bar v1.4.5

```

The leading keyword can be factored out of adjacent lines to create a block, like in Go imports.

```go
use (
  ../foo/bar
  ./baz
)

```

The use directive specifies a module to be included in the workspace's set of main modules. The argument to the use directive is the directory containing the module's go.mod file.

The go directive specifies the version of Go the file was written at. It is possible there may be future changes in the semantics of workspaces that could be controlled by this version, but for now the version specified has no effect.

The replace directive has the same syntax as the replace directive in a go.mod file and takes precedence over replaces in go.mod files. It is primarily intended to override conflicting replaces in different workspace modules.

To determine whether the go command is operating in workspace mode, use the "go env GOWORK" command. This will specify the workspace file being used.

Usage:

```go
go work <command> [arguments]

```

The commands are:

```go
edit        edit go.work from tools or scripts
init        initialize workspace file
sync        sync workspace build list to modules
use         add modules to workspace file
vendor      make vendored copy of dependencies

```

Use "go help work <command>" for more information about a command.

#### Edit go.work from tools or scripts ¶

Usage:

```go
go work edit [editing flags] [go.work]

```

Edit provides a command-line interface for editing go.work, for use primarily by tools or scripts. It only reads go.work; it does not look up information about the modules involved. If no file is specified, Edit looks for a go.work file in the current directory and its parent directories

The editing flags specify a sequence of editing operations.
