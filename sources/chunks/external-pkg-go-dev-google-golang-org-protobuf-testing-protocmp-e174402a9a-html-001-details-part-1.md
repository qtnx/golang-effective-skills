---
source_name: "External Linked Documentation"
source_url: "https://pkg.go.dev/google.golang.org/protobuf/testing/protocmp"
source_path: "sources/raw/external/pkg-go-dev-google-golang-org-protobuf-testing-protocmp-e174402a9a.html"
license_ref: ""
---

protocmp package - google.golang.org/protobuf/testing/protocmp - Go Packages
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

Package protocmp provides protobuf specific options for the github.com/google/go-cmp/cmp package.

The primary feature is the Transform option, which transform proto.Message types into a Message map that is suitable for cmp to introspect upon. All other options in this package must be used in conjunction with Transform.

-  func FilterDescriptor(desc protoreflect.Descriptor, opt cmp.Option) cmp.Option
-  func FilterEnum(enum protoreflect.Enum, opt cmp.Option) cmp.Option
-  func FilterField(message proto.Message, name protoreflect.Name, opt cmp.Option) cmp.Option
-  func FilterMessage(message proto.Message, opt cmp.Option) cmp.Option
-  func FilterOneof(message proto.Message, name protoreflect.Name, opt cmp.Option) cmp.Option
-  func IgnoreDefaultScalars() cmp.Option
-  func IgnoreDescriptors(descs ...protoreflect.Descriptor) cmp.Option
-  func IgnoreEmptyMessages() cmp.Option
-  func IgnoreEnums(enums ...protoreflect.Enum) cmp.Option
-  func IgnoreFields(message proto.Message, names ...protoreflect.Name) cmp.Option
-  func IgnoreMessages(messages ...proto.Message) cmp.Option
-  func IgnoreOneofs(message proto.Message, names ...protoreflect.Name) cmp.Option
-  func IgnoreUnknown() cmp.Option
-  func MessageTypeResolver(r protoregistry.MessageTypeResolver) option
-  func SortRepeated(lessFunc any) cmp.Option
-  func SortRepeatedFields(message proto.Message, names ...protoreflect.Name) cmp.Option
-  func Transform(opts ...option) cmp.Option
-  type Enum
-
-  func (e Enum) Descriptor() protoreflect.EnumDescriptor
-  func (e1 Enum) Equal(e2 Enum) bool
-  func (e Enum) Number() protoreflect.EnumNumber
-  func (e Enum) String() string

-  type Message
-
-  func (m Message) Descriptor() protoreflect.MessageDescriptor
-  func (m Message) ProtoMessage()
-  func (m Message) ProtoReflect() protoreflect.Message
-  func (m Message) Reset()
-  func (m Message) String() string
-  func (m Message) Unwrap() proto.Message

This section is empty.

This section is empty.

```go
func FilterDescriptor(desc protoreflect.Descriptor, opt cmp.Option) cmp.Option
```

FilterDescriptor ignores the specified descriptor.

The following descriptor types may be specified:

- protoreflect.EnumDescriptor
- protoreflect.MessageDescriptor
- protoreflect.FieldDescriptor
- protoreflect.OneofDescriptor

For the behavior of each, see the corresponding filter function. Since this filter accepts a protoreflect.FieldDescriptor, it can be used to also filter for extension fields as a protoreflect.ExtensionDescriptor is just an alias to protoreflect.FieldDescriptor.

This must be used in conjunction with Transform.

```go
func FilterEnum(enum protoreflect.Enum, opt cmp.Option) cmp.Option
```

FilterEnum filters opt to only be applicable on a standalone Enum, singular fields of enums, list fields of enums, or map fields of enum values, where the enum is the same type as the specified enum.

The Go type of the last path step may be an:

- Enum for singular fields, elements of a repeated field, values of a map field, or standalone Enum values
- []Enum for list fields
- map[K]Enum for map fields
- any for a Message map entry value

This must be used in conjunction with Transform.

```go
func FilterField(message proto.Message, name protoreflect.Name, opt cmp.Option) cmp.Option
```

FilterField filters opt to only be applicable on the specified field in the message. It panics if a field of the given name does not exist.

The Go type of the last path step may be an:

- T for singular fields
- []T for list fields
- map[K]T for map fields
- any for a Message map entry value

This must be used in conjunction with Transform.

```go
func FilterMessage(message proto.Message, opt cmp.Option) cmp.Option
```

FilterMessage filters opt to only be applicable on a standalone Message values, singular fields of messages, list fields of messages, or map fields of message values, where the message is the same type as the specified message.

The Go type of the last path step may be an:

- Message for singular fields, elements of a repeated field, values of a map field, or standalone Message values
- []Message for list fields
- map[K]Message for map fields
- any for a Message map entry value

This must be used in conjunction with Transform.

```go
func FilterOneof(message proto.Message, name protoreflect.Name, opt cmp.Option) cmp.Option
```

FilterOneof filters opt to only be applicable on all fields within the specified oneof in the message. It panics if a oneof of the given name does not exist.

The Go type of the last path step may be an:

- T for singular fields
- []T for list fields
- map[K]T for map fields
- any for a Message map entry value

This must be used in conjunction with Transform.

```go
func IgnoreDefaultScalars() cmp.Option
```

IgnoreDefaultScalars ignores singular scalars that are unpopulated or explicitly set to the default value. This option does not effect elements in a list or entries in a map.

This must be used in conjunction with Transform.

```go
func IgnoreDescriptors(descs ...protoreflect.Descriptor) cmp.Option
```

IgnoreDescriptors ignores the specified set of descriptors. It is equivalent to FilterDescriptor(desc, cmp.Ignore()) for each descriptor.

This must be used in conjunction with Transform.

```go
func IgnoreEmptyMessages() cmp.Option
```

IgnoreEmptyMessages ignores messages that are empty or unpopulated. It applies to standalone Message values, singular message fields, list fields of messages, and map fields of message values.

This must be used in conjunction with Transform.

```go
func IgnoreEnums(enums ...protoreflect.Enum) cmp.Option
```

IgnoreEnums ignores all enums of the specified types. It is equivalent to FilterEnum(enum, cmp.Ignore()) for each enum.

This must be used in conjunction with Transform.

```go
func IgnoreFields(message proto.Message, names ...protoreflect.Name) cmp.Option
```

IgnoreFields ignores the specified fields in the specified message. It is equivalent to FilterField(message, name, cmp.Ignore()) for each field in the message.

This must be used in conjunction with Transform.

```go
func IgnoreMessages(messages ...proto.Message) cmp.Option
```

IgnoreMessages ignores all messages of the specified types. It is equivalent to FilterMessage(message, cmp.Ignore()) for each message.

This must be used in conjunction with Transform.

```go
func IgnoreOneofs(message proto.Message, names ...protoreflect.Name) cmp.Option
```

IgnoreOneofs ignores fields of the specified oneofs in the specified message. It is equivalent to FilterOneof(message, name, cmp.Ignore()) for each oneof in the message.

This must be used in conjunction with Transform.

```go
func IgnoreUnknown() cmp.Option
```

IgnoreUnknown ignores unknown fields in all messages.

This must be used in conjunction with Transform.

```go
func MessageTypeResolver(r protoregistry.MessageTypeResolver) option
```

MessageTypeResolver overrides the resolver used for messages packed inside Any. The default is protoregistry.GlobalTypes, which is sufficient for all compiled-in Protobuf messages. Overriding the resolver is useful in tests that dynamically create Protobuf descriptors and messages, e.g. in proxies using dynamicpb.

```go
func SortRepeated(lessFunc any) cmp.Option
```

SortRepeated sorts repeated fields of the specified element type. The less function must be of the form "func(T, T) bool" where T is the Go element type for the repeated field kind.

The element type T can be one of the following:

- Go type for a protobuf scalar kind except for an enum (i.e., bool, int32, int64, uint32, uint64, float32, float64, string, and []byte)
- E where E is a concrete enum type that implements protoreflect.Enum
- M where M is a concrete message type that implement proto.Message

This option only applies to repeated fields within a protobuf message. It does not operate on higher-order Go types that seem like a repeated field. For example, a []T outside the context of a protobuf message will not be handled by this option. To sort Go slices that are not repeated fields, consider using github.com/google/go-cmp/cmp/cmpopts.SortSlices instead.

The sorting of messages does not take into account ignored fields or oneofs as a result of IgnoreFields or IgnoreOneofs.

This must be used in conjunction with Transform.

```go
func SortRepeatedFields(message proto.Message, names ...protoreflect.Name) cmp.Option
```

SortRepeatedFields sorts the specified repeated fields. Sorting a repeated field is useful for treating the list as a multiset (i.e., a set where each value can appear multiple times). It panics if the field does not exist or is not a repeated field.

The sort ordering is as follows:

- Booleans are sorted where false is sorted before true.
- Integers are sorted in ascending order.
- Floating-point numbers are sorted in ascending order according to the total ordering defined by IEEE-754 (section 5.10).
- Strings and bytes are sorted lexicographically in ascending order.
- Enum values are sorted in ascending order based on its numeric value.
- Message values are sorted according to some arbitrary ordering which is undefined and may change in future implementations.

The ordering chosen for repeated messages is unlikely to be aesthetically preferred by humans. Consider using a custom sort function:

```go
FilterField(m, "foo_field", SortRepeated(func(x, y *foopb.MyMessage) bool {
    ... // user-provided definition for less
}))

```

The sorting of messages does not take into account ignored fields or oneofs as a result of IgnoreFields or IgnoreOneofs.

This must be used in conjunction with Transform.

```go
func Transform(opts ...option) cmp.Option
```

Transform returns a cmp.Option that converts each proto.Message to a Message. The transformation does not mutate nor alias any converted messages.

The google.protobuf.Any message is automatically unmarshaled such that the "value" field is a Message representing the underlying message value assuming it could be resolved and properly unmarshaled.

This does not directly transform higher-order composite Go types. For example, []*foopb.Message is not transformed into []Message, but rather the individual message elements of the slice are transformed.

```go
type Enum struct {
	// contains filtered or unexported fields
}
```

Enum is a dynamic representation of a protocol buffer enum that is suitable for cmp.Equal and cmp.Diff to compare upon.

```go
func (e Enum) Descriptor() protoreflect.EnumDescriptor
```

Descriptor returns the enum descriptor. It returns nil for a zero Enum value.

```go
func (e1 Enum) Equal(e2 Enum) bool
```

Equal reports whether e1 and e2 represent the same enum value.

```go
func (e Enum) Number() protoreflect.EnumNumber
```
