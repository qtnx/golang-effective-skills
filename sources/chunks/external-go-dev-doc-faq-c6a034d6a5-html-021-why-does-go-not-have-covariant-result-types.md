---
source_name: "External Linked Documentation"
source_url: "https://go.dev/doc/faq"
source_path: "sources/raw/external/go-dev-doc-faq-c6a034d6a5.html"
license_ref: ""
---

## Types

### Why does Go not have covariant result types?

Covariant result types would mean that an interface like

```go
type Copyable interface {
    Copy() interface{}
}

```

would be satisfied by the method

```go
func (v Value) Copy() Value

```

because `Value` implements the empty interface. In Go method types must match exactly, so `Value` does not implement `Copyable`. Go separates the notion of what a type does—its methods—from the type’s implementation. If two methods return different types, they are not doing the same thing. Programmers who want covariant result types are often trying to express a type hierarchy through interfaces. In Go it’s more natural to have a clean separation between interface and implementation.

# Frequently Asked Questions (FAQ)

## Values

### Why does Go not provide implicit numeric conversions?

The convenience of automatic conversion between numeric types in C is outweighed by the confusion it causes. When is an expression unsigned? How big is the value? Does it overflow? Is the result portable, independent of the machine on which it executes? It also complicates the compiler; C’s “usual arithmetic conversions” are not easy to implement and inconsistent across architectures. For reasons of portability, we decided to make things clear and straightforward at the cost of some explicit conversions in the code. The definition of constants in Go—arbitrary precision values free of signedness and size annotations—ameliorates matters considerably, though.

A related detail is that, unlike in C, `int` and `int64` are distinct types even if `int` is a 64-bit type. The `int` type is generic; if you care about how many bits an integer holds, Go encourages you to be explicit.

### How do constants work in Go?

Although Go is strict about conversion between variables of different numeric types, constants in the language are much more flexible. Literal constants such as `23`, `3.14159` and `math.Pi` occupy a sort of ideal number space, with arbitrary precision and no overflow or underflow. For instance, the value of `math.Pi` is specified to 63 decimal digits in the source code, and constant expressions involving the value keep precision beyond what a `float64` could hold. Only when the constant or constant expression is assigned to a variable—a memory location in the program—does it become a “computer” number with the usual floating-point properties and precision.

Also, because they are just numbers, not typed values, constants in Go can be used more freely than variables, thereby softening some of the awkwardness around the strict conversion rules. One can write expressions such as

```go
sqrt2 := math.Sqrt(2)

```

without complaint from the compiler because the ideal number `2` can be converted safely and accurately to a `float64` for the call to `math.Sqrt`.

A blog post titled Constants explores this topic in more detail.

### Why are maps built in?

The same reason strings are: they are such a powerful and important data structure that providing one excellent implementation with syntactic support makes programming more pleasant. We believe that Go’s implementation of maps is strong enough that it will serve for the vast majority of uses. If a specific application can benefit from a custom implementation, it’s possible to write one but it will not be as convenient syntactically; this seems a reasonable tradeoff.

### Why don’t maps allow slices as keys?

Map lookup requires an equality operator, which slices do not implement. They don’t implement equality because equality is not well defined on such types; there are multiple considerations involving shallow vs. deep comparison, pointer vs. value comparison, how to deal with recursive types, and so on. We may revisit this issue—and implementing equality for slices will not invalidate any existing programs—but without a clear idea of what equality of slices should mean, it was simpler to leave it out for now.

Equality is defined for structs and arrays, so they can be used as map keys.

### Why are maps, slices, and channels references while arrays are values?

There’s a lot of history on that topic. Early on, maps and channels were syntactically pointers and it was impossible to declare or use a non-pointer instance. Also, we struggled with how arrays should work. Eventually we decided that the strict separation of pointers and values made the language harder to use. Changing these types to act as references to the associated, shared data structures resolved these issues. This change added some regrettable complexity to the language but had a large effect on usability: Go became a more productive, comfortable language when it was introduced.
