---
source_name: "External Linked Documentation"
source_url: "https://go.dev/design/43651-type-parameters"
source_path: "sources/raw/external/go-dev-design-43651-type-parameters-8b418b79f1.html"
license_ref: ""
---

## Design

### Methods may not take additional type arguments

Although methods of a generic type may use the type's parameters, methods may not themselves have additional type parameters. Where it would be useful to add type arguments to a method, people will have to write a suitably parameterized top-level function.

There is more discussion of this in the issues section.

## Design

### Operators

As we‘ve seen, we are using interface types as constraints. Interface types provide a set of methods, and nothing else. This means that with what we’ve seen so far, the only thing that generic functions can do with values of type parameters, other than operations that are permitted for any type, is call methods.

However, method calls are not sufficient for everything we want to express. Consider this simple function that returns the smallest element of a slice of values, where the slice is assumed to be non-empty.

```go
// This function is INVALID.
func Smallest[T any](s []T) T {
	r := s[0] // panic if slice is empty
	for _, v := range s[1:] {
		if v < r { // INVALID
			r = v
		}
	}
	return r
}

```

Any reasonable generics implementation should let you write this function. The problem is the expression `v < r`. This assumes that `T` supports the `<` operator, but the constraint on `T` is simply `any`. With the `any` constraint the function `Smallest` can only use operations that are available for all types, but not all Go types support `<`. Unfortunately, since `<` is not a method, there is no obvious way to write a constraint—an interface type—that permits `<`.

We need a way to write a constraint that accepts only types that support `<`. In order to do that, we observe that, aside from two exceptions that we will discuss later, all the arithmetic, comparison, and logical operators defined by the language may only be used with types that are predeclared by the language, or with defined types whose underlying type is one of those predeclared types. That is, the operator `<` can only be used with a predeclared type such as `int` or `float64`, or a defined type whose underlying type is one of those types. Go does not permit using `<` with a composite type or with an arbitrary defined type.

This means that rather than try to write a constraint for `<`, we can approach this the other way around: instead of saying which operators a constraint should support, we can say which types a constraint should accept. We do this by defining a _type set_ for a constraint.

#### Type sets

Although we are primarily interested in defining the type set of constraints, the most straightforward approach is to define the type set of all types. The type set of a constraint is then constructed out of the type sets of its elements. This may seem like a digression from the topic of using operators with parameterized types, but we'll get there in the end.

Every type has an associated type set. The type set of a non-interface type `T` is simply the set `{T}`: a set that contains just `T` itself. The type set of an ordinary interface type is the set of all types that declare all the methods of the interface.

Note that the type set of an ordinary interface type is an infinite set. For any given type `T` and interface type `IT` it's easy to tell whether `T` is in the type set of `IT` (by checking if all methods of `IT` are declared by `T`), but there is no reasonable way to enumerate all the types in the type set of `IT`. The type `IT` is a member of its own type set, because an interface inherently declares all of its own methods. The type set of the empty interface `interface{}` is the set of all possible types.

It will be useful to construct the type set of an interface type by looking at the elements of the interface. This will produce the same result in a different way. The elements of an interface can be either a method signature or an embedded interface type. Although a method signature is not a type, it's convenient to define a type set for it: the set of all types that declare that method. The type set of an embedded interface type `E` is simply that of `E`: the set of all types that declare all the methods of `E`.

For any method signature `M`, the type set of `interface{ M }` is the type of `M`: the set of all types that declare `M`. For any method signatures `M1` and `M2`, the type set of `interface{ M1; M2 }` is set of all types that declare both `M1` and `M2`. This is the intersection of the type set of `M1` and the type set of `M2`. To see this, observe that the type set of `M1` is the set of all types with a method `M1`, and similarly for `M2`. If we take the intersection of those two type sets, the result is the set of all types that declare both `M1` and `M2`. That is exactly the type set of `interface{ M1; M2 }`.

The same applies to embedded interface types. For any two interface types `E1` and `E2`, the type set of `interface{ E1; E2 }` is the intersection of the type sets of `E1` and `E2`.

Therefore, the type set of an interface type is the intersection of the type sets of the element of the interface.

#### Type sets of constraints

Now that we have described the type set of an interface type, we will redefine what it means to satisfy the constraint. Earlier we said that a type argument satisfies a constraint if it implements the constraint. Now we will say that a type argument satisfies a constraint if it is a member of the constraint's type set.

For an ordinary interface type, one whose only elements are method signatures and embedded ordinary interface types, the meaning is exactly the same: the set of types that implement the interface type is exactly the set of types that are in its type set.

We will now proceed to define additional elements that may appear in an interface type that is used as a constraint, and define how those additional elements can be used to further control the type set of the constraint.

#### Constraint elements

The elements of an ordinary interface type are method signatures and embedded interface types. We propose permitting three additional elements that may be used in an interface type used as a constraint. If any of these additional elements are used, the interface type may not be used as an ordinary type, but may only be used as a constraint.
Arbitrary type constraint element
The first new element is to simply permit listing any type, not just an interface type. For example: `type Integer interface{ int }`. When a non-interface type `T` is listed as an element of a constraint, its type set is simply `{T}`. The type set of `int` is `{int}`. Since the type set of a constraint is the intersection of the type sets of all elements, the type set of `Integer` is also `{int}`. This constraint `Integer` can be satisfied by any type that is a member of the set `{int}`. There is exactly one such type: `int`.

The type may be a type literal that refers to a type parameter (or more than one), but it may not be a plain type parameter.

```go
// EmbeddedParameter is INVALID.
type EmbeddedParameter[T any] interface {
	T // INVALID: may not list a plain type parameter
}

```
Approximation constraint element
Listing a single type is useless by itself. For constraint satisfaction, we want to be able to say not just `int`, but “any type whose underlying type is `int`”. Consider the `Smallest` example above. We want it to work not just for slices of the predeclared ordered types, but also for types defined by a program. If a program uses `type MyString string`, the program can use the `<` operator with values of type `MyString`. It should be possible to instantiate `Smallest` with the type `MyString`.

To support this, the second new element we permit in a constraint is a new syntactic construct: an approximation element, written as `~T`. The type set of `~T` is the set of all types whose underlying type is `T`.

For example: `type AnyString interface{ ~string }`. The type set of `~string`, and therefore the type set of `AnyString`, is the set of all types whose underlying type is `string`. That includes the type `MyString`; `MyString` used as a type argument will satisfy the constraint `AnyString`.

This new `~T` syntax will be the first use of `~` as a token in Go.

Since `~T` means the set of all types whose underlying type is `T`, it will be an error to use `~T` with a type `T` whose underlying type is not itself. Types whose underlying types are themselves are:

- Type literals, such as `[]byte` or `struct{ f int }`.
- Most predeclared types, such as `int` or `string` (but not `error`).

Using `~T` is not permitted if `T` is a type parameter or if `T` is an interface type.

```go
type MyString string

// AnyString matches any type whose underlying type is string.
// This includes, among others, the type string itself, and
// the type MyString.
type AnyString interface {
	~string
}
