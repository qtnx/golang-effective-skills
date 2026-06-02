---
source_name: "External Linked Documentation"
source_url: "https://go.dev/doc/faq"
source_path: "sources/raw/external/go-dev-doc-faq-c6a034d6a5.html"
license_ref: ""
---

## Types

### Why doesn’t type T satisfy the Equal interface?

Consider this simple interface to represent an object that can compare itself with another value:

```go
type Equaler interface {
    Equal(Equaler) bool
}

```

and this type, `T`:

```go
type T int
func (t T) Equal(u T) bool { return t == u } // does not satisfy Equaler

```

Unlike the analogous situation in some polymorphic type systems, `T` does not implement `Equaler`. The argument type of `T.Equal` is `T`, not literally the required type `Equaler`.

In Go, the type system does not promote the argument of `Equal`; that is the programmer’s responsibility, as illustrated by the type `T2`, which does implement `Equaler`:

```go
type T2 int
func (t T2) Equal(u Equaler) bool { return t == u.(T2) }  // satisfies Equaler

```

Even this isn’t like other type systems, though, because in Go _any_ type that satisfies `Equaler` could be passed as the argument to `T2.Equal`, and at run time we must check that the argument is of type `T2`. Some languages arrange to make that guarantee at compile time.

A related example goes the other way:

```go
type Opener interface {
   Open() Reader
}

func (t T3) Open() *os.File

```

In Go, `T3` does not satisfy `Opener`, although it might in another language.

While it is true that Go’s type system does less for the programmer in such cases, the lack of subtyping makes the rules about interface satisfaction very easy to state: are the function’s names and signatures exactly those of the interface? Go’s rule is also easy to implement efficiently. We feel these benefits offset the lack of automatic type promotion.
