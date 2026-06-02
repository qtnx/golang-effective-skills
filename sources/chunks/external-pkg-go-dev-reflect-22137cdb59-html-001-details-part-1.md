---
source_name: "External Linked Documentation"
source_url: "https://pkg.go.dev/reflect"
source_path: "sources/raw/external/pkg-go-dev-reflect-22137cdb59.html"
license_ref: ""
---

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
