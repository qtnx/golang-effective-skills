---
source_name: "External Linked Documentation"
source_url: "https://go.dev/doc/comment"
source_path: "sources/raw/external/go-dev-doc-comment-d01a1d6946.html"
license_ref: ""
---

## Syntax

### Paragraphs

A paragraph is a span of unindented non-blank lines. We’ve already seen many examples of paragraphs.

A pair of consecutive backticks (` U+0060) is interpreted as a Unicode left quote (“ U+201C), and a pair of consecutive single quotes (' U+0027) is interpreted as a Unicode right quote (” U+201D).

Gofmt preserves line breaks in paragraph text: it does not rewrap the text. This allows the use of semantic linefeeds <https://rhodesmill.org/brandon/2012/one-sentence-per-line/>, as seen earlier. Gofmt replaces duplicated blank lines between paragraphs with a single blank line. Gofmt also reformats consecutive backticks or single quotes to their Unicode interpretations.

#### Notes

Notes are special comments of the form `MARKER(uid): body`. MARKER should consist of 2 or more upper case `[A-Z]` letters, identifying the type of note, while uid is at least 1 character, usually a username of someone who can provide more information. The `:` following the uid is optional.

Notes are collected and rendered in their own section on pkg.go.dev.

For example:

```go
// TODO(user1): refactor to use standard library context
// BUG(user2): not cleaned up
var ctx context.Context

```

#### Deprecations

Paragraphs starting with `Deprecated: ` are treated as deprecation notices. Some tools will warn when deprecated identifiers are used. pkg.go.dev <https://pkg.go.dev> will hide their docs by default.

Deprecation notices are followed by some information about the deprecation, and a recommendation on what to use instead, if applicable. The paragraph does not have to be the last paragraph in the doc comment.

For example:

```go
// Package rc4 implements the RC4 stream cipher.
//
// Deprecated: RC4 is cryptographically broken and should not be used
// except for compatibility with legacy systems.
//
// This package is frozen and no new functionality will be added.
package rc4

// Reset zeros the key data and makes the Cipher unusable.
//
// Deprecated: Reset can't guarantee that the key will be entirely removed from
// the process's memory.
func (c *Cipher) Reset()

```
