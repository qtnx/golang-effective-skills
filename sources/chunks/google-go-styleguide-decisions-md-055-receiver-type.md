---
source_name: "Google Go Style Guide"
source_url: "https://google.github.io/styleguide/go/"
source_path: "sources/raw/google-go-styleguide/decisions.md"
license_ref: "sources/licenses/google-styleguide-LICENSE.txt"
---

### Receiver type

<a id="TOC-ReceiverType"></a>

A [method receiver] can be passed either as a value or a pointer, just as if it
were a regular function parameter. The choice between the two is based on which
[method set(s)] the method should be a part of.

[method receiver]: https://golang.org/ref/spec#Method_declarations
[method set(s)]: https://golang.org/ref/spec#Method_sets

**Correctness wins over speed or simplicity.** There are cases where you must
use a pointer value. In other cases, pick pointers for large types or as
future-proofing if you don't have a good sense of how the code will grow, and
use values for simple [plain old data].

The list below spells out each case in further detail:

*   If the receiver is a slice and the method doesn't reslice or reallocate the
    slice, use a value rather than a pointer.

    ```go
    // Good:
    type Buffer []byte

    func (b Buffer) Len() int { return len(b) }
    ```

*   If the method needs to mutate the receiver, the receiver must be a pointer.

    ```go
    // Good:
    type Counter int

    func (c *Counter) Inc() { *c++ }

    // See https://pkg.go.dev/container/heap.
    type Queue []Item

    func (q *Queue) Push(x Item) { *q = append([]Item{x}, *q...) }
    ```

*   If the receiver is a struct containing fields that
    [cannot safely be copied](#copying), use a pointer receiver. Common examples
    are [`sync.Mutex`] and other synchronization types.

    ```go
    // Good:
    type Counter struct {
        mu    sync.Mutex
        total int
    }

    func (c *Counter) Inc() {
        c.mu.Lock()
        defer c.mu.Unlock()
        c.total++
    }
    ```

    **Tip:** Check the type's [Godoc] for information about whether it is safe
    or unsafe to copy.

*   If the receiver is a "large" struct or array, a pointer receiver may be more
    efficient. Passing a struct is equivalent to passing all of its fields or
    elements as arguments to the method. If that seems too large to
    [pass by value](#pass-values), a pointer is a good choice.

*   For methods that will call or run concurrently with other functions that
    modify the receiver, use a value if those modifications should not be
    visible to your method; otherwise use a pointer.

*   If the receiver is a struct or array, any of whose elements is a pointer to
    something that may be mutated, prefer a pointer receiver to make the
    intention of mutability clear to the reader.

    ```go
    // Good:
    type Counter struct {
        m *Metric
    }

    func (c *Counter) Inc() {
        c.m.Add(1)
    }
    ```

*   If the receiver is a [built-in type], such as an integer or a string, that
    does not need to be modified, use a value.

    ```go
    // Good:
    type User string

    func (u User) String() { return string(u) }
    ```

*   If the receiver is a map, function, or channel, use a value rather than a
    pointer.

    ```go
    // Good:
    // See https://pkg.go.dev/net/http#Header.
    type Header map[string][]string

    func (h Header) Add(key, value string) { /* omitted */ }
    ```

*   If the receiver is a "small" array or struct that is naturally a value type
    with no mutable fields and no pointers, a value receiver is usually the
    right choice.

    ```go
    // Good:
    // See https://pkg.go.dev/time#Time.
    type Time struct { /* omitted */ }

    func (t Time) Add(d Duration) Time { /* omitted */ }
    ```

*   When in doubt, use a pointer receiver.

As a general guideline, prefer to make the methods for a type either all pointer
methods or all value methods.

**Note:** There is a lot of misinformation about whether passing a value or a
pointer to a function can affect performance. The compiler can choose to pass
pointers to values on the stack as well as copying values on the stack, but
these considerations should not outweigh the readability and correctness of the
code in most circumstances. When the performance does matter, it is important to
profile both approaches with a realistic benchmark before deciding that one
approach outperforms the other.

[plain old data]: https://en.wikipedia.org/wiki/Passive_data_structure
[`sync.Mutex`]: https://pkg.go.dev/sync#Mutex
[built-in type]: https://pkg.go.dev/builtin

<a id="switch-break"></a>
