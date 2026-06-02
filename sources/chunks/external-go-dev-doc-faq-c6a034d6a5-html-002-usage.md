---
source_name: "External Linked Documentation"
source_url: "https://go.dev/doc/faq"
source_path: "sources/raw/external/go-dev-doc-faq-c6a034d6a5.html"
license_ref: ""
---

# Frequently Asked Questions (FAQ)

## Usage

### Is Google using Go internally?

Yes. Go is used widely in production inside Google. One example is Google’s download server, `dl.google.com`, which delivers Chrome binaries and other large installables such as `apt-get` packages.

Go is not the only language used at Google, far from it, but it is a key language for a number of areas including site reliability engineering (SRE) and large-scale data processing. It is also a key part of the software that runs Google Cloud.

### What other companies use Go?

Go usage is growing worldwide, especially but by no means exclusively in the cloud computing space. A couple of major cloud infrastructure projects written in Go are Docker and Kubernetes, but there are many more.

It’s not just cloud, though, as you can see from the list of companies on the go.dev web site along with some success stories. Also, the Go Wiki includes a page, updated regularly, that lists some of the many companies using Go.

The Wiki also has a page with links to more success stories about companies and projects that are using the language.

### Do Go programs link with C/C++ programs?

It is possible to use C and Go together in the same address space, but it is not a natural fit and can require special interface software. Also, linking C with Go code gives up the memory safety and stack management properties that Go provides. Sometimes it’s absolutely necessary to use C libraries to solve a problem, but doing so always introduces an element of risk not present with pure Go code, so do so with care.

If you do need to use C with Go, how to proceed depends on the Go compiler implementation. The “standard” compiler, part of the Go toolchain supported by the Go team at Google, is called `gc`. In addition, there are also a GCC-based compiler (`gccgo`) and an LLVM-based compiler (`gollvm`), as well as a growing list of unusual ones serving different purposes, sometimes implementing language subsets, such as TinyGo <https://tinygo.org/>.

`Gc` uses a different calling convention and linker from C and therefore cannot be called directly from C programs, or vice versa. The `cgo` program provides the mechanism for a “foreign function interface” to allow safe calling of C libraries from Go code. SWIG extends this capability to C++ libraries.

You can also use `cgo` and SWIG with `gccgo` and `gollvm`. Since they use a traditional ABI, it’s also possible, with great care, to link code from these compilers directly with GCC/LLVM-compiled C or C++ programs. However, doing so safely requires an understanding of the calling conventions for all languages concerned, as well as concern for stack limits when calling C or C++ from Go.

### What IDEs does Go support?

The Go project does not include a custom IDE, but the language and libraries have been designed to make it easy to analyze source code. As a consequence, most well-known editors and IDEs support Go well, either directly or through a plugin.

The Go team also supports a Go language server for the LSP protocol, called `gopls` <https://pkg.go.dev/golang.org/x/tools/gopls#section-readme>. Tools that support LSP can use `gopls` to integrate language-specific support.

The list of well-known IDEs and editors that offer good Go support includes Emacs, Vim, VSCode, Atom, Eclipse, Sublime, IntelliJ (through a custom variant called GoLand), and many more. Chances are your favorite environment is a productive one for programming in Go.

### Does Go support Google’s protocol buffers?

A separate open source project provides the necessary compiler plugin and library. It is available at github.com/golang/protobuf/ <https://github.com/golang/protobuf>.
