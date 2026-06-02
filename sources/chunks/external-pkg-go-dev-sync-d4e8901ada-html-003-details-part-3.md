---
source_name: "External Linked Documentation"
source_url: "https://pkg.go.dev/sync"
source_path: "sources/raw/external/pkg-go-dev-sync-d4e8901ada.html"
license_ref: ""
---

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
