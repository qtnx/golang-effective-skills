---
source_name: "External Linked Documentation"
source_url: "https://pkg.go.dev/google.golang.org/protobuf/testing/protocmp"
source_path: "sources/raw/external/pkg-go-dev-google-golang-org-protobuf-testing-protocmp-e174402a9a.html"
license_ref: ""
---

Number returns the enum value as an integer.

```go
func (e Enum) String() string
```

String returns the name of the enum value if known (e.g., "ENUM_VALUE"), otherwise it returns the formatted decimal enum number (e.g., "14").

```go
type Message map[string]any
```

Message is a dynamic representation of a protocol buffer message that is suitable for cmp.Equal and cmp.Diff to directly operate upon.

Every populated known field (excluding extension fields) is stored in the map with the key being the short name of the field (e.g., "field_name") and the value determined by the kind and cardinality of the field.

Singular scalars are represented by the same Go type as protoreflect.Value, singular messages are represented by the Message type, singular enums are represented by the Enum type, list fields are represented as a Go slice, and map fields are represented as a Go map.

Every populated extension field is stored in the map with the key being the full name of the field surrounded by brackets (e.g., "[extension.full.name]") and the value determined according to the same rules as known fields.

Every unknown field is stored in the map with the key being the field number encoded as a decimal string (e.g., "132") and the value being the raw bytes of the encoded field (as the protoreflect.RawFields type).

Message values must not be created by or mutated by users.

```go
func (m Message) Descriptor() protoreflect.MessageDescriptor
```

Descriptor return the message descriptor. It returns nil for a zero Message value.

```go
func (m Message) ProtoMessage()
```

ProtoMessage is a marker method from the legacy message interface.

```go
func (m Message) ProtoReflect() protoreflect.Message
```

ProtoReflect returns a reflective view of m. It only implements the read-only operations of protoreflect.Message. Calling any mutating operations on m panics.

```go
func (m Message) Reset()
```

Reset is the required Reset method from the legacy message interface.

```go
func (m Message) String() string
```

String returns a formatted string for the message. It is intended for human debugging and has no guarantees about its exact format or the stability of its output.

```go
func (m Message) Unwrap() proto.Message
```

Unwrap returns the original message value. It returns nil if this Message was not constructed from another message.

##   Source Files ¶
 View all Source files <https://github.com/protocolbuffers/protobuf-go/tree/v1.36.11/testing/protocmp>

- reflect.go <https://github.com/protocolbuffers/protobuf-go/blob/v1.36.11/testing/protocmp/reflect.go>
- util.go <https://github.com/protocolbuffers/protobuf-go/blob/v1.36.11/testing/protocmp/util.go>
- xform.go <https://github.com/protocolbuffers/protobuf-go/blob/v1.36.11/testing/protocmp/xform.go>

Click to show internal directories.
  Click to hide internal directories.

Close

**?** : This menu   **/** : Search site   **f** or **F** : Jump to   **y** or **Y**  : Canonical URL
  Close
