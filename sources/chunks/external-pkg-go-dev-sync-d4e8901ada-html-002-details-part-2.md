---
source_name: "External Linked Documentation"
source_url: "https://pkg.go.dev/sync"
source_path: "sources/raw/external/pkg-go-dev-sync-d4e8901ada.html"
license_ref: ""
---

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
