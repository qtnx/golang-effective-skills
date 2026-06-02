---
source_name: "External Linked Documentation"
source_url: "https://go.dev/doc/comment"
source_path: "sources/raw/external/go-dev-doc-comment-d01a1d6946.html"
license_ref: ""
---

# Go Doc Comments

## Common mistakes and pitfalls

The rule that any span of indented or blank lines in a doc comment is rendered as a code block dates to the earliest days of Go. Unfortunately, the lack of support for doc comments in gofmt has led to many existing comments that use indentation without meaning to create a code block.

For example, this unindented list has always been interpreted by godoc as a three-line paragraph followed by a one-line code block:

```go
package http

// cancelTimerBody is an io.ReadCloser that wraps rc with two features:
// 1) On Read error or close, the stop func is called.
// 2) On Read failure, if reqDidTimeout is true, the error is wrapped and
//    marked as net.Error that hit its timeout.
type cancelTimerBody struct {
    ...
}

```

This always rendered in `go` `doc` as:

```go
cancelTimerBody is an io.ReadCloser that wraps rc with two features:
1) On Read error or close, the stop func is called. 2) On Read failure,
if reqDidTimeout is true, the error is wrapped and

    marked as net.Error that hit its timeout.

```

Similarly, the command in this comment is a one-line paragraph followed by a one-line code block:

```go
package smtp

// localhostCert is a PEM-encoded TLS cert generated from src/crypto/tls:
//
// go run generate_cert.go --rsa-bits 1024 --host 127.0.0.1,::1,example.com \
//     --ca --start-date "Jan 1 00:00:00 1970" --duration=1000000h
var localhostCert = []byte(`...`)

```

This rendered in `go` `doc` as:

```go
localhostCert is a PEM-encoded TLS cert generated from src/crypto/tls:

go run generate_cert.go --rsa-bits 1024 --host 127.0.0.1,::1,example.com \

    --ca --start-date "Jan 1 00:00:00 1970" --duration=1000000h

```

And this comment is a two-line paragraph (the second line is “{”), followed by a six-line indented code block and a one-line paragraph (“}”).

```go
// On the wire, the JSON will look something like this:
// {
//  "kind":"MyAPIObject",
//  "apiVersion":"v1",
//  "myPlugin": {
//      "kind":"PluginA",
//      "aOption":"foo",
//  },
// }

```

And this rendered in `go` `doc` as:

```go
On the wire, the JSON will look something like this: {

    "kind":"MyAPIObject",
    "apiVersion":"v1",
    "myPlugin": {
        "kind":"PluginA",
        "aOption":"foo",
    },

}

```

Another common mistake was an unindented Go function definition or block statement, similarly bracketed by “{” and “}”.

The introduction of doc comment reformatting in Go 1.19’s gofmt makes mistakes like these more visible by adding blank lines around the code blocks.

Analysis in 2022 found that only 3% of doc comments in public Go modules were reformatted at all by the draft Go 1.19 gofmt. Limiting ourselves to those comments, about 87% of gofmt’s reformattings preserved the structure that a person would infer from reading the comment; about 6% were tripped up by these kinds of unindented lists, unindented multiline shell commands, and unindented brace-delimited code blocks.

Based on this analysis, the Go 1.19 gofmt applies a few heuristics to merge unindented lines into an adjacent indented list or code block. With those adjustments, the Go 1.19 gofmt reformats the above examples to:

```go
// cancelTimerBody is an io.ReadCloser that wraps rc with two features:
//  1. On Read error or close, the stop func is called.
//  2. On Read failure, if reqDidTimeout is true, the error is wrapped and
//     marked as net.Error that hit its timeout.

// localhostCert is a PEM-encoded TLS cert generated from src/crypto/tls:
//
//  go run generate_cert.go --rsa-bits 1024 --host 127.0.0.1,::1,example.com \
//      --ca --start-date "Jan 1 00:00:00 1970" --duration=1000000h

// On the wire, the JSON will look something like this:
//
//  {
//      "kind":"MyAPIObject",
//      "apiVersion":"v1",
//      "myPlugin": {
//          "kind":"PluginA",
//          "aOption":"foo",
//      },
//  }

```

This reformatting makes the meaning clearer as well as making the doc comments render correctly in earlier versions of Go. If the heuristic ever makes a bad decision, it can be overridden by inserting a blank line to clearly separate the paragraph text from non-paragraph text.

Even with these heuristics, other existing comments will need manual adjustment to correct their rendering. The most common mistake is indenting a wrapped unindented line of text. For example:

```go
// TODO Revisit this design. It may make sense to walk those nodes
//      only once.

// According to the document:
// "The alignment factor (in bytes) that is used to align the raw data of sections in
//  the image file. The value should be a power of 2 between 512 and 64 K, inclusive."

```

In both of these, the last line is indented, making it a code block. The fix is to unindent the lines.

Another common mistake is not indenting a wrapped indented line of a list or code block. For example:

```go
// Uses of this error model include:
//
//   - Partial errors. If a service needs to return partial errors to the
// client,
//     it may embed the `Status` in the normal response to indicate the
// partial
//     errors.
//
//   - Workflow errors. A typical workflow has multiple steps. Each step
// may
//     have a `Status` message for error reporting.

```

The fix is to indent the wrapped lines.

Go doc comments do not support nested lists, so gofmt reformats

```go
// Here is a list:
//
//  - Item 1.
//    * Subitem 1.
//    * Subitem 2.
//  - Item 2.
//  - Item 3.

```

to

```go
// Here is a list:
//
//  - Item 1.
//  - Subitem 1.
//  - Subitem 2.
//  - Item 2.
//  - Item 3.

```

Rewriting the text to avoid nested lists usually improves the documentation and is the best solution. Another potential workaround is to mix list markers, since bullet markers do not introduce list items in a numbered list, nor vice versa. For example:

```go
// Here is a list:
//
//  1. Item 1.
//
//     - Subitem 1.
//
//     - Subitem 2.
//
//  2. Item 2.
//
//  3. Item 3.

```
