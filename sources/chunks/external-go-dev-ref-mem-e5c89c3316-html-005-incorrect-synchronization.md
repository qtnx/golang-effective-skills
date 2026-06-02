---
source_name: "External Linked Documentation"
source_url: "https://go.dev/ref/mem"
source_path: "sources/raw/external/go-dev-ref-mem-e5c89c3316.html"
license_ref: ""
---

# The Go Memory Model

## Incorrect synchronization

 Programs with races are incorrect and can exhibit non-sequentially consistent executions. In particular, note that a read _r_ may observe the value written by any write _w_ that executes concurrently with _r_. Even if this occurs, it does not imply that reads happening after _r_ will observe writes that happened before _w_.

 In this program:

```go

var a, b int

func f() {
	a = 1
	b = 2
}

func g() {
	print(b)
	print(a)
}

func main() {
	go f()
	g()
}

```

 it can happen that `g` prints `2` and then `0`.

 This fact invalidates a few common idioms.

 Double-checked locking is an attempt to avoid the overhead of synchronization. For example, the `twoprint` program might be incorrectly written as:

```go

var a string
var done bool

func setup() {
	a = "hello, world"
	done = true
}

func doprint() {
	if !done {
		once.Do(setup)
	}
	print(a)
}

func twoprint() {
	go doprint()
	go doprint()
}

```

 but there is no guarantee that, in `doprint`, observing the write to `done` implies observing the write to `a`. This version can (incorrectly) print an empty string instead of `"hello, world"`.

 Another incorrect idiom is busy waiting for a value, as in:

```go

var a string
var done bool

func setup() {
	a = "hello, world"
	done = true
}

func main() {
	go setup()
	for !done {
	}
	print(a)
}

```

 As before, there is no guarantee that, in `main`, observing the write to `done` implies observing the write to `a`, so this program could print an empty string too. Worse, there is no guarantee that the write to `done` will ever be observed by `main`, since there are no synchronization events between the two threads. The loop in `main` is not guaranteed to finish.

 There are subtler variants on this theme, such as this program.

```go

type T struct {
	msg string
}

var g *T

func setup() {
	t := new(T)
	t.msg = "hello, world"
	g = t
}

func main() {
	go setup()
	for g == nil {
	}
	print(g.msg)
}

```

 Even if `main` observes `g != nil` and exits its loop, there is no guarantee that it will observe the initialized value for `g.msg`.

 In all these examples, the solution is the same: use explicit synchronization.
