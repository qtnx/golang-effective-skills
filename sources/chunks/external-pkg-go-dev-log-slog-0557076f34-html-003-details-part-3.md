---
source_name: "External Linked Documentation"
source_url: "https://pkg.go.dev/log/slog"
source_path: "sources/raw/external/pkg-go-dev-log-slog-0557076f34.html"
license_ref: ""
---

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
