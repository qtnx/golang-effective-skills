---
source_name: "External Linked Documentation"
source_url: "https://research.swtch.com/godata"
source_path: "sources/raw/external/research-swtch-com-godata-4c4e9825fb.html"
license_ref: ""
---

# Go Data Structures   Russ Cox

## Structs and pointers

Now things start to pick up. The variable `bytes` has type `[5]byte`, an array of 5 `byte`s. Its memory representation is just those 5 bytes, one after the other, like a C array. Similarly, `primes` is an array of 4 `int`s.

Go, like C but unlike Java, gives the programmer control over what is and is not a pointer. For example, this type definition:

```go
type Point struct { X, Y int }

```

 defines a simple struct type named `Point`, represented as two adjacent `int`s in memory.

The composite literal syntax <http://golang.org/doc/go_spec.html#Composite_literals> `Point{10, 20}` denotes an initialized `Point`. Taking the address of a composite literal denotes a pointer to a freshly allocated and initialized `Point`. The former is two words in memory; the latter is a pointer to two words in memory.

Fields in a struct are laid out side by side in memory.

```go
type Rect1 struct { Min, Max Point }
type Rect2 struct { Min, Max *Point }
```

`Rect1`, a struct with two `Point` fields, is represented by two `Point`s—four ints—in a row. `Rect2`, a struct with two `*Point` fields, is represented by two `*Point`s.

Programmers who have used C probably won't be surprised by the distinction between `Point` fields and `*Point` fields, while programmers who have only used Java or Python (or ...) may be surprised by having to make the decision. By giving the programmer control over basic memory layout, Go provides the ability to control the total size of a given collection of data structures, the number of allocations, and the memory access patterns, all of which are important for building systems that perform well.
