---
source_name: "External Linked Documentation"
source_url: "https://pkg.go.dev/github.com/kylelemons/godebug/pretty"
source_path: "sources/raw/external/pkg-go-dev-github-com-kylelemons-godebug-pretty-3a16411fec.html"
license_ref: ""
---

pretty package - github.com/kylelemons/godebug/pretty - Go Packages
## Details

-     Valid go.mod <https://github.com/kylelemons/godebug/tree/v1.1.0/go.mod> file
 The Go module system was introduced in Go 1.11 and is the official dependency management solution for Go.

-     Redistributable license
 Redistributable licenses place minimal restrictions on how software can be used, modified, and redistributed.

-     Tagged version
Modules with tagged versions give importers more predictable builds.

-     Stable version
When a project reaches major version v1 it is considered stable.

-  Learn more about best practices

## Repository
   github.com/kylelemons/godebug  <https://github.com/kylelemons/godebug>

##   Documentation ¶

Package pretty pretty-prints Go structures.

This package uses reflection to examine a Go value and can print out in a nice, aligned fashion. It supports three modes (normal, compact, and extended) for advanced use.

See the Reflect and Print examples for what the output looks like.

- Variables
-  func Compare(a, b interface{}) string
-  func Fprint(w io.Writer, vals ...interface{}) (n int64, err error)
-  func Print(vals ...interface{})
-  func Sprint(vals ...interface{}) string
-  type Config
-
-  func (cfg *Config) Compare(a, b interface{}) string
-  func (cfg *Config) Fprint(w io.Writer, vals ...interface{}) (n int64, err error)
-  func (cfg *Config) Print(vals ...interface{})
-  func (cfg *Config) Sprint(vals ...interface{}) string

- Compare (Debugging)
- Compare (Testing)
- Compare (WithCycles)
- Config (CustomFormatter)
- Config (FmtFormatter)
- Config.Sprint
- Print
- Print (WithCycles)

This section is empty.

View Source <https://github.com/kylelemons/godebug/blob/v1.1.0/pretty/public.go#L79>
```go
var (
	// DefaultFormatter is the default set of overrides for stringification.
	DefaultFormatter = map[reflect.Type]interface{}{
		reflect.TypeOf(time.Time{}):          fmt.Sprint,
		reflect.TypeOf(net.IP{}):             fmt.Sprint,
		reflect.TypeOf((*error)(nil)).Elem(): fmt.Sprint,
	}

// CompareConfig is the default configuration used for Compare.
	CompareConfig = &Config{
		Diffable:          true,
		IncludeUnexported: true,
		Formatter:         DefaultFormatter,
	}

// DefaultConfig is the default configuration used for all other top-level functions.
	DefaultConfig = &Config{
		Formatter: DefaultFormatter,
	}

// CycleTracker is a convenience config for formatting and comparing recursive structures.
	CycleTracker = &Config{
		Diffable:    true,
		Formatter:   DefaultFormatter,
		TrackCycles: true,
	}
)
```

Default Config objects

```go
func Compare(a, b interface{}) string
```

Compare returns a string containing a line-by-line unified diff of the values in a and b, using the CompareConfig.

Each line in the output is prefixed with '+', '-', or ' ' to indicate which side it's from. Lines from the a side are marked with '-', lines from the b side are marked with '+' and lines that are the same on both sides are marked with ' '.

The comparison is based on the intentionally-untyped output of Print, and as such this comparison is pretty forviving. In particular, if the types of or types within in a and b are different but have the same representation, Compare will not indicate any differences between them.

```go

package main

import (
	"fmt"

"github.com/kylelemons/godebug/pretty"
)

func main() {
	type ShipManifest struct {
		Name     string
		Crew     map[string]string
		Androids int
		Stolen   bool
	}

reported := &ShipManifest{
		Name: "Spaceship Heart of Gold",
		Crew: map[string]string{
			"Zaphod Beeblebrox": "Galactic President",
			"Trillian":          "Human",
			"Ford Prefect":      "A Hoopy Frood",
			"Arthur Dent":       "Along for the Ride",
		},
		Androids: 1,
		Stolen:   true,
	}

expected := &ShipManifest{
		Name: "Spaceship Heart of Gold",
		Crew: map[string]string{
			"Trillian":      "Human",
			"Rowan Artosok": "Captain",
		},
		Androids: 1,
		Stolen:   false,
	}

fmt.Println(pretty.Compare(reported, expected))
}

```

```go
Output:
 {
  Name: "Spaceship Heart of Gold",
  Crew: {
-  Arthur Dent: "Along for the Ride",
-  Ford Prefect: "A Hoopy Frood",
+  Rowan Artosok: "Captain",
   Trillian: "Human",
-  Zaphod Beeblebrox: "Galactic President",
  },
  Androids: 1,
- Stolen: true,
+ Stolen: false,
 }

```

Share Format Run

```go

package main

import (
	"fmt"

"github.com/kylelemons/godebug/pretty"
)

var t = struct {
	Errorf func(string, ...interface{})
}{
	Errorf: func(format string, args ...interface{}) {
		fmt.Println(fmt.Sprintf(format, args...) + "\n")
	},
}

func main() {
	// Code under test:

type ShipManifest struct {
		Name     string
		Crew     map[string]string
		Androids int
		Stolen   bool
	}

// AddCrew tries to add the given crewmember to the manifest.
	AddCrew := func(m *ShipManifest, name, title string) {
		if m.Crew == nil {
			m.Crew = make(map[string]string)
		}
		m.Crew[title] = name
	}

// Test function:
	tests := []struct {
		desc        string
		before      *ShipManifest
		name, title string
		after       *ShipManifest
	}{
		{
			desc:   "add first",
			before: &ShipManifest{},
			name:   "Zaphod Beeblebrox",
			title:  "Galactic President",
			after: &ShipManifest{
				Crew: map[string]string{
					"Zaphod Beeblebrox": "Galactic President",
				},
			},
		},
		{
			desc: "add another",
			before: &ShipManifest{
				Crew: map[string]string{
					"Zaphod Beeblebrox": "Galactic President",
				},
			},
			name:  "Trillian",
			title: "Human",
			after: &ShipManifest{
				Crew: map[string]string{
					"Zaphod Beeblebrox": "Galactic President",
					"Trillian":          "Human",
				},
			},
		},
		{
			desc: "overwrite",
			before: &ShipManifest{
				Crew: map[string]string{
					"Zaphod Beeblebrox": "Galactic President",
				},
			},
			name:  "Zaphod Beeblebrox",
			title: "Just this guy, you know?",
			after: &ShipManifest{
				Crew: map[string]string{
					"Zaphod Beeblebrox": "Just this guy, you know?",
				},
			},
		},
	}

for _, test := range tests {
		AddCrew(test.before, test.name, test.title)
		if diff := pretty.Compare(test.before, test.after); diff != "" {
			t.Errorf("%s: post-AddCrew diff: (-got +want)\n%s", test.desc, diff)
		}
	}

}

```

```go
Output:
add first: post-AddCrew diff: (-got +want)
 {
  Name: "",
  Crew: {
-  Galactic President: "Zaphod Beeblebrox",
+  Zaphod Beeblebrox: "Galactic President",
  },
  Androids: 0,
  Stolen: false,
 }

add another: post-AddCrew diff: (-got +want)
 {
  Name: "",
  Crew: {
-  Human: "Trillian",
+  Trillian: "Human",
   Zaphod Beeblebrox: "Galactic President",
  },
  Androids: 0,
  Stolen: false,
 }

overwrite: post-AddCrew diff: (-got +want)
 {
  Name: "",
  Crew: {
-  Just this guy, you know?: "Zaphod Beeblebrox",
-  Zaphod Beeblebrox: "Galactic President",
+  Zaphod Beeblebrox: "Just this guy, you know?",
  },
  Androids: 0,
  Stolen: false,
 }

```

Share Format Run

```go

package main

import (
	"fmt"

"github.com/kylelemons/godebug/pretty"
)

type ListNode struct {
	Value int
	Next  *ListNode
}

func circular(nodes int) *ListNode {
	final := &ListNode{
		Value: nodes,
	}
	final.Next = final

recent := final
	for i := nodes - 1; i > 0; i-- {
		n := &ListNode{
			Value: i,
			Next:  recent,
		}
		final.Next = n
		recent = n
	}
	return recent
}

func main() {
	got, want := circular(3), circular(3)

// Make the got one broken
	got.Next.Next.Next = got.Next

fmt.Printf("Diff: (-got +want)\n%s", pretty.CycleTracker.Compare(got, want))

}

```

```go
Output:
Diff: (-got +want)
-{
+<#1> {
  Value: 1,
- Next: <#1> {
+ Next: {
   Value: 2,
   Next: {
    Value: 3,
    Next: <see #1>,
   },
  },
 }

```

Share Format Run

```go
func Fprint(w io.Writer, vals ...interface{}) (n int64, err error)
```

Fprint writes the representation of the given value to the writer according to the DefaultConfig.

```go
func Print(vals ...interface{})
```

Print writes the DefaultConfig representation of the given values to standard output.

```go

package main

import (
	"github.com/kylelemons/godebug/pretty"
)

func main() {
	type ShipManifest struct {
		Name     string
		Crew     map[string]string
		Androids int
		Stolen   bool
	}

manifest := &ShipManifest{
		Name: "Spaceship Heart of Gold",
		Crew: map[string]string{
			"Zaphod Beeblebrox": "Galactic President",
			"Trillian":          "Human",
			"Ford Prefect":      "A Hoopy Frood",
			"Arthur Dent":       "Along for the Ride",
		},
		Androids: 1,
		Stolen:   true,
	}

pretty.Print(manifest)

}

```

```go
Output:
{Name:     "Spaceship Heart of Gold",
 Crew:     {Arthur Dent:       "Along for the Ride",
            Ford Prefect:      "A Hoopy Frood",
            Trillian:          "Human",
            Zaphod Beeblebrox: "Galactic President"},
 Androids: 1,
 Stolen:   true}

```

Share Format Run

```go

package main

import (
	"github.com/kylelemons/godebug/pretty"
)

type ListNode struct {
	Value int
	Next  *ListNode
}

func circular(nodes int) *ListNode {
	final := &ListNode{
		Value: nodes,
	}
	final.Next = final

recent := final
	for i := nodes - 1; i > 0; i-- {
		n := &ListNode{
			Value: i,
			Next:  recent,
		}
		final.Next = n
		recent = n
	}
	return recent
}

func main() {
	pretty.CycleTracker.Print(circular(3))

}

```

```go
Output:
<#1> {
 Value: 1,
 Next: {
  Value: 2,
  Next: {
   Value: 3,
   Next: <see #1>,
  },
 },
}

```

Share Format Run

```go
func Sprint(vals ...interface{}) string
```

Sprint returns a string representation of the given value according to the DefaultConfig.

```go
type Config struct {
	// Verbosity options
	Compact  bool // One-line output. Overrides Diffable.
	Diffable bool // Adds extra newlines for more easily diffable output.

// Field and value options
	IncludeUnexported   bool // Include unexported fields in output
	PrintStringers      bool // Call String on a fmt.Stringer
	PrintTextMarshalers bool // Call MarshalText on an encoding.TextMarshaler

// Output transforms
	ShortList int // Maximum character length for short lists if nonzero.

// Type-specific overrides
	//
	// Formatter maps a type to a function that will provide a one-line string
	// representation of the input value.  Conceptually:
	//   Formatter[reflect.TypeOf(v)](v) = "v as a string"
	//
	// Note that the first argument need not explicitly match the type, it must
	// merely be callable with it.
	//
	// When processing an input value, if its type exists as a key in Formatter:
	//   1) If the value is nil, no stringification is performed.
	//      This allows overriding of PrintStringers and PrintTextMarshalers.
	//   2) The value will be called with the input as its only argument.
	//      The function must return a string as its first return value.
	//
	// In addition to func literals, two common values for this will be:
	//   fmt.Sprint        (function) func Sprint(...interface{}) string
	//   Type.String         (method) func (Type) String() string
	//
	// Note that neither of these work if the String method is a pointer
	// method and the input will be provided as a value.  In that case,
	// use a function that calls .String on the formal value parameter.
	Formatter map[reflect.Type]interface{}

// If TrackCycles is enabled, pretty will detect and track
	// self-referential structures. If a self-referential structure (aka a
	// "recursive" value) is detected, numbered placeholders will be emitted.
	//
	// Pointer tracking is disabled by default for performance reasons.
	TrackCycles bool
}
```

A Config represents optional configuration parameters for formatting.

Some options, notably ShortList, dramatically increase the overhead of pretty-printing a value.

```go

package main

import (
	"fmt"
	"net"
	"reflect"

"github.com/kylelemons/godebug/pretty"
)

func main() {
	pretty.DefaultFormatter[reflect.TypeOf(&net.IPNet{})] = func(n *net.IPNet) string {
		return fmt.Sprintf("CIDR=%s", n)
	}
	pretty.Print(&net.IPNet{
		IP:   net.IPv4(192, 168, 1, 100),
		Mask: net.CIDRMask(24, 32),
	})

}
