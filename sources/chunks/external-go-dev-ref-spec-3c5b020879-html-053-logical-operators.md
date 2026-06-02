---
source_name: "External Linked Documentation"
source_url: "https://go.dev/ref/spec"
source_path: "sources/raw/external/go-dev-ref-spec-3c5b020879.html"
license_ref: ""
---

## Expressions

### Logical operators

 Logical operators apply to boolean values and yield a result of the same type as the operands. The left operand is evaluated, and then the right if the condition requires it.

```go

&&    conditional AND    p && q  is  "if p then q else false"
||    conditional OR     p || q  is  "if p then true else q"
!     NOT                !p      is  "not p"

```

## Expressions

### Address operators

 For an operand `x` of type `T`, the address operation `&x` generates a pointer of type `*T` to `x`. The operand must be _addressable_, that is, either a variable, pointer indirection, or slice indexing operation; or a field selector of an addressable struct operand; or an array indexing operation of an addressable array. As an exception to the addressability requirement, `x` may also be a (possibly parenthesized) composite literal. If the evaluation of `x` would cause a run-time panic, then the evaluation of `&x` does too.

 For an operand `x` of pointer type `*T`, the pointer indirection `*x` denotes the variable of type `T` pointed to by `x`. If `x` is `nil`, an attempt to evaluate `*x` will cause a run-time panic.

```go

&x
&a[f(2)]
&Point{2, 3}
*p
*pf(x)

var x *int = nil
*x   // causes a run-time panic
&*x  // causes a run-time panic

```
