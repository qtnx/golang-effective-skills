---
source_name: "External Linked Documentation"
source_url: "https://go.dev/doc/faq"
source_path: "sources/raw/external/go-dev-doc-faq-c6a034d6a5.html"
license_ref: ""
---

## Design

### Why build concurrency on the ideas of CSP?

Concurrency and multi-threaded programming have over time developed a reputation for difficulty. We believe this is due partly to complex designs such as pthreads <https://en.wikipedia.org/wiki/POSIX_Threads> and partly to overemphasis on low-level details such as mutexes, condition variables, and memory barriers. Higher-level interfaces enable much simpler code, even if there are still mutexes and such under the covers.

One of the most successful models for providing high-level linguistic support for concurrency comes from Hoare’s Communicating Sequential Processes, or CSP. Occam and Erlang are two well known languages that stem from CSP. Go’s concurrency primitives derive from a different part of the family tree whose main contribution is the powerful notion of channels as first class objects. Experience with several earlier languages has shown that the CSP model fits well into a procedural language framework.
