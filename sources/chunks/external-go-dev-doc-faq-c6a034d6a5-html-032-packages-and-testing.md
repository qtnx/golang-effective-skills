---
source_name: "External Linked Documentation"
source_url: "https://go.dev/doc/faq"
source_path: "sources/raw/external/go-dev-doc-faq-c6a034d6a5.html"
license_ref: ""
---

# Frequently Asked Questions (FAQ)

## Packages and Testing

### How do I create a multifile package?

Put all the source files for the package in a directory by themselves. Source files can refer to items from different files at will; there is no need for forward declarations or a header file.

Other than being split into multiple files, the package will compile and test just like a single-file package.

### How do I write a unit test?

Create a new file ending in `_test.go` in the same directory as your package sources. Inside that file, `import "testing"` and write functions of the form

```go
func TestFoo(t *testing.T) {
    ...
}

```

Run `go test` in that directory. That script finds the `Test` functions, builds a test binary, and runs it.

See the How to Write Go Code document, the `testing` package and the `go test` subcommand for more details.

### Where is my favorite helper function for testing?

Go’s standard `testing` package makes it easy to write unit tests, but it lacks features provided in other language’s testing frameworks such as assertion functions. An earlier section of this document explained why Go doesn’t have assertions, and the same arguments apply to the use of `assert` in tests. Proper error handling means letting other tests run after one has failed, so that the person debugging the failure gets a complete picture of what is wrong. It is more useful for a test to report that `isPrime` gives the wrong answer for 2, 3, 5, and 7 (or for 2, 4, 8, and 16) than to report that `isPrime` gives the wrong answer for 2 and therefore no more tests were run. The programmer who triggers the test failure may not be familiar with the code that fails. Time invested writing a good error message now pays off later when the test breaks.

A related point is that testing frameworks tend to develop into mini-languages of their own, with conditionals and controls and printing mechanisms, but Go already has all those capabilities; why recreate them? We’d rather write tests in Go; it’s one fewer language to learn and the approach keeps the tests straightforward and easy to understand.

If the amount of extra code required to write good errors seems repetitive and overwhelming, the test might work better if table-driven, iterating over a list of inputs and outputs defined in a data structure (Go has excellent support for data structure literals). The work to write a good test and good error messages will then be amortized over many test cases. The standard Go library is full of illustrative examples, such as in the formatting tests for the `fmt` package.

### Why isn’t _X_ in the standard library?

The standard library’s purpose is to support the runtime library, connect to the operating system, and provide key functionality that many Go programs require, such as formatted I/O and networking. It also contains elements important for web programming, including cryptography and support for standards like HTTP, JSON, and XML.

There is no clear criterion that defines what is included because for a long time, this was the _only_ Go library. There are criteria that define what gets added today, however.

New additions to the standard library are rare and the bar for inclusion is high. Code included in the standard library bears a large ongoing maintenance cost (often borne by those other than the original author), is subject to the Go 1 compatibility promise (blocking fixes to any flaws in the API), and is subject to the Go release schedule, preventing bug fixes from being available to users quickly.

Most new code should live outside of the standard library and be accessible via the `go` tool’s `go get` command. Such code can have its own maintainers, release cycle, and compatibility guarantees. Users can find packages and read their documentation at pkg.go.dev <https://pkg.go.dev/>.

Although there are pieces in the standard library that don’t really belong, such as `log/syslog`, we continue to maintain everything in the library because of the Go 1 compatibility promise. But we encourage most new code to live elsewhere.
