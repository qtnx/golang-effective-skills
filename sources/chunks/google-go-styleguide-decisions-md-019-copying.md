---
source_name: "Google Go Style Guide"
source_url: "https://google.github.io/styleguide/go/"
source_path: "sources/raw/google-go-styleguide/decisions.md"
license_ref: "sources/licenses/google-styleguide-LICENSE.txt"
---

## Language

### Copying

<a id="TOC-Copying"></a>

To avoid unexpected aliasing and similar bugs, be careful when copying a struct
from another package. For example, synchronization objects such as `sync.Mutex`
must not be copied.

The `bytes.Buffer` type contains a `[]byte` slice and, as an optimization for
small strings, a small byte array to which the slice may refer. If you copy a
`Buffer`, the slice in the copy may alias the array in the original, causing
subsequent method calls to have surprising effects.

In general, do not copy a value of type `T` if its methods are associated with
the pointer type, `*T`.

```go
// Bad:
b1 := bytes.Buffer{}
b2 := b1
```

Invoking a method that takes a value receiver can hide the copy. When you author
an API, you should generally take and return pointer types if your structs
contain fields that should not be copied.

These are acceptable:

```go
// Good:
type Record struct {
  buf bytes.Buffer
  // other fields omitted
}

func New() *Record {...}

func (r *Record) Process(...) {...}

func Consumer(r *Record) {...}
```

But these are usually wrong:

```go
// Bad:
type Record struct {
  buf bytes.Buffer
  // other fields omitted
}

func (r Record) Process(...) {...} // Makes a copy of r.buf

func Consumer(r Record) {...} // Makes a copy of r.buf
```

This guidance also applies to copying `sync.Mutex`.

<a id="dont-panic"></a>
