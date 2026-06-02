---
source_name: "External Linked Documentation"
source_url: "https://research.swtch.com/interfaces"
source_path: "sources/raw/external/research-swtch-com-interfaces-8664b07867.html"
license_ref: ""
---

### Memory Optimizations

The space used by the implementation described above can be optimized in two complementary ways.

First, if the interface type involved is empty—it has no methods—then the itable serves no purpose except to hold the pointer to the original type. In this case, the itable can be dropped and the value can point at the type directly:

Whether an interface type has methods is a static property—either the type in the source code says `interface{}` or it says `interace{ methods... }`—so the compiler knows which representation is in use at each point in the program.

Second, if the value associated with the interface value can fit in a single machine word, there's no need to introduce the indirection or the heap allocation. If we define `Binary32` to be like `Binary` but implemented as a `uint32`, it could be stored in an interface value by keeping the actual value in the second word:

Whether the actual value is being pointed at or inlined depends on the size of the type. The compiler arranges for the functions listed in the type's method table (which get copied into the itables) to do the right thing with the word that gets passed in. If the receiver type fits in a word, it is used directly; if not, it is dereferenced. The diagrams show this: in the `Binary` version far above, the method in the itable is `(*Binary).String`, while in the `Binary32` example, the method in the itable is `Binary32.String` not `(*Binary32).String`.

Of course, empty interfaces holding word-sized (or smaller) values can take advantage of both optimizations:
