---
source_name: "External Linked Documentation"
source_url: "https://go.dev/blog/examples"
source_path: "sources/raw/external/go-dev-blog-examples-e3a4d00ce5.html"
license_ref: ""
---

# The Go Blog

## Output comments

What does it mean that the `ExampleString` function “passes”?

As it executes the example, the testing framework captures data written to standard output and then compares the output against the example’s “Output:” comment. The test passes if the test’s output matches its output comment.

To see a failing example we can change the output comment text to something obviously incorrect

```go
func ExampleString() {
    fmt.Println(reverse.String("hello"))
    // Output: golly
}

```

and run the tests again:

```go
$ go test
--- FAIL: ExampleString (0.00s)
got:
olleh
want:
golly
FAIL

```

If we remove the output comment entirely

```go
func ExampleString() {
    fmt.Println(reverse.String("hello"))
}

```

then the example function is compiled but not executed:

```go
$ go test -v
=== RUN   TestString
--- PASS: TestString (0.00s)
PASS
ok      golang.org/x/example/hello/reverse  0.110s

```

Examples without output comments are useful for demonstrating code that cannot run as unit tests, such as that which accesses the network, while guaranteeing the example at least compiles.
