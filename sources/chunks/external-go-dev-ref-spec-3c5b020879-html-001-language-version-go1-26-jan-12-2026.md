---
source_name: "External Linked Documentation"
source_url: "https://go.dev/ref/spec"
source_path: "sources/raw/external/go-dev-ref-spec-3c5b020879.html"
license_ref: ""
---

# The Go Programming Language Specification

The Go Programming Language Specification - The Go Programming Language
# The Go Programming Language Specification
## Language version go1.26 (Jan 12, 2026)

# The Go Programming Language Specification

## Introduction

 This is the reference manual for the Go programming language. For more information and other documents, see go.dev.

 Go is a general-purpose language designed with systems programming in mind. It is strongly typed and garbage-collected and has explicit support for concurrent programming. Programs are constructed from _packages_, whose properties allow efficient management of dependencies.

 The syntax is compact and simple to parse, allowing for easy analysis by automatic tools such as integrated development environments.

# The Go Programming Language Specification

## Notation

 The syntax is specified using a variant <https://en.wikipedia.org/wiki/Wirth_syntax_notation> of Extended Backus-Naur Form (EBNF):

```go

Syntax      = { Production } .
Production  = production_name "=" [ Expression ] "." .
Expression  = Term { "|" Term } .
Term        = Factor { Factor } .
Factor      = production_name | token [ "…" token ] | Group | Option | Repetition .
Group       = "(" Expression ")" .
Option      = "[" Expression "]" .
Repetition  = "{" Expression "}" .

```

 Productions are expressions constructed from terms and the following operators, in increasing precedence:

```go

|   alternation
()  grouping
[]  option (0 or 1 times)
{}  repetition (0 to n times)

```

 Lowercase production names are used to identify lexical (terminal) tokens. Non-terminals are in CamelCase. Lexical tokens are enclosed in double quotes `""` or back quotes ````.

 The form `a … b` represents the set of characters from `a` through `b` as alternatives. The horizontal ellipsis `…` is also used elsewhere in the spec to informally denote various enumerations or code snippets that are not further specified. The character `…` (as opposed to the three characters `...`) is not a token of the Go language.

 A link of the form [Go 1.xx] indicates that a described language feature (or some aspect of it) was changed or added with language version 1.xx and thus requires at minimum that language version to build. For details, see the linked section in the appendix.
