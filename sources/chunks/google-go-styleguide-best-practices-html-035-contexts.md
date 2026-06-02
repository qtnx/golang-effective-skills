---
source_name: "Google Go Style Guide"
source_url: "https://google.github.io/styleguide/go/"
source_path: "sources/raw/google-go-styleguide/best-practices.html"
license_ref: "sources/licenses/google-styleguide-LICENSE.txt"
---

#### Contexts

It is implied that the cancellation of a context argument interrupts the function it is provided to. If the function can return an error, conventionally it is `ctx.Err()`.

This fact does not need to be restated:

```go
// Bad:
// Run executes the worker's run loop.
//
// The method will process work until the context is cancelled and accordingly
// returns an error.
func (Worker) Run(ctx context.Context) error

```

Because that is implied, the following is better:

```go
// Good:
// Run executes the worker's run loop.
func (Worker) Run(ctx context.Context) error

```

Where context behavior is different or non-obvious, it should be expressly documented if any of the following are true.

-
The function returns an error other than `ctx.Err()` when the context is cancelled:

```go
// Good:
// Run executes the worker's run loop.
//
// If the context is cancelled, Run returns a nil error.
func (Worker) Run(ctx context.Context) error

```

-
The function has other mechanisms that may interrupt it or affect lifetime:

```go
// Good:
// Run executes the worker's run loop.
//
// Run processes work until the context is cancelled or Stop is called.
// Context cancellation is handled asynchronously internally: run may return
// before all work has stopped. The Stop method is synchronous and waits
// until all operations from the run loop finish. Use Stop for graceful
// shutdown.
func (Worker) Run(ctx context.Context) error

func (Worker) Stop()

```

-
The function has special expectations about context lifetime, lineage, or attached values:

```go
// Good:
// NewReceiver starts receiving messages sent to the specified queue.
// The context should not have a deadline.
func NewReceiver(ctx context.Context) *Receiver

// Principal returns a human-readable name of the party who made the call.
// The context must have a value attached to it from security.NewContext.
func Principal(ctx context.Context) (name string, ok bool)

```

**Warning:** Avoid designing APIs that make such demands (like contexts not having deadlines) from their callers. The above is only an example of how to document this if it cannot be avoided, not an endorsement of the pattern.
