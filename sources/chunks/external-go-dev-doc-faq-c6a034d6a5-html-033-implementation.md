---
source_name: "External Linked Documentation"
source_url: "https://go.dev/doc/faq"
source_path: "sources/raw/external/go-dev-doc-faq-c6a034d6a5.html"
license_ref: ""
---

# Frequently Asked Questions (FAQ)

## Implementation

### What compiler technology is used to build the compilers?

There are several production compilers for Go, and a number of others in development for various platforms.

The default compiler, `gc`, is included with the Go distribution as part of the support for the `go` command. `Gc` was originally written in C because of the difficulties of bootstrapping—you’d need a Go compiler to set up a Go environment. But things have advanced and since the Go 1.5 release the compiler has been a Go program. The compiler was converted from C to Go using automatic translation tools, as described in this design document and talk. Thus the compiler is now “self-hosting”, which means we needed to face the bootstrapping problem. The solution is to have a working Go installation already in place, just as one normally has with a working C installation. The story of how to bring up a new Go environment from source is described here and here.

`Gc` is written in Go with a recursive descent parser and uses a custom loader, also written in Go but based on the Plan 9 loader, to generate ELF/Mach-O/PE binaries.

The `Gccgo` compiler is a front end written in C++ with a recursive descent parser coupled to the standard GCC back end. An experimental LLVM back end <https://go.googlesource.com/gollvm/> is using the same front end.

At the beginning of the project we considered using LLVM for `gc` but decided it was too large and slow to meet our performance goals. More important in retrospect, starting with LLVM would have made it harder to introduce some of the ABI and related changes, such as stack management, that Go requires but are not part of the standard C setup.

Go turned out to be a fine language in which to implement a Go compiler, although that was not its original goal. Not being self-hosting from the beginning allowed Go’s design to concentrate on its original use case, which was networked servers. Had we decided Go should compile itself early on, we might have ended up with a language targeted more for compiler construction, which is a worthy goal but not the one we had initially.

Although `gc` has its own implementation, a native lexer and parser are available in the `go/parser` package and there is also a native type checker. The `gc` compiler uses variants of these libraries.

### How is the run-time support implemented?

Again due to bootstrapping issues, the run-time code was originally written mostly in C (with a tiny bit of assembler) but it has since been translated to Go (except for some assembler bits). `Gccgo`’s run-time support uses `glibc`. The `gccgo` compiler implements goroutines using a technique called segmented stacks, supported by recent modifications to the gold linker. `Gollvm` similarly is built on the corresponding LLVM infrastructure.

### Why is my trivial program such a large binary?

The linker in the `gc` toolchain creates statically-linked binaries by default. All Go binaries therefore include the Go runtime, along with the run-time type information necessary to support dynamic type checks, reflection, and even panic-time stack traces.

A simple C “hello, world” program compiled and linked statically using gcc on Linux is around 750 kB, including an implementation of `printf`. An equivalent Go program using `fmt.Printf` weighs a couple of megabytes, but that includes more powerful run-time support and type and debugging information.

A Go program compiled with `gc` can be linked with the `-ldflags=-w` flag to disable DWARF generation, removing debugging information from the binary but with no other loss of functionality. This can reduce the binary size substantially.

### Can I stop these complaints about my unused variable/import?

The presence of an unused variable may indicate a bug, while unused imports just slow down compilation, an effect that can become substantial as a program accumulates code and programmers over time. For these reasons, Go refuses to compile programs with unused variables or imports, trading short-term convenience for long-term build speed and program clarity.

Still, when developing code, it’s common to create these situations temporarily and it can be annoying to have to edit them out before the program will compile.

Some have asked for a compiler option to turn those checks off or at least reduce them to warnings. Such an option has not been added, though, because compiler options should not affect the semantics of the language and because the Go compiler does not report warnings, only errors that prevent compilation.

There are two reasons for having no warnings. First, if it’s worth complaining about, it’s worth fixing in the code. (Conversely, if it’s not worth fixing, it’s not worth mentioning.) Second, having the compiler generate warnings encourages the implementation to warn about weak cases that can make compilation noisy, masking real errors that _should_ be fixed.

It’s easy to address the situation, though. Use the blank identifier to let unused things persist while you’re developing.

```go
import "unused"

// This declaration marks the import as used by referencing an
// item from the package.
var _ = unused.Item  // TODO: Delete before committing!

func main() {
    debugData := debug.Profile()
    _ = debugData // Used only during debugging.
    ....
}

```

Nowadays, most Go programmers use a tool, goimports <https://godoc.org/golang.org/x/tools/cmd/goimports>, which automatically rewrites a Go source file to have the correct imports, eliminating the unused imports issue in practice. This program is easily connected to most editors and IDEs to run automatically when a Go source file is written. This functionality is also built into `gopls`, as discussed above.

### Why does my virus-scanning software think my Go distribution or compiled binary is infected?

This is a common occurrence, especially on Windows machines, and is almost always a false positive. Commercial virus scanning programs are often confused by the structure of Go binaries, which they don’t see as often as those compiled from other languages.

If you’ve just installed the Go distribution and the system reports it is infected, that’s certainly a mistake. To be really thorough, you can verify the download by comparing the checksum with those on the downloads page.

In any case, if you believe the report is in error, please report a bug to the supplier of your virus scanner. Maybe in time virus scanners can learn to understand Go programs.
