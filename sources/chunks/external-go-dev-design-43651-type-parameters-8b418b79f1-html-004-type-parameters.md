---
source_name: "External Linked Documentation"
source_url: "https://go.dev/design/43651-type-parameters"
source_path: "sources/raw/external/go-dev-design-43651-type-parameters-8b418b79f1.html"
license_ref: ""
---

## Design
We will describe the complete design in stages based on simple examples.
### Type parameters

Generic code is written using abstract data types that we call _type parameters_. When running the generic code, the type parameters are replaced by _type arguments_.

Here is a function that prints out each element of a slice, where the element type of the slice, here called `T`, is unknown. This is a trivial example of the kind of function we want to permit in order to support generic programming. (Later we'll also discuss generic types).

```go
// Print prints the elements of a slice.
// It should be possible to call this with any slice value.
func Print(s []T) { // Just an example, not the suggested syntax.
	for _, v := range s {
		fmt.Println(v)
	}
}

```

With this approach, the first decision to make is: how should the type parameter `T` be declared? In a language like Go, we expect every identifier to be declared in some way.

Here we make a design decision: type parameters are similar to ordinary non-type function parameters, and as such should be listed along with other parameters. However, type parameters are not the same as non-type parameters, so although they appear in the list of parameters we want to distinguish them. That leads to our next design decision: we define an additional optional parameter list describing type parameters.

This type parameter list appears before the regular parameters. To distinguish the type parameter list from the regular parameter list, the type parameter list uses square brackets rather than parentheses. Just as regular parameters have types, type parameters have meta-types, also known as constraints. We will discuss the details of constraints later; for now, we will just note that `any` is a valid constraint, meaning that any type is permitted.

```go
// Print prints the elements of any slice.
// Print has a type parameter T and has a single (non-type)
// parameter s which is a slice of that type parameter.
func Print[T any](s []T) {
	// same as above
}

```

This says that within the function `Print` the identifier `T` is a type parameter, a type that is currently unknown but that will be known when the function is called. The `any` means that `T` can be any type at all. As seen above, the type parameter may be used as a type when describing the types of the ordinary non-type parameters. It may also be used as a type within the body of the function.

Unlike regular parameter lists, in type parameter lists names are required for the type parameters. This avoids a syntactic ambiguity, and, as it happens, there is no reason to ever omit the type parameter names.

Since `Print` has a type parameter, any call of `Print` must provide a type argument. Later we will see how this type argument can usually be deduced from the non-type argument, by using type inference. For now, we'll pass the type argument explicitly. Type arguments are passed much like type parameters are declared: as a separate list of arguments. As with the type parameter list, the list of type arguments uses square brackets.

```go
	// Call Print with a []int.
	// Print has a type parameter T, and we want to pass a []int,
	// so we pass a type argument of int by writing Print[int].
	// The function Print[int] expects a []int as an argument.
	Print[int]([]int{1, 2, 3})

	// This will print:
	// 1
	// 2
	// 3

```
