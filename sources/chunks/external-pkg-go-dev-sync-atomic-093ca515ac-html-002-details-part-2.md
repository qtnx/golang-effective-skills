---
source_name: "External Linked Documentation"
source_url: "https://pkg.go.dev/sync/atomic"
source_path: "sources/raw/external/pkg-go-dev-sync-atomic-093ca515ac.html"
license_ref: ""
---

LoadInt32 atomically loads *addr. Consider using the more ergonomic and less error-prone Int32.Load instead.

```go
func LoadInt64(addr *int64) (val int64)
```

LoadInt64 atomically loads *addr. Consider using the more ergonomic and less error-prone Int64.Load instead (particularly if you target 32-bit platforms; see the bugs section).

```go
func LoadPointer(addr *unsafe.Pointer) (val unsafe.Pointer)
```

LoadPointer atomically loads *addr. Consider using the more ergonomic and less error-prone Pointer.Load instead.

```go
func LoadUint32(addr *uint32) (val uint32)
```

LoadUint32 atomically loads *addr. Consider using the more ergonomic and less error-prone Uint32.Load instead.

```go
func LoadUint64(addr *uint64) (val uint64)
```

LoadUint64 atomically loads *addr. Consider using the more ergonomic and less error-prone Uint64.Load instead (particularly if you target 32-bit platforms; see the bugs section).

```go
func LoadUintptr(addr *uintptr) (val uintptr)
```

LoadUintptr atomically loads *addr. Consider using the more ergonomic and less error-prone Uintptr.Load instead.

```go
func OrInt32(addr *int32, mask int32) (old int32)
```

OrInt32 atomically performs a bitwise OR operation on *addr using the bitmask provided as mask and returns the old value. Consider using the more ergonomic and less error-prone Int32.Or instead.

```go
func OrInt64(addr *int64, mask int64) (old int64)
```

OrInt64 atomically performs a bitwise OR operation on *addr using the bitmask provided as mask and returns the old value. Consider using the more ergonomic and less error-prone Int64.Or instead.

```go
func OrUint32(addr *uint32, mask uint32) (old uint32)
```

OrUint32 atomically performs a bitwise OR operation on *addr using the bitmask provided as mask and returns the old value. Consider using the more ergonomic and less error-prone Uint32.Or instead.

```go
func OrUint64(addr *uint64, mask uint64) (old uint64)
```

OrUint64 atomically performs a bitwise OR operation on *addr using the bitmask provided as mask and returns the old value. Consider using the more ergonomic and less error-prone Uint64.Or instead.

```go
func OrUintptr(addr *uintptr, mask uintptr) (old uintptr)
```

OrUintptr atomically performs a bitwise OR operation on *addr using the bitmask provided as mask and returns the old value. Consider using the more ergonomic and less error-prone Uintptr.Or instead.

```go
func StoreInt32(addr *int32, val int32)
```

StoreInt32 atomically stores val into *addr. Consider using the more ergonomic and less error-prone Int32.Store instead.

```go
func StoreInt64(addr *int64, val int64)
```

StoreInt64 atomically stores val into *addr. Consider using the more ergonomic and less error-prone Int64.Store instead (particularly if you target 32-bit platforms; see the bugs section).

```go
func StorePointer(addr *unsafe.Pointer, val unsafe.Pointer)
```

StorePointer atomically stores val into *addr. Consider using the more ergonomic and less error-prone Pointer.Store instead.

```go
func StoreUint32(addr *uint32, val uint32)
```

StoreUint32 atomically stores val into *addr. Consider using the more ergonomic and less error-prone Uint32.Store instead.

```go
func StoreUint64(addr *uint64, val uint64)
```

StoreUint64 atomically stores val into *addr. Consider using the more ergonomic and less error-prone Uint64.Store instead (particularly if you target 32-bit platforms; see the bugs section).

```go
func StoreUintptr(addr *uintptr, val uintptr)
```

StoreUintptr atomically stores val into *addr. Consider using the more ergonomic and less error-prone Uintptr.Store instead.

```go
func SwapInt32(addr *int32, new int32) (old int32)
```

SwapInt32 atomically stores new into *addr and returns the previous *addr value. Consider using the more ergonomic and less error-prone Int32.Swap instead.

```go
func SwapInt64(addr *int64, new int64) (old int64)
```

SwapInt64 atomically stores new into *addr and returns the previous *addr value. Consider using the more ergonomic and less error-prone Int64.Swap instead (particularly if you target 32-bit platforms; see the bugs section).

```go
func SwapPointer(addr *unsafe.Pointer, new unsafe.Pointer) (old unsafe.Pointer)
```

SwapPointer atomically stores new into *addr and returns the previous *addr value. Consider using the more ergonomic and less error-prone Pointer.Swap instead.

```go
func SwapUint32(addr *uint32, new uint32) (old uint32)
```

SwapUint32 atomically stores new into *addr and returns the previous *addr value. Consider using the more ergonomic and less error-prone Uint32.Swap instead.

```go
func SwapUint64(addr *uint64, new uint64) (old uint64)
```

SwapUint64 atomically stores new into *addr and returns the previous *addr value. Consider using the more ergonomic and less error-prone Uint64.Swap instead (particularly if you target 32-bit platforms; see the bugs section).

```go
func SwapUintptr(addr *uintptr, new uintptr) (old uintptr)
```

SwapUintptr atomically stores new into *addr and returns the previous *addr value. Consider using the more ergonomic and less error-prone Uintptr.Swap instead.

```go
type Bool struct {
	// contains filtered or unexported fields
}
```

A Bool is an atomic boolean value. The zero value is false.

Bool must not be copied after first use.

```go
func (x *Bool) CompareAndSwap(old, new bool) (swapped bool)
```

CompareAndSwap executes the compare-and-swap operation for the boolean value x.

```go
func (x *Bool) Load() bool
```

Load atomically loads and returns the value stored in x.

```go
func (x *Bool) Store(val bool)
```

Store atomically stores val into x.

```go
func (x *Bool) Swap(new bool) (old bool)
```

Swap atomically stores new into x and returns the previous value.

```go
type Int32 struct {
	// contains filtered or unexported fields
}
```

An Int32 is an atomic int32. The zero value is zero.

Int32 must not be copied after first use.

```go
func (x *Int32) Add(delta int32) (new int32)
```

Add atomically adds delta to x and returns the new value.

```go
func (x *Int32) And(mask int32) (old int32)
```

And atomically performs a bitwise AND operation on x using the bitmask provided as mask and returns the old value.

```go
func (x *Int32) CompareAndSwap(old, new int32) (swapped bool)
```

CompareAndSwap executes the compare-and-swap operation for x.

```go
func (x *Int32) Load() int32
```

Load atomically loads and returns the value stored in x.

```go
func (x *Int32) Or(mask int32) (old int32)
```

Or atomically performs a bitwise OR operation on x using the bitmask provided as mask and returns the old value.

```go
func (x *Int32) Store(val int32)
```

Store atomically stores val into x.

```go
func (x *Int32) Swap(new int32) (old int32)
```

Swap atomically stores new into x and returns the previous value.

```go
type Int64 struct {
	// contains filtered or unexported fields
}
```

An Int64 is an atomic int64. The zero value is zero.

Int64 must not be copied after first use.

```go
func (x *Int64) Add(delta int64) (new int64)
```

Add atomically adds delta to x and returns the new value.

```go
func (x *Int64) And(mask int64) (old int64)
```

And atomically performs a bitwise AND operation on x using the bitmask provided as mask and returns the old value.

```go
func (x *Int64) CompareAndSwap(old, new int64) (swapped bool)
```

CompareAndSwap executes the compare-and-swap operation for x.

```go
func (x *Int64) Load() int64
```

Load atomically loads and returns the value stored in x.

```go
func (x *Int64) Or(mask int64) (old int64)
```

Or atomically performs a bitwise OR operation on x using the bitmask provided as mask and returns the old value.

```go
func (x *Int64) Store(val int64)
```

Store atomically stores val into x.

```go
func (x *Int64) Swap(new int64) (old int64)
```

Swap atomically stores new into x and returns the previous value.

```go
type Pointer[T any] struct {
	// contains filtered or unexported fields
}
```

A Pointer is an atomic pointer of type *T. The zero value is a nil *T.

Pointer must not be copied after first use.

```go
func (x *Pointer[T]) CompareAndSwap(old, new *T) (swapped bool)
```

CompareAndSwap executes the compare-and-swap operation for x.

```go
func (x *Pointer[T]) Load() *T
```

Load atomically loads and returns the value stored in x.

```go
func (x *Pointer[T]) Store(val *T)
```

Store atomically stores val into x.

```go
func (x *Pointer[T]) Swap(new *T) (old *T)
```

Swap atomically stores new into x and returns the previous value.

```go
type Uint32 struct {
	// contains filtered or unexported fields
}
```

A Uint32 is an atomic uint32. The zero value is zero.

Uint32 must not be copied after first use.

```go
func (x *Uint32) Add(delta uint32) (new uint32)
```

Add atomically adds delta to x and returns the new value.

```go
func (x *Uint32) And(mask uint32) (old uint32)
```

And atomically performs a bitwise AND operation on x using the bitmask provided as mask and returns the old value.

```go
func (x *Uint32) CompareAndSwap(old, new uint32) (swapped bool)
```

CompareAndSwap executes the compare-and-swap operation for x.

```go
func (x *Uint32) Load() uint32
```

Load atomically loads and returns the value stored in x.

```go
func (x *Uint32) Or(mask uint32) (old uint32)
```

Or atomically performs a bitwise OR operation on x using the bitmask provided as mask and returns the old value.

```go
func (x *Uint32) Store(val uint32)
```

Store atomically stores val into x.

```go
func (x *Uint32) Swap(new uint32) (old uint32)
```

Swap atomically stores new into x and returns the previous value.

```go
type Uint64 struct {
	// contains filtered or unexported fields
}
```

A Uint64 is an atomic uint64. The zero value is zero.

Uint64 must not be copied after first use.

```go
func (x *Uint64) Add(delta uint64) (new uint64)
```

Add atomically adds delta to x and returns the new value.

```go
func (x *Uint64) And(mask uint64) (old uint64)
```

And atomically performs a bitwise AND operation on x using the bitmask provided as mask and returns the old value.

```go
func (x *Uint64) CompareAndSwap(old, new uint64) (swapped bool)
```

CompareAndSwap executes the compare-and-swap operation for x.

```go
func (x *Uint64) Load() uint64
```

Load atomically loads and returns the value stored in x.

```go
func (x *Uint64) Or(mask uint64) (old uint64)
```

Or atomically performs a bitwise OR operation on x using the bitmask provided as mask and returns the old value.

```go
func (x *Uint64) Store(val uint64)
```

Store atomically stores val into x.
