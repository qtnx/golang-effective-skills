---
source_name: "External Linked Documentation"
source_url: "https://go.dev/ref/spec"
source_path: "sources/raw/external/go-dev-ref-spec-3c5b020879.html"
license_ref: ""
---

## Declarations and scope

### Type parameter declarations

 A type parameter list declares the _type parameters_ of a generic function or type declaration. The type parameter list looks like an ordinary function parameter list except that the type parameter names must all be present and the list is enclosed in square brackets rather than parentheses [Go 1.18].

```go

TypeParameters = "[" TypeParamList [ "," ] "]" .
TypeParamList  = TypeParamDecl { "," TypeParamDecl } .
TypeParamDecl  = IdentifierList TypeConstraint .

```

 All non-blank names in the list must be unique. Each name declares a type parameter, which is a new and different named type that acts as a placeholder for an (as of yet) unknown type in the declaration. The type parameter is replaced with a _type argument_ upon instantiation of the generic function or type.

```go

[P any]
[S interface{ ~[]byte|string }]
[S ~[]E, E any]
[P Constraint[int]]
[_ any]

```

 Just as each ordinary function parameter has a parameter type, each type parameter has a corresponding (meta-)type which is called its _type constraint_.

 A parsing ambiguity arises when the type parameter list for a generic type declares a single type parameter `P` with a constraint `C` such that the text `P C` forms a valid expression:

```go

type T[P *C] …
type T[P (C)] …
type T[P *C|Q] …
…

```

 In these rare cases, the type parameter list is indistinguishable from an expression and the type declaration is parsed as an array type declaration. To resolve the ambiguity, embed the constraint in an interface or use a trailing comma:

```go

type T[P interface{*C}] …
type T[P *C,] …

```

 Type parameters may also be declared by the receiver specification of a method declaration associated with a generic type.

#### Type constraints

 A _type constraint_ is an interface that defines the set of permissible type arguments for the respective type parameter and controls the operations supported by values of that type parameter [Go 1.18].

```go

TypeConstraint = TypeElem .

```

 If the constraint is an interface literal of the form `interface{E}` where `E` is an embedded type element (not a method), in a type parameter list the enclosing `interface{ … }` may be omitted for convenience:

```go

[T []P]                      // = [T interface{[]P}]
[T ~int]                     // = [T interface{~int}]
[T int|string]               // = [T interface{int|string}]
type Constraint ~int         // illegal: ~int is not in a type parameter list

```

 The predeclared interface type `comparable` denotes the set of all non-interface types that are strictly comparable [Go 1.18].

 Even though interfaces that are not type parameters are comparable, they are not strictly comparable and therefore they do not implement `comparable`. However, they satisfy `comparable`.

```go

int                          // implements comparable (int is strictly comparable)
[]byte                       // does not implement comparable (slices cannot be compared)
interface{}                  // does not implement comparable (see above)
interface{ ~int | ~string }  // type parameter only: implements comparable (int, string types are strictly comparable)
interface{ comparable }      // type parameter only: implements comparable (comparable implements itself)
interface{ ~int | ~[]byte }  // type parameter only: does not implement comparable (slices are not comparable)
interface{ ~struct{ any } }  // type parameter only: does not implement comparable (field any is not strictly comparable)

```

 The `comparable` interface and interfaces that (directly or indirectly) embed `comparable` may only be used as type constraints. They cannot be the types of values or variables, or components of other, non-interface types.

#### Satisfying a type constraint

 A type argument `T`_ satisfies_ a type constraint `C` if `T` is an element of the type set defined by `C`; in other words, if `T` implements `C`. As an exception, a strictly comparable type constraint may also be satisfied by a comparable (not necessarily strictly comparable) type argument [Go 1.20]. More precisely:

 A type T _satisfies_ a constraint `C` if

-  `T` implements `C`; or
-  `C` can be written in the form `interface{ comparable; E }`, where `E` is a basic interface and `T` is comparable and implements `E`.

```go

type argument      type constraint                // constraint satisfaction

int                interface{ ~int }              // satisfied: int implements interface{ ~int }
string             comparable                     // satisfied: string implements comparable (string is strictly comparable)
[]byte             comparable                     // not satisfied: slices are not comparable
any                interface{ comparable; int }   // not satisfied: any does not implement interface{ int }
any                comparable                     // satisfied: any is comparable and implements the basic interface any
struct{f any}      comparable                     // satisfied: struct{f any} is comparable and implements the basic interface any
any                interface{ comparable; m() }   // not satisfied: any does not implement the basic interface interface{ m() }
interface{ m() }   interface{ comparable; m() }   // satisfied: interface{ m() } is comparable and implements the basic interface interface{ m() }

```

 Because of the exception in the constraint satisfaction rule, comparing operands of type parameter type may panic at run-time (even though comparable type parameters are always strictly comparable).
