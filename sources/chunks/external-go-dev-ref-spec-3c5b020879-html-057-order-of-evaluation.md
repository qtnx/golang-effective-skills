---
source_name: "External Linked Documentation"
source_url: "https://go.dev/ref/spec"
source_path: "sources/raw/external/go-dev-ref-spec-3c5b020879.html"
license_ref: ""
---

## Expressions

### Order of evaluation

 At package level, initialization dependencies determine the evaluation order of individual initialization expressions in variable declarations. Otherwise, when evaluating the operands of an expression, assignment, or return statement, all function calls, method calls, receive operations, and binary logical operations are evaluated in lexical left-to-right order.

 For example, in the (function-local) assignment

```go

y[f()], ok = g(z || h(), i()+x[j()], <-c), k()

```

 the function calls and communication happen in the order `f()`, `h()` (if `z` evaluates to false), `i()`, `j()`, `<-c`, `g()`, and `k()`. However, the order of those events compared to the evaluation and indexing of `x` and the evaluation of `y` and `z` is not specified, except as required lexically. For instance, `g` cannot be called before its arguments are evaluated.

```go

a := 1
f := func() int { a++; return a }
x := []int{a, f()}            // x may be [1, 2] or [2, 2]: evaluation order between a and f() is not specified
m := map[int]int{a: 1, a: 2}  // m may be {2: 1} or {2: 2}: evaluation order between the two map assignments is not specified
n := map[int]int{a: f()}      // n may be {2: 3} or {3: 3}: evaluation order between the key and the value is not specified

```

 At package level, initialization dependencies override the left-to-right rule for individual initialization expressions, but not for operands within each expression:

```go

var a, b, c = f() + v(), g(), sqr(u()) + v()

func f() int        { return c }
func g() int        { return a }
func sqr(x int) int { return x*x }

// functions u and v are independent of all other variables and functions

```

 The function calls happen in the order `u()`, `sqr()`, `v()`, `f()`, `v()`, and `g()`.

 Floating-point operations within a single expression are evaluated according to the associativity of the operators. Explicit parentheses affect the evaluation by overriding the default associativity. In the expression `x + (y + z)` the addition `y + z` is performed before adding `x`.
