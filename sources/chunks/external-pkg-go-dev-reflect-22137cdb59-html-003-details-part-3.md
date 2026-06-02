---
source_name: "External Linked Documentation"
source_url: "https://pkg.go.dev/reflect"
source_path: "sources/raw/external/pkg-go-dev-reflect-22137cdb59.html"
license_ref: ""
---

// MethodByName returns the method with that name in the type's
	// method set and a boolean indicating if the method was found.
	//
	// For a non-interface type T or *T, the returned Method's Type and Func
	// fields describe a function whose first argument is the receiver.
	//
	// For an interface type, the returned Method's Type field gives the
	// method signature, without a receiver, and the Func field is nil.
	//
	// Calling this method will cause the linker to retain all methods with this name in all packages.
	// If the linker can't determine the name, it will retain all exported methods.
	// This may make the executable binary larger but will not affect execution time.
	MethodByName(string) (Method, bool)

// NumMethod returns the number of methods accessible using Method.
	//
	// For a non-interface type, it returns the number of exported methods.
	//
	// For an interface type, it returns the number of exported and unexported methods.
	NumMethod() int

// Name returns the type's name within its package for a defined type.
	// For other (non-defined) types it returns the empty string.
	Name() string

// PkgPath returns a defined type's package path, that is, the import path
	// that uniquely identifies the package, such as "encoding/base64".
	// If the type was predeclared (string, error) or not defined (*T, struct{},
	// []int, or A where A is an alias for a non-defined type), the package path
	// will be the empty string.
	PkgPath() string

// Size returns the number of bytes needed to store
	// a value of the given type; it is analogous to unsafe.Sizeof.
	Size() uintptr

// String returns a string representation of the type.
	// The string representation may use shortened package names
	// (e.g., base64 instead of "encoding/base64") and is not
	// guaranteed to be unique among types. To test for type identity,
	// compare the Types directly.
	String() string

// Kind returns the specific kind of this type.
	Kind() Kind

// Implements reports whether the type implements the interface type u.
	Implements(u Type) bool

// AssignableTo reports whether a value of the type is assignable to type u.
	AssignableTo(u Type) bool

// ConvertibleTo reports whether a value of the type is convertible to type u.
	// Even if ConvertibleTo returns true, the conversion may still panic.
	// For example, a slice of type []T is convertible to *[N]T,
	// but the conversion will panic if its length is less than N.
	ConvertibleTo(u Type) bool

// Comparable reports whether values of this type are comparable.
	// Even if Comparable returns true, the comparison may still panic.
	// For example, values of interface type are comparable,
	// but the comparison will panic if their dynamic type is not comparable.
	Comparable() bool

// Bits returns the size of the type in bits.
	// It panics if the type's Kind is not one of the
	// sized or unsized Int, Uint, Float, or Complex kinds.
	Bits() int

// ChanDir returns a channel type's direction.
	// It panics if the type's Kind is not Chan.
	ChanDir() ChanDir

// IsVariadic reports whether a function type's final input parameter
	// is a "..." parameter. If so, t.In(t.NumIn() - 1) returns the parameter's
	// implicit actual type []T.
	//
	// For concreteness, if t represents func(x int, y ... float64), then
	//
	//	t.NumIn() == 2
	//	t.In(0) is the reflect.Type for "int"
	//	t.In(1) is the reflect.Type for "[]float64"
	//	t.IsVariadic() == true
	//
	// IsVariadic panics if the type's Kind is not Func.
	IsVariadic() bool

// Elem returns a type's element type.
	// It panics if the type's Kind is not Array, Chan, Map, Pointer, or Slice.
	Elem() Type

// Field returns a struct type's i'th field.
	// It panics if the type's Kind is not Struct.
	// It panics if i is not in the range [0, NumField()).
	Field(i int) StructField

// Fields returns an iterator over each struct field for struct type t. The sequence is
	// equivalent to calling Field successively for each index i in the range [0, NumField()).
	// It panics if the type's Kind is not Struct.
	Fields() iter.Seq[StructField]

// FieldByIndex returns the nested field corresponding
	// to the index sequence. It is equivalent to calling Field
	// successively for each index i.
	// It panics if the type's Kind is not Struct.
	FieldByIndex(index []int) StructField

// FieldByName returns the struct field with the given name
	// and a boolean indicating if the field was found.
	// If the returned field is promoted from an embedded struct,
	// then Offset in the returned StructField is the offset in
	// the embedded struct.
	FieldByName(name string) (StructField, bool)

// FieldByNameFunc returns the struct field with a name
	// that satisfies the match function and a boolean indicating if
	// the field was found.
	//
	// FieldByNameFunc considers the fields in the struct itself
	// and then the fields in any embedded structs, in breadth first order,
	// stopping at the shallowest nesting depth containing one or more
	// fields satisfying the match function. If multiple fields at that depth
	// satisfy the match function, they cancel each other
	// and FieldByNameFunc returns no match.
	// This behavior mirrors Go's handling of name lookup in
	// structs containing embedded fields.
	//
	// If the returned field is promoted from an embedded struct,
	// then Offset in the returned StructField is the offset in
	// the embedded struct.
	FieldByNameFunc(match func(string) bool) (StructField, bool)

// In returns the type of a function type's i'th input parameter.
	// It panics if the type's Kind is not Func.
	// It panics if i is not in the range [0, NumIn()).
	In(i int) Type

// Ins returns an iterator over each input parameter of function type t. The sequence
	// is equivalent to calling In successively for each index i in the range [0, NumIn()).
	// It panics if the type's Kind is not Func.
	Ins() iter.Seq[Type]

// Key returns a map type's key type.
	// It panics if the type's Kind is not Map.
	Key() Type

// Len returns an array type's length.
	// It panics if the type's Kind is not Array.
	Len() int

// NumField returns a struct type's field count.
	// It panics if the type's Kind is not Struct.
	NumField() int

// NumIn returns a function type's input parameter count.
	// It panics if the type's Kind is not Func.
	NumIn() int

// NumOut returns a function type's output parameter count.
	// It panics if the type's Kind is not Func.
	NumOut() int

// Out returns the type of a function type's i'th output parameter.
	// It panics if the type's Kind is not Func.
	// It panics if i is not in the range [0, NumOut()).
	Out(i int) Type

// Outs returns an iterator over each output parameter of function type t. The sequence
	// is equivalent to calling Out successively for each index i in the range [0, NumOut()).
	// It panics if the type's Kind is not Func.
	Outs() iter.Seq[Type]

// OverflowComplex reports whether the complex128 x cannot be represented by type t.
	// It panics if t's Kind is not Complex64 or Complex128.
	OverflowComplex(x complex128) bool

// OverflowFloat reports whether the float64 x cannot be represented by type t.
	// It panics if t's Kind is not Float32 or Float64.
	OverflowFloat(x float64) bool

// OverflowInt reports whether the int64 x cannot be represented by type t.
	// It panics if t's Kind is not Int, Int8, Int16, Int32, or Int64.
	OverflowInt(x int64) bool

// OverflowUint reports whether the uint64 x cannot be represented by type t.
	// It panics if t's Kind is not Uint, Uintptr, Uint8, Uint16, Uint32, or Uint64.
	OverflowUint(x uint64) bool

// CanSeq reports whether a [Value] with this type can be iterated over using [Value.Seq].
	CanSeq() bool

// CanSeq2 reports whether a [Value] with this type can be iterated over using [Value.Seq2].
	CanSeq2() bool
	// contains filtered or unexported methods
}
```

Type is the representation of a Go type.

Not all methods apply to all kinds of types. Restrictions, if any, are noted in the documentation for each method. Use the Kind method to find out the kind of type before calling kind-specific methods. Calling a method inappropriate to the kind of type causes a run-time panic.

Type values are comparable, such as with the == operator, so they can be used as map keys. Two Type values are equal if they represent identical types.

```go
func ArrayOf(length int, elem Type) Type
```

ArrayOf returns the array type with the given length and element type. For example, if t represents int, ArrayOf(5, t) represents [5]int.

If the resulting type would be larger than the available address space, ArrayOf panics.

```go
func ChanOf(dir ChanDir, t Type) Type
```

ChanOf returns the channel type with the given direction and element type. For example, if t represents int, ChanOf(RecvDir, t) represents <-chan int.

The gc runtime imposes a limit of 64 kB on channel element types. If t's size is equal to or exceeds this limit, ChanOf panics.

```go
func FuncOf(in, out []Type, variadic bool) Type
```

FuncOf returns the function type with the given argument and result types. For example if k represents int and e represents string, FuncOf([]Type{k}, []Type{e}, false) represents func(int) string.

The variadic argument controls whether the function is variadic. FuncOf panics if the in[len(in)-1] does not represent a slice and variadic is true.

```go
func MapOf(key, elem Type) Type
```
