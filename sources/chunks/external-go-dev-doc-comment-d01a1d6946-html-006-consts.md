---
source_name: "External Linked Documentation"
source_url: "https://go.dev/doc/comment"
source_path: "sources/raw/external/go-dev-doc-comment-d01a1d6946.html"
license_ref: ""
---

# Go Doc Comments

## Consts

Go’s declaration syntax allows grouping of declarations, in which case a single doc comment can introduce a group of related constants, with individual constants only documented by short end-of-line comments. For example:

```go
package scanner // import "text/scanner"

// The result of Scan is one of these tokens or a Unicode character.
const (
    EOF = -(iota + 1)
    Ident
    Int
    Float
    Char
    ...
)

```

Sometimes the group needs no doc comment at all. For example:

```go
package unicode // import "unicode"

const (
    MaxRune         = '\U0010FFFF' // maximum valid Unicode code point.
    ReplacementChar = '\uFFFD'     // represents invalid code points.
    MaxASCII        = '\u007F'     // maximum ASCII value.
    MaxLatin1       = '\u00FF'     // maximum Latin-1 value.
)

```

On the other hand, ungrouped constants typically warrant a full doc comment starting with a complete sentence. For example:

```go
package unicode

// Version is the Unicode edition from which the tables are derived.
const Version = "13.0.0"

```

Typed constants are displayed next to the declaration of their type and as a result often omit a const group doc comment in favor of the type’s doc comment. For example:

```go
package syntax

// An Op is a single regular expression operator.
type Op uint8

const (
    OpNoMatch        Op = 1 + iota // matches no strings
    OpEmptyMatch                   // matches empty string
    OpLiteral                      // matches Runes sequence
    OpCharClass                    // matches Runes interpreted as range pair list
    OpAnyCharNotNL                 // matches any character except newline
    ...
)

```

(See pkg.go.dev/regexp/syntax#Op <https://pkg.go.dev/regexp/syntax#Op> for the HTML presentation.)
