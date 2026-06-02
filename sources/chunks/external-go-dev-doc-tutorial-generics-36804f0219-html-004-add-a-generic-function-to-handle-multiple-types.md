---
source_name: "External Linked Documentation"
source_url: "https://go.dev/doc/tutorial/generics"
source_path: "sources/raw/external/go-dev-doc-tutorial-generics-36804f0219.html"
license_ref: ""
---

# Tutorial: Getting started with generics

## Add a generic function to handle multiple types

In this section, you’ll add a single generic function that can receive a map containing either integer or float values, effectively replacing the two functions you just wrote with a single function.

To support values of either type, that single function will need a way to declare what types it supports. Calling code, on the other hand, will need a way to specify whether it is calling with an integer or float map.

To support this, you’ll write a function that declares _type parameters_ in addition to its ordinary function parameters. These type parameters make the function generic, enabling it to work with arguments of different types. You’ll call the function with _type arguments_ and ordinary function arguments.

Each type parameter has a _type constraint_ that acts as a kind of meta-type for the type parameter. Each type constraint specifies the permissible type arguments that calling code can use for the respective type parameter.

While a type parameter’s constraint typically represents a set of types, at compile time the type parameter stands for a single type – the type provided as a type argument by the calling code. If the type argument’s type isn’t allowed by the type parameter’s constraint, the code won’t compile.

Keep in mind that a type parameter must support all the operations the generic code is performing on it. For example, if your function’s code were to try to perform `string` operations (such as indexing) on a type parameter whose constraint included numeric types, the code wouldn’t compile.

In the code you’re about to write, you’ll use a constraint that allows either integer or float types.

#### Write the code

-
Beneath the two functions you added previously, paste the following generic function.

```go
// SumIntsOrFloats sums the values of map m. It supports both int64 and float64
// as types for map values.
func SumIntsOrFloats[K comparable, V int64 | float64](m map[K]V) V {
    var s V
    for _, v := range m {
        s += v
    }
    return s
}

```

In this code, you:

- Declare a `SumIntsOrFloats` function with two type parameters (inside the square brackets), `K` and `V`, and one argument that uses the type parameters, `m` of type `map[K]V`. The function returns a value of type `V`.
- Specify for the `K` type parameter the type constraint `comparable`. Intended specifically for cases like these, the `comparable` constraint is predeclared in Go. It allows any type whose values may be used as an operand of the comparison operators `==` and `!=`. Go requires that map keys be comparable. So declaring `K` as `comparable` is necessary so you can use `K` as the key in the map variable. It also ensures that calling code uses an allowable type for map keys.
- Specify for the `V` type parameter a constraint that is a union of two types: `int64` and `float64`. Using `|` specifies a union of the two types, meaning that this constraint allows either type. Either type will be permitted by the compiler as an argument in the calling code.
- Specify that the `m` argument is of type `map[K]V`, where `K` and `V` are the types already specified for the type parameters. Note that we know `map[K]V` is a valid map type because `K` is a comparable type. If we hadn’t declared `K` comparable, the compiler would reject the reference to `map[K]V`.

-
In main.go, beneath the code you already have, paste the following code.

```go
fmt.Printf("Generic Sums: %v and %v\n",
    SumIntsOrFloats[string, int64](ints),
    SumIntsOrFloats[string, float64](floats))

```

In this code, you:

-
Call the generic function you just declared, passing each of the maps you created.

-
Specify type arguments – the type names in square brackets – to be clear about the types that should replace type parameters in the function you’re calling.

As you’ll see in the next section, you can often omit the type arguments in the function call. Go can often infer them from your code.

-
Print the sums returned by the function.

#### Run the code

From the command line in the directory containing main.go, run the code.

```go
$ go run .
Non-Generic Sums: 46 and 62.97
Generic Sums: 46 and 62.97

```

To run your code, in each call the compiler replaced the type parameters with the concrete types specified in that call.

In calling the generic function you wrote, you specified type arguments that told the compiler what types to use in place of the function’s type parameters. As you’ll see in the next section, in many cases you can omit these type arguments because the compiler can infer them.
