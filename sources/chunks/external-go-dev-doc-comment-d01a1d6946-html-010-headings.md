---
source_name: "External Linked Documentation"
source_url: "https://go.dev/doc/comment"
source_path: "sources/raw/external/go-dev-doc-comment-d01a1d6946.html"
license_ref: ""
---

## Syntax

### Headings

A heading is a line beginning with a number sign (U+0023) and then a space and the heading text. To be recognized as a heading, the line must be unindented and set off from adjacent paragraph text by blank lines.

For example:

```go
// Package strconv implements conversions to and from string representations
// of basic data types.
//
// # Numeric Conversions
//
// The most common numeric conversions are [Atoi] (string to int) and [Itoa] (int to string).
...
package strconv

```

On the other hand:

```go
// #This is not a heading, because there is no space.
//
// # This is not a heading,
// # because it is multiple lines.
//
// # This is not a heading,
// because it is also multiple lines.
//
// The next paragraph is not a heading, because there is no additional text:
//
// #
//
// In the middle of a span of non-blank lines,
// # this is not a heading either.
//
//     # This is not a heading, because it is indented.

```

The # syntax was added in Go 1.19. Before Go 1.19, headings were identified implicitly by single-line paragraphs satisfying certain conditions, most notably the lack of any terminating punctuation.

Gofmt reformats lines treated as implicit headings <https://github.com/golang/proposal/blob/master/design/51082-godocfmt.md#headings> by earlier versions of Go to use # headings instead. If the reformatting is not appropriate—that is, if the line was not meant to be a heading—the easiest way to make it a paragraph is to introduce terminating punctuation such as a period or colon, or to break it into two lines.
