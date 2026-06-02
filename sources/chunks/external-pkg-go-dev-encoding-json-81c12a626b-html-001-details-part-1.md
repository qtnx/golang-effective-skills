---
source_name: "External Linked Documentation"
source_url: "https://pkg.go.dev/encoding/json"
source_path: "sources/raw/external/pkg-go-dev-encoding-json-81c12a626b.html"
license_ref: ""
---

json package - encoding/json - Go Packages
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

Package json implements encoding and decoding of JSON as defined in RFC 7159 <https://rfc-editor.org/rfc/rfc7159.html>. The mapping between JSON and Go values is described in the documentation for the Marshal and Unmarshal functions.

See "JSON and Go" for an introduction to this package: https://golang.org/doc/articles/json_and_go.html <https://golang.org/doc/articles/json_and_go.html>

#### Security Considerations ¶

The JSON standard (RFC 7159 <https://rfc-editor.org/rfc/rfc7159.html>) is lax in its definition of a number of parser behaviors. As such, many JSON parsers behave differently in various scenarios. These differences in parsers mean that systems that use multiple independent JSON parser implementations may parse the same JSON object in differing ways.

Systems that rely on a JSON object being parsed consistently for security purposes should be careful to understand the behaviors of this parser, as well as how these behaviors may cause interoperability issues with other parser implementations.

Due to the Go Backwards Compatibility promise (https://go.dev/doc/go1compat <https://go.dev/doc/go1compat>) there are a number of behaviors this package exhibits that may cause interopability issues, but cannot be changed. In particular the following parsing behaviors may cause issues:

- If a JSON object contains duplicate keys, keys are processed in the order they are observed, meaning later values will replace or be merged into prior values, depending on the field type (in particular maps and structs will have values merged, while other types have values replaced).
- When parsing a JSON object into a Go struct, keys are considered in a case-insensitive fashion.
- When parsing a JSON object into a Go struct, unknown keys in the JSON object are ignored (unless a Decoder is used and Decoder.DisallowUnknownFields has been called).
- Invalid UTF-8 bytes in JSON strings are replaced by the Unicode replacement character.
- Large JSON number integers will lose precision when unmarshaled into floating-point types.

```go

//go:build !goexperiment.jsonv2

package main

import (
	"encoding/json"
	"fmt"
	"log"
	"strings"
)

type Animal int

const (
	Unknown Animal = iota
	Gopher
	Zebra
)

func (a *Animal) UnmarshalJSON(b []byte) error {
	var s string
	if err := json.Unmarshal(b, &s); err != nil {
		return err
	}
	switch strings.ToLower(s) {
	default:
		*a = Unknown
	case "gopher":
		*a = Gopher
	case "zebra":
		*a = Zebra
	}

return nil
}

func (a Animal) MarshalJSON() ([]byte, error) {
	var s string
	switch a {
	default:
		s = "unknown"
	case Gopher:
		s = "gopher"
	case Zebra:
		s = "zebra"
	}

return json.Marshal(s)
}

func main() {
	blob := `["gopher","armadillo","zebra","unknown","gopher","bee","gopher","zebra"]`
	var zoo []Animal
	if err := json.Unmarshal([]byte(blob), &zoo); err != nil {
		log.Fatal(err)
	}

census := make(map[Animal]int)
	for _, animal := range zoo {
		census[animal] += 1
	}

fmt.Printf("Zoo Census:\n* Gophers: %d\n* Zebras:  %d\n* Unknown: %d\n",
		census[Gopher], census[Zebra], census[Unknown])

}

```

```go
Output:
Zoo Census:
* Gophers: 3
* Zebras:  2
* Unknown: 3

```

Share Format Run

```go

//go:build !goexperiment.jsonv2

package main

import (
	"encoding/json"
	"fmt"
	"log"
	"strings"
)

type Size int

const (
	Unrecognized Size = iota
	Small
	Large
)

func (s *Size) UnmarshalText(text []byte) error {
	switch strings.ToLower(string(text)) {
	default:
		*s = Unrecognized
	case "small":
		*s = Small
	case "large":
		*s = Large
	}
	return nil
}

func (s Size) MarshalText() ([]byte, error) {
	var name string
	switch s {
	default:
		name = "unrecognized"
	case Small:
		name = "small"
	case Large:
		name = "large"
	}
	return []byte(name), nil
}

func main() {
	blob := `["small","regular","large","unrecognized","small","normal","small","large"]`
	var inventory []Size
	if err := json.Unmarshal([]byte(blob), &inventory); err != nil {
		log.Fatal(err)
	}

counts := make(map[Size]int)
	for _, size := range inventory {
		counts[size] += 1
	}

fmt.Printf("Inventory Counts:\n* Small:        %d\n* Large:        %d\n* Unrecognized: %d\n",
		counts[Small], counts[Large], counts[Unrecognized])

}

```

```go
Output:
Inventory Counts:
* Small:        3
* Large:        2
* Unrecognized: 3

```

Share Format Run

-  func Compact(dst *bytes.Buffer, src []byte) error
-  func HTMLEscape(dst *bytes.Buffer, src []byte)
-  func Indent(dst *bytes.Buffer, src []byte, prefix, indent string) error
-  func Marshal(v any) ([]byte, error)
-  func MarshalIndent(v any, prefix, indent string) ([]byte, error)
-  func Unmarshal(data []byte, v any) error
-  func Valid(data []byte) bool
-  type Decoder
-
-  func NewDecoder(r io.Reader) *Decoder

-
-  func (dec *Decoder) Buffered() io.Reader
-  func (dec *Decoder) Decode(v any) error
-  func (dec *Decoder) DisallowUnknownFields()
-  func (dec *Decoder) InputOffset() int64
-  func (dec *Decoder) More() bool
-  func (dec *Decoder) Token() (Token, error)
-  func (dec *Decoder) UseNumber()

-  type Delim
-
-  func (d Delim) String() string

-  type Encoder
-
-  func NewEncoder(w io.Writer) *Encoder

-
-  func (enc *Encoder) Encode(v any) error
-  func (enc *Encoder) SetEscapeHTML(on bool)
-  func (enc *Encoder) SetIndent(prefix, indent string)

-  type InvalidUTF8Errordeprecated
-
-  func (e *InvalidUTF8Error) Error() string

-  type InvalidUnmarshalError
-
-  func (e *InvalidUnmarshalError) Error() string

-  type Marshaler
-  type MarshalerError
-
-  func (e *MarshalerError) Error() string
-  func (e *MarshalerError) Unwrap() error

-  type Number
-
-  func (n Number) Float64() (float64, error)
-  func (n Number) Int64() (int64, error)
-  func (n Number) String() string

-  type RawMessage
-
-  func (m RawMessage) MarshalJSON() ([]byte, error)
-  func (m *RawMessage) UnmarshalJSON(data []byte) error

-  type SyntaxError
-
-  func (e *SyntaxError) Error() string

-  type Token
-  type UnmarshalFieldErrordeprecated
-
-  func (e *UnmarshalFieldError) Error() string

-  type UnmarshalTypeError
-
-  func (e *UnmarshalTypeError) Error() string

-  type Unmarshaler
-  type UnsupportedTypeError
-
-  func (e *UnsupportedTypeError) Error() string

-  type UnsupportedValueError
-
-  func (e *UnsupportedValueError) Error() string

- Package (CustomMarshalJSON)
- Package (TextMarshalJSON)
- Decoder
- Decoder.Decode (Stream)
- Decoder.Token
- HTMLEscape
- Indent
- Marshal
- MarshalIndent
- RawMessage (Marshal)
- RawMessage (Unmarshal)
- Unmarshal
- Valid

This section is empty.

This section is empty.

```go
func Compact(dst *bytes.Buffer, src []byte) error
```

Compact appends to dst the JSON-encoded src with insignificant space characters elided.

```go
func HTMLEscape(dst *bytes.Buffer, src []byte)
```

HTMLEscape appends to dst the JSON-encoded src with <, >, &, U+2028 and U+2029 characters inside string literals changed to \u003c, \u003e, \u0026, \u2028, \u2029 so that the JSON will be safe to embed inside HTML <script> tags. For historical reasons, web browsers don't honor standard HTML escaping within <script> tags, so an alternative JSON encoding must be used.

```go

package main

import (
	"bytes"
	"encoding/json"
	"os"
)

func main() {
	var out bytes.Buffer
	json.HTMLEscape(&out, []byte(`{"Name":"<b>HTML content</b>"}`))
	out.WriteTo(os.Stdout)
}

```

```go
Output:
{"Name":"\u003cb\u003eHTML content\u003c/b\u003e"}

```

Share Format Run

```go
func Indent(dst *bytes.Buffer, src []byte, prefix, indent string) error
```

Indent appends to dst an indented form of the JSON-encoded src. Each element in a JSON object or array begins on a new, indented line beginning with prefix followed by one or more copies of indent according to the indentation nesting. The data appended to dst does not begin with the prefix nor any indentation, to make it easier to embed inside other formatted JSON data. Although leading space characters (space, tab, carriage return, newline) at the beginning of src are dropped, trailing space characters at the end of src are preserved and copied to dst. For example, if src has no trailing spaces, neither will dst; if src ends in a trailing newline, so will dst.

```go

package main

import (
	"bytes"
	"encoding/json"
	"log"
	"os"
)

func main() {
	type Road struct {
		Name   string
		Number int
	}
	roads := []Road{
		{"Diamond Fork", 29},
		{"Sheep Creek", 51},
	}

b, err := json.Marshal(roads)
	if err != nil {
		log.Fatal(err)
	}

var out bytes.Buffer
	json.Indent(&out, b, "=", "\t")
	out.WriteTo(os.Stdout)
}

```

```go
Output:
[
=	{
=		"Name": "Diamond Fork",
=		"Number": 29
=	},
=	{
=		"Name": "Sheep Creek",
=		"Number": 51
=	}
=]

```

Share Format Run

```go
func Marshal(v any) ([]byte, error)
```

Marshal returns the JSON encoding of v.

Marshal traverses the value v recursively. If an encountered value implements Marshaler and is not a nil pointer, Marshal calls [Marshaler.MarshalJSON] to produce JSON. If no [Marshaler.MarshalJSON] method is present but the value implements encoding.TextMarshaler instead, Marshal calls encoding.TextMarshaler.MarshalText and encodes the result as a JSON string. The nil pointer exception is not strictly necessary but mimics a similar, necessary exception in the behavior of [Unmarshaler.UnmarshalJSON].

Otherwise, Marshal uses the following type-dependent default encodings:

Boolean values encode as JSON booleans.

Floating point, integer, and Number values encode as JSON numbers. NaN and +/-Inf values will return an UnsupportedValueError.

String values encode as JSON strings coerced to valid UTF-8, replacing invalid bytes with the Unicode replacement rune. So that the JSON will be safe to embed inside HTML <script> tags, the string is encoded using HTMLEscape, which replaces "<", ">", "&", U+2028, and U+2029 are escaped to "\u003c","\u003e", "\u0026", "\u2028", and "\u2029". This replacement can be disabled when using an Encoder, by calling Encoder.SetEscapeHTML(false).

Array and slice values encode as JSON arrays, except that []byte encodes as a base64-encoded string, and a nil slice encodes as the null JSON value.

Struct values encode as JSON objects. Each exported struct field becomes a member of the object, using the field name as the object key, unless the field is omitted for one of the reasons given below.
