---
source_name: "External Linked Documentation"
source_url: "https://pkg.go.dev/reflect"
source_path: "sources/raw/external/pkg-go-dev-reflect-22137cdb59.html"
license_ref: ""
---

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
