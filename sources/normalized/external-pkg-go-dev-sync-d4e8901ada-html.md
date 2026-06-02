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

## Links

-    Report a Vulnerability  <https://go.dev/security/policy>

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

```go
func (m *Map) LoadOrStore(key, value any) (actual any, loaded bool)
```

LoadOrStore returns the existing value for the key if present. Otherwise, it stores and returns the given value. The loaded result is true if the value was loaded, false if stored.

```go
func (m *Map) Range(f func(key, value any) bool)
```

Range calls f sequentially for each key and value present in the map. If f returns false, range stops the iteration.

Range does not necessarily correspond to any consistent snapshot of the Map's contents: no key will be visited more than once, but if the value for any key is stored or deleted concurrently (including by f), Range may reflect any mapping for that key from any point during the Range call. Range does not block other methods on the receiver; even f itself may call any method on m.

Range may be O(N) with the number of elements in the map even if f returns false after a constant number of calls.

```go
func (m *Map) Store(key, value any)
```

Store sets the value for a key.

```go
func (m *Map) Swap(key, value any) (previous any, loaded bool)
```

Swap swaps the value for a key and returns the previous value if any. The loaded result reports whether the key was present.

```go
type Mutex struct {
	// contains filtered or unexported fields
}
```

A Mutex is a mutual exclusion lock. The zero value for a Mutex is an unlocked mutex.

A Mutex must not be copied after first use.

In the terminology of the Go memory model <https://go.dev/ref/mem>, the n'th call to Mutex.Unlock “synchronizes before” the m'th call to Mutex.Lock for any n < m. A successful call to Mutex.TryLock is equivalent to a call to Lock. A failed call to TryLock does not establish any “synchronizes before” relation at all.

```go
func (m *Mutex) Lock()
```

Lock locks m. If the lock is already in use, the calling goroutine blocks until the mutex is available.

```go
func (m *Mutex) TryLock() bool
```

TryLock tries to lock m and reports whether it succeeded.

Note that while correct uses of TryLock do exist, they are rare, and use of TryLock is often a sign of a deeper problem in a particular use of mutexes.

```go
func (m *Mutex) Unlock()
```

Unlock unlocks m. It is a run-time error if m is not locked on entry to Unlock.

A locked Mutex is not associated with a particular goroutine. It is allowed for one goroutine to lock a Mutex and then arrange for another goroutine to unlock it.

```go
type Once struct {
	// contains filtered or unexported fields
}
```

Once is an object that will perform exactly one action.

A Once must not be copied after first use.

In the terminology of the Go memory model <https://go.dev/ref/mem>, the return from f “synchronizes before” the return from any call of once.Do(f).

```go

package main

import (
	"fmt"
	"sync"
)

func main() {
	var once sync.Once
	onceBody := func() {
		fmt.Println("Only once")
	}
	done := make(chan bool)
	for i := 0; i < 10; i++ {
		go func() {
			once.Do(onceBody)
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
Only once

```

 Share Format Run

```go
func (o *Once) Do(f func())
```

Do calls the function f if and only if Do is being called for the first time for this instance of Once. In other words, given

```go
var once Once

```

if once.Do(f) is called multiple times, only the first call will invoke f, even if f has a different value in each invocation. A new instance of Once is required for each function to execute.

Do is intended for initialization that must be run exactly once. Since f is niladic, it may be necessary to use a function literal to capture the arguments to a function to be invoked by Do:

```go
config.once.Do(func() { config.init(filename) })

```

Because no call to Do returns until the one call to f returns, if f causes Do to be called, it will deadlock.

If f panics, Do considers it to have returned; future calls of Do return without calling f.

```go
type Pool struct {

	// New optionally specifies a function to generate
	// a value when Get would otherwise return nil.
	// It may not be changed concurrently with calls to Get.
	New func() any
	// contains filtered or unexported fields
}
```

A Pool is a set of temporary objects that may be individually saved and retrieved.

Any item stored in the Pool may be removed automatically at any time without notification. If the Pool holds the only reference when this happens, the item might be deallocated.

A Pool is safe for use by multiple goroutines simultaneously.

Pool's purpose is to cache allocated but unused items for later reuse, relieving pressure on the garbage collector. That is, it makes it easy to build efficient, thread-safe free lists. However, it is not suitable for all free lists.

An appropriate use of a Pool is to manage a group of temporary items silently shared among and potentially reused by concurrent independent clients of a package. Pool provides a way to amortize allocation overhead across many clients.

An example of good use of a Pool is in the fmt package, which maintains a dynamically-sized store of temporary output buffers. The store scales under load (when many goroutines are actively printing) and shrinks when quiescent.

On the other hand, a free list maintained as part of a short-lived object is not a suitable use for a Pool, since the overhead does not amortize well in that scenario. It is more efficient to have such objects implement their own free list.

A Pool must not be copied after first use.

In the terminology of the Go memory model <https://go.dev/ref/mem>, a call to Put(x) “synchronizes before” a call to Pool.Get returning that same value x. Similarly, a call to New returning x “synchronizes before” a call to Get returning that same value x.

```go

package main

import (
	"bytes"
	"io"
	"os"
	"sync"
	"time"
)

var bufPool = sync.Pool{
	New: func() any {
		// The Pool's New function should generally only return pointer
		// types, since a pointer can be put into the return interface
		// value without an allocation:
		return new(bytes.Buffer)
	},
}

// timeNow is a fake version of time.Now for tests.
func timeNow() time.Time {
	return time.Unix(1136214245, 0)
}

func Log(w io.Writer, key, val string) {
	b := bufPool.Get().(*bytes.Buffer)
	b.Reset()
	// Replace this with time.Now() in a real logger.
	b.WriteString(timeNow().UTC().Format(time.RFC3339))
	b.WriteByte(' ')
	b.WriteString(key)
	b.WriteByte('=')
	b.WriteString(val)
	w.Write(b.Bytes())
	bufPool.Put(b)
}

func main() {
	Log(os.Stdout, "path", "/search?q=flowers")
}

```

```go
Output:
2006-01-02T15:04:05Z path=/search?q=flowers

```

 Share Format Run

```go
func (p *Pool) Get() any
```

Get selects an arbitrary item from the Pool, removes it from the Pool, and returns it to the caller. Get may choose to ignore the pool and treat it as empty. Callers should not assume any relation between values passed to Pool.Put and the values returned by Get.

If Get would otherwise return nil and p.New is non-nil, Get returns the result of calling p.New.

```go
func (p *Pool) Put(x any)
```

Put adds x to the pool.

```go
type RWMutex struct {
	// contains filtered or unexported fields
}
```

A RWMutex is a reader/writer mutual exclusion lock. The lock can be held by an arbitrary number of readers or a single writer. The zero value for a RWMutex is an unlocked mutex.

A RWMutex must not be copied after first use.

If any goroutine calls RWMutex.Lock while the lock is already held by one or more readers, concurrent calls to RWMutex.RLock will block until the writer has acquired (and released) the lock, to ensure that the lock eventually becomes available to the writer. Note that this prohibits recursive read-locking. A RWMutex.RLock cannot be upgraded into a RWMutex.Lock, nor can a RWMutex.Lock be downgraded into a RWMutex.RLock.

In the terminology of the Go memory model <https://go.dev/ref/mem>, the n'th call to RWMutex.Unlock “synchronizes before” the m'th call to Lock for any n < m, just as for Mutex. For any call to RLock, there exists an n such that the n'th call to Unlock “synchronizes before” that call to RLock, and the corresponding call to RWMutex.RUnlock “synchronizes before” the n+1'th call to Lock.

```go
func (rw *RWMutex) Lock()
```

Lock locks rw for writing. If the lock is already locked for reading or writing, Lock blocks until the lock is available.

```go
func (rw *RWMutex) RLock()
```

RLock locks rw for reading.

It should not be used for recursive read locking; a blocked Lock call excludes new readers from acquiring the lock. See the documentation on the RWMutex type.

```go
func (rw *RWMutex) RLocker() Locker
```

RLocker returns a Locker interface that implements the [Locker.Lock] and [Locker.Unlock] methods by calling rw.RLock and rw.RUnlock.

```go
func (rw *RWMutex) RUnlock()
```

RUnlock undoes a single RWMutex.RLock call; it does not affect other simultaneous readers. It is a run-time error if rw is not locked for reading on entry to RUnlock.

```go
func (rw *RWMutex) TryLock() bool
```

TryLock tries to lock rw for writing and reports whether it succeeded.

Note that while correct uses of TryLock do exist, they are rare, and use of TryLock is often a sign of a deeper problem in a particular use of mutexes.

```go
func (rw *RWMutex) TryRLock() bool
```

TryRLock tries to lock rw for reading and reports whether it succeeded.

Note that while correct uses of TryRLock do exist, they are rare, and use of TryRLock is often a sign of a deeper problem in a particular use of mutexes.

```go
func (rw *RWMutex) Unlock()
```

Unlock unlocks rw for writing. It is a run-time error if rw is not locked for writing on entry to Unlock.

As with Mutexes, a locked RWMutex is not associated with a particular goroutine. One goroutine may RWMutex.RLock (RWMutex.Lock) a RWMutex and then arrange for another goroutine to RWMutex.RUnlock (RWMutex.Unlock) it.

```go
type WaitGroup struct {
	// contains filtered or unexported fields
}
```

A WaitGroup is a counting semaphore typically used to wait for a group of goroutines or tasks to finish.

Typically, a main goroutine will start tasks, each in a new goroutine, by calling WaitGroup.Go and then wait for all tasks to complete by calling WaitGroup.Wait. For example:

```go
var wg sync.WaitGroup
wg.Go(task1)
wg.Go(task2)
wg.Wait()

```

A WaitGroup may also be used for tracking tasks without using Go to start new goroutines by using WaitGroup.Add and WaitGroup.Done.

The previous example can be rewritten using explicitly created goroutines along with Add and Done:

```go
var wg sync.WaitGroup
wg.Add(1)
go func() {
	defer wg.Done()
	task1()
}()
wg.Add(1)
go func() {
	defer wg.Done()
	task2()
}()
wg.Wait()

```

This pattern is common in code that predates WaitGroup.Go.

A WaitGroup must not be copied after first use.

This example fetches several URLs concurrently, using a WaitGroup to block until all the fetches are complete.

```go

package main

import (
	"sync"
)

type httpPkg struct{}

func (httpPkg) Get(url string) {}

var http httpPkg

func main() {
	var wg sync.WaitGroup
	var urls = []string{
		"http://www.golang.org/",
		"http://www.google.com/",
		"http://www.example.com/",
	}
	for _, url := range urls {
		// Launch a goroutine to fetch the URL.
		wg.Go(func() {
			// Fetch the URL.
			http.Get(url)
		})
	}
	// Wait for all HTTP fetches to complete.
	wg.Wait()
}

```

```go
Output:

```

 Share Format Run

This example is equivalent to the main example, but uses Add/Done instead of Go.

```go

package main

import (
	"sync"
)

type httpPkg struct{}

func (httpPkg) Get(url string) {}

var http httpPkg

func main() {
	var wg sync.WaitGroup
	var urls = []string{
		"http://www.golang.org/",
		"http://www.google.com/",
		"http://www.example.com/",
	}
	for _, url := range urls {
		// Increment the WaitGroup counter.
		wg.Add(1)
		// Launch a goroutine to fetch the URL.
		go func(url string) {
			// Decrement the counter when the goroutine completes.
			defer wg.Done()
			// Fetch the URL.
			http.Get(url)
		}(url)
	}
	// Wait for all HTTP fetches to complete.
	wg.Wait()
}

```

```go
Output:

```

 Share Format Run

```go
func (wg *WaitGroup) Add(delta int)
```

Add adds delta, which may be negative, to the WaitGroup task counter. If the counter becomes zero, all goroutines blocked on WaitGroup.Wait are released. If the counter goes negative, Add panics.

Callers should prefer WaitGroup.Go.

Note that calls with a positive delta that occur when the counter is zero must happen before a Wait. Calls with a negative delta, or calls with a positive delta that start when the counter is greater than zero, may happen at any time. Typically this means the calls to Add should execute before the statement creating the goroutine or other event to be waited for. If a WaitGroup is reused to wait for several independent sets of events, new Add calls must happen after all previous Wait calls have returned. See the WaitGroup example.

```go
func (wg *WaitGroup) Done()
```

Done decrements the WaitGroup task counter by one. It is equivalent to Add(-1).

Callers should prefer WaitGroup.Go.

In the terminology of the Go memory model <https://go.dev/ref/mem>, a call to Done "synchronizes before" the return of any Wait call that it unblocks.

```go
func (wg *WaitGroup) Go(f func())
```

Go calls f in a new goroutine and adds that task to the WaitGroup. When f returns, the task is removed from the WaitGroup.

The function f must not panic.

If the WaitGroup is empty, Go must happen before a WaitGroup.Wait. Typically, this simply means Go is called to start tasks before Wait is called. If the WaitGroup is not empty, Go may happen at any time. This means a goroutine started by Go may itself call Go. If a WaitGroup is reused to wait for several independent sets of tasks, new Go calls must happen after all previous Wait calls have returned.

In the terminology of the Go memory model <https://go.dev/ref/mem>, the return from f "synchronizes before" the return of any Wait call that it unblocks.

```go
func (wg *WaitGroup) Wait()
```

Wait blocks until the WaitGroup task counter is zero.

##   Source Files ¶
 View all Source files <https://cs.opensource.google/go/go/+/go1.26.3:src/sync>

- cond.go <https://cs.opensource.google/go/go/+/go1.26.3:src/sync/cond.go>
- map.go <https://cs.opensource.google/go/go/+/go1.26.3:src/sync/map.go>
- mutex.go <https://cs.opensource.google/go/go/+/go1.26.3:src/sync/mutex.go>
- once.go <https://cs.opensource.google/go/go/+/go1.26.3:src/sync/once.go>
- oncefunc.go <https://cs.opensource.google/go/go/+/go1.26.3:src/sync/oncefunc.go>
- pool.go <https://cs.opensource.google/go/go/+/go1.26.3:src/sync/pool.go>
- poolqueue.go <https://cs.opensource.google/go/go/+/go1.26.3:src/sync/poolqueue.go>
- runtime.go <https://cs.opensource.google/go/go/+/go1.26.3:src/sync/runtime.go>
- runtime2.go <https://cs.opensource.google/go/go/+/go1.26.3:src/sync/runtime2.go>
- rwmutex.go <https://cs.opensource.google/go/go/+/go1.26.3:src/sync/rwmutex.go>
- waitgroup.go <https://cs.opensource.google/go/go/+/go1.26.3:src/sync/waitgroup.go>

##   Directories ¶
    Show internal   Expand all

      atomic
 Package atomic provides low-level atomic memory primitives useful for implementing synchronization algorithms.

  Package atomic provides low-level atomic memory primitives useful for implementing synchronization algorithms.

  Click to show internal directories.
  Click to hide internal directories.

  Close

     **?** : This menu   **/** : Search site   **f** or **F** : Jump to   **y** or **Y**  : Canonical URL
  Close
