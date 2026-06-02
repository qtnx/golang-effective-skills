---
source_name: "External Linked Documentation"
source_url: "https://go.dev/ref/spec"
source_path: "sources/raw/external/go-dev-ref-spec-3c5b020879.html"
license_ref: ""
---

## Statements

### Send statements

 A send statement sends a value on a channel. The channel expression must be of channel type, the channel direction must permit send operations, and the type of the value to be sent must be assignable to the channel's element type.

```go

SendStmt = Channel "<-" Expression .
Channel  = Expression .

```

 Both the channel and the value expression are evaluated before communication begins. Communication blocks until the send can proceed. A send on an unbuffered channel can proceed if a receiver is ready. A send on a buffered channel can proceed if there is room in the buffer. A send on a closed channel proceeds by causing a run-time panic. A send on a `nil` channel blocks forever.

```go

ch <- 3  // send value 3 to channel ch

```

 If the type of the channel expression is a type parameter, all types in its type set must be channel types that permit send operations, they must all have the same element type, and the type of the value to be sent must be assignable to that element type.
