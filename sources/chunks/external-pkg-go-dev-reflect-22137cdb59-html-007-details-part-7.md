---
source_name: "External Linked Documentation"
source_url: "https://pkg.go.dev/reflect"
source_path: "sources/raw/external/pkg-go-dev-reflect-22137cdb59.html"
license_ref: ""
---

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
