---
source_name: "External Linked Documentation"
source_url: "https://go.dev/cmd/go/"
source_path: "sources/raw/external/go-dev-cmd-go-8fc4a393a0.html"
license_ref: ""
---

# golang.org/x/text/language

Note that when a module has been replaced, its Replace field describes the replacement module, and its Dir field is set to the replacement's source code, if present. (That is, if Replace is non-nil, then Dir is set to Replace.Dir, with no access to the replaced source code.)

The -u flag adds information about available upgrades. When the latest version of a given module is newer than the current one, list -u sets the Module's Update field to information about the newer module. list -u will also set the module's Retracted field if the current version is retracted. The Module's String method indicates an available upgrade by formatting the newer version in brackets after the current version. If a version is retracted, the string "(retracted)" will follow it. For example, 'go list -m -u all' might print:

```go
my/main/module
golang.org/x/text v0.3.0 [v0.4.0] => /tmp/text
rsc.io/pdf v0.1.1 (retracted) [v0.1.2]

```

(For tools, 'go list -m -u -json all' may be more convenient to parse.)

The -versions flag causes list to set the Module's Versions field to a list of all known versions of that module, ordered according to semantic versioning, earliest to latest. The flag also changes the default output format to display the module path followed by the space-separated version list.

The -retracted flag causes list to report information about retracted module versions. When -retracted is used with -f or -json, the Retracted field explains why the version was retracted. The strings are taken from comments on the retract directive in the module's go.mod file. When -retracted is used with -versions, retracted versions are listed together with unretracted versions. The -retracted flag may be used with or without -m.

The arguments to list -m are interpreted as a list of modules, not packages. The main module is the module containing the current directory. The active modules are the main module and its dependencies. With no arguments, list -m shows the main module. With arguments, list -m shows the modules specified by the arguments. Any of the active modules can be specified by its module path. The special pattern "all" specifies all the active modules, first the main module and then dependencies sorted by module path. A pattern containing "..." specifies the active modules whose module paths match the pattern. A query of the form path@version specifies the result of that query, which is not limited to active modules. See 'go help modules' for more about module queries.

The template function "module" takes a single string argument that must be a module path or query and returns the specified module as a Module struct. If an error occurs, the result will be a Module struct with a non-nil Error field.

When using -m, the -reuse=old.json flag accepts the name of file containing the JSON output of a previous 'go list -m -json' invocation with the same set of modifier flags (such as -u, -retracted, and -versions). The go command may use this file to determine that a module is unchanged since the previous invocation and avoid redownloading information about it. Modules that are not redownloaded will be marked in the new output by setting the Reuse field to true. Normally the module cache provides this kind of reuse automatically; the -reuse flag can be useful on systems that do not preserve the module cache.

For more about build flags, see 'go help build'.

For more about specifying packages, see 'go help packages'.

For more about modules, see https://golang.org/ref/mod <https://golang.org/ref/mod>.

#### Module maintenance ¶

Go mod provides access to operations on modules.

Note that support for modules is built into all the go commands, not just 'go mod'. For example, day-to-day adding, removing, upgrading, and downgrading of dependencies should be done using 'go get'. See 'go help modules' for an overview of module functionality.

Usage:

```go
go mod <command> [arguments]

```

The commands are:

```go
download    download modules to local cache
edit        edit go.mod from tools or scripts
graph       print module requirement graph
init        initialize new module in current directory
tidy        add missing and remove unused modules
vendor      make vendored copy of dependencies
verify      verify dependencies have expected content
why         explain why packages or modules are needed

```

Use "go help mod <command>" for more information about a command.

#### Download modules to local cache ¶

Usage:

```go
go mod download [-x] [-json] [-reuse=old.json] [modules]

```

Download downloads the named modules, which can be module patterns selecting dependencies of the main module or module queries of the form path@version.

With no arguments, download applies to the modules needed to build and test the packages in the main module: the modules explicitly required by the main module if it is at 'go 1.17' or higher, or all transitively-required modules if at 'go 1.16' or lower.

The go command will automatically download modules as needed during ordinary execution. The "go mod download" command is useful mainly for pre-filling the local cache or to compute the answers for a Go module proxy.

By default, download writes nothing to standard output. It may print progress messages and errors to standard error.

The -json flag causes download to print a sequence of JSON objects to standard output, describing each downloaded module (or failure), corresponding to this Go struct:

```go
type Module struct {
    Path     string // module path
    Query    string // version query corresponding to this version
    Version  string // module version
    Error    string // error loading module
    Info     string // absolute path to cached .info file
    GoMod    string // absolute path to cached .mod file
    Zip      string // absolute path to cached .zip file
    Dir      string // absolute path to cached source root directory
    Sum      string // checksum for path, version (as in go.sum)
    GoModSum string // checksum for go.mod (as in go.sum)
    Origin   any    // provenance of module
    Reuse    bool   // reuse of old module info is safe
}

```

The -reuse flag accepts the name of file containing the JSON output of a previous 'go mod download -json' invocation. The go command may use this file to determine that a module is unchanged since the previous invocation and avoid redownloading it. Modules that are not redownloaded will be marked in the new output by setting the Reuse field to true. Normally the module cache provides this kind of reuse automatically; the -reuse flag can be useful on systems that do not preserve the module cache.

The -x flag causes download to print the commands download executes.

See https://golang.org/ref/mod#go-mod-download <https://golang.org/ref/mod#go-mod-download> for more about 'go mod download'.

See https://golang.org/ref/mod#version-queries <https://golang.org/ref/mod#version-queries> for more about version queries.

#### Edit go.mod from tools or scripts ¶

Usage:

```go
go mod edit [editing flags] [-fmt|-print|-json] [go.mod]

```

Edit provides a command-line interface for editing go.mod, for use primarily by tools or scripts. It reads only go.mod; it does not look up information about the modules involved. By default, edit reads and writes the go.mod file of the main module, but a different target file can be specified after the editing flags.

The editing flags specify a sequence of editing operations.

The -fmt flag reformats the go.mod file without making other changes. This reformatting is also implied by any other modifications that use or rewrite the go.mod file. The only time this flag is needed is if no other flags are specified, as in 'go mod edit -fmt'.

The -module flag changes the module's path (the go.mod file's module line).

The -godebug=key=value flag adds a godebug key=value line, replacing any existing godebug lines with the given key.

The -dropgodebug=key flag drops any existing godebug lines with the given key.

The -require=path@version and -droprequire=path flags add and drop a requirement on the given module path and version. Note that -require overrides any existing requirements on path. These flags are mainly for tools that understand the module graph. Users should prefer 'go get path@version' or 'go get path@none', which make other go.mod adjustments as needed to satisfy constraints imposed by other modules.

The -go=version flag sets the expected Go language version. This flag is mainly for tools that understand Go version dependencies. Users should prefer 'go get go@version'.

The -toolchain=version flag sets the Go toolchain to use. This flag is mainly for tools that understand Go version dependencies. Users should prefer 'go get toolchain@version'.

The -exclude=path@version and -dropexclude=path@version flags add and drop an exclusion for the given module path and version. Note that -exclude=path@version is a no-op if that exclusion already exists.

The -replace=old[@v]=new[@v] flag adds a replacement of the given module path and version pair. If the @v in old@v is omitted, a replacement without a version on the left side is added, which applies to all versions of the old module path. If the @v in new@v is omitted, the new path should be a local module root directory, not a module path. Note that -replace overrides any redundant replacements for old[@v], so omitting @v will drop existing replacements for specific versions.

The -dropreplace=old[@v] flag drops a replacement of the given module path and version pair. If the @v is omitted, a replacement without a version on the left side is dropped.

The -retract=version and -dropretract=version flags add and drop a retraction on the given version. The version may be a single version like "v1.2.3" or a closed interval like "[v1.1.0,v1.1.9]". Note that -retract=version is a no-op if that retraction already exists.

The -tool=path and -droptool=path flags add and drop a tool declaration for the given path.

The -ignore=path and -dropignore=path flags add and drop a ignore declaration for the given path.
