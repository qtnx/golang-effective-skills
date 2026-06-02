---
source_name: "External Linked Documentation"
source_url: "https://research.swtch.com/godata"
source_path: "sources/raw/external/research-swtch-com-godata-4c4e9825fb.html"
license_ref: ""
---

# Go Data Structures   Russ Cox

## New and Make

Go has two data structure creation functions: `new` and `make`. The distinction is a common early point of confusion but seems to quickly become natural. The basic distinction is that `new(T)` returns a `*T`, a pointer that Go programs can dereference implicitly (the black pointers in the diagrams), while `make(T, `_args_`)` returns an ordinary `T`, not a pointer. Often that `T` has inside it some implicit pointers (the gray pointers in the diagrams). `New` returns a pointer to zeroed memory, while `make` returns a complex structure.

There is a way to unify these two, but it would be a significant break from the C and C++ tradition: define `make(*T)` to return a pointer to a newly allocated `T`, so that the current `new(Point)` would be written `make(*Point)`. We tried this for a few days but decided it was too different from what people expected of an allocation function.
