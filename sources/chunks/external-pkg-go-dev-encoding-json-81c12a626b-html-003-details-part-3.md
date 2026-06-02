---
source_name: "External Linked Documentation"
source_url: "https://pkg.go.dev/encoding/json"
source_path: "sources/raw/external/pkg-go-dev-encoding-json-81c12a626b.html"
license_ref: ""
---

fmt.Println(json.Valid([]byte(goodJSON)), json.Valid([]byte(badJSON)))
}

```

```go
Output:
true false

```

Share Format Run

```go
type Decoder struct {
	// contains filtered or unexported fields
}
```

A Decoder reads and decodes JSON values from an input stream.

This example uses a Decoder to decode a stream of distinct JSON values.

```go

package main

import (
	"encoding/json"
	"fmt"
	"io"
	"log"
	"strings"
)

func main() {
	const jsonStream = `
	{"Name": "Ed", "Text": "Knock knock."}
	{"Name": "Sam", "Text": "Who's there?"}
	{"Name": "Ed", "Text": "Go fmt."}
	{"Name": "Sam", "Text": "Go fmt who?"}
	{"Name": "Ed", "Text": "Go fmt yourself!"}
`
	type Message struct {
		Name, Text string
	}
	dec := json.NewDecoder(strings.NewReader(jsonStream))
	for {
		var m Message
		if err := dec.Decode(&m); err == io.EOF {
			break
		} else if err != nil {
			log.Fatal(err)
		}
		fmt.Printf("%s: %s\n", m.Name, m.Text)
	}
}

```

```go
Output:
Ed: Knock knock.
Sam: Who's there?
Ed: Go fmt.
Sam: Go fmt who?
Ed: Go fmt yourself!

```

Share Format Run

```go
func NewDecoder(r io.Reader) *Decoder
```

NewDecoder returns a new decoder that reads from r.

The decoder introduces its own buffering and may read data from r beyond the JSON values requested.

```go
func (dec *Decoder) Buffered() io.Reader
```

Buffered returns a reader of the data remaining in the Decoder's buffer. The reader is valid until the next call to Decoder.Decode.

```go
func (dec *Decoder) Decode(v any) error
```

Decode reads the next JSON-encoded value from its input and stores it in the value pointed to by v.

See the documentation for Unmarshal for details about the conversion of JSON into a Go value.

This example uses a Decoder to decode a streaming array of JSON objects.

```go

package main

import (
	"encoding/json"
	"fmt"
	"log"
	"strings"
)

func main() {
	const jsonStream = `
	[
		{"Name": "Ed", "Text": "Knock knock."},
		{"Name": "Sam", "Text": "Who's there?"},
		{"Name": "Ed", "Text": "Go fmt."},
		{"Name": "Sam", "Text": "Go fmt who?"},
		{"Name": "Ed", "Text": "Go fmt yourself!"}
	]
`
	type Message struct {
		Name, Text string
	}
	dec := json.NewDecoder(strings.NewReader(jsonStream))

// read open bracket
	t, err := dec.Token()
	if err != nil {
		log.Fatal(err)
	}
	fmt.Printf("%T: %v\n", t, t)

// while the array contains values
	for dec.More() {
		var m Message
		// decode an array value (Message)
		err := dec.Decode(&m)
		if err != nil {
			log.Fatal(err)
		}

fmt.Printf("%v: %v\n", m.Name, m.Text)
	}

// read closing bracket
	t, err = dec.Token()
	if err != nil {
		log.Fatal(err)
	}
	fmt.Printf("%T: %v\n", t, t)

}

```

```go
Output:
json.Delim: [
Ed: Knock knock.
Sam: Who's there?
Ed: Go fmt.
Sam: Go fmt who?
Ed: Go fmt yourself!
json.Delim: ]

```

Share Format Run

```go
func (dec *Decoder) DisallowUnknownFields()
```

DisallowUnknownFields causes the Decoder to return an error when the destination is a struct and the input contains object keys which do not match any non-ignored, exported fields in the destination.

```go
func (dec *Decoder) InputOffset() int64
```

InputOffset returns the input stream byte offset of the current decoder position. The offset gives the location of the end of the most recently returned token and the beginning of the next token.

```go
func (dec *Decoder) More() bool
```

More reports whether there is another element in the current array or object being parsed.

```go
func (dec *Decoder) Token() (Token, error)
```

Token returns the next JSON token in the input stream. At the end of the input stream, Token returns nil, io.EOF.

Token guarantees that the delimiters [ ] { } it returns are properly nested and matched: if Token encounters an unexpected delimiter in the input, it will return an error.

The input stream consists of basic JSON values—bool, string, number, and null—along with delimiters [ ] { } of type Delim to mark the start and end of arrays and objects. Commas and colons are elided.

This example uses a Decoder to decode a stream of distinct JSON values.

```go

package main

import (
	"encoding/json"
	"fmt"
	"io"
	"log"
	"strings"
)

func main() {
	const jsonStream = `
	{"Message": "Hello", "Array": [1, 2, 3], "Null": null, "Number": 1.234}
`
	dec := json.NewDecoder(strings.NewReader(jsonStream))
	for {
		t, err := dec.Token()
		if err == io.EOF {
			break
		}
		if err != nil {
			log.Fatal(err)
		}
		fmt.Printf("%T: %v", t, t)
		if dec.More() {
			fmt.Printf(" (more)")
		}
		fmt.Printf("\n")
	}
}

```

```go
Output:
json.Delim: { (more)
string: Message (more)
string: Hello (more)
string: Array (more)
json.Delim: [ (more)
float64: 1 (more)
float64: 2 (more)
float64: 3
json.Delim: ] (more)
string: Null (more)
<nil>: <nil> (more)
string: Number (more)
float64: 1.234
json.Delim: }

```

Share Format Run

```go
func (dec *Decoder) UseNumber()
```

UseNumber causes the Decoder to unmarshal a number into an interface value as a Number instead of as a float64.

```go
type Delim rune
```

A Delim is a JSON array or object delimiter, one of [ ] { or }.

```go
func (d Delim) String() string
```

```go
type Encoder struct {
	// contains filtered or unexported fields
}
```

An Encoder writes JSON values to an output stream.

```go
func NewEncoder(w io.Writer) *Encoder
```

NewEncoder returns a new encoder that writes to w.

```go
func (enc *Encoder) Encode(v any) error
```

Encode writes the JSON encoding of v to the stream, with insignificant space characters elided, followed by a newline character.

See the documentation for Marshal for details about the conversion of Go values to JSON.

```go
func (enc *Encoder) SetEscapeHTML(on bool)
```

SetEscapeHTML specifies whether problematic HTML characters should be escaped inside JSON quoted strings. The default behavior is to escape &, <, and > to \u0026, \u003c, and \u003e to avoid certain safety problems that can arise when embedding JSON in HTML.

In non-HTML settings where the escaping interferes with the readability of the output, SetEscapeHTML(false) disables this behavior.

```go
func (enc *Encoder) SetIndent(prefix, indent string)
```

SetIndent instructs the encoder to format each subsequent encoded value as if indented by the package-level function Indent(dst, src, prefix, indent). Calling SetIndent("", "") disables indentation.

```go
type InvalidUTF8Error struct {
	S string // the whole string value that caused the error
}
```

Before Go 1.2, an InvalidUTF8Error was returned by Marshal when attempting to encode a string value with invalid UTF-8 sequences. As of Go 1.2, Marshal instead coerces the string to valid UTF-8 by replacing invalid bytes with the Unicode replacement rune U+FFFD.

Deprecated: No longer used; kept for compatibility.

```go
func (e *InvalidUTF8Error) Error() string
```

```go
type InvalidUnmarshalError struct {
	Type reflect.Type
}
```

An InvalidUnmarshalError describes an invalid argument passed to Unmarshal. (The argument to Unmarshal must be a non-nil pointer.)

```go
func (e *InvalidUnmarshalError) Error() string
```

```go
type Marshaler interface {
	MarshalJSON() ([]byte, error)
}
```

Marshaler is the interface implemented by types that can marshal themselves into valid JSON.

```go
type MarshalerError struct {
	Type reflect.Type
	Err  error
	// contains filtered or unexported fields
}
```

A MarshalerError represents an error from calling a [Marshaler.MarshalJSON] or encoding.TextMarshaler.MarshalText method.

```go
func (e *MarshalerError) Error() string
```

```go
func (e *MarshalerError) Unwrap() error
```

Unwrap returns the underlying error.

```go
type Number string
```

A Number represents a JSON number literal.

```go
func (n Number) Float64() (float64, error)
```

Float64 returns the number as a float64.

```go
func (n Number) Int64() (int64, error)
```

Int64 returns the number as an int64.

```go
func (n Number) String() string
```

String returns the literal text of the number.

```go
type RawMessage []byte
```

RawMessage is a raw encoded JSON value. It implements Marshaler and Unmarshaler and can be used to delay JSON decoding or precompute a JSON encoding.

This example uses RawMessage to use a precomputed JSON during marshal.

```go

package main

import (
	"encoding/json"
	"fmt"
	"os"
)

func main() {
	h := json.RawMessage(`{"precomputed": true}`)

c := struct {
		Header *json.RawMessage `json:"header"`
		Body   string           `json:"body"`
	}{Header: &h, Body: "Hello Gophers!"}

b, err := json.MarshalIndent(&c, "", "\t")
	if err != nil {
		fmt.Println("error:", err)
	}
	os.Stdout.Write(b)

}

```

```go
Output:
{
	"header": {
		"precomputed": true
	},
	"body": "Hello Gophers!"
}

```

Share Format Run

This example uses RawMessage to delay parsing part of a JSON message.

```go

package main

import (
	"encoding/json"
	"fmt"
	"log"
)

func main() {
	type Color struct {
		Space string
		Point json.RawMessage // delay parsing until we know the color space
	}
	type RGB struct {
		R uint8
		G uint8
		B uint8
	}
	type YCbCr struct {
		Y  uint8
		Cb int8
		Cr int8
	}

var j = []byte(`[
	{"Space": "YCbCr", "Point": {"Y": 255, "Cb": 0, "Cr": -10}},
	{"Space": "RGB",   "Point": {"R": 98, "G": 218, "B": 255}}
]`)
	var colors []Color
	err := json.Unmarshal(j, &colors)
	if err != nil {
		log.Fatalln("error:", err)
	}

for _, c := range colors {
		var dst any
		switch c.Space {
		case "RGB":
			dst = new(RGB)
		case "YCbCr":
			dst = new(YCbCr)
		}
		err := json.Unmarshal(c.Point, dst)
		if err != nil {
			log.Fatalln("error:", err)
		}
		fmt.Println(c.Space, dst)
	}
}

```

```go
Output:
YCbCr &{255 0 -10}
RGB &{98 218 255}

```

Share Format Run

```go
func (m RawMessage) MarshalJSON() ([]byte, error)
```

MarshalJSON returns m as the JSON encoding of m.

```go
func (m *RawMessage) UnmarshalJSON(data []byte) error
```

UnmarshalJSON sets *m to a copy of data.

```go
type SyntaxError struct {
	Offset int64 // error occurred after reading Offset bytes
	// contains filtered or unexported fields
}
```

A SyntaxError is a description of a JSON syntax error. Unmarshal will return a SyntaxError if the JSON can't be parsed.

```go
func (e *SyntaxError) Error() string
```

```go
type Token any
```

A Token holds a value of one of these types:
