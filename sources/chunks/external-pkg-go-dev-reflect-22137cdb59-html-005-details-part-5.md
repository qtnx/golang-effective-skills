---
source_name: "External Linked Documentation"
source_url: "https://pkg.go.dev/reflect"
source_path: "sources/raw/external/pkg-go-dev-reflect-22137cdb59.html"
license_ref: ""
---

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
