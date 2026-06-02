glog package - github.com/golang/glog - Go Packages

## Details

-     Valid go.mod <https://github.com/golang/glog/tree/v1.2.5/go.mod> file
 The Go module system was introduced in Go 1.11 and is the official dependency management solution for Go.

-     Redistributable license
 Redistributable licenses place minimal restrictions on how software can be used, modified, and redistributed.

-     Tagged version
Modules with tagged versions give importers more predictable builds.

-     Stable version
When a project reaches major version v1 it is considered stable.

-  Learn more about best practices

## Repository
   github.com/golang/glog  <https://github.com/golang/glog>

## Links

-    Open Source Insights  <https://deps.dev/go/github.com%2Fgolang%2Fglog/v1.2.5>
-    Code Wiki

##   README ¶

### glog

 <https://pkg.go.dev/github.com/golang/glog>

Leveled execution logs for Go.

This is an efficient pure Go implementation of leveled logs in the manner of the open source C++ package _glog_ <https://github.com/google/glog>.

By binding methods to booleans it is possible to use the log package without paying the expense of evaluating the arguments to the log. Through the `-vmodule` flag, the package also provides fine-grained control over logging at the file level.

The comment from `glog.go` introduces the ideas:

Package _glog_ implements logging analogous to the Google-internal C++ INFO/ERROR/V setup. It provides the functions Info, Warning, Error, Fatal, plus formatting variants such as Infof. It also provides V-style loggingcontrolled by the `-v` and `-vmodule=file=2` flags.

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

The repository contains an open source version of the log package used inside Google. The master copy of the source lives inside Google, not here. The code in this repo is for export only and is not itself under development. Feature requests will be ignored.

Send bug reports to golang-nuts@googlegroups.com.

 Expand ▾ Collapse ▴

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

Infoln is equivalent to the global Infoln function, guarded by the value of v. See the documentation of V for usage.

##   Source Files ¶
 View all Source files <https://github.com/golang/glog/tree/v1.2.5>

- glog.go <https://github.com/golang/glog/blob/v1.2.5/glog.go>
- glog_file.go <https://github.com/golang/glog/blob/v1.2.5/glog_file.go>
- glog_file_linux.go <https://github.com/golang/glog/blob/v1.2.5/glog_file_linux.go>
- glog_file_nonwindows.go <https://github.com/golang/glog/blob/v1.2.5/glog_file_nonwindows.go>
- glog_flags.go <https://github.com/golang/glog/blob/v1.2.5/glog_flags.go>

##   Directories ¶
    Show internal   Expand all

        internal      logsink

      stackdump  Package stackdump provides wrappers for runtime.Stack and runtime.Callers with uniform support for skipping caller frames.

  Package stackdump provides wrappers for runtime.Stack and runtime.Callers with uniform support for skipping caller frames.

  Click to show internal directories.
  Click to hide internal directories.

  Close

     **?** : This menu   **/** : Search site   **f** or **F** : Jump to   **y** or **Y**  : Canonical URL
  Close
