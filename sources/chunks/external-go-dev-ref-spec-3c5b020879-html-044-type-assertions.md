---
source_name: "External Linked Documentation"
source_url: "https://go.dev/ref/spec"
source_path: "sources/raw/external/go-dev-ref-spec-3c5b020879.html"
license_ref: ""
---

## Expressions

### Type assertions

 For an expression `x` of interface type, but not a type parameter, and a type `T`, the primary expression

```go

x.(T)

```

 asserts that `x` is not `nil` and that the value stored in `x` is of type `T`. The notation `x.(T)` is called a _type assertion_.

 More precisely, if `T` is not an interface type, `x.(T)` asserts that the dynamic type of `x` is identical to the type `T`. In this case, `T` must implement the (interface) type of `x`; otherwise the type assertion is invalid since it is not possible for `x` to store a value of type `T`. If `T` is an interface type, `x.(T)` asserts that the dynamic type of `x` implements the interface `T`.

 If the type assertion holds, the value of the expression is the value stored in `x` and its type is `T`. If the type assertion is false, a run-time panic occurs. In other words, even though the dynamic type of `x` is known only at run time, the type of `x.(T)` is known to be `T` in a correct program.

```go

var x interface{} = 7          // x has dynamic type int and value 7
i := x.(int)                   // i has type int and value 7

type I interface { m() }

func f(y I) {
	s := y.(string)        // illegal: string does not implement I (missing method m)
	r := y.(io.Reader)     // r has type io.Reader and the dynamic type of y must implement both I and io.Reader
	…
}

```

 A type assertion used in an assignment statement or initialization of the special form

```go

v, ok = x.(T)
v, ok := x.(T)
var v, ok = x.(T)
var v, ok interface{} = x.(T) // dynamic types of v and ok are T and bool

```

 yields an additional untyped boolean value. The value of `ok` is `true` if the assertion holds. Otherwise it is `false` and the value of `v` is the zero value for type `T`. No run-time panic occurs in this case.
