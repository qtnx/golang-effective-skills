---
source_name: "External Linked Documentation"
source_url: "https://go.dev/ref/spec"
source_path: "sources/raw/external/go-dev-ref-spec-3c5b020879.html"
license_ref: ""
---

# The Go Programming Language Specification

## Source code representation

 Source code is Unicode text encoded in UTF-8 <https://en.wikipedia.org/wiki/UTF-8>. The text is not canonicalized, so a single accented code point is distinct from the same character constructed from combining an accent and a letter; those are treated as two code points. For simplicity, this document will use the unqualified term _character_ to refer to a Unicode code point in the source text.

 Each code point is distinct; for instance, uppercase and lowercase letters are different characters.

 Implementation restriction: For compatibility with other tools, a compiler may disallow the NUL character (U+0000) in the source text.

 Implementation restriction: For compatibility with other tools, a compiler may ignore a UTF-8-encoded byte order mark (U+FEFF) if it is the first Unicode code point in the source text. A byte order mark may be disallowed anywhere else in the source.

### Characters

 The following terms are used to denote specific Unicode character categories:

```go

newline        = /* the Unicode code point U+000A */ .
unicode_char   = /* an arbitrary Unicode code point except newline */ .
unicode_letter = /* a Unicode code point categorized as "Letter" */ .
unicode_digit  = /* a Unicode code point categorized as "Number, decimal digit" */ .

```

 In The Unicode Standard 8.0 <https://www.unicode.org/versions/Unicode8.0.0/>, Section 4.5 "General Category" defines a set of character categories. Go treats all characters in any of the Letter categories Lu, Ll, Lt, Lm, or Lo as Unicode letters, and those in the Number category Nd as Unicode digits.

### Letters and digits

 The underscore character `_` (U+005F) is considered a lowercase letter.

```go

letter        = unicode_letter | "_" .
decimal_digit = "0" … "9" .
binary_digit  = "0" | "1" .
octal_digit   = "0" … "7" .
hex_digit     = "0" … "9" | "A" … "F" | "a" … "f" .

```
