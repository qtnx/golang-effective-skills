---
source_name: "External Linked Documentation"
source_url: "https://go.dev/pkg/fmt/"
source_path: "sources/raw/external/go-dev-pkg-fmt-1c6a18c9a7.html"
license_ref: ""
---

In Printf, Sprintf, Fprintf, and Appendf, the default behavior is for each formatting verb to format successive arguments passed in the call. However, the notation [n] immediately before the verb indicates that the nth one-indexed argument is to be formatted instead. The same notation before a '*' for a width or precision selects the argument index holding the value. After processing a bracketed expression [n], subsequent verbs will use arguments n+1, n+2, etc. unless otherwise directed.

For example,

```go
fmt.Sprintf("%[2]d %[1]d\n", 11, 22)

```

will yield "22 11", while

```go
fmt.Sprintf("%[3]*.[2]*[1]f", 12.0, 2, 6)

```

equivalent to

```go
fmt.Sprintf("%6.2f", 12.0)

```

will yield " 12.00". Because an explicit index affects subsequent verbs, this notation can be used to print the same values multiple times by resetting the index for the first argument to be repeated:

```go
fmt.Sprintf("%d %d %#[1]x %#x", 16, 17)

```

will yield "16 17 0x10 0x11".

#### Format errors ¶

If an invalid argument is given for a verb, such as providing a string to %d, the generated string will contain a description of the problem, as in these examples:

```go
Wrong type or unknown verb: %!verb(type=value)
	Printf("%d", "hi"):        %!d(string=hi)
Too many arguments: %!(EXTRA type=value)
	Printf("hi", "guys"):      hi%!(EXTRA string=guys)
Too few arguments: %!verb(MISSING)
	Printf("hi%d"):            hi%!d(MISSING)
Non-int for width or precision: %!(BADWIDTH) or %!(BADPREC)
	Printf("%*s", 4.5, "hi"):  %!(BADWIDTH)hi
	Printf("%.*s", 4.5, "hi"): %!(BADPREC)hi
Invalid or invalid use of argument index: %!(BADINDEX)
	Printf("%*[2]d", 7):       %!d(BADINDEX)
	Printf("%.[2]d", 7):       %!d(BADINDEX)

```

All errors begin with the string "%!" followed sometimes by a single character (the verb) and end with a parenthesized description.

If an Error or String method triggers a panic when called by a print routine, the fmt package reformats the error message from the panic, decorating it with an indication that it came through the fmt package. For example, if a String method calls panic("bad"), the resulting formatted message will look like

```go
%!s(PANIC=bad)

```

The %!s just shows the print verb in use when the failure occurred. If the panic is caused by a nil receiver to an Error, String, or GoString method, however, the output is the undecorated string, "<nil>".

#### Scanning ¶

An analogous set of functions scans formatted text to yield values. Scan, Scanf and Scanln read from os.Stdin; Fscan, Fscanf and Fscanln read from a specified io.Reader; Sscan, Sscanf and Sscanln read from an argument string.

Scan, Fscan, Sscan treat newlines in the input as spaces.

Scanln, Fscanln and Sscanln stop scanning at a newline and require that the items be followed by a newline or EOF.

Scanf, Fscanf, and Sscanf parse the arguments according to a format string, analogous to that of Printf. In the text that follows, 'space' means any Unicode whitespace character except newline.

In the format string, a verb introduced by the % character consumes and parses input; these verbs are described in more detail below. A character other than %, space, or newline in the format consumes exactly that input character, which must be present. A newline with zero or more spaces before it in the format string consumes zero or more spaces in the input followed by a single newline or the end of the input. A space following a newline in the format string consumes zero or more spaces in the input. Otherwise, any run of one or more spaces in the format string consumes as many spaces as possible in the input. Unless the run of spaces in the format string appears adjacent to a newline, the run must consume at least one space from the input or find the end of the input.

The handling of spaces and newlines differs from that of C's scanf family: in C, newlines are treated as any other space, and it is never an error when a run of spaces in the format string finds no spaces to consume in the input.

The verbs behave analogously to those of Printf. For example, %x will scan an integer as a hexadecimal number, and %v will scan the default representation format for the value. The Printf verbs %p and %T and the flags # and + are not implemented. For floating-point and complex values, all valid formatting verbs (%b %e %E %f %F %g %G %x %X and %v) are equivalent and accept both decimal and hexadecimal notation (for example: "2.3e+7", "0x4.5p-8") and digit-separating underscores (for example: "3.14159_26535_89793").

Input processed by verbs is implicitly space-delimited: the implementation of every verb except %c starts by discarding leading spaces from the remaining input, and the %s verb (and %v reading into a string) stops consuming input at the first space or newline character.

The familiar base-setting prefixes 0b (binary), 0o and 0 (octal), and 0x (hexadecimal) are accepted when scanning integers without a format or with the %v verb, as are digit-separating underscores.

Width is interpreted in the input text but there is no syntax for scanning with a precision (no %5.2f, just %5f). If width is provided, it applies after leading spaces are trimmed and specifies the maximum number of runes to read to satisfy the verb. For example,

```go
Sscanf(" 1234567 ", "%5s%d", &s, &i)

```

will set s to "12345" and i to 67 while

```go
Sscanf(" 12 34 567 ", "%5s%d", &s, &i)

```

will set s to "12" and i to 34.

In all the scanning functions, a carriage return followed immediately by a newline is treated as a plain newline (\r\n means the same as \n).

In all the scanning functions, if an operand implements method Scan (that is, it implements the Scanner interface) that method will be used to scan the text for that operand. Also, if the number of arguments scanned is less than the number of arguments provided, an error is returned.

All arguments to be scanned must be either pointers to basic types or implementations of the Scanner interface.

Like Scanf and Fscanf, Sscanf need not consume its entire input. There is no way to recover how much of the input string Sscanf used.

Note: Fscan etc. can read one character (rune) past the input they return, which means that a loop calling a scan routine may skip some of the input. This is usually a problem only when there is no space between input values. If the reader provided to Fscan implements ReadRune, that method will be used to read characters. If the reader also implements UnreadRune, that method will be used to save the character and successive calls will not lose data. To attach ReadRune and UnreadRune methods to a reader without that capability, use bufio.NewReader.

These examples demonstrate the basics of printing using a format string. Printf, Sprintf, and Fprintf all take a format string that specifies how to format the subsequent arguments. For example, %d (we call that a 'verb') says to print the corresponding argument, which must be an integer (or something containing an integer, such as a slice of ints) in decimal. The verb %v ('v' for 'value') always formats the argument in its default form, just how Print or Println would show it. The special verb %T ('T' for 'Type') prints the type of the argument rather than its value. The examples are not exhaustive; see the package comment for all the details.

```go

package main

import (
	"fmt"
	"math"
	"time"
)

func main() {
	// A basic set of examples showing that %v is the default format, in this
	// case decimal for integers, which can be explicitly requested with %d;
	// the output is just what Println generates.
	integer := 23
	// Each of these prints "23" (without the quotes).
	fmt.Println(integer)
	fmt.Printf("%v\n", integer)
	fmt.Printf("%d\n", integer)

// The special verb %T shows the type of an item rather than its value.
	fmt.Printf("%T %T\n", integer, &integer)
	// Result: int *int

// Println(x) is the same as Printf("%v\n", x) so we will use only Printf
	// in the following examples. Each one demonstrates how to format values of
	// a particular type, such as integers or strings. We start each format
	// string with %v to show the default output and follow that with one or
	// more custom formats.

// Booleans print as "true" or "false" with %v or %t.
	truth := true
	fmt.Printf("%v %t\n", truth, truth)
	// Result: true true

// Integers print as decimals with %v and %d,
	// or in hex with %x, octal with %o, or binary with %b.
	answer := 42
	fmt.Printf("%v %d %x %o %b\n", answer, answer, answer, answer, answer)
	// Result: 42 42 2a 52 101010

// Floats have multiple formats: %v and %g print a compact representation,
	// while %f prints a decimal point and %e uses exponential notation. The
	// format %6.2f used here shows how to set the width and precision to
	// control the appearance of a floating-point value. In this instance, 6 is
	// the total width of the printed text for the value (note the extra spaces
	// in the output) and 2 is the number of decimal places to show.
	pi := math.Pi
	fmt.Printf("%v %g %.2f (%6.2f) %e\n", pi, pi, pi, pi, pi)
	// Result: 3.141592653589793 3.141592653589793 3.14 (  3.14) 3.141593e+00

// Complex numbers format as parenthesized pairs of floats, with an 'i'
	// after the imaginary part.
	point := 110.7 + 22.5i
	fmt.Printf("%v %g %.2f %.2e\n", point, point, point, point)
	// Result: (110.7+22.5i) (110.7+22.5i) (110.70+22.50i) (1.11e+02+2.25e+01i)
