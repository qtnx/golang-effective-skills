---
source_name: "External Linked Documentation"
source_url: "https://go.dev/ref/spec"
source_path: "sources/raw/external/go-dev-ref-spec-3c5b020879.html"
license_ref: ""
---

## Types

### Channel types

 A channel provides a mechanism for concurrently executing functions to communicate by sending and receiving values of a specified element type. The value of an uninitialized channel is `nil`.

```go

ChannelType = ( "chan" | "chan" "<-" | "<-" "chan" ) ElementType .

```

 The optional `<-` operator specifies the channel _direction_, _send_ or _receive_. If a direction is given, the channel is _directional_, otherwise it is _bidirectional_. A channel may be constrained only to send or only to receive by assignment or explicit conversion.

```go

chan T          // can be used to send and receive values of type T
chan<- float64  // can only be used to send float64s
<-chan int      // can only be used to receive ints

```

 The `<-` operator associates with the leftmost `chan` possible:

```go

chan<- chan int    // same as chan<- (chan int)
chan<- <-chan int  // same as chan<- (<-chan int)
<-chan <-chan int  // same as <-chan (<-chan int)
chan (<-chan int)

```

 A new, initialized channel value can be made using the built-in function `make`, which takes the channel type and an optional _capacity_ as arguments:

```go

make(chan int, 100)

```

 The capacity, in number of elements, sets the size of the buffer in the channel. If the capacity is zero or absent, the channel is unbuffered and communication succeeds only when both a sender and receiver are ready. Otherwise, the channel is buffered and communication succeeds without blocking if the buffer is not full (sends) or not empty (receives). A `nil` channel is never ready for communication.

 A channel may be closed with the built-in function `close`. The multi-valued assignment form of the receive operator reports whether a received value was sent before the channel was closed.

 A single channel may be used in send statements, receive operations, and calls to the built-in functions `cap` and `len` by any number of goroutines without further synchronization. Channels act as first-in-first-out queues. For example, if one goroutine sends values on a channel and a second goroutine receives them, the values are received in the order sent.
