---
source_name: "External Linked Documentation"
source_url: "https://go.dev/ref/spec"
source_path: "sources/raw/external/go-dev-ref-spec-3c5b020879.html"
license_ref: ""
---

## Declarations and scope

### Method declarations

 A method is a function with a _receiver_. A method declaration binds an identifier, the _method name_, to a method, and associates the method with the receiver's _base type_.

```go

MethodDecl = "func" Receiver MethodName Signature [ FunctionBody ] .
Receiver   = Parameters .

```

 The receiver is specified via an extra parameter section preceding the method name. That parameter section must declare a single non-variadic parameter, the receiver. Its type must be a defined type `T` or a pointer to a defined type `T`, possibly followed by a list of type parameter names `[P1, P2, …]` enclosed in square brackets. `T` is called the receiver _base type_. A receiver base type cannot be a pointer or interface type and it must be defined in the same package as the method. The method is said to be _bound_ to its receiver base type and the method name is visible only within selectors for type `T` or `*T`.

 A non-blank receiver identifier must be unique in the method signature. If the receiver's value is not referenced inside the body of the method, its identifier may be omitted in the declaration. The same applies in general to parameters of functions and methods.

 For a base type, the non-blank names of methods bound to it must be unique. If the base type is a struct type, the non-blank method and field names must be distinct.

 Given defined type `Point` the declarations

```go

func (p *Point) Length() float64 {
	return math.Sqrt(p.x * p.x + p.y * p.y)
}

func (p *Point) Scale(factor float64) {
	p.x *= factor
	p.y *= factor
}

```

 bind the methods `Length` and `Scale`, with receiver type `*Point`, to the base type `Point`.

 If the receiver base type is a generic type, the receiver specification must declare corresponding type parameters for the method to use. This makes the receiver type parameters available to the method. Syntactically, this type parameter declaration looks like an instantiation of the receiver base type: the type arguments must be identifiers denoting the type parameters being declared, one for each type parameter of the receiver base type. The type parameter names do not need to match their corresponding parameter names in the receiver base type definition, and all non-blank parameter names must be unique in the receiver parameter section and the method signature. The receiver type parameter constraints are implied by the receiver base type definition: corresponding type parameters have corresponding constraints.

```go

type Pair[A, B any] struct {
	a A
	b B
}

func (p Pair[A, B]) Swap() Pair[B, A]  { … }  // receiver declares A, B
func (p Pair[First, _]) First() First  { … }  // receiver declares First, corresponds to A in Pair

```

 If the receiver type is denoted by (a pointer to) an alias, the alias must not be generic and it must not denote an instantiated generic type, neither directly nor indirectly via another alias, and irrespective of pointer indirections.

```go

type GPoint[P any] = Point
type HPoint        = *GPoint[int]
type IPair         = Pair[int, int]

func (*GPoint[P]) Draw(P)   { … }  // illegal: alias must not be generic
func (HPoint) Draw(P)       { … }  // illegal: alias must not denote instantiated type GPoint[int]
func (*IPair) Second() int  { … }  // illegal: alias must not denote instantiated type Pair[int, int]

```
