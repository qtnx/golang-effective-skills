---
source_name: "External Linked Documentation"
source_url: "https://go.dev/design/43651-type-parameters"
source_path: "sources/raw/external/go-dev-design-43651-type-parameters-8b418b79f1.html"
license_ref: ""
---

# Type Parameters Proposal

## Acknowledgements

We‘d like to thank many people on the Go team, many contributors to the Go issue tracker, and all the people who have shared their ideas and their feedback on earlier design drafts. We read all of it, and we’re grateful.

For this version of the proposal in particular we received detailed feedback from Josh Bleecher-Snyder, Jon Bodner, Dave Cheney, Jaana Dogan, Kevin Gillette, Mitchell Hashimoto, Chris Hines, Bill Kennedy, Ayke van Laethem, Daniel Martí, Elena Morozova, Roger Peppe, and Ronna Steinberg.

# Type Parameters Proposal

## Appendix

This appendix covers various details of the design that don't seem significant enough to cover in earlier sections.

### Generic type aliases

A type alias may refer to a generic type, but the type alias may not have its own parameters. This restriction exists because it is unclear how to handle a type alias with type parameters that have constraints.

```go
type VectorAlias = Vector

```

In this case uses of the type alias will have to provide type arguments appropriate for the generic type being aliased.

```go
var v VectorAlias[int]

```

Type aliases may also refer to instantiated types.

```go
type VectorInt = Vector[int]

```

### Instantiating a function

Go normally permits you to refer to a function without passing any arguments, producing a value of function type. You may not do this with a function that has type parameters; all type arguments must be known at compile time. That said, you can instantiate the function, by passing type arguments, but you don't have to call the instantiation. This will produce a function value with no type parameters.

```go
// PrintInts is type func([]int).
var PrintInts = Print[int]

```

### Embedded type parameter

When a generic type is a struct, and the type parameter is embedded as a field in the struct, the name of the field is the name of the type parameter.

```go
// A Lockable is a value that may be safely simultaneously accessed
// from multiple goroutines via the Get and Set methods.
type Lockable[T any] struct {
	T
	mu sync.Mutex
}

// Get returns the value stored in a Lockable.
func (l *Lockable[T]) Get() T {
	l.mu.Lock()
	defer l.mu.Unlock()
	return l.T
}

// Set sets the value in a Lockable.
func (l *Lockable[T]) Set(v T) {
	l.mu.Lock()
	defer l.mu.Unlock()
	l.T = v
}

```

### Embedded type parameter methods

When a generic type is a struct, and the type parameter is embedded as a field in the struct, any methods of the type parameter's constraint are promoted to be methods of the struct. (For purposes of selector resolution <https://golang.org/ref/spec#Selectors>, these methods are treated as being at depth 0 of the type parameter, even if in the actual type argument the methods were themselves promoted from an embedded type.)

```go
// NamedInt is an int with a name. The name can be any type with
// a String method.
type NamedInt[Name fmt.Stringer] struct {
	Name
	val int
}

// Name returns the name of a NamedInt.
func (ni NamedInt[Name]) Name() string {
	// The String method is promoted from the embedded Name.
	return ni.String()
}

```

### Embedded instantiated type

When embedding an instantiated type, the name of the field is the name of type without the type arguments.

```go
type S struct {
	T[int] // field name is T
}

func F(v S) int {
	return v.T // not v.T[int]
}

```

### Generic types as type switch cases

A generic type may be used as the type in a type assertion or as a case in a type switch.

Here are some trivial examples:

```go
func Assertion[T any](v interface{}) (T, bool) {
	t, ok := v.(T)
	return t, ok
}

func Switch[T any](v interface{}) (T, bool) {
	switch v := v.(type) {
	case T:
		return v, true
	default:
		var zero T
		return zero, false
	}
}

```

In a type switch, it's OK if a generic type turns out to duplicate some other case in the type switch. The first matching case is chosen.

```go
func Switch2[T any](v interface{}) int {
	switch v.(type) {
	case T:
		return 0
	case string:
		return 1
	default:
		return 2
	}
}

// S2a will be set to 0.
var S2a = Switch2[string]("a string")

// S2b will be set to 1.
var S2b = Switch2[int]("another string")

```

### Method sets of constraint elements

Much as the type set of an interface type is the intersection of the type sets of the elements of the interface, the method set of an interface type can be defined as the union of the method sets of the elements of the interface. In most cases, an embedded element will have no methods, and as such will not contribute any methods to the interface type. That said, for completeness, we'll note that the method set of `~T` is the method set of `T`. The method set of a union element is the intersection of the method sets of the elements of the union. These rules are implied by the definition of type sets, but they are not needed for understanding the behavior of constraints.

### Permitting constraints as ordinary interface types

This is a feature we are not suggesting now, but could consider for later versions of the language.

We have proposed that constraints can embed some additional elements. With this proposal, any interface type that embeds anything other than an interface type can only be used as a constraint or as an embedded element in another constraint. A natural next step would be to permit using interface types that embed any type, or that embed these new elements, as an ordinary type, not just as a constraint.

We are not proposing that now. But the rules for type sets and method sets above describe how they would behave. Any type that is an element of the type set could be assigned to such an interface type. A value of such an interface type would permit calling any member of the method set.

This would permit a version of what other languages call sum types or union types. It would be a Go interface type to which only specific types could be assigned. Such an interface type could still take the value `nil`, of course, so it would not be quite the same as a typical sum type as found in other languages.

Another natural next step would be to permit approximation elements and union elements in type switch cases. That would make it easier to determine the contents of an interface type that used those elements. That said, approximation elements and union elements are not types, and as such could not be used in type assertions.

### Type inference for composite literals

This is a feature we are not suggesting now, but could consider for later versions of the language.

We could also consider supporting type inference for composite literals of generic types.

```go
type Pair[T any] struct { f1, f2 T }
var V = Pair{1, 2} // inferred as Pair[int]{1, 2}

```

It's not clear how often this will arise in real code.

### Type inference for generic function arguments

This is a feature we are not suggesting now, but could consider for later versions of the language.

In the following example, consider the call to `Find` in `FindClose`. Type inference can determine that the type argument to `Find` is `T4`, and from that we know that the type of the final argument must be `func(T4, T4) bool`, and from that we could deduce that the type argument to `IsClose` must also be `T4`. However, the type inference algorithm described earlier cannot do that, so we must explicitly write `IsClose[T4]`.

This may seem esoteric at first, but it comes up when passing generic functions to generic `Map` and `Filter` functions.

```go
// Differ has a Diff method that returns how different a value is.
type Differ[T1 any] interface {
	Diff(T1) int
}

// IsClose returns whether a and b are close together, based on Diff.
func IsClose[T2 Differ](a, b T2) bool {
	return a.Diff(b) < 2
}

// Find returns the index of the first element in s that matches e,
// based on the cmp function. It returns -1 if no element matches.
func Find[T3 any](s []T3, e T3, cmp func(a, b T3) bool) int {
	for i, v := range s {
		if cmp(v, e) {
			return i
		}
	}
	return -1
}

// FindClose returns the index of the first element in s that is
// close to e, based on IsClose.
func FindClose[T4 Differ](s []T4, e T4) int {
	// With the current type inference algorithm we have to
	// explicitly write IsClose[T4] here, although it
	// is the only type argument we could possibly use.
	return Find(s, e, IsClose[T4])
}

```

### Reflection on type arguments

Although we don‘t suggest changing the reflect package, one possibility to consider for the future would be to add two new methods to `reflect.Type`: `NumTypeArgument() int` would return the number of type arguments to a type, and `TypeArgument(i) Type` would return the i’th type argument. `NumTypeArgument` would return non-zero for an instantiated generic type. Similar methods could be defined for `reflect.Value`, for which `NumTypeArgument` would return non-zero for an instantiated generic function. There might be programs that care about this information.
