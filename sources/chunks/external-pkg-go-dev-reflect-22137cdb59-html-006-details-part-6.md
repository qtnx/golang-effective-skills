---
source_name: "External Linked Documentation"
source_url: "https://pkg.go.dev/reflect"
source_path: "sources/raw/external/pkg-go-dev-reflect-22137cdb59.html"
license_ref: ""
---

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
