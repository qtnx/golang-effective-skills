---
source_name: "External Linked Documentation"
source_url: "https://pkg.go.dev/sync/atomic"
source_path: "sources/raw/external/pkg-go-dev-sync-atomic-093ca515ac.html"
license_ref: ""
---

atomic package - sync/atomic - Go Packages
## Details

-     Valid go.mod <https://cs.opensource.google/go/go/+/go1.26.3:src/go.mod> file
 The Go module system was introduced in Go 1.11 and is the official dependency management solution for Go.

-     Redistributable license
 Redistributable licenses place minimal restrictions on how software can be used, modified, and redistributed.

-     Tagged version
Modules with tagged versions give importers more predictable builds.

-     Stable version
When a project reaches major version v1 it is considered stable.

-  Learn more about best practices

## Repository
   cs.opensource.google/go/go  <https://cs.opensource.google/go/go>

##   Documentation ¶

Package atomic provides low-level atomic memory primitives useful for implementing synchronization algorithms.

These functions require great care to be used correctly. Except for special, low-level applications, synchronization is better done with channels or the facilities of the sync package. Share memory by communicating; don't communicate by sharing memory.

The swap operation, implemented by the SwapT functions, is the atomic equivalent of:

```go
old = *addr
*addr = new
return old

```

The compare-and-swap operation, implemented by the CompareAndSwapT functions, is the atomic equivalent of:

```go
if *addr == old {
	*addr = new
	return true
}
return false

```

The add operation, implemented by the AddT functions, is the atomic equivalent of:

```go
*addr += delta
return *addr

```

The load and store operations, implemented by the LoadT and StoreT functions, are the atomic equivalents of "return *addr" and "*addr = val".

In the terminology of the Go memory model <https://go.dev/ref/mem>, if the effect of an atomic operation A is observed by atomic operation B, then A “synchronizes before” B. Additionally, all the atomic operations executed in a program behave as though executed in some sequentially consistent order. This definition provides the same semantics as C++'s sequentially consistent atomics and Java's volatile variables.

-  func AddInt32(addr *int32, delta int32) (new int32)
-  func AddInt64(addr *int64, delta int64) (new int64)
-  func AddUint32(addr *uint32, delta uint32) (new uint32)
-  func AddUint64(addr *uint64, delta uint64) (new uint64)
-  func AddUintptr(addr *uintptr, delta uintptr) (new uintptr)
-  func AndInt32(addr *int32, mask int32) (old int32)
-  func AndInt64(addr *int64, mask int64) (old int64)
-  func AndUint32(addr *uint32, mask uint32) (old uint32)
-  func AndUint64(addr *uint64, mask uint64) (old uint64)
-  func AndUintptr(addr *uintptr, mask uintptr) (old uintptr)
-  func CompareAndSwapInt32(addr *int32, old, new int32) (swapped bool)
-  func CompareAndSwapInt64(addr *int64, old, new int64) (swapped bool)
-  func CompareAndSwapPointer(addr *unsafe.Pointer, old, new unsafe.Pointer) (swapped bool)
-  func CompareAndSwapUint32(addr *uint32, old, new uint32) (swapped bool)
-  func CompareAndSwapUint64(addr *uint64, old, new uint64) (swapped bool)
-  func CompareAndSwapUintptr(addr *uintptr, old, new uintptr) (swapped bool)
-  func LoadInt32(addr *int32) (val int32)
-  func LoadInt64(addr *int64) (val int64)
-  func LoadPointer(addr *unsafe.Pointer) (val unsafe.Pointer)
-  func LoadUint32(addr *uint32) (val uint32)
-  func LoadUint64(addr *uint64) (val uint64)
-  func LoadUintptr(addr *uintptr) (val uintptr)
-  func OrInt32(addr *int32, mask int32) (old int32)
-  func OrInt64(addr *int64, mask int64) (old int64)
-  func OrUint32(addr *uint32, mask uint32) (old uint32)
-  func OrUint64(addr *uint64, mask uint64) (old uint64)
-  func OrUintptr(addr *uintptr, mask uintptr) (old uintptr)
-  func StoreInt32(addr *int32, val int32)
-  func StoreInt64(addr *int64, val int64)
-  func StorePointer(addr *unsafe.Pointer, val unsafe.Pointer)
-  func StoreUint32(addr *uint32, val uint32)
-  func StoreUint64(addr *uint64, val uint64)
-  func StoreUintptr(addr *uintptr, val uintptr)
-  func SwapInt32(addr *int32, new int32) (old int32)
-  func SwapInt64(addr *int64, new int64) (old int64)
-  func SwapPointer(addr *unsafe.Pointer, new unsafe.Pointer) (old unsafe.Pointer)
-  func SwapUint32(addr *uint32, new uint32) (old uint32)
-  func SwapUint64(addr *uint64, new uint64) (old uint64)
-  func SwapUintptr(addr *uintptr, new uintptr) (old uintptr)
-  type Bool
-
-  func (x *Bool) CompareAndSwap(old, new bool) (swapped bool)
-  func (x *Bool) Load() bool
-  func (x *Bool) Store(val bool)
-  func (x *Bool) Swap(new bool) (old bool)

-  type Int32
-
-  func (x *Int32) Add(delta int32) (new int32)
-  func (x *Int32) And(mask int32) (old int32)
-  func (x *Int32) CompareAndSwap(old, new int32) (swapped bool)
-  func (x *Int32) Load() int32
-  func (x *Int32) Or(mask int32) (old int32)
-  func (x *Int32) Store(val int32)
-  func (x *Int32) Swap(new int32) (old int32)

-  type Int64
-
-  func (x *Int64) Add(delta int64) (new int64)
-  func (x *Int64) And(mask int64) (old int64)
-  func (x *Int64) CompareAndSwap(old, new int64) (swapped bool)
-  func (x *Int64) Load() int64
-  func (x *Int64) Or(mask int64) (old int64)
-  func (x *Int64) Store(val int64)
-  func (x *Int64) Swap(new int64) (old int64)

-  type Pointer
-
-  func (x *Pointer[T]) CompareAndSwap(old, new *T) (swapped bool)
-  func (x *Pointer[T]) Load() *T
-  func (x *Pointer[T]) Store(val *T)
-  func (x *Pointer[T]) Swap(new *T) (old *T)

-  type Uint32
-
-  func (x *Uint32) Add(delta uint32) (new uint32)
-  func (x *Uint32) And(mask uint32) (old uint32)
-  func (x *Uint32) CompareAndSwap(old, new uint32) (swapped bool)
-  func (x *Uint32) Load() uint32
-  func (x *Uint32) Or(mask uint32) (old uint32)
-  func (x *Uint32) Store(val uint32)
-  func (x *Uint32) Swap(new uint32) (old uint32)

-  type Uint64
-
-  func (x *Uint64) Add(delta uint64) (new uint64)
-  func (x *Uint64) And(mask uint64) (old uint64)
-  func (x *Uint64) CompareAndSwap(old, new uint64) (swapped bool)
-  func (x *Uint64) Load() uint64
-  func (x *Uint64) Or(mask uint64) (old uint64)
-  func (x *Uint64) Store(val uint64)
-  func (x *Uint64) Swap(new uint64) (old uint64)

-  type Uintptr
-
-  func (x *Uintptr) Add(delta uintptr) (new uintptr)
-  func (x *Uintptr) And(mask uintptr) (old uintptr)
-  func (x *Uintptr) CompareAndSwap(old, new uintptr) (swapped bool)
-  func (x *Uintptr) Load() uintptr
-  func (x *Uintptr) Or(mask uintptr) (old uintptr)
-  func (x *Uintptr) Store(val uintptr)
-  func (x *Uintptr) Swap(new uintptr) (old uintptr)

-  type Value
-
-  func (v *Value) CompareAndSwap(old, new any) (swapped bool)
-  func (v *Value) Load() (val any)
-  func (v *Value) Store(val any)
-  func (v *Value) Swap(new any) (old any)

- Bugs

- Value (Config)
- Value (ReadMostly)

This section is empty.

This section is empty.

```go
func AddInt32(addr *int32, delta int32) (new int32)
```

AddInt32 atomically adds delta to *addr and returns the new value. Consider using the more ergonomic and less error-prone Int32.Add instead.

```go
func AddInt64(addr *int64, delta int64) (new int64)
```

AddInt64 atomically adds delta to *addr and returns the new value. Consider using the more ergonomic and less error-prone Int64.Add instead (particularly if you target 32-bit platforms; see the bugs section).

```go
func AddUint32(addr *uint32, delta uint32) (new uint32)
```

AddUint32 atomically adds delta to *addr and returns the new value. To subtract a signed positive constant value c from x, do AddUint32(&x, ^uint32(c-1)). In particular, to decrement x, do AddUint32(&x, ^uint32(0)). Consider using the more ergonomic and less error-prone Uint32.Add instead.

```go
func AddUint64(addr *uint64, delta uint64) (new uint64)
```

AddUint64 atomically adds delta to *addr and returns the new value. To subtract a signed positive constant value c from x, do AddUint64(&x, ^uint64(c-1)). In particular, to decrement x, do AddUint64(&x, ^uint64(0)). Consider using the more ergonomic and less error-prone Uint64.Add instead (particularly if you target 32-bit platforms; see the bugs section).

```go
func AddUintptr(addr *uintptr, delta uintptr) (new uintptr)
```

AddUintptr atomically adds delta to *addr and returns the new value. Consider using the more ergonomic and less error-prone Uintptr.Add instead.

```go
func AndInt32(addr *int32, mask int32) (old int32)
```

AndInt32 atomically performs a bitwise AND operation on *addr using the bitmask provided as mask and returns the old value. Consider using the more ergonomic and less error-prone Int32.And instead.

```go
func AndInt64(addr *int64, mask int64) (old int64)
```

AndInt64 atomically performs a bitwise AND operation on *addr using the bitmask provided as mask and returns the old value. Consider using the more ergonomic and less error-prone Int64.And instead.

```go
func AndUint32(addr *uint32, mask uint32) (old uint32)
```

AndUint32 atomically performs a bitwise AND operation on *addr using the bitmask provided as mask and returns the old value. Consider using the more ergonomic and less error-prone Uint32.And instead.

```go
func AndUint64(addr *uint64, mask uint64) (old uint64)
```

AndUint64 atomically performs a bitwise AND operation on *addr using the bitmask provided as mask and returns the old. Consider using the more ergonomic and less error-prone Uint64.And instead.

```go
func AndUintptr(addr *uintptr, mask uintptr) (old uintptr)
```

AndUintptr atomically performs a bitwise AND operation on *addr using the bitmask provided as mask and returns the old value. Consider using the more ergonomic and less error-prone Uintptr.And instead.

```go
func CompareAndSwapInt32(addr *int32, old, new int32) (swapped bool)
```

CompareAndSwapInt32 executes the compare-and-swap operation for an int32 value. Consider using the more ergonomic and less error-prone Int32.CompareAndSwap instead.

```go
func CompareAndSwapInt64(addr *int64, old, new int64) (swapped bool)
```

CompareAndSwapInt64 executes the compare-and-swap operation for an int64 value. Consider using the more ergonomic and less error-prone Int64.CompareAndSwap instead (particularly if you target 32-bit platforms; see the bugs section).

```go
func CompareAndSwapPointer(addr *unsafe.Pointer, old, new unsafe.Pointer) (swapped bool)
```

CompareAndSwapPointer executes the compare-and-swap operation for a unsafe.Pointer value. Consider using the more ergonomic and less error-prone Pointer.CompareAndSwap instead.

```go
func CompareAndSwapUint32(addr *uint32, old, new uint32) (swapped bool)
```

CompareAndSwapUint32 executes the compare-and-swap operation for a uint32 value. Consider using the more ergonomic and less error-prone Uint32.CompareAndSwap instead.

```go
func CompareAndSwapUint64(addr *uint64, old, new uint64) (swapped bool)
```

CompareAndSwapUint64 executes the compare-and-swap operation for a uint64 value. Consider using the more ergonomic and less error-prone Uint64.CompareAndSwap instead (particularly if you target 32-bit platforms; see the bugs section).

```go
func CompareAndSwapUintptr(addr *uintptr, old, new uintptr) (swapped bool)
```

CompareAndSwapUintptr executes the compare-and-swap operation for a uintptr value. Consider using the more ergonomic and less error-prone Uintptr.CompareAndSwap instead.

```go
func LoadInt32(addr *int32) (val int32)
```
