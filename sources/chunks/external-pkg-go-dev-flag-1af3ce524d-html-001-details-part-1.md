---
source_name: "External Linked Documentation"
source_url: "https://pkg.go.dev/flag"
source_path: "sources/raw/external/pkg-go-dev-flag-1af3ce524d.html"
license_ref: ""
---

flag package - flag - Go Packages
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

##   Documentation ¶

Package flag implements command-line flag parsing.

#### Usage ¶

Define flags using flag.String, Bool, Int, etc.

This declares an integer flag, -n, stored in the pointer nFlag, with type *int:

```go
import "flag"
var nFlag = flag.Int("n", 1234, "help message for flag n")

```

If you like, you can bind the flag to a variable using the Var() functions.

```go
var flagvar int
func init() {
	flag.IntVar(&flagvar, "flagname", 1234, "help message for flagname")
}

```

Or you can create custom flags that satisfy the Value interface (with pointer receivers) and couple them to flag parsing by

```go
flag.Var(&flagVal, "name", "help message for flagname")

```

For such flags, the default value is just the initial value of the variable.

After all flags are defined, call

```go
flag.Parse()

```

to parse the command line into the defined flags.

Flags may then be used directly. If you're using the flags themselves, they are all pointers; if you bind to variables, they're values.

```go
fmt.Println("ip has value ", *ip)
fmt.Println("flagvar has value ", flagvar)

```

After parsing, the arguments following the flags are available as the slice flag.Args or individually as flag.Arg(i). The arguments are indexed from 0 through flag.NArg-1.

#### Command line flag syntax ¶

The following forms are permitted:

```go
-flag
--flag   // double dashes are also permitted
-flag=x
-flag x  // non-boolean flags only

```

One or two dashes may be used; they are equivalent. The last form is not permitted for boolean flags because the meaning of the command

```go
cmd -x *

```

where * is a Unix shell wildcard, will change if there is a file called 0, false, etc. You must use the -flag=false form to turn off a boolean flag.

Flag parsing stops just before the first non-flag argument ("-" is a non-flag argument) or after the terminator "--".

Integer flags accept 1234, 0664, 0x1234 and may be negative. Boolean flags may be:

```go
1, 0, t, f, T, F, true, false, TRUE, FALSE, True, False

```

Duration flags accept any input valid for time.ParseDuration.

The default set of command-line flags is controlled by top-level functions. The FlagSet type allows one to define independent sets of flags, such as to implement subcommands in a command-line interface. The methods of FlagSet are analogous to the top-level functions for the command-line flag set.

```go

// These examples demonstrate more intricate uses of the flag package.
package main

import (
	"errors"
	"flag"
	"fmt"
	"strings"
	"time"
)

// Example 1: A single string flag called "species" with default value "gopher".
var species = flag.String("species", "gopher", "the species we are studying")

// Example 2: Two flags sharing a variable, so we can have a shorthand.
// The order of initialization is undefined, so make sure both use the
// same default value. They must be set up with an init function.
var gopherType string

func init() {
	const (
		defaultGopher = "pocket"
		usage         = "the variety of gopher"
	)
	flag.StringVar(&gopherType, "gopher_type", defaultGopher, usage)
	flag.StringVar(&gopherType, "g", defaultGopher, usage+" (shorthand)")
}

// Example 3: A user-defined flag type, a slice of durations.
type interval []time.Duration

// String is the method to format the flag's value, part of the flag.Value interface.
// The String method's output will be used in diagnostics.
func (i *interval) String() string {
	return fmt.Sprint(*i)
}

// Set is the method to set the flag value, part of the flag.Value interface.
// Set's argument is a string to be parsed to set the flag.
// It's a comma-separated list, so we split it.
func (i *interval) Set(value string) error {
	// If we wanted to allow the flag to be set multiple times,
	// accumulating values, we would delete this if statement.
	// That would permit usages such as
	//	-deltaT 10s -deltaT 15s
	// and other combinations.
	if len(*i) > 0 {
		return errors.New("interval flag already set")
	}
	for _, dt := range strings.Split(value, ",") {
		duration, err := time.ParseDuration(dt)
		if err != nil {
			return err
		}
		*i = append(*i, duration)
	}
	return nil
}

// Define a flag to accumulate durations. Because it has a special type,
// we need to use the Var function and therefore create the flag during
// init.

var intervalFlag interval

func init() {
	// Tie the command-line flag to the intervalFlag variable and
	// set a usage message.
	flag.Var(&intervalFlag, "deltaT", "comma-separated list of intervals to use between events")
}

func main() {
	// All the interesting pieces are with the variables declared above, but
	// to enable the flag package to see the flags defined there, one must
	// execute, typically at the start of main (not init!):
	//	flag.Parse()
	// We don't call it here because this code is a function called "Example"
	// that is part of the testing suite for the package, which has already
	// parsed the flags. When viewed at pkg.go.dev, however, the function is
	// renamed to "main" and it could be run as a standalone example.
}

```

```go
Output:

```

Share Format Run

- Variables
-  func Arg(i int) string
-  func Args() []string
-  func Bool(name string, value bool, usage string) *bool
-  func BoolFunc(name, usage string, fn func(string) error)
-  func BoolVar(p *bool, name string, value bool, usage string)
-  func Duration(name string, value time.Duration, usage string) *time.Duration
-  func DurationVar(p *time.Duration, name string, value time.Duration, usage string)
-  func Float64(name string, value float64, usage string) *float64
-  func Float64Var(p *float64, name string, value float64, usage string)
-  func Func(name, usage string, fn func(string) error)
-  func Int(name string, value int, usage string) *int
-  func Int64(name string, value int64, usage string) *int64
-  func Int64Var(p *int64, name string, value int64, usage string)
-  func IntVar(p *int, name string, value int, usage string)
-  func NArg() int
-  func NFlag() int
-  func Parse()
-  func Parsed() bool
-  func PrintDefaults()
-  func Set(name, value string) error
-  func String(name string, value string, usage string) *string
-  func StringVar(p *string, name string, value string, usage string)
-  func TextVar(p encoding.TextUnmarshaler, name string, value encoding.TextMarshaler, ...)
-  func Uint(name string, value uint, usage string) *uint
-  func Uint64(name string, value uint64, usage string) *uint64
-  func Uint64Var(p *uint64, name string, value uint64, usage string)
-  func UintVar(p *uint, name string, value uint, usage string)
-  func UnquoteUsage(flag *Flag) (name string, usage string)
-  func Var(value Value, name string, usage string)
-  func Visit(fn func(*Flag))
-  func VisitAll(fn func(*Flag))
-  type ErrorHandling
-  type Flag
-
-  func Lookup(name string) *Flag

-  type FlagSet
-
-  func NewFlagSet(name string, errorHandling ErrorHandling) *FlagSet

-
-  func (f *FlagSet) Arg(i int) string
-  func (f *FlagSet) Args() []string
-  func (f *FlagSet) Bool(name string, value bool, usage string) *bool
-  func (f *FlagSet) BoolFunc(name, usage string, fn func(string) error)
-  func (f *FlagSet) BoolVar(p *bool, name string, value bool, usage string)
-  func (f *FlagSet) Duration(name string, value time.Duration, usage string) *time.Duration
-  func (f *FlagSet) DurationVar(p *time.Duration, name string, value time.Duration, usage string)
-  func (f *FlagSet) ErrorHandling() ErrorHandling
-  func (f *FlagSet) Float64(name string, value float64, usage string) *float64
-  func (f *FlagSet) Float64Var(p *float64, name string, value float64, usage string)
-  func (f *FlagSet) Func(name, usage string, fn func(string) error)
-  func (f *FlagSet) Init(name string, errorHandling ErrorHandling)
-  func (f *FlagSet) Int(name string, value int, usage string) *int
-  func (f *FlagSet) Int64(name string, value int64, usage string) *int64
-  func (f *FlagSet) Int64Var(p *int64, name string, value int64, usage string)
-  func (f *FlagSet) IntVar(p *int, name string, value int, usage string)
-  func (f *FlagSet) Lookup(name string) *Flag
-  func (f *FlagSet) NArg() int
-  func (f *FlagSet) NFlag() int
-  func (f *FlagSet) Name() string
-  func (f *FlagSet) Output() io.Writer
-  func (f *FlagSet) Parse(arguments []string) error
-  func (f *FlagSet) Parsed() bool
-  func (f *FlagSet) PrintDefaults()
-  func (f *FlagSet) Set(name, value string) error
-  func (f *FlagSet) SetOutput(output io.Writer)
-  func (f *FlagSet) String(name string, value string, usage string) *string
-  func (f *FlagSet) StringVar(p *string, name string, value string, usage string)
-  func (f *FlagSet) TextVar(p encoding.TextUnmarshaler, name string, value encoding.TextMarshaler, ...)
-  func (f *FlagSet) Uint(name string, value uint, usage string) *uint
-  func (f *FlagSet) Uint64(name string, value uint64, usage string) *uint64
-  func (f *FlagSet) Uint64Var(p *uint64, name string, value uint64, usage string)
-  func (f *FlagSet) UintVar(p *uint, name string, value uint, usage string)
-  func (f *FlagSet) Var(value Value, name string, usage string)
-  func (f *FlagSet) Visit(fn func(*Flag))
-  func (f *FlagSet) VisitAll(fn func(*Flag))

-  type Getter
-  type Value

- Package
- BoolFunc
- FlagSet
- Func
- TextVar
- Value

This section is empty.

View Source <https://cs.opensource.google/go/go/+/go1.26.3:src/flag/flag.go;l=101>
```go
var ErrHelp = errors.New("flag: help requested")
```

ErrHelp is the error returned if the -help or -h flag is invoked but no such flag is defined.
  View Source <https://cs.opensource.google/go/go/+/go1.26.3:src/flag/flag.go;l=706>
```go
var Usage = func() {
	fmt.Fprintf(CommandLine.Output(), "Usage of %s:\n", os.Args[0])
	PrintDefaults()
}
```
