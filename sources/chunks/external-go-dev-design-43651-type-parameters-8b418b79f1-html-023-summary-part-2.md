---
source_name: "External Linked Documentation"
source_url: "https://go.dev/design/43651-type-parameters"
source_path: "sources/raw/external/go-dev-design-43651-type-parameters-8b418b79f1.html"
license_ref: ""
---

## Design

This code will panic when initializing `G`, because the type of `v` in the `NewtonSqrt` function will be `MyFloat`, not `float32` or `float64`. What this function actually wants to test is not the type of `v`, but the approximate type that `v` matched in the constraint's type set.

One way to handle this would be to permit writing approximate types in a type switch, as in `case ~float32:`. Such a case would match any type whose underlying type is `float32`. This would be meaningful, and potentially useful, even in type switches outside of generic functions.
No way to express convertibility
The design has no way to express convertibility between two different type parameters. For example, there is no way to write this function:

```go
// Copy copies values from src to dst, converting them as they go.
// It returns the number of items copied, which is the minimum of
// the lengths of dst and src.
// This implementation is INVALID.
func Copy[T1, T2 any](dst []T1, src []T2) int {
	for i, x := range src {
		if i > len(dst) {
			return i
		}
		dst[i] = T1(x) // INVALID
	}
	return len(src)
}

```

The conversion from type `T2` to type `T1` is invalid, as there is no constraint on either type that permits the conversion. Worse, there is no way to write such a constraint in general. In the particular case where both `T1` and `T2` have limited type sets this function can be written as described earlier when discussing type conversions using type sets. But, for example, there is no way to write a constraint for the case in which `T1` is an interface type and `T2` is a type that implements that interface.

It's worth noting that if `T1` is an interface type then this can be written using a conversion to the empty interface type and a type assertion, but this is, of course, not compile-time type-safe.

```go
// Copy copies values from src to dst, converting them as they go.
// It returns the number of items copied, which is the minimum of
// the lengths of dst and src.
func Copy[T1, T2 any](dst []T1, src []T2) int {
	for i, x := range src {
		if i > len(dst) {
			return i
		}
		dst[i] = (interface{})(x).(T1)
	}
	return len(src)
}

```
No parameterized methods
This design does not permit methods to declare type parameters that are specific to the method. The receiver may have type parameters, but the method may not add any type parameters.

In Go, one of the main roles of methods is to permit types to implement interfaces. It is not clear whether it is reasonably possible to permit parameterized methods to implement interfaces. For example, consider this code, which uses the obvious syntax for parameterized methods. This code uses multiple packages to make the problem clearer.

```go
package p1

// S is a type with a parameterized method Identity.
type S struct{}

// Identity is a simple identity method that works for any type.
func (S) Identity[T any](v T) T { return v }

package p2

// HasIdentity is an interface that matches any type with a
// parameterized Identity method.
type HasIdentity interface {
	Identity[T any](T) T
}

package p3

import "p2"

// CheckIdentity checks the Identity method if it exists.
// Note that although this function calls a parameterized method,
// this function is not itself parameterized.
func CheckIdentity(v interface{}) {
	if vi, ok := v.(p2.HasIdentity); ok {
		if got := vi.Identity[int](0); got != 0 {
			panic(got)
		}
	}
}

package p4

import (
	"p1"
	"p3"
)

// CheckSIdentity passes an S value to CheckIdentity.
func CheckSIdentity() {
	p3.CheckIdentity(p1.S{})
}

```

In this example, we have a type `p1.S` with a parameterized method and a type `p2.HasIdentity` that also has a parameterized method. `p1.S` implements `p2.HasIdentity`. Therefore, the function `p3.CheckIdentity` can call `vi.Identity` with an `int` argument, which in the call from `p4.CheckSIdentity` will be a call to `p1.S.Identity[int]`. But package p3 does not know anything about the type `p1.S`. There may be no other call to `p1.S.Identity` elsewhere in the program. We need to instantiate `p1.S.Identity[int]` somewhere, but how?

We could instantiate it at link time, but in the general case that requires the linker to traverse the complete call graph of the program to determine the set of types that might be passed to `CheckIdentity`. And even that traversal is not sufficient in the general case when type reflection gets involved, as reflection might look up methods based on strings input by the user. So in general instantiating parameterized methods in the linker might require instantiating every parameterized method for every possible type argument, which seems untenable.

Or, we could instantiate it at run time. In general this means using some sort of JIT, or compiling the code to use some sort of reflection based approach. Either approach would be very complex to implement, and would be surprisingly slow at run time.

Or, we could decide that parameterized methods do not, in fact, implement interfaces, but then it's much less clear why we need methods at all. If we disregard interfaces, any parameterized method can be implemented as a parameterized function.

So while parameterized methods seem clearly useful at first glance, we would have to decide what they mean and how to implement that.
No way to require pointer methods
In some cases a parameterized function is naturally written such that it always invokes methods on addressable values. For example, this happens when calling a method on each element of a slice. In such a case, the function only requires that the method be in the slice element type's pointer method set. The type constraints described in this design have no way to write that requirement.

For example, consider a variant of the `Stringify` example we showed earlier.

```go
// Stringify2 calls the String method on each element of s,
// and returns the results.
func Stringify2[T Stringer](s []T) (ret []string) {
	for i := range s {
		ret = append(ret, s[i].String())
	}
	return ret
}

```

Suppose we have a `[]bytes.Buffer` and we want to convert it into a `[]string`. The `Stringify2` function here won‘t help us. We want to write `Stringify2[bytes.Buffer]`, but we can’t, because `bytes.Buffer` doesn‘t have a `String` method. The type that has a `String` method is `*bytes.Buffer`. Writing `Stringify2[*bytes.Buffer]` doesn’t help because that function expects a `[]*bytes.Buffer`, but we have a `[]bytes.Buffer`.

We discussed a similar case in the pointer method example above. There we used constraint type inference to help simplify the problem. Here that doesn‘t help, because `Stringify2` doesn’t really care about calling a pointer method. It just wants a type that has a `String` method, and it's OK if the method is only in the pointer method set, not the value method set. But we also want to accept the case where the method is in the value method set, for example if we really do have a `[]*bytes.Buffer`.

What we need is a way to say that the type constraint applies to either the pointer method set or the value method set. The body of the function would be required to only call the method on addressable values of the type.

It's not clear how often this problem comes up in practice.
No association between float and complex
Constraint type inference lets us give a name to the element of a slice type, and to apply other similar type decompositions. However, there is no way to associate a float type and a complex type. For example, there is no way to write the predeclared `real`, `imag`, or `complex` functions with this design. There is no way to say “if the argument type is `complex64`, then the result type is `float32`.”

One possible approach here would be to permit `real(T)` as a type constraint meaning “the float type associated with the complex type `T`”. Similarly, `complex(T)` would mean “the complex type associated with the floating point type `T`”. Constraint type inference would simplify the call site. However, that would be unlike other type constraints.

#### Discarded ideas

This design is not perfect, and there may be ways to improve it. That said, there are many ideas that we've already considered in detail. This section lists some of those ideas in the hopes that it will help to reduce repetitive discussion. The ideas are presented in the form of a FAQ.
What happened to contracts?
An earlier draft design of generics implemented constraints using a new language construct called contracts. Type sets appeared only in contracts, rather than in interface types. However, many people had a hard time understanding the difference between contracts and interface types. It also turned out that contracts could be represented as a set of corresponding interfaces; there was no loss in expressive power without contracts. We decided to simplify the approach to use only interface types.
Why not use methods instead of type sets?
_Type sets are weird._ _Why not write methods for all operators?_
