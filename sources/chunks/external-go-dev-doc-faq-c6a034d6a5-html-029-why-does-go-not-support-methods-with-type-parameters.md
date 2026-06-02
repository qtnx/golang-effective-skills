---
source_name: "External Linked Documentation"
source_url: "https://go.dev/doc/faq"
source_path: "sources/raw/external/go-dev-doc-faq-c6a034d6a5.html"
license_ref: ""
---

## Type Parameters

### Why does Go not support methods with type parameters?

Go permits a generic type to have methods, but, other than the receiver, the arguments to those methods cannot use parameterized types. We do not anticipate that Go will ever add generic methods.

The problem is how to implement them. Specifically, consider checking whether a value in an interface implements another interface with additional methods. For example, consider this type, an empty struct with a generic `Nop` method that returns its argument, for any possible type:

```go
type Empty struct{}

func (Empty) Nop[T any](x T) T {
    return x
}

```

Now suppose an `Empty` value is stored in an `any` and passed to other code that checks what it can do:

```go
func TryNops(x any) {
    if x, ok := x.(interface{ Nop(string) string }); ok {
        fmt.Printf("string %s\n", x.Nop("hello"))
    }
    if x, ok := x.(interface{ Nop(int) int }); ok {
        fmt.Printf("int %d\n", x.Nop(42))
    }
    if x, ok := x.(interface{ Nop(io.Reader) io.Reader }); ok {
        data, err := io.ReadAll(x.Nop(strings.NewReader("hello world")))
        fmt.Printf("reader %q %v\n", data, err)
    }
}

```

How does that code work if `x` is an `Empty`? It seems that `x` must satisfy all three tests, along with any other form with any other type.

What code runs when those methods are called? For non-generic methods, the compiler generates the code for all method implementations and links them into the final program. But for generic methods, there can be an infinite number of method implementations, so a different strategy is needed.

There are four choices:

-
At link time, make a list of all the possible dynamic interface checks, and then look for types that would satisfy them but are missing compiled methods, and then reinvoke the compiler to add those methods.

This would make builds significantly slower, by needing to stop after linking and repeat some compilations. It would especially slow down incremental builds. Worse, it is possible that the newly compiled method code would itself have new dynamic interface checks, and the process would have to be repeated. Examples can be constructed where the process never even finishes.

-
Implement some kind of JIT, compiling the needed method code at runtime.

Go benefits greatly from the simplicity and predictable performance of being purely ahead-of-time compiled. We are reluctant to take on the complexity of a JIT just to implement one language feature.

-
Arrange to emit a slow fallback for each generic method that uses a table of functions for every possible language operation on the type parameter, and then use that fallback implementation for the dynamic tests.

This approach would make a generic method parameterized by an unexpected type much slower than the same method parameterized by a type observed at compile time. This would make performance much less predictable.

-
Define that generic methods cannot be used to satisfy interfaces at all.

Interfaces are an essential part of programming in Go. Disallowing generic methods from satisfying interfaces is unacceptable from a design point of view.

None of these choices are good ones, so we chose “none of the above.”

Instead of methods with type parameters, use top-level functions with type parameters, or add the type parameters to the receiver type.

For more details, including more examples, see the proposal.
