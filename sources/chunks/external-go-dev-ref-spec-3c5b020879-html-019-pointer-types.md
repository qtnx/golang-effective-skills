---
source_name: "External Linked Documentation"
source_url: "https://go.dev/ref/spec"
source_path: "sources/raw/external/go-dev-ref-spec-3c5b020879.html"
license_ref: ""
---

## Types

### Pointer types

 A pointer type denotes the set of all pointers to variables of a given type, called the _base type_ of the pointer. The value of an uninitialized pointer is `nil`.

```go

PointerType = "*" BaseType .
BaseType    = Type .

```

```go

*Point
*[4]int

```

## Types

### Function types

 A function type denotes the set of all functions with the same parameter and result types. The value of an uninitialized variable of function type is `nil`.

```go

FunctionType  = "func" Signature .
Signature     = Parameters [ Result ] .
Result        = Parameters | Type .
Parameters    = "(" [ ParameterList [ "," ] ] ")" .
ParameterList = ParameterDecl { "," ParameterDecl } .
ParameterDecl = [ IdentifierList ] [ "..." ] Type .

```

 Within a list of parameters or results, the names (IdentifierList) must either all be present or all be absent. If present, each name stands for one item (parameter or result) of the specified type and all non-blank names in the signature must be unique. If absent, each type stands for one item of that type. Parameter and result lists are always parenthesized except that if there is exactly one unnamed result it may be written as an unparenthesized type.

 The final incoming parameter in a function signature may have a type prefixed with `...`. A function with such a parameter is called _variadic_ and may be invoked with zero or more arguments for that parameter.

```go

func()
func(x int) int
func(a, _ int, z float32) bool
func(a, b int, z float32) (bool)
func(prefix string, values ...int)
func(a, b int, z float64, opt ...interface{}) (success bool)
func(int, int, float64) (float64, *[]int)
func(n int) func(p *T)

```
