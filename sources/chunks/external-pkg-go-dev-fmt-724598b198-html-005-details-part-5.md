---
source_name: "External Linked Documentation"
source_url: "https://pkg.go.dev/fmt"
source_path: "sources/raw/external/pkg-go-dev-fmt-724598b198.html"
license_ref: ""
---

p2 := Person{
		Name: "Theia",
		Age:  4,
	}
	// If GoString() wasn't implemented, the output of `fmt.Printf("%#v", p2)` would be similar to
	// Person{Name:"Theia", Age:0x4, Addr:(*main.Address)(nil)}
	fmt.Printf("%#v\n", p2)

}

```

```go
Output:
Person{Name: "Warren", Age: 31, Addr: &Address{City: "Denver", State: "CO", Country: "U.S.A."}}
Person{Name: "Theia", Age: 4}

```

Share Format Run

```go
type ScanState interface {
	// ReadRune reads the next rune (Unicode code point) from the input.
	// If invoked during Scanln, Fscanln, or Sscanln, ReadRune() will
	// return EOF after returning the first '\n' or when reading beyond
	// the specified width.
	ReadRune() (r rune, size int, err error)
	// UnreadRune causes the next call to ReadRune to return the same rune.
	UnreadRune() error
	// for the operation being performed; see the package documentation
	// for more information.
	SkipSpace()
	// Token skips space in the input if skipSpace is true, then returns the
	// run of Unicode code points c satisfying f(c).  If f is nil,
	// !unicode.IsSpace(c) is used; that is, the token will hold non-space
	// characters. Newlines are treated appropriately for the operation being
	// performed; see the package documentation for more information.
	// The returned slice points to shared data that may be overwritten
	// by the next call to Token, a call to a Scan function using the ScanState
	// as input, or when the calling Scan method returns.
	Token(skipSpace bool, f func(rune) bool) (token []byte, err error)
	// Width returns the value of the width option and whether it has been set.
	// The unit is Unicode code points.
	Width() (wid int, ok bool)
	// Because ReadRune is implemented by the interface, Read should never be
	// called by the scanning routines and a valid implementation of
	// ScanState may choose always to return an error from Read.
	Read(buf []byte) (n int, err error)
}
```

ScanState represents the scanner state passed to custom scanners. Scanners may do rune-at-a-time scanning or ask the ScanState to discover the next space-delimited token.

```go
type Scanner interface {
	Scan(state ScanState, verb rune) error
}
```

Scanner is implemented by any value that has a Scan method, which scans the input for the representation of a value and stores the result in the receiver, which must be a pointer to be useful. The Scan method is called for any argument to Scan, Scanf, or Scanln that implements it.

```go
type State interface {
	// Write is the function to call to emit formatted output to be printed.
	Write(b []byte) (n int, err error)
	// Width returns the value of the width option and whether it has been set.
	Width() (wid int, ok bool)
	// Precision returns the value of the precision option and whether it has been set.
	Precision() (prec int, ok bool)

// Flag reports whether the flag c, a character, has been set.
	Flag(c int) bool
}
```

State represents the printer state passed to custom formatters. It provides access to the io.Writer interface plus information about the flags and options for the operand's format specifier.

```go
type Stringer interface {
	String() string
}
```

Stringer is implemented by any value that has a String method, which defines the “native” format for that value. The String method is used to print values passed as an operand to any format that accepts a string or to an unformatted printer such as Print.

```go

package main

import (
	"fmt"
)

// Animal has a Name and an Age to represent an animal.
type Animal struct {
	Name string
	Age  uint
}

// String makes Animal satisfy the Stringer interface.
func (a Animal) String() string {
	return fmt.Sprintf("%v (%d)", a.Name, a.Age)
}

func main() {
	a := Animal{
		Name: "Gopher",
		Age:  2,
	}
	fmt.Println(a)
}

```

```go
Output:
Gopher (2)

```

Share Format Run

##   Source Files ¶
 View all Source files <https://cs.opensource.google/go/go/+/go1.26.3:src/fmt>

- doc.go <https://cs.opensource.google/go/go/+/go1.26.3:src/fmt/doc.go>
- errors.go <https://cs.opensource.google/go/go/+/go1.26.3:src/fmt/errors.go>
- format.go <https://cs.opensource.google/go/go/+/go1.26.3:src/fmt/format.go>
- print.go <https://cs.opensource.google/go/go/+/go1.26.3:src/fmt/print.go>
- scan.go <https://cs.opensource.google/go/go/+/go1.26.3:src/fmt/scan.go>

Click to show internal directories.
  Click to hide internal directories.

Close

**?** : This menu   **/** : Search site   **f** or **F** : Jump to   **y** or **Y**  : Canonical URL
  Close
