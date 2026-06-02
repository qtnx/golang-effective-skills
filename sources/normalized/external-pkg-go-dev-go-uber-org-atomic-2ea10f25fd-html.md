atomic package - go.uber.org/atomic - Go Packages

## Details

-     Valid go.mod <https://github.com/uber-go/atomic/tree/v1.11.0/go.mod> file
 The Go module system was introduced in Go 1.11 and is the official dependency management solution for Go.

-     Redistributable license
 Redistributable licenses place minimal restrictions on how software can be used, modified, and redistributed.

-     Tagged version
Modules with tagged versions give importers more predictable builds.

-     Stable version
When a project reaches major version v1 it is considered stable.

-  Learn more about best practices

## Repository
   github.com/uber-go/atomic  <https://github.com/uber-go/atomic>

## Links

-    Open Source Insights  <https://deps.dev/go/go.uber.org%2Fatomic/v1.11.0>

##   README ¶

### atomic  <https://godoc.org/go.uber.org/atomic>  <https://github.com/uber-go/atomic/actions/workflows/go.yml>  <https://codecov.io/gh/uber-go/atomic>  <https://goreportcard.com/report/go.uber.org/atomic>

Simple wrappers for primitive types to enforce atomic access.

#### Installation

```go
$ go get -u go.uber.org/atomic@v1

```
 Legacy Import Path
As of v1.5.0, the import path `go.uber.org/atomic` is the only supported way of using this package. If you are using Go modules, this package will fail to compile with the legacy import path path `github.com/uber-go/atomic`.

We recommend migrating your code to the new import path but if you're unable to do so, or if your dependencies are still using the old import path, you will have to add a `replace` directive to your `go.mod` file downgrading the legacy import path to an older version.

```go
replace github.com/uber-go/atomic => github.com/uber-go/atomic v1.4.0

```

You can do so automatically by running the following command.

```go
$ go mod edit -replace github.com/uber-go/atomic=github.com/uber-go/atomic@v1.4.0

```

#### Usage

The standard library's `sync/atomic` is powerful, but it's easy to forget which variables must be accessed atomically. `go.uber.org/atomic` preserves all the functionality of the standard library, but wraps the primitive types to provide a safer, more convenient API.

```go
var atom atomic.Uint32
atom.Store(42)
atom.Sub(2)
atom.CAS(40, 11)

```

See the documentation <https://godoc.org/go.uber.org/atomic> for a complete API specification.

#### Development Status

Stable.

Released under the MIT License <https://github.com/uber-go/atomic/blob/v1.11.0/LICENSE.txt>.

 Expand ▾ Collapse ▴

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

```go
func (f *Float32) Add(delta float32) float32
```

Add atomically adds to the wrapped float32 and returns the new value.

```go
func (f *Float32) CAS(old, new float32) (swapped bool)
```

CAS is an atomic compare-and-swap for float32 values.

Deprecated: Use CompareAndSwap

```go
func (f *Float32) CompareAndSwap(old, new float32) (swapped bool)
```

CompareAndSwap is an atomic compare-and-swap for float32 values.

Note: CompareAndSwap handles NaN incorrectly. NaN != NaN using Go's inbuilt operators but CompareAndSwap allows a stored NaN to compare equal to a passed in NaN. This avoids typical CompareAndSwap loops from blocking forever, e.g.,

```go
for {
  old := atom.Load()
  new = f(old)
  if atom.CompareAndSwap(old, new) {
    break
  }
}

```

If CompareAndSwap did not match NaN to match, then the above would loop forever.

```go
func (x *Float32) Load() float32
```

Load atomically loads the wrapped float32.

```go
func (x *Float32) MarshalJSON() ([]byte, error)
```

MarshalJSON encodes the wrapped float32 into JSON.

```go
func (x *Float32) Store(val float32)
```

Store atomically stores the passed float32.

```go
func (f *Float32) String() string
```

String encodes the wrapped value as a string.

```go
func (f *Float32) Sub(delta float32) float32
```

Sub atomically subtracts from the wrapped float32 and returns the new value.

```go
func (x *Float32) Swap(val float32) (old float32)
```

Swap atomically stores the given float32 and returns the old value.

```go
func (x *Float32) UnmarshalJSON(b []byte) error
```

UnmarshalJSON decodes a float32 from JSON.

```go
type Float64 struct {
	// contains filtered or unexported fields
}
```

Float64 is an atomic type-safe wrapper for float64 values.

```go
func NewFloat64(val float64) *Float64
```

NewFloat64 creates a new Float64.

```go
func (f *Float64) Add(delta float64) float64
```

Add atomically adds to the wrapped float64 and returns the new value.

```go
func (f *Float64) CAS(old, new float64) (swapped bool)
```

CAS is an atomic compare-and-swap for float64 values.

Deprecated: Use CompareAndSwap

```go
func (f *Float64) CompareAndSwap(old, new float64) (swapped bool)
```

CompareAndSwap is an atomic compare-and-swap for float64 values.

Note: CompareAndSwap handles NaN incorrectly. NaN != NaN using Go's inbuilt operators but CompareAndSwap allows a stored NaN to compare equal to a passed in NaN. This avoids typical CompareAndSwap loops from blocking forever, e.g.,

```go
for {
  old := atom.Load()
  new = f(old)
  if atom.CompareAndSwap(old, new) {
    break
  }
}

```

If CompareAndSwap did not match NaN to match, then the above would loop forever.

```go
func (x *Float64) Load() float64
```

Load atomically loads the wrapped float64.

```go
func (x *Float64) MarshalJSON() ([]byte, error)
```

MarshalJSON encodes the wrapped float64 into JSON.

```go
func (x *Float64) Store(val float64)
```

Store atomically stores the passed float64.

```go
func (f *Float64) String() string
```

String encodes the wrapped value as a string.

```go
func (f *Float64) Sub(delta float64) float64
```

Sub atomically subtracts from the wrapped float64 and returns the new value.

```go
func (x *Float64) Swap(val float64) (old float64)
```

Swap atomically stores the given float64 and returns the old value.

```go
func (x *Float64) UnmarshalJSON(b []byte) error
```

UnmarshalJSON decodes a float64 from JSON.

```go
type Int32 struct {
	// contains filtered or unexported fields
}
```

Int32 is an atomic wrapper around int32.

```go
func NewInt32(val int32) *Int32
```

NewInt32 creates a new Int32.

```go
func (i *Int32) Add(delta int32) int32
```

Add atomically adds to the wrapped int32 and returns the new value.

```go
func (i *Int32) CAS(old, new int32) (swapped bool)
```

CAS is an atomic compare-and-swap.

Deprecated: Use CompareAndSwap.

```go
func (i *Int32) CompareAndSwap(old, new int32) (swapped bool)
```

CompareAndSwap is an atomic compare-and-swap.

```go
func (i *Int32) Dec() int32
```

Dec atomically decrements the wrapped int32 and returns the new value.

```go
func (i *Int32) Inc() int32
```

Inc atomically increments the wrapped int32 and returns the new value.

```go
func (i *Int32) Load() int32
```

Load atomically loads the wrapped value.

```go
func (i *Int32) MarshalJSON() ([]byte, error)
```

MarshalJSON encodes the wrapped int32 into JSON.

```go
func (i *Int32) Store(val int32)
```

Store atomically stores the passed value.

```go
func (i *Int32) String() string
```

String encodes the wrapped value as a string.

```go
func (i *Int32) Sub(delta int32) int32
```

Sub atomically subtracts from the wrapped int32 and returns the new value.

```go
func (i *Int32) Swap(val int32) (old int32)
```

Swap atomically swaps the wrapped int32 and returns the old value.

```go
func (i *Int32) UnmarshalJSON(b []byte) error
```

UnmarshalJSON decodes JSON into the wrapped int32.

```go
type Int64 struct {
	// contains filtered or unexported fields
}
```

Int64 is an atomic wrapper around int64.

```go
func NewInt64(val int64) *Int64
```

NewInt64 creates a new Int64.

```go
func (i *Int64) Add(delta int64) int64
```

Add atomically adds to the wrapped int64 and returns the new value.

```go
func (i *Int64) CAS(old, new int64) (swapped bool)
```

CAS is an atomic compare-and-swap.

Deprecated: Use CompareAndSwap.

```go
func (i *Int64) CompareAndSwap(old, new int64) (swapped bool)
```

CompareAndSwap is an atomic compare-and-swap.

```go
func (i *Int64) Dec() int64
```

Dec atomically decrements the wrapped int64 and returns the new value.

```go
func (i *Int64) Inc() int64
```

Inc atomically increments the wrapped int64 and returns the new value.

```go
func (i *Int64) Load() int64
```

Load atomically loads the wrapped value.

```go
func (i *Int64) MarshalJSON() ([]byte, error)
```

MarshalJSON encodes the wrapped int64 into JSON.

```go
func (i *Int64) Store(val int64)
```

Store atomically stores the passed value.

```go
func (i *Int64) String() string
```

String encodes the wrapped value as a string.

```go
func (i *Int64) Sub(delta int64) int64
```

Sub atomically subtracts from the wrapped int64 and returns the new value.

```go
func (i *Int64) Swap(val int64) (old int64)
```

Swap atomically swaps the wrapped int64 and returns the old value.

```go
func (i *Int64) UnmarshalJSON(b []byte) error
```

UnmarshalJSON decodes JSON into the wrapped int64.

```go
type Pointer[T any] struct {
	// contains filtered or unexported fields
}
```

Pointer is an atomic pointer of type *T.

```go
func NewPointer[T any](v *T) *Pointer[T]
```

NewPointer creates a new Pointer.

```go
func (p *Pointer[T]) CompareAndSwap(old, new *T) (swapped bool)
```

CompareAndSwap is an atomic compare-and-swap.

```go
func (p *Pointer[T]) Load() *T
```

Load atomically loads the wrapped value.

```go
func (p *Pointer[T]) Store(val *T)
```

Store atomically stores the passed value.

```go
func (p *Pointer[T]) String() string
```

String returns a human readable representation of a Pointer's underlying value.

```go
func (p *Pointer[T]) Swap(val *T) (old *T)
```

Swap atomically swaps the wrapped pointer and returns the old value.

```go
type String struct {
	// contains filtered or unexported fields
}
```

String is an atomic type-safe wrapper for string values.

```go
func NewString(val string) *String
```

NewString creates a new String.

```go
func (x *String) CompareAndSwap(old, new string) (swapped bool)
```

CompareAndSwap is an atomic compare-and-swap for string values.

```go
func (x *String) Load() string
```

Load atomically loads the wrapped string.

```go
func (s *String) MarshalText() ([]byte, error)
```

MarshalText encodes the wrapped string into a textual form.

This makes it encodable as JSON, YAML, XML, and more.

```go
func (x *String) Store(val string)
```

Store atomically stores the passed string.

```go
func (s *String) String() string
```

String returns the wrapped value.

```go
func (x *String) Swap(val string) (old string)
```

Swap atomically stores the given string and returns the old value.

```go
func (s *String) UnmarshalText(b []byte) error
```

UnmarshalText decodes text and replaces the wrapped string with it.

This makes it decodable from JSON, YAML, XML, and more.

```go
type Time struct {
	// contains filtered or unexported fields
}
```

Time is an atomic type-safe wrapper for time.Time values.

```go
func NewTime(val time.Time) *Time
```

NewTime creates a new Time.

```go
func (x *Time) Load() time.Time
```

Load atomically loads the wrapped time.Time.

```go
func (x *Time) Store(val time.Time)
```

Store atomically stores the passed time.Time.

```go
type Uint32 struct {
	// contains filtered or unexported fields
}
```

Uint32 is an atomic wrapper around uint32.

```go
func NewUint32(val uint32) *Uint32
```

NewUint32 creates a new Uint32.

```go
func (i *Uint32) Add(delta uint32) uint32
```

Add atomically adds to the wrapped uint32 and returns the new value.

```go
func (i *Uint32) CAS(old, new uint32) (swapped bool)
```

CAS is an atomic compare-and-swap.

Deprecated: Use CompareAndSwap.

```go
func (i *Uint32) CompareAndSwap(old, new uint32) (swapped bool)
```

CompareAndSwap is an atomic compare-and-swap.

```go
func (i *Uint32) Dec() uint32
```

Dec atomically decrements the wrapped uint32 and returns the new value.

```go
func (i *Uint32) Inc() uint32
```

Inc atomically increments the wrapped uint32 and returns the new value.

```go
func (i *Uint32) Load() uint32
```

Load atomically loads the wrapped value.

```go
func (i *Uint32) MarshalJSON() ([]byte, error)
```

MarshalJSON encodes the wrapped uint32 into JSON.

```go
func (i *Uint32) Store(val uint32)
```

Store atomically stores the passed value.

```go
func (i *Uint32) String() string
```

String encodes the wrapped value as a string.

```go
func (i *Uint32) Sub(delta uint32) uint32
```

Sub atomically subtracts from the wrapped uint32 and returns the new value.

```go
func (i *Uint32) Swap(val uint32) (old uint32)
```

Swap atomically swaps the wrapped uint32 and returns the old value.

```go
func (i *Uint32) UnmarshalJSON(b []byte) error
```

UnmarshalJSON decodes JSON into the wrapped uint32.

```go
type Uint64 struct {
	// contains filtered or unexported fields
}
```

Uint64 is an atomic wrapper around uint64.

```go
func NewUint64(val uint64) *Uint64
```

NewUint64 creates a new Uint64.

```go
func (i *Uint64) Add(delta uint64) uint64
```

Add atomically adds to the wrapped uint64 and returns the new value.

```go
func (i *Uint64) CAS(old, new uint64) (swapped bool)
```

CAS is an atomic compare-and-swap.

Deprecated: Use CompareAndSwap.

```go
func (i *Uint64) CompareAndSwap(old, new uint64) (swapped bool)
```

CompareAndSwap is an atomic compare-and-swap.

```go
func (i *Uint64) Dec() uint64
```

Dec atomically decrements the wrapped uint64 and returns the new value.

```go
func (i *Uint64) Inc() uint64
```

Inc atomically increments the wrapped uint64 and returns the new value.

```go
func (i *Uint64) Load() uint64
```

Load atomically loads the wrapped value.

```go
func (i *Uint64) MarshalJSON() ([]byte, error)
```

MarshalJSON encodes the wrapped uint64 into JSON.

```go
func (i *Uint64) Store(val uint64)
```

Store atomically stores the passed value.

```go
func (i *Uint64) String() string
```

String encodes the wrapped value as a string.

```go
func (i *Uint64) Sub(delta uint64) uint64
```

Sub atomically subtracts from the wrapped uint64 and returns the new value.

```go
func (i *Uint64) Swap(val uint64) (old uint64)
```

Swap atomically swaps the wrapped uint64 and returns the old value.

```go
func (i *Uint64) UnmarshalJSON(b []byte) error
```

UnmarshalJSON decodes JSON into the wrapped uint64.

```go
type Uintptr struct {
	// contains filtered or unexported fields
}
```

Uintptr is an atomic wrapper around uintptr.

```go
func NewUintptr(val uintptr) *Uintptr
```

NewUintptr creates a new Uintptr.

```go
func (i *Uintptr) Add(delta uintptr) uintptr
```

Add atomically adds to the wrapped uintptr and returns the new value.

```go
func (i *Uintptr) CAS(old, new uintptr) (swapped bool)
```

CAS is an atomic compare-and-swap.

Deprecated: Use CompareAndSwap.

```go
func (i *Uintptr) CompareAndSwap(old, new uintptr) (swapped bool)
```

CompareAndSwap is an atomic compare-and-swap.

```go
func (i *Uintptr) Dec() uintptr
```

Dec atomically decrements the wrapped uintptr and returns the new value.

```go
func (i *Uintptr) Inc() uintptr
```

Inc atomically increments the wrapped uintptr and returns the new value.

```go
func (i *Uintptr) Load() uintptr
```

Load atomically loads the wrapped value.

```go
func (i *Uintptr) MarshalJSON() ([]byte, error)
```

MarshalJSON encodes the wrapped uintptr into JSON.

```go
func (i *Uintptr) Store(val uintptr)
```

Store atomically stores the passed value.

```go
func (i *Uintptr) String() string
```

String encodes the wrapped value as a string.

```go
func (i *Uintptr) Sub(delta uintptr) uintptr
```

Sub atomically subtracts from the wrapped uintptr and returns the new value.

```go
func (i *Uintptr) Swap(val uintptr) (old uintptr)
```

Swap atomically swaps the wrapped uintptr and returns the old value.

```go
func (i *Uintptr) UnmarshalJSON(b []byte) error
```

UnmarshalJSON decodes JSON into the wrapped uintptr.

```go
type UnsafePointer struct {
	// contains filtered or unexported fields
}
```

UnsafePointer is an atomic wrapper around unsafe.Pointer.

```go
func NewUnsafePointer(val unsafe.Pointer) *UnsafePointer
```

NewUnsafePointer creates a new UnsafePointer.

```go
func (p *UnsafePointer) CAS(old, new unsafe.Pointer) (swapped bool)
```

CAS is an atomic compare-and-swap.

Deprecated: Use CompareAndSwap

```go
func (p *UnsafePointer) CompareAndSwap(old, new unsafe.Pointer) (swapped bool)
```

CompareAndSwap is an atomic compare-and-swap.

```go
func (p *UnsafePointer) Load() unsafe.Pointer
```

Load atomically loads the wrapped value.

```go
func (p *UnsafePointer) Store(val unsafe.Pointer)
```

Store atomically stores the passed value.

```go
func (p *UnsafePointer) Swap(val unsafe.Pointer) (old unsafe.Pointer)
```

Swap atomically swaps the wrapped unsafe.Pointer and returns the old value.

```go
type Value struct {
	atomic.Value
	// contains filtered or unexported fields
}
```

Value shadows the type of the same name from sync/atomic https://godoc.org/sync/atomic#Value <https://godoc.org/sync/atomic#Value>

##   Source Files ¶
 View all Source files <https://github.com/uber-go/atomic/tree/v1.11.0>

- bool.go <https://github.com/uber-go/atomic/blob/v1.11.0/bool.go>
- bool_ext.go <https://github.com/uber-go/atomic/blob/v1.11.0/bool_ext.go>
- doc.go <https://github.com/uber-go/atomic/blob/v1.11.0/doc.go>
- duration.go <https://github.com/uber-go/atomic/blob/v1.11.0/duration.go>
- duration_ext.go <https://github.com/uber-go/atomic/blob/v1.11.0/duration_ext.go>
- error.go <https://github.com/uber-go/atomic/blob/v1.11.0/error.go>
- error_ext.go <https://github.com/uber-go/atomic/blob/v1.11.0/error_ext.go>
- float32.go <https://github.com/uber-go/atomic/blob/v1.11.0/float32.go>
- float32_ext.go <https://github.com/uber-go/atomic/blob/v1.11.0/float32_ext.go>
- float64.go <https://github.com/uber-go/atomic/blob/v1.11.0/float64.go>
- float64_ext.go <https://github.com/uber-go/atomic/blob/v1.11.0/float64_ext.go>
- gen.go <https://github.com/uber-go/atomic/blob/v1.11.0/gen.go>
- int32.go <https://github.com/uber-go/atomic/blob/v1.11.0/int32.go>
- int64.go <https://github.com/uber-go/atomic/blob/v1.11.0/int64.go>
- nocmp.go <https://github.com/uber-go/atomic/blob/v1.11.0/nocmp.go>
- pointer_go118.go <https://github.com/uber-go/atomic/blob/v1.11.0/pointer_go118.go>
- pointer_go119.go <https://github.com/uber-go/atomic/blob/v1.11.0/pointer_go119.go>
- string.go <https://github.com/uber-go/atomic/blob/v1.11.0/string.go>
- string_ext.go <https://github.com/uber-go/atomic/blob/v1.11.0/string_ext.go>
- time.go <https://github.com/uber-go/atomic/blob/v1.11.0/time.go>
- time_ext.go <https://github.com/uber-go/atomic/blob/v1.11.0/time_ext.go>
- uint32.go <https://github.com/uber-go/atomic/blob/v1.11.0/uint32.go>
- uint64.go <https://github.com/uber-go/atomic/blob/v1.11.0/uint64.go>
- uintptr.go <https://github.com/uber-go/atomic/blob/v1.11.0/uintptr.go>
- unsafe_pointer.go <https://github.com/uber-go/atomic/blob/v1.11.0/unsafe_pointer.go>
- value.go <https://github.com/uber-go/atomic/blob/v1.11.0/value.go>

##   Directories ¶
    Show internal   Expand all

        internal      gen-atomicint command  gen-atomicint generates an atomic wrapper around an integer type.

  gen-atomicint generates an atomic wrapper around an integer type.    gen-atomicwrapper command  gen-atomicwrapper generates wrapper types around other atomic types.

  gen-atomicwrapper generates wrapper types around other atomic types.

  Click to show internal directories.
  Click to hide internal directories.

  Close

     **?** : This menu   **/** : Search site   **f** or **F** : Jump to   **y** or **Y**  : Canonical URL
  Close
