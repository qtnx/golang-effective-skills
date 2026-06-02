---
source_name: "External Linked Documentation"
source_url: "https://go.dev/ref/spec"
source_path: "sources/raw/external/go-dev-ref-spec-3c5b020879.html"
license_ref: ""
---

## Expressions

### Receive operator

 For an operand `ch` of channel type, the value of the receive operation `<-ch` is the value received from the channel `ch`. The channel direction must permit receive operations, and the type of the receive operation is the element type of the channel. The expression blocks until a value is available. Receiving from a `nil` channel blocks forever. A receive operation on a closed channel can always proceed immediately, yielding the element type's zero value after any previously sent values have been received.

```go

v1 := <-ch
v2 = <-ch
f(<-ch)
<-strobe  // wait until clock pulse and discard received value

```

 If the operand type is a type parameter, all types in its type set must be channel types that permit receive operations, and they must all have the same element type, which is the type of the receive operation.

 A receive expression used in an assignment statement or initialization of the special form

```go

x, ok = <-ch
x, ok := <-ch
var x, ok = <-ch
var x, ok T = <-ch

```

 yields an additional untyped boolean result reporting whether the communication succeeded. The value of `ok` is `true` if the value received was delivered by a successful send operation to the channel, or `false` if it is a zero value generated because the channel is closed and empty.
