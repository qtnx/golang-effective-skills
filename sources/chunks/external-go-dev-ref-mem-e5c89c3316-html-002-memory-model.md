---
source_name: "External Linked Documentation"
source_url: "https://go.dev/ref/mem"
source_path: "sources/raw/external/go-dev-ref-mem-e5c89c3316.html"
license_ref: ""
---

# The Go Memory Model

## Memory Model

 The following formal definition of Go's memory model closely follows the approach presented by Hans-J. Boehm and Sarita V. Adve in “Foundations of the C++ Concurrency Memory Model <https://dl.acm.org/doi/10.1145/1375581.1375591>”, published in PLDI 2008. The definition of data-race-free programs and the guarantee of sequential consistency for race-free programs are equivalent to the ones in that work.

 The memory model describes the requirements on program executions, which are made up of goroutine executions, which in turn are made up of memory operations.

 A _memory operation_ is modeled by four details:

- its kind, indicating whether it is an ordinary data read, an ordinary data write, or a _synchronizing operation_ such as an atomic data access, a mutex operation, or a channel operation,
- its location in the program,
- the memory location or variable being accessed, and
- the values read or written by the operation.

 Some memory operations are _read-like_, including read, atomic read, mutex lock, and channel receive. Other memory operations are _write-like_, including write, atomic write, mutex unlock, channel send, and channel close. Some, such as atomic compare-and-swap, are both read-like and write-like.

 A _goroutine execution_ is modeled as a set of memory operations executed by a single goroutine.

 **Requirement 1**: The memory operations in each goroutine must correspond to a correct sequential execution of that goroutine, given the values read from and written to memory. That execution must be consistent with the _sequenced before_ relation, defined as the partial order requirements set out by the Go language specification for Go's control flow constructs as well as the order of evaluation for expressions.

 A Go _program execution_ is modeled as a set of goroutine executions, together with a mapping _W_ that specifies the write-like operation that each read-like operation reads from. (Multiple executions of the same program can have different program executions.)

 **Requirement 2**: For a given program execution, the mapping _W_, when limited to synchronizing operations, must be explainable by some implicit total order of the synchronizing operations that is consistent with sequencing and the values read and written by those operations.

 The _synchronized before_ relation is a partial order on synchronizing memory operations, derived from _W_. If a synchronizing read-like memory operation _r_ observes a synchronizing write-like memory operation _w_ (that is, if _W_(_r_) = _w_), then _w_ is synchronized before _r_. Informally, the synchronized before relation is a subset of the implied total order mentioned in the previous paragraph, limited to the information that _W_ directly observes.

 The _happens before_ relation is defined as the transitive closure of the union of the sequenced before and synchronized before relations.

 **Requirement 3**: For an ordinary (non-synchronizing) data read _r_ on a memory location _x_, _W_(_r_) must be a write _w_ that is _visible_ to _r_, where visible means that both of the following hold:

- _w_ happens before _r_.
- _w_ does not happen before any other write _w'_ (to _x_) that happens before _r_.

 A _read-write data race_ on memory location _x_ consists of a read-like memory operation _r_ on _x_ and a write-like memory operation _w_ on _x_, at least one of which is non-synchronizing, which are unordered by happens before (that is, neither _r_ happens before _w_ nor _w_ happens before _r_).

 A _write-write data race_ on memory location _x_ consists of two write-like memory operations _w_ and _w'_ on _x_, at least one of which is non-synchronizing, which are unordered by happens before.

 Note that if there are no read-write or write-write data races on memory location _x_, then any read _r_ on _x_ has only one possible _W_(_r_): the single _w_ that immediately precedes it in the happens before order.

 More generally, it can be shown that any Go program that is data-race-free, meaning it has no program executions with read-write or write-write data races, can only have outcomes explained by some sequentially consistent interleaving of the goroutine executions. (The proof is the same as Section 7 of Boehm and Adve's paper cited above.) This property is called DRF-SC.

 The intent of the formal definition is to match the DRF-SC guarantee provided to race-free programs by other languages, including C, C++, Java, JavaScript, Rust, and Swift.

 Certain Go language operations such as goroutine creation and memory allocation act as synchronization operations. The effect of these operations on the synchronized-before partial order is documented in the “Synchronization” section below. Individual packages are responsible for providing similar documentation for their own operations.
