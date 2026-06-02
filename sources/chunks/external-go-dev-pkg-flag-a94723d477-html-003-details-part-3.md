---
source_name: "External Linked Documentation"
source_url: "https://go.dev/pkg/flag/"
source_path: "sources/raw/external/go-dev-pkg-flag-a94723d477.html"
license_ref: ""
---

Var defines a flag with the specified name and usage string. The type and value of the flag are represented by the first argument, of type Value, which typically holds a user-defined implementation of Value. For instance, the caller could create a flag that turns a comma-separated string into a slice of strings by giving the slice the methods of Value; in particular, Set would decompose the comma-separated string into the slice.

```go
func Visit(fn func(*Flag))
```

Visit visits the command-line flags in lexicographical order, calling fn for each. It visits only those flags that have been set.

```go
func VisitAll(fn func(*Flag))
```

VisitAll visits the command-line flags in lexicographical order, calling fn for each. It visits all flags, even those not set.

```go
type ErrorHandling int
```

ErrorHandling defines how FlagSet.Parse behaves if the parse fails.

```go
const (
	ContinueOnError ErrorHandling = iota // Return a descriptive error.
	ExitOnError                          // Call os.Exit(2) or for -h/-help Exit(0).
	PanicOnError                         // Call panic with a descriptive error.
)
```

These constants cause FlagSet.Parse to behave as described if the parse fails.

```go
type Flag struct {
	Name     string // name as it appears on command line
	Usage    string // help message
	Value    Value  // value as set
	DefValue string // default value (as text); for usage message
}
```

A Flag represents the state of a flag.

```go
func Lookup(name string) *Flag
```

Lookup returns the Flag structure of the named command-line flag, returning nil if none exists.

```go
type FlagSet struct {
	// Usage is the function called when an error occurs while parsing flags.
	// The field is a function (not a method) that may be changed to point to
	// a custom error handler. What happens after Usage is called depends
	// on the ErrorHandling setting; for the command line, this defaults
	// to ExitOnError, which exits the program after calling Usage.
	Usage func()
	// contains filtered or unexported fields
}
```

A FlagSet represents a set of defined flags. The zero value of a FlagSet has no name and has ContinueOnError error handling.

Flag names must be unique within a FlagSet. An attempt to define a flag whose name is already in use will cause a panic.

```go

package main

import (
	"flag"
	"fmt"
	"time"
)

func main() {

start := func(args []string) {
		// A real program (not an example) would use flag.ExitOnError.
		fs := flag.NewFlagSet("start", flag.ContinueOnError)
		addr := fs.String("addr", ":8080", "`address` to listen on")
		if err := fs.Parse(args); err != nil {
			fmt.Printf("error: %s", err)
			return
		}
		fmt.Printf("starting server on %s\n", *addr)
	}

stop := func(args []string) {
		fs := flag.NewFlagSet("stop", flag.ContinueOnError)
		timeout := fs.Duration("timeout", time.Second, "stop timeout duration")
		if err := fs.Parse(args); err != nil {
			fmt.Printf("error: %s", err)
			return
		}
		fmt.Printf("stopping server (timeout=%v)\n", *timeout)
	}

main := func(args []string) {
		subArgs := args[2:] // Drop program name and command.
		switch args[1] {
		case "start":
			start(subArgs)
		case "stop":
			stop(subArgs)
		default:
			fmt.Printf("error: unknown command - %q\n", args[1])
			// In a real program (not an example) print to os.Stderr and exit the program with non-zero value.
		}
	}

main([]string{"httpd", "start", "-addr", ":9999"})
	main([]string{"httpd", "stop"})
	main([]string{"http", "start", "-log-level", "verbose"})

}

```

```go
Output:
starting server on :9999
stopping server (timeout=1s)
error: flag provided but not defined: -log-level

```

Share Format Run

```go
var CommandLine *FlagSet
```

CommandLine is the default set of command-line flags, parsed from os.Args. The top-level functions such as BoolVar, Arg, and so on are wrappers for the methods of CommandLine.

```go
func NewFlagSet(name string, errorHandling ErrorHandling) *FlagSet
```

NewFlagSet returns a new, empty flag set with the specified name and error handling property. If the name is not empty, it will be printed in the default usage message and in error messages.

```go
func (f *FlagSet) Arg(i int) string
```

Arg returns the i'th argument. Arg(0) is the first remaining argument after flags have been processed. Arg returns an empty string if the requested element does not exist.

```go
func (f *FlagSet) Args() []string
```

Args returns the non-flag arguments.

```go
func (f *FlagSet) Bool(name string, value bool, usage string) *bool
```

Bool defines a bool flag with specified name, default value, and usage string. The return value is the address of a bool variable that stores the value of the flag.

```go
func (f *FlagSet) BoolFunc(name, usage string, fn func(string) error)
```

BoolFunc defines a flag with the specified name and usage string without requiring values. Each time the flag is seen, fn is called with the value of the flag. If fn returns a non-nil error, it will be treated as a flag value parsing error.

```go
func (f *FlagSet) BoolVar(p *bool, name string, value bool, usage string)
```

BoolVar defines a bool flag with specified name, default value, and usage string. The argument p points to a bool variable in which to store the value of the flag.

```go
func (f *FlagSet) Duration(name string, value time.Duration, usage string) *time.Duration
```

Duration defines a time.Duration flag with specified name, default value, and usage string. The return value is the address of a time.Duration variable that stores the value of the flag. The flag accepts a value acceptable to time.ParseDuration.

```go
func (f *FlagSet) DurationVar(p *time.Duration, name string, value time.Duration, usage string)
```

DurationVar defines a time.Duration flag with specified name, default value, and usage string. The argument p points to a time.Duration variable in which to store the value of the flag. The flag accepts a value acceptable to time.ParseDuration.

```go
func (f *FlagSet) ErrorHandling() ErrorHandling
```

ErrorHandling returns the error handling behavior of the flag set.

```go
func (f *FlagSet) Float64(name string, value float64, usage string) *float64
```

Float64 defines a float64 flag with specified name, default value, and usage string. The return value is the address of a float64 variable that stores the value of the flag.

```go
func (f *FlagSet) Float64Var(p *float64, name string, value float64, usage string)
```

Float64Var defines a float64 flag with specified name, default value, and usage string. The argument p points to a float64 variable in which to store the value of the flag.

```go
func (f *FlagSet) Func(name, usage string, fn func(string) error)
```

Func defines a flag with the specified name and usage string. Each time the flag is seen, fn is called with the value of the flag. If fn returns a non-nil error, it will be treated as a flag value parsing error.

```go
func (f *FlagSet) Init(name string, errorHandling ErrorHandling)
```

Init sets the name and error handling property for a flag set. By default, the zero FlagSet uses an empty name and the ContinueOnError error handling policy.

```go
func (f *FlagSet) Int(name string, value int, usage string) *int
```

Int defines an int flag with specified name, default value, and usage string. The return value is the address of an int variable that stores the value of the flag.

```go
func (f *FlagSet) Int64(name string, value int64, usage string) *int64
```

Int64 defines an int64 flag with specified name, default value, and usage string. The return value is the address of an int64 variable that stores the value of the flag.

```go
func (f *FlagSet) Int64Var(p *int64, name string, value int64, usage string)
```

Int64Var defines an int64 flag with specified name, default value, and usage string. The argument p points to an int64 variable in which to store the value of the flag.

```go
func (f *FlagSet) IntVar(p *int, name string, value int, usage string)
```

IntVar defines an int flag with specified name, default value, and usage string. The argument p points to an int variable in which to store the value of the flag.

```go
func (f *FlagSet) Lookup(name string) *Flag
```

Lookup returns the Flag structure of the named flag, returning nil if none exists.

```go
func (f *FlagSet) NArg() int
```

NArg is the number of arguments remaining after flags have been processed.

```go
func (f *FlagSet) NFlag() int
```

NFlag returns the number of flags that have been set.

```go
func (f *FlagSet) Name() string
```

Name returns the name of the flag set.

```go
func (f *FlagSet) Output() io.Writer
```

Output returns the destination for usage and error messages. os.Stderr is returned if output was not set or was set to nil.

```go
func (f *FlagSet) Parse(arguments []string) error
```

Parse parses flag definitions from the argument list, which should not include the command name. Must be called after all flags in the FlagSet are defined and before flags are accessed by the program. The return value will be ErrHelp if -help or -h were set but not defined.

```go
func (f *FlagSet) Parsed() bool
```

Parsed reports whether f.Parse has been called.

```go
func (f *FlagSet) PrintDefaults()
```

PrintDefaults prints, to standard error unless configured otherwise, the default values of all defined command-line flags in the set. See the documentation for the global function PrintDefaults for more information.

```go
func (f *FlagSet) Set(name, value string) error
```

Set sets the value of the named flag.

```go
func (f *FlagSet) SetOutput(output io.Writer)
```

SetOutput sets the destination for usage and error messages. If output is nil, os.Stderr is used.

```go
func (f *FlagSet) String(name string, value string, usage string) *string
```

String defines a string flag with specified name, default value, and usage string. The return value is the address of a string variable that stores the value of the flag.

```go
func (f *FlagSet) StringVar(p *string, name string, value string, usage string)
```
