---
source_name: "External Linked Documentation"
source_url: "https://pkg.go.dev/sync"
source_path: "sources/raw/external/pkg-go-dev-sync-d4e8901ada.html"
license_ref: ""
---

sync package - sync - Go Packages
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

Package sync provides basic synchronization primitives such as mutual exclusion locks. Other than the Once and WaitGroup types, most are intended for use by low-level library routines. Higher-level synchronization is better done via channels and communication.

Values containing the types defined in this package should not be copied.

-  func OnceFunc(f func()) func()
-  func OnceValue[T any](f func() T) func() T
-  func OnceValues[T1, T2 any](f func() (T1, T2)) func() (T1, T2)
-  type Cond
-
-  func NewCond(l Locker) *Cond

-
-  func (c *Cond) Broadcast()
-  func (c *Cond) Signal()
-  func (c *Cond) Wait()

-  type Locker
-  type Map
-
-  func (m *Map) Clear()
-  func (m *Map) CompareAndDelete(key, old any) (deleted bool)
-  func (m *Map) CompareAndSwap(key, old, new any) (swapped bool)
-  func (m *Map) Delete(key any)
-  func (m *Map) Load(key any) (value any, ok bool)
-  func (m *Map) LoadAndDelete(key any) (value any, loaded bool)
-  func (m *Map) LoadOrStore(key, value any) (actual any, loaded bool)
-  func (m *Map) Range(f func(key, value any) bool)
-  func (m *Map) Store(key, value any)
-  func (m *Map) Swap(key, value any) (previous any, loaded bool)

-  type Mutex
-
-  func (m *Mutex) Lock()
-  func (m *Mutex) TryLock() bool
-  func (m *Mutex) Unlock()

-  type Once
-
-  func (o *Once) Do(f func())

-  type Pool
-
-  func (p *Pool) Get() any
-  func (p *Pool) Put(x any)

-  type RWMutex
-
-  func (rw *RWMutex) Lock()
-  func (rw *RWMutex) RLock()
-  func (rw *RWMutex) RLocker() Locker
-  func (rw *RWMutex) RUnlock()
-  func (rw *RWMutex) TryLock() bool
-  func (rw *RWMutex) TryRLock() bool
-  func (rw *RWMutex) Unlock()

-  type WaitGroup
-
-  func (wg *WaitGroup) Add(delta int)
-  func (wg *WaitGroup) Done()
-  func (wg *WaitGroup) Go(f func())
-  func (wg *WaitGroup) Wait()

- Once
- OnceValue
- OnceValues
- Pool
- WaitGroup
- WaitGroup (AddAndDone)

This section is empty.

This section is empty.

```go
func OnceFunc(f func()) func()
```

OnceFunc returns a function that invokes f only once. The returned function may be called concurrently.

If f panics, the returned function will panic with the same value on every call.

```go
func OnceValue[T any](f func() T) func() T
```

OnceValue returns a function that invokes f only once and returns the value returned by f. The returned function may be called concurrently.

If f panics, the returned function will panic with the same value on every call.

This example uses OnceValue to perform an "expensive" computation just once, even when used concurrently.

```go

package main

import (
	"fmt"
	"sync"
)

func main() {
	once := sync.OnceValue(func() int {
		sum := 0
		for i := 0; i < 1000; i++ {
			sum += i
		}
		fmt.Println("Computed once:", sum)
		return sum
	})
	done := make(chan bool)
	for i := 0; i < 10; i++ {
		go func() {
			const want = 499500
			got := once()
			if got != want {
				fmt.Println("want", want, "got", got)
			}
			done <- true
		}()
	}
	for i := 0; i < 10; i++ {
		<-done
	}
}

```

```go
Output:
Computed once: 499500

```

Share Format Run

```go
func OnceValues[T1, T2 any](f func() (T1, T2)) func() (T1, T2)
```

OnceValues returns a function that invokes f only once and returns the values returned by f. The returned function may be called concurrently.

If f panics, the returned function will panic with the same value on every call.

This example uses OnceValues to read a file just once.

```go

package main

import (
	"fmt"
	"os"
	"sync"
)

func main() {
	once := sync.OnceValues(func() ([]byte, error) {
		fmt.Println("Reading file once")
		return os.ReadFile("example_test.go")
	})
	done := make(chan bool)
	for i := 0; i < 10; i++ {
		go func() {
			data, err := once()
			if err != nil {
				fmt.Println("error:", err)
			}
			_ = data // Ignore the data for this example
			done <- true
		}()
	}
	for i := 0; i < 10; i++ {
		<-done
	}
}

```

```go
Output:
Reading file once

```

Share Format Run

```go
type Cond struct {

// L is held while observing or changing the condition
	L Locker
	// contains filtered or unexported fields
}
```

Cond implements a condition variable, a rendezvous point for goroutines waiting for or announcing the occurrence of an event.

Each Cond has an associated Locker L (often a *Mutex or *RWMutex), which must be held when changing the condition and when calling the Cond.Wait method.

A Cond must not be copied after first use.

In the terminology of the Go memory model <https://go.dev/ref/mem>, Cond arranges that a call to Cond.Broadcast or Cond.Signal “synchronizes before” any Wait call that it unblocks.

For many simple use cases, users will be better off using channels than a Cond (Broadcast corresponds to closing a channel, and Signal corresponds to sending on a channel).

For more on replacements for sync.Cond, see Roberto Clapis's series on advanced concurrency patterns <https://blogtitle.github.io/categories/concurrency/>, as well as Bryan Mills's talk on concurrency patterns <https://drive.google.com/file/d/1nPdvhB0PutEJzdCq5ms6UI58dp50fcAN/view>.

```go
func NewCond(l Locker) *Cond
```

NewCond returns a new Cond with Locker l.

```go
func (c *Cond) Broadcast()
```

Broadcast wakes all goroutines waiting on c.

It is allowed but not required for the caller to hold c.L during the call.

```go
func (c *Cond) Signal()
```

Signal wakes one goroutine waiting on c, if there is any.

It is allowed but not required for the caller to hold c.L during the call.

Signal() does not affect goroutine scheduling priority; if other goroutines are attempting to lock c.L, they may be awoken before a "waiting" goroutine.

```go
func (c *Cond) Wait()
```

Wait atomically unlocks c.L and suspends execution of the calling goroutine. After later resuming execution, Wait locks c.L before returning. Unlike in other systems, Wait cannot return unless awoken by Cond.Broadcast or Cond.Signal.

Because c.L is not locked while Wait is waiting, the caller typically cannot assume that the condition is true when Wait returns. Instead, the caller should Wait in a loop:

```go
c.L.Lock()
for !condition() {
    c.Wait()
}
... make use of condition ...
c.L.Unlock()

```

```go
type Locker interface {
	Lock()
	Unlock()
}
```

A Locker represents an object that can be locked and unlocked.

```go
type Map struct {
	// contains filtered or unexported fields
}
```

Map is like a Go map[any]any but is safe for concurrent use by multiple goroutines without additional locking or coordination. Loads, stores, and deletes run in amortized constant time.

The Map type is specialized. Most code should use a plain Go map instead, with separate locking or coordination, for better type safety and to make it easier to maintain other invariants along with the map content.

The Map type is optimized for two common use cases: (1) when the entry for a given key is only ever written once but read many times, as in caches that only grow, or (2) when multiple goroutines read, write, and overwrite entries for disjoint sets of keys. In these two cases, use of a Map may significantly reduce lock contention compared to a Go map paired with a separate Mutex or RWMutex.

The zero Map is empty and ready for use. A Map must not be copied after first use.

In the terminology of the Go memory model <https://go.dev/ref/mem>, Map arranges that a write operation “synchronizes before” any read operation that observes the effect of the write, where read and write operations are defined as follows. Map.Load, Map.LoadAndDelete, Map.LoadOrStore, Map.Swap, Map.CompareAndSwap, and Map.CompareAndDelete are read operations; Map.Delete, Map.LoadAndDelete, Map.Store, and Map.Swap are write operations; Map.LoadOrStore is a write operation when it returns loaded set to false; Map.CompareAndSwap is a write operation when it returns swapped set to true; and Map.CompareAndDelete is a write operation when it returns deleted set to true.

```go
func (m *Map) Clear()
```

Clear deletes all the entries, resulting in an empty Map.

```go
func (m *Map) CompareAndDelete(key, old any) (deleted bool)
```

CompareAndDelete deletes the entry for key if its value is equal to old. The old value must be of a comparable type.

If there is no current value for key in the map, CompareAndDelete returns false (even if the old value is the nil interface value).

```go
func (m *Map) CompareAndSwap(key, old, new any) (swapped bool)
```

CompareAndSwap swaps the old and new values for key if the value stored in the map is equal to old. The old value must be of a comparable type.

```go
func (m *Map) Delete(key any)
```

Delete deletes the value for a key. If the key is not in the map, Delete does nothing.

```go
func (m *Map) Load(key any) (value any, ok bool)
```

Load returns the value stored in the map for a key, or nil if no value is present. The ok result indicates whether value was found in the map.

```go
func (m *Map) LoadAndDelete(key any) (value any, loaded bool)
```

LoadAndDelete deletes the value for a key, returning the previous value if any. The loaded result reports whether the key was present.
