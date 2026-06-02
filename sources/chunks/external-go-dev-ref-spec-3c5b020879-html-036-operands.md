---
source_name: "External Linked Documentation"
source_url: "https://go.dev/ref/spec"
source_path: "sources/raw/external/go-dev-ref-spec-3c5b020879.html"
license_ref: ""
---

## Expressions
 An expression specifies the computation of a value by applying operators and functions to operands.
### Operands

 Operands denote the elementary values in an expression. An operand may be a literal, a (possibly qualified) non-blank identifier denoting a constant, variable, or function, or a parenthesized expression.

```go

Operand     = Literal | OperandName [ TypeArgs ] | "(" Expression ")" .
Literal     = BasicLit | CompositeLit | FunctionLit .
BasicLit    = int_lit | float_lit | imaginary_lit | rune_lit | string_lit .
OperandName = identifier | QualifiedIdent .

```

 An operand name denoting a generic function may be followed by a list of type arguments; the resulting operand is an instantiated function.

 The blank identifier may appear as an operand only on the left-hand side of an assignment statement.

 Implementation restriction: A compiler need not report an error if an operand's type is a type parameter with an empty type set. Functions with such type parameters cannot be instantiated; any attempt will lead to an error at the instantiation site.
