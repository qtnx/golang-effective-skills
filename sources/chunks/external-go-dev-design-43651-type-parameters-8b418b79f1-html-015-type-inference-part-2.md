---
source_name: "External Linked Documentation"
source_url: "https://go.dev/design/43651-type-parameters"
source_path: "sources/raw/external/go-dev-design-43651-type-parameters-8b418b79f1.html"
license_ref: ""
---

## Design

Constraint type inference can only infer types if some type parameter has a constraint that has a type set with exactly one type in it, or a type set for which the underlying type of every type in the type set is the same type. The two cases are slightly different, as in the first case, in which the type set has exactly one type, the single type need not be its own underlying type. Either way, the single type is called a _structural type_, and the constraint is called a _structural constraint_. The structural type describes the required structure of the type parameter. A structural constraint may also define methods, but the methods are ignored by constraint type inference. For constraint type inference to be useful, the structural type will normally be defined using one or more type parameters.

Constraint type inference is only tried if there is at least one type parameter whose type argument is not yet known.

While the algorithm we describe here may seem complex, for typical concrete examples it is straightforward to see what constraint type inference will deduce. The description of the algorithm is followed by a couple of examples.

We start by creating a mapping from type parameters to type arguments. We initialize the mapping with all type parameters whose type arguments are already known, if any.

For each type parameter with a structural constraint, we unify the type parameter with the structural type. This will have the effect of associating the type parameter with its constraint. We add the result into the mapping we are maintaining. If unification finds any associations of type parameters, we add those to the mapping as well. When we find multiple associations of any one type parameter, we unify each such association to produce a single mapping entry. If a type parameter is associated directly with another type parameter, meaning that they must both be matched with the same type, we unify the associations of each parameter together. If any of these various unifications fail, then constraint type inference fails.

After merging all type parameters with structural constraints, we have a mapping of various type parameters to types (which may be or contain other type parameters). We continue by looking for a type parameter `T` that is mapped to a fully known type argument `A`, one that does not contain any type parameters. Anywhere that `T` appears in a type argument in the mapping, we replace `T` with `A`. We repeat this process until we have replaced every type parameter.

When constraint type inference is possible, type inference proceeds as followed:

- Build the mapping using known type arguments.
- Apply constraint type inference.
- Apply function type inference using typed arguments.
- Apply constraint type inference again.
- Apply function type inference using the default types of any remaining untyped arguments.
- Apply constraint type inference again.
Element constraint example
For an example of where constraint type inference is useful, let's consider a function that takes a defined type that is a slice of numbers, and returns an instance of that same defined type in which each number is doubled.

It's easy to write a function similar to this if we ignore the defined type <https://golang.org/ref/spec#Type_definitions> requirement.

```go
// Double returns a new slice that contains all the elements of s, doubled.
func Double[E constraints.Integer](s []E) []E {
	r := make([]E, len(s))
	for i, v := range s {
		r[i] = v + v
	}
	return r
}

```

However, with that definition, if we call the function with a defined slice type, the result will not be that defined type.

```go
// MySlice is a slice of ints.
type MySlice []int

// The type of V1 will be []int, not MySlice.
// Here we are using function argument type inference,
// but not constraint type inference.
var V1 = Double(MySlice{1})

```

We can do what we want by introducing a new type parameter.

```go
// DoubleDefined returns a new slice that contains the elements of s,
// doubled, and also has the same type as s.
func DoubleDefined[S ~[]E, E constraints.Integer](s S) S {
	// Note that here we pass S to make, where above we passed []E.
	r := make(S, len(s))
	for i, v := range s {
		r[i] = v + v
	}
	return r
}

```

Now if we use explicit type arguments, we can get the right type.

```go
// The type of V2 will be MySlice.
var V2 = DoubleDefined[MySlice, int](MySlice{1})

```

Function argument type inference by itself is not enough to infer the type arguments here, because the type parameter E is not used for any input parameter. But a combination of function argument type inference and constraint type inference works.

```go
// The type of V3 will be MySlice.
var V3 = DoubleDefined(MySlice{1})

```

First we apply function argument type inference. We see that the type of the argument is `MySlice`. Function argument type inference matches the type parameter `S` with `MySlice`.

We then move on to constraint type inference. We know one type argument, `S`. We see that the type argument `S` has a structural type constraint.

We create a mapping of known type arguments:

```go
{S -> MySlice}

```

We then unify each type parameter with a structural constraint with the single type in that constraint's type set. In this case the structural constraint is `~[]E` which has the structural type `[]E`, so we unify `S` with `[]E`. Since we already have a mapping for `S`, we then unify `[]E` with `MySlice`. As `MySlice` is defined as `[]int`, that associates `E` with `int`. We now have:

```go
{S -> MySlice, E -> int}

```

We then substitute `E` with `int`, which changes nothing, and we are done. The type arguments for this call to `DoubleDefined` are `[MySlice, int]`.

This example shows how we can use constraint type inference to set a type name for an element of some other type parameter. In this case we can name the element type of `S` as `E`, and we can then apply further constraints to `E`, in this case requiring that it be a number.
Pointer method example
Consider this example of a function that expects a type `T` that has a `Set(string)` method that initializes a value based on a string.

```go
// Setter is a type constraint that requires that the type
// implement a Set method that sets the value from a string.
type Setter interface {
	Set(string)
}

// FromStrings takes a slice of strings and returns a slice of T,
// calling the Set method to set each returned value.
//
// Note that because T is only used for a result parameter,
// function argument type inference does not work when calling
// this function.
func FromStrings[T Setter](s []string) []T {
	result := make([]T, len(s))
	for i, v := range s {
		result[i].Set(v)
	}
	return result
}

```

Now let's see some calling code (this example is invalid).

```go
// Settable is an integer type that can be set from a string.
type Settable int

// Set sets the value of *p from a string.
func (p *Settable) Set(s string) {
	i, _ := strconv.Atoi(s) // real code should not ignore the error
	*p = Settable(i)
}

func F() {
	// INVALID
	nums := FromStrings[Settable]([]string{"1", "2"})
	// Here we want nums to be []Settable{1, 2}.
	...
}

```

The goal is to use `FromStrings` to get a slice of type `[]Settable`. Unfortunately, this example is not valid and will not compile.

The problem is that `FromStrings` requires a type that has a `Set(string)` method. The function `F` is trying to instantiate `FromStrings` with `Settable`, but `Settable` does not have a `Set` method. The type that has a `Set` method is `*Settable`.

So let's rewrite `F` to use `*Settable` instead.

```go
func F() {
	// Compiles but does not work as desired.
	// This will panic at run time when calling the Set method.
	nums := FromStrings[*Settable]([]string{"1", "2"})
	...
}

```

This compiles but unfortunately it will panic at run time. The problem is that `FromStrings` creates a slice of type `[]T`. When instantiated with `*Settable`, that means a slice of type `[]*Settable`. When `FromStrings` calls `result[i].Set(v)`, that invokes the `Set` method on the pointer stored in `result[i]`. That pointer is `nil`. The `Settable.Set` method will be invoked with a `nil` receiver, and will raise a panic due to a `nil` dereference error.

The pointer type `*Settable` implements the constraint, but the code really wants to use the non-pointer type`Settable`. What we need is a way to write `FromStrings` such that it can take the type `Settable` as an argument but invoke a pointer method. To repeat, we can‘t use `Settable` because it doesn’t have a `Set` method, and we can‘t use `*Settable` because then we can’t create a slice of type `Settable`.

What we can do is pass both types.

```go
// Setter2 is a type constraint that requires that the type
// implement a Set method that sets the value from a string,
// and also requires that the type be a pointer to its type parameter.
type Setter2[B any] interface {
	Set(string)
	*B // non-interface type constraint element
}
