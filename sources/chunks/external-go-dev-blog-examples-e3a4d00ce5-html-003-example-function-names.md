---
source_name: "External Linked Documentation"
source_url: "https://go.dev/blog/examples"
source_path: "sources/raw/external/go-dev-blog-examples-e3a4d00ce5.html"
license_ref: ""
---

# The Go Blog

## Example function names

Godoc uses a naming convention to associate an example function with a package-level identifier.

```go
func ExampleFoo()     // documents the Foo function or type
func ExampleBar_Qux() // documents the Qux method of type Bar
func Example()        // documents the package as a whole

```

Following this convention, godoc displays the `ExampleString` example alongside the documentation for the `String` function.

Multiple examples can be provided for a given identifier by using a suffix beginning with an underscore followed by a lowercase letter. Each of these examples documents the `String` function:

```go
func ExampleString()
func ExampleString_second()
func ExampleString_third()

```

# The Go Blog

## Larger examples

Sometimes we need more than just a function to write a good example.

For instance, to demonstrate the `sort` package we should show an implementation of `sort.Interface`. Since methods cannot be declared inside a function body, the example must include some context in addition to the example function.

To achieve this we can use a “whole file example.” A whole file example is a file that ends in `_test.go` and contains exactly one example function, no test or benchmark functions, and at least one other package-level declaration. When displaying such examples godoc will show the entire file.

Here is a whole file example from the `sort` package:

```go
package sort_test

import (
    "fmt"
    "sort"
)

type Person struct {
    Name string
    Age  int
}

func (p Person) String() string {
    return fmt.Sprintf("%s: %d", p.Name, p.Age)
}

// ByAge implements sort.Interface for []Person based on
// the Age field.
type ByAge []Person

func (a ByAge) Len() int           { return len(a) }
func (a ByAge) Swap(i, j int)      { a[i], a[j] = a[j], a[i] }
func (a ByAge) Less(i, j int) bool { return a[i].Age < a[j].Age }

func Example() {
    people := []Person{
        {"Bob", 31},
        {"John", 42},
        {"Michael", 17},
        {"Jenny", 26},
    }

    fmt.Println(people)
    sort.Sort(ByAge(people))
    fmt.Println(people)

    // Output:
    // [Bob: 31 John: 42 Michael: 17 Jenny: 26]
    // [Michael: 17 Jenny: 26 Bob: 31 John: 42]
}

```

A package can contain multiple whole file examples; one example per file. Take a look at the `sort` package’s source code to see this in practice.

# The Go Blog

## Conclusion

Godoc examples are a great way to write and maintain code as documentation. They also present editable, working, runnable examples your users can build on. Use them!

 **Next article: **GopherChina Trip Report
 **Previous article: **Package names
 **Blog Index**
