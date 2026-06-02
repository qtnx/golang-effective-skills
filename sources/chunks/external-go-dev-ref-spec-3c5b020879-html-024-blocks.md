---
source_name: "External Linked Documentation"
source_url: "https://go.dev/ref/spec"
source_path: "sources/raw/external/go-dev-ref-spec-3c5b020879.html"
license_ref: ""
---

# The Go Programming Language Specification

## Blocks

 A _block_ is a possibly empty sequence of declarations and statements within matching brace brackets.

```go

Block         = "{" StatementList "}" .
StatementList = { Statement ";" } .

```

 In addition to explicit blocks in the source code, there are implicit blocks:

- The _universe block_ encompasses all Go source text.
- Each package has a _package block_ containing all Go source text for that package.
- Each file has a _file block_ containing all Go source text in that file.
- Each "if", "for", and "switch" statement is considered to be in its own implicit block.
- Each clause in a "switch" or "select" statement acts as an implicit block.

 Blocks nest and influence scoping.
