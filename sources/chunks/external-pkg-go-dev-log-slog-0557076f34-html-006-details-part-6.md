---
source_name: "External Linked Documentation"
source_url: "https://pkg.go.dev/log/slog"
source_path: "sources/raw/external/pkg-go-dev-log-slog-0557076f34.html"
license_ref: ""
---

// The program counter at the time the record was constructed, as determined
	// by runtime.Callers. If zero, no program counter is available.
	//
	// The only valid use for this value is as an argument to
	// [runtime.CallersFrames]. In particular, it must not be passed to
	// [runtime.FuncForPC].
	PC uintptr
	// contains filtered or unexported fields
}
```

A Record holds information about a log event. Copies of a Record share state. Do not modify a Record after handing out a copy to it. Call NewRecord to create a new Record. Use Record.Clone to create a copy with no shared state.

```go
func NewRecord(t time.Time, level Level, msg string, pc uintptr) Record
```

NewRecord creates a Record from the given arguments. Use Record.AddAttrs to add attributes to the Record.

NewRecord is intended for logging APIs that want to support a Handler as a backend.

```go
func (r *Record) Add(args ...any)
```

Add converts the args to Attrs as described in Logger.Log, then appends the Attrs to the Record's list of Attrs. It omits empty groups.

```go
func (r *Record) AddAttrs(attrs ...Attr)
```

AddAttrs appends the given Attrs to the Record's list of Attrs. It omits empty groups.

```go
func (r Record) Attrs(f func(Attr) bool)
```

Attrs calls f on each Attr in the Record. Iteration stops if f returns false.

```go
func (r Record) Clone() Record
```

Clone returns a copy of the record with no shared state. The original record and the clone can both be modified without interfering with each other.

```go
func (r Record) NumAttrs() int
```

NumAttrs returns the number of attributes in the Record.

```go
func (r Record) Source() *Source
```

Source returns a new Source for the log event using r's PC. If the PC field is zero, meaning the Record was created without the necessary information or the location is unavailable, then nil is returned.

```go
type Source struct {
	// Function is the package path-qualified function name containing the
	// source line. If non-empty, this string uniquely identifies a single
	// function in the program. This may be the empty string if not known.
	Function string `json:"function"`
	// File and Line are the file name and line number (1-based) of the source
	// line. These may be the empty string and zero, respectively, if not known.
	File string `json:"file"`
	Line int    `json:"line"`
}
```

Source describes the location of a line of source code.

```go
type TextHandler struct {
	// contains filtered or unexported fields
}
```

TextHandler is a Handler that writes Records to an io.Writer as a sequence of key=value pairs separated by spaces and followed by a newline.

```go
func NewTextHandler(w io.Writer, opts *HandlerOptions) *TextHandler
```

NewTextHandler creates a TextHandler that writes to w, using the given options. If opts is nil, the default options are used.

```go
func (h *TextHandler) Enabled(_ context.Context, level Level) bool
```

Enabled reports whether the handler handles records at the given level. The handler ignores records whose level is lower.

```go
func (h *TextHandler) Handle(_ context.Context, r Record) error
```

Handle formats its argument Record as a single line of space-separated key=value items.

If the Record's time is zero, the time is omitted. Otherwise, the key is "time" and the value is output in RFC3339 format with millisecond precision.

The level's key is "level" and its value is the result of calling Level.String.

If the AddSource option is set and source information is available, the key is "source" and the value is output as FILE:LINE.

The message's key is "msg".

To modify these or other attributes, or remove them from the output, use [HandlerOptions.ReplaceAttr].

If a value implements encoding.TextMarshaler, the result of MarshalText is written. Otherwise, the result of fmt.Sprint is written.

Keys and values are quoted with strconv.Quote if they contain Unicode space characters, non-printing characters, '"' or '='.

Keys inside groups consist of components (keys or group names) separated by dots. No further escaping is performed. Thus there is no way to determine from the key "a.b.c" whether there are two groups "a" and "b" and a key "c", or a single group "a.b" and a key "c", or single group "a" and a key "b.c". If it is necessary to reconstruct the group structure of a key even in the presence of dots inside components, use [HandlerOptions.ReplaceAttr] to encode that information in the key.

Each call to Handle results in a single serialized call to io.Writer.Write.

```go
func (h *TextHandler) WithAttrs(attrs []Attr) Handler
```

WithAttrs returns a new TextHandler whose attributes consists of h's attributes followed by attrs.

```go
func (h *TextHandler) WithGroup(name string) Handler
```

```go
type Value struct {
	// contains filtered or unexported fields
}
```

A Value can represent any Go value, but unlike type any, it can represent most small values without an allocation. The zero Value corresponds to nil.

```go
func AnyValue(v any) Value
```

AnyValue returns a Value for the supplied value.

If the supplied value is of type Value, it is returned unmodified.

Given a value of one of Go's predeclared string, bool, or (non-complex) numeric types, AnyValue returns a Value of kind KindString, KindBool, KindUint64, KindInt64, or KindFloat64. The width of the original numeric type is not preserved.

Given a time.Time or time.Duration value, AnyValue returns a Value of kind KindTime or KindDuration. The monotonic time is not preserved.

For nil, or values of all other types, including named types whose underlying type is numeric, AnyValue returns a value of kind KindAny.

```go
func BoolValue(v bool) Value
```

BoolValue returns a Value for a bool.

```go
func DurationValue(v time.Duration) Value
```

DurationValue returns a Value for a time.Duration.

```go
func Float64Value(v float64) Value
```

Float64Value returns a Value for a floating-point number.

```go
func GroupValue(as ...Attr) Value
```

GroupValue returns a new Value for a list of Attrs. The caller must not subsequently mutate the argument slice.

```go
func Int64Value(v int64) Value
```

Int64Value returns a Value for an int64.

```go
func IntValue(v int) Value
```

IntValue returns a Value for an int.

```go
func StringValue(value string) Value
```

StringValue returns a new Value for a string.

```go
func TimeValue(v time.Time) Value
```

TimeValue returns a Value for a time.Time. It discards the monotonic portion.

```go
func Uint64Value(v uint64) Value
```

Uint64Value returns a Value for a uint64.

```go
func (v Value) Any() any
```

Any returns v's value as an any.

```go
func (v Value) Bool() bool
```

Bool returns v's value as a bool. It panics if v is not a bool.

```go
func (v Value) Duration() time.Duration
```

Duration returns v's value as a time.Duration. It panics if v is not a time.Duration.

```go
func (v Value) Equal(w Value) bool
```

Equal reports whether v and w represent the same Go value.

```go
func (v Value) Float64() float64
```

Float64 returns v's value as a float64. It panics if v is not a float64.

```go
func (v Value) Group() []Attr
```

Group returns v's value as a []Attr. It panics if v's Kind is not KindGroup.

```go
func (v Value) Int64() int64
```

Int64 returns v's value as an int64. It panics if v is not a signed integer.

```go
func (v Value) Kind() Kind
```

Kind returns v's Kind.

```go
func (v Value) LogValuer() LogValuer
```

LogValuer returns v's value as a LogValuer. It panics if v is not a LogValuer.

```go
func (v Value) Resolve() (rv Value)
```

Resolve repeatedly calls LogValue on v while it implements LogValuer, and returns the result. If v resolves to a group, the group's attributes' values are not recursively resolved. If the number of LogValue calls exceeds a threshold, a Value containing an error is returned. Resolve's return value is guaranteed not to be of Kind KindLogValuer.

```go
func (v Value) String() string
```

String returns Value's value as a string, formatted like fmt.Sprint. Unlike the methods Int64, Float64, and so on, which panic if v is of the wrong kind, String never panics.

```go
func (v Value) Time() time.Time
```

Time returns v's value as a time.Time. It panics if v is not a time.Time.

```go
func (v Value) Uint64() uint64
```

Uint64 returns v's value as a uint64. It panics if v is not an unsigned integer.

##   Source Files ¶
 View all Source files <https://cs.opensource.google/go/go/+/go1.26.3:src/log/slog>

- attr.go <https://cs.opensource.google/go/go/+/go1.26.3:src/log/slog/attr.go>
- doc.go <https://cs.opensource.google/go/go/+/go1.26.3:src/log/slog/doc.go>
- handler.go <https://cs.opensource.google/go/go/+/go1.26.3:src/log/slog/handler.go>
- json_handler.go <https://cs.opensource.google/go/go/+/go1.26.3:src/log/slog/json_handler.go>
- level.go <https://cs.opensource.google/go/go/+/go1.26.3:src/log/slog/level.go>
- logger.go <https://cs.opensource.google/go/go/+/go1.26.3:src/log/slog/logger.go>
- multi_handler.go <https://cs.opensource.google/go/go/+/go1.26.3:src/log/slog/multi_handler.go>
- record.go <https://cs.opensource.google/go/go/+/go1.26.3:src/log/slog/record.go>
- text_handler.go <https://cs.opensource.google/go/go/+/go1.26.3:src/log/slog/text_handler.go>
- value.go <https://cs.opensource.google/go/go/+/go1.26.3:src/log/slog/value.go>

##   Directories ¶
    Show internal   Expand all

internal

benchmarks  Package benchmarks contains benchmarks for slog.

Package benchmarks contains benchmarks for slog.    buffer  Package buffer provides a pool-allocated byte buffer.

Package buffer provides a pool-allocated byte buffer.

Click to show internal directories.
  Click to hide internal directories.

Close

**?** : This menu   **/** : Search site   **f** or **F** : Jump to   **y** or **Y**  : Canonical URL
  Close
