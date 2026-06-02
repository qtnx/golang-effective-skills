---
source_name: "External Linked Documentation"
source_url: "https://research.swtch.com/interfaces"
source_path: "sources/raw/external/research-swtch-com-interfaces-8664b07867.html"
license_ref: ""
---

### Method Lookup Performance

Smalltalk and the many dynamic systems that have followed it perform a method lookup every time a method gets called. For speed, many implementations use a simple one-entry cache at each call site, often in the instruction stream itself. In a multithreaded program, these caches must be managed carefully, since multiple threads could be at the same call site simultaneously. Even once the races have been avoided, the caches would end up being a source of memory contention.

Because Go has the hint of static typing to go along with the dynamic method lookups, it can move the lookups back from the call sites to the point when the value is stored in the interface. For example, consider this code snippet:

```go

1   var any interface{}  // initialized elsewhere
2   s := any.(Stringer)  // dynamic conversion
3   for i := 0; i < 100; i++ {
4       fmt.Println(s.String())
5   }

```

In Go, the itable gets computed (or found in a cache) during the assignment on line 2; the dispatch for the `s.String()` call executed on line 4 is a couple of memory fetches and a single indirect call instruction.

In contrast, the implementation of this program in a dynamic language like Smalltalk (or JavaScript, or Python, or ...) would do the method lookup at line 4, which in a loop repeats needless work. The cache mentioned earlier makes this less expensive than it might be, but it's still more expensive than a single indirect call instruction.

Of course, this being a blog post, I don't have any numbers to back up this discussion, but it certainly seems like the lack of memory contention would be a big win in a heavily parallel program, as is being able to move the method lookup out of tight loops. Also, I'm talking about the general architecture, not the specifics o the implementation: the latter probably has a few constant factor optimizations still available.
