---
source_name: "External Linked Documentation"
source_url: "https://go.dev/doc/tutorial/generics"
source_path: "sources/raw/external/go-dev-doc-tutorial-generics-36804f0219.html"
license_ref: ""
---

# Tutorial: Getting started with generics

## Add non-generic functions

In this step, you’ll add two functions that each add together the values of a map and return the total.

You’re declaring two functions instead of one because you’re working with two different types of maps: one that stores `int64` values, and one that stores `float64` values.

#### Write the code

-
Using your text editor, create a file called main.go in the generics directory. You’ll write your Go code in this file.

-
Into main.go, at the top of the file, paste the following package declaration.

```go
package main

```

A standalone program (as opposed to a library) is always in package `main`.

-
Beneath the package declaration, paste the following two function declarations.

```go
// SumInts adds together the values of m.
func SumInts(m map[string]int64) int64 {
    var s int64
    for _, v := range m {
        s += v
    }
    return s
}

// SumFloats adds together the values of m.
func SumFloats(m map[string]float64) float64 {
    var s float64
    for _, v := range m {
        s += v
    }
    return s
}

```

In this code, you:

- Declare two functions to add together the values of a map and return the sum.
- `SumFloats` takes a map of `string` to `float64` values.
- `SumInts` takes a map of `string` to `int64` values.

-
At the top of main.go, beneath the package declaration, paste the following `main` function to initialize the two maps and use them as arguments when calling the functions you declared in the preceding step.

```go
func main() {
    // Initialize a map for the integer values
    ints := map[string]int64{
        "first":  34,
        "second": 12,
    }

    // Initialize a map for the float values
    floats := map[string]float64{
        "first":  35.98,
        "second": 26.99,
    }

    fmt.Printf("Non-Generic Sums: %v and %v\n",
        SumInts(ints),
        SumFloats(floats))
}

```

In this code, you:

- Initialize a map of `float64` values and a map of `int64` values, each with two entries.
- Call the two functions you declared earlier to find the sum of each map’s values.
- Print the result.

-
Near the top of main.go, just beneath the package declaration, import the package you’ll need to support the code you’ve just written.

The first lines of code should look like this:

```go
package main

import "fmt"

```

-
Save main.go.

#### Run the code

From the command line in the directory containing main.go, run the code.

```go
$ go run .
Non-Generic Sums: 46 and 62.97

```

With generics, you can write one function here instead of two. Next, you’ll add a single generic function for maps containing either integer or float values.
