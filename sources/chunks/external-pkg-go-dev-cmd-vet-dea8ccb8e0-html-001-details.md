---
source_name: "External Linked Documentation"
source_url: "https://pkg.go.dev/cmd/vet"
source_path: "sources/raw/external/pkg-go-dev-cmd-vet-dea8ccb8e0.html"
license_ref: ""
---

vet command - cmd/vet - Go Packages
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

## Repository
   cs.opensource.google/go/go  <https://cs.opensource.google/go/go>

##   Documentation ¶

Vet examines Go source code and reports suspicious constructs, such as Printf calls whose arguments do not align with the format string. Vet uses heuristics that do not guarantee all reports are genuine problems, but it can find errors not caught by the compilers.

Vet is normally invoked through the go command. This command vets the package in the current directory:

```go
go vet

```

whereas this one vets the packages whose path is provided:

```go
go vet my/project/...

```

Use "go help packages" to see other ways of specifying which packages to vet.

Vet's exit code is non-zero for erroneous invocation of the tool or if a problem was reported, and 0 otherwise. Note that the tool does not check every possible problem and depends on unreliable heuristics, so it should be used as guidance only, not as a firm indicator of program correctness.

To list the available checks, run "go tool vet help":

```go
appends          check for missing values after append
asmdecl          report mismatches between assembly files and Go declarations
assign           check for useless assignments
atomic           check for common mistakes using the sync/atomic package
bools            check for common mistakes involving boolean operators
buildtag         check //go:build and // +build directives
cgocall          detect some violations of the cgo pointer passing rules
composites       check for unkeyed composite literals
copylocks        check for locks erroneously passed by value
defers           report common mistakes in defer statements
directive        check Go toolchain directives such as //go:debug
errorsas         report passing non-pointer or non-error values to errors.As
framepointer     report assembly that clobbers the frame pointer before saving it
hostport         check format of addresses passed to net.Dial
httpresponse     check for mistakes using HTTP responses
ifaceassert      detect impossible interface-to-interface type assertions
loopclosure      check references to loop variables from within nested functions
lostcancel       check cancel func returned by context.WithCancel is called
nilfunc          check for useless comparisons between functions and nil
printf           check consistency of Printf format strings and arguments
shift            check for shifts that equal or exceed the width of the integer
sigchanyzer      check for unbuffered channel of os.Signal
slog             check for invalid structured logging calls
stdmethods       check signature of methods of well-known interfaces
stdversion       report uses of too-new standard library symbols
stringintconv    check for string(int) conversions
structtag        check that struct field tags conform to reflect.StructTag.Get
testinggoroutine report calls to (*testing.T).Fatal from goroutines started by a test
tests            check for common mistaken usages of tests and examples
timeformat       check for calls of (time.Time).Format or time.Parse with 2006-02-01
unmarshal        report passing non-pointer or non-interface values to unmarshal
unreachable      check for unreachable code
unsafeptr        check for invalid conversions of uintptr to unsafe.Pointer
unusedresult     check for unused results of calls to some functions
waitgroup        check for misuses of sync.WaitGroup

```

For details and flags of a particular check, such as printf, run "go tool vet help printf".

By default, all checks are performed. If any flags are explicitly set to true, only those tests are run. Conversely, if any flag is explicitly set to false, only those tests are disabled. Thus -printf=true runs the printf check, and -printf=false runs all checks except the printf check.

For information on writing a new check, see golang.org/x/tools/go/analysis.

Core flags:

```go
-c=N
  	display offending line plus N lines of surrounding context
-json
  	emit analysis diagnostics (and errors) in JSON format

```

##   Source Files ¶
 View all Source files <https://cs.opensource.google/go/go/+/go1.26.3:src/cmd/vet>

- doc.go <https://cs.opensource.google/go/go/+/go1.26.3:src/cmd/vet/doc.go>
- main.go <https://cs.opensource.google/go/go/+/go1.26.3:src/cmd/vet/main.go>

  Click to show internal directories.
  Click to hide internal directories.

  Close

     **?** : This menu   **/** : Search site   **f** or **F** : Jump to   **y** or **Y**  : Canonical URL
  Close
