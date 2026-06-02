---
source_name: "External Linked Documentation"
source_url: "https://go.dev/ref/spec"
source_path: "sources/raw/external/go-dev-ref-spec-3c5b020879.html"
license_ref: ""
---

## Expressions

### Calls

 Given an expression `f` of function type `F`,

```go

f(a1, a2, … an)

```

 calls `f` with arguments `a1, a2, … an`. Except for one special case, arguments must be single-valued expressions assignable to the parameter types of `F` and are evaluated before the function is called. The type of the expression is the result type of `F`. A method invocation is similar but the method itself is specified as a selector upon a value of the receiver type for the method.

```go

math.Atan2(x, y)  // function call
var pt *Point
pt.Scale(3.5)     // method call with receiver pt

```

 If `f` denotes a generic function, it must be instantiated before it can be called or used as a function value.

 If the type of `f` is a type parameter, all types in its type set must have the same underlying type, which must be a function type, and the function call must be valid for that type.

 In a function call, the function value and arguments are evaluated in the usual order. After they are evaluated, new storage is allocated for the function's variables, which includes its parameters and results. Then, the arguments of the call are _passed_ to the function, which means that they are assigned to their corresponding function parameters, and the called function begins execution. The return parameters of the function are passed back to the caller when the function returns.

 Calling a `nil` function value causes a run-time panic.

 As a special case, if the return values of a function or method `g` are equal in number and individually assignable to the parameters of another function or method `f`, then the call `f(g(_parameters_of_g_))` will invoke `f` after passing the return values of `g` to the parameters of `f` in order. The call of `f` must contain no parameters other than the call of `g`, and `g` must have at least one return value. If `f` has a final `...` parameter, it is assigned the return values of `g` that remain after assignment of regular parameters.

```go

func Split(s string, pos int) (string, string) {
	return s[0:pos], s[pos:]
}

func Join(s, t string) string {
	return s + t
}

if Join(Split(value, len(value)/2)) != value {
	log.Panic("test fails")
}

```

 A method call `x.m()` is valid if the method set of (the type of) `x` contains `m` and the argument list can be assigned to the parameter list of `m`. If `x` is addressable and `&x`'s method set contains `m`, `x.m()` is shorthand for `(&x).m()`:

```go

var p Point
p.Scale(3.5)

```

 There is no distinct method type and there are no method literals.
