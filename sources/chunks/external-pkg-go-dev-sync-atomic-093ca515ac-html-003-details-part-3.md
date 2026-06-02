---
source_name: "External Linked Documentation"
source_url: "https://pkg.go.dev/sync/atomic"
source_path: "sources/raw/external/pkg-go-dev-sync-atomic-093ca515ac.html"
license_ref: ""
---

```go
func (x *Uint64) Swap(new uint64) (old uint64)
```

Swap atomically stores new into x and returns the previous value.

```go
type Uintptr struct {
	// contains filtered or unexported fields
}
```

A Uintptr is an atomic uintptr. The zero value is zero.

Uintptr must not be copied after first use.

```go
func (x *Uintptr) Add(delta uintptr) (new uintptr)
```

Add atomically adds delta to x and returns the new value.

```go
func (x *Uintptr) And(mask uintptr) (old uintptr)
```

And atomically performs a bitwise AND operation on x using the bitmask provided as mask and returns the old value.

```go
func (x *Uintptr) CompareAndSwap(old, new uintptr) (swapped bool)
```

CompareAndSwap executes the compare-and-swap operation for x.

```go
func (x *Uintptr) Load() uintptr
```

Load atomically loads and returns the value stored in x.

```go
func (x *Uintptr) Or(mask uintptr) (old uintptr)
```

Or atomically performs a bitwise OR operation on x using the bitmask provided as mask and returns the old value.

```go
func (x *Uintptr) Store(val uintptr)
```

Store atomically stores val into x.

```go
func (x *Uintptr) Swap(new uintptr) (old uintptr)
```

Swap atomically stores new into x and returns the previous value.

```go
type Value struct {
	// contains filtered or unexported fields
}
```

A Value provides an atomic load and store of a consistently typed value. The zero value for a Value returns nil from Value.Load. Once Value.Store has been called, a Value must not be copied.

A Value must not be copied after first use.

The following example shows how to use Value for periodic program config updates and propagation of the changes to worker goroutines.

```go

package main

import (
	"sync/atomic"
	"time"
)

func loadConfig() map[string]string {
	return make(map[string]string)
}

func requests() chan int {
	return make(chan int)
}

func main() {
	var config atomic.Value // holds current server configuration
	// Create initial config value and store into config.
	config.Store(loadConfig())
	go func() {
		// Reload config every 10 seconds
		// and update config value with the new version.
		for {
			time.Sleep(10 * time.Second)
			config.Store(loadConfig())
		}
	}()
	// Create worker goroutines that handle incoming requests
	// using the latest config value.
	for i := 0; i < 10; i++ {
		go func() {
			for r := range requests() {
				c := config.Load()
				// Handle request r using config c.
				_, _ = r, c
			}
		}()
	}
}

```

```go
Output:

```

Share Format Run

The following example shows how to maintain a scalable frequently read, but infrequently updated data structure using copy-on-write idiom.

```go

package main

import (
	"sync"
	"sync/atomic"
)

func main() {
	type Map map[string]string
	var m atomic.Value
	m.Store(make(Map))
	var mu sync.Mutex // used only by writers
	// read function can be used to read the data without further synchronization
	read := func(key string) (val string) {
		m1 := m.Load().(Map)
		return m1[key]
	}
	// insert function can be used to update the data without further synchronization
	insert := func(key, val string) {
		mu.Lock() // synchronize with other potential writers
		defer mu.Unlock()
		m1 := m.Load().(Map) // load current value of the data structure
		m2 := make(Map)      // create a new value
		for k, v := range m1 {
			m2[k] = v // copy all data from the current object to the new one
		}
		m2[key] = val // do the update that we need
		m.Store(m2)   // atomically replace the current object with the new one
		// At this point all new readers start working with the new version.
		// The old version will be garbage collected once the existing readers
		// (if any) are done with it.
	}
	_, _ = read, insert
}

```

```go
Output:

```

Share Format Run

```go
func (v *Value) CompareAndSwap(old, new any) (swapped bool)
```

CompareAndSwap executes the compare-and-swap operation for the Value.

All calls to CompareAndSwap for a given Value must use values of the same concrete type. CompareAndSwap of an inconsistent type panics, as does CompareAndSwap(old, nil).

```go
func (v *Value) Load() (val any)
```

Load returns the value set by the most recent Store. It returns nil if there has been no call to Store for this Value.

```go
func (v *Value) Store(val any)
```

Store sets the value of the Value v to val. All calls to Store for a given Value must use values of the same concrete type. Store of an inconsistent type panics, as does Store(nil).

```go
func (v *Value) Swap(new any) (old any)
```

Swap stores new into Value and returns the previous value. It returns nil if the Value is empty.

All calls to Swap for a given Value must use values of the same concrete type. Swap of an inconsistent type panics, as does Swap(nil).

-
On 386, the 64-bit functions use instructions unavailable before the Pentium MMX.

On non-Linux ARM, the 64-bit functions use instructions unavailable before the ARMv6k core.

On ARM, 386, and 32-bit MIPS, it is the caller's responsibility to arrange for 64-bit alignment of 64-bit words accessed atomically via the primitive atomic functions (types Int64 and Uint64 are automatically aligned). The first word in an allocated struct, array, or slice; in a global variable; or in a local variable (because on 32-bit architectures, the subject of 64-bit atomic operations will escape to the heap) can be relied upon to be 64-bit aligned.

##   Source Files ¶
 View all Source files <https://cs.opensource.google/go/go/+/go1.26.3:src/sync/atomic>

- doc.go <https://cs.opensource.google/go/go/+/go1.26.3:src/sync/atomic/doc.go>
- doc_64.go <https://cs.opensource.google/go/go/+/go1.26.3:src/sync/atomic/doc_64.go>
- type.go <https://cs.opensource.google/go/go/+/go1.26.3:src/sync/atomic/type.go>
- value.go <https://cs.opensource.google/go/go/+/go1.26.3:src/sync/atomic/value.go>

Click to show internal directories.
  Click to hide internal directories.

Close

**?** : This menu   **/** : Search site   **f** or **F** : Jump to   **y** or **Y**  : Canonical URL
  Close
