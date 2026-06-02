---
source_name: "External Linked Documentation"
source_url: "https://go.dev/pkg/fmt/"
source_path: "sources/raw/external/go-dev-pkg-fmt-1c6a18c9a7.html"
license_ref: ""
---

```go
func Fprintf(w io.Writer, format string, a ...any) (n int, err error)
```

Fprintf formats according to a format specifier and writes to w. It returns the number of bytes written and any write error encountered.

```go

package main

import (
	"fmt"
	"os"
)

func main() {
	const name, age = "Kim", 22
	n, err := fmt.Fprintf(os.Stdout, "%s is %d years old.\n", name, age)

// The n and err return values from Fprintf are
	// those returned by the underlying io.Writer.
	if err != nil {
		fmt.Fprintf(os.Stderr, "Fprintf: %v\n", err)
	}
	fmt.Printf("%d bytes written.\n", n)

}

```

```go
Output:
Kim is 22 years old.
21 bytes written.

```

Share Format Run

```go
func Fprintln(w io.Writer, a ...any) (n int, err error)
```

Fprintln formats using the default formats for its operands and writes to w. Spaces are always added between operands and a newline is appended. It returns the number of bytes written and any write error encountered.

```go

package main

import (
	"fmt"
	"os"
)

func main() {
	const name, age = "Kim", 22
	n, err := fmt.Fprintln(os.Stdout, name, "is", age, "years old.")

// The n and err return values from Fprintln are
	// those returned by the underlying io.Writer.
	if err != nil {
		fmt.Fprintf(os.Stderr, "Fprintln: %v\n", err)
	}
	fmt.Println(n, "bytes written.")

}

```

```go
Output:
Kim is 22 years old.
21 bytes written.

```

Share Format Run

```go
func Fscan(r io.Reader, a ...any) (n int, err error)
```

Fscan scans text read from r, storing successive space-separated values into successive arguments. Newlines count as space. It returns the number of items successfully scanned. If that is less than the number of arguments, err will report why.

```go
func Fscanf(r io.Reader, format string, a ...any) (n int, err error)
```

Fscanf scans text read from r, storing successive space-separated values into successive arguments as determined by the format. It returns the number of items successfully parsed. Newlines in the input must match newlines in the format.

```go

package main

import (
	"fmt"
	"os"
	"strings"
)

func main() {
	var (
		i int
		b bool
		s string
	)
	r := strings.NewReader("5 true gophers")
	n, err := fmt.Fscanf(r, "%d %t %s", &i, &b, &s)
	if err != nil {
		fmt.Fprintf(os.Stderr, "Fscanf: %v\n", err)
	}
	fmt.Println(i, b, s)
	fmt.Println(n)
}

```

```go
Output:
5 true gophers
3

```

Share Format Run

```go
func Fscanln(r io.Reader, a ...any) (n int, err error)
```

Fscanln is similar to Fscan, but stops scanning at a newline and after the final item there must be a newline or EOF.

```go

package main

import (
	"fmt"
	"io"
	"strings"
)

func main() {
	s := `dmr 1771 1.61803398875
	ken 271828 3.14159`
	r := strings.NewReader(s)
	var a string
	var b int
	var c float64
	for {
		n, err := fmt.Fscanln(r, &a, &b, &c)
		if err == io.EOF {
			break
		}
		if err != nil {
			panic(err)
		}
		fmt.Printf("%d: %s, %d, %f\n", n, a, b, c)
	}
}

```

```go
Output:
3: dmr, 1771, 1.618034
3: ken, 271828, 3.141590

```

Share Format Run

```go
func Print(a ...any) (n int, err error)
```

Print formats using the default formats for its operands and writes to standard output. Spaces are added between operands when neither is a string. It returns the number of bytes written and any write error encountered.

```go

package main

import (
	"fmt"
)

func main() {
	const name, age = "Kim", 22
	fmt.Print(name, " is ", age, " years old.\n")

// It is conventional not to worry about any
	// error returned by Print.

}

```

```go
Output:
Kim is 22 years old.

```

Share Format Run

```go
func Printf(format string, a ...any) (n int, err error)
```

Printf formats according to a format specifier and writes to standard output. It returns the number of bytes written and any write error encountered.

```go

package main

import (
	"fmt"
)

func main() {
	const name, age = "Kim", 22
	fmt.Printf("%s is %d years old.\n", name, age)

// It is conventional not to worry about any
	// error returned by Printf.

}

```

```go
Output:
Kim is 22 years old.

```

Share Format Run

```go
func Println(a ...any) (n int, err error)
```

Println formats using the default formats for its operands and writes to standard output. Spaces are always added between operands and a newline is appended. It returns the number of bytes written and any write error encountered.

```go

package main

import (
	"fmt"
)

func main() {
	const name, age = "Kim", 22
	fmt.Println(name, "is", age, "years old.")

// It is conventional not to worry about any
	// error returned by Println.

}

```

```go
Output:
Kim is 22 years old.

```

Share Format Run

```go
func Scan(a ...any) (n int, err error)
```

Scan scans text read from standard input, storing successive space-separated values into successive arguments. Newlines count as space. It returns the number of items successfully scanned. If that is less than the number of arguments, err will report why.

```go
func Scanf(format string, a ...any) (n int, err error)
```

Scanf scans text read from standard input, storing successive space-separated values into successive arguments as determined by the format. It returns the number of items successfully scanned. If that is less than the number of arguments, err will report why. Newlines in the input must match newlines in the format. The one exception: the verb %c always scans the next rune in the input, even if it is a space (or tab etc.) or newline.

```go
func Scanln(a ...any) (n int, err error)
```

Scanln is similar to Scan, but stops scanning at a newline and after the final item there must be a newline or EOF.

```go
func Sprint(a ...any) string
```

Sprint formats using the default formats for its operands and returns the resulting string. Spaces are added between operands when neither is a string.

```go

package main

import (
	"fmt"
	"io"
	"os"
)

func main() {
	const name, age = "Kim", 22
	s := fmt.Sprint(name, " is ", age, " years old.\n")

io.WriteString(os.Stdout, s) // Ignoring error for simplicity.

}

```

```go
Output:
Kim is 22 years old.

```

Share Format Run

```go
func Sprintf(format string, a ...any) string
```

Sprintf formats according to a format specifier and returns the resulting string.

```go

package main

import (
	"fmt"
	"io"
	"os"
)

func main() {
	const name, age = "Kim", 22
	s := fmt.Sprintf("%s is %d years old.\n", name, age)

io.WriteString(os.Stdout, s) // Ignoring error for simplicity.

}

```

```go
Output:
Kim is 22 years old.

```

Share Format Run

```go
func Sprintln(a ...any) string
```

Sprintln formats using the default formats for its operands and returns the resulting string. Spaces are always added between operands and a newline is appended.

```go

package main

import (
	"fmt"
	"io"
	"os"
)

func main() {
	const name, age = "Kim", 22
	s := fmt.Sprintln(name, "is", age, "years old.")

io.WriteString(os.Stdout, s) // Ignoring error for simplicity.

}

```

```go
Output:
Kim is 22 years old.

```

Share Format Run

```go
func Sscan(str string, a ...any) (n int, err error)
```

Sscan scans the argument string, storing successive space-separated values into successive arguments. Newlines count as space. It returns the number of items successfully scanned. If that is less than the number of arguments, err will report why.

```go
func Sscanf(str string, format string, a ...any) (n int, err error)
```

Sscanf scans the argument string, storing successive space-separated values into successive arguments as determined by the format. It returns the number of items successfully parsed. Newlines in the input must match newlines in the format.

```go

package main

import (
	"fmt"
)

func main() {
	var name string
	var age int
	n, err := fmt.Sscanf("Kim is 22 years old", "%s is %d years old", &name, &age)
	if err != nil {
		panic(err)
	}
	fmt.Printf("%d: %s, %d\n", n, name, age)

}

```

```go
Output:
2: Kim, 22

```

Share Format Run

```go
func Sscanln(str string, a ...any) (n int, err error)
```

Sscanln is similar to Sscan, but stops scanning at a newline and after the final item there must be a newline or EOF.

```go
type Formatter interface {
	Format(f State, verb rune)
}
```

Formatter is implemented by any value that has a Format method. The implementation controls how State and rune are interpreted, and may call Sprint or Fprint(f) etc. to generate its output.

```go
type GoStringer interface {
	GoString() string
}
```

GoStringer is implemented by any value that has a GoString method, which defines the Go syntax for that value. The GoString method is used to print values passed as an operand to a %#v format.

```go

package main

import (
	"fmt"
)

// Address has a City, State and a Country.
type Address struct {
	City    string
	State   string
	Country string
}

// Person has a Name, Age and Address.
type Person struct {
	Name string
	Age  uint
	Addr *Address
}

// GoString makes Person satisfy the GoStringer interface.
// The return value is valid Go code that can be used to reproduce the Person struct.
func (p Person) GoString() string {
	if p.Addr != nil {
		return fmt.Sprintf("Person{Name: %q, Age: %d, Addr: &Address{City: %q, State: %q, Country: %q}}", p.Name, int(p.Age), p.Addr.City, p.Addr.State, p.Addr.Country)
	}
	return fmt.Sprintf("Person{Name: %q, Age: %d}", p.Name, int(p.Age))
}

func main() {
	p1 := Person{
		Name: "Warren",
		Age:  31,
		Addr: &Address{
			City:    "Denver",
			State:   "CO",
			Country: "U.S.A.",
		},
	}
	// If GoString() wasn't implemented, the output of `fmt.Printf("%#v", p1)` would be similar to
	// Person{Name:"Warren", Age:0x1f, Addr:(*main.Address)(0x10448240)}
	fmt.Printf("%#v\n", p1)
