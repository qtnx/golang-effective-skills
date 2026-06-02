---
source_name: "External Linked Documentation"
source_url: "https://pkg.go.dev/log/slog"
source_path: "sources/raw/external/pkg-go-dev-log-slog-0557076f34.html"
license_ref: ""
---

Sometimes a Handler will need to modify a Record before passing it on to another Handler or backend. A Record contains a mixture of simple public fields (e.g. Time, Level, Message) and hidden fields that refer to state (such as attributes) indirectly. This means that modifying a simple copy of a Record (e.g. by calling Record.Add or Record.AddAttrs to add attributes) may have unexpected effects on the original. Before modifying a Record, use Record.Clone to create a copy that shares no state with the original, or create a new Record with NewRecord and build up its Attrs by traversing the old ones with Record.Attrs.

#### Performance considerations ¶

If profiling your application demonstrates that logging is taking significant time, the following suggestions may help.

If many log lines have a common attribute, use Logger.With to create a Logger with that attribute. The built-in handlers will format that attribute only once, at the call to Logger.With. The Handler interface is designed to allow that optimization, and a well-written Handler should take advantage of it.

The arguments to a log call are always evaluated, even if the log event is discarded. If possible, defer computation so that it happens only if the value is actually logged. For example, consider the call

```go
slog.Info("starting request", "url", r.URL.String())  // may compute String unnecessarily

```

The URL.String method will be called even if the logger discards Info-level events. Instead, pass the URL directly:

```go
slog.Info("starting request", "url", &r.URL) // calls URL.String only if needed

```

The built-in TextHandler will call its String method, but only if the log event is enabled. Avoiding the call to String also preserves the structure of the underlying value. For example JSONHandler emits the components of the parsed URL as a JSON object. If you want to avoid eagerly paying the cost of the String call without causing the handler to potentially inspect the structure of the value, wrap the value in a fmt.Stringer implementation that hides its Marshal methods.

You can also use the LogValuer interface to avoid unnecessary work in disabled log calls. Say you need to log some expensive value:

```go
slog.Debug("frobbing", "value", computeExpensiveValue(arg))

```

Even if this line is disabled, computeExpensiveValue will be called. To avoid that, define a type implementing LogValuer:

```go
type expensive struct { arg int }

func (e expensive) LogValue() slog.Value {
    return slog.AnyValue(computeExpensiveValue(e.arg))
}

```

Then use a value of that type in log calls:

```go
slog.Debug("frobbing", "value", expensive{arg})

```

Now computeExpensiveValue will only be called when the line is enabled.

The built-in handlers acquire a lock before calling io.Writer.Write to ensure that exactly one Record is written at a time in its entirety. Although each log record has a timestamp, the built-in handlers do not use that time to sort the written records. User-defined handlers are responsible for their own locking and sorting.

#### Writing a handler ¶

For a guide to writing a custom handler, see https://golang.org/s/slog-handler-guide <https://golang.org/s/slog-handler-guide>.

```go

package main

import (
	"log/slog"
	"os"
)

func main() {
	removeTime := func(groups []string, a slog.Attr) slog.Attr {
		if a.Key == slog.TimeKey && len(groups) == 0 {
			return slog.Attr{}
		}
		return a
	}
	// A slog.TextHandler can output log messages.
	logger1 := slog.New(slog.NewTextHandler(
		os.Stdout,
		&slog.HandlerOptions{ReplaceAttr: removeTime},
	))
	logger1.Info("message 1")

// A slog.DiscardHandler will discard all messages.
	logger2 := slog.New(slog.DiscardHandler)
	logger2.Info("message 2")

}

```

```go
Output:
level=INFO msg="message 1"

```

Share Format Run

```go

package main

import (
	"context"
	"fmt"
	"log/slog"
	"os"
	"path/filepath"
	"runtime"
	"time"
)

// Infof is an example of a user-defined logging function that wraps slog.
// The log record contains the source position of the caller of Infof.
func Infof(logger *slog.Logger, format string, args ...any) {
	if !logger.Enabled(context.Background(), slog.LevelInfo) {
		return
	}
	var pcs [1]uintptr
	runtime.Callers(2, pcs[:]) // skip [Callers, Infof]
	r := slog.NewRecord(time.Now(), slog.LevelInfo, fmt.Sprintf(format, args...), pcs[0])
	_ = logger.Handler().Handle(context.Background(), r)
}

func main() {
	replace := func(groups []string, a slog.Attr) slog.Attr {
		// Remove time.
		if a.Key == slog.TimeKey && len(groups) == 0 {
			return slog.Attr{}
		}
		// Remove the directory from the source's filename.
		if a.Key == slog.SourceKey {
			source := a.Value.Any().(*slog.Source)
			source.File = filepath.Base(source.File)
		}
		return a
	}
	logger := slog.New(slog.NewTextHandler(os.Stdout, &slog.HandlerOptions{AddSource: true, ReplaceAttr: replace}))
	Infof(logger, "message, %s", "formatted")

}

```

```go
Output:
level=INFO source=example_wrap_test.go:43 msg="message, formatted"

```

Share Format Run

- Constants
-  func Debug(msg string, args ...any)
-  func DebugContext(ctx context.Context, msg string, args ...any)
-  func Error(msg string, args ...any)
-  func ErrorContext(ctx context.Context, msg string, args ...any)
-  func Info(msg string, args ...any)
-  func InfoContext(ctx context.Context, msg string, args ...any)
-  func Log(ctx context.Context, level Level, msg string, args ...any)
-  func LogAttrs(ctx context.Context, level Level, msg string, attrs ...Attr)
-  func NewLogLogger(h Handler, level Level) *log.Logger
-  func SetDefault(l *Logger)
-  func Warn(msg string, args ...any)
-  func WarnContext(ctx context.Context, msg string, args ...any)
-  type Attr
-
-  func Any(key string, value any) Attr
-  func Bool(key string, v bool) Attr
-  func Duration(key string, v time.Duration) Attr
-  func Float64(key string, v float64) Attr
-  func Group(key string, args ...any) Attr
-  func GroupAttrs(key string, attrs ...Attr) Attr
-  func Int(key string, value int) Attr
-  func Int64(key string, value int64) Attr
-  func String(key, value string) Attr
-  func Time(key string, v time.Time) Attr
-  func Uint64(key string, v uint64) Attr

-
-  func (a Attr) Equal(b Attr) bool
-  func (a Attr) String() string

-  type Handler
-  type HandlerOptions
-  type JSONHandler
-
-  func NewJSONHandler(w io.Writer, opts *HandlerOptions) *JSONHandler

-
-  func (h *JSONHandler) Enabled(_ context.Context, level Level) bool
-  func (h *JSONHandler) Handle(_ context.Context, r Record) error
-  func (h *JSONHandler) WithAttrs(attrs []Attr) Handler
-  func (h *JSONHandler) WithGroup(name string) Handler

-  type Kind
-
-  func (k Kind) String() string

-  type Level
-
-  func SetLogLoggerLevel(level Level) (oldLevel Level)

-
-  func (l Level) AppendText(b []byte) ([]byte, error)
-  func (l Level) Level() Level
-  func (l Level) MarshalJSON() ([]byte, error)
-  func (l Level) MarshalText() ([]byte, error)
-  func (l Level) String() string
-  func (l *Level) UnmarshalJSON(data []byte) error
-  func (l *Level) UnmarshalText(data []byte) error

-  type LevelVar
-
-  func (v *LevelVar) AppendText(b []byte) ([]byte, error)
-  func (v *LevelVar) Level() Level
-  func (v *LevelVar) MarshalText() ([]byte, error)
-  func (v *LevelVar) Set(l Level)
-  func (v *LevelVar) String() string
-  func (v *LevelVar) UnmarshalText(data []byte) error

-  type Leveler
-  type LogValuer
-  type Logger
-
-  func Default() *Logger
-  func New(h Handler) *Logger
-  func With(args ...any) *Logger

-
-  func (l *Logger) Debug(msg string, args ...any)
-  func (l *Logger) DebugContext(ctx context.Context, msg string, args ...any)
-  func (l *Logger) Enabled(ctx context.Context, level Level) bool
-  func (l *Logger) Error(msg string, args ...any)
-  func (l *Logger) ErrorContext(ctx context.Context, msg string, args ...any)
-  func (l *Logger) Handler() Handler
-  func (l *Logger) Info(msg string, args ...any)
-  func (l *Logger) InfoContext(ctx context.Context, msg string, args ...any)
-  func (l *Logger) Log(ctx context.Context, level Level, msg string, args ...any)
-  func (l *Logger) LogAttrs(ctx context.Context, level Level, msg string, attrs ...Attr)
-  func (l *Logger) Warn(msg string, args ...any)
-  func (l *Logger) WarnContext(ctx context.Context, msg string, args ...any)
-  func (l *Logger) With(args ...any) *Logger
-  func (l *Logger) WithGroup(name string) *Logger

-  type MultiHandler
-
-  func NewMultiHandler(handlers ...Handler) *MultiHandler

-
-  func (h *MultiHandler) Enabled(ctx context.Context, l Level) bool
-  func (h *MultiHandler) Handle(ctx context.Context, r Record) error
-  func (h *MultiHandler) WithAttrs(attrs []Attr) Handler
-  func (h *MultiHandler) WithGroup(name string) Handler

-  type Record
-
-  func NewRecord(t time.Time, level Level, msg string, pc uintptr) Record

-
-  func (r *Record) Add(args ...any)
-  func (r *Record) AddAttrs(attrs ...Attr)
-  func (r Record) Attrs(f func(Attr) bool)
-  func (r Record) Clone() Record
-  func (r Record) NumAttrs() int
-  func (r Record) Source() *Source

-  type Source
-  type TextHandler
-
-  func NewTextHandler(w io.Writer, opts *HandlerOptions) *TextHandler

-
-  func (h *TextHandler) Enabled(_ context.Context, level Level) bool
-  func (h *TextHandler) Handle(_ context.Context, r Record) error
-  func (h *TextHandler) WithAttrs(attrs []Attr) Handler
-  func (h *TextHandler) WithGroup(name string) Handler

-  type Value
-
-  func AnyValue(v any) Value
-  func BoolValue(v bool) Value
-  func DurationValue(v time.Duration) Value
-  func Float64Value(v float64) Value
-  func GroupValue(as ...Attr) Value
-  func Int64Value(v int64) Value
-  func IntValue(v int) Value
-  func StringValue(value string) Value
-  func TimeValue(v time.Time) Value
-  func Uint64Value(v uint64) Value

-
-  func (v Value) Any() any
-  func (v Value) Bool() bool
-  func (v Value) Duration() time.Duration
-  func (v Value) Equal(w Value) bool
-  func (v Value) Float64() float64
-  func (v Value) Group() []Attr
-  func (v Value) Int64() int64
-  func (v Value) Kind() Kind
-  func (v Value) LogValuer() LogValuer
-  func (v Value) Resolve() (rv Value)
-  func (v Value) String() string
-  func (v Value) Time() time.Time
-  func (v Value) Uint64() uint64

- Package (DiscardHandler)
- Package (Wrapping)
- Group
- GroupAttrs
- Handler (LevelHandler)
- HandlerOptions (CustomLevels)
- LogValuer (Group)
- LogValuer (Secret)
- MultiHandler
- SetLogLoggerLevel (Log)
- SetLogLoggerLevel (Slog)
