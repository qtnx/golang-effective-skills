---
source_name: "External Linked Documentation"
source_url: "https://research.swtch.com/interfaces"
source_path: "sources/raw/external/research-swtch-com-interfaces-8664b07867.html"
license_ref: ""
---

### Interface Values

Languages with methods typically fall into one of two camps: prepare tables for all the method calls statically (as in C++ and Java), or do a method lookup at each call (as in Smalltalk and its many imitators, JavaScript and Python included) and add fancy caching to make that call efficient. Go sits halfway between the two: it has method tables but computes them at run time. I don't know whether Go is the first language to use this technique, but it's certainly not a common one. (I'd be interested to hear about earlier examples; leave a comment below.)

 As a warmup, a value of type `Binary` is just a 64-bit integer made up of two 32-bit words (like in the last post <http://research.swtch.com/2009/11/go-data-structures.html>, we'll assume a 32-bit machine; this time memory grows down instead of to the right):

Interface values are represented as a two-word pair giving a pointer to information about the type stored in the interface and a pointer to the associated data. Assigning `b` to an interface value of type `Stringer` sets both words of the interface value.

 (The pointers contained in the interface value are gray to emphasize that they are implicit, not directly exposed to Go programs.)

The first word in the interface value points at what I call an interface table or itable (pronounced i-table; in the runtime sources <http://golang.org/src/pkg/runtime/iface.c#L23>, the C implementation name is `Itab`). The itable begins with some metadata about the types involved and then becomes a list of function pointers. Note that the itable corresponds to the _interface type_, not the dynamic type. In terms of our example, the itable for `Stringer` holding type `Binary` lists the methods used to satisfy `Stringer`, which is just `String`: `Binary`'s other methods (`Get`) make no appearance in the itable.

The second word in the interface value points at the actual data, in this case a copy of `b`. The assignment `var s Stringer = b` makes a copy of `b` rather than point at `b` for the same reason that `var c uint64 = b` makes a copy: if `b` later changes, `s` and `c` are supposed to have the original value, not the new one. Values stored in interfaces might be arbitrarily large, but only one word is dedicated to holding the value in the interface structure, so the assignment allocates a chunk of memory on the heap and records the pointer in the one-word slot. (There's an obvious optimization when the value does fit in the slot; we'll get to that later.)

To check whether an interface value holds a particular type, as in the type switch above, the Go compiler generates code equivalent to the C expression `s.tab->type` to obtain the type pointer and check it against the desired type. If the types match, the value can be copied by by dereferencing `s.data`.

To call `s.String()`, the Go compiler generates code that does the equivalent of the C expression `s.tab->fun[0](s.data)`: it calls the appropriate function pointer from the itable, passing the interface value's data word as the function's first (in this example, only) argument. You can see this code if you run `8g -S x.go` (details at the bottom of this post). Note that the function in the itable is being passed the 32-bit pointer from the second word of the interface value, not the 64-bit value it points at. In general, the interface call site doesn't know the meaning of this word nor how much data it points at. Instead, the interface code arranges that the function pointers in the itable expect the 32-bit representation stored in the interface values. Thus the function pointer in this example is `(*Binary).String` not `Binary.String`.

The example we're considering is an interface with just one method. An interface with more methods would have more entries in the _fun_ list at the bottom of the itable.
