---
source_name: "External Linked Documentation"
source_url: "https://go.dev/ref/spec"
source_path: "sources/raw/external/go-dev-ref-spec-3c5b020879.html"
license_ref: ""
---

## Expressions

### Type inference

A use of a generic function may omit some or all type arguments if they can be _inferred_ from the context within which the function is used, including the constraints of the function's type parameters. Type inference succeeds if it can infer the missing type arguments and instantiation succeeds with the inferred type arguments. Otherwise, type inference fails and the program is invalid.

Type inference uses the type relationships between pairs of types for inference: For instance, a function argument must be assignable to its respective function parameter; this establishes a relationship between the type of the argument and the type of the parameter. If either of these two types contains type parameters, type inference looks for the type arguments to substitute the type parameters with such that the assignability relationship is satisfied. Similarly, type inference uses the fact that a type argument must satisfy the constraint of its respective type parameter.

Each such pair of matched types corresponds to a _type equation_ containing one or multiple type parameters, from one or possibly multiple generic functions. Inferring the missing type arguments means solving the resulting set of type equations for the respective type parameters.

For example, given

```go

// dedup returns a copy of the argument slice with any duplicate entries removed.
func dedup[S ~[]E, E comparable](S) S { … }

type Slice []int
var s Slice
s = dedup(s)   // same as s = dedup[Slice, int](s)

```

the variable `s` of type `Slice` must be assignable to the function parameter type `S` for the program to be valid. To reduce complexity, type inference ignores the directionality of assignments, so the type relationship between `Slice` and `S` can be expressed via the (symmetric) type equation `Slice ≡A S` (or `S ≡A Slice` for that matter), where the `A` in `≡A` indicates that the LHS and RHS types must match per assignability rules (see the section on type unification for details). Similarly, the type parameter `S` must satisfy its constraint `~[]E`. This can be expressed as `S ≡C ~[]E` where `X ≡C Y` stands for "`X` satisfies constraint `Y`". These observations lead to a set of two equations

```go

Slice ≡A S      (1)
	S     ≡C ~[]E   (2)

```

which now can be solved for the type parameters `S` and `E`. From (1) a compiler can infer that the type argument for `S` is `Slice`. Similarly, because the underlying type of `Slice` is `[]int` and `[]int` must match `[]E` of the constraint, a compiler can infer that `E` must be `int`. Thus, for these two equations, type inference infers

```go

S ➞ Slice
	E ➞ int

```

Given a set of type equations, the type parameters to solve for are the type parameters of the functions that need to be instantiated and for which no explicit type arguments is provided. These type parameters are called _bound_ type parameters. For instance, in the `dedup` example above, the type parameters `S` and `E` are bound to `dedup`. An argument to a generic function call may be a generic function itself. The type parameters of that function are included in the set of bound type parameters. The types of function arguments may contain type parameters from other functions (such as a generic function enclosing a function call). Those type parameters may also appear in type equations but they are not bound in that context. Type equations are always solved for the bound type parameters only.

Type inference supports calls of generic functions and assignments of generic functions to (explicitly function-typed) variables. This includes passing generic functions as arguments to other (possibly also generic) functions, and returning generic functions as results. Type inference operates on a set of equations specific to each of these cases. The equations are as follows (type argument lists are omitted for clarity):

-
 For a function call `f(a0, a1, …)` where `f` or a function argument `ai` is a generic function:
 Each pair `(ai, pi)` of corresponding function arguments and parameters where `ai` is not an untyped constant yields an equation `typeof(pi) ≡A typeof(ai)`.
 If `ai` is an untyped constant `cj`, and `typeof(pi)` is a bound type parameter `Pk`, the pair `(cj, Pk)` is collected separately from the type equations.

-
 For an assignment `v = f` of a generic function `f` to a (non-generic) variable `v` of function type:
 `typeof(v) ≡A typeof(f)`.

-
 For a return statement `return …, f, … ` where `f` is a generic function returned as a result to a (non-generic) result variable `r` of function type:
 `typeof(r) ≡A typeof(f)`.

Additionally, each type parameter `Pk` and corresponding type constraint `Ck` yields the type equation `Pk ≡C Ck`.

Type inference gives precedence to type information obtained from typed operands before considering untyped constants. Therefore, inference proceeds in two phases:

-
 The type equations are solved for the bound type parameters using type unification. If unification fails, type inference fails.

-
 For each bound type parameter `Pk` for which no type argument has been inferred yet and for which one or more pairs `(cj, Pk)` with that same type parameter were collected, determine the constant kind of the constants `cj` in all those pairs the same way as for constant expressions. The type argument for `Pk` is the default type for the determined constant kind. If a constant kind cannot be determined due to conflicting constant kinds, type inference fails.

If not all type arguments have been found after these two phases, type inference fails.

If the two phases are successful, type inference determined a type argument for each bound type parameter:

```go

Pk ➞ Ak

```

A type argument `Ak` may be a composite type, containing other bound type parameters `Pk` as element types (or even be just another bound type parameter). In a process of repeated simplification, the bound type parameters in each type argument are substituted with the respective type arguments for those type parameters until each type argument is free of bound type parameters.

If type arguments contain cyclic references to themselves through bound type parameters, simplification and thus type inference fails. Otherwise, type inference succeeds.

#### Type unification

Type inference solves type equations through _type unification_. Type unification recursively compares the LHS and RHS types of an equation, where either or both types may be or contain bound type parameters, and looks for type arguments for those type parameters such that the LHS and RHS match (become identical or assignment-compatible, depending on context). To that effect, type inference maintains a map of bound type parameters to inferred type arguments; this map is consulted and updated during type unification. Initially, the bound type parameters are known but the map is empty. During type unification, if a new type argument `A` is inferred, the respective mapping `P ➞ A` from type parameter to argument is added to the map. Conversely, when comparing types, a known type argument (a type argument for which a map entry already exists) takes the place of its corresponding type parameter. As type inference progresses, the map is populated more and more until all equations have been considered, or until unification fails. Type inference succeeds if no unification step fails and the map has an entry for each type parameter.

For example, given the type equation with the bound type parameter `P`

```go

[10]struct{ elem P, list []P } ≡A [10]struct{ elem string; list []string }

```

type inference starts with an empty map. Unification first compares the top-level structure of the LHS and RHS types. Both are arrays of the same length; they unify if the element types unify. Both element types are structs; they unify if they have the same number of fields with the same names and if the field types unify. The type argument for `P` is not known yet (there is no map entry), so unifying `P` with `string` adds the mapping `P ➞ string` to the map. Unifying the types of the `list` field requires unifying `[]P` and `[]string` and thus `P` and `string`. Since the type argument for `P` is known at this point (there is a map entry for `P`), its type argument `string` takes the place of `P`. And since `string` is identical to `string`, this unification step succeeds as well. Unification of the LHS and RHS of the equation is now finished. Type inference succeeds because there is only one type equation, no unification step failed, and the map is fully populated.

Unification uses a combination of _exact_ and _loose_ unification depending on whether two types have to be identical, assignment-compatible, or only structurally equal. The respective type unification rules are spelled out in detail in the Appendix.

For an equation of the form `X ≡A Y`, where `X` and `Y` are types involved in an assignment (including parameter passing and return statements), the top-level type structures may unify loosely but element types must unify exactly, matching the rules for assignments.

For an equation of the form `P ≡C C`, where `P` is a type parameter and `C` its corresponding constraint, the unification rules are bit more complicated:
