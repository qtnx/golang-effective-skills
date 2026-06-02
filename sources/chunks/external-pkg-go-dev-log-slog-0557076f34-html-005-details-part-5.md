---
source_name: "External Linked Documentation"
source_url: "https://pkg.go.dev/log/slog"
source_path: "sources/raw/external/pkg-go-dev-log-slog-0557076f34.html"
license_ref: ""
---

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
