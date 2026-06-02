---
source_name: "External Linked Documentation"
source_url: "https://pkg.go.dev/log/slog"
source_path: "sources/raw/external/pkg-go-dev-log-slog-0557076f34.html"
license_ref: ""
---

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
