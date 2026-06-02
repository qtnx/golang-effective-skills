---
source_name: "External Linked Documentation"
source_url: "https://go.dev/ref/spec"
source_path: "sources/raw/external/go-dev-ref-spec-3c5b020879.html"
license_ref: ""
---

## Expressions

### Function literals

 A function literal represents an anonymous function. Function literals cannot declare type parameters.

```go

FunctionLit = "func" Signature FunctionBody .

```

```go

func(a, b int, z float64) bool { return a*b < int(z) }

```

 A function literal can be assigned to a variable or invoked directly.

```go

f := func(x, y int) int { return x + y }
func(ch chan int) { ch <- ACK }(replyChan)

```

 Function literals are _closures_: they may refer to variables defined in a surrounding function. Those variables are then shared between the surrounding function and the function literal, and they survive as long as they are accessible.

## Expressions

### Primary expressions

 Primary expressions are the operands for unary and binary expressions.

```go

PrimaryExpr   = Operand |
                Conversion |
                MethodExpr |
                PrimaryExpr Selector |
                PrimaryExpr Index |
                PrimaryExpr Slice |
                PrimaryExpr TypeAssertion |
                PrimaryExpr Arguments .

Selector      = "." identifier .
Index         = "[" Expression [ "," ] "]" .
Slice         = "[" [ Expression ] ":" [ Expression ] "]" |
                "[" [ Expression ] ":" Expression ":" Expression "]" .
TypeAssertion = "." "(" Type ")" .
Arguments     = "(" [ ( ExpressionList | Type [ "," ExpressionList ] ) [ "..." ] [ "," ] ] ")" .

```

```go

x
2
(s + ".txt")
f(3.1415, true)
Point{1, 2}
m["foo"]
s[i : j + 1]
obj.color
f.p[i].x()

```
