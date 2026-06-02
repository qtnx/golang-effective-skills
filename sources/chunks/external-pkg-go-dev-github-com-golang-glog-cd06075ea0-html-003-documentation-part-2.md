---
source_name: "External Linked Documentation"
source_url: "https://pkg.go.dev/github.com/golang/glog"
source_path: "sources/raw/external/pkg-go-dev-github-com-golang-glog-cd06075ea0.html"
license_ref: ""
---

##   Documentation ¶

```go
func Exitf(format string, args ...any)
```

Exitf logs to the FATAL, ERROR, WARNING, and INFO logs, then calls os.Exit(1). Arguments are handled in the manner of fmt.Printf; a newline is appended if missing.

```go
func Exitln(args ...any)
```

Exitln logs to the FATAL, ERROR, WARNING, and INFO logs, then calls os.Exit(1).

```go
func Fatal(args ...any)
```

Fatal logs to the FATAL, ERROR, WARNING, and INFO logs, including a stack trace of all running goroutines, then calls os.Exit(2). Arguments are handled in the manner of fmt.Print; a newline is appended if missing.

```go
func FatalContext(ctx context.Context, args ...any)
```

FatalContext is like Fatal, but with an extra context.Context parameter. The context is used to pass the Trace Context to log sinks.

```go
func FatalContextDepth(ctx context.Context, depth int, args ...any)
```

FatalContextDepth is like FatalDepth, but with an extra context.Context parameter. The context is used to pass the Trace Context to log sinks.

```go
func FatalContextDepthf(ctx context.Context, depth int, format string, args ...any)
```

FatalContextDepthf is like FatalDepthf, but with an extra context.Context parameter.

```go
func FatalContextf(ctx context.Context, format string, args ...any)
```

FatalContextf is like Fatalf, but with an extra context.Context parameter. The context is used to pass the Trace Context to log sinks.

```go
func FatalDepth(depth int, args ...any)
```

FatalDepth acts as Fatal but uses depth to determine which call frame to log. FatalDepth(0, "msg") is the same as Fatal("msg").

```go
func FatalDepthf(depth int, format string, args ...any)
```

FatalDepthf acts as Fatalf but uses depth to determine which call frame to log. FatalDepthf(0, "msg") is the same as Fatalf("msg").

```go
func Fatalf(format string, args ...any)
```

Fatalf logs to the FATAL, ERROR, WARNING, and INFO logs, including a stack trace of all running goroutines, then calls os.Exit(2). Arguments are handled in the manner of fmt.Printf; a newline is appended if missing.

```go
func Fatalln(args ...any)
```

Fatalln logs to the FATAL, ERROR, WARNING, and INFO logs, including a stack trace of all running goroutines, then calls os.Exit(2). Arguments are handled in the manner of fmt.Println; a newline is appended if missing.

```go
func Flush()
```

Flush flushes all pending log I/O.

```go
func Info(args ...any)
```

Info logs to the INFO log. Arguments are handled in the manner of fmt.Print; a newline is appended if missing.

```go
func InfoContext(ctx context.Context, args ...any)
```

InfoContext is like Info, but with an extra context.Context parameter. The context is used to pass the Trace Context to log sinks.

```go
func InfoContextDepth(ctx context.Context, depth int, args ...any)
```

InfoContextDepth is like InfoDepth, but with an extra context.Context parameter. The context is used to pass the Trace Context to log sinks.

```go
func InfoContextDepthf(ctx context.Context, depth int, format string, args ...any)
```

InfoContextDepthf is like InfoDepthf, but with an extra context.Context parameter. The context is used to pass the Trace Context to log sinks.

```go
func InfoContextf(ctx context.Context, format string, args ...any)
```

InfoContextf is like Infof, but with an extra context.Context parameter. The context is used to pass the Trace Context to log sinks.

```go
func InfoDepth(depth int, args ...any)
```

InfoDepth calls Info from a different depth in the call stack. This enables a callee to emit logs that use the callsite information of its caller or any other callers in the stack. When depth == 0, the original callee's line information is emitted. When depth > 0, depth frames are skipped in the call stack and the final frame is treated like the original callee to Info.

```go
func InfoDepthf(depth int, format string, args ...any)
```

InfoDepthf acts as InfoDepth but with format string.

```go
func Infof(format string, args ...any)
```

Infof logs to the INFO log. Arguments are handled in the manner of fmt.Printf; a newline is appended if missing.

```go
func Infoln(args ...any)
```

Infoln logs to the INFO log. Arguments are handled in the manner of fmt.Println; a newline is appended if missing.

```go
func Names(s string) ([]string, error)
```

Names returns the names of the log files holding the FATAL, ERROR, WARNING, or INFO logs. Returns ErrNoLog if the log for the given level doesn't exist (e.g. because no messages of that level have been written). This may return multiple names if the log type requested has rolled over.

```go
func NewStandardLogger(name string) *stdLog.Logger
```

NewStandardLogger returns a Logger that writes to the Google logs for the named and lower severities.

Valid names are "INFO", "WARNING", "ERROR", and "FATAL". If the name is not recognized, NewStandardLogger panics.

```go
func Warning(args ...any)
```

Warning logs to the WARNING and INFO logs. Arguments are handled in the manner of fmt.Print; a newline is appended if missing.

```go
func WarningContext(ctx context.Context, args ...any)
```

WarningContext is like Warning, but with an extra context.Context parameter. The context is used to pass the Trace Context to log sinks.

```go
func WarningContextDepth(ctx context.Context, depth int, args ...any)
```

WarningContextDepth is like WarningDepth, but with an extra context.Context parameter. The context is used to pass the Trace Context to log sinks.

```go
func WarningContextDepthf(ctx context.Context, depth int, format string, args ...any)
```

WarningContextDepthf is like WarningDepthf, but with an extra context.Context parameter. The context is used to pass the Trace Context to log sinks.

```go
func WarningContextf(ctx context.Context, format string, args ...any)
```

WarningContextf is like Warningf, but with an extra context.Context parameter. The context is used to pass the Trace Context to log sinks.

```go
func WarningDepth(depth int, args ...any)
```

WarningDepth acts as Warning but uses depth to determine which call frame to log. WarningDepth(0, "msg") is the same as Warning("msg").

```go
func WarningDepthf(depth int, format string, args ...any)
```

WarningDepthf acts as Warningf but uses depth to determine which call frame to log. WarningDepthf(0, "msg") is the same as Warningf("msg").

```go
func Warningf(format string, args ...any)
```

Warningf logs to the WARNING and INFO logs. Arguments are handled in the manner of fmt.Printf; a newline is appended if missing.

```go
func Warningln(args ...any)
```

Warningln logs to the WARNING and INFO logs. Arguments are handled in the manner of fmt.Println; a newline is appended if missing.

```go
type Level int32
```

Level specifies a level of verbosity for V logs. The -v flag is of type Level and should be modified only through the flag.Value interface.

```go
func (l *Level) Get() any
```

Get is part of the flag.Value interface.

```go
func (l *Level) Set(value string) error
```

Set is part of the flag.Value interface.

```go
func (l *Level) String() string
```

String is part of the flag.Value interface.

```go
type OutputStats struct {
	// contains filtered or unexported fields
}
```

OutputStats tracks the number of output lines and bytes written.

```go
func (s *OutputStats) Bytes() int64
```

Bytes returns the number of bytes written.

```go
func (s *OutputStats) Lines() int64
```

Lines returns the number of lines written.

```go
type Verbose bool
```

Verbose is a boolean type that implements Infof (like Printf) etc. See the documentation of V for more information.

```go
func V(level Level) Verbose
```

V reports whether verbosity at the call site is at least the requested level. The returned value is a boolean of type Verbose, which implements Info, Infoln and Infof. These methods will write to the Info log if called. Thus, one may write either

```go
if glog.V(2) { glog.Info("log this") }

```

or

```go
glog.V(2).Info("log this")

```

The second form is shorter but the first is cheaper if logging is off because it does not evaluate its arguments.

Whether an individual call to V generates a log record depends on the setting of the -v and --vmodule flags; both are off by default. If the level in the call to V is at most the value of -v, or of -vmodule for the source file containing the call, the V call will log.

```go
func VDepth(depth int, level Level) Verbose
```

VDepth acts as V but uses depth to determine which call frame to check vmodule for. VDepth(0, level) is the same as V(level).

```go
func (v Verbose) Info(args ...any)
```

Info is equivalent to the global Info function, guarded by the value of v. See the documentation of V for usage.

```go
func (v Verbose) InfoContext(ctx context.Context, args ...any)
```

InfoContext is equivalent to the global InfoContext function, guarded by the value of v. See the documentation of V for usage.

```go
func (v Verbose) InfoContextDepth(ctx context.Context, depth int, args ...any)
```

InfoContextDepth is equivalent to the global InfoContextDepth function, guarded by the value of v. See the documentation of V for usage.

```go
func (v Verbose) InfoContextDepthf(ctx context.Context, depth int, format string, args ...any)
```

InfoContextDepthf is equivalent to the global InfoContextDepthf function, guarded by the value of v. See the documentation of V for usage.

```go
func (v Verbose) InfoContextf(ctx context.Context, format string, args ...any)
```

InfoContextf is equivalent to the global InfoContextf function, guarded by the value of v. See the documentation of V for usage.

```go
func (v Verbose) InfoDepth(depth int, args ...any)
```

InfoDepth is equivalent to the global InfoDepth function, guarded by the value of v. See the documentation of V for usage.

```go
func (v Verbose) InfoDepthf(depth int, format string, args ...any)
```

InfoDepthf is equivalent to the global InfoDepthf function, guarded by the value of v. See the documentation of V for usage.

```go
func (v Verbose) Infof(format string, args ...any)
```

Infof is equivalent to the global Infof function, guarded by the value of v. See the documentation of V for usage.

```go
func (v Verbose) Infoln(args ...any)
```
