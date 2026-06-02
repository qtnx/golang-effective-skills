---
source_name: "External Linked Documentation"
source_url: "https://go.dev/blog/package-names"
source_path: "sources/raw/external/go-dev-blog-package-names-a6de1f37de.html"
license_ref: ""
---

# The Go Blog

## Package names

Good package names are short and clear. They are lower case, with no `under_scores` or `mixedCaps`. They are often simple nouns, such as:

- `time` (provides functionality for measuring and displaying time)
- `list` (implements a doubly linked list)
- `http` (provides HTTP client and server implementations)

The style of names typical of another language might not be idiomatic in a Go program. Here are two examples of names that might be good style in other languages but do not fit well in Go:

- `computeServiceClient`
- `priority_queue`

A Go package may export several types and functions. For example, a `compute` package could export a `Client` type with methods for using the service as well as functions for partitioning a compute task across several clients.

**Abbreviate judiciously.** Package names may be abbreviated when the abbreviation is familiar to the programmer. Widely-used packages often have compressed names:

- `strconv` (string conversion)
- `syscall` (system call)
- `fmt` (formatted I/O)

On the other hand, if abbreviating a package name makes it ambiguous or unclear, don’t do it.

**Don’t steal good names from the user.** Avoid giving a package a name that is commonly used in client code. For example, the buffered I/O package is called `bufio`, not `buf`, since `buf` is a good variable name for a buffer.
