---
source_name: "External Linked Documentation"
source_url: "https://go.dev/design/43651-type-parameters"
source_path: "sources/raw/external/go-dev-design-43651-type-parameters-8b418b79f1.html"
license_ref: ""
---

## Design

### Type inference

In many cases we can use type inference to avoid having to explicitly write out some or all of the type arguments. We can use _function argument type inference_ for a function call to deduce type arguments from the types of the non-type arguments. We can use _constraint type inference_ to deduce unknown type arguments from known type arguments.

In the examples above, when instantiating a generic function or type, we always specified type arguments for all the type parameters. We also permit specifying just some of the type arguments, or omitting the type arguments entirely, when the missing type arguments can be inferred. When only some type arguments are passed, they are the arguments for the first type parameters in the list.

For example, a function like this:

```go
func Map[F, T any](s []F, f func(F) T) []T { ... }

```

can be called in these ways. (We'll explain below how type inference works in detail; this example is to show how an incomplete list of type arguments is handled.)

```go
	var s []int
	f := func(i int) int64 { return int64(i) }
	var r []int64
	// Specify both type arguments explicitly.
	r = Map[int, int64](s, f)
	// Specify just the first type argument, for F,
	// and let T be inferred.
	r = Map[int](s, f)
	// Don't specify any type arguments, and let both be inferred.
	r = Map(s, f)

```

If a generic function or type is used without specifying all the type arguments, it is an error if any of the unspecified type arguments cannot be inferred.

(Note: type inference is a convenience feature. Although we think it is an important feature, it does not add any functionality to the design, only convenience in using it. It would be possible to omit it from the initial implementation, and see whether it seems to be needed. That said, this feature doesn't require additional syntax, and produces more readable code.)

#### Type unification

Type inference is based on _type unification_. Type unification applies to two types, either or both of which may be or contain type parameters.

Type unification works by comparing the structure of the types. Their structure disregarding type parameters must be identical, and types other than type parameters must be equivalent. A type parameter in one type may match any complete subtype in the other type. If the structure differs, or types other than type parameters are not equivalent, then type unification fails. A successful type unification provides a list of associations of type parameters with other types (which may themselves be or contain type parameters).

For type unification, two types that don‘t contain any type parameters are equivalent if they are identical <https://golang.org/ref/spec#Type_identity>, or if they are channel types that are identical ignoring channel direction, or if their underlying types are equivalent. It’s OK to permit types to not be identical during type inference, because we will still check the constraints if inference succeeds, and we will still check that the function arguments are assignable to the inferred types.

For example, if `T1` and `T2` are type parameters, `[]map[int]bool` can be unified with any of the following:

- `[]map[int]bool`
- `T1` (`T1` matches `[]map[int]bool`)
- `[]T1` (`T1` matches `map[int]bool`)
- `[]map[T1]T2` (`T1` matches `int`, `T2` matches `bool`)

(This is not an exclusive list, there are other possible successful unifications.)

On the other hand, `[]map[int]bool` cannot be unified with any of

- `int`
- `struct{}`
- `[]struct{}`
- `[]map[T1]string`

(This list is of course also not exclusive; there are an infinite number of types that cannot be successfully unified.)

In general we can also have type parameters on both sides, so in some cases we might associate `T1` with, for example, `T2`, or `[]T2`.

#### Function argument type inference

Function argument type inference is used with a function call to infer type arguments from non-type arguments. Function argument type inference is not used when a type is instantiated, and it is not used when a function is instantiated but not called.

To see how it works, let's go back to the example of a call to the simple `Print` function:

```go
	Print[int]([]int{1, 2, 3})

```

The type argument `int` in this function call can be inferred from the type of the non-type argument.

The only type arguments that can be inferred are those that are used for the types of the function‘s (non-type) input parameters. If there are some type parameters that are used only for the function’s result parameter types, or only in the body of the function, then those type arguments cannot be inferred using function argument type inference.

To infer function type arguments, we unify the types of the function call arguments with the types of the function‘s non-type parameters. On the caller side we have the list of types of the actual (non-type) arguments, which for the `Print` example is simply `[]int`. On the function side is the list of the types of the function’s non-type parameters, which for `Print` is `[]T`. In the lists, we discard respective arguments for which the function side does not use a type parameter. We must then apply type unification to the remaining argument types.

Function argument type inference is a two-pass algorithm. In the first pass, we ignore untyped constants on the caller side and their corresponding types in the function definition. We use two passes so that in some cases later arguments can determine the type of an untyped constant.

We unify corresponding types in the lists. This will give us an association of type parameters on the function side to types on the caller side. If the same type parameter appears more than once on the function side, it will match multiple argument types on the caller side. If those caller types are not equivalent, we report an error.

After the first pass, we check any untyped constants on the caller side. If there are no untyped constants, or if the type parameters in the corresponding function types have matched other input types, then type unification is complete.

Otherwise, for the second pass, for any untyped constants whose corresponding function types are not yet set, we determine the default type of the untyped constant in the usual way <https://golang.org/ref/spec#Constants>. Then we unify the remaining types again, this time with no untyped constants.

When constraint type inference is possible, as described below, it is applied between the two passes.

In this example

```go
	s1 := []int{1, 2, 3}
	Print(s1)

```

we compare `[]int` with `[]T`, match `T` with `int`, and we are done. The single type parameter `T` is `int`, so we infer that the call to `Print` is really a call to `Print[int]`.

For a more complex example, consider

```go
// Map calls the function f on every element of the slice s,
// returning a new slice of the results.
func Map[F, T any](s []F, f func(F) T) []T {
	r := make([]T, len(s))
	for i, v := range s {
		r[i] = f(v)
	}
	return r
}

```

The two type parameters `F` and `T` are both used for input parameters, so function argument type inference is possible. In the call

```go
	strs := Map([]int{1, 2, 3}, strconv.Itoa)

```

we unify `[]int` with `[]F`, matching `F` with `int`. We unify the type of `strconv.Itoa`, which is `func(int) string`, with `func(F) T`, matching `F` with `int` and `T` with `string`. The type parameter `F` is matched twice, both times with `int`. Unification succeeds, so the call written as `Map` is a call of `Map[int, string]`.

To see the untyped constant rule in effect, consider:

```go
// NewPair returns a pair of values of the same type.
func NewPair[F any](f1, f2 F) *Pair[F] { ... }

```

In the call `NewPair(1, 2)` both arguments are untyped constants, so both are ignored in the first pass. There is nothing to unify. We still have two untyped constants after the first pass. Both are set to their default type, `int`. The second run of the type unification pass unifies `F` with `int`, so the final call is `NewPair[int](1, 2)`.

In the call `NewPair(1, int64(2))` the first argument is an untyped constant, so we ignore it in the first pass. We then unify `int64` with `F`. At this point the type parameter corresponding to the untyped constant is fully determined, so the final call is `NewPair[int64](1, int64(2))`.

In the call `NewPair(1, 2.5)` both arguments are untyped constants, so we move on the second pass. This time we set the first constant to `int` and the second to `float64`. We then try to unify `F` with both `int` and `float64`, so unification fails, and we report a compilation error.

As mentioned earlier, function argument type inference is done without regard to constraints. First we use function argument type inference to determine type arguments to use for the function, and then, if that succeeds, we check whether those type arguments implement the constraints (if any).

Note that after successful function argument type inference, the compiler must still check that the arguments can be assigned to the parameters, as for any function call.

#### Constraint type inference

Constraint type inference permits inferring a type argument from another type argument, based on type parameter constraints. Constraint type inference is useful when a function wants to have a type name for an element of some other type parameter, or when a function wants to apply a constraint to a type that is based on some other type parameter.
