---
source_name: "External Linked Documentation"
source_url: "https://go.dev/design/43651-type-parameters"
source_path: "sources/raw/external/go-dev-design-43651-type-parameters-8b418b79f1.html"
license_ref: ""
---

## Design

### Defining constraints

Go already has a construct that is close to what we need for a constraint: an interface type. An interface type is a set of methods. The only values that can be assigned to a variable of interface type are those whose types implement the same methods. The only operations that can be done with a value of interface type, other than operations permitted for any type, are to call the methods.

Calling a generic function with a type argument is similar to assigning to a variable of interface type: the type argument must implement the constraints of the type parameter. Writing a generic function is like using values of interface type: the generic code can only use the operations permitted by the constraint (or operations that are permitted for any type).

Therefore, in this design, constraints are simply interface types. Satisfying a constraint means implementing the interface type. (Later we'll restate this in order to define constraints for operations other than method calls, such as binary operators).

For the `Stringify` example, we need an interface type with a `String` method that takes no arguments and returns a value of type `string`.

```go
// Stringer is a type constraint that requires the type argument to have
// a String method and permits the generic function to call String.
// The String method should return a string representation of the value.
type Stringer interface {
	String() string
}

```

(It doesn‘t matter for this discussion, but this defines the same interface as the standard library’s `fmt.Stringer` type, and real code would likely simply use `fmt.Stringer`.)
