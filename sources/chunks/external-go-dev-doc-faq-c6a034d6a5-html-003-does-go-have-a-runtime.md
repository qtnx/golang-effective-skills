---
source_name: "External Linked Documentation"
source_url: "https://go.dev/doc/faq"
source_path: "sources/raw/external/go-dev-doc-faq-c6a034d6a5.html"
license_ref: ""
---

## Design
### Does Go have a runtime?

Go has an extensive runtime library, often just called the _runtime_, that is part of every Go program. This library implements garbage collection, concurrency, stack management, and other critical features of the Go language. Although it is more central to the language, Go’s runtime is analogous to `libc`, the C library.

It is important to understand, however, that Go’s runtime does not include a virtual machine, such as is provided by the Java runtime. Go programs are compiled ahead of time to native machine code (or JavaScript or WebAssembly, for some variant implementations). Thus, although the term is often used to describe the virtual environment in which a program runs, in Go the word “runtime” is just the name given to the library providing critical language services.
