---
source_name: "External Linked Documentation"
source_url: "https://go.dev/blog/examples"
source_path: "sources/raw/external/go-dev-blog-examples-e3a4d00ce5.html"
license_ref: ""
---

# The Go Blog

Testable Examples in Go - The Go Programming Language
# The Go Blog
# Testable Examples in Go
 Andrew Gerrand
 7 May 2015
## Introduction

Godoc examples are snippets of Go code that are displayed as package documentation and that are verified by running them as tests. They can also be run by a user visiting the godoc web page for the package and clicking the associated “Run” button.

Having executable documentation for a package guarantees that the information will not go out of date as the API changes.

The standard library includes many such examples (see the `strings` package, for instance).

This article explains how to write your own example functions.

# The Go Blog

## Examples are tests

Examples are compiled (and optionally executed) as part of a package’s test suite.

As with typical tests, examples are functions that reside in a package’s `_test.go` files. Unlike normal test functions, though, example functions take no arguments and begin with the word `Example` instead of `Test`.

The `reverse` package <https://pkg.go.dev/golang.org/x/example/hello/reverse/> is part of the Go example repository <https://cs.opensource.google/go/x/example>. Here’s an example that demonstrates its `String` function:

```go
package reverse_test

import (
    "fmt"

    "golang.org/x/example/hello/reverse"
)

func ExampleString() {
    fmt.Println(reverse.String("hello"))
    // Output: olleh
}

```

This code might live in `example_test.go` in the `reverse` directory.

The Go package documentation server _pkg.go.dev_ presents this example alongside the `String` function’s documentation <https://pkg.go.dev/golang.org/x/example/hello/reverse/#String>:

Running the package’s test suite, we can see the example function is executed with no further arrangement from us:

```go
$ go test -v
=== RUN   TestString
--- PASS: TestString (0.00s)
=== RUN   ExampleString
--- PASS: ExampleString (0.00s)
PASS
ok      golang.org/x/example/hello/reverse  0.209s

```
