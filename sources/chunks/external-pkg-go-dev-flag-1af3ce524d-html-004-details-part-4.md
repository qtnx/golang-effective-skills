---
source_name: "External Linked Documentation"
source_url: "https://pkg.go.dev/flag"
source_path: "sources/raw/external/pkg-go-dev-flag-1af3ce524d.html"
license_ref: ""
---

StringVar defines a string flag with specified name, default value, and usage string. The argument p points to a string variable in which to store the value of the flag.

```go
func (f *FlagSet) TextVar(p encoding.TextUnmarshaler, name string, value encoding.TextMarshaler, usage string)
```

TextVar defines a flag with a specified name, default value, and usage string. The argument p must be a pointer to a variable that will hold the value of the flag, and p must implement encoding.TextUnmarshaler. If the flag is used, the flag value will be passed to p's UnmarshalText method. The type of the default value must be the same as the type of p.

```go
func (f *FlagSet) Uint(name string, value uint, usage string) *uint
```

Uint defines a uint flag with specified name, default value, and usage string. The return value is the address of a uint variable that stores the value of the flag.

```go
func (f *FlagSet) Uint64(name string, value uint64, usage string) *uint64
```

Uint64 defines a uint64 flag with specified name, default value, and usage string. The return value is the address of a uint64 variable that stores the value of the flag.

```go
func (f *FlagSet) Uint64Var(p *uint64, name string, value uint64, usage string)
```

Uint64Var defines a uint64 flag with specified name, default value, and usage string. The argument p points to a uint64 variable in which to store the value of the flag.

```go
func (f *FlagSet) UintVar(p *uint, name string, value uint, usage string)
```

UintVar defines a uint flag with specified name, default value, and usage string. The argument p points to a uint variable in which to store the value of the flag.

```go
func (f *FlagSet) Var(value Value, name string, usage string)
```

Var defines a flag with the specified name and usage string. The type and value of the flag are represented by the first argument, of type Value, which typically holds a user-defined implementation of Value. For instance, the caller could create a flag that turns a comma-separated string into a slice of strings by giving the slice the methods of Value; in particular, Set would decompose the comma-separated string into the slice.

```go
func (f *FlagSet) Visit(fn func(*Flag))
```

Visit visits the flags in lexicographical order, calling fn for each. It visits only those flags that have been set.

```go
func (f *FlagSet) VisitAll(fn func(*Flag))
```

VisitAll visits the flags in lexicographical order, calling fn for each. It visits all flags, even those not set.

```go
type Getter interface {
	Value
	Get() any
}
```

Getter is an interface that allows the contents of a Value to be retrieved. It wraps the Value interface, rather than being part of it, because it appeared after Go 1 and its compatibility rules. All Value types provided by this package satisfy the Getter interface, except the type used by Func.

```go
type Value interface {
	String() string
	Set(string) error
}
```

Value is the interface to the dynamic value stored in a flag. (The default value is represented as a string.)

If a Value has an IsBoolFlag() bool method returning true, the command-line parser makes -name equivalent to -name=true rather than using the next command-line argument.

Set is called once, in command line order, for each flag present. The flag package may call the String method with a zero-valued receiver, such as a nil pointer.

```go

package main

import (
	"flag"
	"fmt"
	"net/url"
)

type URLValue struct {
	URL *url.URL
}

func (v URLValue) String() string {
	if v.URL != nil {
		return v.URL.String()
	}
	return ""
}

func (v URLValue) Set(s string) error {
	if u, err := url.Parse(s); err != nil {
		return err
	} else {
		*v.URL = *u
	}
	return nil
}

var u = &url.URL{}

func main() {
	fs := flag.NewFlagSet("ExampleValue", flag.ExitOnError)
	fs.Var(&URLValue{u}, "url", "URL to parse")

fs.Parse([]string{"-url", "https://golang.org/pkg/flag/"})
	fmt.Printf(`{scheme: %q, host: %q, path: %q}`, u.Scheme, u.Host, u.Path)

}

```

```go
Output:
{scheme: "https", host: "golang.org", path: "/pkg/flag/"}

```

Share Format Run

##   Source Files ¶
 View all Source files <https://cs.opensource.google/go/go/+/go1.26.3:src/flag>

- flag.go <https://cs.opensource.google/go/go/+/go1.26.3:src/flag/flag.go>

Click to show internal directories.
  Click to hide internal directories.

Close

**?** : This menu   **/** : Search site   **f** or **F** : Jump to   **y** or **Y**  : Canonical URL
  Close
