---
source_name: "External Linked Documentation"
source_url: "https://pkg.go.dev/encoding/gob"
source_path: "sources/raw/external/pkg-go-dev-encoding-gob-fa8ae5ca51.html"
license_ref: ""
---

-  type Encoder
-
-  func NewEncoder(w io.Writer) *Encoder

-
-  func (enc *Encoder) Encode(e any) error
-  func (enc *Encoder) EncodeValue(value reflect.Value) error

-  type GobDecoder
-  type GobEncoder

- Package (Basic)
- Package (EncodeDecode)
- Package (Interface)

This section is empty.

This section is empty.

```go
func Register(value any)
```

Register records a type, identified by a value for that type, under its internal type name. That name will identify the concrete type of a value sent or received as an interface variable. Only types that will be transferred as implementations of interface values need to be registered. Expecting to be used only during initialization, it panics if the mapping between types and names is not a bijection.

```go
func RegisterName(name string, value any)
```

RegisterName is like Register but uses the provided name rather than the type's default.

```go
type CommonType struct {
	Name string
	Id   typeId
}
```

CommonType holds elements of all types. It is a historical artifact, kept for binary compatibility and exported only for the benefit of the package's encoding of type descriptors. It is not intended for direct use by clients.

```go
type Decoder struct {
	// contains filtered or unexported fields
}
```

A Decoder manages the receipt of type and data information read from the remote side of a connection. It is safe for concurrent use by multiple goroutines.

The Decoder does only basic sanity checking on decoded input sizes, and its limits are not configurable. Take caution when decoding gob data from untrusted sources.

```go
func NewDecoder(r io.Reader) *Decoder
```

NewDecoder returns a new decoder that reads from the io.Reader. If r does not also implement io.ByteReader, it will be wrapped in a bufio.Reader.

```go
func (dec *Decoder) Decode(e any) error
```

Decode reads the next value from the input stream and stores it in the data represented by the empty interface value. If e is nil, the value will be discarded. Otherwise, the value underlying e must be a pointer to the correct type for the next data item received. If the input is at EOF, Decode returns io.EOF and does not modify e.

```go
func (dec *Decoder) DecodeValue(v reflect.Value) error
```

DecodeValue reads the next value from the input stream. If v is the zero reflect.Value (v.Kind() == Invalid), DecodeValue discards the value. Otherwise, it stores the value into v. In that case, v must represent a non-nil pointer to data or be an assignable reflect.Value (v.CanSet()) If the input is at EOF, DecodeValue returns io.EOF and does not modify v.

```go
type Encoder struct {
	// contains filtered or unexported fields
}
```

An Encoder manages the transmission of type and data information to the other side of a connection. It is safe for concurrent use by multiple goroutines.

```go
func NewEncoder(w io.Writer) *Encoder
```

NewEncoder returns a new encoder that will transmit on the io.Writer.

```go
func (enc *Encoder) Encode(e any) error
```

Encode transmits the data item represented by the empty interface value, guaranteeing that all necessary type information has been transmitted first. Passing a nil pointer to Encoder will panic, as they cannot be transmitted by gob.

```go
func (enc *Encoder) EncodeValue(value reflect.Value) error
```

EncodeValue transmits the data item represented by the reflection value, guaranteeing that all necessary type information has been transmitted first. Passing a nil pointer to EncodeValue will panic, as they cannot be transmitted by gob.

```go
type GobDecoder interface {
	// GobDecode overwrites the receiver, which must be a pointer,
	// with the value represented by the byte slice, which was written
	// by GobEncode, usually for the same concrete type.
	GobDecode([]byte) error
}
```

GobDecoder is the interface describing data that provides its own routine for decoding transmitted values sent by a GobEncoder.

```go
type GobEncoder interface {
	// GobEncode returns a byte slice representing the encoding of the
	// receiver for transmission to a GobDecoder, usually of the same
	// concrete type.
	GobEncode() ([]byte, error)
}
```

GobEncoder is the interface describing data that provides its own representation for encoding values for transmission to a GobDecoder. A type that implements GobEncoder and GobDecoder has complete control over the representation of its data and may therefore contain things such as private fields, channels, and functions, which are not usually transmissible in gob streams.

Note: Since gobs can be stored permanently, it is good design to guarantee the encoding used by a GobEncoder is stable as the software evolves. For instance, it might make sense for GobEncode to include a version number in the encoding.

##   Source Files ¶
 View all Source files <https://cs.opensource.google/go/go/+/go1.26.3:src/encoding/gob>

- dec_helpers.go <https://cs.opensource.google/go/go/+/go1.26.3:src/encoding/gob/dec_helpers.go>
- decode.go <https://cs.opensource.google/go/go/+/go1.26.3:src/encoding/gob/decode.go>
- decoder.go <https://cs.opensource.google/go/go/+/go1.26.3:src/encoding/gob/decoder.go>
- doc.go <https://cs.opensource.google/go/go/+/go1.26.3:src/encoding/gob/doc.go>
- enc_helpers.go <https://cs.opensource.google/go/go/+/go1.26.3:src/encoding/gob/enc_helpers.go>
- encode.go <https://cs.opensource.google/go/go/+/go1.26.3:src/encoding/gob/encode.go>
- encoder.go <https://cs.opensource.google/go/go/+/go1.26.3:src/encoding/gob/encoder.go>
- error.go <https://cs.opensource.google/go/go/+/go1.26.3:src/encoding/gob/error.go>
- type.go <https://cs.opensource.google/go/go/+/go1.26.3:src/encoding/gob/type.go>

Click to show internal directories.
  Click to hide internal directories.

Close

**?** : This menu   **/** : Search site   **f** or **F** : Jump to   **y** or **Y**  : Canonical URL
  Close
