---
source_name: "External Linked Documentation"
source_url: "https://pkg.go.dev/encoding/gob"
source_path: "sources/raw/external/pkg-go-dev-encoding-gob-fa8ae5ca51.html"
license_ref: ""
---

Interface types are not checked for compatibility; all interface types are treated, for transmission, as members of a single "interface" type, analogous to int or []byte - in effect they're all treated as interface{}. Interface values are transmitted as a string identifying the concrete type being sent (a name that must be pre-defined by calling Register), followed by a byte count of the length of the following data (so the value can be skipped if it cannot be stored), followed by the usual encoding of concrete (dynamic) value stored in the interface value. (A nil interface value is identified by the empty string and transmits no value.) Upon receipt, the decoder verifies that the unpacked concrete item satisfies the interface of the receiving variable.

If a value is passed to Encoder.Encode and the type is not a struct (or pointer to struct, etc.), for simplicity of processing it is represented as a struct of one field. The only visible effect of this is to encode a zero byte after the value, just as after the last field of an encoded struct, so that the decode algorithm knows when the top-level value is complete.

The representation of types is described below. When a type is defined on a given connection between an Encoder and Decoder, it is assigned a signed integer type id. When Encoder.Encode(v) is called, it makes sure there is an id assigned for the type of v and all its elements and then it sends the pair (typeid, encoded-v) where typeid is the type id of the encoded type of v and encoded-v is the gob encoding of the value v.

To define a type, the encoder chooses an unused, positive type id and sends the pair (-type id, encoded-type) where encoded-type is the gob encoding of a wireType description, constructed from these types:

```go
type wireType struct {
	ArrayT           *arrayType
	SliceT           *sliceType
	StructT          *structType
	MapT             *mapType
	GobEncoderT      *gobEncoderType
	BinaryMarshalerT *gobEncoderType
	TextMarshalerT   *gobEncoderType
}
type arrayType struct {
	CommonType
	Elem typeId
	Len  int
}
type CommonType struct {
	Name string // the name of the struct type
	Id  int    // the id of the type, repeated so it's inside the type
}
type sliceType struct {
	CommonType
	Elem typeId
}
type structType struct {
	CommonType
	Field []fieldType // the fields of the struct.
}
type fieldType struct {
	Name string // the name of the field.
	Id   int    // the type id of the field, which must be already defined
}
type mapType struct {
	CommonType
	Key  typeId
	Elem typeId
}
type gobEncoderType struct {
	CommonType
}

```

If there are nested type ids, the types for all inner type ids must be defined before the top-level type id is used to describe an encoded-v.

For simplicity in setup, the connection is defined to understand these types a priori, as well as the basic gob types int, uint, etc. Their ids are:

```go
bool        1
int         2
uint        3
float       4
[]byte      5
string      6
complex     7
interface   8
// gap for reserved ids.
WireType    16
ArrayType   17
CommonType  18
SliceType   19
StructType  20
FieldType   21
// 22 is slice of fieldType.
MapType     23

```

Finally, each message created by a call to Encode is preceded by an encoded unsigned integer count of the number of bytes remaining in the message. After the initial type name, interface values are wrapped the same way; in effect, the interface value acts like a recursive invocation of Encode.

In summary, a gob stream looks like

```go
(byteCount (-type id, encoding of a wireType)* (type id, encoding of a value))*

```

where * signifies zero or more repetitions and the type id of a value must be predefined or be defined before the value in the stream.

Compatibility: Any future changes to the package will endeavor to maintain compatibility with streams encoded using previous versions. That is, any released version of this package should be able to decode data written with any previously released version, subject to issues such as security fixes. See the Go compatibility document for background: https://golang.org/doc/go1compat <https://golang.org/doc/go1compat>

See "Gobs of data" for a design discussion of the gob wire format: https://go.dev/blog/gob <https://go.dev/blog/gob>

#### Security ¶

This package is not designed to be hardened against adversarial inputs, and is outside the scope of https://go.dev/security/policy <https://go.dev/security/policy>. In particular, the Decoder does only basic sanity checking on decoded input sizes, and its limits are not configurable. Care should be taken when decoding gob data from untrusted sources, which may consume significant resources.

This example shows the basic usage of the package: Create an encoder, transmit some values, receive them with a decoder.

```go

package main

import (
	"bytes"
	"encoding/gob"
	"fmt"
	"log"
)

type P struct {
	X, Y, Z int
	Name    string
}

type Q struct {
	X, Y *int32
	Name string
}

// This example shows the basic usage of the package: Create an encoder,
// transmit some values, receive them with a decoder.
func main() {
	// Initialize the encoder and decoder. Normally enc and dec would be
	// bound to network connections and the encoder and decoder would
	// run in different processes.
	var network bytes.Buffer        // Stand-in for a network connection
	enc := gob.NewEncoder(&network) // Will write to network.
	dec := gob.NewDecoder(&network) // Will read from network.

// Encode (send) some values.
	err := enc.Encode(P{3, 4, 5, "Pythagoras"})
	if err != nil {
		log.Fatal("encode error:", err)
	}
	err = enc.Encode(P{1782, 1841, 1922, "Treehouse"})
	if err != nil {
		log.Fatal("encode error:", err)
	}

// Decode (receive) and print the values.
	var q Q
	err = dec.Decode(&q)
	if err != nil {
		log.Fatal("decode error 1:", err)
	}
	fmt.Printf("%q: {%d, %d}\n", q.Name, *q.X, *q.Y)
	err = dec.Decode(&q)
	if err != nil {
		log.Fatal("decode error 2:", err)
	}
	fmt.Printf("%q: {%d, %d}\n", q.Name, *q.X, *q.Y)

}

```

```go
Output:
"Pythagoras": {3, 4}
"Treehouse": {1782, 1841}

```

Share Format Run

This example transmits a value that implements the custom encoding and decoding methods.

```go

package main

import (
	"bytes"
	"encoding/gob"
	"fmt"
	"log"
)

// The Vector type has unexported fields, which the package cannot access.
// We therefore write a BinaryMarshal/BinaryUnmarshal method pair to allow us
// to send and receive the type with the gob package. These interfaces are
// defined in the "encoding" package.
// We could equivalently use the locally defined GobEncode/GobDecoder
// interfaces.
type Vector struct {
	x, y, z int
}

func (v Vector) MarshalBinary() ([]byte, error) {
	// A simple encoding: plain text.
	var b bytes.Buffer
	fmt.Fprintln(&b, v.x, v.y, v.z)
	return b.Bytes(), nil
}

// UnmarshalBinary modifies the receiver so it must take a pointer receiver.
func (v *Vector) UnmarshalBinary(data []byte) error {
	// A simple encoding: plain text.
	b := bytes.NewBuffer(data)
	_, err := fmt.Fscanln(b, &v.x, &v.y, &v.z)
	return err
}

// This example transmits a value that implements the custom encoding and decoding methods.
func main() {
	var network bytes.Buffer // Stand-in for the network.

// Create an encoder and send a value.
	enc := gob.NewEncoder(&network)
	err := enc.Encode(Vector{3, 4, 5})
	if err != nil {
		log.Fatal("encode:", err)
	}

// Create a decoder and receive a value.
	dec := gob.NewDecoder(&network)
	var v Vector
	err = dec.Decode(&v)
	if err != nil {
		log.Fatal("decode:", err)
	}
	fmt.Println(v)

}

```

```go
Output:
{3 4 5}

```

Share Format Run

This example shows how to encode an interface value. The key distinction from regular types is to register the concrete type that implements the interface.

```go

package main

import (
	"bytes"
	"encoding/gob"
	"fmt"
	"log"
	"math"
)

type Point struct {
	X, Y int
}

func (p Point) Hypotenuse() float64 {
	return math.Hypot(float64(p.X), float64(p.Y))
}

type Pythagoras interface {
	Hypotenuse() float64
}

// This example shows how to encode an interface value. The key
// distinction from regular types is to register the concrete type that
// implements the interface.
func main() {
	var network bytes.Buffer // Stand-in for the network.

// We must register the concrete type for the encoder and decoder (which would
	// normally be on a separate machine from the encoder). On each end, this tells the
	// engine which concrete type is being sent that implements the interface.
	gob.Register(Point{})

// Create an encoder and send some values.
	enc := gob.NewEncoder(&network)
	for i := 1; i <= 3; i++ {
		interfaceEncode(enc, Point{3 * i, 4 * i})
	}

// Create a decoder and receive some values.
	dec := gob.NewDecoder(&network)
	for i := 1; i <= 3; i++ {
		result := interfaceDecode(dec)
		fmt.Println(result.Hypotenuse())
	}

}

// interfaceEncode encodes the interface value into the encoder.
func interfaceEncode(enc *gob.Encoder, p Pythagoras) {
	// The encode will fail unless the concrete type has been
	// registered. We registered it in the calling function.

// Pass pointer to interface so Encode sees (and hence sends) a value of
	// interface type. If we passed p directly it would see the concrete type instead.
	// See the blog post, "The Laws of Reflection" for background.
	err := enc.Encode(&p)
	if err != nil {
		log.Fatal("encode:", err)
	}
}

// interfaceDecode decodes the next interface value from the stream and returns it.
func interfaceDecode(dec *gob.Decoder) Pythagoras {
	// The decode will fail unless the concrete type on the wire has been
	// registered. We registered it in the calling function.
	var p Pythagoras
	err := dec.Decode(&p)
	if err != nil {
		log.Fatal("decode:", err)
	}
	return p
}

```

```go
Output:
5
10
15

```

Share Format Run

-  func Register(value any)
-  func RegisterName(name string, value any)
-  type CommonType
-  type Decoder
-
-  func NewDecoder(r io.Reader) *Decoder

-
-  func (dec *Decoder) Decode(e any) error
-  func (dec *Decoder) DecodeValue(v reflect.Value) error
