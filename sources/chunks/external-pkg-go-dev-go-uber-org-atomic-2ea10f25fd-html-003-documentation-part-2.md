---
source_name: "External Linked Documentation"
source_url: "https://pkg.go.dev/go.uber.org/atomic"
source_path: "sources/raw/external/pkg-go-dev-go-uber-org-atomic-2ea10f25fd.html"
license_ref: ""
---

##   Documentation ¶

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
