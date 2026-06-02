slog package - log/slog - Go Packages

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

## Links

-    Report a Vulnerability  <https://go.dev/security/policy>

##   Documentation ¶

Package slog provides structured logging, in which log records include a message, a severity level, and various other attributes expressed as key-value pairs.

It defines a type, Logger, which provides several methods (such as Logger.Info and Logger.Error) for reporting events of interest.

Each Logger is associated with a Handler. A Logger output method creates a Record from the method arguments and passes it to the Handler, which decides how to handle it. There is a default Logger accessible through top-level functions (such as Info and Error) that call the corresponding Logger methods.

A log record consists of a time, a level, a message, and a set of key-value pairs, where the keys are strings and the values may be of any type. As an example,

```go
slog.Info("hello", "count", 3)

```

creates a record containing the time of the call, a level of Info, the message "hello", and a single pair with key "count" and value 3.

The Info top-level function calls the Logger.Info method on the default Logger. In addition to Logger.Info, there are methods for Debug, Warn and Error levels. Besides these convenience methods for common levels, there is also a Logger.Log method which takes the level as an argument. Each of these methods has a corresponding top-level function that uses the default logger.

The default handler formats the log record's message, time, level, and attributes as a string and passes it to the log package.

```go
2022/11/08 15:28:26 INFO hello count=3

```

For more control over the output format, create a logger with a different handler. This statement uses New to create a new logger with a TextHandler that writes structured records in text form to standard error:

```go
logger := slog.New(slog.NewTextHandler(os.Stderr, nil))

```

TextHandler output is a sequence of key=value pairs, easily and unambiguously parsed by machine. This statement:

```go
logger.Info("hello", "count", 3)

```

produces this output:

```go
time=2022-11-08T15:28:26.000-05:00 level=INFO msg=hello count=3

```

The package also provides JSONHandler, whose output is line-delimited JSON:

```go
logger := slog.New(slog.NewJSONHandler(os.Stdout, nil))
logger.Info("hello", "count", 3)

```

produces this output:

```go
{"time":"2022-11-08T15:28:26.000000000-05:00","level":"INFO","msg":"hello","count":3}

```

Both TextHandler and JSONHandler can be configured with HandlerOptions. There are options for setting the minimum level (see Levels, below), displaying the source file and line of the log call, and modifying attributes before they are logged.

Setting a logger as the default with

```go
slog.SetDefault(logger)

```

will cause the top-level functions like Info to use it. SetDefault also updates the default logger used by the log package, so that existing applications that use log.Printf and related functions will send log records to the logger's handler without needing to be rewritten.

Some attributes are common to many log calls. For example, you may wish to include the URL or trace identifier of a server request with all log events arising from the request. Rather than repeat the attribute with every log call, you can use Logger.With to construct a new Logger containing the attributes:

```go
logger2 := logger.With("url", r.URL)

```

The arguments to With are the same key-value pairs used in Logger.Info. The result is a new Logger with the same handler as the original, but additional attributes that will appear in the output of every call.

#### Levels ¶

A Level is an integer representing the importance or severity of a log event. The higher the level, the more severe the event. This package defines constants for the most common levels, but any int can be used as a level.

In an application, you may wish to log messages only at a certain level or greater. One common configuration is to log messages at Info or higher levels, suppressing debug logging until it is needed. The built-in handlers can be configured with the minimum level to output by setting [HandlerOptions.Level]. The program's `main` function typically does this. The default value is LevelInfo.

Setting the [HandlerOptions.Level] field to a Level value fixes the handler's minimum level throughout its lifetime. Setting it to a LevelVar allows the level to be varied dynamically. A LevelVar holds a Level and is safe to read or write from multiple goroutines. To vary the level dynamically for an entire program, first initialize a global LevelVar:

```go
var programLevel = new(slog.LevelVar) // Info by default

```

Then use the LevelVar to construct a handler, and make it the default:

```go
h := slog.NewJSONHandler(os.Stderr, &slog.HandlerOptions{Level: programLevel})
slog.SetDefault(slog.New(h))

```

Now the program can change its logging level with a single statement:

```go
programLevel.Set(slog.LevelDebug)

```

#### Groups ¶

Attributes can be collected into groups. A group has a name that is used to qualify the names of its attributes. How this qualification is displayed depends on the handler. TextHandler separates the group and attribute names with a dot. JSONHandler treats each group as a separate JSON object, with the group name as the key.

Use Group to create a Group attribute from a name and a list of key-value pairs:

```go
slog.Group("request",
    "method", r.Method,
    "url", r.URL)

```

TextHandler would display this group as

```go
request.method=GET request.url=http://example.com

```

JSONHandler would display it as

```go
"request":{"method":"GET","url":"http://example.com"}

```

Use Logger.WithGroup to qualify all of a Logger's output with a group name. Calling WithGroup on a Logger results in a new Logger with the same Handler as the original, but with all its attributes qualified by the group name.

This can help prevent duplicate attribute keys in large systems, where subsystems might use the same keys. Pass each subsystem a different Logger with its own group name so that potential duplicates are qualified:

```go
logger := slog.Default().With("id", systemID)
parserLogger := logger.WithGroup("parser")
parseInput(input, parserLogger)

```

When parseInput logs with parserLogger, its keys will be qualified with "parser", so even if it uses the common key "id", the log line will have distinct keys.

#### Contexts ¶

Some handlers may wish to include information from the context.Context that is available at the call site. One example of such information is the identifier for the current span when tracing is enabled.

The Logger.Log and Logger.LogAttrs methods take a context as a first argument, as do their corresponding top-level functions.

Although the convenience methods on Logger (Info and so on) and the corresponding top-level functions do not take a context, the alternatives ending in "Context" do. For example,

```go
slog.InfoContext(ctx, "message")

```

It is recommended to pass a context to an output method if one is available.

#### Attrs and Values ¶

An Attr is a key-value pair. The Logger output methods accept Attrs as well as alternating keys and values. The statement

```go
slog.Info("hello", slog.Int("count", 3))

```

behaves the same as

```go
slog.Info("hello", "count", 3)

```

There are convenience constructors for Attr such as Int, String, and Bool for common types, as well as the function Any for constructing Attrs of any type.

The value part of an Attr is a type called Value. Like an [any], a Value can hold any Go value, but it can represent typical values, including all numbers and strings, without an allocation.

For the most efficient log output, use Logger.LogAttrs. It is similar to Logger.Log but accepts only Attrs, not alternating keys and values; this allows it, too, to avoid allocation.

The call

```go
logger.LogAttrs(ctx, slog.LevelInfo, "hello", slog.Int("count", 3))

```

is the most efficient way to achieve the same output as

```go
slog.InfoContext(ctx, "hello", "count", 3)

```

#### Customizing a type's logging behavior ¶

If a type implements the LogValuer interface, the Value returned from its LogValue method is used for logging. You can use this to control how values of the type appear in logs. For example, you can redact secret information like passwords, or gather a struct's fields in a Group. See the examples under LogValuer for details.

A LogValue method may return a Value that itself implements LogValuer. The Value.Resolve method handles these cases carefully, avoiding infinite loops and unbounded recursion. Handler authors and others may wish to use Value.Resolve instead of calling LogValue directly.

#### Wrapping output methods ¶

The logger functions use reflection over the call stack to find the file name and line number of the logging call within the application. This can produce incorrect source information for functions that wrap slog. For instance, if you define this function in file mylog.go:

```go
func Infof(logger *slog.Logger, format string, args ...any) {
    logger.Info(fmt.Sprintf(format, args...))
}

```

and you call it like this in main.go:

```go
Infof(slog.Default(), "hello, %s", "world")

```

then slog will report the source file as mylog.go, not main.go.

A correct implementation of Infof will obtain the source location (pc) and pass it to NewRecord. The Infof function in the package-level example called "wrapping" demonstrates how to do this.

#### Working with Records ¶

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

   View Source <https://cs.opensource.google/go/go/+/go1.26.3:src/log/slog/handler.go;l=176>
```go
const (
	// TimeKey is the key used by the built-in handlers for the time
	// when the log method is called. The associated Value is a [time.Time].
	TimeKey = "time"
	// LevelKey is the key used by the built-in handlers for the level
	// of the log call. The associated value is a [Level].
	LevelKey = "level"
	// MessageKey is the key used by the built-in handlers for the
	// message of the log call. The associated value is a string.
	MessageKey = "msg"
	// SourceKey is the key used by the built-in handlers for the source file
	// and line of the log call. The associated value is a *[Source].
	SourceKey = "source"
)
```

Keys for "built-in" attributes.

This section is empty.

```go
func Debug(msg string, args ...any)
```

Debug calls Logger.Debug on the default logger.

```go
func DebugContext(ctx context.Context, msg string, args ...any)
```

DebugContext calls Logger.DebugContext on the default logger.

```go
func Error(msg string, args ...any)
```

Error calls Logger.Error on the default logger.

```go
func ErrorContext(ctx context.Context, msg string, args ...any)
```

ErrorContext calls Logger.ErrorContext on the default logger.

```go
func Info(msg string, args ...any)
```

Info calls Logger.Info on the default logger.

```go
func InfoContext(ctx context.Context, msg string, args ...any)
```

InfoContext calls Logger.InfoContext on the default logger.

```go
func Log(ctx context.Context, level Level, msg string, args ...any)
```

Log calls Logger.Log on the default logger.

```go
func LogAttrs(ctx context.Context, level Level, msg string, attrs ...Attr)
```

LogAttrs calls Logger.LogAttrs on the default logger.

```go
func NewLogLogger(h Handler, level Level) *log.Logger
```

NewLogLogger returns a new log.Logger such that each call to its Output method dispatches a Record to the specified handler. The logger acts as a bridge from the older log API to newer structured logging handlers.

```go
func SetDefault(l *Logger)
```

SetDefault makes l the default Logger, which is used by the top-level functions Info, Debug and so on. After this call, output from the log package's default Logger (as with log.Print, etc.) will be logged using l's Handler, at a level controlled by SetLogLoggerLevel.

```go
func Warn(msg string, args ...any)
```

Warn calls Logger.Warn on the default logger.

```go
func WarnContext(ctx context.Context, msg string, args ...any)
```

WarnContext calls Logger.WarnContext on the default logger.

```go
type Attr struct {
	Key   string
	Value Value
}
```

An Attr is a key-value pair.

```go
func Any(key string, value any) Attr
```

Any returns an Attr for the supplied value. See AnyValue for how values are treated.

```go
func Bool(key string, v bool) Attr
```

Bool returns an Attr for a bool.

```go
func Duration(key string, v time.Duration) Attr
```

Duration returns an Attr for a time.Duration.

```go
func Float64(key string, v float64) Attr
```

Float64 returns an Attr for a floating-point number.

```go
func Group(key string, args ...any) Attr
```

Group returns an Attr for a Group Value. The first argument is the key; the remaining arguments are converted to Attrs as in Logger.Log.

Use Group to collect several key-value pairs under a single key on a log line, or as the result of LogValue in order to log a single value as multiple Attrs.

```go

package main

import (
	"log/slog"
	"net/http"
	"os"
	"time"
)

func main() {
	r, _ := http.NewRequest("GET", "localhost", nil)
	// ...

	logger := slog.New(
		slog.NewTextHandler(os.Stdout, &slog.HandlerOptions{
			ReplaceAttr: func(groups []string, a slog.Attr) slog.Attr {
				if a.Key == slog.TimeKey && len(groups) == 0 {
					return slog.Attr{}
				}
				return a
			},
		}),
	)
	logger.Info("finished",
		slog.Group("req",
			slog.String("method", r.Method),
			slog.String("url", r.URL.String())),
		slog.Int("status", http.StatusOK),
		slog.Duration("duration", time.Second))

}

```

```go
Output:
level=INFO msg=finished req.method=GET req.url=localhost status=200 duration=1s

```

 Share Format Run

```go
func GroupAttrs(key string, attrs ...Attr) Attr
```

GroupAttrs returns an Attr for a Group Value consisting of the given Attrs.

GroupAttrs is a more efficient version of Group that accepts only Attr values.

```go

package main

import (
	"context"
	"log/slog"
	"net/http"
	"os"
)

func main() {
	r, _ := http.NewRequest("POST", "localhost", http.NoBody)
	// ...

	logger := slog.New(
		slog.NewTextHandler(os.Stdout, &slog.HandlerOptions{
			Level: slog.LevelDebug,
			ReplaceAttr: func(groups []string, a slog.Attr) slog.Attr {
				if a.Key == slog.TimeKey && len(groups) == 0 {
					return slog.Attr{}
				}
				return a
			},
		}),
	)

	// Use []slog.Attr to accumulate attributes.
	attrs := []slog.Attr{slog.String("method", r.Method)}
	attrs = append(attrs, slog.String("url", r.URL.String()))

	if r.Method == "POST" {
		attrs = append(attrs, slog.Int("content-length", int(r.ContentLength)))
	}

	// Group the attributes under a key.
	logger.LogAttrs(context.Background(), slog.LevelInfo,
		"finished",
		slog.Int("status", http.StatusOK),
		slog.GroupAttrs("req", attrs...),
	)

	// Groups with empty keys are inlined.
	logger.LogAttrs(context.Background(), slog.LevelInfo,
		"finished",
		slog.Int("status", http.StatusOK),
		slog.GroupAttrs("", attrs...),
	)

}

```

```go
Output:
level=INFO msg=finished status=200 req.method=POST req.url=localhost req.content-length=0
level=INFO msg=finished status=200 method=POST url=localhost content-length=0

```

 Share Format Run

```go
func Int(key string, value int) Attr
```

Int converts an int to an int64 and returns an Attr with that value.

```go
func Int64(key string, value int64) Attr
```

Int64 returns an Attr for an int64.

```go
func String(key, value string) Attr
```

String returns an Attr for a string value.

```go
func Time(key string, v time.Time) Attr
```

Time returns an Attr for a time.Time. It discards the monotonic portion.

```go
func Uint64(key string, v uint64) Attr
```

Uint64 returns an Attr for a uint64.

```go
func (a Attr) Equal(b Attr) bool
```

Equal reports whether a and b have equal keys and values.

```go
func (a Attr) String() string
```

```go
type Handler interface {
	// Enabled reports whether the handler handles records at the given level.
	// The handler ignores records whose level is lower.
	// It is called early, before any arguments are processed,
	// to save effort if the log event should be discarded.
	// If called from a Logger method, the first argument is the context
	// passed to that method, or context.Background() if nil was passed
	// or the method does not take a context.
	// The context is passed so Enabled can use its values
	// to make a decision.
	Enabled(context.Context, Level) bool

	// Handle handles the Record.
	// It will only be called when Enabled returns true.
	// The Context argument is as for Enabled.
	// It is present solely to provide Handlers access to the context's values.
	// Canceling the context should not affect record processing.
	// (Among other things, log messages may be necessary to debug a
	// cancellation-related problem.)
	//
	// Handle methods that produce output should observe the following rules:
	//   - If r.Time is the zero time, ignore the time.
	//   - If r.PC is zero, ignore it.
	//   - Attr's values should be resolved.
	//   - If an Attr's key and value are both the zero value, ignore the Attr.
	//     This can be tested with attr.Equal(Attr{}).
	//   - If a group's key is empty, inline the group's Attrs.
	//   - If a group has no Attrs (even if it has a non-empty key),
	//     ignore it.
	//
	// [Logger] discards any errors from Handle. Wrap the Handle method to
	// process any errors from Handlers.
	Handle(context.Context, Record) error

	// WithAttrs returns a new Handler whose attributes consist of
	// both the receiver's attributes and the arguments.
	// The Handler owns the slice: it may retain, modify or discard it.
	WithAttrs(attrs []Attr) Handler

	// WithGroup returns a new Handler with the given group appended to
	// the receiver's existing groups.
	// The keys of all subsequent attributes, whether added by With or in a
	// Record, should be qualified by the sequence of group names.
	//
	// How this qualification happens is up to the Handler, so long as
	// this Handler's attribute keys differ from those of another Handler
	// with a different sequence of group names.
	//
	// A Handler should treat WithGroup as starting a Group of Attrs that ends
	// at the end of the log event. That is,
	//
	//     logger.WithGroup("s").LogAttrs(ctx, level, msg, slog.Int("a", 1), slog.Int("b", 2))
	//
	// should behave like
	//
	//     logger.LogAttrs(ctx, level, msg, slog.Group("s", slog.Int("a", 1), slog.Int("b", 2)))
	//
	// If the name is empty, WithGroup returns the receiver.
	WithGroup(name string) Handler
}
```

A Handler handles log records produced by a Logger.

A typical handler may print log records to standard error, or write them to a file or database, or perhaps augment them with additional attributes and pass them on to another handler.

Any of the Handler's methods may be called concurrently with itself or with other methods. It is the responsibility of the Handler to manage this concurrency.

Users of the slog package should not invoke Handler methods directly. They should use the methods of Logger instead.

Before implementing your own handler, consult https://go.dev/s/slog-handler-guide <https://go.dev/s/slog-handler-guide>.

This example shows how to Use a LevelHandler to change the level of an existing Handler while preserving its other behavior.

This example demonstrates increasing the log level to reduce a logger's output.

Another typical use would be to decrease the log level (to LevelDebug, say) during a part of the program that was suspected of containing a bug.

```go

package main

import (
	"context"
	"log/slog"
	"os"
)

// A LevelHandler wraps a Handler with an Enabled method
// that returns false for levels below a minimum.
type LevelHandler struct {
	level   slog.Leveler
	handler slog.Handler
}

// NewLevelHandler returns a LevelHandler with the given level.
// All methods except Enabled delegate to h.
func NewLevelHandler(level slog.Leveler, h slog.Handler) *LevelHandler {
	// Optimization: avoid chains of LevelHandlers.
	if lh, ok := h.(*LevelHandler); ok {
		h = lh.Handler()
	}
	return &LevelHandler{level, h}
}

// Enabled implements Handler.Enabled by reporting whether
// level is at least as large as h's level.
func (h *LevelHandler) Enabled(_ context.Context, level slog.Level) bool {
	return level >= h.level.Level()
}

// Handle implements Handler.Handle.
func (h *LevelHandler) Handle(ctx context.Context, r slog.Record) error {
	return h.handler.Handle(ctx, r)
}

// WithAttrs implements Handler.WithAttrs.
func (h *LevelHandler) WithAttrs(attrs []slog.Attr) slog.Handler {
	return NewLevelHandler(h.level, h.handler.WithAttrs(attrs))
}

// WithGroup implements Handler.WithGroup.
func (h *LevelHandler) WithGroup(name string) slog.Handler {
	return NewLevelHandler(h.level, h.handler.WithGroup(name))
}

// Handler returns the Handler wrapped by h.
func (h *LevelHandler) Handler() slog.Handler {
	return h.handler
}

// This example shows how to Use a LevelHandler to change the level of an
// existing Handler while preserving its other behavior.
//
// This example demonstrates increasing the log level to reduce a logger's
// output.
//
// Another typical use would be to decrease the log level (to LevelDebug, say)
// during a part of the program that was suspected of containing a bug.
func main() {
	removeTime := func(groups []string, a slog.Attr) slog.Attr {
		if a.Key == slog.TimeKey && len(groups) == 0 {
			return slog.Attr{}
		}
		return a
	}
	th := slog.NewTextHandler(os.Stdout, &slog.HandlerOptions{ReplaceAttr: removeTime})
	logger := slog.New(NewLevelHandler(slog.LevelWarn, th))
	logger.Info("not printed")
	logger.Warn("printed")

}

```

```go
Output:
level=WARN msg=printed

```

 Share Format Run

```go
var DiscardHandler Handler = discardHandler{}
```

DiscardHandler discards all log output. DiscardHandler.Enabled returns false for all Levels.

```go
type HandlerOptions struct {
	// AddSource causes the handler to compute the source code position
	// of the log statement and add a SourceKey attribute to the output.
	AddSource bool

	// Level reports the minimum record level that will be logged.
	// The handler discards records with lower levels.
	// If Level is nil, the handler assumes LevelInfo.
	// The handler calls Level.Level for each record processed;
	// to adjust the minimum level dynamically, use a LevelVar.
	Level Leveler

	// ReplaceAttr is called to rewrite each non-group attribute before it is logged.
	// The attribute's value has been resolved (see [Value.Resolve]).
	// If ReplaceAttr returns a zero Attr, the attribute is discarded.
	//
	// The built-in attributes with keys "time", "level", "source", and "msg"
	// are passed to this function, except that time is omitted
	// if zero, and source is omitted if AddSource is false.
	//
	// The first argument is a list of currently open groups that contain the
	// Attr. It must not be retained or modified. ReplaceAttr is never called
	// for Group attributes, only their contents. For example, the attribute
	// list
	//
	//     Int("a", 1), Group("g", Int("b", 2)), Int("c", 3)
	//
	// results in consecutive calls to ReplaceAttr with the following arguments:
	//
	//     nil, Int("a", 1)
	//     []string{"g"}, Int("b", 2)
	//     nil, Int("c", 3)
	//
	// ReplaceAttr can be used to change the default keys of the built-in
	// attributes, convert types (for example, to replace a `time.Time` with the
	// integer seconds since the Unix epoch), sanitize personal information, or
	// remove attributes from the output.
	ReplaceAttr func(groups []string, a Attr) Attr
}
```

HandlerOptions are options for a TextHandler or JSONHandler. A zero HandlerOptions consists entirely of default values.

This example demonstrates using custom log levels and custom log level names. In addition to the default log levels, it introduces Trace, Notice, and Emergency levels. The ReplaceAttr changes the way levels are printed for both the standard log levels and the custom log levels.

```go

package main

import (
	"context"
	"log/slog"
	"os"
)

func main() {
	// Exported constants from a custom logging package.
	const (
		LevelTrace     = slog.Level(-8)
		LevelDebug     = slog.LevelDebug
		LevelInfo      = slog.LevelInfo
		LevelNotice    = slog.Level(2)
		LevelWarning   = slog.LevelWarn
		LevelError     = slog.LevelError
		LevelEmergency = slog.Level(12)
	)

	th := slog.NewTextHandler(os.Stdout, &slog.HandlerOptions{
		// Set a custom level to show all log output. The default value is
		// LevelInfo, which would drop Debug and Trace logs.
		Level: LevelTrace,

		ReplaceAttr: func(groups []string, a slog.Attr) slog.Attr {
			// Remove time from the output for predictable test output.
			if a.Key == slog.TimeKey {
				return slog.Attr{}
			}

			// Customize the name of the level key and the output string, including
			// custom level values.
			if a.Key == slog.LevelKey {
				// Rename the level key from "level" to "sev".
				a.Key = "sev"

				// Handle custom level values.
				level := a.Value.Any().(slog.Level)

				// This could also look up the name from a map or other structure, but
				// this demonstrates using a switch statement to rename levels. For
				// maximum performance, the string values should be constants, but this
				// example uses the raw strings for readability.
				switch {
				case level < LevelDebug:
					a.Value = slog.StringValue("TRACE")
				case level < LevelInfo:
					a.Value = slog.StringValue("DEBUG")
				case level < LevelNotice:
					a.Value = slog.StringValue("INFO")
				case level < LevelWarning:
					a.Value = slog.StringValue("NOTICE")
				case level < LevelError:
					a.Value = slog.StringValue("WARNING")
				case level < LevelEmergency:
					a.Value = slog.StringValue("ERROR")
				default:
					a.Value = slog.StringValue("EMERGENCY")
				}
			}

			return a
		},
	})

	logger := slog.New(th)
	ctx := context.Background()
	logger.Log(ctx, LevelEmergency, "missing pilots")
	logger.Error("failed to start engines", "err", "missing fuel")
	logger.Warn("falling back to default value")
	logger.Log(ctx, LevelNotice, "all systems are running")
	logger.Info("initiating launch")
	logger.Debug("starting background job")
	logger.Log(ctx, LevelTrace, "button clicked")

}

```

```go
Output:
sev=EMERGENCY msg="missing pilots"
sev=ERROR msg="failed to start engines" err="missing fuel"
sev=WARNING msg="falling back to default value"
sev=NOTICE msg="all systems are running"
sev=INFO msg="initiating launch"
sev=DEBUG msg="starting background job"
sev=TRACE msg="button clicked"

```

 Share Format Run

```go
type JSONHandler struct {
	// contains filtered or unexported fields
}
```

JSONHandler is a Handler that writes Records to an io.Writer as line-delimited JSON objects.

```go
func NewJSONHandler(w io.Writer, opts *HandlerOptions) *JSONHandler
```

NewJSONHandler creates a JSONHandler that writes to w, using the given options. If opts is nil, the default options are used.

```go
func (h *JSONHandler) Enabled(_ context.Context, level Level) bool
```

Enabled reports whether the handler handles records at the given level. The handler ignores records whose level is lower.

```go
func (h *JSONHandler) Handle(_ context.Context, r Record) error
```

Handle formats its argument Record as a JSON object on a single line.

If the Record's time is zero, the time is omitted. Otherwise, the key is "time" and the value is output as with json.Marshal.

The level's key is "level" and its value is the result of calling Level.String.

If the AddSource option is set and source information is available, the key is "source", and the value is a record of type Source.

The message's key is "msg".

To modify these or other attributes, or remove them from the output, use [HandlerOptions.ReplaceAttr].

Values are formatted as with an encoding/json.Encoder with SetEscapeHTML(false), with two exceptions.

First, an Attr whose Value is of type error is formatted as a string, by calling its Error method. Only errors in Attrs receive this special treatment, not errors embedded in structs, slices, maps or other data structures that are processed by the encoding/json package.

Second, an encoding failure does not cause Handle to return an error. Instead, the error message is formatted as a string.

Each call to Handle results in a single serialized call to io.Writer.Write.

```go
func (h *JSONHandler) WithAttrs(attrs []Attr) Handler
```

WithAttrs returns a new JSONHandler whose attributes consists of h's attributes followed by attrs.

```go
func (h *JSONHandler) WithGroup(name string) Handler
```

```go
type Kind int
```

Kind is the kind of a Value.

```go
const (
	KindAny Kind = iota
	KindBool
	KindDuration
	KindFloat64
	KindInt64
	KindString
	KindTime
	KindUint64
	KindGroup
	KindLogValuer
)
```

```go
func (k Kind) String() string
```

```go
type Level int
```

A Level is the importance or severity of a log event. The higher the level, the more important or severe the event.

```go
const (
	LevelDebug Level = -4
	LevelInfo  Level = 0
	LevelWarn  Level = 4
	LevelError Level = 8
)
```

Names for common levels.

Level numbers are inherently arbitrary, but we picked them to satisfy three constraints. Any system can map them to another numbering scheme if it wishes.

First, we wanted the default level to be Info, Since Levels are ints, Info is the default value for int, zero.

Second, we wanted to make it easy to use levels to specify logger verbosity. Since a larger level means a more severe event, a logger that accepts events with smaller (or more negative) level means a more verbose logger. Logger verbosity is thus the negation of event severity, and the default verbosity of 0 accepts all events at least as severe as INFO.

Third, we wanted some room between levels to accommodate schemes with named levels between ours. For example, Google Cloud Logging defines a Notice level between Info and Warn. Since there are only a few of these intermediate levels, the gap between the numbers need not be large. Our gap of 4 matches OpenTelemetry's mapping. Subtracting 9 from an OpenTelemetry level in the DEBUG, INFO, WARN and ERROR ranges converts it to the corresponding slog Level range. OpenTelemetry also has the names TRACE and FATAL, which slog does not. But those OpenTelemetry levels can still be represented as slog Levels by using the appropriate integers.

```go
func SetLogLoggerLevel(level Level) (oldLevel Level)
```

SetLogLoggerLevel controls the level for the bridge to the log package.

Before SetDefault is called, slog top-level logging functions call the default log.Logger. In that mode, SetLogLoggerLevel sets the minimum level for those calls. By default, the minimum level is Info, so calls to Debug (as well as top-level logging calls at lower levels) will not be passed to the log.Logger. After calling

```go
slog.SetLogLoggerLevel(slog.LevelDebug)

```

calls to Debug will be passed to the log.Logger.

After SetDefault is called, calls to the default log.Logger are passed to the slog default handler. In that mode, SetLogLoggerLevel sets the level at which those calls are logged. That is, after calling

```go
slog.SetLogLoggerLevel(slog.LevelDebug)

```

A call to log.Printf will result in output at level LevelDebug.

SetLogLoggerLevel returns the previous value.

This example shows how to use slog.SetLogLoggerLevel to change the minimal level of the internal default handler for slog package before calling slog.SetDefault.

```go

package main

import (
	"log"
	"log/slog"
	"os"
)

func main() {
	defer log.SetFlags(log.Flags()) // revert changes after the example
	log.SetFlags(0)
	defer log.SetOutput(log.Writer()) // revert changes after the example
	log.SetOutput(os.Stdout)

	// Default logging level is slog.LevelInfo.
	log.Print("log debug") // log debug
	slog.Debug("debug")    // no output
	slog.Info("info")      // INFO info

	// Set the default logging level to slog.LevelDebug.
	currentLogLevel := slog.SetLogLoggerLevel(slog.LevelDebug)
	defer slog.SetLogLoggerLevel(currentLogLevel) // revert changes after the example

	log.Print("log debug") // log debug
	slog.Debug("debug")    // DEBUG debug
	slog.Info("info")      // INFO info

}

```

```go
Output:
log debug
INFO info
log debug
DEBUG debug
INFO info

```

 Share Format Run

This example shows how to use slog.SetLogLoggerLevel to change the minimal level of the internal writer that uses the custom handler for log package after calling slog.SetDefault.

```go

package main

import (
	"log"
	"log/slog"
	"os"
)

func main() {
	// Set the default logging level to slog.LevelError.
	currentLogLevel := slog.SetLogLoggerLevel(slog.LevelError)
	defer slog.SetLogLoggerLevel(currentLogLevel) // revert changes after the example

	defer slog.SetDefault(slog.Default()) // revert changes after the example
	removeTime := func(groups []string, a slog.Attr) slog.Attr {
		if a.Key == slog.TimeKey && len(groups) == 0 {
			return slog.Attr{}
		}
		return a
	}
	slog.SetDefault(slog.New(slog.NewTextHandler(os.Stdout, &slog.HandlerOptions{ReplaceAttr: removeTime})))

	log.Print("error") // level=ERROR msg=error

}

```

```go
Output:
level=ERROR msg=error

```

 Share Format Run

```go
func (l Level) AppendText(b []byte) ([]byte, error)
```

AppendText implements encoding.TextAppender by calling Level.String.

```go
func (l Level) Level() Level
```

Level returns the receiver. It implements Leveler.

```go
func (l Level) MarshalJSON() ([]byte, error)
```

MarshalJSON implements encoding/json.Marshaler by quoting the output of Level.String.

```go
func (l Level) MarshalText() ([]byte, error)
```

MarshalText implements encoding.TextMarshaler by calling Level.AppendText.

```go
func (l Level) String() string
```

String returns a name for the level. If the level has a name, then that name in uppercase is returned. If the level is between named values, then an integer is appended to the uppercased name. Examples:

```go
LevelWarn.String() => "WARN"
(LevelInfo+2).String() => "INFO+2"

```

```go
func (l *Level) UnmarshalJSON(data []byte) error
```

UnmarshalJSON implements encoding/json.Unmarshaler It accepts any string produced by Level.MarshalJSON, ignoring case. It also accepts numeric offsets that would result in a different string on output. For example, "Error-8" would marshal as "INFO".

```go
func (l *Level) UnmarshalText(data []byte) error
```

UnmarshalText implements encoding.TextUnmarshaler. It accepts any string produced by Level.MarshalText, ignoring case. It also accepts numeric offsets that would result in a different string on output. For example, "Error-8" would marshal as "INFO".

```go
type LevelVar struct {
	// contains filtered or unexported fields
}
```

A LevelVar is a Level variable, to allow a Handler level to change dynamically. It implements Leveler as well as a Set method, and it is safe for use by multiple goroutines. The zero LevelVar corresponds to LevelInfo.

```go
func (v *LevelVar) AppendText(b []byte) ([]byte, error)
```

AppendText implements encoding.TextAppender by calling Level.AppendText.

```go
func (v *LevelVar) Level() Level
```

Level returns v's level.

```go
func (v *LevelVar) MarshalText() ([]byte, error)
```

MarshalText implements encoding.TextMarshaler by calling LevelVar.AppendText.

```go
func (v *LevelVar) Set(l Level)
```

Set sets v's level to l.

```go
func (v *LevelVar) String() string
```

```go
func (v *LevelVar) UnmarshalText(data []byte) error
```

UnmarshalText implements encoding.TextUnmarshaler by calling Level.UnmarshalText.

```go
type Leveler interface {
	Level() Level
}
```

A Leveler provides a Level value.

As Level itself implements Leveler, clients typically supply a Level value wherever a Leveler is needed, such as in HandlerOptions. Clients who need to vary the level dynamically can provide a more complex Leveler implementation such as *LevelVar.

```go
type LogValuer interface {
	LogValue() Value
}
```

A LogValuer is any Go value that can convert itself into a Value for logging.

This mechanism may be used to defer expensive operations until they are needed, or to expand a single value into a sequence of components.

```go

package main

import "log/slog"

type Name struct {
	First, Last string
}

// LogValue implements slog.LogValuer.
// It returns a group containing the fields of
// the Name, so that they appear together in the log output.
func (n Name) LogValue() slog.Value {
	return slog.GroupValue(
		slog.String("first", n.First),
		slog.String("last", n.Last))
}

func main() {
	n := Name{"Perry", "Platypus"}
	slog.Info("mission accomplished", "agent", n)

	// JSON Output would look in part like:
	// {
	//     ...
	//     "msg": "mission accomplished",
	//     "agent": {
	//         "first": "Perry",
	//         "last": "Platypus"
	//     }
	// }
}

```

```go
Output:

```

 Share Format Run

This example demonstrates a Value that replaces itself with an alternative representation to avoid revealing secrets.

```go

package main

import (
	"log/slog"
	"os"
)

// A token is a secret value that grants permissions.
type Token string

// LogValue implements slog.LogValuer.
// It avoids revealing the token.
func (Token) LogValue() slog.Value {
	return slog.StringValue("REDACTED_TOKEN")
}

// This example demonstrates a Value that replaces itself
// with an alternative representation to avoid revealing secrets.
func main() {
	t := Token("shhhh!")
	removeTime := func(groups []string, a slog.Attr) slog.Attr {
		if a.Key == slog.TimeKey && len(groups) == 0 {
			return slog.Attr{}
		}
		return a
	}
	logger := slog.New(slog.NewTextHandler(os.Stdout, &slog.HandlerOptions{ReplaceAttr: removeTime}))
	logger.Info("permission granted", "user", "Perry", "token", t)

}

```

```go
Output:
level=INFO msg="permission granted" user=Perry token=REDACTED_TOKEN

```

 Share Format Run

```go
type Logger struct {
	// contains filtered or unexported fields
}
```

A Logger records structured information about each call to its Log, Debug, Info, Warn, and Error methods. For each call, it creates a Record and passes it to a Handler.

To create a new Logger, call New or a Logger method that begins "With".

```go
func Default() *Logger
```

Default returns the default Logger.

```go
func New(h Handler) *Logger
```

New creates a new Logger with the given non-nil Handler.

```go
func With(args ...any) *Logger
```

With calls Logger.With on the default logger.

```go
func (l *Logger) Debug(msg string, args ...any)
```

Debug logs at LevelDebug.

```go
func (l *Logger) DebugContext(ctx context.Context, msg string, args ...any)
```

DebugContext logs at LevelDebug with the given context.

```go
func (l *Logger) Enabled(ctx context.Context, level Level) bool
```

Enabled reports whether l emits log records at the given context and level.

```go
func (l *Logger) Error(msg string, args ...any)
```

Error logs at LevelError.

```go
func (l *Logger) ErrorContext(ctx context.Context, msg string, args ...any)
```

ErrorContext logs at LevelError with the given context.

```go
func (l *Logger) Handler() Handler
```

Handler returns l's Handler.

```go
func (l *Logger) Info(msg string, args ...any)
```

Info logs at LevelInfo.

```go
func (l *Logger) InfoContext(ctx context.Context, msg string, args ...any)
```

InfoContext logs at LevelInfo with the given context.

```go
func (l *Logger) Log(ctx context.Context, level Level, msg string, args ...any)
```

Log emits a log record with the current time and the given level and message. The Record's Attrs consist of the Logger's attributes followed by the Attrs specified by args.

The attribute arguments are processed as follows:

- If an argument is an Attr, it is used as is.
- If an argument is a string and this is not the last argument, the following argument is treated as the value and the two are combined into an Attr.
- Otherwise, the argument is treated as a value with key "!BADKEY".

```go
func (l *Logger) LogAttrs(ctx context.Context, level Level, msg string, attrs ...Attr)
```

LogAttrs is a more efficient version of Logger.Log that accepts only Attrs.

```go
func (l *Logger) Warn(msg string, args ...any)
```

Warn logs at LevelWarn.

```go
func (l *Logger) WarnContext(ctx context.Context, msg string, args ...any)
```

WarnContext logs at LevelWarn with the given context.

```go
func (l *Logger) With(args ...any) *Logger
```

With returns a Logger that includes the given attributes in each output operation. Arguments are converted to attributes as if by Logger.Log.

```go
func (l *Logger) WithGroup(name string) *Logger
```

WithGroup returns a Logger that starts a group, if name is non-empty. The keys of all attributes added to the Logger will be qualified by the given name. (How that qualification happens depends on the [Handler.WithGroup] method of the Logger's Handler.)

If name is empty, WithGroup returns the receiver.

```go
type MultiHandler struct {
	// contains filtered or unexported fields
}
```

MultiHandler is a Handler that invokes all the given Handlers. Its Enabled method reports whether any of the handlers' Enabled methods return true. Its Handle, WithAttrs and WithGroup methods call the corresponding method on each of the enabled handlers.

```go

package main

import (
	"bytes"
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

	var textBuf, jsonBuf bytes.Buffer
	textHandler := slog.NewTextHandler(&textBuf, &slog.HandlerOptions{ReplaceAttr: removeTime})
	jsonHandler := slog.NewJSONHandler(&jsonBuf, &slog.HandlerOptions{ReplaceAttr: removeTime})

	multiHandler := slog.NewMultiHandler(textHandler, jsonHandler)
	logger := slog.New(multiHandler)

	logger.Info("login",
		slog.String("name", "whoami"),
		slog.Int("id", 42),
	)

	os.Stdout.WriteString(textBuf.String())
	os.Stdout.WriteString(jsonBuf.String())

}

```

```go
Output:
level=INFO msg=login name=whoami id=42
{"level":"INFO","msg":"login","name":"whoami","id":42}

```

 Share Format Run

```go
func NewMultiHandler(handlers ...Handler) *MultiHandler
```

NewMultiHandler creates a MultiHandler with the given Handlers.

```go
func (h *MultiHandler) Enabled(ctx context.Context, l Level) bool
```

```go
func (h *MultiHandler) Handle(ctx context.Context, r Record) error
```

```go
func (h *MultiHandler) WithAttrs(attrs []Attr) Handler
```

```go
func (h *MultiHandler) WithGroup(name string) Handler
```

```go
type Record struct {
	// The time at which the output method (Log, Info, etc.) was called.
	Time time.Time

	// The log message.
	Message string

	// The level of the event.
	Level Level

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
