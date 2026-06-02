---
source_name: "External Linked Documentation"
source_url: "https://research.swtch.com/interfaces"
source_path: "sources/raw/external/research-swtch-com-interfaces-8664b07867.html"
license_ref: ""
---

### Computing the Itable

Now we know what the itables look like, but where do they come from? Go's dynamic type conversions mean that it isn't reasonable for the compiler or linker to precompute all possible itables: there are too many (interface type, concrete type) pairs, and most won't be needed. Instead, the compiler generates a type description structure for each concrete type like `Binary` or `int` or `func(map[int]string)`. Among other metadata, the type description structure contains a list of the methods implemented by that type. Similarly, the compiler generates a (different) type description structure for each interface type like `Stringer`; it too contains a method list. The interface runtime computes the itable by looking for each method listed in the interface type's method table in the concrete type's method table. The runtime caches the itable after generating it, so that this correspondence need only be computed once.

In our simple example, the method table for `Stringer` has one method, while the table for `Binary` has two methods. In general there might be _ni_ methods for the interface type and _nt_ methods for the concrete type. The obvious search to find the mapping from interface methods to concrete methods would take _O_(_ni_ × _nt_) time, but we can do better. By sorting the two method tables and walking them simultaneously, we can build the mapping <http://code.google.com/p/go/source/browse/src/pkg/runtime/iface.c#98> in _O_(_ni_ + _nt_) time instead.
