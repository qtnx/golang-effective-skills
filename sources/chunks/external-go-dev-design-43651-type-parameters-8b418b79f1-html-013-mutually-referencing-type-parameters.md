---
source_name: "External Linked Documentation"
source_url: "https://go.dev/design/43651-type-parameters"
source_path: "sources/raw/external/go-dev-design-43651-type-parameters-8b418b79f1.html"
license_ref: ""
---

## Design

### Mutually referencing type parameters

Within a single type parameter list, constraints may refer to any of the other type parameters, even ones that are declared later in the same list. (The scope of a type parameter starts at the beginning of the type parameter list and extends to the end of the enclosing function or type declaration.)

For example, consider a generic graph package that contains generic algorithms that work with graphs. The algorithms use two types, `Node` and `Edge`. `Node` is expected to have a method `Edges() []Edge`. `Edge` is expected to have a method `Nodes() (Node, Node)`. A graph can be represented as a `[]Node`.

This simple representation is enough to implement graph algorithms like finding the shortest path.

```go
package graph

// NodeConstraint is the type constraint for graph nodes:
// they must have an Edges method that returns the Edge's
// that connect to this Node.
type NodeConstraint[Edge any] interface {
	Edges() []Edge
}

// EdgeConstraint is the type constraint for graph edges:
// they must have a Nodes method that returns the two Nodes
// that this edge connects.
type EdgeConstraint[Node any] interface {
	Nodes() (from, to Node)
}

// Graph is a graph composed of nodes and edges.
type Graph[Node NodeConstraint[Edge], Edge EdgeConstraint[Node]] struct { ... }

// New returns a new graph given a list of nodes.
func New[Node NodeConstraint[Edge], Edge EdgeConstraint[Node]] (nodes []Node) *Graph[Node, Edge] {
	...
}

// ShortestPath returns the shortest path between two nodes,
// as a list of edges.
func (g *Graph[Node, Edge]) ShortestPath(from, to Node) []Edge { ... }

```

There are a lot of type arguments and instantiations here. In the constraint on `Node` in `Graph`, the `Edge` being passed to the type constraint `NodeConstraint` is the second type parameter of `Graph`. This instantiates `NodeConstraint` with the type parameter `Edge`, so we see that `Node` must have a method `Edges` that returns a slice of `Edge`, which is what we want. The same applies to the constraint on `Edge`, and the same type parameters and constraints are repeated for the function `New`. We aren't claiming that this is simple, but we are claiming that it is possible.

It‘s worth noting that while at first glance this may look like a typical use of interface types, `Node` and `Edge` are non-interface types with specific methods. In order to use `graph.Graph`, the type arguments used for `Node` and `Edge` have to define methods that follow a certain pattern, but they don’t have to actually use interface types to do so. In particular, the methods do not return interface types.

For example, consider these type definitions in some other package:

```go
// Vertex is a node in a graph.
type Vertex struct { ... }

// Edges returns the edges connected to v.
func (v *Vertex) Edges() []*FromTo { ... }

// FromTo is an edge in a graph.
type FromTo struct { ... }

// Nodes returns the nodes that ft connects.
func (ft *FromTo) Nodes() (*Vertex, *Vertex) { ... }

```

There are no interface types here, but we can instantiate `graph.Graph` using the type arguments `*Vertex` and `*FromTo`.

```go
var g = graph.New[*Vertex, *FromTo]([]*Vertex{ ... })

```

`*Vertex` and `*FromTo` are not interface types, but when used together they define methods that implement the constraints of `graph.Graph`. Note that we couldn't pass plain `Vertex` or `FromTo` to `graph.New`, since `Vertex` and `FromTo` do not implement the constraints. The `Edges` and `Nodes` methods are defined on the pointer types `*Vertex` and `*FromTo`; the types `Vertex` and `FromTo` do not have any methods.

When we use a generic interface type as a constraint, we first instantiate the type with the type argument(s) supplied in the type parameter list, and then compare the corresponding type argument against the instantiated constraint. In this example, the `Node` type argument to `graph.New` has a constraint `NodeConstraint[Edge]`. When we call `graph.New` with a `Node` type argument of `*Vertex` and an `Edge` type argument of `*FromTo`, in order to check the constraint on `Node` the compiler instantiates `NodeConstraint` with the type argument `*FromTo`. That produces an instantiated constraint, in this case a requirement that `Node` have a method `Edges() []*FromTo`, and the compiler verifies that `*Vertex` satisfies that constraint.

Although `Node` and `Edge` do not have to be instantiated with interface types, it is also OK to use interface types if you like.

```go
type NodeInterface interface { Edges() []EdgeInterface }
type EdgeInterface interface { Nodes() (NodeInterface, NodeInterface) }

```

We could instantiate `graph.Graph` with the types `NodeInterface` and `EdgeInterface`, since they implement the type constraints. There isn't much reason to instantiate a type this way, but it is permitted.

This ability for type parameters to refer to other type parameters illustrates an important point: it should be a requirement for any attempt to add generics to Go that it be possible to instantiate generic code with multiple type arguments that refer to each other in ways that the compiler can check.
