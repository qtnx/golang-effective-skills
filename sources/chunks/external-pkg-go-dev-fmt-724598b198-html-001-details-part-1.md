---
source_name: "External Linked Documentation"
source_url: "https://pkg.go.dev/fmt"
source_path: "sources/raw/external/pkg-go-dev-fmt-724598b198.html"
license_ref: ""
---

fmt package - fmt - Go Packages
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

Package fmt implements formatted I/O with functions analogous to C's printf and scanf. The format 'verbs' are derived from C's but are simpler.

#### Printing ¶

There are four families of printing functions defined by their output destination. Print, Println and Printf write to os.Stdout; Sprint, Sprintln and Sprintf return a string; Fprint, Fprintln and Fprintf write to an io.Writer; and Append, Appendln and Appendf append the output to a byte slice.

The functions within each family do the formatting according to the end of the name. Print, Sprint, Fprint and Append use the default format for each argument, adding a space between operands when neither is a string. Println, Sprintln, Fprintln and Appendln always add spaces and append a newline. Printf, Sprintf, Fprintf and Appendf use a sequence of "verbs" to control the formatting.

The verbs:

General:

```go
%v	the value in a default format
	when printing structs, the plus flag (%+v) adds field names
%#v	a Go-syntax representation of the value
	(floating-point infinities and NaNs print as ±Inf and NaN)
%T	a Go-syntax representation of the type of the value
%%	a literal percent sign; consumes no value

```

Boolean:

```go
%t	the word true or false

```

Integer:

```go
%b	base 2
%c	the character represented by the corresponding Unicode code point
%d	base 10
%o	base 8
%O	base 8 with 0o prefix
%q	a single-quoted character literal safely escaped with Go syntax.
%x	base 16, with lower-case letters for a-f
%X	base 16, with upper-case letters for A-F
%U	Unicode format: U+1234; same as "U+%04X"

```

Floating-point and complex constituents:

```go
%b	decimalless scientific notation with exponent a power of two,
	in the manner of strconv.FormatFloat with the 'b' format,
	e.g. -123456p-78
%e	scientific notation, e.g. -1.234456e+78
%E	scientific notation, e.g. -1.234456E+78
%f	decimal point but no exponent, e.g. 123.456
%F	synonym for %f
%g	%e for large exponents, %f otherwise. Precision is discussed below.
%G	%E for large exponents, %F otherwise
%x	hexadecimal notation (with decimal power of two exponent), e.g. -0x1.23abcp+20
%X	upper-case hexadecimal notation, e.g. -0X1.23ABCP+20

The exponent is always a decimal integer.
For formats other than %b the exponent is at least two digits.

```

String and slice of bytes (treated equivalently with these verbs):

```go
%s	the uninterpreted bytes of the string or slice
%q	a double-quoted string safely escaped with Go syntax
%x	base 16, lower-case, two characters per byte
%X	base 16, upper-case, two characters per byte

```

Slice:

```go
%p	address of 0th element in base 16 notation, with leading 0x

```

Pointer:

```go
%p	base 16 notation, with leading 0x
The %b, %d, %o, %x and %X verbs also work with pointers,
formatting the value exactly as if it were an integer.

```

The default format for %v is:

```go
bool:                    %t
int, int8 etc.:          %d
uint, uint8 etc.:        %d, %#x if printed with %#v
float32, complex64, etc: %g
string:                  %s
chan:                    %p
pointer:                 %p

```

For compound objects, the elements are printed using these rules, recursively, laid out like this:

```go
struct:             {field0 field1 ...}
array, slice:       [elem0 elem1 ...]
maps:               map[key1:value1 key2:value2 ...]
pointer to above:   &{}, &[], &map[]

```

Width is specified by an optional decimal number immediately preceding the verb. If absent, the width is whatever is necessary to represent the value. Precision is specified after the (optional) width by a period followed by a decimal number. If no period is present, a default precision is used. A period with no following number specifies a precision of zero. Examples:

```go
%f     default width, default precision
%9f    width 9, default precision
%.2f   default width, precision 2
%9.2f  width 9, precision 2
%9.f   width 9, precision 0

```

Width and precision are measured in units of Unicode code points, that is, runes. (This differs from C's printf where the units are always measured in bytes.) Either or both of the flags may be replaced with the character '*', causing their values to be obtained from the next operand (preceding the one to format), which must be of type int.

For most values, width is the minimum number of runes to output, padding the formatted form with spaces if necessary.

For strings, byte slices and byte arrays, however, precision limits the length of the input to be formatted (not the size of the output), truncating if necessary. Normally it is measured in runes, but for these types when formatted with the %x or %X format it is measured in bytes.

For floating-point values, width sets the minimum width of the field and precision sets the number of places after the decimal, if appropriate, except that for %g/%G precision sets the maximum number of significant digits (trailing zeros are removed). For example, given 12.345 the format %6.3f prints 12.345 while %.3g prints 12.3. The default precision for %e, %f and %#g is 6; for %g it is the smallest number of digits necessary to identify the value uniquely.

For complex numbers, the width and precision apply to the two components independently and the result is parenthesized, so %f applied to 1.2+3.4i produces (1.200000+3.400000i).

When formatting a single integer code point or a rune string (type []rune) with %q, invalid Unicode code points are changed to the Unicode replacement character, U+FFFD, as in strconv.QuoteRune.

Other flags:

```go
'+'	always print a sign for numeric values;
	guarantee ASCII-only output for %q (%+q)
'-'	pad with spaces on the right rather than the left (left-justify the field)
'#'	alternate format: add leading 0b for binary (%#b), 0 for octal (%#o),
	0x or 0X for hex (%#x or %#X); suppress 0x for %p (%#p);
	for %q, print a raw (backquoted) string if [strconv.CanBackquote]
	returns true;
	always print a decimal point for %e, %E, %f, %F, %g and %G;
	do not remove trailing zeros for %g and %G;
	write e.g. U+0078 'x' if the character is printable for %U (%#U)
' '	(space) leave a space for elided sign in numbers (% d);
	put spaces between bytes printing strings or slices in hex (% x, % X)
'0'	pad with leading zeros rather than spaces;
	for numbers, this moves the padding after the sign

```

Flags are ignored by verbs that do not expect them. For example there is no alternate decimal format, so %#d and %d behave identically.

For each Printf-like function, there is also a Print function that takes no format and is equivalent to saying %v for every operand. Another variant Println inserts blanks between operands and appends a newline.

Regardless of the verb, if an operand is an interface value, the internal concrete value is used, not the interface itself. Thus:

```go
var i interface{} = 23
fmt.Printf("%v\n", i)

```

will print 23.

Except when printed using the verbs %T and %p, special formatting considerations apply for operands that implement certain interfaces. In order of application:

1. If the operand is a reflect.Value, the operand is replaced by the concrete value that it holds, and printing continues with the next rule.

2. If an operand implements the Formatter interface, it will be invoked. In this case the interpretation of verbs and flags is controlled by that implementation.

3. If the %v verb is used with the # flag (%#v) and the operand implements the GoStringer interface, that will be invoked.

If the format (which is implicitly %v for Println etc.) is valid for a string (%s %q %x %X), or is %v but not %#v, the following two rules apply:

4. If an operand implements the error interface, the Error method will be invoked to convert the object to a string, which will then be formatted as required by the verb (if any).

5. If an operand implements method String() string, that method will be invoked to convert the object to a string, which will then be formatted as required by the verb (if any).

For compound operands such as slices and structs, the format applies to the elements of each operand, recursively, not to the operand as a whole. Thus %q will quote each element of a slice of strings, and %6.2f will control formatting for each element of a floating-point array.

However, when printing a byte slice with a string-like verb (%s %q %x %X), it is treated identically to a string, as a single item.

To avoid recursion in cases such as

```go
type X string
func (x X) String() string { return Sprintf("<%s>", x) }

```

convert the value before recurring:

```go
func (x X) String() string { return Sprintf("<%s>", string(x)) }

```

Infinite recursion can also be triggered by self-referential data structures, such as a slice that contains itself as an element, if that type has a String method. Such pathologies are rare, however, and the package does not protect against them.

When printing a struct, fmt cannot and therefore does not invoke formatting methods such as Error or String on unexported fields.

#### Explicit argument indexes ¶
