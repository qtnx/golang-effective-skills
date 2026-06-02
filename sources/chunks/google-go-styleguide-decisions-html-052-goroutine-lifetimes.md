---
source_name: "Google Go Style Guide"
source_url: "https://google.github.io/styleguide/go/"
source_path: "sources/raw/google-go-styleguide/decisions.html"
license_ref: "sources/licenses/google-styleguide-LICENSE.txt"
---

### Goroutine lifetimes

When you spawn goroutines, make it clear when or whether they exit.

Goroutines can leak by blocking on channel sends or receives. The garbage collector will not terminate a goroutine blocked on a channel even if no other goroutine has a reference to the channel.

Even when goroutines do not leak, leaving them in-flight when they are no longer needed can cause other subtle and hard-to-diagnose problems. Sending on a channel that has been closed causes a panic.

```go
// Bad:
ch := make(chan int)
ch <- 42
close(ch)
ch <- 13 // panic

```

Modifying still-in-use inputs “after the result isn’t needed” can lead to data races. Leaving goroutines in-flight for arbitrarily long can lead to unpredictable memory usage.

Concurrent code should be written such that the goroutine lifetimes are obvious. Typically this will mean keeping synchronization-related code constrained within the scope of a function and factoring out the logic into synchronous functions. If the concurrency is still not obvious, it is important to document when and why the goroutines exit.

Code that follows best practices around context usage often helps make this clear. It is conventionally managed with a `context.Context`:

```go
// Good:
func (w *Worker) Run(ctx context.Context) error {
    var wg sync.WaitGroup
    // ...
    for item := range w.q {
        // process returns at latest when the context is cancelled.
        wg.Add(1)
        go func() {
            defer wg.Done()
            process(ctx, item)
        }()
    }
    // ...
    wg.Wait()  // Prevent spawned goroutines from outliving this function.
}

```

There are other variants of the above that use raw signal channels like `chan struct{}`, synchronized variables, condition variables, and more. The important part is that the goroutine’s end is evident for subsequent maintainers.

In contrast, the following code is careless about when its spawned goroutines finish:

```go
// Bad:
func (w *Worker) Run() {
    // ...
    for item := range w.q {
        // process returns when it finishes, if ever, possibly not cleanly
        // handling a state transition or termination of the Go program itself.
        go process(item)
    }
    // ...
}

```

This code may look OK, but there are several underlying problems:

-
The code probably has undefined behavior in production, and the program may not terminate cleanly, even if the operating system releases the resources.

-
The code is difficult to test meaningfully due to the code’s indeterminate lifecycle.

-
The code may leak resources as described above.

See also:

- Never start a goroutine without knowing how it will stop
- Rethinking Classical Concurrency Patterns: slides, video
- When Go programs end
- Documentation Conventions: Contexts
