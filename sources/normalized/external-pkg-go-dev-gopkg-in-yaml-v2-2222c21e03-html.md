yaml package - gopkg.in/yaml.v2 - Go Packages

        The highest tagged major version is v3.

## Details

-     Valid go.mod <https://github.com/go-yaml/yaml/tree/v2.4.0/go.mod> file
 The Go module system was introduced in Go 1.11 and is the official dependency management solution for Go.

-     Redistributable license
 Redistributable licenses place minimal restrictions on how software can be used, modified, and redistributed.

-     Tagged version
Modules with tagged versions give importers more predictable builds.

-     Stable version
When a project reaches major version v1 it is considered stable.

-  Learn more about best practices

## Repository
   github.com/go-yaml/yaml  <https://github.com/go-yaml/yaml>

## Links

-    Open Source Insights  <https://deps.dev/go/gopkg.in%2Fyaml.v2/v2.4.0>

##   README ¶

### YAML support for the Go language

#### Introduction

The yaml package enables Go programs to comfortably encode and decode YAML values. It was developed within Canonical <https://www.canonical.com> as part of the juju <https://juju.ubuntu.com> project, and is based on a pure Go port of the well-known libyaml <http://pyyaml.org/wiki/LibYAML> C library to parse and generate YAML data quickly and reliably.

#### Compatibility

The yaml package supports most of YAML 1.1 and 1.2, including support for anchors, tags, map merging, etc. Multi-document unmarshalling is not yet implemented, and base-60 floats from YAML 1.1 are purposefully not supported since they're a poor design and are gone in YAML 1.2.

#### Installation and usage

The import path for the package is _gopkg.in/yaml.v2_.

To install it, run:

```go
go get gopkg.in/yaml.v2

```

#### API documentation

If opened in a browser, the import path itself leads to the API documentation:

- https://gopkg.in/yaml.v2 <https://gopkg.in/yaml.v2>

#### API stability

The package API for yaml v2 will remain stable as described in gopkg.in <https://gopkg.in>.

#### License

The yaml package is licensed under the Apache License 2.0. Please see the LICENSE file for details.

#### Example

```go
package main

import (
        "fmt"
        "log"

        "gopkg.in/yaml.v2"
)

var data = `
a: Easy!
b:
  c: 2
  d: [3, 4]
`

// Note: struct fields must be public in order for unmarshal to
// correctly populate the data.
type T struct {
        A string
        B struct {
                RenamedC int   `yaml:"c"`
                D        []int `yaml:",flow"`
        }
}

func main() {
        t := T{}

        err := yaml.Unmarshal([]byte(data), &t)
        if err != nil {
                log.Fatalf("error: %v", err)
        }
        fmt.Printf("--- t:\n%v\n\n", t)

        d, err := yaml.Marshal(&t)
        if err != nil {
                log.Fatalf("error: %v", err)
        }
        fmt.Printf("--- t dump:\n%s\n\n", string(d))

        m := make(map[interface{}]interface{})

        err = yaml.Unmarshal([]byte(data), &m)
        if err != nil {
                log.Fatalf("error: %v", err)
        }
        fmt.Printf("--- m:\n%v\n\n", m)

        d, err = yaml.Marshal(&m)
        if err != nil {
                log.Fatalf("error: %v", err)
        }
        fmt.Printf("--- m dump:\n%s\n\n", string(d))
}

```

This example will generate the following output:

```go
--- t:
{Easy! {2 [3 4]}}

--- t dump:
a: Easy!
b:
  c: 2
  d: [3, 4]

--- m:
map[a:Easy! b:map[c:2 d:[3 4]]]

--- m dump:
a: Easy!
b:
  c: 2
  d:
  - 3
  - 4

```

 Expand ▾ Collapse ▴

##   Documentation ¶

Package yaml implements YAML support for the Go language.

Source code and other details for the project are available at GitHub:

```go
https://github.com/go-yaml/yaml

```

-  func FutureLineWrap()
-  func Marshal(in interface{}) (out []byte, err error)
-  func Unmarshal(in []byte, out interface{}) (err error)
-  func UnmarshalStrict(in []byte, out interface{}) (err error)
-  type Decoder
-
-  func NewDecoder(r io.Reader) *Decoder

-
-  func (dec *Decoder) Decode(v interface{}) (err error)
-  func (dec *Decoder) SetStrict(strict bool)

-  type Encoder
-
-  func NewEncoder(w io.Writer) *Encoder

-
-  func (e *Encoder) Close() (err error)
-  func (e *Encoder) Encode(v interface{}) (err error)

-  type IsZeroer
-  type MapItem
-  type MapSlice
-  type Marshaler
-  type TypeError
-
-  func (e *TypeError) Error() string

-  type Unmarshaler

- Unmarshal (Embedded)

This section is empty.

This section is empty.

```go
func FutureLineWrap()
```

FutureLineWrap globally disables line wrapping when encoding long strings. This is a temporary and thus deprecated method introduced to faciliate migration towards v3, which offers more control of line lengths on individual encodings, and has a default matching the behavior introduced by this function.

The default formatting of v2 was erroneously changed in v2.3.0 and reverted in v2.4.0, at which point this function was introduced to help migration.

```go
func Marshal(in interface{}) (out []byte, err error)
```

Marshal serializes the value provided into a YAML document. The structure of the generated document will reflect the structure of the value itself. Maps and pointers (to struct, string, int, etc) are accepted as the in value.

Struct fields are only marshalled if they are exported (have an upper case first letter), and are marshalled using the field name lowercased as the default key. Custom keys may be defined via the "yaml" name in the field tag: the content preceding the first comma is used as the key, and the following comma-separated options are used to tweak the marshalling process. Conflicting names result in a runtime error.

The field tag format accepted is:

```go
`(...) yaml:"[<key>][,<flag1>[,<flag2>]]" (...)`

```

The following flags are currently supported:

```go
omitempty    Only include the field if it's not set to the zero
             value for the type or to empty slices or maps.
             Zero valued structs will be omitted if all their public
             fields are zero, unless they implement an IsZero
             method (see the IsZeroer interface type), in which
             case the field will be excluded if IsZero returns true.

flow         Marshal using a flow style (useful for structs,
             sequences and maps).

inline       Inline the field, which must be a struct or a map,
             causing all of its fields or keys to be processed as if
             they were part of the outer struct. For maps, keys must
             not conflict with the yaml keys of other struct fields.

```

In addition, if the key is "-", the field is ignored.

For example:

```go
type T struct {
    F int `yaml:"a,omitempty"`
    B int
}
yaml.Marshal(&T{B: 2}) // Returns "b: 2\n"
yaml.Marshal(&T{F: 1}} // Returns "a: 1\nb: 0\n"

```

```go
func Unmarshal(in []byte, out interface{}) (err error)
```

Unmarshal decodes the first document found within the in byte slice and assigns decoded values into the out value.

Maps and pointers (to a struct, string, int, etc) are accepted as out values. If an internal pointer within a struct is not initialized, the yaml package will initialize it if necessary for unmarshalling the provided data. The out parameter must not be nil.

The type of the decoded values should be compatible with the respective values in out. If one or more values cannot be decoded due to a type mismatches, decoding continues partially until the end of the YAML content, and a *yaml.TypeError is returned with details for all missed values.

Struct fields are only unmarshalled if they are exported (have an upper case first letter), and are unmarshalled using the field name lowercased as the default key. Custom keys may be defined via the "yaml" name in the field tag: the content preceding the first comma is used as the key, and the following comma-separated options are used to tweak the marshalling process (see Marshal). Conflicting names result in a runtime error.

For example:

```go
type T struct {
    F int `yaml:"a,omitempty"`
    B int
}
var t T
yaml.Unmarshal([]byte("a: 1\nb: 2"), &t)

```

See the documentation of Marshal for the format of tags and a list of supported tag options.

```go

package main

import (
	"fmt"
	"log"

	"gopkg.in/yaml.v2"
)

// An example showing how to unmarshal embedded
// structs from YAML.

type StructA struct {
	A string `yaml:"a"`
}

type StructB struct {
	// Embedded structs are not treated as embedded in YAML by default. To do that,
	// add the ",inline" annotation below
	StructA `yaml:",inline"`
	B       string `yaml:"b"`
}

var data = `
a: a string from struct A
b: a string from struct B
`

func main() {
	var b StructB

	err := yaml.Unmarshal([]byte(data), &b)
	if err != nil {
		log.Fatalf("cannot unmarshal data: %v", err)
	}
	fmt.Println(b.A)
	fmt.Println(b.B)
}

```

```go
Output:
a string from struct A
a string from struct B

```

 Share Format Run

```go
func UnmarshalStrict(in []byte, out interface{}) (err error)
```

UnmarshalStrict is like Unmarshal except that any fields that are found in the data that do not have corresponding struct members, or mapping keys that are duplicates, will result in an error.

```go
type Decoder struct {
	// contains filtered or unexported fields
}
```

A Decoder reads and decodes YAML values from an input stream.

```go
func NewDecoder(r io.Reader) *Decoder
```

NewDecoder returns a new decoder that reads from r.

The decoder introduces its own buffering and may read data from r beyond the YAML values requested.

```go
func (dec *Decoder) Decode(v interface{}) (err error)
```

Decode reads the next YAML-encoded value from its input and stores it in the value pointed to by v.

See the documentation for Unmarshal for details about the conversion of YAML into a Go value.

```go
func (dec *Decoder) SetStrict(strict bool)
```

SetStrict sets whether strict decoding behaviour is enabled when decoding items in the data (see UnmarshalStrict). By default, decoding is not strict.

```go
type Encoder struct {
	// contains filtered or unexported fields
}
```

An Encoder writes YAML values to an output stream.

```go
func NewEncoder(w io.Writer) *Encoder
```

NewEncoder returns a new encoder that writes to w. The Encoder should be closed after use to flush all data to w.

```go
func (e *Encoder) Close() (err error)
```

Close closes the encoder by writing any remaining data. It does not write a stream terminating string "...".

```go
func (e *Encoder) Encode(v interface{}) (err error)
```

Encode writes the YAML encoding of v to the stream. If multiple items are encoded to the stream, the second and subsequent document will be preceded with a "---" document separator, but the first will not.

See the documentation for Marshal for details about the conversion of Go values to YAML.

```go
type IsZeroer interface {
	IsZero() bool
}
```

IsZeroer is used to check whether an object is zero to determine whether it should be omitted when marshaling with the omitempty flag. One notable implementation is time.Time.

```go
type MapItem struct {
	Key, Value interface{}
}
```

MapItem is an item in a MapSlice.

```go
type MapSlice []MapItem
```

MapSlice encodes and decodes as a YAML map. The order of keys is preserved when encoding and decoding.

```go
type Marshaler interface {
	MarshalYAML() (interface{}, error)
}
```

The Marshaler interface may be implemented by types to customize their behavior when being marshaled into a YAML document. The returned value is marshaled in place of the original value implementing Marshaler.

If an error is returned by MarshalYAML, the marshaling procedure stops and returns with the provided error.

```go
type TypeError struct {
	Errors []string
}
```

A TypeError is returned by Unmarshal when one or more fields in the YAML document cannot be properly decoded into the requested types. When this error is returned, the value is still unmarshaled partially.

```go
func (e *TypeError) Error() string
```

```go
type Unmarshaler interface {
	UnmarshalYAML(unmarshal func(interface{}) error) error
}
```

The Unmarshaler interface may be implemented by types to customize their behavior when being unmarshaled from a YAML document. The UnmarshalYAML method receives a function that may be called to unmarshal the original YAML value into a field or variable. It is safe to call the unmarshal function parameter more than once if necessary.

##   Source Files ¶
 View all Source files <https://github.com/go-yaml/yaml/tree/v2.4.0>

- apic.go <https://github.com/go-yaml/yaml/blob/v2.4.0/apic.go>
- decode.go <https://github.com/go-yaml/yaml/blob/v2.4.0/decode.go>
- emitterc.go <https://github.com/go-yaml/yaml/blob/v2.4.0/emitterc.go>
- encode.go <https://github.com/go-yaml/yaml/blob/v2.4.0/encode.go>
- parserc.go <https://github.com/go-yaml/yaml/blob/v2.4.0/parserc.go>
- readerc.go <https://github.com/go-yaml/yaml/blob/v2.4.0/readerc.go>
- resolve.go <https://github.com/go-yaml/yaml/blob/v2.4.0/resolve.go>
- scannerc.go <https://github.com/go-yaml/yaml/blob/v2.4.0/scannerc.go>
- sorter.go <https://github.com/go-yaml/yaml/blob/v2.4.0/sorter.go>
- writerc.go <https://github.com/go-yaml/yaml/blob/v2.4.0/writerc.go>
- yaml.go <https://github.com/go-yaml/yaml/blob/v2.4.0/yaml.go>
- yamlh.go <https://github.com/go-yaml/yaml/blob/v2.4.0/yamlh.go>
- yamlprivateh.go <https://github.com/go-yaml/yaml/blob/v2.4.0/yamlprivateh.go>

  Click to show internal directories.
  Click to hide internal directories.

  Close

     **?** : This menu   **/** : Search site   **f** or **F** : Jump to   **y** or **Y**  : Canonical URL
  Close
