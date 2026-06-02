---
source_name: "External Linked Documentation"
source_url: "https://go.dev/ref/mem"
source_path: "sources/raw/external/go-dev-ref-mem-e5c89c3316.html"
license_ref: ""
---

# The Go Memory Model

## Synchronization

### Initialization

 Program initialization runs in a single goroutine, but that goroutine may create other goroutines, which run concurrently.

 If a package `p` imports package `q`, the completion of `q`'s `init` functions happens before the start of any of `p`'s.

 The completion of all `init` functions is synchronized before the start of the function `main.main`.

### Goroutine creation

 The `go` statement that starts a new goroutine is synchronized before the start of the goroutine's execution.

 For example, in this program:

```go

var a string

func f() {
	print(a)
}

func hello() {
	a = "hello, world"
	go f()
}

```

 calling `hello` will print `"hello, world"` at some point in the future (perhaps after `hello` has returned).

### Goroutine destruction

 The exit of a goroutine is not guaranteed to be synchronized before any event in the program. For example, in this program:

```go

var a string

func hello() {
	go func() { a = "hello" }()
	print(a)
}

```

 the assignment to `a` is not followed by any synchronization event, so it is not guaranteed to be observed by any other goroutine. In fact, an aggressive compiler might delete the entire `go` statement.

 If the effects of a goroutine must be observed by another goroutine, use a synchronization mechanism such as a lock or channel communication to establish a relative ordering.

### Channel communication

 Channel communication is the main method of synchronization between goroutines. Each send on a particular channel is matched to a corresponding receive from that channel, usually in a different goroutine.

 A send on a channel is synchronized before the completion of the corresponding receive from that channel.

 This program:

```go

var c = make(chan int, 10)
var a string

func f() {
	a = "hello, world"
	c <- 0
}

func main() {
	go f()
	<-c
	print(a)
}

```

 is guaranteed to print `"hello, world"`. The write to `a` is sequenced before the send on `c`, which is synchronized before the corresponding receive on `c` completes, which is sequenced before the `print`.

 The closing of a channel is synchronized before a receive that returns a zero value because the channel is closed.

 In the previous example, replacing `c <- 0` with `close(c)` yields a program with the same guaranteed behavior.

 A receive from an unbuffered channel is synchronized before the completion of the corresponding send on that channel.

 This program (as above, but with the send and receive statements swapped and using an unbuffered channel):

```go

var c = make(chan int)
var a string

func f() {
	a = "hello, world"
	<-c
}

func main() {
	go f()
	c <- 0
	print(a)
}

```

 is also guaranteed to print `"hello, world"`. The write to `a` is sequenced before the receive on `c`, which is synchronized before the corresponding send on `c` completes, which is sequenced before the `print`.

 If the channel were buffered (e.g., `c = make(chan int, 1)`) then the program would not be guaranteed to print `"hello, world"`. (It might print the empty string, crash, or do something else.)

 The _k_th receive from a channel with capacity _C_ is synchronized before the completion of the _k_+_C_th send on that channel.

 This rule generalizes the previous rule to buffered channels. It allows a counting semaphore to be modeled by a buffered channel: the number of items in the channel corresponds to the number of active uses, the capacity of the channel corresponds to the maximum number of simultaneous uses, sending an item acquires the semaphore, and receiving an item releases the semaphore. This is a common idiom for limiting concurrency.

 This program starts a goroutine for every entry in the work list, but the goroutines coordinate using the `limit` channel to ensure that at most three are running work functions at a time.

```go

var limit = make(chan int, 3)

func main() {
	for _, w := range work {
		go func(w func()) {
			limit <- 1
			w()
			<-limit
		}(w)
	}
	select{}
}

```

### Locks

 The `sync` package implements two lock data types, `sync.Mutex` and `sync.RWMutex`.

 For any `sync.Mutex` or `sync.RWMutex` variable `l` and _n_ < _m_, call _n_ of `l.Unlock()` is synchronized before call _m_ of `l.Lock()` returns.

 This program:

```go

var l sync.Mutex
var a string

func f() {
	a = "hello, world"
	l.Unlock()
}

func main() {
	l.Lock()
	go f()
	l.Lock()
	print(a)
}

```

 is guaranteed to print `"hello, world"`. The first call to `l.Unlock()` (in `f`) is synchronized before the second call to `l.Lock()` (in `main`) returns, which is sequenced before the `print`.

 For any call to `l.RLock` on a `sync.RWMutex` variable `l`, there is an _n_ such that the _n_th call to `l.Unlock` is synchronized before the return from `l.RLock`, and the matching call to `l.RUnlock` is synchronized before the return from call _n_+1 to `l.Lock`.

 A successful call to `l.TryLock` (or `l.TryRLock`) is equivalent to a call to `l.Lock` (or `l.RLock`). An unsuccessful call has no synchronizing effect at all. As far as the memory model is concerned, `l.TryLock` (or `l.TryRLock`) may be considered to be able to return false even when the mutex _l_ is unlocked.

### Once

 The `sync` package provides a safe mechanism for initialization in the presence of multiple goroutines through the use of the `Once` type. Multiple threads can execute `once.Do(f)` for a particular `f`, but only one will run `f()`, and the other calls block until `f()` has returned.

 The completion of a single call of `f()` from `once.Do(f)` is synchronized before the return of any call of `once.Do(f)`.

 In this program:

```go

var a string
var once sync.Once

func setup() {
	a = "hello, world"
}

func doprint() {
	once.Do(setup)
	print(a)
}

func twoprint() {
	go doprint()
	go doprint()
}

```

 calling `twoprint` will call `setup` exactly once. The `setup` function will complete before either call of `print`. The result will be that `"hello, world"` will be printed twice.

### Atomic Values

 The APIs in the `sync/atomic` package are collectively “atomic operations” that can be used to synchronize the execution of different goroutines. If the effect of an atomic operation _A_ is observed by atomic operation _B_, then _A_ is synchronized before _B_. All the atomic operations executed in a program behave as though executed in some sequentially consistent order.

 The preceding definition has the same semantics as C++’s sequentially consistent atomics and Java’s `volatile` variables.

### Finalizers

 The `runtime` package provides a `SetFinalizer` function that adds a finalizer to be called when a particular object is no longer reachable by the program. A call to `SetFinalizer(x, f)` is synchronized before the finalization call `f(x)`.

### Additional Mechanisms

 The `sync` package provides additional synchronization abstractions, including condition variables, lock-free maps, allocation pools, and wait groups. The documentation for each of these specifies the guarantees it makes concerning synchronization.

 Other packages that provide synchronization abstractions should document the guarantees they make too.
