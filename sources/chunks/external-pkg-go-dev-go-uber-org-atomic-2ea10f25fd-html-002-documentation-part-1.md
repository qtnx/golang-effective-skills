---
source_name: "External Linked Documentation"
source_url: "https://pkg.go.dev/go.uber.org/atomic"
source_path: "sources/raw/external/pkg-go-dev-go-uber-org-atomic-2ea10f25fd.html"
license_ref: ""
---

##   Documentation ¶

Package atomic provides simple wrappers around numerics to enforce atomic access.

```go

package main

import (
	"fmt"

"go.uber.org/atomic"
)

func main() {
	// Uint32 is a thin wrapper around the primitive uint32 type.
	var atom atomic.Uint32

// The wrapper ensures that all operations are atomic.
	atom.Store(42)
	fmt.Println(atom.Inc())
	fmt.Println(atom.CAS(43, 0))
	fmt.Println(atom.Load())

}

```

```go
Output:
43
true
0

```

Share Format Run

-  type Bool
-
-  func NewBool(val bool) *Bool

-
-  func (x *Bool) CAS(old, new bool) (swapped bool)deprecated
-  func (x *Bool) CompareAndSwap(old, new bool) (swapped bool)
-  func (x *Bool) Load() bool
-  func (x *Bool) MarshalJSON() ([]byte, error)
-  func (x *Bool) Store(val bool)
-  func (b *Bool) String() string
-  func (x *Bool) Swap(val bool) (old bool)
-  func (b *Bool) Toggle() (old bool)
-  func (x *Bool) UnmarshalJSON(b []byte) error

-  type Duration
-
-  func NewDuration(val time.Duration) *Duration

-
-  func (d *Duration) Add(delta time.Duration) time.Duration
-  func (x *Duration) CAS(old, new time.Duration) (swapped bool)deprecated
-  func (x *Duration) CompareAndSwap(old, new time.Duration) (swapped bool)
-  func (x *Duration) Load() time.Duration
-  func (x *Duration) MarshalJSON() ([]byte, error)
-  func (x *Duration) Store(val time.Duration)
-  func (d *Duration) String() string
-  func (d *Duration) Sub(delta time.Duration) time.Duration
-  func (x *Duration) Swap(val time.Duration) (old time.Duration)
-  func (x *Duration) UnmarshalJSON(b []byte) error

-  type Error
-
-  func NewError(val error) *Error

-
-  func (x *Error) CompareAndSwap(old, new error) (swapped bool)
-  func (x *Error) Load() error
-  func (x *Error) Store(val error)
-  func (x *Error) Swap(val error) (old error)

-  type Float32
-
-  func NewFloat32(val float32) *Float32

-
-  func (f *Float32) Add(delta float32) float32
-  func (f *Float32) CAS(old, new float32) (swapped bool)deprecated
-  func (f *Float32) CompareAndSwap(old, new float32) (swapped bool)
-  func (x *Float32) Load() float32
-  func (x *Float32) MarshalJSON() ([]byte, error)
-  func (x *Float32) Store(val float32)
-  func (f *Float32) String() string
-  func (f *Float32) Sub(delta float32) float32
-  func (x *Float32) Swap(val float32) (old float32)
-  func (x *Float32) UnmarshalJSON(b []byte) error

-  type Float64
-
-  func NewFloat64(val float64) *Float64

-
-  func (f *Float64) Add(delta float64) float64
-  func (f *Float64) CAS(old, new float64) (swapped bool)deprecated
-  func (f *Float64) CompareAndSwap(old, new float64) (swapped bool)
-  func (x *Float64) Load() float64
-  func (x *Float64) MarshalJSON() ([]byte, error)
-  func (x *Float64) Store(val float64)
-  func (f *Float64) String() string
-  func (f *Float64) Sub(delta float64) float64
-  func (x *Float64) Swap(val float64) (old float64)
-  func (x *Float64) UnmarshalJSON(b []byte) error

-  type Int32
-
-  func NewInt32(val int32) *Int32

-
-  func (i *Int32) Add(delta int32) int32
-  func (i *Int32) CAS(old, new int32) (swapped bool)deprecated
-  func (i *Int32) CompareAndSwap(old, new int32) (swapped bool)
-  func (i *Int32) Dec() int32
-  func (i *Int32) Inc() int32
-  func (i *Int32) Load() int32
-  func (i *Int32) MarshalJSON() ([]byte, error)
-  func (i *Int32) Store(val int32)
-  func (i *Int32) String() string
-  func (i *Int32) Sub(delta int32) int32
-  func (i *Int32) Swap(val int32) (old int32)
-  func (i *Int32) UnmarshalJSON(b []byte) error

-  type Int64
-
-  func NewInt64(val int64) *Int64

-
-  func (i *Int64) Add(delta int64) int64
-  func (i *Int64) CAS(old, new int64) (swapped bool)deprecated
-  func (i *Int64) CompareAndSwap(old, new int64) (swapped bool)
-  func (i *Int64) Dec() int64
-  func (i *Int64) Inc() int64
-  func (i *Int64) Load() int64
-  func (i *Int64) MarshalJSON() ([]byte, error)
-  func (i *Int64) Store(val int64)
-  func (i *Int64) String() string
-  func (i *Int64) Sub(delta int64) int64
-  func (i *Int64) Swap(val int64) (old int64)
-  func (i *Int64) UnmarshalJSON(b []byte) error

-  type Pointer
-
-  func NewPointer[T any](v *T) *Pointer[T]

-
-  func (p *Pointer[T]) CompareAndSwap(old, new *T) (swapped bool)
-  func (p *Pointer[T]) Load() *T
-  func (p *Pointer[T]) Store(val *T)
-  func (p *Pointer[T]) String() string
-  func (p *Pointer[T]) Swap(val *T) (old *T)

-  type String
-
-  func NewString(val string) *String

-
-  func (x *String) CompareAndSwap(old, new string) (swapped bool)
-  func (x *String) Load() string
-  func (s *String) MarshalText() ([]byte, error)
-  func (x *String) Store(val string)
-  func (s *String) String() string
-  func (x *String) Swap(val string) (old string)
-  func (s *String) UnmarshalText(b []byte) error

-  type Time
-
-  func NewTime(val time.Time) *Time

-
-  func (x *Time) Load() time.Time
-  func (x *Time) Store(val time.Time)

-  type Uint32
-
-  func NewUint32(val uint32) *Uint32

-
-  func (i *Uint32) Add(delta uint32) uint32
-  func (i *Uint32) CAS(old, new uint32) (swapped bool)deprecated
-  func (i *Uint32) CompareAndSwap(old, new uint32) (swapped bool)
-  func (i *Uint32) Dec() uint32
-  func (i *Uint32) Inc() uint32
-  func (i *Uint32) Load() uint32
-  func (i *Uint32) MarshalJSON() ([]byte, error)
-  func (i *Uint32) Store(val uint32)
-  func (i *Uint32) String() string
-  func (i *Uint32) Sub(delta uint32) uint32
-  func (i *Uint32) Swap(val uint32) (old uint32)
-  func (i *Uint32) UnmarshalJSON(b []byte) error

-  type Uint64
-
-  func NewUint64(val uint64) *Uint64

-
-  func (i *Uint64) Add(delta uint64) uint64
-  func (i *Uint64) CAS(old, new uint64) (swapped bool)deprecated
-  func (i *Uint64) CompareAndSwap(old, new uint64) (swapped bool)
-  func (i *Uint64) Dec() uint64
-  func (i *Uint64) Inc() uint64
-  func (i *Uint64) Load() uint64
-  func (i *Uint64) MarshalJSON() ([]byte, error)
-  func (i *Uint64) Store(val uint64)
-  func (i *Uint64) String() string
-  func (i *Uint64) Sub(delta uint64) uint64
-  func (i *Uint64) Swap(val uint64) (old uint64)
-  func (i *Uint64) UnmarshalJSON(b []byte) error

-  type Uintptr
-
-  func NewUintptr(val uintptr) *Uintptr

-
-  func (i *Uintptr) Add(delta uintptr) uintptr
-  func (i *Uintptr) CAS(old, new uintptr) (swapped bool)deprecated
-  func (i *Uintptr) CompareAndSwap(old, new uintptr) (swapped bool)
-  func (i *Uintptr) Dec() uintptr
-  func (i *Uintptr) Inc() uintptr
-  func (i *Uintptr) Load() uintptr
-  func (i *Uintptr) MarshalJSON() ([]byte, error)
-  func (i *Uintptr) Store(val uintptr)
-  func (i *Uintptr) String() string
-  func (i *Uintptr) Sub(delta uintptr) uintptr
-  func (i *Uintptr) Swap(val uintptr) (old uintptr)
-  func (i *Uintptr) UnmarshalJSON(b []byte) error

-  type UnsafePointer
-
-  func NewUnsafePointer(val unsafe.Pointer) *UnsafePointer

-
-  func (p *UnsafePointer) CAS(old, new unsafe.Pointer) (swapped bool)deprecated
-  func (p *UnsafePointer) CompareAndSwap(old, new unsafe.Pointer) (swapped bool)
-  func (p *UnsafePointer) Load() unsafe.Pointer
-  func (p *UnsafePointer) Store(val unsafe.Pointer)
-  func (p *UnsafePointer) Swap(val unsafe.Pointer) (old unsafe.Pointer)

-  type Value

- Package

This section is empty.

This section is empty.

This section is empty.

```go
type Bool struct {
	// contains filtered or unexported fields
}
```

Bool is an atomic type-safe wrapper for bool values.

```go
func NewBool(val bool) *Bool
```

NewBool creates a new Bool.

```go
func (x *Bool) CAS(old, new bool) (swapped bool)
```

CAS is an atomic compare-and-swap for bool values.

Deprecated: Use CompareAndSwap.

```go
func (x *Bool) CompareAndSwap(old, new bool) (swapped bool)
```

CompareAndSwap is an atomic compare-and-swap for bool values.

```go
func (x *Bool) Load() bool
```

Load atomically loads the wrapped bool.

```go
func (x *Bool) MarshalJSON() ([]byte, error)
```

MarshalJSON encodes the wrapped bool into JSON.

```go
func (x *Bool) Store(val bool)
```

Store atomically stores the passed bool.

```go
func (b *Bool) String() string
```

String encodes the wrapped value as a string.

```go
func (x *Bool) Swap(val bool) (old bool)
```

Swap atomically stores the given bool and returns the old value.

```go
func (b *Bool) Toggle() (old bool)
```

Toggle atomically negates the Boolean and returns the previous value.

```go
func (x *Bool) UnmarshalJSON(b []byte) error
```

UnmarshalJSON decodes a bool from JSON.

```go
type Duration struct {
	// contains filtered or unexported fields
}
```

Duration is an atomic type-safe wrapper for time.Duration values.

```go
func NewDuration(val time.Duration) *Duration
```

NewDuration creates a new Duration.

```go
func (d *Duration) Add(delta time.Duration) time.Duration
```

Add atomically adds to the wrapped time.Duration and returns the new value.

```go
func (x *Duration) CAS(old, new time.Duration) (swapped bool)
```

CAS is an atomic compare-and-swap for time.Duration values.

Deprecated: Use CompareAndSwap.

```go
func (x *Duration) CompareAndSwap(old, new time.Duration) (swapped bool)
```

CompareAndSwap is an atomic compare-and-swap for time.Duration values.

```go
func (x *Duration) Load() time.Duration
```

Load atomically loads the wrapped time.Duration.

```go
func (x *Duration) MarshalJSON() ([]byte, error)
```

MarshalJSON encodes the wrapped time.Duration into JSON.

```go
func (x *Duration) Store(val time.Duration)
```

Store atomically stores the passed time.Duration.

```go
func (d *Duration) String() string
```

String encodes the wrapped value as a string.

```go
func (d *Duration) Sub(delta time.Duration) time.Duration
```

Sub atomically subtracts from the wrapped time.Duration and returns the new value.

```go
func (x *Duration) Swap(val time.Duration) (old time.Duration)
```

Swap atomically stores the given time.Duration and returns the old value.

```go
func (x *Duration) UnmarshalJSON(b []byte) error
```

UnmarshalJSON decodes a time.Duration from JSON.

```go
type Error struct {
	// contains filtered or unexported fields
}
```

Error is an atomic type-safe wrapper for error values.

```go
func NewError(val error) *Error
```

NewError creates a new Error.

```go
func (x *Error) CompareAndSwap(old, new error) (swapped bool)
```

CompareAndSwap is an atomic compare-and-swap for error values.

```go
func (x *Error) Load() error
```

Load atomically loads the wrapped error.

```go
func (x *Error) Store(val error)
```

Store atomically stores the passed error.

```go
func (x *Error) Swap(val error) (old error)
```

Swap atomically stores the given error and returns the old value.

```go
type Float32 struct {
	// contains filtered or unexported fields
}
```

Float32 is an atomic type-safe wrapper for float32 values.

```go
func NewFloat32(val float32) *Float32
```

NewFloat32 creates a new Float32.
