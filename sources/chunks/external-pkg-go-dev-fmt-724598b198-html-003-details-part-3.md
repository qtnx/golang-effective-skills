---
source_name: "External Linked Documentation"
source_url: "https://pkg.go.dev/fmt"
source_path: "sources/raw/external/pkg-go-dev-fmt-724598b198.html"
license_ref: ""
---

// Runes are integers but when printed with %c show the character with that
	// Unicode value. The %q verb shows them as quoted characters, %U as a
	// hex Unicode code point, and %#U as both a code point and a quoted
	// printable form if the rune is printable.
	smile := '😀'
	fmt.Printf("%v %d %c %q %U %#U\n", smile, smile, smile, smile, smile, smile)
	// Result: 128512 128512 😀 '😀' U+1F600 U+1F600 '😀'

// Strings are formatted with %v and %s as-is, with %q as quoted strings,
	// and %#q as backquoted strings.
	placeholders := `foo "bar"`
	fmt.Printf("%v %s %q %#q\n", placeholders, placeholders, placeholders, placeholders)
	// Result: foo "bar" foo "bar" "foo \"bar\"" `foo "bar"`

// Maps formatted with %v show keys and values in their default formats.
	// The %#v form (the # is called a "flag" in this context) shows the map in
	// the Go source format. Maps are printed in a consistent order, sorted
	// by the values of the keys.
	isLegume := map[string]bool{
		"peanut":    true,
		"dachshund": false,
	}
	fmt.Printf("%v %#v\n", isLegume, isLegume)
	// Result: map[dachshund:false peanut:true] map[string]bool{"dachshund":false, "peanut":true}

// Structs formatted with %v show field values in their default formats.
	// The %+v form shows the fields by name, while %#v formats the struct in
	// Go source format.
	person := struct {
		Name string
		Age  int
	}{"Kim", 22}
	fmt.Printf("%v %+v %#v\n", person, person, person)
	// Result: {Kim 22} {Name:Kim Age:22} struct { Name string; Age int }{Name:"Kim", Age:22}

// The default format for a pointer shows the underlying value preceded by
	// an ampersand. The %p verb prints the pointer value in hex. We use a
	// typed nil for the argument to %p here because the value of any non-nil
	// pointer would change from run to run; run the commented-out Printf
	// call yourself to see.
	pointer := &person
	fmt.Printf("%v %p\n", pointer, (*int)(nil))
	// Result: &{Kim 22} 0x0
	// fmt.Printf("%v %p\n", pointer, pointer)
	// Result: &{Kim 22} 0x010203 // See comment above.

// Arrays and slices are formatted by applying the format to each element.
	greats := [5]string{"Kitano", "Kobayashi", "Kurosawa", "Miyazaki", "Ozu"}
	fmt.Printf("%v %q\n", greats, greats)
	// Result: [Kitano Kobayashi Kurosawa Miyazaki Ozu] ["Kitano" "Kobayashi" "Kurosawa" "Miyazaki" "Ozu"]

kGreats := greats[:3]
	fmt.Printf("%v %q %#v\n", kGreats, kGreats, kGreats)
	// Result: [Kitano Kobayashi Kurosawa] ["Kitano" "Kobayashi" "Kurosawa"] []string{"Kitano", "Kobayashi", "Kurosawa"}

// Byte slices are special. Integer verbs like %d print the elements in
	// that format. The %s and %q forms treat the slice like a string. The %x
	// verb has a special form with the space flag that puts a space between
	// the bytes.
	cmd := []byte("a⌘")
	fmt.Printf("%v %d %s %q %x % x\n", cmd, cmd, cmd, cmd, cmd, cmd)
	// Result: [97 226 140 152] [97 226 140 152] a⌘ "a⌘" 61e28c98 61 e2 8c 98

// Types that implement Stringer are printed the same as strings. Because
	// Stringers return a string, we can print them using a string-specific
	// verb such as %q.
	now := time.Unix(123456789, 0).UTC() // time.Time implements fmt.Stringer.
	fmt.Printf("%v %q\n", now, now)
	// Result: 1973-11-29 21:33:09 +0000 UTC "1973-11-29 21:33:09 +0000 UTC"

}

```

```go
Output:
23
23
23
int *int
true true
42 42 2a 52 101010
3.141592653589793 3.141592653589793 3.14 (  3.14) 3.141593e+00
(110.7+22.5i) (110.7+22.5i) (110.70+22.50i) (1.11e+02+2.25e+01i)
128512 128512 😀 '😀' U+1F600 U+1F600 '😀'
foo "bar" foo "bar" "foo \"bar\"" `foo "bar"`
map[dachshund:false peanut:true] map[string]bool{"dachshund":false, "peanut":true}
{Kim 22} {Name:Kim Age:22} struct { Name string; Age int }{Name:"Kim", Age:22}
&{Kim 22} 0x0
[Kitano Kobayashi Kurosawa Miyazaki Ozu] ["Kitano" "Kobayashi" "Kurosawa" "Miyazaki" "Ozu"]
[Kitano Kobayashi Kurosawa] ["Kitano" "Kobayashi" "Kurosawa"] []string{"Kitano", "Kobayashi", "Kurosawa"}
[97 226 140 152] [97 226 140 152] a⌘ "a⌘" 61e28c98 61 e2 8c 98
1973-11-29 21:33:09 +0000 UTC "1973-11-29 21:33:09 +0000 UTC"

```

Share Format Run

Print, Println, and Printf lay out their arguments differently. In this example we can compare their behaviors. Println always adds blanks between the items it prints, while Print adds blanks only between non-string arguments and Printf does exactly what it is told. Sprint, Sprintln, Sprintf, Fprint, Fprintln, and Fprintf behave the same as their corresponding Print, Println, and Printf functions shown here.

```go

package main

import (
	"fmt"
	"math"
)

func main() {
	a, b := 3.0, 4.0
	h := math.Hypot(a, b)

// Print inserts blanks between arguments when neither is a string.
	// It does not add a newline to the output, so we add one explicitly.
	fmt.Print("The vector (", a, b, ") has length ", h, ".\n")

// Println always inserts spaces between its arguments,
	// so it cannot be used to produce the same output as Print in this case;
	// its output has extra spaces.
	// Also, Println always adds a newline to the output.
	fmt.Println("The vector (", a, b, ") has length", h, ".")

// Printf provides complete control but is more complex to use.
	// It does not add a newline to the output, so we add one explicitly
	// at the end of the format specifier string.
	fmt.Printf("The vector (%g %g) has length %g.\n", a, b, h)

}

```

```go
Output:
The vector (3 4) has length 5.
The vector ( 3 4 ) has length 5 .
The vector (3 4) has length 5.

```

Share Format Run

-  func Append(b []byte, a ...any) []byte
-  func Appendf(b []byte, format string, a ...any) []byte
-  func Appendln(b []byte, a ...any) []byte
-  func Errorf(format string, a ...any) (err error)
-  func FormatString(state State, verb rune) string
-  func Fprint(w io.Writer, a ...any) (n int, err error)
-  func Fprintf(w io.Writer, format string, a ...any) (n int, err error)
-  func Fprintln(w io.Writer, a ...any) (n int, err error)
-  func Fscan(r io.Reader, a ...any) (n int, err error)
-  func Fscanf(r io.Reader, format string, a ...any) (n int, err error)
-  func Fscanln(r io.Reader, a ...any) (n int, err error)
-  func Print(a ...any) (n int, err error)
-  func Printf(format string, a ...any) (n int, err error)
-  func Println(a ...any) (n int, err error)
-  func Scan(a ...any) (n int, err error)
-  func Scanf(format string, a ...any) (n int, err error)
-  func Scanln(a ...any) (n int, err error)
-  func Sprint(a ...any) string
-  func Sprintf(format string, a ...any) string
-  func Sprintln(a ...any) string
-  func Sscan(str string, a ...any) (n int, err error)
-  func Sscanf(str string, format string, a ...any) (n int, err error)
-  func Sscanln(str string, a ...any) (n int, err error)
-  type Formatter
-  type GoStringer
-  type ScanState
-  type Scanner
-  type State
-  type Stringer

- Package (Formats)
- Package (Printers)
- Errorf
- Fprint
- Fprintf
- Fprintln
- Fscanf
- Fscanln
- GoStringer
- Print
- Printf
- Println
- Sprint
- Sprintf
- Sprintln
- Sscanf
- Stringer

This section is empty.

This section is empty.

```go
func Append(b []byte, a ...any) []byte
```

Append formats using the default formats for its operands, appends the result to the byte slice, and returns the updated slice. Spaces are added between operands when neither is a string.

```go
func Appendf(b []byte, format string, a ...any) []byte
```

Appendf formats according to a format specifier, appends the result to the byte slice, and returns the updated slice.

```go
func Appendln(b []byte, a ...any) []byte
```

Appendln formats using the default formats for its operands, appends the result to the byte slice, and returns the updated slice. Spaces are always added between operands and a newline is appended.

```go
func Errorf(format string, a ...any) (err error)
```

Errorf formats according to a format specifier and returns the string as a value that satisfies error.

If the format specifier includes a %w verb with an error operand, the returned error will implement an Unwrap method returning the operand. If there is more than one %w verb, the returned error will implement an Unwrap method returning a []error containing all the %w operands in the order they appear in the arguments. It is invalid to supply the %w verb with an operand that does not implement the error interface. The %w verb is otherwise a synonym for %v.

The Errorf function lets us use formatting features to create descriptive error messages.

```go

package main

import (
	"fmt"
)

func main() {
	const name, id = "bueller", 17
	err := fmt.Errorf("user %q (id %d) not found", name, id)
	fmt.Println(err.Error())

}

```

```go
Output:
user "bueller" (id 17) not found

```

Share Format Run

```go
func FormatString(state State, verb rune) string
```

FormatString returns a string representing the fully qualified formatting directive captured by the State, followed by the argument verb. (State does not itself contain the verb.) The result has a leading percent sign followed by any flags, the width, and the precision. Missing flags, width, and precision are omitted. This function allows a Formatter to reconstruct the original directive triggering the call to Format.

```go
func Fprint(w io.Writer, a ...any) (n int, err error)
```

Fprint formats using the default formats for its operands and writes to w. Spaces are added between operands when neither is a string. It returns the number of bytes written and any write error encountered.

```go

package main

import (
	"fmt"
	"os"
)

func main() {
	const name, age = "Kim", 22
	n, err := fmt.Fprint(os.Stdout, name, " is ", age, " years old.\n")

// The n and err return values from Fprint are
	// those returned by the underlying io.Writer.
	if err != nil {
		fmt.Fprintf(os.Stderr, "Fprint: %v\n", err)
	}
	fmt.Print(n, " bytes written.\n")

}

```

```go
Output:
Kim is 22 years old.
21 bytes written.

```

Share Format Run
