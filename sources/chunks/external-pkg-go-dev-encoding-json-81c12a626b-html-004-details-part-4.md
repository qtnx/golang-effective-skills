---
source_name: "External Linked Documentation"
source_url: "https://pkg.go.dev/encoding/json"
source_path: "sources/raw/external/pkg-go-dev-encoding-json-81c12a626b.html"
license_ref: ""
---

- Delim, for the four JSON delimiters [ ] { }
- bool, for JSON booleans
- float64, for JSON numbers
- Number, for JSON numbers
- string, for JSON string literals
- nil, for JSON null

```go
type UnmarshalFieldError struct {
	Key   string
	Type  reflect.Type
	Field reflect.StructField
}
```

An UnmarshalFieldError describes a JSON object key that led to an unexported (and therefore unwritable) struct field.

Deprecated: No longer used; kept for compatibility.

```go
func (e *UnmarshalFieldError) Error() string
```

```go
type UnmarshalTypeError struct {
	Value  string       // description of JSON value - "bool", "array", "number -5"
	Type   reflect.Type // type of Go value it could not be assigned to
	Offset int64        // error occurred after reading Offset bytes
	Struct string       // name of the struct type containing the field
	Field  string       // the full path from root node to the field, include embedded struct
}
```

An UnmarshalTypeError describes a JSON value that was not appropriate for a value of a specific Go type.

```go
func (e *UnmarshalTypeError) Error() string
```

```go
type Unmarshaler interface {
	UnmarshalJSON([]byte) error
}
```

Unmarshaler is the interface implemented by types that can unmarshal a JSON description of themselves. The input can be assumed to be a valid encoding of a JSON value. UnmarshalJSON must copy the JSON data if it wishes to retain the data after returning.

```go
type UnsupportedTypeError struct {
	Type reflect.Type
}
```

An UnsupportedTypeError is returned by Marshal when attempting to encode an unsupported value type.

```go
func (e *UnsupportedTypeError) Error() string
```

```go
type UnsupportedValueError struct {
	Value reflect.Value
	Str   string
}
```

An UnsupportedValueError is returned by Marshal when attempting to encode an unsupported value.

```go
func (e *UnsupportedValueError) Error() string
```
