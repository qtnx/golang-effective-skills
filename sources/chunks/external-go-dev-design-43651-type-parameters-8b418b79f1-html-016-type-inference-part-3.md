---
source_name: "External Linked Documentation"
source_url: "https://go.dev/design/43651-type-parameters"
source_path: "sources/raw/external/go-dev-design-43651-type-parameters-8b418b79f1.html"
license_ref: ""
---

## Design

// FromStrings2 takes a slice of strings and returns a slice of T,
// calling the Set method to set each returned value.
//
// We use two different type parameters so that we can return
// a slice of type T but call methods on *T aka PT.
// The Setter2 constraint ensures that PT is a pointer to T.
func FromStrings2[T any, PT Setter2[T]](s []string) []T {
	result := make([]T, len(s))
	for i, v := range s {
		// The type of &result[i] is *T which is in the type set
		// of Setter2, so we can convert it to PT.
		p := PT(&result[i])
		// PT has a Set method.
		p.Set(v)
	}
	return result
}

```

We can then call `FromStrings2` like this:

```go
func F2() {
	// FromStrings2 takes two type parameters.
	// The second parameter must be a pointer to the first.
	// Settable is as above.
	nums := FromStrings2[Settable, *Settable]([]string{"1", "2"})
	// Now nums is []Settable{1, 2}.
	...
}

```

This approach works as expected, but it is awkward to have to repeat `Settable` in the type arguments. Fortunately, constraint type inference makes it less awkward. Using constraint type inference we can write

```go
func F3() {
	// Here we just pass one type argument.
	nums := FromStrings2[Settable]([]string{"1", "2"})
	// Now nums is []Settable{1, 2}.
	...
}

```

There is no way to avoid passing the type argument `Settable`. But given that type argument, constraint type inference can infer the type argument `*Settable` for the type parameter `PT`.

As before, we create a mapping of known type arguments:

```go
{T -> Settable}

```

We then unify each type parameter with a structural constraint. In this case, we unify `PT` with the single type of `Setter2[T]`, which is `*T`. The mapping is now

```go
{T -> Settable, PT -> *T}

```

We then replace `T` with `Settable` throughout, giving us:

```go
{T -> Settable, PT -> *Settable}

```

After this nothing changes, and we are done. Both type arguments are known.

This example shows how we can use constraint type inference to apply a constraint to a type that is based on some other type parameter. In this case we are saying that `PT`, which is `*T`, must have a `Set` method. We can do this without requiring the caller to explicitly mention `*T`.
Constraints apply even after constraint type inference
Even when constraint type inference is used to infer type arguments based on constraints, we must still check the constraints after the type arguments are determined.

In the `FromStrings2` example above, we were able to deduce the type argument for `PT` based on the `Setter2` constraint. But in doing so we only looked at the type set, we didn't look at the methods. We still have to verify that the method is there, satisfying the constraint, even if constraint type inference succeeds.

For example, consider this invalid code:

```go
// Unsettable is a type that does not have a Set method.
type Unsettable int

func F4() {
	// This call is INVALID.
	nums := FromStrings2[Unsettable]([]string{"1", "2"})
	...
}

```

When this call is made, we will apply constraint type inference just as before. It will succeed, just as before, and infer that the type arguments are `[Unsettable, *Unsettable]`. Only after constraint type inference is complete will we check whether `*Unsettable` implements the constraint `Setter2[Unsettable]`. Since `*Unsettable` does not have a `Set` method, constraint checking will fail, and this code will not compile.
