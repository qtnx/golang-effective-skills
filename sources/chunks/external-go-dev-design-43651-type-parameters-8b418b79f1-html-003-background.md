---
source_name: "External Linked Documentation"
source_url: "https://go.dev/design/43651-type-parameters"
source_path: "sources/raw/external/go-dev-design-43651-type-parameters-8b418b79f1.html"
license_ref: ""
---

# Type Parameters Proposal

## Background

There have been many requests to add additional support for generic programming <https://github.com/golang/go/wiki/ExperienceReports#generics> in Go. There has been extensive discussion on the issue tracker <https://golang.org/issue/15292> and on a living document <https://docs.google.com/document/d/1vrAy9gMpMoS3uaVphB32uVXX4pi-HnNjkMEgyAHX4N4/view>.

This design suggests extending the Go language to add a form of parametric polymorphism, where the type parameters are bounded not by a declared subtyping relationship (as in some object oriented languages) but by explicitly defined structural constraints.

This version of the design has many similarities to a design draft presented on July 31, 2019, but contracts have been removed and replaced by interface types, and the syntax has changed.

There have been several proposals for adding type parameters, which can be found through the links above. Many of the ideas presented here have appeared before. The main new features described here are the syntax and the careful examination of interface types as constraints.

This design does not support template metaprogramming or any other form of compile time programming.

As the term _generic_ is widely used in the Go community, we will use it below as a shorthand to mean a function or type that takes type parameters. Don't confuse the term generic as used in this design with the same term in other languages like C++, C#, Java, or Rust; they have similarities but are not the same.
