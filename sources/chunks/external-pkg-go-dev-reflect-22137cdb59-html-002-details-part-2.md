---
source_name: "External Linked Documentation"
source_url: "https://pkg.go.dev/reflect"
source_path: "sources/raw/external/pkg-go-dev-reflect-22137cdb59.html"
license_ref: ""
---

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
