---
source_name: "External Linked Documentation"
source_url: "https://go.dev/doc/tutorial/generics"
source_path: "sources/raw/external/go-dev-doc-tutorial-generics-36804f0219.html"
license_ref: ""
---

# Tutorial: Getting started with generics

## Remove type arguments when calling the generic function

In this section, you’ll add a modified version of the generic function call, making a small change to simplify the calling code. You’ll remove the type arguments, which aren’t needed in this case.

You can omit type arguments in calling code when the Go compiler can infer the types you want to use. The compiler infers type arguments from the types of function arguments.

Note that this isn’t always possible. For example, if you needed to call a generic function that had no arguments, you would need to include the type arguments in the function call.

#### Write the code

-
In main.go, beneath the code you already have, paste the following code.

```go
fmt.Printf("Generic Sums, type parameters inferred: %v and %v\n",
    SumIntsOrFloats(ints),
    SumIntsOrFloats(floats))

```

In this code, you:

- Call the generic function, omitting the type arguments.

#### Run the code

From the command line in the directory containing main.go, run the code.

```go
$ go run .
Non-Generic Sums: 46 and 62.97
Generic Sums: 46 and 62.97
Generic Sums, type parameters inferred: 46 and 62.97

```

Next, you’ll further simplify the function by capturing the union of integers and floats into a type constraint you can reuse, such as from other code.
