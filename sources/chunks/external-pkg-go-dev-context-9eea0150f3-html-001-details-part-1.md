---
source_name: "External Linked Documentation"
source_url: "https://pkg.go.dev/context"
source_path: "sources/raw/external/pkg-go-dev-context-9eea0150f3.html"
license_ref: ""
---

context package - context - Go Packages
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

Package context defines the Context type, which carries deadlines, cancellation signals, and other request-scoped values across API boundaries and between processes.

Incoming requests to a server should create a Context, and outgoing calls to servers should accept a Context. The chain of function calls between them must propagate the Context, optionally replacing it with a derived Context created using WithCancel, WithDeadline, WithTimeout, or WithValue.

A Context may be canceled to indicate that work done on its behalf should stop. A Context with a deadline is canceled after the deadline passes. When a Context is canceled, all Contexts derived from it are also canceled.

The WithCancel, WithDeadline, and WithTimeout functions take a Context (the parent) and return a derived Context (the child) and a CancelFunc. Calling the CancelFunc directly cancels the child and its children, removes the parent's reference to the child, and stops any associated timers. Failing to call the CancelFunc leaks the child and its children until the parent is canceled. The go vet tool checks that CancelFuncs are used on all control-flow paths.

The WithCancelCause, WithDeadlineCause, and WithTimeoutCause functions return a CancelCauseFunc, which takes an error and records it as the cancellation cause. Calling Cause on the canceled context or any of its children retrieves the cause. If no cause is specified, Cause(ctx) returns the same value as ctx.Err().

Programs that use Contexts should follow these rules to keep interfaces consistent across packages and enable static analysis tools to check context propagation:

Do not store Contexts inside a struct type; instead, pass a Context explicitly to each function that needs it. This is discussed further in https://go.dev/blog/context-and-structs <https://go.dev/blog/context-and-structs>. The Context should be the first parameter, typically named ctx:

```go
func DoSomething(ctx context.Context, arg Arg) error {
	// ... use ctx ...
}

```

Do not pass a nil Context, even if a function permits it. Pass context.TODO if you are unsure about which Context to use.

Use context Values only for request-scoped data that transits processes and APIs, not for passing optional parameters to functions.

The same Context may be passed to functions running in different goroutines; Contexts are safe for simultaneous use by multiple goroutines.

See https://go.dev/blog/context <https://go.dev/blog/context> for example code for a server that uses Contexts.

- Variables
-  func AfterFunc(ctx Context, f func()) (stop func() bool)
-  func Cause(c Context) error
-  func WithCancel(parent Context) (ctx Context, cancel CancelFunc)
-  func WithCancelCause(parent Context) (ctx Context, cancel CancelCauseFunc)
-  func WithDeadline(parent Context, d time.Time) (Context, CancelFunc)
-  func WithDeadlineCause(parent Context, d time.Time, cause error) (Context, CancelFunc)
-  func WithTimeout(parent Context, timeout time.Duration) (Context, CancelFunc)
-  func WithTimeoutCause(parent Context, timeout time.Duration, cause error) (Context, CancelFunc)
-  type CancelCauseFunc
-  type CancelFunc
-  type Context
-
-  func Background() Context
-  func TODO() Context
-  func WithValue(parent Context, key, val any) Context
-  func WithoutCancel(parent Context) Context

- AfterFunc (Cond)
- AfterFunc (Connection)
- AfterFunc (Merge)
- WithCancel
- WithDeadline
- WithTimeout
- WithValue

This section is empty.

View Source <https://cs.opensource.google/go/go/+/go1.26.3:src/context/context.go;l=167>
```go
var Canceled = errors.New("context canceled")
```

Canceled is the error returned by [Context.Err] when the context is canceled for some reason other than its deadline passing.
  View Source <https://cs.opensource.google/go/go/+/go1.26.3:src/context/context.go;l=171>
```go
var DeadlineExceeded error = deadlineExceededError{}
```

DeadlineExceeded is the error returned by [Context.Err] when the context is canceled due to its deadline passing.

```go
func AfterFunc(ctx Context, f func()) (stop func() bool)
```

AfterFunc arranges to call f in its own goroutine after ctx is canceled. If ctx is already canceled, AfterFunc calls f immediately in its own goroutine.

Multiple calls to AfterFunc on a context operate independently; one does not replace another.

Calling the returned stop function stops the association of ctx with f. It returns true if the call stopped f from being run. If stop returns false, either the context is canceled and f has been started in its own goroutine; or f was already stopped. The stop function does not wait for f to complete before returning. If the caller needs to know whether f is completed, it must coordinate with f explicitly.

If ctx has a "AfterFunc(func()) func() bool" method, AfterFunc will use it to schedule the call.

This example uses AfterFunc to define a function which waits on a sync.Cond, stopping the wait when a context is canceled.

```go

package main

import (
	"context"
	"fmt"
	"sync"
	"time"
)

func main() {
	waitOnCond := func(ctx context.Context, cond *sync.Cond, conditionMet func() bool) error {
		stopf := context.AfterFunc(ctx, func() {
			// We need to acquire cond.L here to be sure that the Broadcast
			// below won't occur before the call to Wait, which would result
			// in a missed signal (and deadlock).
			cond.L.Lock()
			defer cond.L.Unlock()

// If multiple goroutines are waiting on cond simultaneously,
			// we need to make sure we wake up exactly this one.
			// That means that we need to Broadcast to all of the goroutines,
			// which will wake them all up.
			//
			// If there are N concurrent calls to waitOnCond, each of the goroutines
			// will spuriously wake up O(N) other goroutines that aren't ready yet,
			// so this will cause the overall CPU cost to be O(N²).
			cond.Broadcast()
		})
		defer stopf()

// Since the wakeups are using Broadcast instead of Signal, this call to
		// Wait may unblock due to some other goroutine's context being canceled,
		// so to be sure that ctx is actually canceled we need to check it in a loop.
		for !conditionMet() {
			cond.Wait()
			if ctx.Err() != nil {
				return ctx.Err()
			}
		}

return nil
	}

cond := sync.NewCond(new(sync.Mutex))

var wg sync.WaitGroup
	for i := 0; i < 4; i++ {
		wg.Add(1)
		go func() {
			defer wg.Done()

ctx, cancel := context.WithTimeout(context.Background(), 1*time.Millisecond)
			defer cancel()

cond.L.Lock()
			defer cond.L.Unlock()

err := waitOnCond(ctx, cond, func() bool { return false })
			fmt.Println(err)
		}()
	}
	wg.Wait()

}

```

```go
Output:
context deadline exceeded
context deadline exceeded
context deadline exceeded
context deadline exceeded

```

Share Format Run

This example uses AfterFunc to define a function which reads from a net.Conn, stopping the read when a context is canceled.

```go

package main

import (
	"context"
	"fmt"
	"net"
	"time"
)

func main() {
	readFromConn := func(ctx context.Context, conn net.Conn, b []byte) (n int, err error) {
		stopc := make(chan struct{})
		stop := context.AfterFunc(ctx, func() {
			conn.SetReadDeadline(time.Now())
			close(stopc)
		})
		n, err = conn.Read(b)
		if !stop() {
			// The AfterFunc was started.
			// Wait for it to complete, and reset the Conn's deadline.
			<-stopc
			conn.SetReadDeadline(time.Time{})
			return n, ctx.Err()
		}
		return n, err
	}

listener, err := net.Listen("tcp", "localhost:0")
	if err != nil {
		fmt.Println(err)
		return
	}
	defer listener.Close()

conn, err := net.Dial(listener.Addr().Network(), listener.Addr().String())
	if err != nil {
		fmt.Println(err)
		return
	}
	defer conn.Close()

ctx, cancel := context.WithTimeout(context.Background(), 1*time.Millisecond)
	defer cancel()

b := make([]byte, 1024)
	_, err = readFromConn(ctx, conn, b)
	fmt.Println(err)

}

```

```go
Output:
context deadline exceeded

```

Share Format Run

This example uses AfterFunc to define a function which combines the cancellation signals of two Contexts.

```go

package main

import (
	"context"
	"errors"
	"fmt"
)

func main() {
	// mergeCancel returns a context that contains the values of ctx,
	// and which is canceled when either ctx or cancelCtx is canceled.
	mergeCancel := func(ctx, cancelCtx context.Context) (context.Context, context.CancelFunc) {
		ctx, cancel := context.WithCancelCause(ctx)
		stop := context.AfterFunc(cancelCtx, func() {
			cancel(context.Cause(cancelCtx))
		})
		return ctx, func() {
			stop()
			cancel(context.Canceled)
		}
	}

ctx1, cancel1 := context.WithCancelCause(context.Background())
	defer cancel1(errors.New("ctx1 canceled"))

ctx2, cancel2 := context.WithCancelCause(context.Background())

mergedCtx, mergedCancel := mergeCancel(ctx1, ctx2)
	defer mergedCancel()

cancel2(errors.New("ctx2 canceled"))
	<-mergedCtx.Done()
	fmt.Println(context.Cause(mergedCtx))

}

```

```go
Output:
ctx2 canceled

```

Share Format Run

```go
func Cause(c Context) error
```

Cause returns a non-nil error explaining why c was canceled. The first cancellation of c or one of its parents sets the cause. If that cancellation happened via a call to CancelCauseFunc(err), then Cause returns err. Otherwise Cause(c) returns the same value as c.Err(). Cause returns nil if c has not been canceled yet.

```go
func WithCancel(parent Context) (ctx Context, cancel CancelFunc)
```

WithCancel returns a derived context that points to the parent context but has a new Done channel. The returned context's Done channel is closed when the returned cancel function is called or when the parent context's Done channel is closed, whichever happens first.

Canceling this context releases resources associated with it, so code should call cancel as soon as the operations running in this Context complete.

This example demonstrates the use of a cancelable context to prevent a goroutine leak. By the end of the example function, the goroutine started by gen will return without leaking.

```go

package main

import (
	"context"
	"fmt"
)

func main() {
	// gen generates integers in a separate goroutine and
	// sends them to the returned channel.
	// The callers of gen need to cancel the context once
	// they are done consuming generated integers not to leak
	// the internal goroutine started by gen.
	gen := func(ctx context.Context) <-chan int {
		dst := make(chan int)
		n := 1
		go func() {
			for {
				select {
				case <-ctx.Done():
					return // returning not to leak the goroutine
				case dst <- n:
					n++
				}
			}
		}()
		return dst
	}
