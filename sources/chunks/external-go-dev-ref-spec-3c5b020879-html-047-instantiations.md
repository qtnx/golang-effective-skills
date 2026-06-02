---
source_name: "External Linked Documentation"
source_url: "https://go.dev/ref/spec"
source_path: "sources/raw/external/go-dev-ref-spec-3c5b020879.html"
license_ref: ""
---

## Expressions

### Instantiations

 A generic function or type is _instantiated_ by substituting _type arguments_ for the type parameters [Go 1.18]. Instantiation proceeds in two steps:

-  Each type argument is substituted for its corresponding type parameter in the generic declaration. This substitution happens across the entire function or type declaration, including the type parameter list itself and any types in that list.
-  After substitution, each type argument must satisfy the constraint (instantiated, if necessary) of the corresponding type parameter. Otherwise instantiation fails.

 Instantiating a type results in a new non-generic named type; instantiating a function produces a new non-generic function.

```go

type parameter list    type arguments    after substitution

[P any]                int               int satisfies any
[S ~[]E, E any]        []int, int        []int satisfies ~[]int, int satisfies any
[P io.Writer]          string            illegal: string doesn't satisfy io.Writer
[P comparable]         any               any satisfies (but does not implement) comparable

```

 When using a generic function, type arguments may be provided explicitly, or they may be partially or completely inferred from the context in which the function is used. Provided that they can be inferred, type argument lists may be omitted entirely if the function is:

-  called with ordinary arguments,
-  assigned to a variable with a known type
-  passed as an argument to another function, or
-  returned as a result.

 In all other cases, a (possibly partial) type argument list must be present. If a type argument list is absent or partial, all missing type arguments must be inferrable from the context in which the function is used.

```go

// sum returns the sum (concatenation, for strings) of its arguments.
func sum[T ~int | ~float64 | ~string](x... T) T { … }

x := sum                       // illegal: the type of x is unknown
intSum := sum[int]             // intSum has type func(x... int) int
a := intSum(2, 3)              // a has value 5 of type int
b := sum[float64](2.0, 3)      // b has value 5.0 of type float64
c := sum(b, -1)                // c has value 4.0 of type float64

type sumFunc func(x... string) string
var f sumFunc = sum            // same as var f sumFunc = sum[string]
f = sum                        // same as f = sum[string]

```

 A partial type argument list cannot be empty; at least the first argument must be present. The list is a prefix of the full list of type arguments, leaving the remaining arguments to be inferred. Loosely speaking, type arguments may be omitted from "right to left".

```go

func apply[S ~[]E, E any](s S, f func(E) E) S { … }

f0 := apply[]                  // illegal: type argument list cannot be empty
f1 := apply[[]int]             // type argument for S explicitly provided, type argument for E inferred
f2 := apply[[]string, string]  // both type arguments explicitly provided

var bytes []byte
r := apply(bytes, func(byte) byte { … })  // both type arguments inferred from the function arguments

```

 For a generic type, all type arguments must always be provided explicitly.
