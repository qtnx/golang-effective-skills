---
source_name: "External Linked Documentation"
source_url: "https://go.dev/ref/spec"
source_path: "sources/raw/external/go-dev-ref-spec-3c5b020879.html"
license_ref: ""
---

## Declarations and scope

### Type declarations

 A type declaration binds an identifier, the _type name_, to a type. Type declarations come in two forms: alias declarations and type definitions.

```go

TypeDecl = "type" ( TypeSpec | "(" { TypeSpec ";" } ")" ) .
TypeSpec = AliasDecl | TypeDef .

```

#### Alias declarations

 An alias declaration binds an identifier to the given type [Go 1.9].

```go

AliasDecl = identifier [ TypeParameters ] "=" Type .

```

 Within the scope of the identifier, it serves as an _alias_ for the given type.

```go

type (
	nodeList = []*Node  // nodeList and []*Node are identical types
	Polar    = polar    // Polar and polar denote identical types
)

```

 If the alias declaration specifies type parameters [Go 1.24], the type name denotes a _generic alias_. Generic aliases must be instantiated when they are used.

```go

type set[P comparable] = map[P]bool

```

 In an alias declaration the given type cannot be a type parameter declared in the same declaration.

```go

type A[P any] = P   // illegal: P is a type parameter declared in the declaration of A

func f[P any]() {
	type A = P  // ok: T is a type parameter declared by the enclosing function
}

```

#### Type definitions

 A type definition creates a new, distinct type with the same underlying type and operations as the given type and binds an identifier, the _type name_, to it.

```go

TypeDef = identifier [ TypeParameters ] Type .

```

 The new type is called a _defined type_. It is different from any other type, including the type it is created from.

```go

type (
	Point struct{ x, y float64 }  // Point and struct{ x, y float64 } are different types
	polar Point                   // polar and Point denote different types
)

type TreeNode struct {
	left, right *TreeNode
	value any
}

type Block interface {
	BlockSize() int
	Encrypt(src, dst []byte)
	Decrypt(src, dst []byte)
}

```

 A defined type may have methods associated with it. It does not inherit any methods bound to the given type, but the method set of an interface type or of elements of a composite type remains unchanged:

```go

// A Mutex is a data type with two methods, Lock and Unlock.
type Mutex struct         { /* Mutex fields */ }
func (m *Mutex) Lock()    { /* Lock implementation */ }
func (m *Mutex) Unlock()  { /* Unlock implementation */ }

// NewMutex has the same composition as Mutex but its method set is empty.
type NewMutex Mutex

// The method set of PtrMutex's underlying type *Mutex remains unchanged,
// but the method set of PtrMutex is empty.
type PtrMutex *Mutex

// The method set of *PrintableMutex contains the methods
// Lock and Unlock bound to its embedded field Mutex.
type PrintableMutex struct {
	Mutex
}

// MyBlock is an interface type that has the same method set as Block.
type MyBlock Block

```

 Type definitions may be used to define different boolean, numeric, or string types and associate methods with them:

```go

type TimeZone int

const (
	EST TimeZone = -(5 + iota)
	CST
	MST
	PST
)

func (tz TimeZone) String() string {
	return fmt.Sprintf("GMT%+dh", tz)
}

```

 If the type definition specifies type parameters, the type name denotes a _generic type_. Generic types must be instantiated when they are used.

```go

type List[T any] struct {
	next  *List[T]
	value T
}

```

 In a type definition the given type cannot be a type parameter.

```go

type T[P any] P    // illegal: P is a type parameter

func f[P any]() {
	type L P   // illegal: P is a type parameter declared by the enclosing function
}

```

 A generic type may also have methods associated with it. In this case, the method receivers must declare the same number of type parameters as present in the generic type definition.

```go

// The method Len returns the number of elements in the linked list l.
func (l *List[T]) Len() int  { … }

```
