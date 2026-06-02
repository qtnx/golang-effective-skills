---
source_name: "External Linked Documentation"
source_url: "https://pkg.go.dev/context"
source_path: "sources/raw/external/pkg-go-dev-context-9eea0150f3.html"
license_ref: ""
---

ctx, cancel := context.WithCancel(context.Background())
	defer cancel() // cancel when we are finished consuming integers

for n := range gen(ctx) {
		fmt.Println(n)
		if n == 5 {
			break
		}
	}
}

```

```go
Output:
1
2
3
4
5

```

Share Format Run

```go
func WithCancelCause(parent Context) (ctx Context, cancel CancelCauseFunc)
```

WithCancelCause behaves like WithCancel but returns a CancelCauseFunc instead of a CancelFunc. Calling cancel with a non-nil error (the "cause") records that error in ctx; it can then be retrieved using Cause(ctx). Calling cancel with nil sets the cause to Canceled.

Example use:

```go
ctx, cancel := context.WithCancelCause(parent)
cancel(myError)
ctx.Err() // returns context.Canceled
context.Cause(ctx) // returns myError

```

```go
func WithDeadline(parent Context, d time.Time) (Context, CancelFunc)
```

WithDeadline returns a derived context that points to the parent context but has the deadline adjusted to be no later than d. If the parent's deadline is already earlier than d, WithDeadline(parent, d) is semantically equivalent to parent. The returned [Context.Done] channel is closed when the deadline expires, when the returned cancel function is called, or when the parent context's Done channel is closed, whichever happens first.

Canceling this context releases resources associated with it, so code should call cancel as soon as the operations running in this Context complete.

This example passes a context with an arbitrary deadline to tell a blocking function that it should abandon its work as soon as it gets to it.

```go

d := time.Now().Add(shortDuration)
ctx, cancel := context.WithDeadline(context.Background(), d)

// Even though ctx will be expired, it is good practice to call its
// cancellation function in any case. Failure to do so may keep the
// context and its parent alive longer than necessary.
defer cancel()

select {
case <-neverReady:
	fmt.Println("ready")
case <-ctx.Done():
	fmt.Println(ctx.Err())
}

```

```go
Output:
context deadline exceeded

```

```go
func WithDeadlineCause(parent Context, d time.Time, cause error) (Context, CancelFunc)
```

WithDeadlineCause behaves like WithDeadline but also sets the cause of the returned Context when the deadline is exceeded. The returned CancelFunc does not set the cause.

```go
func WithTimeout(parent Context, timeout time.Duration) (Context, CancelFunc)
```

WithTimeout returns WithDeadline(parent, time.Now().Add(timeout)).

Canceling this context releases resources associated with it, so code should call cancel as soon as the operations running in this Context complete:

```go
func slowOperationWithTimeout(ctx context.Context) (Result, error) {
	ctx, cancel := context.WithTimeout(ctx, 100*time.Millisecond)
	defer cancel()  // releases resources if slowOperation completes before timeout elapses
	return slowOperation(ctx)
}

```

This example passes a context with a timeout to tell a blocking function that it should abandon its work after the timeout elapses.

```go

// Pass a context with a timeout to tell a blocking function that it
// should abandon its work after the timeout elapses.
ctx, cancel := context.WithTimeout(context.Background(), shortDuration)
defer cancel()

select {
case <-neverReady:
	fmt.Println("ready")
case <-ctx.Done():
	fmt.Println(ctx.Err()) // prints "context deadline exceeded"
}

```

```go
Output:
context deadline exceeded

```

```go
func WithTimeoutCause(parent Context, timeout time.Duration, cause error) (Context, CancelFunc)
```

WithTimeoutCause behaves like WithTimeout but also sets the cause of the returned Context when the timeout expires. The returned CancelFunc does not set the cause.

```go
type CancelCauseFunc func(cause error)
```

A CancelCauseFunc behaves like a CancelFunc but additionally sets the cancellation cause. This cause can be retrieved by calling Cause on the canceled Context or on any of its derived Contexts.

If the context has already been canceled, CancelCauseFunc does not set the cause. For example, if childContext is derived from parentContext:

- if parentContext is canceled with cause1 before childContext is canceled with cause2, then Cause(parentContext) == Cause(childContext) == cause1
- if childContext is canceled with cause2 before parentContext is canceled with cause1, then Cause(parentContext) == cause1 and Cause(childContext) == cause2

```go
type CancelFunc func()
```

A CancelFunc tells an operation to abandon its work. A CancelFunc does not wait for the work to stop. A CancelFunc may be called by multiple goroutines simultaneously. After the first call, subsequent calls to a CancelFunc do nothing.

```go
type Context interface {
	// Deadline returns the time when work done on behalf of this context
	// should be canceled. Deadline returns ok==false when no deadline is
	// set. Successive calls to Deadline return the same results.
	Deadline() (deadline time.Time, ok bool)

// Done returns a channel that's closed when work done on behalf of this
	// context should be canceled. Done may return nil if this context can
	// never be canceled. Successive calls to Done return the same value.
	// The close of the Done channel may happen asynchronously,
	// after the cancel function returns.
	//
	// WithCancel arranges for Done to be closed when cancel is called;
	// WithDeadline arranges for Done to be closed when the deadline
	// expires; WithTimeout arranges for Done to be closed when the timeout
	// elapses.
	//
	// Done is provided for use in select statements:
	//
	//  // Stream generates values with DoSomething and sends them to out
	//  // until DoSomething returns an error or ctx.Done is closed.
	//  func Stream(ctx context.Context, out chan<- Value) error {
	//  	for {
	//  		v, err := DoSomething(ctx)
	//  		if err != nil {
	//  			return err
	//  		}
	//  		select {
	//  		case <-ctx.Done():
	//  			return ctx.Err()
	//  		case out <- v:
	//  		}
	//  	}
	//  }
	//
	// See https://go.dev/blog/pipelines <https://go.dev/blog/pipelines> for more examples of how to use
	// a Done channel for cancellation.
	Done() <-chan struct{}

// If Done is not yet closed, Err returns nil.
	// If Done is closed, Err returns a non-nil error explaining why:
	// DeadlineExceeded if the context's deadline passed,
	// or Canceled if the context was canceled for some other reason.
	// After Err returns a non-nil error, successive calls to Err return the same error.
	Err() error

// Value returns the value associated with this context for key, or nil
	// if no value is associated with key. Successive calls to Value with
	// the same key returns the same result.
	//
	// Use context values only for request-scoped data that transits
	// processes and API boundaries, not for passing optional parameters to
	// functions.
	//
	// A key identifies a specific value in a Context. Functions that wish
	// to store values in Context typically allocate a key in a global
	// variable then use that key as the argument to context.WithValue and
	// Context.Value. A key can be any type that supports equality;
	// packages should define keys as an unexported type to avoid
	// collisions.
	//
	// Packages that define a Context key should provide type-safe accessors
	// for the values stored using that key:
	//
	// 	// Package user defines a User type that's stored in Contexts.
	// 	package user
	//
	// 	import "context"
	//
	// 	// User is the type of value stored in the Contexts.
	// 	type User struct {...}
	//
	// 	// key is an unexported type for keys defined in this package.
	// 	// This prevents collisions with keys defined in other packages.
	// 	type key int
	//
	// 	// userKey is the key for user.User values in Contexts. It is
	// 	// unexported; clients use user.NewContext and user.FromContext
	// 	// instead of using this key directly.
	// 	var userKey key
	//
	// 	// NewContext returns a new Context that carries value u.
	// 	func NewContext(ctx context.Context, u *User) context.Context {
	// 		return context.WithValue(ctx, userKey, u)
	// 	}
	//
	// 	// FromContext returns the User value stored in ctx, if any.
	// 	func FromContext(ctx context.Context) (*User, bool) {
	// 		u, ok := ctx.Value(userKey).(*User)
	// 		return u, ok
	// 	}
	Value(key any) any
}
```

A Context carries a deadline, a cancellation signal, and other values across API boundaries.

Context's methods may be called by multiple goroutines simultaneously.

```go
func Background() Context
```

Background returns a non-nil, empty Context. It is never canceled, has no values, and has no deadline. It is typically used by the main function, initialization, and tests, and as the top-level Context for incoming requests.

```go
func TODO() Context
```

TODO returns a non-nil, empty Context. Code should use context.TODO when it's unclear which Context to use or it is not yet available (because the surrounding function has not yet been extended to accept a Context parameter).

```go
func WithValue(parent Context, key, val any) Context
```

WithValue returns a derived context that points to the parent Context. In the derived context, the value associated with key is val.

Use context Values only for request-scoped data that transits processes and APIs, not for passing optional parameters to functions.

The provided key must be comparable and should not be of type string or any other built-in type to avoid collisions between packages using context. Users of WithValue should define their own types for keys. To avoid allocating when assigning to an interface{}, context keys often have concrete type struct{}. Alternatively, exported context key variables' static type should be a pointer or interface.

This example demonstrates how a value can be passed to the context and also how to retrieve it if it exists.

```go

package main

import (
	"context"
	"fmt"
)

func main() {
	type favContextKey string

f := func(ctx context.Context, k favContextKey) {
		if v := ctx.Value(k); v != nil {
			fmt.Println("found value:", v)
			return
		}
		fmt.Println("key not found:", k)
	}

k := favContextKey("language")
	ctx := context.WithValue(context.Background(), k, "Go")

f(ctx, k)
	f(ctx, favContextKey("color"))

}

```

```go
Output:
found value: Go
key not found: color

```

Share Format Run

```go
func WithoutCancel(parent Context) Context
```
