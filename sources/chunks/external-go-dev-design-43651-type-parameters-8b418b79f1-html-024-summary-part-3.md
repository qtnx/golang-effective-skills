---
source_name: "External Linked Documentation"
source_url: "https://go.dev/design/43651-type-parameters"
source_path: "sources/raw/external/go-dev-design-43651-type-parameters-8b418b79f1.html"
license_ref: ""
---

## Design

It is possible to permit operator tokens as method names, leading to methods such as `+(T) T`. Unfortunately, that is not sufficient. We would need some mechanism to describe a type that matches any integer type, for operations such as shifts `<<(integer) T` and indexing `[](integer) T` which are not restricted to a single int type. We would need an untyped boolean type for operations such as `==(T) untyped bool`. We would need to introduce new notation for operations such as conversions, or to express that one may range over a type, which would likely require some new syntax. We would need some mechanism to describe valid values of untyped constants. We would have to consider whether support for `<(T) bool` means that a generic function can also use `<=`, and similarly whether support for `+(T) T` means that a function can also use `++`. It might be possible to make this approach work but it's not straightforward. The approach used in this design seems simpler and relies on only one new syntactic construct (type sets) and one new name (`comparable`).
Why not put type parameters on packages?
We investigated this extensively. It becomes problematic when you want to write a `list` package, and you want that package to include a `Transform` function that converts a `List` of one element type to a `List` of another element type. It's very awkward for a function in one instantiation of a package to return a type that requires a different instantiation of the same package.

It also confuses package boundaries with type definitions. There is no particular reason to think that the uses of generic types will break down neatly into packages. Sometimes they will, sometimes they won't.
Why not use the syntax `F<T>` like C++ and Java?
When parsing code within a function, such as `v := F<T>`, at the point of seeing the `<` it's ambiguous whether we are seeing a type instantiation or an expression using the `<` operator. This is very difficult to resolve without type information.

For example, consider a statement like

```go
	a, b = w < x, y > (z)

```

Without type information, it is impossible to decide whether the right hand side of the assignment is a pair of expressions (`w < x` and `y > (z)`), or whether it is a generic function instantiation and call that returns two result values (`(w<x, y>)(z)`).

It is a key design decision of Go that parsing be possible without type information, which seems impossible when using angle brackets for generics.
Why not use the syntax `F(T)`?
An earlier version of this design used that syntax. It was workable but it introduced several parsing ambiguities. For example, when writing `var f func(x(T))` it wasn't clear whether the type was a function with a single unnamed parameter of the instantiated type `x(T)` or whether it was a function with a parameter named `x` with type `(T)` (more usually written as `func(x T)`, but in this case with a parenthesized type).

There were other ambiguities as well. For `[]T(v1)` and `[]T(v2){}`, at the point of the open parentheses we don‘t know whether this is a type conversion (of the value `v1` to the type `[]T`) or a type literal (whose type is the instantiated type `T(v2)`). For `interface { M(T) }` we don’t know whether this an interface with a method `M` or an interface with an embedded instantiated interface `M(T)`. These ambiguities are solvable, by adding more parentheses, but awkward.

Also some people were troubled by the number of parenthesized lists involved in declarations like `func F(T any)(v T)(r1, r2 T)` or in calls like `F(int)(1)`.
Why not use `F«T»`?
We considered it but we couldn't bring ourselves to require non-ASCII.
Why not define constraints in a builtin package?
_Instead of writing out type sets, use names like_ _`constraints.Arithmetic` and `constraints.Comparable`._

Listing all the possible combinations of types gets rather lengthy. It also introduces a new set of names that not only the writer of generic code, but, more importantly, the reader, must remember. One of the driving goals of this design is to introduce as few new names as possible. In this design we introduce only two new predeclared names, `comparable` and `any`.

We expect that if people find such names useful, we can introduce a package `constraints` that defines those names in the form of constraints that can be used by other types and functions and embedded in other constraints. That will define the most useful names in the standard library while giving programmers the flexibility to use other combinations of types where appropriate.
Why not permit type assertions on values whose type is a type parameter?
In an earlier version of this design, we permitted using type assertions and type switches on variables whose type was a type parameter, or whose type was based on a type parameter. We removed this facility because it is always possible to convert a value of any type to the empty interface type, and then use a type assertion or type switch on that. Also, it was sometimes confusing that in a constraint with a type set that uses approximation elements, a type assertion or type switch would use the actual type argument, not the underlying type of the type argument (the difference is explained in the section on identifying the matched predeclared type).

#### Comparison with Java

Most complaints about Java generics center around type erasure. This design does not have type erasure. The reflection information for a generic type will include the full compile-time type information.

In Java type wildcards (`List<? extends Number>`, `List<? super Number>`) implement covariance and contravariance. These concepts are missing from Go, which makes generic types much simpler.

#### Comparison with C++

C++ templates do not enforce any constraints on the type arguments (unless the concept proposal is adopted). This means that changing template code can accidentally break far-off instantiations. It also means that error messages are reported only at instantiation time, and can be deeply nested and difficult to understand. This design avoids these problems through mandatory and explicit constraints.

C++ supports template metaprogramming, which can be thought of as ordinary programming done at compile time using a syntax that is completely different than that of non-template C++. This design has no similar feature. This saves considerable complexity while losing some power and run time efficiency.

C++ uses two-phase name lookup, in which some names are looked up in the context of the template definition, and some names are looked up in the context of the template instantiation. In this design all names are looked up at the point where they are written.

In practice, all C++ compilers compile each template at the point where it is instantiated. This can slow down compilation time. This design offers flexibility as to how to handle the compilation of generic functions.

#### Comparison with Rust

The generics described in this design are similar to generics in Rust.

One difference is that in Rust the association between a trait bound and a type must be defined explicitly, either in the crate that defines the trait bound or the crate that defines the type. In Go terms, this would mean that we would have to declare somewhere whether a type satisfied a constraint. Just as Go types can satisfy Go interfaces without an explicit declaration, in this design Go type arguments can satisfy a constraint without an explicit declaration.

Where this design uses type sets, the Rust standard library defines standard traits for operations like comparison. These standard traits are automatically implemented by Rust's primitive types, and can be implemented by user defined types as well. Rust provides a fairly extensive list of traits, at least 34, covering all of the operators.

Rust supports type parameters on methods, which this design does not.
