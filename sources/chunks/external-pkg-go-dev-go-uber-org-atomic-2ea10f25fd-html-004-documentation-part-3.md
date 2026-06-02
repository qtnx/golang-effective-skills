---
source_name: "External Linked Documentation"
source_url: "https://pkg.go.dev/go.uber.org/atomic"
source_path: "sources/raw/external/pkg-go-dev-go-uber-org-atomic-2ea10f25fd.html"
license_ref: ""
---

##   Documentation ¶

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
