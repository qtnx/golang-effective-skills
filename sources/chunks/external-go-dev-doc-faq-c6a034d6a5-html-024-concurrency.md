---
source_name: "External Linked Documentation"
source_url: "https://go.dev/doc/faq"
source_path: "sources/raw/external/go-dev-doc-faq-c6a034d6a5.html"
license_ref: ""
---

# Frequently Asked Questions (FAQ)

## Concurrency

### What operations are atomic? What about mutexes?

A description of the atomicity of operations in Go can be found in the Go Memory Model document.

Low-level synchronization and atomic primitives are available in the sync and sync/atomic packages. These packages are good for simple tasks such as incrementing reference counts or guaranteeing small-scale mutual exclusion.

For higher-level operations, such as coordination among concurrent servers, higher-level techniques can lead to nicer programs, and Go supports this approach through its goroutines and channels. For instance, you can structure your program so that only one goroutine at a time is ever responsible for a particular piece of data. That approach is summarized by the original Go proverb <https://www.youtube.com/watch?v=PAAkCSZUG1c>,

Do not communicate by sharing memory. Instead, share memory by communicating.

See the Share Memory By Communicating code walk and its associated article for a detailed discussion of this concept.

Large concurrent programs are likely to borrow from both these toolkits.

### Why doesn’t my program run faster with more CPUs?

Whether a program runs faster with more CPUs depends on the problem it is solving. The Go language provides concurrency primitives, such as goroutines and channels, but concurrency only enables parallelism when the underlying problem is intrinsically parallel. Problems that are intrinsically sequential cannot be sped up by adding more CPUs, while those that can be broken into pieces that can execute in parallel can be sped up, sometimes dramatically.

Sometimes adding more CPUs can slow a program down. In practical terms, programs that spend more time synchronizing or communicating than doing useful computation may experience performance degradation when using multiple OS threads. This is because passing data between threads involves switching contexts, which has significant cost, and that cost can increase with more CPUs. For instance, the prime sieve example from the Go specification has no significant parallelism although it launches many goroutines; increasing the number of threads (CPUs) is more likely to slow it down than to speed it up.

For more detail on this topic see the talk entitled Concurrency is not Parallelism.

### How can I control the number of CPUs?

The number of CPUs available simultaneously to executing goroutines is controlled by the `GOMAXPROCS` shell environment variable, whose default value is the number of CPU cores available. Programs with the potential for parallel execution should therefore achieve it by default on a multiple-CPU machine. To change the number of parallel CPUs to use, set the environment variable or use the similarly-named function of the runtime package to configure the run-time support to utilize a different number of threads. Setting it to 1 eliminates the possibility of true parallelism, forcing independent goroutines to take turns executing.

The runtime can allocate more threads than the value of `GOMAXPROCS` to service multiple outstanding I/O requests. `GOMAXPROCS` only affects how many goroutines can actually execute at once; arbitrarily more may be blocked in system calls.

Go’s goroutine scheduler does well at balancing goroutines and threads, and can even preempt execution of a goroutine to make sure others on the same thread are not starved. However, it is not perfect. If you see performance issues, setting `GOMAXPROCS` on a per-application basis may help.

### Why is there no goroutine ID?

Goroutines do not have names; they are just anonymous workers. They expose no unique identifier, name, or data structure to the programmer. Some people are surprised by this, expecting the `go` statement to return some item that can be used to access and control the goroutine later.

The fundamental reason goroutines are anonymous is so that the full Go language is available when programming concurrent code. By contrast, the usage patterns that develop when threads and goroutines are named can restrict what a library using them can do.

Here is an illustration of the difficulties. Once one names a goroutine and constructs a model around it, it becomes special, and one is tempted to associate all computation with that goroutine, ignoring the possibility of using multiple, possibly shared goroutines for the processing. If the `net/http` package associated per-request state with a goroutine, clients would be unable to use more goroutines when serving a request.

Moreover, experience with libraries such as those for graphics systems that require all processing to occur on the “main thread” has shown how awkward and limiting the approach can be when deployed in a concurrent language. The very existence of a special thread or goroutine forces the programmer to distort the program to avoid crashes and other problems caused by inadvertently operating on the wrong thread.

For those cases where a particular goroutine is truly special, the language provides features such as channels that can be used in flexible ways to interact with it.
