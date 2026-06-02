---
source_name: "External Linked Documentation"
source_url: "https://go.dev/doc/comment"
source_path: "sources/raw/external/go-dev-doc-comment-d01a1d6946.html"
license_ref: ""
---

## Syntax

### Lists

A list is a span of indented or blank lines (which would otherwise be a code block, as described in the next section) in which the first indented line begins with a bullet list marker or a numbered list marker.

A bullet list marker is a star, plus, dash, or Unicode bullet (*, +, -, •; U+002A, U+002B, U+002D, U+2022) followed by a space or tab and then text. In a bullet list, each line beginning with a bullet list marker starts a new list item.

For example:

```go
package url

// PublicSuffixList provides the public suffix of a domain. For example:
//   - the public suffix of "example.com" is "com",
//   - the public suffix of "foo1.foo2.foo3.co.uk" is "co.uk", and
//   - the public suffix of "bar.pvt.k12.ma.us" is "pvt.k12.ma.us".
//
// Implementations of PublicSuffixList must be safe for concurrent use by
// multiple goroutines.
//
// An implementation that always returns "" is valid and may be useful for
// testing but it is not secure: it means that the HTTP server for foo.com can
// set a cookie for bar.com.
//
// A public suffix list implementation is in the package
// golang.org/x/net/publicsuffix.
type PublicSuffixList interface {
    ...
}

```

A numbered list marker is a decimal number of any length followed by a period or right parenthesis, then a space or tab, and then text. In a numbered list, each line beginning with a number list marker starts a new list item. Item numbers are left as is, never renumbered.

For example:

```go
package path

// Clean returns the shortest path name equivalent to path
// by purely lexical processing. It applies the following rules
// iteratively until no further processing can be done:
//
//  1. Replace multiple slashes with a single slash.
//  2. Eliminate each . path name element (the current directory).
//  3. Eliminate each inner .. path name element (the parent directory)
//     along with the non-.. element that precedes it.
//  4. Eliminate .. elements that begin a rooted path:
//     that is, replace "/.." by "/" at the beginning of a path.
//
// The returned path ends in a slash only if it is the root "/".
//
// If the result of this process is an empty string, Clean
// returns the string ".".
//
// See also Rob Pike, “[Lexical File Names in Plan 9].”
//
// [Lexical File Names in Plan 9]: https://9p.io/sys/doc/lexnames.html
func Clean(path string) string {
    ...
}

```

List items only contain paragraphs, not code blocks or nested lists. This avoids any space-counting subtlety as well as questions about how many spaces a tab counts for in inconsistent indentation.

Gofmt reformats bullet lists to use a dash as the bullet marker, two spaces of indentation before the dash, and four spaces of indentation for continuation lines.

Gofmt reformats numbered lists to use a single space before the number, a period after the number, and again four spaces of indentation for continuation lines.

Gofmt preserves but does not require a blank line between a list and the preceding paragraph. It inserts a blank line between a list and the following paragraph or heading.
