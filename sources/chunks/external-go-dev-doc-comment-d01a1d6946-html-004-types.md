---
source_name: "External Linked Documentation"
source_url: "https://go.dev/doc/comment"
source_path: "sources/raw/external/go-dev-doc-comment-d01a1d6946.html"
license_ref: ""
---

# Go Doc Comments

## Types

A type’s doc comment should explain what each instance of that type represents or provides. If the API is simple, the doc comment can be quite short. For example:

```go
package zip

// A Reader serves content from a ZIP archive.
type Reader struct {
    ...
}

```

By default, programmers should expect that a type is safe for use only by a single goroutine at a time. If a type provides stronger guarantees, the doc comment should state them. For example:

```go
package regexp

// Regexp is the representation of a compiled regular expression.
// A Regexp is safe for concurrent use by multiple goroutines,
// except for configuration methods, such as Longest.
type Regexp struct {
    ...
}

```

Go types should also aim to make the zero value have a useful meaning. If it isn’t obvious, that meaning should be documented. For example:

```go
package bytes

// A Buffer is a variable-sized buffer of bytes with Read and Write methods.
// The zero value for Buffer is an empty buffer ready to use.
type Buffer struct {
    ...
}

```

For a struct with exported fields, either the doc comment or per-field comments should explain the meaning of each exported field. For example, this type’s doc comment explains the fields:

```go
package io

// A LimitedReader reads from R but limits the amount of
// data returned to just N bytes. Each call to Read
// updates N to reflect the new amount remaining.
// Read returns EOF when N <= 0.
type LimitedReader struct {
    R   Reader // underlying reader
    N   int64  // max bytes remaining
}

```

In contrast, this type’s doc comment leaves the explanations to per-field comments:

```go
package comment

// A Printer is a doc comment printer.
// The fields in the struct can be filled in before calling
// any of the printing methods
// in order to customize the details of the printing process.
type Printer struct {
    // HeadingLevel is the nesting level used for
    // HTML and Markdown headings.
    // If HeadingLevel is zero, it defaults to level 3,
    // meaning to use <h3> and ###.
    HeadingLevel int
    ...
}

```

As with packages (above) and funcs (below), doc comments for types start with complete sentences naming the declared symbol. An explicit subject often makes the wording clearer, and it makes the text easier to search, whether on a web page or a command line. For example:

```go
$ go doc -all regexp | grep pairs
pairs within the input string: result[2*n:2*n+2] identifies the indexes
    FindReaderSubmatchIndex returns a slice holding the index pairs identifying
    FindStringSubmatchIndex returns a slice holding the index pairs identifying
    FindSubmatchIndex returns a slice holding the index pairs identifying the
$

```
