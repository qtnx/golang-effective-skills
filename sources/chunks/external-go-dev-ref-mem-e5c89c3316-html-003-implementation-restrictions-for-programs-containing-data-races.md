---
source_name: "External Linked Documentation"
source_url: "https://go.dev/ref/mem"
source_path: "sources/raw/external/go-dev-ref-mem-e5c89c3316.html"
license_ref: ""
---

# The Go Memory Model

## Implementation Restrictions for Programs Containing Data Races

 The preceding section gave a formal definition of data-race-free program execution. This section informally describes the semantics that implementations must provide for programs that do contain races.

 Any implementation can, upon detecting a data race, report the race and halt execution of the program. Implementations using ThreadSanitizer (accessed with “`go` `build` `-race`”) do exactly this.

 A read of an array, struct, or complex number may be implemented as a read of each individual sub-value (array element, struct field, or real/imaginary component), in any order. Similarly, a write of an array, struct, or complex number may be implemented as a write of each individual sub-value, in any order.

 A read _r_ of a memory location _x_ holding a value that is not larger than a machine word must observe some write _w_ such that _r_ does not happen before _w_ and there is no write _w'_ such that _w_ happens before _w'_ and _w'_ happens before _r_. That is, each read must observe a value written by a preceding or concurrent write.

 Additionally, observation of acausal and “out of thin air” writes is disallowed.

 Reads of memory locations larger than a single machine word are encouraged but not required to meet the same semantics as word-sized memory locations, observing a single allowed write _w_. For performance reasons, implementations may instead treat larger operations as a set of individual machine-word-sized operations in an unspecified order. This means that races on multiword data structures can lead to inconsistent values not corresponding to a single write. When the values depend on the consistency of internal (pointer, length) or (pointer, type) pairs, as can be the case for interface values, maps, slices, and strings in most Go implementations, such races can in turn lead to arbitrary memory corruption.

 Examples of incorrect synchronization are given in the “Incorrect synchronization” section below.

 Examples of the limitations on implementations are given in the “Incorrect compilation” section below.
