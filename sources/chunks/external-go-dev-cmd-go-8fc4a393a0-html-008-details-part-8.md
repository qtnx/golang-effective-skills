---
source_name: "External Linked Documentation"
source_url: "https://go.dev/cmd/go/"
source_path: "sources/raw/external/go-dev-cmd-go-8fc4a393a0.html"
license_ref: ""
---

# golang.org/x/text/language

The -fmt flag reformats the go.work file without making other changes. This reformatting is also implied by any other modifications that use or rewrite the go.mod file. The only time this flag is needed is if no other flags are specified, as in 'go work edit -fmt'.

The -godebug=key=value flag adds a godebug key=value line, replacing any existing godebug lines with the given key.

The -dropgodebug=key flag drops any existing godebug lines with the given key.

The -use=path and -dropuse=path flags add and drop a use directive from the go.work file's set of module directories.

The -replace=old[@v]=new[@v] flag adds a replacement of the given module path and version pair. If the @v in old@v is omitted, a replacement without a version on the left side is added, which applies to all versions of the old module path. If the @v in new@v is omitted, the new path should be a local module root directory, not a module path. Note that -replace overrides any redundant replacements for old[@v], so omitting @v will drop existing replacements for specific versions.

The -dropreplace=old[@v] flag drops a replacement of the given module path and version pair. If the @v is omitted, a replacement without a version on the left side is dropped.

The -use, -dropuse, -replace, and -dropreplace, editing flags may be repeated, and the changes are applied in the order given.

The -go=version flag sets the expected Go language version.

The -toolchain=name flag sets the Go toolchain to use.

The -print flag prints the final go.work in its text format instead of writing it back to go.mod.

The -json flag prints the final go.work file in JSON format instead of writing it back to go.mod. The JSON output corresponds to these Go types:

```go
type GoWork struct {
	Go        string
	Toolchain string
	Godebug   []Godebug
	Use       []Use
	Replace   []Replace
}

type Godebug struct {
	Key   string
	Value string
}

type Use struct {
	DiskPath   string
	ModulePath string
}

type Replace struct {
	Old Module
	New Module
}

type Module struct {
	Path    string
	Version string
}

```

See the workspaces reference at https://go.dev/ref/mod#workspaces <https://go.dev/ref/mod#workspaces> for more information.

#### Initialize workspace file ¶

Usage:

```go
go work init [moddirs]

```

Init initializes and writes a new go.work file in the current directory, in effect creating a new workspace at the current directory.

go work init optionally accepts paths to the workspace modules as arguments. If the argument is omitted, an empty workspace with no modules will be created.

Each argument path is added to a use directive in the go.work file. The current go version will also be listed in the go.work file.

See the workspaces reference at https://go.dev/ref/mod#workspaces <https://go.dev/ref/mod#workspaces> for more information.

#### Sync workspace build list to modules ¶

Usage:

```go
go work sync

```

Sync syncs the workspace's build list back to the workspace's modules

The workspace's build list is the set of versions of all the (transitive) dependency modules used to do builds in the workspace. go work sync generates that build list using the Minimal Version Selection algorithm, and then syncs those versions back to each of modules specified in the workspace (with use directives).

The syncing is done by sequentially upgrading each of the dependency modules specified in a workspace module to the version in the build list if the dependency module's version is not already the same as the build list's version. Note that Minimal Version Selection guarantees that the build list's version of each module is always the same or higher than that in each workspace module.

See the workspaces reference at https://go.dev/ref/mod#workspaces <https://go.dev/ref/mod#workspaces> for more information.

#### Add modules to workspace file ¶

Usage:

```go
go work use [-r] [moddirs]

```

Use provides a command-line interface for adding directories, optionally recursively, to a go.work file.

A use directive will be added to the go.work file for each argument directory listed on the command line go.work file, if it exists, or removed from the go.work file if it does not exist. Use fails if any remaining use directives refer to modules that do not exist.

Use updates the go line in go.work to specify a version at least as new as all the go lines in the used modules, both preexisting ones and newly added ones. With no arguments, this update is the only thing that go work use does.

The -r flag searches recursively for modules in the argument directories, and the use command operates as if each of the directories were specified as arguments.

See the workspaces reference at https://go.dev/ref/mod#workspaces <https://go.dev/ref/mod#workspaces> for more information.

#### Make vendored copy of dependencies ¶

Usage:

```go
go work vendor [-e] [-v] [-o outdir]

```

Vendor resets the workspace's vendor directory to include all packages needed to build and test all the workspace's packages. It does not include test code for vendored packages.

The -v flag causes vendor to print the names of vendored modules and packages to standard error.

The -e flag causes vendor to attempt to proceed despite errors encountered while loading packages.

The -o flag causes vendor to create the vendor directory at the given path instead of "vendor". The go command can only use a vendor directory named "vendor" within the module root directory, so this flag is primarily useful for other tools.

#### Compile and run Go program ¶

Usage:

```go
go run [build flags] [-exec xprog] package [arguments...]

```

Run compiles and runs the named main Go package. Typically the package is specified as a list of .go source files from a single directory, but it may also be an import path, file system path, or pattern matching a single known package, as in 'go run .' or 'go run my/cmd'.

If the package argument has a version suffix (like @latest or @v1.0.0), "go run" builds the program in module-aware mode, ignoring the go.mod file in the current directory or any parent directory, if there is one. This is useful for running programs without affecting the dependencies of the main module.

If the package argument doesn't have a version suffix, "go run" may run in module-aware mode or GOPATH mode, depending on the GO111MODULE environment variable and the presence of a go.mod file. See 'go help modules' for details. If module-aware mode is enabled, "go run" runs in the context of the main module.

By default, 'go run' runs the compiled binary directly: 'a.out arguments...'. If the -exec flag is given, 'go run' invokes the binary using xprog:

```go
'xprog a.out arguments...'.

```

If the -exec flag is not given, GOOS or GOARCH is different from the system default, and a program named go_$GOOS_$GOARCH_exec can be found on the current search path, 'go run' invokes the binary using that program, for example 'go_js_wasm_exec a.out arguments...'. This allows execution of cross-compiled programs when a simulator or other execution method is available.

By default, 'go run' compiles the binary without generating the information used by debuggers, to reduce build time. To include debugger information in the binary, use 'go build'.

The exit status of Run is not the exit status of the compiled binary.

For more about build flags, see 'go help build'. For more about specifying packages, see 'go help packages'.

See also: go build.

#### Manage telemetry data and settings ¶

Usage:

```go
go telemetry [off|local|on]

```

Telemetry is used to manage Go telemetry data and settings.

Telemetry can be in one of three modes: off, local, or on.

When telemetry is in local mode, counter data is written to the local file system, but will not be uploaded to remote servers.

When telemetry is off, local counter data is neither collected nor uploaded.

When telemetry is on, telemetry data is written to the local file system and periodically sent to https://telemetry.go.dev/ <https://telemetry.go.dev/>. Uploaded data is used to help improve the Go toolchain and related tools, and it will be published as part of a public dataset.

For more details, see https://telemetry.go.dev/privacy <https://telemetry.go.dev/privacy>. This data is collected in accordance with the Google Privacy Policy (https://policies.google.com/privacy <https://policies.google.com/privacy>).

To view the current telemetry mode, run "go telemetry". To disable telemetry uploading, but keep local data collection, run "go telemetry local". To enable both collection and uploading, run “go telemetry on”. To disable both collection and uploading, run "go telemetry off".

The current telemetry mode is also available as the value of the non-settable "GOTELEMETRY" go env variable. The directory in the local file system that telemetry data is written to is available as the value of the non-settable "GOTELEMETRYDIR" go env variable.

See https://go.dev/doc/telemetry <https://go.dev/doc/telemetry> for more information on telemetry.

#### Test packages ¶

Usage:

```go
go test [build/test flags] [packages] [build/test flags & test binary flags]

```

'Go test' automates testing the packages named by the import paths. It prints a summary of the test results in the format:

```go
ok   archive/tar   0.011s
FAIL archive/zip   0.022s
ok   compress/gzip 0.033s
...

```

followed by detailed output for each failed package.

'Go test' recompiles each package along with any files with names matching the file pattern "*_test.go". These additional files can contain test functions, benchmark functions, fuzz tests and example functions. See 'go help testfunc' for more. Each listed package causes the execution of a separate test binary. Files whose names begin with "_" (including "_test.go") or "." are ignored.

Test files that declare a package with the suffix "_test" will be compiled as a separate package, and then linked and run with the main test binary.

The go tool will ignore a directory named "testdata", making it available to hold ancillary data needed by the tests.
