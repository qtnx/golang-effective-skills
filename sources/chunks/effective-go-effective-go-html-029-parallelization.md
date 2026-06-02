---
source_name: "Effective Go"
source_url: "https://go.dev/doc/effective_go"
source_path: "sources/raw/effective-go/effective_go.html"
license_ref: "sources/licenses/go-LICENSE.txt"
---

## Concurrency

### Parallelization

 Another application of these ideas is to parallelize a calculation across multiple CPU cores. If the calculation can be broken into separate pieces that can execute independently, it can be parallelized, with a channel to signal when each piece completes.

 Let's say we have an expensive operation to perform on a vector of items, and that the value of the operation on each item is independent, as in this idealized example.

```go

type Vector []float64

// Apply the operation to v[i], v[i+1] ... up to v[n-1].
func (v Vector) DoSome(i, n int, u Vector, c chan int) {
    for ; i < n; i++ {
        v[i] += u.Op(v[i])
    }
    c <- 1    // signal that this piece is done
}

```

 We launch the pieces independently in a loop, one per CPU. They can complete in any order but it doesn't matter; we just count the completion signals by draining the channel after launching all the goroutines.

```go

const numCPU = 4 // number of CPU cores

func (v Vector) DoAll(u Vector) {
    c := make(chan int, numCPU)  // Buffering optional but sensible.
    for i := 0; i < numCPU; i++ {
        go v.DoSome(i*len(v)/numCPU, (i+1)*len(v)/numCPU, u, c)
    }
    // Drain the channel.
    for i := 0; i < numCPU; i++ {
        <-c    // wait for one task to complete
    }
    // All done.
}

```

 Rather than create a constant value for numCPU, we can ask the runtime what value is appropriate. The function `runtime.NumCPU` returns the number of hardware CPU cores in the machine, so we could write

```go

var numCPU = runtime.NumCPU()

```

 There is also a function `runtime.GOMAXPROCS`, which reports (or sets) the user-specified number of cores that a Go program can have running simultaneously. It defaults to the value of `runtime.NumCPU` but can be overridden by setting the similarly named shell environment variable or by calling the function with a positive number. Calling it with zero just queries the value. Therefore if we want to honor the user's resource request, we should write

```go

var numCPU = runtime.GOMAXPROCS(0)

```

 Be sure not to confuse the ideas of concurrency—structuring a program as independently executing components—and parallelism—executing calculations in parallel for efficiency on multiple CPUs. Although the concurrency features of Go can make some problems easy to structure as parallel computations, Go is a concurrent language, not a parallel one, and not all parallelization problems fit Go's model. For a discussion of the distinction, see the talk cited in this blog post.
