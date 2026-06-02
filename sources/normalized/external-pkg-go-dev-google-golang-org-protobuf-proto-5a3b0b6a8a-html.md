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

## Links

-    Open Source Insights  <https://deps.dev/go/google.golang.org%2Fprotobuf/v1.36.11>

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

This example hard-codes a duration of 125ns for the illustration of struct fields, but note that you do not need to fill the fields of well-known types like duration.proto yourself. To convert a time.Duration, use google.golang.org/protobuf/types/known/durationpb.New.

```go

package main

import (
	"fmt"

	"google.golang.org/protobuf/proto"
	"google.golang.org/protobuf/types/known/durationpb"
)

func main() {
	b, err := proto.Marshal(&durationpb.Duration{
		Nanos: 125,
	})
	if err != nil {
		panic(err)
	}

	fmt.Printf("125ns encoded into %d bytes of Protobuf wire format:\n% x\n", len(b), b)

	// You can use protoscope to explore the wire format:
	// https://github.com/protocolbuffers/protoscope
	//
	// echo -n '10 7d' | xxd -r -ps | protoscope
	// 2: 125

}

```

```go
Output:
125ns encoded into 2 bytes of Protobuf wire format:
10 7d

```

 Share Format Run

```go
func Merge(dst, src Message)
```

Merge merges src into dst, which must be a message with the same descriptor.

Populated scalar fields in src are copied to dst, while populated singular messages in src are merged into dst by recursively calling Merge. The elements of every list field in src is appended to the corresponded list fields in dst. The entries of every map field in src is copied into the corresponding map field in dst, possibly replacing existing entries. The unknown fields of src are appended to the unknown fields of dst.

It is semantically equivalent to unmarshaling the encoded form of src into dst with the [UnmarshalOptions.Merge] option specified.

```go
func MessageName(m Message) protoreflect.FullName
```

MessageName returns the full name of m. If m is nil, it returns an empty string.

```go
func RangeExtensions(m Message, f func(protoreflect.ExtensionType, any) bool)
```

RangeExtensions iterates over every populated extension field in m in an undefined order, calling f for each extension type and value encountered. It returns immediately if f returns false. While iterating, mutating operations may only be performed on the current extension field.

```go
func Reset(m Message)
```

Reset clears every field in the message. The resulting message shares no observable memory with its previous state other than the memory for the message itself.

```go
func SetExtension(m Message, xt protoreflect.ExtensionType, v any)
```

SetExtension stores the value of an extension field. It panics if m is invalid, xt does not extend m, or if type of v is invalid for the specified extension field.

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

If a generated extension descriptor variable is directly passed to SetExtension (e.g., foopb.E_MyExtension), then the value should be a concrete type that matches the expected Go type for the extension descriptor so that static analysis tools can verify type correctness. This also enables a possible future migration to a type-safe extension API.

```go

package main

import (
	"fmt"

	"google.golang.org/protobuf/proto"

	extpb "google.golang.org/protobuf/internal/testprotos/examples/ext"
)

func main() {
	concert := extpb.Concert_builder{
		HeadlinerName: proto.String("Go Protobuf Acapella Band"),
	}.Build()
	fmt.Printf("Has PromoId? %v\n", proto.HasExtension(concert, extpb.E_PromoId))
	proto.SetExtension(concert, extpb.E_PromoId, int32(2342))
	fmt.Printf("Has PromoId? %v\n", proto.HasExtension(concert, extpb.E_PromoId))
}

```

```go
Output:
Has PromoId? false
Has PromoId? true

```

 Share Format Run

```go
func Size(m Message) int
```

Size returns the size in bytes of the wire-format encoding of m.

Note that Size might return more bytes than Marshal will write in the case of lazily decoded messages that arrive in non-minimal wire format: see https://protobuf.dev/reference/go/size/ <https://protobuf.dev/reference/go/size/> for more details.

Checking if Size returns 0 is an easy way to recognize empty messages:

```go

package main

import (
	"google.golang.org/protobuf/proto"
)

func main() {
	var m proto.Message
	if proto.Size(m) == 0 {
		// No fields set (or, in proto3, all fields matching the default);
		// skip processing this message, or return an error, or similar.
	}
}

```

```go
Output:

```

 Share Format Run

```go
func String(v string) *string
```

String stores v in a new string value and returns a pointer to it.

```go
func Uint32(v uint32) *uint32
```

Uint32 stores v in a new uint32 value and returns a pointer to it.

```go
func Uint64(v uint64) *uint64
```

Uint64 stores v in a new uint64 value and returns a pointer to it.

```go
func Unmarshal(b []byte, m Message) error
```

Unmarshal parses the wire-format message in b and places the result in m. The provided message must be mutable (e.g., a non-nil pointer to a message).

See the UnmarshalOptions type if you need more control.

This example illustrates how to unmarshal (decode) wire format encoding into a Protobuf message.

```go

package main

import (
	"fmt"

	"google.golang.org/protobuf/proto"
	"google.golang.org/protobuf/types/known/durationpb"
)

func main() {
	// This is the wire format encoding produced by the Marshal example.
	// Typically you would read from the network, from disk, etc.
	b := []byte{0x10, 0x7d}

	var dur durationpb.Duration
	if err := proto.Unmarshal(b, &dur); err != nil {
		panic(err)
	}

	fmt.Printf("Protobuf wire format decoded to duration %v\n", dur.AsDuration())

}

```

```go
Output:
Protobuf wire format decoded to duration 125ns

```

 Share Format Run

```go
func ValueOrDefault[T interface {
	*P
	Message
}, P any](val T) T
```

ValueOrDefault returns the protobuf message val if val is not nil, otherwise it returns a pointer to an empty val message.

This function allows for translating code from the old Open Struct API to the new Opaque API.

The old Open Struct API represented oneof fields with a wrapper struct:

```go
var signedImg *accountpb.SignedImage
profile := &accountpb.Profile{
	// The Avatar oneof will be set, with an empty SignedImage.
	Avatar: &accountpb.Profile_SignedImage{signedImg},
}

```

The new Opaque API treats oneof fields like regular fields, there are no more wrapper structs:

```go
var signedImg *accountpb.SignedImage
profile := &accountpb.Profile{}
profile.SetSignedImage(signedImg)

```

For convenience, the Opaque API also offers Builders, which allow for a direct translation of struct initialization. However, because Builders use nilness to represent field presence (but there is no non-nil wrapper struct anymore), Builders cannot distinguish between an unset oneof and a set oneof with nil message. The above code would need to be translated with help of the ValueOrDefault function to retain the same behavior:

```go
var signedImg *accountpb.SignedImage
return &accountpb.Profile_builder{
	SignedImage: proto.ValueOrDefault(signedImg),
}.Build()

```

```go
func ValueOrDefaultBytes(val []byte) []byte
```

ValueOrDefaultBytes is like ValueOrDefault but for working with fields of type []byte.

```go
func ValueOrNil[T any](has bool, getter func() T) *T
```

ValueOrNil returns nil if has is false, or a pointer to a new variable containing the value returned by the specified getter.

This function is similar to the wrappers (proto.Int32(), proto.String(), etc.), but is generic (works for any field type) and works with the hasser and getter of a field, as opposed to a value.

This is convenient when populating builder fields.

Example:

```go
hop := attr.GetDirectHop()
injectedRoute := ripb.InjectedRoute_builder{
  Prefixes: route.GetPrefixes(),
  NextHop:  proto.ValueOrNil(hop.HasAddress(), hop.GetAddress),
}

```

```go
type MarshalOptions struct {
	pragma.NoUnkeyedLiterals

	// AllowPartial allows messages that have missing required fields to marshal
	// without returning an error. If AllowPartial is false (the default),
	// Marshal will return an error if there are any missing required fields.
	AllowPartial bool

	// Deterministic controls whether the same message will always be
	// serialized to the same bytes within the same binary.
	//
	// Setting this option guarantees that repeated serialization of
	// the same message will return the same bytes, and that different
	// processes of the same binary (which may be executing on different
	// machines) will serialize equal messages to the same bytes.
	// It has no effect on the resulting size of the encoded message compared
	// to a non-deterministic marshal.
	//
	// Note that the deterministic serialization is NOT canonical across
	// languages. It is not guaranteed to remain stable over time. It is
	// unstable across different builds with schema changes due to unknown
	// fields. Users who need canonical serialization (e.g., persistent
	// storage in a canonical form, fingerprinting, etc.) must define
	// their own canonicalization specification and implement their own
	// serializer rather than relying on this API.
	//
	// If deterministic serialization is requested, map entries will be
	// sorted by keys in lexographical order. This is an implementation
	// detail and subject to change.
	Deterministic bool

	// UseCachedSize indicates that the result of a previous Size call
	// may be reused.
	//
	// Setting this option asserts that:
	//
	// 1. Size has previously been called on this message with identical
	// options (except for UseCachedSize itself).
	//
	// 2. The message and all its submessages have not changed in any
	// way since the Size call. For lazily decoded messages, accessing
	// a message results in decoding the message, which is a change.
	//
	// If either of these invariants is violated,
	// the results are undefined and may include panics or corrupted output.
	//
	// Implementations MAY take this option into account to provide
	// better performance, but there is no guarantee that they will do so.
	// There is absolutely no guarantee that Size followed by Marshal with
	// UseCachedSize set will perform equivalently to Marshal alone.
	UseCachedSize bool
}
```

MarshalOptions configures the marshaler.

Example usage:

```go
b, err := MarshalOptions{Deterministic: true}.Marshal(m)

```

```go
func (o MarshalOptions) Marshal(m Message) ([]byte, error)
```

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
