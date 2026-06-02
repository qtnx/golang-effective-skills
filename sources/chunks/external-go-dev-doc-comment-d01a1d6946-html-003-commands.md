---
source_name: "External Linked Documentation"
source_url: "https://go.dev/doc/comment"
source_path: "sources/raw/external/go-dev-doc-comment-d01a1d6946.html"
license_ref: ""
---

# Go Doc Comments

## Commands

A package comment for a command is similar, but it describes the behavior of the program rather than the Go symbols in the package. The first sentence conventionally begins with the name of the program itself, capitalized because it is at the start of a sentence. For example, here is an abridged version of the package comment for gofmt:

```go
/*
Gofmt formats Go programs.
It uses tabs for indentation and blanks for alignment.
Alignment assumes that an editor is using a fixed-width font.

Without an explicit path, it processes the standard input. Given a file,
it operates on that file; given a directory, it operates on all .go files in
that directory, recursively. (Files starting with a period are ignored.)
By default, gofmt prints the reformatted sources to standard output.

Usage:

    gofmt [flags] [path ...]

The flags are:

    -d
        Do not print reformatted sources to standard output.
        If a file's formatting is different than gofmt's, print diffs
        to standard output.
    -w
        Do not print reformatted sources to standard output.
        If a file's formatting is different from gofmt's, overwrite it
        with gofmt's version. If an error occurred during overwriting,
        the original file is restored from an automatic backup.

When gofmt reads from standard input, it accepts either a full Go program
or a program fragment. A program fragment must be a syntactically
valid declaration list, statement list, or expression. When formatting
such a fragment, gofmt preserves leading indentation as well as leading
and trailing spaces, so that individual sections of a Go program can be
formatted by piping them through gofmt.
*/
package main

```

The beginning of the comment is written using semantic linefeeds <https://rhodesmill.org/brandon/2012/one-sentence-per-line/>, in which each new sentence or long phrase is on a line by itself, which can make diffs easier to read as code and comments evolve. The later paragraphs happen not to follow this convention and have been wrapped by hand. Whatever is best for your code base is fine. Either way, `go` `doc` and `pkgsite` rewrap doc comment text when printing it. For example:

```go
$ go doc gofmt
Gofmt formats Go programs. It uses tabs for indentation and blanks for
alignment. Alignment assumes that an editor is using a fixed-width font.

Without an explicit path, it processes the standard input. Given a file, it
operates on that file; given a directory, it operates on all .go files in that
directory, recursively. (Files starting with a period are ignored.) By default,
gofmt prints the reformatted sources to standard output.

Usage:

    gofmt [flags] [path ...]

The flags are:

    -d
        Do not print reformatted sources to standard output.
        If a file's formatting is different than gofmt's, print diffs
        to standard output.
...

```

The indented lines are treated as preformatted text: they are not rewrapped and are printed in code font in HTML and Markdown presentations. (The Syntax section below gives the details.)
