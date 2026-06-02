---
source_name: "Uber Go Style Guide"
source_url: "https://github.com/uber-go/guide/blob/master/style.md"
source_path: "sources/raw/uber-go-guide/style.md"
license_ref: "sources/licenses/uber-go-guide-LICENSE.txt"
---

## Guidelines

### Don't fire-and-forget goroutines

Goroutines are lightweight, but they're not free:
at minimum, they cost memory for their stack and CPU to be scheduled.
While these costs are small for typical uses of goroutines,
they can cause significant performance issues
when spawned in large numbers without controlled lifetimes.
Goroutines with unmanaged lifetimes can also cause other issues
like preventing unused objects from being garbage collected
and holding onto resources that are otherwise no longer used.

Therefore, do not leak goroutines in production code.
Use [go.uber.org/goleak](https://pkg.go.dev/go.uber.org/goleak)
to test for goroutine leaks inside packages that may spawn goroutines.

In general, every goroutine:

- must have a predictable time at which it will stop running; or
- there must be a way to signal to the goroutine that it should stop

In both cases, there must be a way for code to block and wait for the goroutine to
finish.

For example:

<table>
<thead><tr><th>Bad</th><th>Good</th></tr></thead>
<tbody>
<tr><td>

```go
go func() {
  for {
    flush()
    time.Sleep(delay)
  }
}()
```

</td><td>

```go
var (
  stop = make(chan struct{}) // tells the goroutine to stop
  done = make(chan struct{}) // tells us that the goroutine exited
)
go func() {
  defer close(done)

  ticker := time.NewTicker(delay)
  defer ticker.Stop()
  for {
    select {
    case <-ticker.C:
      flush()
    case <-stop:
      return
    }
  }
}()

// Elsewhere...
close(stop)  // signal the goroutine to stop
<-done       // and wait for it to exit
```

</td></tr>
<tr><td>

There's no way to stop this goroutine.
This will run until the application exits.

</td><td>

This goroutine can be stopped with `close(stop)`,
and we can wait for it to exit with `<-done`.

</td></tr>
</tbody></table>

#### Wait for goroutines to exit

Given a goroutine spawned by the system,
there must be a way to wait for the goroutine to exit.
There are two popular ways to do this:

- Use a `sync.WaitGroup` to wait for multiple goroutines to complete.
  Do this if there are multiple goroutines that you want to wait for.

  ```go
  var wg sync.WaitGroup
  for i := 0; i < N; i++ {
    wg.Go(...)
  }

  // To wait for all to finish:
  wg.Wait()
  ```

- Add another `chan struct{}` that the goroutine closes when it's done.
  Do this if there's only one goroutine.

  ```go
  done := make(chan struct{})
  go func() {
    defer close(done)
    // ...
  }()

  // To wait for the goroutine to finish:
  <-done
  ```

#### No goroutines in `init()`

`init()` functions should not spawn goroutines.
See also [Avoid init()](#avoid-init).

If a package has need of a background goroutine,
it must expose an object that is responsible for managing a goroutine's
lifetime.
The object must provide a method (`Close`, `Stop`, `Shutdown`, etc)
that signals the background goroutine to stop, and waits for it to exit.

<table>
<thead><tr><th>Bad</th><th>Good</th></tr></thead>
<tbody>
<tr><td>

```go
func init() {
  go doWork()
}

func doWork() {
  for {
    // ...
  }
}
```

</td><td>

```go
type Worker struct{ /* ... */ }

func NewWorker(...) *Worker {
  w := &Worker{
    stop: make(chan struct{}),
    done: make(chan struct{}),
    // ...
  }
  go w.doWork()
  return w
}

func (w *Worker) doWork() {
  defer close(w.done)
  for {
    // ...
    case <-w.stop:
      return
  }
}

// Shutdown tells the worker to stop
// and waits until it has finished.
func (w *Worker) Shutdown() {
  close(w.stop)
  <-w.done
}
```

</td></tr>
<tr><td>

Spawns a background goroutine unconditionally when the user exports this package.
The user has no control over the goroutine or a means of stopping it.

</td><td>

Spawns the worker only if the user requests it.
Provides a means of shutting down the worker so that the user can free up
resources used by the worker.

Note that you should use `WaitGroup`s if the worker manages multiple
goroutines.
See [Wait for goroutines to exit](#wait-for-goroutines-to-exit).

</td></tr>
</tbody></table>
