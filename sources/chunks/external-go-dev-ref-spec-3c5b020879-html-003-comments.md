---
source_name: "External Linked Documentation"
source_url: "https://go.dev/ref/spec"
source_path: "sources/raw/external/go-dev-ref-spec-3c5b020879.html"
license_ref: ""
---

## Lexical elements
### Comments

 Comments serve as program documentation. There are two forms:

-  _Line comments_ start with the character sequence `//` and stop at the end of the line.
-  _General comments_ start with the character sequence `/*` and stop with the first subsequent character sequence `*/`.

 A comment cannot start inside a rune or string literal, or inside a comment. A general comment containing no newlines acts like a space. Any other comment acts like a newline.

## Lexical elements

### Tokens

 Tokens form the vocabulary of the Go language. There are four classes: _identifiers_, _keywords_, _operators and punctuation_, and _literals_. _White space_, formed from spaces (U+0020), horizontal tabs (U+0009), carriage returns (U+000D), and newlines (U+000A), is ignored except as it separates tokens that would otherwise combine into a single token. Also, a newline or end of file may trigger the insertion of a semicolon. While breaking the input into tokens, the next token is the longest sequence of characters that form a valid token.
