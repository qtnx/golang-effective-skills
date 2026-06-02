---
source_name: "External Linked Documentation"
source_url: "https://go.dev/doc/faq"
source_path: "sources/raw/external/go-dev-doc-faq-c6a034d6a5.html"
license_ref: ""
---

## Types

### How do I get dynamic dispatch of methods?

The only way to have dynamically dispatched methods is through an interface. Methods on a struct or any other concrete type are always resolved statically.

## Types

### Why is there no type inheritance?

Object-oriented programming, at least in the best-known languages, involves too much discussion of the relationships between types, relationships that often could be derived automatically. Go takes a different approach.

Rather than requiring the programmer to declare ahead of time that two types are related, in Go a type automatically satisfies any interface that specifies a subset of its methods. Besides reducing the bookkeeping, this approach has real advantages. Types can satisfy many interfaces at once, without the complexities of traditional multiple inheritance. Interfaces can be very lightweight—an interface with one or even zero methods can express a useful concept. Interfaces can be added after the fact if a new idea comes along or for testing—without annotating the original types. Because there are no explicit relationships between types and interfaces, there is no type hierarchy to manage or discuss.

It’s possible to use these ideas to construct something analogous to type-safe Unix pipes. For instance, see how `fmt.Fprintf` enables formatted printing to any output, not just a file, or how the `bufio` package can be completely separate from file I/O, or how the `image` packages generate compressed image files. All these ideas stem from a single interface (`io.Writer`) representing a single method (`Write`). And that’s only scratching the surface. Go’s interfaces have a profound influence on how programs are structured.

It takes some getting used to but this implicit style of type dependency is one of the most productive things about Go.
