---
source_name: "External Linked Documentation"
source_url: "https://pkg.go.dev/google.golang.org/protobuf/proto"
source_path: "sources/raw/external/pkg-go-dev-google-golang-org-protobuf-proto-5a3b0b6a8a.html"
license_ref: ""
---

proto package - google.golang.org/protobuf/proto - Go Packages
## Details

-     Valid go.mod <https://github.com/protocolbuffers/protobuf-go/tree/v1.36.11/go.mod> file
 The Go module system was introduced in Go 1.11 and is the official dependency management solution for Go.

-     Redistributable license
 Redistributable licenses place minimal restrictions on how software can be used, modified, and redistributed.

-     Tagged version
Modules with tagged versions give importers more predictable builds.

-     Stable version
When a project reaches major version v1 it is considered stable.

-  Learn more about best practices

## Repository
   github.com/protocolbuffers/protobuf-go  <https://github.com/protocolbuffers/protobuf-go>

##   Documentation ¶

Package proto provides functions operating on protocol buffer messages.

For documentation on protocol buffers in general, see: https://protobuf.dev <https://protobuf.dev>.

For a tutorial on using protocol buffers with Go, see: https://protobuf.dev/getting-started/gotutorial <https://protobuf.dev/getting-started/gotutorial>.

For a guide to generated Go protocol buffer code, see: https://protobuf.dev/reference/go/go-generated <https://protobuf.dev/reference/go/go-generated>.

#### Binary serialization ¶

This package contains functions to convert to and from the wire format, an efficient binary serialization of protocol buffers.

-
Size reports the size of a message in the wire format.

-
Marshal converts a message to the wire format. The MarshalOptions type provides more control over wire marshaling.

-
Unmarshal converts a message from the wire format. The UnmarshalOptions type provides more control over wire unmarshaling.

#### Basic message operations ¶

-
Clone makes a deep copy of a message.

-
Merge merges the content of a message into another.

-
Equal compares two messages. For more control over comparisons and detailed reporting of differences, see package google.golang.org/protobuf/testing/protocmp.

-
Reset clears the content of a message.

-
CheckInitialized reports whether all required fields in a message are set.

#### Optional scalar constructors ¶

The API for some generated messages represents optional scalar fields as pointers to a value. For example, an optional string field has the Go type *string.

- Bool, Int32, Int64, Uint32, Uint64, Float32, Float64, and String take a value and return a pointer to a new instance of it, to simplify construction of optional field values.

Generated enum types usually have an Enum method which performs the same operation.

Optional scalar fields are only supported in proto2.

#### Extension accessors ¶

- HasExtension, GetExtension, SetExtension, and ClearExtension access extension field values in a protocol buffer message.

Extension fields are only supported in proto2.

#### Related packages ¶

-
Package google.golang.org/protobuf/encoding/protojson converts messages to and from JSON.

-
Package google.golang.org/protobuf/encoding/prototext converts messages to and from the text format.

-
Package google.golang.org/protobuf/reflect/protoreflect provides a reflection interface for protocol buffer data types.

-
Package google.golang.org/protobuf/testing/protocmp provides features to compare protocol buffer messages with the github.com/google/go-cmp/cmp package.

-
Package google.golang.org/protobuf/types/dynamicpb provides a dynamic message type, suitable for working with messages where the protocol buffer type is only known at runtime.

This module contains additional packages for more specialized use cases. Consult the individual package documentation for details.

- Variables
-  func Bool(v bool) *bool
-  func CheckInitialized(m Message) error
-  func ClearExtension(m Message, xt protoreflect.ExtensionType)
-  func CloneOf[M Message](m M) M
-  func Equal(x, y Message) bool
-  func Float32(v float32) *float32
-  func Float64(v float64) *float64
-  func GetExtension(m Message, xt protoreflect.ExtensionType) any
-  func HasExtension(m Message, xt protoreflect.ExtensionType) bool
-  func Int32(v int32) *int32
-  func Int64(v int64) *int64
-  func Marshal(m Message) ([]byte, error)
-  func Merge(dst, src Message)
-  func MessageName(m Message) protoreflect.FullName
-  func RangeExtensions(m Message, f func(protoreflect.ExtensionType, any) bool)
-  func Reset(m Message)
-  func SetExtension(m Message, xt protoreflect.ExtensionType, v any)
-  func Size(m Message) int
-  func String(v string) *string
-  func Uint32(v uint32) *uint32
-  func Uint64(v uint64) *uint64
-  func Unmarshal(b []byte, m Message) error
-  func ValueOrDefault[T interface{ ... }, P any](val T) T
-  func ValueOrDefaultBytes(val []byte) []byte
-  func ValueOrNil[T any](has bool, getter func() T) *T
-  type MarshalOptions
-
-  func (o MarshalOptions) Marshal(m Message) ([]byte, error)
-  func (o MarshalOptions) MarshalAppend(b []byte, m Message) ([]byte, error)
-  func (o MarshalOptions) MarshalState(in protoiface.MarshalInput) (protoiface.MarshalOutput, error)
-  func (o MarshalOptions) Size(m Message) int

-  type Message
-
-  func Clone(m Message) Message

-  type UnmarshalOptions
-
-  func (o UnmarshalOptions) Unmarshal(b []byte, m Message) error
-  func (o UnmarshalOptions) UnmarshalState(in protoiface.UnmarshalInput) (protoiface.UnmarshalOutput, error)

- GetExtension
- Marshal
- MarshalOptions.MarshalAppend (SameBuffer)
- SetExtension
- Size
- Unmarshal

This section is empty.

View Source <https://github.com/protocolbuffers/protobuf-go/blob/v1.36.11/proto/proto.go#L32>
```go
var Error error
```

Error matches all errors produced by packages in the protobuf module according to errors.Is.

Example usage:

```go
if errors.Is(err, proto.Error) { ... }

```

```go
func Bool(v bool) *bool
```

Bool stores v in a new bool value and returns a pointer to it.

```go
func CheckInitialized(m Message) error
```

CheckInitialized returns an error if any required fields in m are not set.

```go
func ClearExtension(m Message, xt protoreflect.ExtensionType)
```

ClearExtension clears an extension field such that subsequent HasExtension calls return false. It panics if m is invalid or if xt does not extend m.

```go
func CloneOf[M Message](m M) M
```

CloneOf returns a deep copy of m. If the top-level message is invalid, it returns an invalid message as well.

```go
func Equal(x, y Message) bool
```

Equal reports whether two messages are equal, by recursively comparing the fields of the message.

-
Bytes fields are equal if they contain identical bytes. Empty bytes (regardless of nil-ness) are considered equal.

-
Floating-point fields are equal if they contain the same value. Unlike the == operator, a NaN is equal to another NaN.

-
Other scalar fields are equal if they contain the same value.

-
Message fields are equal if they have the same set of populated known and extension field values, and the same set of unknown fields values.

-
Lists are equal if they are the same length and each corresponding element is equal.

-
Maps are equal if they have the same set of keys and the corresponding value for each key is equal.

An invalid message is not equal to a valid message. An invalid message is only equal to another invalid message of the same type. An invalid message often corresponds to a nil pointer of the concrete message type. For example, (*pb.M)(nil) is not equal to &pb.M{}. If two valid messages marshal to the same bytes under deterministic serialization, then Equal is guaranteed to report true.

```go
func Float32(v float32) *float32
```

Float32 stores v in a new float32 value and returns a pointer to it.

```go
func Float64(v float64) *float64
```

Float64 stores v in a new float64 value and returns a pointer to it.

```go
func GetExtension(m Message, xt protoreflect.ExtensionType) any
```

GetExtension retrieves the value for an extension field. If the field is unpopulated, it returns the default value for scalars and an immutable, empty value for lists or messages. It panics if xt does not extend m.

The type of the value is dependent on the field type of the extension. For extensions generated by protoc-gen-go, the Go type is as follows:

```go
╔═══════════════════╤═════════════════════════╗
║ Go type           │ Protobuf kind           ║
╠═══════════════════╪═════════════════════════╣
║ bool              │ bool                    ║
║ int32             │ int32, sint32, sfixed32 ║
║ int64             │ int64, sint64, sfixed64 ║
║ uint32            │ uint32, fixed32         ║
║ uint64            │ uint64, fixed64         ║
║ float32           │ float                   ║
║ float64           │ double                  ║
║ string            │ string                  ║
║ []byte            │ bytes                   ║
║ protoreflect.Enum │ enum                    ║
║ proto.Message     │ message, group          ║
╚═══════════════════╧═════════════════════════╝

```

The protoreflect.Enum and proto.Message types are the concrete Go type associated with the named enum or message. Repeated fields are represented using a Go slice of the base element type.

If a generated extension descriptor variable is directly passed to GetExtension, then the call should be followed immediately by a type assertion to the expected output value. For example:

```go
mm := proto.GetExtension(m, foopb.E_MyExtension).(*foopb.MyMessage)

```

This pattern enables static analysis tools to verify that the asserted type matches the Go type associated with the extension field and also enables a possible future migration to a type-safe extension API.

Since singular messages are the most common extension type, the pattern of calling HasExtension followed by GetExtension may be simplified to:

```go
if mm := proto.GetExtension(m, foopb.E_MyExtension).(*foopb.MyMessage); mm != nil {
    ... // make use of mm
}

```

The mm variable is non-nil if and only if HasExtension reports true.

```go

package main

import (
	"fmt"

"google.golang.org/protobuf/proto"

extpb "google.golang.org/protobuf/internal/testprotos/examples/ext"
)

func concertDetails() *extpb.Concert {
	concert := &extpb.Concert{}
	concert.SetHeadlinerName("Go Protobuf Acapella Band")
	proto.SetExtension(concert, extpb.E_PromoId, int32(2342))
	return concert
}

func main() {
	concert := concertDetails( /* req.ConcertID */ )
	fmt.Printf("finding backend server for live stream %q\n", concert.GetHeadlinerName())

if proto.HasExtension(concert, extpb.E_PromoId) {
		promoId := proto.GetExtension(concert, extpb.E_PromoId).(int32)
		fmt.Printf("routing stream to high-priority backend (concert is part of promo %v)\n", promoId)
	} else {
		fmt.Printf("routing stream to default backend\n")
	}

}

```

```go
Output:
finding backend server for live stream "Go Protobuf Acapella Band"
routing stream to high-priority backend (concert is part of promo 2342)

```

Share Format Run

```go
func HasExtension(m Message, xt protoreflect.ExtensionType) bool
```

HasExtension reports whether an extension field is populated. It returns false if m is invalid or if xt does not extend m.

```go
func Int32(v int32) *int32
```

Int32 stores v in a new int32 value and returns a pointer to it.

```go
func Int64(v int64) *int64
```

Int64 stores v in a new int64 value and returns a pointer to it.

```go
func Marshal(m Message) ([]byte, error)
```

Marshal returns the wire-format encoding of m.

This is the most common entry point for encoding a Protobuf message.

See the MarshalOptions type if you need more control.

This example illustrates how to marshal (encode) a Protobuf message struct literal into wire-format encoding.
