---
source_name: "External Linked Documentation"
source_url: "https://pkg.go.dev/google.golang.org/protobuf/proto"
source_path: "sources/raw/external/pkg-go-dev-google-golang-org-protobuf-proto-5a3b0b6a8a.html"
license_ref: ""
---

Marshal returns the wire-format encoding of m.

```go
func (o MarshalOptions) MarshalAppend(b []byte, m Message) ([]byte, error)
```

MarshalAppend appends the wire-format encoding of m to b, returning the result.

This is a less common entry point than Marshal, which is only needed if you need to supply your own buffers for performance reasons.

This example illustrates how to marshal (encode) many Protobuf messages into wire-format encoding, using the same buffer.

MarshalAppend will grow the buffer as needed, so over time it will grow large enough to not need further allocations.

If unbounded growth of the buffer is undesirable in your application, you can use MarshalOptions.Size to determine a buffer size that is guaranteed to be large enough for marshaling without allocations.

```go

package main

import (
	"google.golang.org/protobuf/proto"
)

func main() {
	var m proto.Message

opts := proto.MarshalOptions{
		// set e.g. Deterministic: true, if needed
	}

var buf []byte
	for i := 0; i < 100000; i++ {
		var err error
		buf, err = opts.MarshalAppend(buf[:0], m)
		if err != nil {
			panic(err)
		}
		// cap(buf) will grow to hold the largest m.

// write buf to disk, network, etc.
	}
}

```

```go
Output:

```

Share Format Run

```go
func (o MarshalOptions) MarshalState(in protoiface.MarshalInput) (protoiface.MarshalOutput, error)
```

MarshalState returns the wire-format encoding of a message.

This method permits fine-grained control over the marshaler. Most users should use Marshal instead.

```go
func (o MarshalOptions) Size(m Message) int
```

Size returns the size in bytes of the wire-format encoding of m.

Note that Size might return more bytes than Marshal will write in the case of lazily decoded messages that arrive in non-minimal wire format: see https://protobuf.dev/reference/go/size/ <https://protobuf.dev/reference/go/size/> for more details.

```go
type Message = protoreflect.ProtoMessage
```

Message is the top-level interface that all messages must implement. It provides access to a reflective view of a message. Any implementation of this interface may be used with all functions in the protobuf module that accept a Message, except where otherwise specified.

This is the v2 interface definition for protobuf messages. The v1 interface definition is github.com/golang/protobuf/proto.Message.

- To convert a v1 message to a v2 message, use google.golang.org/protobuf/protoadapt.MessageV2Of.
- To convert a v2 message to a v1 message, use google.golang.org/protobuf/protoadapt.MessageV1Of.

```go
func Clone(m Message) Message
```

Clone returns a deep copy of m. If the top-level message is invalid, it returns an invalid message as well.

```go
type UnmarshalOptions struct {
	pragma.NoUnkeyedLiterals

// Merge merges the input into the destination message.
	// The default behavior is to always reset the message before unmarshaling,
	// unless Merge is specified.
	Merge bool

// AllowPartial accepts input for messages that will result in missing
	// required fields. If AllowPartial is false (the default), Unmarshal will
	// return an error if there are any missing required fields.
	AllowPartial bool

// If DiscardUnknown is set, unknown fields are ignored.
	DiscardUnknown bool

// Resolver is used for looking up types when unmarshaling extension fields.
	// If nil, this defaults to using protoregistry.GlobalTypes.
	Resolver interface {
		FindExtensionByName(field protoreflect.FullName) (protoreflect.ExtensionType, error)
		FindExtensionByNumber(message protoreflect.FullName, field protoreflect.FieldNumber) (protoreflect.ExtensionType, error)
	}

// RecursionLimit limits how deeply messages may be nested.
	// If zero, a default limit is applied.
	RecursionLimit int

//
	// NoLazyDecoding turns off lazy decoding, which otherwise is enabled by
	// default. Lazy decoding only affects submessages (annotated with [lazy =
	// true] in the .proto file) within messages that use the Opaque API.
	NoLazyDecoding bool
}
```

UnmarshalOptions configures the unmarshaler.

Example usage:

```go
err := UnmarshalOptions{DiscardUnknown: true}.Unmarshal(b, m)

```

```go
func (o UnmarshalOptions) Unmarshal(b []byte, m Message) error
```

Unmarshal parses the wire-format message in b and places the result in m. The provided message must be mutable (e.g., a non-nil pointer to a message).

```go
func (o UnmarshalOptions) UnmarshalState(in protoiface.UnmarshalInput) (protoiface.UnmarshalOutput, error)
```

UnmarshalState parses a wire-format message and places the result in m.

This method permits fine-grained control over the unmarshaler. Most users should use Unmarshal instead.

##   Source Files ¶
 View all Source files <https://github.com/protocolbuffers/protobuf-go/tree/v1.36.11/proto>

- checkinit.go <https://github.com/protocolbuffers/protobuf-go/blob/v1.36.11/proto/checkinit.go>
- decode.go <https://github.com/protocolbuffers/protobuf-go/blob/v1.36.11/proto/decode.go>
- decode_gen.go <https://github.com/protocolbuffers/protobuf-go/blob/v1.36.11/proto/decode_gen.go>
- doc.go <https://github.com/protocolbuffers/protobuf-go/blob/v1.36.11/proto/doc.go>
- encode.go <https://github.com/protocolbuffers/protobuf-go/blob/v1.36.11/proto/encode.go>
- encode_gen.go <https://github.com/protocolbuffers/protobuf-go/blob/v1.36.11/proto/encode_gen.go>
- equal.go <https://github.com/protocolbuffers/protobuf-go/blob/v1.36.11/proto/equal.go>
- extension.go <https://github.com/protocolbuffers/protobuf-go/blob/v1.36.11/proto/extension.go>
- merge.go <https://github.com/protocolbuffers/protobuf-go/blob/v1.36.11/proto/merge.go>
- messageset.go <https://github.com/protocolbuffers/protobuf-go/blob/v1.36.11/proto/messageset.go>
- proto.go <https://github.com/protocolbuffers/protobuf-go/blob/v1.36.11/proto/proto.go>
- proto_methods.go <https://github.com/protocolbuffers/protobuf-go/blob/v1.36.11/proto/proto_methods.go>
- reset.go <https://github.com/protocolbuffers/protobuf-go/blob/v1.36.11/proto/reset.go>
- size.go <https://github.com/protocolbuffers/protobuf-go/blob/v1.36.11/proto/size.go>
- size_gen.go <https://github.com/protocolbuffers/protobuf-go/blob/v1.36.11/proto/size_gen.go>
- wrapperopaque.go <https://github.com/protocolbuffers/protobuf-go/blob/v1.36.11/proto/wrapperopaque.go>
- wrappers.go <https://github.com/protocolbuffers/protobuf-go/blob/v1.36.11/proto/wrappers.go>

Click to show internal directories.
  Click to hide internal directories.

Close

**?** : This menu   **/** : Search site   **f** or **F** : Jump to   **y** or **Y**  : Canonical URL
  Close
