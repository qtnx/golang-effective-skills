---
source_name: "External Linked Documentation"
source_url: "https://go.dev/ref/spec"
source_path: "sources/raw/external/go-dev-ref-spec-3c5b020879.html"
license_ref: ""
---

## Built-in functions

### Clear

 The built-in function `clear` takes an argument of map, slice, or type parameter type, and deletes or zeroes out all elements [Go 1.21].

```go

Call        Argument type     Result

clear(m)    map[K]T           deletes all entries, resulting in an
                              empty map (len(m) == 0)

clear(s)    []T               sets all elements up to the length of
                              s to the zero value of T

clear(t)    type parameter    see below

```

 If the type of the argument to `clear` is a type parameter, all types in its type set must be maps or slices, and `clear` performs the operation corresponding to the actual type argument.

 If the map or slice is `nil`, `clear` is a no-op.

## Built-in functions

### Close

 For a channel `ch`, the built-in function `close(ch)` records that no more values will be sent on the channel. It is an error if `ch` is a receive-only channel. Sending to or closing a closed channel causes a run-time panic. Closing the nil channel also causes a run-time panic. After calling `close`, and after any previously sent values have been received, receive operations will return the zero value for the channel's type without blocking. The multi-valued receive operation returns a received value along with an indication of whether the channel is closed.

 If the type of the argument to `close` is a type parameter, all types in its type set must be channels. It is an error if any of those channels is a receive-only channel.
