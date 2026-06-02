---
source_name: "External Linked Documentation"
source_url: "https://go.dev/ref/spec"
source_path: "sources/raw/external/go-dev-ref-spec-3c5b020879.html"
license_ref: ""
---

## Types

### Interface types

 An interface type defines a _type set_. A variable of interface type can store a value of any type that is in the type set of the interface. Such a type is said to implement the interface. The value of an uninitialized variable of interface type is `nil`.

```go

InterfaceType  = "interface" "{" { InterfaceElem ";" } "}" .
InterfaceElem  = MethodElem | TypeElem .
MethodElem     = MethodName Signature .
MethodName     = identifier .
TypeElem       = TypeTerm { "|" TypeTerm } .
TypeTerm       = Type | UnderlyingType .
UnderlyingType = "~" Type .

```

 An interface type is specified by a list of _interface elements_. An interface element is either a _method_ or a _type element_, where a type element is a union of one or more _type terms_. A type term is either a single type or a single underlying type.

#### Basic interfaces

 In its most basic form an interface specifies a (possibly empty) list of methods. The type set defined by such an interface is the set of types which implement all of those methods, and the corresponding method set consists exactly of the methods specified by the interface. Interfaces whose type sets can be defined entirely by a list of methods are called _basic interfaces._

```go

// A simple File interface.
interface {
	Read([]byte) (int, error)
	Write([]byte) (int, error)
	Close() error
}

```

 The name of each explicitly specified method must be unique and not blank.

```go

interface {
	String() string
	String() string  // illegal: String not unique
	_(x int)         // illegal: method must have non-blank name
}

```

 More than one type may implement an interface. For instance, if two types `S1` and `S2` have the method set

```go

func (p T) Read(p []byte) (n int, err error)
func (p T) Write(p []byte) (n int, err error)
func (p T) Close() error

```

 (where `T` stands for either `S1` or `S2`) then the `File` interface is implemented by both `S1` and `S2`, regardless of what other methods `S1` and `S2` may have or share.

 Every type that is a member of the type set of an interface implements that interface. Any given type may implement several distinct interfaces. For instance, all types implement the _empty interface_ which stands for the set of all (non-interface) types:

```go

interface{}

```

 For convenience, the predeclared type `any` is an alias for the empty interface. [Go 1.18]

 Similarly, consider this interface specification, which appears within a type declaration to define an interface called `Locker`:

```go

type Locker interface {
	Lock()
	Unlock()
}

```

 If `S1` and `S2` also implement

```go

func (p T) Lock() { … }
func (p T) Unlock() { … }

```

 they implement the `Locker` interface as well as the `File` interface.

#### Embedded interfaces

 In a slightly more general form an interface `T` may use a (possibly qualified) interface type name `E` as an interface element. This is called _embedding_ interface `E` in `T` [Go 1.14]. The type set of `T` is the _intersection_ of the type sets defined by `T`'s explicitly declared methods and the type sets of `T`’s embedded interfaces. In other words, the type set of `T` is the set of all types that implement all the explicitly declared methods of `T` and also all the methods of `E` [Go 1.18].

```go

type Reader interface {
	Read(p []byte) (n int, err error)
	Close() error
}

type Writer interface {
	Write(p []byte) (n int, err error)
	Close() error
}

// ReadWriter's methods are Read, Write, and Close.
type ReadWriter interface {
	Reader  // includes methods of Reader in ReadWriter's method set
	Writer  // includes methods of Writer in ReadWriter's method set
}

```

 When embedding interfaces, methods with the same names must have identical signatures.

```go

type ReadCloser interface {
	Reader   // includes methods of Reader in ReadCloser's method set
	Close()  // illegal: signatures of Reader.Close and Close are different
}

```

#### General interfaces

 In their most general form, an interface element may also be an arbitrary type term `T`, or a term of the form `~T` specifying the underlying type `T`, or a union of terms `t1|t2|…|tn` [Go 1.18]. Together with method specifications, these elements enable the precise definition of an interface's type set as follows:

- The type set of the empty interface is the set of all non-interface types.
- The type set of a non-empty interface is the intersection of the type sets of its interface elements.
- The type set of a method specification is the set of all non-interface types whose method sets include that method.
- The type set of a non-interface type term is the set consisting of just that type.
- The type set of a term of the form `~T` is the set of all types whose underlying type is `T`.
- The type set of a _union_ of terms `t1|t2|…|tn` is the union of the type sets of the terms.

 The quantification "the set of all non-interface types" refers not just to all (non-interface) types declared in the program at hand, but all possible types in all possible programs, and hence is infinite. Similarly, given the set of all non-interface types that implement a particular method, the intersection of the method sets of those types will contain exactly that method, even if all types in the program at hand always pair that method with another method.

 By construction, an interface's type set never contains an interface type.

```go

// An interface representing only the type int.
interface {
	int
}

// An interface representing all types with underlying type int.
interface {
	~int
}

// An interface representing all types with underlying type int that implement the String method.
interface {
	~int
	String() string
}

// An interface representing an empty type set: there is no type that is both an int and a string.
interface {
	int
	string
}

```

 In a term of the form `~T`, the underlying type of `T` must be itself, and `T` cannot be an interface.

```go

type MyInt int

interface {
	~[]byte  // the underlying type of []byte is itself
	~MyInt   // illegal: the underlying type of MyInt is not MyInt
	~error   // illegal: error is an interface
}

```

 Union elements denote unions of type sets:

```go

// The Float interface represents all floating-point types
// (including any named types whose underlying types are
// either float32 or float64).
type Float interface {
	~float32 | ~float64
}

```

 The type `T` in a term of the form `T` or `~T` cannot be a type parameter, and the type sets of all non-interface terms must be pairwise disjoint (the pairwise intersection of the type sets must be empty). Given a type parameter `P`:

```go

interface {
	P                // illegal: P is a type parameter
	int | ~P         // illegal: P is a type parameter
	~int | MyInt     // illegal: the type sets for ~int and MyInt are not disjoint (~int includes MyInt)
	float32 | Float  // overlapping type sets but Float is an interface
}

```

 Implementation restriction: A union (with more than one term) cannot contain the predeclared identifier `comparable` or interfaces that specify methods, or embed `comparable` or interfaces that specify methods.

 Interfaces that are not basic may only be used as type constraints, or as elements of other interfaces used as constraints. They cannot be the types of values or variables, or components of other, non-interface types.

```go

var x Float                     // illegal: Float is not a basic interface

var x interface{} = Float(nil)  // illegal

type Floatish struct {
	f Float                 // illegal
}

```

 An interface type `T` may not embed a type element that is, contains, or embeds `T`, directly or indirectly.

```go

// illegal: Bad may not embed itself
type Bad interface {
	Bad
}

// illegal: Bad1 may not embed itself using Bad2
type Bad1 interface {
	Bad2
}
type Bad2 interface {
	Bad1
}

// illegal: Bad3 may not embed a union containing Bad3
type Bad3 interface {
	~int | ~string | Bad3
}

// illegal: Bad4 may not embed an array containing Bad4 as element type
type Bad4 interface {
	[10]Bad4
}

```

#### Implementing an interface

 A type `T` implements an interface `I` if

-  `T` is not an interface and is an element of the type set of `I`; or
-  `T` is an interface and the type set of `T` is a subset of the type set of `I`.

 A value of type `T` implements an interface if `T` implements the interface.
