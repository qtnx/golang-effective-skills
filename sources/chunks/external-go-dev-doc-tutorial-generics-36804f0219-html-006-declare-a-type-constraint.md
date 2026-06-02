---
source_name: "External Linked Documentation"
source_url: "https://go.dev/doc/tutorial/generics"
source_path: "sources/raw/external/go-dev-doc-tutorial-generics-36804f0219.html"
license_ref: ""
---

# Tutorial: Getting started with generics

## Declare a type constraint

In this last section, you’ll move the constraint you defined earlier into its own interface so that you can reuse it in multiple places. Declaring constraints in this way helps streamline code, such as when a constraint is more complex.

You declare a _type constraint_ as an interface. The constraint allows any type implementing the interface. For example, if you declare a type constraint interface with three methods, then use it with a type parameter in a generic function, type arguments used to call the function must have all of those methods.

Constraint interfaces can also refer to specific types, as you’ll see in this section.

#### Write the code

-
Just above `main`, immediately after the import statements, paste the following code to declare a type constraint.

```go
type Number interface {
    int64 | float64
}

```

In this code, you:

-
Declare the `Number` interface type to use as a type constraint.

-
Declare a union of `int64` and `float64` inside the interface.

Essentially, you’re moving the union from the function declaration into a new type constraint. That way, when you want to constrain a type parameter to either `int64` or `float64`, you can use this `Number` type constraint instead of writing out `int64 | float64`.

-
Beneath the functions you already have, paste the following generic `SumNumbers` function.

```go
// SumNumbers sums the values of map m. It supports both integers
// and floats as map values.
func SumNumbers[K comparable, V Number](m map[K]V) V {
    var s V
    for _, v := range m {
        s += v
    }
    return s
}

```

In this code, you:

- Declare a generic function with the same logic as the generic function you declared previously, but with the new interface type instead of the union as the type constraint. As before, you use the type parameters for the argument and return types.

-
In main.go, beneath the code you already have, paste the following code.

```go
fmt.Printf("Generic Sums with Constraint: %v and %v\n",
    SumNumbers(ints),
    SumNumbers(floats))

```

In this code, you:

-
Call `SumNumbers` with each map, printing the sum from the values of each.

As in the preceding section, you omit the type arguments (the type names in square brackets) in calls to the generic function. The Go compiler can infer the type argument from other arguments.

#### Run the code

From the command line in the directory containing main.go, run the code.

```go
$ go run .
Non-Generic Sums: 46 and 62.97
Generic Sums: 46 and 62.97
Generic Sums, type parameters inferred: 46 and 62.97
Generic Sums with Constraint: 46 and 62.97

```
