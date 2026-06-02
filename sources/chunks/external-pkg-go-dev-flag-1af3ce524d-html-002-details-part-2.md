---
source_name: "External Linked Documentation"
source_url: "https://pkg.go.dev/flag"
source_path: "sources/raw/external/pkg-go-dev-flag-1af3ce524d.html"
license_ref: ""
---

Usage prints a usage message documenting all defined command-line flags to CommandLine's output, which by default is os.Stderr. It is called when an error occurs while parsing flags. The function is a variable that may be changed to point to a custom function. By default it prints a simple header and calls PrintDefaults; for details about the format of the output and how to control it, see the documentation for PrintDefaults. Custom usage functions may choose to exit the program; by default exiting happens anyway as the command line's error handling strategy is set to ExitOnError.

```go
func Arg(i int) string
```

Arg returns the i'th command-line argument. Arg(0) is the first remaining argument after flags have been processed. Arg returns an empty string if the requested element does not exist.

```go
func Args() []string
```

Args returns the non-flag command-line arguments.

```go
func Bool(name string, value bool, usage string) *bool
```

Bool defines a bool flag with specified name, default value, and usage string. The return value is the address of a bool variable that stores the value of the flag.

```go
func BoolFunc(name, usage string, fn func(string) error)
```

BoolFunc defines a flag with the specified name and usage string without requiring values. Each time the flag is seen, fn is called with the value of the flag. If fn returns a non-nil error, it will be treated as a flag value parsing error.

```go

package main

import (
	"flag"
	"fmt"
	"os"
)

func main() {
	fs := flag.NewFlagSet("ExampleBoolFunc", flag.ContinueOnError)
	fs.SetOutput(os.Stdout)

fs.BoolFunc("log", "logs a dummy message", func(s string) error {
		fmt.Println("dummy message:", s)
		return nil
	})
	fs.Parse([]string{"-log"})
	fs.Parse([]string{"-log=0"})

}

```

```go
Output:
dummy message: true
dummy message: 0

```

Share Format Run

```go
func BoolVar(p *bool, name string, value bool, usage string)
```

BoolVar defines a bool flag with specified name, default value, and usage string. The argument p points to a bool variable in which to store the value of the flag.

```go
func Duration(name string, value time.Duration, usage string) *time.Duration
```

Duration defines a time.Duration flag with specified name, default value, and usage string. The return value is the address of a time.Duration variable that stores the value of the flag. The flag accepts a value acceptable to time.ParseDuration.

```go
func DurationVar(p *time.Duration, name string, value time.Duration, usage string)
```

DurationVar defines a time.Duration flag with specified name, default value, and usage string. The argument p points to a time.Duration variable in which to store the value of the flag. The flag accepts a value acceptable to time.ParseDuration.

```go
func Float64(name string, value float64, usage string) *float64
```

Float64 defines a float64 flag with specified name, default value, and usage string. The return value is the address of a float64 variable that stores the value of the flag.

```go
func Float64Var(p *float64, name string, value float64, usage string)
```

Float64Var defines a float64 flag with specified name, default value, and usage string. The argument p points to a float64 variable in which to store the value of the flag.

```go
func Func(name, usage string, fn func(string) error)
```

Func defines a flag with the specified name and usage string. Each time the flag is seen, fn is called with the value of the flag. If fn returns a non-nil error, it will be treated as a flag value parsing error.

```go

package main

import (
	"errors"
	"flag"
	"fmt"
	"net"
	"os"
)

func main() {
	fs := flag.NewFlagSet("ExampleFunc", flag.ContinueOnError)
	fs.SetOutput(os.Stdout)
	var ip net.IP
	fs.Func("ip", "`IP address` to parse", func(s string) error {
		ip = net.ParseIP(s)
		if ip == nil {
			return errors.New("could not parse IP")
		}
		return nil
	})
	fs.Parse([]string{"-ip", "127.0.0.1"})
	fmt.Printf("{ip: %v, loopback: %t}\n\n", ip, ip.IsLoopback())

// 256 is not a valid IPv4 component
	fs.Parse([]string{"-ip", "256.0.0.1"})
	fmt.Printf("{ip: %v, loopback: %t}\n\n", ip, ip.IsLoopback())

}

```

```go
Output:
{ip: 127.0.0.1, loopback: true}

invalid value "256.0.0.1" for flag -ip: could not parse IP
Usage of ExampleFunc:
  -ip IP address
    	IP address to parse
{ip: <nil>, loopback: false}

```

Share Format Run

```go
func Int(name string, value int, usage string) *int
```

Int defines an int flag with specified name, default value, and usage string. The return value is the address of an int variable that stores the value of the flag.

```go
func Int64(name string, value int64, usage string) *int64
```

Int64 defines an int64 flag with specified name, default value, and usage string. The return value is the address of an int64 variable that stores the value of the flag.

```go
func Int64Var(p *int64, name string, value int64, usage string)
```

Int64Var defines an int64 flag with specified name, default value, and usage string. The argument p points to an int64 variable in which to store the value of the flag.

```go
func IntVar(p *int, name string, value int, usage string)
```

IntVar defines an int flag with specified name, default value, and usage string. The argument p points to an int variable in which to store the value of the flag.

```go
func NArg() int
```

NArg is the number of arguments remaining after flags have been processed.

```go
func NFlag() int
```

NFlag returns the number of command-line flags that have been set.

```go
func Parse()
```

Parse parses the command-line flags from os.Args[1:]. Must be called after all flags are defined and before flags are accessed by the program.

```go
func Parsed() bool
```

Parsed reports whether the command-line flags have been parsed.

```go
func PrintDefaults()
```

PrintDefaults prints, to standard error unless configured otherwise, a usage message showing the default settings of all defined command-line flags. For an integer valued flag x, the default output has the form

```go
-x int
	usage-message-for-x (default 7)

```

The usage message will appear on a separate line for anything but a bool flag with a one-byte name. For bool flags, the type is omitted and if the flag name is one byte the usage message appears on the same line. The parenthetical default is omitted if the default is the zero value for the type. The listed type, here int, can be changed by placing a back-quoted name in the flag's usage string; the first such item in the message is taken to be a parameter name to show in the message and the back quotes are stripped from the message when displayed. For instance, given

```go
flag.String("I", "", "search `directory` for include files")

```

the output will be

```go
-I directory
	search directory for include files.

```

To change the destination for flag messages, call CommandLine.SetOutput.

```go
func Set(name, value string) error
```

Set sets the value of the named command-line flag.

```go
func String(name string, value string, usage string) *string
```

String defines a string flag with specified name, default value, and usage string. The return value is the address of a string variable that stores the value of the flag.

```go
func StringVar(p *string, name string, value string, usage string)
```

StringVar defines a string flag with specified name, default value, and usage string. The argument p points to a string variable in which to store the value of the flag.

```go
func TextVar(p encoding.TextUnmarshaler, name string, value encoding.TextMarshaler, usage string)
```

TextVar defines a flag with a specified name, default value, and usage string. The argument p must be a pointer to a variable that will hold the value of the flag, and p must implement encoding.TextUnmarshaler. If the flag is used, the flag value will be passed to p's UnmarshalText method. The type of the default value must be the same as the type of p.

```go

package main

import (
	"flag"
	"fmt"
	"net"
	"os"
)

func main() {
	fs := flag.NewFlagSet("ExampleTextVar", flag.ContinueOnError)
	fs.SetOutput(os.Stdout)
	var ip net.IP
	fs.TextVar(&ip, "ip", net.IPv4(192, 168, 0, 100), "`IP address` to parse")
	fs.Parse([]string{"-ip", "127.0.0.1"})
	fmt.Printf("{ip: %v}\n\n", ip)

// 256 is not a valid IPv4 component
	ip = nil
	fs.Parse([]string{"-ip", "256.0.0.1"})
	fmt.Printf("{ip: %v}\n\n", ip)

}

```

```go
Output:
{ip: 127.0.0.1}

invalid value "256.0.0.1" for flag -ip: invalid IP address: 256.0.0.1
Usage of ExampleTextVar:
  -ip IP address
    	IP address to parse (default 192.168.0.100)
{ip: <nil>}

```

Share Format Run

```go
func Uint(name string, value uint, usage string) *uint
```

Uint defines a uint flag with specified name, default value, and usage string. The return value is the address of a uint variable that stores the value of the flag.

```go
func Uint64(name string, value uint64, usage string) *uint64
```

Uint64 defines a uint64 flag with specified name, default value, and usage string. The return value is the address of a uint64 variable that stores the value of the flag.

```go
func Uint64Var(p *uint64, name string, value uint64, usage string)
```

Uint64Var defines a uint64 flag with specified name, default value, and usage string. The argument p points to a uint64 variable in which to store the value of the flag.

```go
func UintVar(p *uint, name string, value uint, usage string)
```

UintVar defines a uint flag with specified name, default value, and usage string. The argument p points to a uint variable in which to store the value of the flag.

```go
func UnquoteUsage(flag *Flag) (name string, usage string)
```

UnquoteUsage extracts a back-quoted name from the usage string for a flag and returns it and the un-quoted usage. Given "a `name` to show" it returns ("name", "a name to show"). If there are no back quotes, the name is an educated guess of the type of the flag's value, or the empty string if the flag is boolean.

```go
func Var(value Value, name string, usage string)
```
