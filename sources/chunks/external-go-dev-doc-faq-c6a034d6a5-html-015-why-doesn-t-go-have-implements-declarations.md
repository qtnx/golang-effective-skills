---
source_name: "External Linked Documentation"
source_url: "https://go.dev/doc/faq"
source_path: "sources/raw/external/go-dev-doc-faq-c6a034d6a5.html"
license_ref: ""
---

## Types

### Why doesn’t Go have “implements” declarations?

A Go type implements an interface by implementing the methods of that interface, nothing more. This property allows interfaces to be defined and used without needing to modify existing code. It enables a kind of structural typing <https://en.wikipedia.org/wiki/Structural_type_system> that promotes separation of concerns and improves code re-use, and makes it easier to build on patterns that emerge as the code develops. The semantics of interfaces is one of the main reasons for Go’s nimble, lightweight feel.

See the question on type inheritance for more detail.

## Types

### How can I guarantee my type satisfies an interface?

You can ask the compiler to check that the type `T` implements the interface `I` by attempting an assignment using the zero value for `T` or pointer to `T`, as appropriate:

```go
type T struct{}
var _ I = T{}       // Verify that T implements I.
var _ I = (*T)(nil) // Verify that *T implements I.

```

If `T` (or `*T`, accordingly) doesn’t implement `I`, the mistake will be caught at compile time.

If you wish the users of an interface to explicitly declare that they implement it, you can add a method with a descriptive name to the interface’s method set. For example:

```go
type Fooer interface {
    Foo()
    ImplementsFooer()
}

```

A type must then implement the `ImplementsFooer` method to be a `Fooer`, clearly documenting the fact and announcing it in go doc’s output.

```go
type Bar struct{}
func (b Bar) ImplementsFooer() {}
func (b Bar) Foo() {}

```

Most code doesn’t make use of such constraints, since they limit the utility of the interface idea. Sometimes, though, they’re necessary to resolve ambiguities among similar interfaces.
