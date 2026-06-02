---
source_name: "Google Go Style Guide"
source_url: "https://google.github.io/styleguide/go/"
source_path: "sources/raw/google-go-styleguide/best-practices.md"
license_ref: "sources/licenses/google-styleguide-LICENSE.txt"
---

# Go Style Best Practices

## Variable declarations

<a id="vardeclinitialization"></a>

### Initialization

For consistency, prefer `:=` over `var` when initializing a new variable with a
non-zero value.

```go
// Good:
i := 42
```

```go
// Bad:
var i = 42
```

<a id="vardeclzero"></a>

### Declaring variables with zero values

The following declarations use the [zero value]:

```go
// Good:
var (
    coords Point
    magic  [4]byte
    primes []int
)
```

[zero value]: https://golang.org/ref/spec#The_zero_value

You should declare values using the zero value when you want to convey an empty
value that **is ready for later use**. Using composite literals with explicit
initialization can be clunky:

```go
// Bad:
var (
    coords = Point{X: 0, Y: 0}
    magic  = [4]byte{0, 0, 0, 0}
    primes = []int(nil)
)
```

A common application of zero value declaration is when using a variable as the
output when unmarshalling:

```go
// Good:
var coords Point
if err := json.Unmarshal(data, &coords); err != nil {
```

It is also okay to use the zero value in the following form when you need a
variable of a pointer type:

```go
// Good:
msg := new(pb.Bar) // or "&pb.Bar{}"
if err := proto.Unmarshal(data, msg); err != nil {
```

If you need a lock or other field that [must not be copied](decisions#copying)
in your struct, you can make it a value type to take advantage of zero value
initialization. It does mean that the containing type must now be passed via a
pointer and not a value. Methods on the type must take pointer receivers.

```go
// Good:
type Counter struct {
    // This field does not have to be "*sync.Mutex". However,
    // users must now pass *Counter objects between themselves, not Counter.
    mu   sync.Mutex
    data map[string]int64
}

// Note this must be a pointer receiver to prevent copying.
func (c *Counter) IncrementBy(name string, n int64)
```

It's acceptable to use value types for local variables of composites (such as
structs and arrays) even if they contain such uncopyable fields. However, if the
composite is returned by the function, or if all accesses to it end up needing
to take an address anyway, prefer declaring the variable as a pointer type at
the outset. Similarly, protobuf messages should be declared as pointer types.

```go
// Good:
func NewCounter(name string) *Counter {
    c := new(Counter) // "&Counter{}" is also fine.
    registerCounter(name, c)
    return c
}

var msg = new(pb.Bar) // or "&pb.Bar{}".
```

This is because `*pb.Something` satisfies [`proto.Message`] while `pb.Something`
does not.

```go
// Bad:
func NewCounter(name string) *Counter {
    var c Counter
    registerCounter(name, &c)
    return &c
}

var msg = pb.Bar{}
```

[`proto.Message`]: https://pkg.go.dev/google.golang.org/protobuf/proto#Message

> **Important:** Map types must be explicitly initialized before they can be
> modified. However, reading from zero-value maps is perfectly fine.
>
> For map and slice types, if the code is particularly performance sensitive and
> if you know the sizes in advance, see the [size hints](#vardeclsize) section.

<a id="vardeclcomposite"></a>

### Composite literals

The following are [composite literal] declarations:

```go
// Good:
var (
    coords   = Point{X: x, Y: y}
    magic    = [4]byte{'I', 'W', 'A', 'D'}
    primes   = []int{2, 3, 5, 7, 11}
    captains = map[string]string{"Kirk": "James Tiberius", "Picard": "Jean-Luc"}
)
```

You should declare a value using a composite literal when you know initial
elements or members.

In contrast, using composite literals to declare empty or memberless values can
be visually noisy compared to [zero-value initialization](#vardeclzero).

When you need a pointer to a zero value, you have two options: empty composite
literals and `new`. Both are fine, but the `new` keyword can serve to remind the
reader that if a non-zero value were needed, a composite literal wouldn't work:

```go
// Good:
var (
  buf = new(bytes.Buffer) // non-empty Buffers are initialized with constructors.
  msg = new(pb.Message) // non-empty proto messages are initialized with builders or by setting fields one by one.
)
```

[composite literal]: https://golang.org/ref/spec#Composite_literals

<a id="vardeclsize"></a>

### Size hints

The following are declarations that take advantage of size hints in order to
preallocate capacity:

```go
// Good:
var (
    // Preferred buffer size for target filesystem: st_blksize.
    buf = make([]byte, 131072)
    // Typically process up to 8-10 elements per run (16 is a safe assumption).
    q = make([]Node, 0, 16)
    // Each shard processes shardSize (typically 32000+) elements.
    seen = make(map[string]bool, shardSize)
)
```

Size hints and preallocation are important steps **when combined with empirical
analysis of the code and its integrations**, to create performance-sensitive and
resource-efficient code.

Most code does not need a size hint or preallocation, and can allow the runtime
to grow the slice or map as necessary. It is acceptable to preallocate when the
final size is known (e.g. when converting between a map and a slice) but this is
not a readability requirement, and may not be worth the clutter in small cases.

**Warning:** Preallocating more memory than you need can waste memory in the
fleet or even harm performance. When in doubt, see
[GoTip #3: Benchmarking Go Code] and default to a
[zero initialization](#vardeclzero) or a
[composite literal declaration](#vardeclcomposite).

[GoTip #3: Benchmarking Go Code]: https://google.github.io/styleguide/go/index.html#gotip

<a id="decl-chan"></a>

### Channel direction

Specify [channel direction] where possible.

```go
// Good:
// sum computes the sum of all of the values. It reads from the channel until
// the channel is closed.
func sum(values <-chan int) int {
    // ...
}
```

This prevents casual programming errors that are possible without specification:

```go
// Bad:
func sum(values chan int) (out int) {
    for v := range values {
        out += v
    }
    // values must already be closed for this code to be reachable, which means
    // a second close triggers a panic.
    close(values)
}
```

When the direction is specified, the compiler catches simple errors like this.
It also helps to convey a measure of ownership to the type.

See also Bryan Mills' talk "Rethinking Classical Concurrency Patterns":
[slides][rethinking-concurrency-slides] [video][rethinking-concurrency-video].

[rethinking-concurrency-slides]: https://drive.google.com/file/d/1nPdvhB0PutEJzdCq5ms6UI58dp50fcAN/view?usp=sharing
[rethinking-concurrency-video]: https://www.youtube.com/watch?v=5zXAHh5tJqQ
[channel direction]: https://go.dev/ref/spec#Channel_types

<a id="funcargs"></a>
