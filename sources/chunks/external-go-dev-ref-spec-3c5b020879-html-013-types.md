---
source_name: "External Linked Documentation"
source_url: "https://go.dev/ref/spec"
source_path: "sources/raw/external/go-dev-ref-spec-3c5b020879.html"
license_ref: ""
---

## Types
 A type determines a set of values together with operations and methods specific to those values. A type may be denoted by a _type name_, if it has one, which must be followed by type arguments if the type is generic. A type may also be specified using a _type literal_, which composes a type from existing types.
```go
Type     = TypeName [ TypeArgs ] | TypeLit | "(" Type ")" .
TypeName = identifier | QualifiedIdent .
TypeArgs = "[" TypeList [ "," ] "]" .
TypeList = Type { "," Type } .
TypeLit  = ArrayType | StructType | PointerType | FunctionType | InterfaceType |
           SliceType | MapType | ChannelType .
```
 The language predeclares certain type names. Others are introduced with type declarations or type parameter lists. _Composite types_—array, struct, pointer, function, interface, slice, map, and channel types—may be constructed using type literals.
 Predeclared types, defined types, and type parameters are called _named types_. An alias denotes a named type if the type given in the alias declaration is a named type.
