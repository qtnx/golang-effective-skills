---
source_name: "External Linked Documentation"
source_url: "https://pkg.go.dev/encoding/gob"
source_path: "sources/raw/external/pkg-go-dev-encoding-gob-fa8ae5ca51.html"
license_ref: ""
---

gob package - encoding/gob - Go Packages
## Details

-     Valid go.mod <https://cs.opensource.google/go/go/+/go1.26.3:src/go.mod> file
 The Go module system was introduced in Go 1.11 and is the official dependency management solution for Go.

-     Redistributable license
 Redistributable licenses place minimal restrictions on how software can be used, modified, and redistributed.

-     Tagged version
Modules with tagged versions give importers more predictable builds.

-     Stable version
When a project reaches major version v1 it is considered stable.

-  Learn more about best practices

## Repository
   cs.opensource.google/go/go  <https://cs.opensource.google/go/go>

##   Documentation ¶

Package gob manages streams of gobs - binary values exchanged between an Encoder (transmitter) and a Decoder (receiver). A typical use is transporting arguments and results of remote procedure calls (RPCs) such as those provided by net/rpc.

The implementation compiles a custom codec for each data type in the stream and is most efficient when a single Encoder is used to transmit a stream of values, amortizing the cost of compilation.

#### Basics ¶

A stream of gobs is self-describing. Each data item in the stream is preceded by a specification of its type, expressed in terms of a small set of predefined types. Pointers are not transmitted, but the things they point to are transmitted; that is, the values are flattened. Nil pointers are not permitted, as they have no value. Recursive types work fine, but recursive values (data with cycles) are problematic. This may change.

To use gobs, create an Encoder and present it with a series of data items as values or addresses that can be dereferenced to values. The Encoder makes sure all type information is sent before it is needed. At the receive side, a Decoder retrieves values from the encoded stream and unpacks them into local variables.

#### Types and Values ¶

The source and destination values/types need not correspond exactly. For structs, fields (identified by name) that are in the source but absent from the receiving variable will be ignored. Fields that are in the receiving variable but missing from the transmitted type or value will be ignored in the destination. If a field with the same name is present in both, their types must be compatible. Both the receiver and transmitter will do all necessary indirection and dereferencing to convert between gobs and actual Go values. For instance, a gob type that is schematically,

```go
struct { A, B int }

```

can be sent from or received into any of these Go types:

```go
struct { A, B int }	// the same
*struct { A, B int }	// extra indirection of the struct
struct { *A, **B int }	// extra indirection of the fields
struct { A, B int64 }	// different concrete value type; see below

```

It may also be received into any of these:

```go
struct { A, B int }	// the same
struct { B, A int }	// ordering doesn't matter; matching is by name
struct { A, B, C int }	// extra field (C) ignored
struct { B int }	// missing field (A) ignored; data will be dropped
struct { B, C int }	// missing field (A) ignored; extra field (C) ignored.

```

Attempting to receive into these types will draw a decode error:

```go
struct { A int; B uint }	// change of signedness for B
struct { A int; B float }	// change of type for B
struct { }			// no field names in common
struct { C, D int }		// no field names in common

```

Integers are transmitted two ways: arbitrary precision signed integers or arbitrary precision unsigned integers. There is no int8, int16 etc. discrimination in the gob format; there are only signed and unsigned integers. As described below, the transmitter sends the value in a variable-length encoding; the receiver accepts the value and stores it in the destination variable. Floating-point numbers are always sent using IEEE 754 64-bit precision (see below).

Signed integers may be received into any signed integer variable: int, int16, etc.; unsigned integers may be received into any unsigned integer variable; and floating point values may be received into any floating point variable. However, the destination variable must be able to represent the value or the decode operation will fail.

Structs, arrays and slices are also supported. Structs encode and decode only exported fields. Strings and arrays of bytes are supported with a special, efficient representation (see below). When a slice is decoded, if the existing slice has capacity the slice will be extended in place; if not, a new array is allocated. Regardless, the length of the resulting slice reports the number of elements decoded.

In general, if allocation is required, the decoder will allocate memory. If not, it will update the destination variables with values read from the stream. It does not initialize them first, so if the destination is a compound value such as a map, struct, or slice, the decoded values will be merged elementwise into the existing variables.

Functions and channels will not be sent in a gob. Attempting to encode such a value at the top level will fail. A struct field of chan or func type is treated exactly like an unexported field and is ignored.

Gob can encode a value of any type implementing the GobEncoder or encoding.BinaryMarshaler interfaces by calling the corresponding method, in that order of preference.

Gob can decode a value of any type implementing the GobDecoder or encoding.BinaryUnmarshaler interfaces by calling the corresponding method, again in that order of preference.

#### Encoding Details ¶

This section documents the encoding, details that are not important for most users. Details are presented bottom-up.

An unsigned integer is sent one of two ways. If it is less than 128, it is sent as a byte with that value. Otherwise it is sent as a minimal-length big-endian (high byte first) byte stream holding the value, preceded by one byte holding the byte count, negated. Thus 0 is transmitted as (00), 7 is transmitted as (07) and 256 is transmitted as (FE 01 00).

A boolean is encoded within an unsigned integer: 0 for false, 1 for true.

A signed integer, i, is encoded within an unsigned integer, u. Within u, bits 1 upward contain the value; bit 0 says whether they should be complemented upon receipt. The encode algorithm looks like this:

```go
var u uint
if i < 0 {
	u = (^uint(i) << 1) | 1 // complement i, bit 0 is 1
} else {
	u = (uint(i) << 1) // do not complement i, bit 0 is 0
}
encodeUnsigned(u)

```

The low bit is therefore analogous to a sign bit, but making it the complement bit instead guarantees that the largest negative integer is not a special case. For example, -129=^128=(^256>>1) encodes as (FE 01 01).

Floating-point numbers are always sent as a representation of a float64 value. That value is converted to a uint64 using math.Float64bits. The uint64 is then byte-reversed and sent as a regular unsigned integer. The byte-reversal means the exponent and high-precision part of the mantissa go first. Since the low bits are often zero, this can save encoding bytes. For instance, 17.0 is encoded in only three bytes (FE 31 40).

Strings and slices of bytes are sent as an unsigned count followed by that many uninterpreted bytes of the value.

All other slices and arrays are sent as an unsigned count followed by that many elements using the standard gob encoding for their type, recursively.

Maps are sent as an unsigned count followed by that many key, element pairs. Empty but non-nil maps are sent, so if the receiver has not allocated one already, one will always be allocated on receipt unless the transmitted map is nil and not at the top level.

In slices and arrays, as well as maps, all elements, even zero-valued elements, are transmitted, even if all the elements are zero.

Structs are sent as a sequence of (field number, field value) pairs. The field value is sent using the standard gob encoding for its type, recursively. If a field has the zero value for its type (except for arrays; see above) or it's a pointer to a zero value, it is omitted from the transmission. The field number is defined by the type of the encoded struct: the first field of the encoded type is field 0, the second is field 1, etc. When encoding a value, the field numbers are delta encoded for efficiency and the fields are always sent in order of increasing field number; the deltas are therefore unsigned. The initialization for the delta encoding sets the field number to -1, so an unsigned integer field 0 with value 7 is transmitted as unsigned delta = 1, unsigned value = 7 or (01 07). Finally, after all the fields have been sent a terminating mark denotes the end of the struct. That mark is a delta=0 value, which has representation (00).
