---
source_name: "External Linked Documentation"
source_url: "https://pkg.go.dev/github.com/golang/glog"
source_path: "sources/raw/external/pkg-go-dev-github-com-golang-glog-cd06075ea0.html"
license_ref: ""
---

##   Documentation ¶

Rendered for <https://go.dev/about#build-context>  linux/amd64 windows/amd64 darwin/amd64 js/wasm

Package glog implements logging analogous to the Google-internal C++ INFO/ERROR/V setup. It provides functions that have a name matched by regex:

```go
(Info|Warning|Error|Fatal)(Context)?(Depth)?(f)?

```

If Context is present, function takes context.Context argument. The context is used to pass through the Trace Context to log sinks that can make use of it. It is recommended to use the context variant of the functions over the non-context variants if a context is available to make sure the Trace Contexts are present in logs.

If Depth is present, this function calls log from a different depth in the call stack. This enables a callee to emit logs that use the callsite information of its caller or any other callers in the stack. When depth == 0, the original callee's line information is emitted. When depth > 0, depth frames are skipped in the call stack and the final frame is treated like the original callee to Info.

If 'f' is present, function formats according to a format specifier.

This package also provides V-style logging controlled by the -v and -vmodule=file=2 flags.

Basic examples:

```go
glog.Info("Prepare to repel boarders")

glog.Fatalf("Initialization failed: %s", err)

```

See the documentation for the V function for an explanation of these examples:

```go
if glog.V(2) {
	glog.Info("Starting transaction...")
}

glog.V(2).Infoln("Processed", nItems, "elements")

```

Log output is buffered and written periodically using Flush. Programs should call Flush before exiting to guarantee all log output is written.

By default, all log statements write to files in a temporary directory. This package provides several flags that modify this behavior. As a result, flag.Parse must be called before any logging is done.

```go
-logtostderr=false
	Logs are written to standard error instead of to files.
-alsologtostderr=false
	Logs are written to standard error as well as to files.
-stderrthreshold=ERROR
	Log events at or above this severity are logged to standard
	error as well as to files.
-log_dir=""
	Log files will be written to this directory instead of the
	default temporary directory.

```

Other flags provide aids to debugging.

```go
-log_backtrace_at=""
	A comma-separated list of file and line numbers holding a logging
	statement, such as
		-log_backtrace_at=gopherflakes.go:234
	A stack trace will be written to the Info log whenever execution
	hits one of these statements. (Unlike with -vmodule, the ".go"
	must be present.)
-v=0
	Enable V-leveled logging at the specified level.
-vmodule=""
	The syntax of the argument is a comma-separated list of pattern=N,
	where pattern is a literal file name (minus the ".go" suffix) or
	"glob" pattern and N is a V level. For instance,
		-vmodule=gopher*=3
	sets the V level to 3 in all Go files whose names begin with "gopher",
	and
		-vmodule=/path/to/glog/glog_test=1
	sets the V level to 1 in the Go file /path/to/glog/glog_test.go.
	If a glob pattern contains a slash, it is matched against the full path,
	and the file name. Otherwise, the pattern is
	matched only against the file's basename.  When both -vmodule and -v
	are specified, the -vmodule values take precedence for the specified
	modules.

```

- Variables
-  func CopyStandardLogTo(name string)
-  func Error(args ...any)
-  func ErrorContext(ctx context.Context, args ...any)
-  func ErrorContextDepth(ctx context.Context, depth int, args ...any)
-  func ErrorContextDepthf(ctx context.Context, depth int, format string, args ...any)
-  func ErrorContextf(ctx context.Context, format string, args ...any)
-  func ErrorDepth(depth int, args ...any)
-  func ErrorDepthf(depth int, format string, args ...any)
-  func Errorf(format string, args ...any)
-  func Errorln(args ...any)
-  func Exit(args ...any)
-  func ExitContext(ctx context.Context, args ...any)
-  func ExitContextDepth(ctx context.Context, depth int, args ...any)
-  func ExitContextDepthf(ctx context.Context, depth int, format string, args ...any)
-  func ExitContextf(ctx context.Context, format string, args ...any)
-  func ExitDepth(depth int, args ...any)
-  func ExitDepthf(depth int, format string, args ...any)
-  func Exitf(format string, args ...any)
-  func Exitln(args ...any)
-  func Fatal(args ...any)
-  func FatalContext(ctx context.Context, args ...any)
-  func FatalContextDepth(ctx context.Context, depth int, args ...any)
-  func FatalContextDepthf(ctx context.Context, depth int, format string, args ...any)
-  func FatalContextf(ctx context.Context, format string, args ...any)
-  func FatalDepth(depth int, args ...any)
-  func FatalDepthf(depth int, format string, args ...any)
-  func Fatalf(format string, args ...any)
-  func Fatalln(args ...any)
-  func Flush()
-  func Info(args ...any)
-  func InfoContext(ctx context.Context, args ...any)
-  func InfoContextDepth(ctx context.Context, depth int, args ...any)
-  func InfoContextDepthf(ctx context.Context, depth int, format string, args ...any)
-  func InfoContextf(ctx context.Context, format string, args ...any)
-  func InfoDepth(depth int, args ...any)
-  func InfoDepthf(depth int, format string, args ...any)
-  func Infof(format string, args ...any)
-  func Infoln(args ...any)
-  func Names(s string) ([]string, error)
-  func NewStandardLogger(name string) *stdLog.Logger
-  func Warning(args ...any)
-  func WarningContext(ctx context.Context, args ...any)
-  func WarningContextDepth(ctx context.Context, depth int, args ...any)
-  func WarningContextDepthf(ctx context.Context, depth int, format string, args ...any)
-  func WarningContextf(ctx context.Context, format string, args ...any)
-  func WarningDepth(depth int, args ...any)
-  func WarningDepthf(depth int, format string, args ...any)
-  func Warningf(format string, args ...any)
-  func Warningln(args ...any)
-  type Level
-
-  func (l *Level) Get() any
-  func (l *Level) Set(value string) error
-  func (l *Level) String() string

-  type OutputStats
-
-  func (s *OutputStats) Bytes() int64
-  func (s *OutputStats) Lines() int64

-  type Verbose
-
-  func V(level Level) Verbose
-  func VDepth(depth int, level Level) Verbose

-
-  func (v Verbose) Info(args ...any)
-  func (v Verbose) InfoContext(ctx context.Context, args ...any)
-  func (v Verbose) InfoContextDepth(ctx context.Context, depth int, args ...any)
-  func (v Verbose) InfoContextDepthf(ctx context.Context, depth int, format string, args ...any)
-  func (v Verbose) InfoContextf(ctx context.Context, format string, args ...any)
-  func (v Verbose) InfoDepth(depth int, args ...any)
-  func (v Verbose) InfoDepthf(depth int, format string, args ...any)
-  func (v Verbose) Infof(format string, args ...any)
-  func (v Verbose) Infoln(args ...any)

This section is empty.

View Source <https://github.com/golang/glog/blob/v1.2.5/glog.go#L127>
```go
var ErrNoLog = errors.New("log file not yet created")
```

ErrNoLog is the error we return if no log file has yet been created for the specified log type.
  View Source <https://github.com/golang/glog/blob/v1.2.5/glog.go#L123>
```go
var MaxSize uint64 = 1024 * 1024 * 1800
```

MaxSize is the maximum size of a log file in bytes.
  View Source <https://github.com/golang/glog/blob/v1.2.5/glog.go#L147>
```go
var Stats struct {
	Info, Warning, Error OutputStats
}
```

Stats tracks the number of lines of output and number of bytes per severity level. Values must be read with atomic.LoadInt64.

```go
func CopyStandardLogTo(name string)
```

CopyStandardLogTo arranges for messages written to the Go "log" package's default logs to also appear in the Google logs for the named and lower severities. Subsequent changes to the standard log's default output location or format may break this behavior.

Valid names are "INFO", "WARNING", "ERROR", and "FATAL". If the name is not recognized, CopyStandardLogTo panics.

```go
func Error(args ...any)
```

Error logs to the ERROR, WARNING, and INFO logs. Arguments are handled in the manner of fmt.Print; a newline is appended if missing.

```go
func ErrorContext(ctx context.Context, args ...any)
```

ErrorContext is like Error, but with an extra context.Context parameter. The context is used to pass the Trace Context to log sinks.

```go
func ErrorContextDepth(ctx context.Context, depth int, args ...any)
```

ErrorContextDepth is like ErrorDepth, but with an extra context.Context parameter. The context is used to pass the Trace Context to log sinks.

```go
func ErrorContextDepthf(ctx context.Context, depth int, format string, args ...any)
```

ErrorContextDepthf is like ErrorDepthf, but with an extra context.Context parameter. The context is used to pass the Trace Context to log sinks.

```go
func ErrorContextf(ctx context.Context, format string, args ...any)
```

ErrorContextf is like Errorf, but with an extra context.Context parameter. The context is used to pass the Trace Context to log sinks.

```go
func ErrorDepth(depth int, args ...any)
```

ErrorDepth acts as Error but uses depth to determine which call frame to log. ErrorDepth(0, "msg") is the same as Error("msg").

```go
func ErrorDepthf(depth int, format string, args ...any)
```

ErrorDepthf acts as Errorf but uses depth to determine which call frame to log. ErrorDepthf(0, "msg") is the same as Errorf("msg").

```go
func Errorf(format string, args ...any)
```

Errorf logs to the ERROR, WARNING, and INFO logs. Arguments are handled in the manner of fmt.Printf; a newline is appended if missing.

```go
func Errorln(args ...any)
```

Errorln logs to the ERROR, WARNING, and INFO logs. Arguments are handled in the manner of fmt.Println; a newline is appended if missing.

```go
func Exit(args ...any)
```

Exit logs to the FATAL, ERROR, WARNING, and INFO logs, then calls os.Exit(1). Arguments are handled in the manner of fmt.Print; a newline is appended if missing.

```go
func ExitContext(ctx context.Context, args ...any)
```

ExitContext is like Exit, but with an extra context.Context parameter. The context is used to pass the Trace Context to log sinks.

```go
func ExitContextDepth(ctx context.Context, depth int, args ...any)
```

ExitContextDepth is like ExitDepth, but with an extra context.Context parameter. The context is used to pass the Trace Context to log sinks.

```go
func ExitContextDepthf(ctx context.Context, depth int, format string, args ...any)
```

ExitContextDepthf is like ExitDepthf, but with an extra context.Context parameter. The context is used to pass the Trace Context to log sinks.

```go
func ExitContextf(ctx context.Context, format string, args ...any)
```

ExitContextf is like Exitf, but with an extra context.Context parameter. The context is used to pass the Trace Context to log sinks.

```go
func ExitDepth(depth int, args ...any)
```

ExitDepth acts as Exit but uses depth to determine which call frame to log. ExitDepth(0, "msg") is the same as Exit("msg").

```go
func ExitDepthf(depth int, format string, args ...any)
```

ExitDepthf acts as Exitf but uses depth to determine which call frame to log. ExitDepthf(0, "msg") is the same as Exitf("msg").
