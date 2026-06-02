---
source_name: "External Linked Documentation"
source_url: "https://go.dev/design/43651-type-parameters"
source_path: "sources/raw/external/go-dev-design-43651-type-parameters-8b418b79f1.html"
license_ref: ""
---

## Design

### Values of type parameters are not boxed

In the current implementations of Go, interface values always hold pointers. Putting a non-pointer value in an interface variable causes the value to be _boxed_. That means that the actual value is stored somewhere else, on the heap or stack, and the interface value holds a pointer to that location.

In this design, values of generic types are not boxed. For example, let's look back at our earlier example of `FromStrings2`. When it is instantiated with type `Settable`, it returns a value of type `[]Settable`. For example, we can write

```go
// Settable is an integer type that can be set from a string.
type Settable int

// Set sets the value of *p from a string.
func (p *Settable) Set(s string) {
	// same as above
}

func F() {
	// The type of nums is []Settable.
	nums := FromStrings2[Settable]([]string{"1", "2"})
	// Settable can be converted directly to int.
	// This will set first to 1.
	first := int(nums[0])
	...
}

```

When we call `FromStrings2` instantiated with the type `Settable` we get back a `[]Settable`. The elements of that slice will be `Settable` values, which is to say, they will be integers. They will not be boxed, even though they were created and set by a generic function.

Similarly, when a generic type is instantiated it will have the expected types as components.

```go
type Pair[F1, F2 any] struct {
	first  F1
	second F2
}

```

When this is instantiated, the fields will not be boxed, and no unexpected memory allocations will occur. The type `Pair[int, string]` is convertible to `struct { first int; second string }`.
