---
source_name: "Google Go Style Guide"
source_url: "https://google.github.io/styleguide/go/"
source_path: "sources/raw/google-go-styleguide/decisions.md"
license_ref: "sources/licenses/google-styleguide-LICENSE.txt"
---

### Nil slices

For most purposes, there is no functional difference between `nil` and the empty
slice. Built-in functions like `len` and `cap` behave as expected on `nil`
slices.

```go
// Good:
import "fmt"

var s []int         // nil

fmt.Println(s)      // []
fmt.Println(len(s)) // 0
fmt.Println(cap(s)) // 0
for range s {...}   // no-op

s = append(s, 42)
fmt.Println(s)      // [42]
```

If you declare an empty slice as a local variable (especially if it can be the
source of a return value), prefer the nil initialization to reduce the risk of
bugs by callers.

```go
// Good:
var t []string
```

```go
// Bad:
t := []string{}
```

Do not create APIs that force their clients to make distinctions between nil and
the empty slice.

```go
// Good:
// Ping pings its targets.
// Returns hosts that successfully responded.
func Ping(hosts []string) ([]string, error) { ... }
```

```go
// Bad:
// Ping pings its targets and returns a list of hosts
// that successfully responded. Can be empty if the input was empty.
// nil signifies that a system error occurred.
func Ping(hosts []string) []string { ... }
```

When designing interfaces, avoid making a distinction between a `nil` slice and
a non-`nil`, zero-length slice, as this can lead to subtle programming errors.
This is typically accomplished by using `len` to check for emptiness, rather
than `== nil`.

This implementation accepts both `nil` and zero-length slices as "empty":

```go
// Good:
// describeInts describes s with the given prefix, unless s is empty.
func describeInts(prefix string, s []int) {
    if len(s) == 0 {
        return
    }
    fmt.Println(prefix, s)
}
```

Instead of relying on the distinction as a part of the API:

```go
// Bad:
func maybeInts() []int { /* ... */ }

// describeInts describes s with the given prefix; pass nil to skip completely.
func describeInts(prefix string, s []int) {
  // The behavior of this function unintentionally changes depending on what
  // maybeInts() returns in 'empty' cases (nil or []int{}).
  if s == nil {
    return
  }
  fmt.Println(prefix, s)
}

describeInts("Here are some ints:", maybeInts())
```

See [in-band errors] for further discussion.

[in-band errors]: #in-band-errors

<a id="indentation-confusion"></a>
