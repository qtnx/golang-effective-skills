---
source_name: "External Linked Documentation"
source_url: "https://go.dev/design/43651-type-parameters"
source_path: "sources/raw/external/go-dev-design-43651-type-parameters-8b418b79f1.html"
license_ref: ""
---

## Design

### Summary

While this document is long and detailed, the actual design reduces to a few major points.

- Functions and types can have type parameters, which are defined using constraints, which are interface types.
- Constraints describe the methods required and the types permitted for a type argument.
- Constraints describe the methods and operations permitted for a type parameter.
- Type inference will often permit omitting type arguments when calling functions with type parameters.

This design is completely backward compatible.

We believe that this design addresses people's needs for generic programming in Go, without making the language any more complex than necessary.

We can't truly know the impact on the language without years of experience with this design. That said, here are some speculations.

#### Complexity

One of the great aspects of Go is its simplicity. Clearly this design makes the language more complex.

We believe that the increased complexity is small for people reading well written generic code, rather than writing it. Naturally people must learn the new syntax for declaring type parameters. This new syntax, and the new support for type sets in interfaces, are the only new syntactic constructs in this design. The code within a generic function reads like ordinary Go code, as can be seen in the examples below. It is an easy shift to go from `[]int` to `[]T`. Type parameter constraints serve effectively as documentation, describing the type.

We expect that most packages will not define generic types or functions, but many packages are likely to use generic types or functions defined elsewhere. In the common case, generic functions work exactly like non-generic functions: you simply call them. Type inference means that you do not have to write out the type arguments explicitly. The type inference rules are designed to be unsurprising: either the type arguments are deduced correctly, or the call fails and requires explicit type parameters. Type inference uses type equivalence, with no attempt to resolve two types that are similar but not equivalent, which removes significant complexity.

Packages using generic types will have to pass explicit type arguments. The syntax for this is straightforward. The only change is passing arguments to types rather than only to functions.

In general, we have tried to avoid surprises in the design. Only time will tell whether we succeeded.

#### Pervasiveness

We expect that a few new packages will be added to the standard library. A new `slices` packages will be similar to the existing bytes and strings packages, operating on slices of any element type. New `maps` and `chans` packages will provide algorithms that are currently duplicated for each element type. A `sets` package may be added.

A new `constraints` package will provide standard constraints, such as constraints that permit all integer types or all numeric types.

Packages like `container/list` and `container/ring`, and types like `sync.Map` and `sync/atomic.Value`, will be updated to be compile-time type-safe, either using new names or new versions of the packages.

The `math` package will be extended to provide a set of simple standard algorithms for all numeric types, such as the ever popular `Min` and `Max` functions.

We may add generic variants to the `sort` package.

It is likely that new special purpose compile-time type-safe container types will be developed.

We do not expect approaches like the C++ STL iterator types to become widely used. In Go that sort of idea is more naturally expressed using an interface type. In C++ terms, using an interface type for an iterator can be seen as carrying an abstraction penalty, in that run-time efficiency will be less than C++ approaches that in effect inline all code; we believe that Go programmers will continue to find that sort of penalty to be acceptable.

As we get more container types, we may develop a standard `Iterator` interface. That may in turn lead to pressure to modify the language to add some mechanism for using an `Iterator` with the `range` clause. That is very speculative, though.

#### Efficiency

It is not clear what sort of efficiency people expect from generic code.

Generic functions, rather than generic types, can probably be compiled using an interface-based approach. That will optimize compile time, in that the function is only compiled once, but there will be some run time cost.

Generic types may most naturally be compiled multiple times for each set of type arguments. This will clearly carry a compile time cost, but there shouldn't be any run time cost. Compilers can also choose to implement generic types similarly to interface types, using special purpose methods to access each element that depends on a type parameter.

Only experience will show what people expect in this area.

#### Omissions

We believe that this design covers the basic requirements for generic programming. However, there are a number of programming constructs that are not supported.

- No specialization. There is no way to write multiple versions of a generic function that are designed to work with specific type arguments.
- No metaprogramming. There is no way to write code that is executed at compile time to generate code to be executed at run time.
- No higher level abstraction. There is no way to use a function with type arguments other than to call it or instantiate it. There is no way to use a generic type other than to instantiate it.
- No general type description. In order to use operators in a generic function, constraints list specific types, rather than describing the characteristics that a type must have. This is easy to understand but may be limiting at times.
- No covariance or contravariance of function parameters.
- No operator methods. You can write a generic container that is compile-time type-safe, but you can only access it with ordinary methods, not with syntax like `c[k]`.
- No currying. There is no way to partially instantiate a generic function or type, other than by using a helper function or a wrapper type. All type arguments must be either explicitly passed or inferred at instantiation time.
- No variadic type parameters. There is no support for variadic type parameters, which would permit writing a single generic function that takes different numbers of both type parameters and regular parameters.
- No adaptors. There is no way for a constraint to define adaptors that could be used to support type arguments that do not already implement the constraint, such as, for example, defining an `==` operator in terms of an `Equal` method, or vice-versa.
- No parameterization on non-type values such as constants. This arises most obviously for arrays, where it might sometimes be convenient to write `type Matrix[n int] [n][n]float64`. It might also sometimes be useful to specify significant values for a container type, such as a default value for elements.

#### Issues

There are some issues with this design that deserve a more detailed discussion. We think these issues are relatively minor compared to the design as a whole, but they still deserve a complete hearing and discussion.
The zero value
This design has no simple expression for the zero value of a type parameter. For example, consider this implementation of optional values that uses pointers:

```go
type Optional[T any] struct {
	p *T
}

func (o Optional[T]) Val() T {
	if o.p != nil {
		return *o.p
	}
	var zero T
	return zero
}

```

In the case where `o.p == nil`, we want to return the zero value of `T`, but we have no way to write that. It would be nice to be able to write `return nil`, but that wouldn't work if `T` is, say, `int`; in that case we would have to write `return 0`. And, of course, there is no way to write a constraint to support either `return nil` or `return 0`.

Some approaches to this are:

- Use `var zero T`, as above, which works with the existing design but requires an extra statement.
- Use `*new(T)`, which is cryptic but works with the existing design.
- For results only, name the result parameter, and use a naked `return` statement to return the zero value.
- Extend the design to permit using `nil` as the zero value of any generic type (but see issue 22729 <https://golang.org/issue/22729>).
- Extend the design to permit using `T{}`, where `T` is a type parameter, to indicate the zero value of the type.
- Change the language to permit using `_` on the right hand of an assignment (including `return` or a function call) as proposed in issue 19642 <https://golang.org/issue/19642>.
- Change the language to permit `return ...` to return zero values of the result types, as proposed in issue 21182 <https://golang.org/issue/21182>.

We feel that more experience with this design is needed before deciding what, if anything, to do here.
Identifying the matched predeclared type
The design doesn't provide any way to test the underlying type matched by a `~T` constraint element. Code can test the actual type argument through the somewhat awkward approach of converting to an empty interface type and using a type assertion or a type switch. But that lets code test the actual type argument, which is not the same as the underlying type.

Here is an example that shows the difference.

```go
type Float interface {
	~float32 | ~float64
}

func NewtonSqrt[T Float](v T) T {
	var iterations int
	switch (interface{})(v).(type) {
	case float32:
		iterations = 4
	case float64:
		iterations = 5
	default:
		panic(fmt.Sprintf("unexpected type %T", v))
	}
	// Code omitted.
}

type MyFloat float32

var G = NewtonSqrt(MyFloat(64))

```
