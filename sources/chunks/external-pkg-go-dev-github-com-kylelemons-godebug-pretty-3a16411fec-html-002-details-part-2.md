---
source_name: "External Linked Documentation"
source_url: "https://pkg.go.dev/github.com/kylelemons/godebug/pretty"
source_path: "sources/raw/external/pkg-go-dev-github-com-kylelemons-godebug-pretty-3a16411fec.html"
license_ref: ""
---

```

```go
Output:
CIDR=192.168.1.100/24

```

Share Format Run

```go

package main

import (
	"fmt"
	"net"
	"reflect"

"github.com/kylelemons/godebug/pretty"
)

func main() {
	pretty.DefaultFormatter[reflect.TypeOf(&net.IPNet{})] = fmt.Sprint
	pretty.DefaultFormatter[reflect.TypeOf(net.HardwareAddr{})] = fmt.Sprint
	pretty.Print(&net.IPNet{
		IP:   net.IPv4(192, 168, 1, 100),
		Mask: net.CIDRMask(24, 32),
	})
	pretty.Print(net.HardwareAddr{1, 2, 3, 4, 5, 6})

}

```

```go
Output:
192.168.1.100/24
01:02:03:04:05:06

```

Share Format Run

```go
func (cfg *Config) Compare(a, b interface{}) string
```

Compare returns a string containing a line-by-line unified diff of the values in got and want according to the cfg.

Each line in the output is prefixed with '+', '-', or ' ' to indicate which side it's from. Lines from the a side are marked with '-', lines from the b side are marked with '+' and lines that are the same on both sides are marked with ' '.

The comparison is based on the intentionally-untyped output of Print, and as such this comparison is pretty forviving. In particular, if the types of or types within in a and b are different but have the same representation, Compare will not indicate any differences between them.

```go
func (cfg *Config) Fprint(w io.Writer, vals ...interface{}) (n int64, err error)
```

Fprint writes the representation of the given value to the writer according to the cfg.

```go
func (cfg *Config) Print(vals ...interface{})
```

Print writes the configured presentation of the given values to standard output.

```go
func (cfg *Config) Sprint(vals ...interface{}) string
```

Sprint returns a string representation of the given value according to cfg.

```go

package main

import (
	"fmt"

"github.com/kylelemons/godebug/pretty"
)

func main() {
	type Pair [2]int
	type Map struct {
		Name      string
		Players   map[string]Pair
		Obstacles map[Pair]string
	}

m := Map{
		Name: "Rock Creek",
		Players: map[string]Pair{
			"player1": {1, 3},
			"player2": {0, -1},
		},
		Obstacles: map[Pair]string{
			Pair{0, 0}: "rock",
			Pair{2, 1}: "pond",
			Pair{1, 1}: "stream",
			Pair{0, 1}: "stream",
		},
	}

// Specific output formats
	compact := &pretty.Config{
		Compact: true,
	}
	diffable := &pretty.Config{
		Diffable: true,
	}

// Print out a summary
	fmt.Printf("Players: %s\n", compact.Sprint(m.Players))

// Print diffable output
	fmt.Printf("Map State:\n%s", diffable.Sprint(m))

}

```

```go
Output:
Players: {player1:[1,3],player2:[0,-1]}
Map State:
{
 Name: "Rock Creek",
 Players: {
  player1: [
   1,
   3,
  ],
  player2: [
   0,
   -1,
  ],
 },
 Obstacles: {
  [0,0]: "rock",
  [0,1]: "stream",
  [1,1]: "stream",
  [2,1]: "pond",
 },
}

```

Share Format Run

##   Source Files ¶
 View all Source files <https://github.com/kylelemons/godebug/tree/v1.1.0/pretty>

- doc.go <https://github.com/kylelemons/godebug/blob/v1.1.0/pretty/doc.go>
- public.go <https://github.com/kylelemons/godebug/blob/v1.1.0/pretty/public.go>
- reflect.go <https://github.com/kylelemons/godebug/blob/v1.1.0/pretty/reflect.go>
- structure.go <https://github.com/kylelemons/godebug/blob/v1.1.0/pretty/structure.go>

Click to show internal directories.
  Click to hide internal directories.

Close

**?** : This menu   **/** : Search site   **f** or **F** : Jump to   **y** or **Y**  : Canonical URL
  Close
