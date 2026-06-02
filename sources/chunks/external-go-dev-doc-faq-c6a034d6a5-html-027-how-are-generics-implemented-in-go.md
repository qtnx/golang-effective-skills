---
source_name: "External Linked Documentation"
source_url: "https://go.dev/doc/faq"
source_path: "sources/raw/external/go-dev-doc-faq-c6a034d6a5.html"
license_ref: ""
---

## Type Parameters

### How are generics implemented in Go?

The compiler can choose whether to compile each instantiation separately or whether to compile similar instantiations as a single implementation. The single implementation approach is similar to a function with an interface parameter. Different compilers will make different choices for different cases. The standard Go compiler ordinarily emits a single instantiation for every type argument with the same shape, where the shape is determined by properties of the type such as the size and the location of pointers that it contains. Future releases may experiment with the tradeoff between compile time, run-time efficiency, and code size.

## Type Parameters

### How do generics in Go compare to generics in other languages?

The basic functionality in all languages is similar: it is possible to write types and functions using types that are specified later. That said, there are some differences.

-
Java

In Java, the compiler checks generic types at compile time but removes the types at run time. This is known as type erasure <https://en.wikipedia.org/wiki/Generics_in_Java#Problems_with_type_erasure>. For example, a Java type known as `List<Integer>` at compile time will become the non-generic type `List` at run time. This means, for example, that when using the Java form of type reflection it is impossible to distinguish a value of type `List<Integer>` from a value of type `List<Float>`. In Go the reflection information for a generic type includes the full compile-time type information.

Java uses type wildcards such as `List<? extends Number>` or `List<? super Number>` to implement generic covariance and contravariance. Go does not have these concepts, which makes generic types in Go much simpler.

-
C++

Traditionally C++ templates do not enforce any constraints on type arguments, although C++20 supports optional constraints via concepts <https://en.wikipedia.org/wiki/Concepts_(C%2B%2B)>. In Go constraints are mandatory for all type parameters. C++20 concepts are expressed as small code fragments that must compile with the type arguments. Go constraints are interface types that define the set of all permitted type arguments.

C++ supports template metaprogramming; Go does not. In practice, all C++ compilers compile each template at the point where it is instantiated; as noted above, Go can and does use different approaches for different instantiations.

-
Rust

The Rust version of constraints is known as trait bounds. In Rust the association between a trait bound and a type must be defined explicitly, either in the crate that defines the trait bound or the crate that defines the type. In Go type arguments implicitly satisfy constraints, just as Go types implicitly implement interface types. The Rust standard library defines standard traits for operations such as comparison or addition; the Go standard library does not, as these can be expressed in user code via interface types. The one exception is Go’s `comparable` predefined interface, which captures a property not expressible in the type system.

-
Python

Python is not a statically typed language, so one can reasonably say that all Python functions are always generic by default: they can always be called with values of any type, and any type errors are detected at run time.
