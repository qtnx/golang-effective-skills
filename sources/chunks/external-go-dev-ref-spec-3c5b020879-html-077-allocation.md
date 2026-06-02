---
source_name: "External Linked Documentation"
source_url: "https://go.dev/ref/spec"
source_path: "sources/raw/external/go-dev-ref-spec-3c5b020879.html"
license_ref: ""
---

## Built-in functions

### Allocation

 The built-in function `new` creates a new, initialized variable and returns a pointer to it. It accepts a single argument, which may be either a type or an expression.

 If the argument is a type `T`, then `new(T)` allocates a variable of type `T` initialized to its zero value.

 If the argument is an expression `x`, then `new(x)` allocates a variable of the type of `x` initialized to the value of `x`. If that value is an untyped constant, it is first implicitly converted to its default type; if it is an untyped boolean value, it is first implicitly converted to type bool. The predeclared identifier `nil` cannot be used as an argument to `new`.

 For example, `new(int)` and `new(123)` each return a pointer to a new variable of type `int`. The value of the first variable is `0`, and the value of the second is `123`. Similarly

```go

type S struct { a int; b float64 }
new(S)

```

 allocates a variable of type `S`, initializes it (`a=0`, `b=0.0`), and returns a value of type `*S` containing the address of the variable.
