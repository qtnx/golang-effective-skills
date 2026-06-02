---
source_name: "Google Go Style Guide"
source_url: "https://google.github.io/styleguide/go/"
source_path: "sources/raw/google-go-styleguide/best-practices.html"
license_ref: "sources/licenses/google-styleguide-LICENSE.txt"
---

### Declaring variables with zero values

The following declarations use the zero value:

```go
// Good:
var (
    coords Point
    magic  [4]byte
    primes []int
)

```

You should declare values using the zero value when you want to convey an empty value that **is ready for later use**. Using composite literals with explicit initialization can be clunky:

```go
// Bad:
var (
    coords = Point{X: 0, Y: 0}
    magic  = [4]byte{0, 0, 0, 0}
    primes = []int(nil)
)

```

A common application of zero value declaration is when using a variable as the output when unmarshalling:

```go
// Good:
var coords Point
if err := json.Unmarshal(data, &coords); err != nil {

```

It is also okay to use the zero value in the following form when you need a variable of a pointer type:

```go
// Good:
msg := new(pb.Bar) // or "&pb.Bar{}"
if err := proto.Unmarshal(data, msg); err != nil {

```

If you need a lock or other field that must not be copied in your struct, you can make it a value type to take advantage of zero value initialization. It does mean that the containing type must now be passed via a pointer and not a value. Methods on the type must take pointer receivers.

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

It’s acceptable to use value types for local variables of composites (such as structs and arrays) even if they contain such uncopyable fields. However, if the composite is returned by the function, or if all accesses to it end up needing to take an address anyway, prefer declaring the variable as a pointer type at the outset. Similarly, protobuf messages should be declared as pointer types.

```go
// Good:
func NewCounter(name string) *Counter {
    c := new(Counter) // "&Counter{}" is also fine.
    registerCounter(name, c)
    return c
}

var msg = new(pb.Bar) // or "&pb.Bar{}".

```

This is because `*pb.Something` satisfies `proto.Message` while `pb.Something` does not.

```go
// Bad:
func NewCounter(name string) *Counter {
    var c Counter
    registerCounter(name, &c)
    return &c
}

var msg = pb.Bar{}

```

**Important:** Map types must be explicitly initialized before they can be modified. However, reading from zero-value maps is perfectly fine.

For map and slice types, if the code is particularly performance sensitive and if you know the sizes in advance, see the size hints section.
