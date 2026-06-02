reflect package - reflect - Go Packages

## Details

-     Valid go.mod <https://cs.opensource.google/go/go/+/go1.26.3:src/go.mod> file
 The Go module system was introduced in Go 1.11 and is the official dependency management solution for Go.

-     Redistributable license
 Redistributable licenses place minimal restrictions on how software can be used, modified, and redistributed.

-     Tagged version
Modules with tagged versions give importers more predictable builds.

-     Stable version
When a project reaches major version v1 it is considered stable.

-  Learn more about best practices

## Repository
   cs.opensource.google/go/go  <https://cs.opensource.google/go/go>

## Links

-    Report a Vulnerability  <https://go.dev/security/policy>

##   Documentation ¶

Package reflect implements run-time reflection, allowing a program to manipulate objects with arbitrary types. The typical use is to take a value with static type interface{} and extract its dynamic type information by calling TypeOf, which returns a Type.

A call to ValueOf returns a Value representing the run-time data. Zero takes a Type and returns a Value representing a zero value for that type.

See "The Laws of Reflection" for an introduction to reflection in Go: https://golang.org/doc/articles/laws_of_reflection.html <https://golang.org/doc/articles/laws_of_reflection.html>

- Constants
-  func Copy(dst, src Value) int
-  func DeepEqual(x, y any) bool
-  func Swapper(slice any) func(i, j int)
-  func TypeAssert[T any](v Value) (T, bool)
-  type ChanDir
-
-  func (d ChanDir) String() string

-  type Kind
-
-  func (k Kind) String() string

-  type MapIter
-
-  func (iter *MapIter) Key() Value
-  func (iter *MapIter) Next() bool
-  func (iter *MapIter) Reset(v Value)
-  func (iter *MapIter) Value() Value

-  type Method
-
-  func (m Method) IsExported() bool

-  type SelectCase
-  type SelectDir
-  type SliceHeaderdeprecated
-  type StringHeaderdeprecated
-  type StructField
-
-  func VisibleFields(t Type) []StructField

-
-  func (f StructField) IsExported() bool

-  type StructTag
-
-  func (tag StructTag) Get(key string) string
-  func (tag StructTag) Lookup(key string) (value string, ok bool)

-  type Type
-
-  func ArrayOf(length int, elem Type) Type
-  func ChanOf(dir ChanDir, t Type) Type
-  func FuncOf(in, out []Type, variadic bool) Type
-  func MapOf(key, elem Type) Type
-  func PointerTo(t Type) Type
-  func PtrTo(t Type) Typedeprecated
-  func SliceOf(t Type) Type
-  func StructOf(fields []StructField) Type
-  func TypeFor[T any]() Type
-  func TypeOf(i any) Type

-  type Value
-
-  func Append(s Value, x ...Value) Value
-  func AppendSlice(s, t Value) Value
-  func Indirect(v Value) Value
-  func MakeChan(typ Type, buffer int) Value
-  func MakeFunc(typ Type, fn func(args []Value) (results []Value)) Value
-  func MakeMap(typ Type) Value
-  func MakeMapWithSize(typ Type, n int) Value
-  func MakeSlice(typ Type, len, cap int) Value
-  func New(typ Type) Value
-  func NewAt(typ Type, p unsafe.Pointer) Value
-  func Select(cases []SelectCase) (chosen int, recv Value, recvOK bool)
-  func SliceAt(typ Type, p unsafe.Pointer, n int) Value
-  func ValueOf(i any) Value
-  func Zero(typ Type) Value

-
-  func (v Value) Addr() Value
-  func (v Value) Bool() bool
-  func (v Value) Bytes() []byte
-  func (v Value) Call(in []Value) []Value
-  func (v Value) CallSlice(in []Value) []Value
-  func (v Value) CanAddr() bool
-  func (v Value) CanComplex() bool
-  func (v Value) CanConvert(t Type) bool
-  func (v Value) CanFloat() bool
-  func (v Value) CanInt() bool
-  func (v Value) CanInterface() bool
-  func (v Value) CanSet() bool
-  func (v Value) CanUint() bool
-  func (v Value) Cap() int
-  func (v Value) Clear()
-  func (v Value) Close()
-  func (v Value) Comparable() bool
-  func (v Value) Complex() complex128
-  func (v Value) Convert(t Type) Value
-  func (v Value) Elem() Value
-  func (v Value) Equal(u Value) bool
-  func (v Value) Field(i int) Value
-  func (v Value) FieldByIndex(index []int) Value
-  func (v Value) FieldByIndexErr(index []int) (Value, error)
-  func (v Value) FieldByName(name string) Value
-  func (v Value) FieldByNameFunc(match func(string) bool) Value
-  func (v Value) Fields() iter.Seq2[StructField, Value]
-  func (v Value) Float() float64
-  func (v Value) Grow(n int)
-  func (v Value) Index(i int) Value
-  func (v Value) Int() int64
-  func (v Value) Interface() (i any)
-  func (v Value) InterfaceData() [2]uintptrdeprecated
-  func (v Value) IsNil() bool
-  func (v Value) IsValid() bool
-  func (v Value) IsZero() bool
-  func (v Value) Kind() Kind
-  func (v Value) Len() int
-  func (v Value) MapIndex(key Value) Value
-  func (v Value) MapKeys() []Value
-  func (v Value) MapRange() *MapIter
-  func (v Value) Method(i int) Value
-  func (v Value) MethodByName(name string) Value
-  func (v Value) Methods() iter.Seq2[Method, Value]
-  func (v Value) NumField() int
-  func (v Value) NumMethod() int
-  func (v Value) OverflowComplex(x complex128) bool
-  func (v Value) OverflowFloat(x float64) bool
-  func (v Value) OverflowInt(x int64) bool
-  func (v Value) OverflowUint(x uint64) bool
-  func (v Value) Pointer() uintptr
-  func (v Value) Recv() (x Value, ok bool)
-  func (v Value) Send(x Value)
-  func (v Value) Seq() iter.Seq[Value]
-  func (v Value) Seq2() iter.Seq2[Value, Value]
-  func (v Value) Set(x Value)
-  func (v Value) SetBool(x bool)
-  func (v Value) SetBytes(x []byte)
-  func (v Value) SetCap(n int)
-  func (v Value) SetComplex(x complex128)
-  func (v Value) SetFloat(x float64)
-  func (v Value) SetInt(x int64)
-  func (v Value) SetIterKey(iter *MapIter)
-  func (v Value) SetIterValue(iter *MapIter)
-  func (v Value) SetLen(n int)
-  func (v Value) SetMapIndex(key, elem Value)
-  func (v Value) SetPointer(x unsafe.Pointer)
-  func (v Value) SetString(x string)
-  func (v Value) SetUint(x uint64)
-  func (v Value) SetZero()
-  func (v Value) Slice(i, j int) Value
-  func (v Value) Slice3(i, j, k int) Value
-  func (v Value) String() string
-  func (v Value) TryRecv() (x Value, ok bool)
-  func (v Value) TrySend(x Value) bool
-  func (v Value) Type() Type
-  func (v Value) Uint() uint64
-  func (v Value) UnsafeAddr() uintptr
-  func (v Value) UnsafePointer() unsafe.Pointer

-  type ValueError
-
-  func (e *ValueError) Error() string

- Bugs

- Kind
- MakeFunc
- StructOf
- StructTag
- StructTag.Lookup
- TypeOf
- Value.FieldByIndex
- Value.FieldByName

   View Source <https://cs.opensource.google/go/go/+/go1.26.3:src/reflect/type.go;l=333>
```go
const Ptr = Pointer
```

Ptr is the old name for the Pointer kind.

This section is empty.

```go
func Copy(dst, src Value) int
```

Copy copies the contents of src into dst until either dst has been filled or src has been exhausted. It returns the number of elements copied. Dst and src each must have kind Slice or Array, and dst and src must have the same element type. It dst is an Array, it panics if Value.CanSet returns false.

As a special case, src can have kind String if the element type of dst is kind Uint8.

```go
func DeepEqual(x, y any) bool
```

DeepEqual reports whether x and y are “deeply equal,” defined as follows. Two values of identical type are deeply equal if one of the following cases applies. Values of distinct types are never deeply equal.

Array values are deeply equal when their corresponding elements are deeply equal.

Struct values are deeply equal if their corresponding fields, both exported and unexported, are deeply equal.

Func values are deeply equal if both are nil; otherwise they are not deeply equal.

Interface values are deeply equal if they hold deeply equal concrete values.

Map values are deeply equal when all of the following are true: they are both nil or both non-nil, they have the same length, and either they are the same map object or their corresponding keys (matched using Go equality) map to deeply equal values.

Pointer values are deeply equal if they are equal using Go's == operator or if they point to deeply equal values.

Slice values are deeply equal when all of the following are true: they are both nil or both non-nil, they have the same length, and either they point to the same initial entry of the same underlying array (that is, &x[0] == &y[0]) or their corresponding elements (up to length) are deeply equal. Note that a non-nil empty slice and a nil slice (for example, []byte{} and []byte(nil)) are not deeply equal.

Other values - numbers, bools, strings, and channels - are deeply equal if they are equal using Go's == operator.

In general DeepEqual is a recursive relaxation of Go's == operator. However, this idea is impossible to implement without some inconsistency. Specifically, it is possible for a value to be unequal to itself, either because it is of func type (uncomparable in general) or because it is a floating-point NaN value (not equal to itself in floating-point comparison), or because it is an array, struct, or interface containing such a value. On the other hand, pointer values are always equal to themselves, even if they point at or contain such problematic values, because they compare equal using Go's == operator, and that is a sufficient condition to be deeply equal, regardless of content. DeepEqual has been defined so that the same short-cut applies to slices and maps: if x and y are the same slice or the same map, they are deeply equal regardless of content.

As DeepEqual traverses the data values it may find a cycle. The second and subsequent times that DeepEqual compares two pointer values that have been compared before, it treats the values as equal rather than examining the values to which they point. This ensures that DeepEqual terminates.

```go
func Swapper(slice any) func(i, j int)
```

Swapper returns a function that swaps the elements in the provided slice.

Swapper panics if the provided interface is not a slice.

```go
func TypeAssert[T any](v Value) (T, bool)
```

TypeAssert is semantically equivalent to:

```go
v2, ok := v.Interface().(T)

```

```go
type ChanDir int
```

ChanDir represents a channel type's direction.

```go
const (
	RecvDir ChanDir             = 1 << iota // <-chan
	SendDir                                 // chan<-
	BothDir = RecvDir | SendDir             // chan
)
```

```go
func (d ChanDir) String() string
```

```go
type Kind uint
```

A Kind represents the specific kind of type that a Type represents. The zero Kind is not a valid kind.

```go

package main

import (
	"fmt"
	"reflect"
)

func main() {
	for _, v := range []any{"hi", 42, func() {}} {
		switch v := reflect.ValueOf(v); v.Kind() {
		case reflect.String:
			fmt.Println(v.String())
		case reflect.Int, reflect.Int8, reflect.Int16, reflect.Int32, reflect.Int64:
			fmt.Println(v.Int())
		default:
			fmt.Printf("unhandled kind %s", v.Kind())
		}
	}

}

```

```go
Output:
hi
42
unhandled kind func

```

 Share Format Run

```go
const (
	Invalid Kind = iota
	Bool
	Int
	Int8
	Int16
	Int32
	Int64
	Uint
	Uint8
	Uint16
	Uint32
	Uint64
	Uintptr
	Float32
	Float64
	Complex64
	Complex128
	Array
	Chan
	Func
	Interface
	Map
	Pointer
	Slice
	String
	Struct
	UnsafePointer
)
```

```go
func (k Kind) String() string
```

String returns the name of k.

```go
type MapIter struct {
	// contains filtered or unexported fields
}
```

A MapIter is an iterator for ranging over a map. See Value.MapRange.

```go
func (iter *MapIter) Key() Value
```

Key returns the key of iter's current map entry.

```go
func (iter *MapIter) Next() bool
```

Next advances the map iterator and reports whether there is another entry. It returns false when iter is exhausted; subsequent calls to MapIter.Key, MapIter.Value, or MapIter.Next will panic.

```go
func (iter *MapIter) Reset(v Value)
```

Reset modifies iter to iterate over v. It panics if v's Kind is not Map and v is not the zero Value. Reset(Value{}) causes iter to not to refer to any map, which may allow the previously iterated-over map to be garbage collected.

```go
func (iter *MapIter) Value() Value
```

Value returns the value of iter's current map entry.

```go
type Method struct {
	// Name is the method name.
	Name string

	// PkgPath is the package path that qualifies a lower case (unexported)
	// method name. It is empty for upper case (exported) method names.
	// The combination of PkgPath and Name uniquely identifies a method
	// in a method set.
	// See https://golang.org/ref/spec#Uniqueness_of_identifiers <https://golang.org/ref/spec#Uniqueness_of_identifiers>
	PkgPath string

	Type  Type  // method type
	Func  Value // func with receiver as first argument
	Index int   // index for Type.Method
}
```

Method represents a single method.

```go
func (m Method) IsExported() bool
```

IsExported reports whether the method is exported.

```go
type SelectCase struct {
	Dir  SelectDir // direction of case
	Chan Value     // channel to use (for send or receive)
	Send Value     // value to send (for send)
}
```

A SelectCase describes a single case in a select operation. The kind of case depends on Dir, the communication direction.

If Dir is SelectDefault, the case represents a default case. Chan and Send must be zero Values.

If Dir is SelectSend, the case represents a send operation. Normally Chan's underlying value must be a channel, and Send's underlying value must be assignable to the channel's element type. As a special case, if Chan is a zero Value, then the case is ignored, and the field Send will also be ignored and may be either zero or non-zero.

If Dir is SelectRecv, the case represents a receive operation. Normally Chan's underlying value must be a channel and Send must be a zero Value. If Chan is a zero Value, then the case is ignored, but Send must still be a zero Value. When a receive operation is selected, the received Value is returned by Select.

```go
type SelectDir int
```

A SelectDir describes the communication direction of a select case.

```go
const (
	SelectSend    SelectDir // case Chan <- Send
	SelectRecv              // case <-Chan:
	SelectDefault           // default
)
```

```go
type SliceHeader struct {
}
```

SliceHeader is the runtime representation of a slice. It cannot be used safely or portably and its representation may change in a later release. Moreover, the Data field is not sufficient to guarantee the data it references will not be garbage collected, so programs must keep a separate, correctly typed pointer to the underlying data.

Deprecated: Use unsafe.Slice or unsafe.SliceData instead.

```go
type StringHeader struct {
}
```

StringHeader is the runtime representation of a string. It cannot be used safely or portably and its representation may change in a later release. Moreover, the Data field is not sufficient to guarantee the data it references will not be garbage collected, so programs must keep a separate, correctly typed pointer to the underlying data.

Deprecated: Use unsafe.String or unsafe.StringData instead.

```go
type StructField struct {
	// Name is the field name.
	Name string

	// PkgPath is the package path that qualifies a lower case (unexported)
	// field name. It is empty for upper case (exported) field names.
	// See https://golang.org/ref/spec#Uniqueness_of_identifiers <https://golang.org/ref/spec#Uniqueness_of_identifiers>
	PkgPath string

	Type      Type      // field type
	Tag       StructTag // field tag string
	Offset    uintptr   // offset within struct, in bytes
	Index     []int     // index sequence for Type.FieldByIndex
	Anonymous bool      // is an embedded field
}
```

A StructField describes a single field in a struct.

```go
func VisibleFields(t Type) []StructField
```

VisibleFields returns all the visible fields in t, which must be a struct type. A field is defined as visible if it's accessible directly with a FieldByName call. The returned fields include fields inside anonymous struct members and unexported fields. They follow the same order found in the struct, with anonymous fields followed immediately by their promoted fields.

For each element e of the returned slice, the corresponding field can be retrieved from a value v of type t by calling v.FieldByIndex(e.Index).

```go
func (f StructField) IsExported() bool
```

IsExported reports whether the field is exported.

```go
type StructTag string
```

A StructTag is the tag string in a struct field.

By convention, tag strings are a concatenation of optionally space-separated key:"value" pairs. Each key is a non-empty string consisting of non-control characters other than space (U+0020 ' '), quote (U+0022 '"'), and colon (U+003A ':'). Each value is quoted using U+0022 '"' characters and Go string literal syntax.

```go

package main

import (
	"fmt"
	"reflect"
)

func main() {
	type S struct {
		F string `species:"gopher" color:"blue"`
	}

	s := S{}
	st := reflect.TypeOf(s)
	field := st.Field(0)
	fmt.Println(field.Tag.Get("color"), field.Tag.Get("species"))

}

```

```go
Output:
blue gopher

```

 Share Format Run

```go
func (tag StructTag) Get(key string) string
```

Get returns the value associated with key in the tag string. If there is no such key in the tag, Get returns the empty string. If the tag does not have the conventional format, the value returned by Get is unspecified. To determine whether a tag is explicitly set to the empty string, use StructTag.Lookup.

```go
func (tag StructTag) Lookup(key string) (value string, ok bool)
```

Lookup returns the value associated with key in the tag string. If the key is present in the tag the value (which may be empty) is returned. Otherwise the returned value will be the empty string. The ok return value reports whether the value was explicitly set in the tag string. If the tag does not have the conventional format, the value returned by Lookup is unspecified.

```go

package main

import (
	"fmt"
	"reflect"
)

func main() {
	type S struct {
		F0 string `alias:"field_0"`
		F1 string `alias:""`
		F2 string
	}

	s := S{}
	st := reflect.TypeOf(s)
	for field := range st.Fields() {
		if alias, ok := field.Tag.Lookup("alias"); ok {
			if alias == "" {
				fmt.Println("(blank)")
			} else {
				fmt.Println(alias)
			}
		} else {
			fmt.Println("(not specified)")
		}
	}

}

```

```go
Output:
field_0
(blank)
(not specified)

```

 Share Format Run

```go
type Type interface {

	// Align returns the alignment in bytes of a value of
	// this type when allocated in memory.
	Align() int

	// FieldAlign returns the alignment in bytes of a value of
	// this type when used as a field in a struct.
	FieldAlign() int

	// Method returns the i'th method in the type's method set.
	// It panics if i is not in the range [0, NumMethod()).
	//
	// For a non-interface type T or *T, the returned Method's Type and Func
	// fields describe a function whose first argument is the receiver,
	// and only exported methods are accessible.
	//
	// For an interface type, the returned Method's Type field gives the
	// method signature, without a receiver, and the Func field is nil.
	//
	// Methods are sorted in lexicographic order.
	//
	// Calling this method will force the linker to retain all exported methods in all packages.
	// This may make the executable binary larger but will not affect execution time.
	Method(int) Method

	// Methods returns an iterator over each method in the type's method set. The sequence is
	// equivalent to calling Method successively for each index i in the range [0, NumMethod()).
	Methods() iter.Seq[Method]

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

MapOf returns the map type with the given key and element types. For example, if k represents int and e represents string, MapOf(k, e) represents map[int]string.

If the key type is not a valid map key type (that is, if it does not implement Go's == operator), MapOf panics.

```go
func PointerTo(t Type) Type
```

PointerTo returns the pointer type with element t. For example, if t represents type Foo, PointerTo(t) represents *Foo.

```go
func PtrTo(t Type) Type
```

PtrTo returns the pointer type with element t. For example, if t represents type Foo, PtrTo(t) represents *Foo.

PtrTo is the old spelling of PointerTo. The two functions behave identically.

Deprecated: Superseded by PointerTo.

```go
func SliceOf(t Type) Type
```

SliceOf returns the slice type with element type t. For example, if t represents int, SliceOf(t) represents []int.

```go
func StructOf(fields []StructField) Type
```

StructOf returns the struct type containing fields. The Offset and Index fields are ignored and computed as they would be by the compiler.

StructOf currently does not support promoted methods of embedded fields and panics if passed unexported StructFields.

```go

package main

import (
	"bytes"
	"encoding/json"
	"fmt"
	"reflect"
)

func main() {
	typ := reflect.StructOf([]reflect.StructField{
		{
			Name: "Height",
			Type: reflect.TypeOf(float64(0)),
			Tag:  `json:"height"`,
		},
		{
			Name: "Age",
			Type: reflect.TypeOf(int(0)),
			Tag:  `json:"age"`,
		},
	})

	v := reflect.New(typ).Elem()
	v.Field(0).SetFloat(0.4)
	v.Field(1).SetInt(2)
	s := v.Addr().Interface()

	w := new(bytes.Buffer)
	if err := json.NewEncoder(w).Encode(s); err != nil {
		panic(err)
	}

	fmt.Printf("value: %+v\n", s)
	fmt.Printf("json:  %s", w.Bytes())

	r := bytes.NewReader([]byte(`{"height":1.5,"age":10}`))
	if err := json.NewDecoder(r).Decode(s); err != nil {
		panic(err)
	}
	fmt.Printf("value: %+v\n", s)

}

```

```go
Output:
value: &{Height:0.4 Age:2}
json:  {"height":0.4,"age":2}
value: &{Height:1.5 Age:10}

```

 Share Format Run

```go
func TypeFor[T any]() Type
```

TypeFor returns the Type that represents the type argument T.

```go
func TypeOf(i any) Type
```

TypeOf returns the reflection Type that represents the dynamic type of i. If i is a nil interface value, TypeOf returns nil.

```go

package main

import (
	"fmt"
	"io"
	"os"
	"reflect"
)

func main() {
	// As interface types are only used for static typing, a
	// common idiom to find the reflection Type for an interface
	// type Foo is to use a *Foo value.
	writerType := reflect.TypeOf((*io.Writer)(nil)).Elem()

	fileType := reflect.TypeOf((*os.File)(nil))
	fmt.Println(fileType.Implements(writerType))

}

```

```go
Output:
true

```

 Share Format Run

```go
type Value struct {
	// contains filtered or unexported fields
}
```

Value is the reflection interface to a Go value.

Not all methods apply to all kinds of values. Restrictions, if any, are noted in the documentation for each method. Use the Kind method to find out the kind of value before calling kind-specific methods. Calling a method inappropriate to the kind of type causes a run time panic.

The zero Value represents no value. Its Value.IsValid method returns false, its Kind method returns Invalid, its String method returns "<invalid Value>", and all other methods panic. Most functions and methods never return an invalid value. If one does, its documentation states the conditions explicitly.

A Value can be used concurrently by multiple goroutines provided that the underlying Go value can be used concurrently for the equivalent direct operations.

To compare two Values, compare the results of the Interface method. Using == on two Values does not compare the underlying values they represent.

```go
func Append(s Value, x ...Value) Value
```

Append appends the values x to a slice s and returns the resulting slice. As in Go, each x's value must be assignable to the slice's element type.

```go
func AppendSlice(s, t Value) Value
```

AppendSlice appends a slice t to a slice s and returns the resulting slice. The slices s and t must have the same element type.

```go
func Indirect(v Value) Value
```

Indirect returns the value that v points to. If v is a nil pointer, Indirect returns a zero Value. If v is not a pointer, Indirect returns v.

```go
func MakeChan(typ Type, buffer int) Value
```

MakeChan creates a new channel with the specified type and buffer size.

```go
func MakeFunc(typ Type, fn func(args []Value) (results []Value)) Value
```

MakeFunc returns a new function of the given Type that wraps the function fn. When called, that new function does the following:

- converts its arguments to a slice of Values.
- runs results := fn(args).
- returns the results as a slice of Values, one per formal result.

The implementation fn can assume that the argument Value slice has the number and type of arguments given by typ. If typ describes a variadic function, the final Value is itself a slice representing the variadic arguments, as in the body of a variadic function. The result Value slice returned by fn must have the number and type of results given by typ.

The Value.Call method allows the caller to invoke a typed function in terms of Values; in contrast, MakeFunc allows the caller to implement a typed function in terms of Values.

The Examples section of the documentation includes an illustration of how to use MakeFunc to build a swap function for different types.

```go

package main

import (
	"fmt"
	"reflect"
)

func main() {
	// swap is the implementation passed to MakeFunc.
	// It must work in terms of reflect.Values so that it is possible
	// to write code without knowing beforehand what the types
	// will be.
	swap := func(in []reflect.Value) []reflect.Value {
		return []reflect.Value{in[1], in[0]}
	}

	// makeSwap expects fptr to be a pointer to a nil function.
	// It sets that pointer to a new function created with MakeFunc.
	// When the function is invoked, reflect turns the arguments
	// into Values, calls swap, and then turns swap's result slice
	// into the values returned by the new function.
	makeSwap := func(fptr any) {
		// fptr is a pointer to a function.
		// Obtain the function value itself (likely nil) as a reflect.Value
		// so that we can query its type and then set the value.
		fn := reflect.ValueOf(fptr).Elem()

		// Make a function of the right type.
		v := reflect.MakeFunc(fn.Type(), swap)

		// Assign it to the value fn represents.
		fn.Set(v)
	}

	// Make and call a swap function for ints.
	var intSwap func(int, int) (int, int)
	makeSwap(&intSwap)
	fmt.Println(intSwap(0, 1))

	// Make and call a swap function for float64s.
	var floatSwap func(float64, float64) (float64, float64)
	makeSwap(&floatSwap)
	fmt.Println(floatSwap(2.72, 3.14))

}

```

```go
Output:
1 0
3.14 2.72

```

 Share Format Run

```go
func MakeMap(typ Type) Value
```

MakeMap creates a new map with the specified type.

```go
func MakeMapWithSize(typ Type, n int) Value
```

MakeMapWithSize creates a new map with the specified type and initial space for approximately n elements.

```go
func MakeSlice(typ Type, len, cap int) Value
```

MakeSlice creates a new zero-initialized slice value for the specified slice type, length, and capacity.

```go
func New(typ Type) Value
```

New returns a Value representing a pointer to a new zero value for the specified type. That is, the returned Value's Type is PointerTo(typ).

```go
func NewAt(typ Type, p unsafe.Pointer) Value
```

NewAt returns a Value representing a pointer to a value of the specified type, using p as that pointer.

```go
func Select(cases []SelectCase) (chosen int, recv Value, recvOK bool)
```

Select executes a select operation described by the list of cases. Like the Go select statement, it blocks until at least one of the cases can proceed, makes a uniform pseudo-random choice, and then executes that case. It returns the index of the chosen case and, if that case was a receive operation, the value received and a boolean indicating whether the value corresponds to a send on the channel (as opposed to a zero value received because the channel is closed). Select supports a maximum of 65536 cases.

```go
func SliceAt(typ Type, p unsafe.Pointer, n int) Value
```

SliceAt returns a Value representing a slice whose underlying data starts at p, with length and capacity equal to n.

This is like unsafe.Slice.

```go
func ValueOf(i any) Value
```

ValueOf returns a new Value initialized to the concrete value stored in the interface i. ValueOf(nil) returns the zero Value.

```go
func Zero(typ Type) Value
```

Zero returns a Value representing the zero value for the specified type. The result is different from the zero value of the Value struct, which represents no value at all. For example, Zero(TypeOf(42)) returns a Value with Kind Int and value 0. The returned value is neither addressable nor settable.

```go
func (v Value) Addr() Value
```

Addr returns a pointer value representing the address of v. It panics if Value.CanAddr returns false. Addr is typically used to obtain a pointer to a struct field or slice element in order to call a method that requires a pointer receiver.

```go
func (v Value) Bool() bool
```

Bool returns v's underlying value. It panics if v's kind is not Bool.

```go
func (v Value) Bytes() []byte
```

Bytes returns v's underlying value. It panics if v's underlying value is not a slice of bytes or an addressable array of bytes.

```go
func (v Value) Call(in []Value) []Value
```

Call calls the function v with the input arguments in. For example, if len(in) == 3, v.Call(in) represents the Go call v(in[0], in[1], in[2]). Call panics if v's Kind is not Func. It returns the output results as Values. As in Go, each input argument must be assignable to the type of the function's corresponding input parameter. If v is a variadic function, Call creates the variadic slice parameter itself, copying in the corresponding values. It panics if the Value was obtained by accessing unexported struct fields.

```go
func (v Value) CallSlice(in []Value) []Value
```

CallSlice calls the variadic function v with the input arguments in, assigning the slice in[len(in)-1] to v's final variadic argument. For example, if len(in) == 3, v.CallSlice(in) represents the Go call v(in[0], in[1], in[2]...). CallSlice panics if v's Kind is not Func or if v is not variadic. It returns the output results as Values. As in Go, each input argument must be assignable to the type of the function's corresponding input parameter. It panics if the Value was obtained by accessing unexported struct fields.

```go
func (v Value) CanAddr() bool
```

CanAddr reports whether the value's address can be obtained with Value.Addr. Such values are called addressable. A value is addressable if it is an element of a slice, an element of an addressable array, a field of an addressable struct, or the result of dereferencing a pointer. If CanAddr returns false, calling Value.Addr will panic.

```go
func (v Value) CanComplex() bool
```

CanComplex reports whether Value.Complex can be used without panicking.

```go
func (v Value) CanConvert(t Type) bool
```

CanConvert reports whether the value v can be converted to type t. If v.CanConvert(t) returns true then v.Convert(t) will not panic.

```go
func (v Value) CanFloat() bool
```

CanFloat reports whether Value.Float can be used without panicking.

```go
func (v Value) CanInt() bool
```

CanInt reports whether Int can be used without panicking.

```go
func (v Value) CanInterface() bool
```

CanInterface reports whether Value.Interface can be used without panicking.

```go
func (v Value) CanSet() bool
```

CanSet reports whether the value of v can be changed. A Value can be changed only if it is addressable and was not obtained by the use of unexported struct fields. If CanSet returns false, calling Value.Set or any type-specific setter (e.g., Value.SetBool, Value.SetInt) will panic.

```go
func (v Value) CanUint() bool
```

CanUint reports whether Value.Uint can be used without panicking.

```go
func (v Value) Cap() int
```

Cap returns v's capacity. It panics if v's Kind is not Array, Chan, Slice or pointer to Array.

```go
func (v Value) Clear()
```

Clear clears the contents of a map or zeros the contents of a slice.

It panics if v's Kind is not Map or Slice.

```go
func (v Value) Close()
```

Close closes the channel v. It panics if v's Kind is not Chan or v is a receive-only channel.

```go
func (v Value) Comparable() bool
```

Comparable reports whether the value v is comparable. If the type of v is an interface, this checks the dynamic type. If this reports true then v.Interface() == x will not panic for any x, nor will v.Equal(u) for any Value u.

```go
func (v Value) Complex() complex128
```

Complex returns v's underlying value, as a complex128. It panics if v's Kind is not Complex64 or Complex128

```go
func (v Value) Convert(t Type) Value
```

Convert returns the value v converted to type t. If the usual Go conversion rules do not allow conversion of the value v to type t, or if converting v to type t panics, Convert panics.

```go
func (v Value) Elem() Value
```

Elem returns the value that the interface v contains or that the pointer v points to. It panics if v's Kind is not Interface or Pointer. It returns the zero Value if v is nil.

```go
func (v Value) Equal(u Value) bool
```

Equal reports true if v is equal to u. For two invalid values, Equal will report true. For an interface value, Equal will compare the value within the interface. Otherwise, If the values have different types, Equal will report false. Otherwise, for arrays and structs Equal will compare each element in order, and report false if it finds non-equal elements. During all comparisons, if values of the same type are compared, and the type is not comparable, Equal will panic.

```go
func (v Value) Field(i int) Value
```

Field returns the i'th field of the struct v. It panics if v's Kind is not Struct or i is out of range.

```go
func (v Value) FieldByIndex(index []int) Value
```

FieldByIndex returns the nested field corresponding to index. It panics if evaluation requires stepping through a nil pointer or a field that is not a struct.

```go

package main

import (
	"fmt"
	"reflect"
)

func main() {
	// This example shows a case in which the name of a promoted field
	// is hidden by another field: FieldByName will not work, so
	// FieldByIndex must be used instead.
	type user struct {
		firstName string
		lastName  string
	}

	type data struct {
		user
		firstName string
		lastName  string
	}

	u := data{
		user:      user{"Embedded John", "Embedded Doe"},
		firstName: "John",
		lastName:  "Doe",
	}

	s := reflect.ValueOf(u).FieldByIndex([]int{0, 1})
	fmt.Println("embedded last name:", s)

}

```

```go
Output:
embedded last name: Embedded Doe

```

 Share Format Run

```go
func (v Value) FieldByIndexErr(index []int) (Value, error)
```

FieldByIndexErr returns the nested field corresponding to index. It returns an error if evaluation requires stepping through a nil pointer, but panics if it must step through a field that is not a struct.

```go
func (v Value) FieldByName(name string) Value
```

FieldByName returns the struct field with the given name. It returns the zero Value if no field was found. It panics if v's Kind is not Struct.

```go

package main

import (
	"fmt"
	"reflect"
)

func main() {
	type user struct {
		firstName string
		lastName  string
	}
	u := user{firstName: "John", lastName: "Doe"}
	s := reflect.ValueOf(u)

	fmt.Println("Name:", s.FieldByName("firstName"))
}

```

```go
Output:
Name: John

```

 Share Format Run

```go
func (v Value) FieldByNameFunc(match func(string) bool) Value
```

FieldByNameFunc returns the struct field with a name that satisfies the match function. It panics if v's Kind is not Struct. It returns the zero Value if no field was found.

```go
func (v Value) Fields() iter.Seq2[StructField, Value]
```

Fields returns an iterator over each StructField of v along with its Value.

The sequence is equivalent to calling Value.Field successively for each index i in the range [0, NumField()).

It panics if v's Kind is not Struct.

```go
func (v Value) Float() float64
```

Float returns v's underlying value, as a float64. It panics if v's Kind is not Float32 or Float64

```go
func (v Value) Grow(n int)
```

Grow increases the slice's capacity, if necessary, to guarantee space for another n elements. After Grow(n), at least n elements can be appended to the slice without another allocation.

It panics if v's Kind is not a Slice, or if n is negative or too large to allocate the memory, or if Value.CanSet returns false.

```go
func (v Value) Index(i int) Value
```

Index returns v's i'th element. It panics if v's Kind is not Array, Slice, or String or i is out of range.

```go
func (v Value) Int() int64
```

Int returns v's underlying value, as an int64. It panics if v's Kind is not Int, Int8, Int16, Int32, or Int64.

```go
func (v Value) Interface() (i any)
```

Interface returns v's current value as an interface{}. It is equivalent to:

```go
var i interface{} = (v's underlying value)

```

It panics if the Value was obtained by accessing unexported struct fields.

```go
func (v Value) InterfaceData() [2]uintptr
```

InterfaceData returns a pair of unspecified uintptr values. It panics if v's Kind is not Interface.

In earlier versions of Go, this function returned the interface's value as a uintptr pair. As of Go 1.4, the implementation of interface values precludes any defined use of InterfaceData.

Deprecated: The memory representation of interface values is not compatible with InterfaceData.

```go
func (v Value) IsNil() bool
```

IsNil reports whether its argument v is nil. The argument must be a chan, func, interface, map, pointer, or slice value; if it is not, IsNil panics. Note that IsNil is not always equivalent to a regular comparison with nil in Go. For example, if v was created by calling ValueOf with an uninitialized interface variable i, i==nil will be true but v.IsNil will panic as v will be the zero Value.

```go
func (v Value) IsValid() bool
```

IsValid reports whether v represents a value. It returns false if v is the zero Value. If Value.IsValid returns false, all other methods except String panic. Most functions and methods never return an invalid Value. If one does, its documentation states the conditions explicitly.

```go
func (v Value) IsZero() bool
```

IsZero reports whether v is the zero value for its type. It panics if the argument is invalid.

```go
func (v Value) Kind() Kind
```

Kind returns v's Kind. If v is the zero Value (Value.IsValid returns false), Kind returns Invalid.

```go
func (v Value) Len() int
```

Len returns v's length. It panics if v's Kind is not Array, Chan, Map, Slice, String, or pointer to Array.

```go
func (v Value) MapIndex(key Value) Value
```

MapIndex returns the value associated with key in the map v. It panics if v's Kind is not Map. It returns the zero Value if key is not found in the map or if v represents a nil map. As in Go, the key's value must be assignable to the map's key type.

```go
func (v Value) MapKeys() []Value
```

MapKeys returns a slice containing all the keys present in the map, in unspecified order. It panics if v's Kind is not Map. It returns an empty slice if v represents a nil map.

```go
func (v Value) MapRange() *MapIter
```

MapRange returns a range iterator for a map. It panics if v's Kind is not Map.

Call MapIter.Next to advance the iterator, and MapIter.Key/MapIter.Value to access each entry. MapIter.Next returns false when the iterator is exhausted. MapRange follows the same iteration semantics as a range statement.

Example:

```go
iter := reflect.ValueOf(m).MapRange()
for iter.Next() {
	k := iter.Key()
	v := iter.Value()
	...
}

```

```go
func (v Value) Method(i int) Value
```

Method returns a function value corresponding to v's i'th method. The arguments to a Call on the returned function should not include a receiver; the returned function will always use v as the receiver. Method panics if i is out of range or if v is a nil interface value.

Calling this method will force the linker to retain all exported methods in all packages. This may make the executable binary larger but will not affect execution time.

```go
func (v Value) MethodByName(name string) Value
```

MethodByName returns a function value corresponding to the method of v with the given name. The arguments to a Call on the returned function should not include a receiver; the returned function will always use v as the receiver. It returns the zero Value if no method was found.

Calling this method will cause the linker to retain all methods with this name in all packages. If the linker can't determine the name, it will retain all exported methods. This may make the executable binary larger but will not affect execution time.

```go
func (v Value) Methods() iter.Seq2[Method, Value]
```

Methods returns an iterator over each Method of v along with the corresponding method Value; this is a function with v bound as the receiver. As such, the receiver shouldn't be included in the arguments to Value.Call.

The sequence is equivalent to calling Value.Method successively for each index i in the range [0, NumMethod()).

Methods panics if v is a nil interface value.

Calling this method will force the linker to retain all exported methods in all packages. This may make the executable binary larger but will not affect execution time.

```go
func (v Value) NumField() int
```

NumField returns the number of fields in the struct v. It panics if v's Kind is not Struct.

```go
func (v Value) NumMethod() int
```

NumMethod returns the number of methods in the value's method set.

For a non-interface type, it returns the number of exported methods.

For an interface type, it returns the number of exported and unexported methods.

```go
func (v Value) OverflowComplex(x complex128) bool
```

OverflowComplex reports whether the complex128 x cannot be represented by v's type. It panics if v's Kind is not Complex64 or Complex128.

```go
func (v Value) OverflowFloat(x float64) bool
```

OverflowFloat reports whether the float64 x cannot be represented by v's type. It panics if v's Kind is not Float32 or Float64.

```go
func (v Value) OverflowInt(x int64) bool
```

OverflowInt reports whether the int64 x cannot be represented by v's type. It panics if v's Kind is not Int, Int8, Int16, Int32, or Int64.

```go
func (v Value) OverflowUint(x uint64) bool
```

OverflowUint reports whether the uint64 x cannot be represented by v's type. It panics if v's Kind is not Uint, Uintptr, Uint8, Uint16, Uint32, or Uint64.

```go
func (v Value) Pointer() uintptr
```

Pointer returns v's value as a uintptr. It panics if v's Kind is not Chan, Func, Map, Pointer, Slice, String, or UnsafePointer.

If v's Kind is Func, the returned pointer is an underlying code pointer, but not necessarily enough to identify a single function uniquely. The only guarantee is that the result is zero if and only if v is a nil func Value.

If v's Kind is Slice, the returned pointer is to the first element of the slice. If the slice is nil the returned value is 0. If the slice is empty but non-nil the return value is non-zero.

If v's Kind is String, the returned pointer is to the first element of the underlying bytes of string.

It's preferred to use uintptr(Value.UnsafePointer()) to get the equivalent result.

```go
func (v Value) Recv() (x Value, ok bool)
```

Recv receives and returns a value from the channel v. It panics if v's Kind is not Chan. The receive blocks until a value is ready. The boolean value ok is true if the value x corresponds to a send on the channel, false if it is a zero value received because the channel is closed.

```go
func (v Value) Send(x Value)
```

Send sends x on the channel v. It panics if v's kind is not Chan or if x's type is not the same type as v's element type. As in Go, x's value must be assignable to the channel's element type.

```go
func (v Value) Seq() iter.Seq[Value]
```

Seq returns an iter.Seq[Value] that loops over the elements of v. If v's kind is Func, it must be a function that has no results and that takes a single argument of type func(T) bool for some type T. If v's kind is Pointer, the pointer element type must have kind Array. Otherwise v's kind must be Int, Int8, Int16, Int32, Int64, Uint, Uint8, Uint16, Uint32, Uint64, Uintptr, Array, Chan, Map, Slice, or String.

```go
func (v Value) Seq2() iter.Seq2[Value, Value]
```

Seq2 returns an iter.Seq2[Value, Value] that loops over the elements of v. If v's kind is Func, it must be a function that has no results and that takes a single argument of type func(K, V) bool for some type K, V. If v's kind is Pointer, the pointer element type must have kind Array. Otherwise v's kind must be Array, Map, Slice, or String.

```go
func (v Value) Set(x Value)
```

Set assigns x to the value v. It panics if Value.CanSet returns false. As in Go, x's value must be assignable to v's type and must not be derived from an unexported field.

```go
func (v Value) SetBool(x bool)
```

SetBool sets v's underlying value. It panics if v's Kind is not Bool or if Value.CanSet returns false.

```go
func (v Value) SetBytes(x []byte)
```

SetBytes sets v's underlying value. It panics if v's underlying value is not a slice of bytes or if Value.CanSet returns false.

```go
func (v Value) SetCap(n int)
```

SetCap sets v's capacity to n. It panics if v's Kind is not Slice, or if n is smaller than the length or greater than the capacity of the slice, or if Value.CanSet returns false.

```go
func (v Value) SetComplex(x complex128)
```

SetComplex sets v's underlying value to x. It panics if v's Kind is not Complex64 or Complex128, or if Value.CanSet returns false.

```go
func (v Value) SetFloat(x float64)
```

SetFloat sets v's underlying value to x. It panics if v's Kind is not Float32 or Float64, or if Value.CanSet returns false.

```go
func (v Value) SetInt(x int64)
```

SetInt sets v's underlying value to x. It panics if v's Kind is not Int, Int8, Int16, Int32, or Int64, or if Value.CanSet returns false.

```go
func (v Value) SetIterKey(iter *MapIter)
```

SetIterKey assigns to v the key of iter's current map entry. It is equivalent to v.Set(iter.Key()), but it avoids allocating a new Value. As in Go, the key must be assignable to v's type and must not be derived from an unexported field. It panics if Value.CanSet returns false.

```go
func (v Value) SetIterValue(iter *MapIter)
```

SetIterValue assigns to v the value of iter's current map entry. It is equivalent to v.Set(iter.Value()), but it avoids allocating a new Value. As in Go, the value must be assignable to v's type and must not be derived from an unexported field. It panics if Value.CanSet returns false.

```go
func (v Value) SetLen(n int)
```

SetLen sets v's length to n. It panics if v's Kind is not Slice, or if n is negative or greater than the capacity of the slice, or if Value.CanSet returns false.

```go
func (v Value) SetMapIndex(key, elem Value)
```

SetMapIndex sets the element associated with key in the map v to elem. It panics if v's Kind is not Map. If elem is the zero Value, SetMapIndex deletes the key from the map. Otherwise if v holds a nil map, SetMapIndex will panic. As in Go, key's elem must be assignable to the map's key type, and elem's value must be assignable to the map's elem type.

```go
func (v Value) SetPointer(x unsafe.Pointer)
```

SetPointer sets the unsafe.Pointer value v to x. It panics if v's Kind is not UnsafePointer or if Value.CanSet returns false.

```go
func (v Value) SetString(x string)
```

SetString sets v's underlying value to x. It panics if v's Kind is not String or if Value.CanSet returns false.

```go
func (v Value) SetUint(x uint64)
```

SetUint sets v's underlying value to x. It panics if v's Kind is not Uint, Uintptr, Uint8, Uint16, Uint32, or Uint64, or if Value.CanSet returns false.

```go
func (v Value) SetZero()
```

SetZero sets v to be the zero value of v's type. It panics if Value.CanSet returns false.

```go
func (v Value) Slice(i, j int) Value
```

Slice returns v[i:j]. It panics if v's Kind is not Array, Slice or String, or if v is an unaddressable array, or if the indexes are out of bounds.

```go
func (v Value) Slice3(i, j, k int) Value
```

Slice3 is the 3-index form of the slice operation: it returns v[i:j:k]. It panics if v's Kind is not Array or Slice, or if v is an unaddressable array, or if the indexes are out of bounds.

```go
func (v Value) String() string
```

String returns the string v's underlying value, as a string. String is a special case because of Go's String method convention. Unlike the other getters, it does not panic if v's Kind is not String. Instead, it returns a string of the form "<T value>" where T is v's type. The fmt package treats Values specially. It does not call their String method implicitly but instead prints the concrete values they hold.

```go
func (v Value) TryRecv() (x Value, ok bool)
```

TryRecv attempts to receive a value from the channel v but will not block. It panics if v's Kind is not Chan. If the receive delivers a value, x is the transferred value and ok is true. If the receive cannot finish without blocking, x is the zero Value and ok is false. If the channel is closed, x is the zero value for the channel's element type and ok is false.

```go
func (v Value) TrySend(x Value) bool
```

TrySend attempts to send x on the channel v but will not block. It panics if v's Kind is not Chan. It reports whether the value was sent. As in Go, x's value must be assignable to the channel's element type.

```go
func (v Value) Type() Type
```

Type returns v's type.

```go
func (v Value) Uint() uint64
```

Uint returns v's underlying value, as a uint64. It panics if v's Kind is not Uint, Uintptr, Uint8, Uint16, Uint32, or Uint64.

```go
func (v Value) UnsafeAddr() uintptr
```

UnsafeAddr returns a pointer to v's data, as a uintptr. It panics if v is not addressable.

It's preferred to use uintptr(Value.Addr().UnsafePointer()) to get the equivalent result.

```go
func (v Value) UnsafePointer() unsafe.Pointer
```

UnsafePointer returns v's value as a unsafe.Pointer. It panics if v's Kind is not Chan, Func, Map, Pointer, Slice, String or UnsafePointer.

If v's Kind is Func, the returned pointer is an underlying code pointer, but not necessarily enough to identify a single function uniquely. The only guarantee is that the result is zero if and only if v is a nil func Value.

If v's Kind is Slice, the returned pointer is to the first element of the slice. If the slice is nil the returned value is nil. If the slice is empty but non-nil the return value is non-nil.

If v's Kind is String, the returned pointer is to the first element of the underlying bytes of string.

```go
type ValueError struct {
	Method string
	Kind   Kind
}
```

A ValueError occurs when a Value method is invoked on a Value that does not support it. Such cases are documented in the description of each method.

```go
func (e *ValueError) Error() string
```

-
FieldByName and related functions consider struct field names to be equal if the names are equal, even if they are unexported names originating in different packages. The practical effect of this is that the result of t.FieldByName("x") is not well defined if the struct type t contains multiple fields named x (embedded from different packages). FieldByName may return one of the fields named x or may report that there are none. See https://golang.org/issue/4876 <https://golang.org/issue/4876> for more details.

##   Source Files ¶
 View all Source files <https://cs.opensource.google/go/go/+/go1.26.3:src/reflect>

- abi.go <https://cs.opensource.google/go/go/+/go1.26.3:src/reflect/abi.go>
- badlinkname.go <https://cs.opensource.google/go/go/+/go1.26.3:src/reflect/badlinkname.go>
- deepequal.go <https://cs.opensource.google/go/go/+/go1.26.3:src/reflect/deepequal.go>
- float32reg_generic.go <https://cs.opensource.google/go/go/+/go1.26.3:src/reflect/float32reg_generic.go>
- iter.go <https://cs.opensource.google/go/go/+/go1.26.3:src/reflect/iter.go>
- makefunc.go <https://cs.opensource.google/go/go/+/go1.26.3:src/reflect/makefunc.go>
- map.go <https://cs.opensource.google/go/go/+/go1.26.3:src/reflect/map.go>
- swapper.go <https://cs.opensource.google/go/go/+/go1.26.3:src/reflect/swapper.go>
- type.go <https://cs.opensource.google/go/go/+/go1.26.3:src/reflect/type.go>
- value.go <https://cs.opensource.google/go/go/+/go1.26.3:src/reflect/value.go>
- visiblefields.go <https://cs.opensource.google/go/go/+/go1.26.3:src/reflect/visiblefields.go>

##   Directories ¶
    Show internal   Expand all

        internal      example1

      example2

  Click to show internal directories.
  Click to hide internal directories.

  Close

     **?** : This menu   **/** : Search site   **f** or **F** : Jump to   **y** or **Y**  : Canonical URL
  Close
