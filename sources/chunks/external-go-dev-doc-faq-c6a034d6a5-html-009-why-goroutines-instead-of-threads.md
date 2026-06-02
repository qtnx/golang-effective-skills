---
source_name: "External Linked Documentation"
source_url: "https://go.dev/doc/faq"
source_path: "sources/raw/external/go-dev-doc-faq-c6a034d6a5.html"
license_ref: ""
---

## Design

### Why goroutines instead of threads?

Goroutines are part of making concurrency easy to use. The idea, which has been around for a while, is to multiplex independently executing functions—coroutines—onto a set of threads. When a coroutine blocks, such as by calling a blocking system call, the run-time automatically moves other coroutines on the same operating system thread to a different, runnable thread so they won’t be blocked. The programmer sees none of this, which is the point. The result, which we call goroutines, can be very cheap: they have little overhead beyond the memory for the stack, which is just a few kilobytes.

To make the stacks small, Go’s run-time uses resizable, bounded stacks. A newly minted goroutine is given a few kilobytes, which is almost always enough. When it isn’t, the run-time grows (and shrinks) the memory for storing the stack automatically, allowing many goroutines to live in a modest amount of memory. The CPU overhead averages about three cheap instructions per function call. It is practical to create hundreds of thousands of goroutines in the same address space. If goroutines were just threads, system resources would run out at a much smaller number.
