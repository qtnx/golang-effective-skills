csv package - encoding/csv - Go Packages

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

## Links

-    Report a Vulnerability  <https://go.dev/security/policy>

##   Documentation ¶

Package csv reads and writes comma-separated values (CSV) files. There are many kinds of CSV files; this package supports the format described in RFC 4180 <https://rfc-editor.org/rfc/rfc4180.html>, except that Writer uses LF instead of CRLF as newline character by default.

A csv file contains zero or more records of one or more fields per record. Each record is separated by the newline character. The final record may optionally be followed by a newline character.

```go
field1,field2,field3

```

White space is considered part of a field.

Carriage returns before newline characters are silently removed.

Blank lines are ignored. A line with only whitespace characters (excluding the ending newline character) is not considered a blank line.

Fields which start and stop with the quote character " are called quoted-fields. The beginning and ending quote are not part of the field.

The source:

```go
normal string,"quoted-field"

```

results in the fields

```go
{`normal string`, `quoted-field`}

```

Within a quoted-field a quote character followed by a second quote character is considered a single quote.

```go
"the ""word"" is true","a ""quoted-field"""

```

results in

```go
{`the "word" is true`, `a "quoted-field"`}

```

Newlines and commas may be included in a quoted-field

```go
"Multi-line
field","comma is ,"

```

results in

```go
{`Multi-line
field`, `comma is ,`}

```

- Variables
-  type ParseError
-
-  func (e *ParseError) Error() string
-  func (e *ParseError) Unwrap() error

-  type Reader
-
-  func NewReader(r io.Reader) *Reader

-
-  func (r *Reader) FieldPos(field int) (line, column int)
-  func (r *Reader) InputOffset() int64
-  func (r *Reader) Read() (record []string, err error)
-  func (r *Reader) ReadAll() (records [][]string, err error)

-  type Writer
-
-  func NewWriter(w io.Writer) *Writer

-
-  func (w *Writer) Error() error
-  func (w *Writer) Flush()
-  func (w *Writer) Write(record []string) error
-  func (w *Writer) WriteAll(records [][]string) error

- Reader
- Reader (Options)
- Reader.ReadAll
- Writer
- Writer.WriteAll

This section is empty.

    View Source <https://cs.opensource.google/go/go/+/go1.26.3:src/encoding/csv/reader.go;l=87>
```go
var (
	ErrBareQuote  = errors.New("bare \" in non-quoted-field")
	ErrQuote      = errors.New("extraneous or missing \" in quoted-field")
	ErrFieldCount = errors.New("wrong number of fields")

	// Deprecated: ErrTrailingComma is no longer used.
	ErrTrailingComma = errors.New("extra delimiter at end of line")
)
```

These are the errors that can be returned in [ParseError.Err].

This section is empty.

```go
type ParseError struct {
	StartLine int   // Line where the record starts
	Line      int   // Line where the error occurred
	Column    int   // Column (1-based byte index) where the error occurred
	Err       error // The actual error
}
```

A ParseError is returned for parsing errors. Line and column numbers are 1-indexed.

```go
func (e *ParseError) Error() string
```

```go
func (e *ParseError) Unwrap() error
```

```go
type Reader struct {
	// Comma is the field delimiter.
	// It is set to comma (',') by NewReader.
	// Comma must be a valid rune and must not be \r, \n,
	// or the Unicode replacement character (0xFFFD).
	Comma rune

	// Comment, if not 0, is the comment character. Lines beginning with the
	// Comment character without preceding whitespace are ignored.
	// With leading whitespace the Comment character becomes part of the
	// field, even if TrimLeadingSpace is true.
	// Comment must be a valid rune and must not be \r, \n,
	// or the Unicode replacement character (0xFFFD).
	// It must also not be equal to Comma.
	Comment rune

	// FieldsPerRecord is the number of expected fields per record.
	// If FieldsPerRecord is positive, Read requires each record to
	// have the given number of fields. If FieldsPerRecord is 0, Read sets it to
	// the number of fields in the first record, so that future records must
	// have the same field count. If FieldsPerRecord is negative, no check is
	// made and records may have a variable number of fields.
	FieldsPerRecord int

	// If LazyQuotes is true, a quote may appear in an unquoted field and a
	// non-doubled quote may appear in a quoted field.
	LazyQuotes bool

	// If TrimLeadingSpace is true, leading white space in a field is ignored.
	// This is done even if the field delimiter, Comma, is white space.
	TrimLeadingSpace bool

	// ReuseRecord controls whether calls to Read may return a slice sharing
	// the backing array of the previous call's returned slice for performance.
	// By default, each call to Read returns newly allocated memory owned by the caller.
	ReuseRecord bool

	// Deprecated: TrailingComma is no longer used.
	TrailingComma bool
	// contains filtered or unexported fields
}
```

A Reader reads records from a CSV-encoded file.

As returned by NewReader, a Reader expects input conforming to RFC 4180 <https://rfc-editor.org/rfc/rfc4180.html>. The exported fields can be changed to customize the details before the first call to Reader.Read or Reader.ReadAll.

The Reader converts all \r\n sequences in its input to plain \n, including in multiline field values, so that the returned data does not depend on which line-ending convention an input file uses.

```go

package main

import (
	"encoding/csv"
	"fmt"
	"io"
	"log"
	"strings"
)

func main() {
	in := `first_name,last_name,username
"Rob","Pike",rob
Ken,Thompson,ken
"Robert","Griesemer","gri"
`
	r := csv.NewReader(strings.NewReader(in))

	for {
		record, err := r.Read()
		if err == io.EOF {
			break
		}
		if err != nil {
			log.Fatal(err)
		}

		fmt.Println(record)
	}
}

```

```go
Output:
[first_name last_name username]
[Rob Pike rob]
[Ken Thompson ken]
[Robert Griesemer gri]

```

 Share Format Run

This example shows how csv.Reader can be configured to handle other types of CSV files.

```go

package main

import (
	"encoding/csv"
	"fmt"
	"log"
	"strings"
)

func main() {
	in := `first_name;last_name;username
"Rob";"Pike";rob
# lines beginning with a # character are ignored
Ken;Thompson;ken
"Robert";"Griesemer";"gri"
`
	r := csv.NewReader(strings.NewReader(in))
	r.Comma = ';'
	r.Comment = '#'

	records, err := r.ReadAll()
	if err != nil {
		log.Fatal(err)
	}

	fmt.Print(records)
}

```

```go
Output:
[[first_name last_name username] [Rob Pike rob] [Ken Thompson ken] [Robert Griesemer gri]]

```

 Share Format Run

```go
func NewReader(r io.Reader) *Reader
```

NewReader returns a new Reader that reads from r.

```go
func (r *Reader) FieldPos(field int) (line, column int)
```

FieldPos returns the line and column corresponding to the start of the field with the given index in the slice most recently returned by Reader.Read. Numbering of lines and columns starts at 1; columns are counted in bytes, not runes.

If this is called with an out-of-bounds index, it panics.

```go
func (r *Reader) InputOffset() int64
```

InputOffset returns the input stream byte offset of the current reader position. The offset gives the location of the end of the most recently read row and the beginning of the next row.

```go
func (r *Reader) Read() (record []string, err error)
```

Read reads one record (a slice of fields) from r. If the record has an unexpected number of fields, Read returns the record along with the error ErrFieldCount. If the record contains a field that cannot be parsed, Read returns a partial record along with the parse error. The partial record contains all fields read before the error. If there is no data left to be read, Read returns nil, io.EOF. If [Reader.ReuseRecord] is true, the returned slice may be shared between multiple calls to Read.

```go
func (r *Reader) ReadAll() (records [][]string, err error)
```

ReadAll reads all the remaining records from r. Each record is a slice of fields. A successful call returns err == nil, not err == io.EOF. Because ReadAll is defined to read until EOF, it does not treat end of file as an error to be reported.

```go

package main

import (
	"encoding/csv"
	"fmt"
	"log"
	"strings"
)

func main() {
	in := `first_name,last_name,username
"Rob","Pike",rob
Ken,Thompson,ken
"Robert","Griesemer","gri"
`
	r := csv.NewReader(strings.NewReader(in))

	records, err := r.ReadAll()
	if err != nil {
		log.Fatal(err)
	}

	fmt.Print(records)
}

```

```go
Output:
[[first_name last_name username] [Rob Pike rob] [Ken Thompson ken] [Robert Griesemer gri]]

```

 Share Format Run

```go
type Writer struct {
	Comma   rune // Field delimiter (set to ',' by NewWriter)
	UseCRLF bool // True to use \r\n as the line terminator
	// contains filtered or unexported fields
}
```

A Writer writes records using CSV encoding.

As returned by NewWriter, a Writer writes records terminated by a newline and uses ',' as the field delimiter. The exported fields can be changed to customize the details before the first call to Writer.Write or Writer.WriteAll.

[Writer.Comma] is the field delimiter.

If [Writer.UseCRLF] is true, the Writer ends each output line with \r\n instead of \n.

The writes of individual records are buffered. After all data has been written, the client should call the Writer.Flush method to guarantee all data has been forwarded to the underlying io.Writer. Any errors that occurred should be checked by calling the Writer.Error method.

```go

package main

import (
	"encoding/csv"
	"log"
	"os"
)

func main() {
	records := [][]string{
		{"first_name", "last_name", "username"},
		{"Rob", "Pike", "rob"},
		{"Ken", "Thompson", "ken"},
		{"Robert", "Griesemer", "gri"},
	}

	w := csv.NewWriter(os.Stdout)

	for _, record := range records {
		if err := w.Write(record); err != nil {
			log.Fatalln("error writing record to csv:", err)
		}
	}

	// Write any buffered data to the underlying writer (standard output).
	w.Flush()

	if err := w.Error(); err != nil {
		log.Fatal(err)
	}
}

```

```go
Output:
first_name,last_name,username
Rob,Pike,rob
Ken,Thompson,ken
Robert,Griesemer,gri

```

 Share Format Run

```go
func NewWriter(w io.Writer) *Writer
```

NewWriter returns a new Writer that writes to w.

```go
func (w *Writer) Error() error
```

Error reports any error that has occurred during a previous Writer.Write or Writer.Flush.

```go
func (w *Writer) Flush()
```

Flush writes any buffered data to the underlying io.Writer. To check if an error occurred during Flush, call Writer.Error.

```go
func (w *Writer) Write(record []string) error
```

Write writes a single CSV record to w along with any necessary quoting. A record is a slice of strings with each string being one field. Writes are buffered, so Writer.Flush must eventually be called to ensure that the record is written to the underlying io.Writer.

```go
func (w *Writer) WriteAll(records [][]string) error
```

WriteAll writes multiple CSV records to w using Writer.Write and then calls Writer.Flush, returning any error from the Flush.

```go

package main

import (
	"encoding/csv"
	"log"
	"os"
)

func main() {
	records := [][]string{
		{"first_name", "last_name", "username"},
		{"Rob", "Pike", "rob"},
		{"Ken", "Thompson", "ken"},
		{"Robert", "Griesemer", "gri"},
	}

	w := csv.NewWriter(os.Stdout)
	w.WriteAll(records) // calls Flush internally

	if err := w.Error(); err != nil {
		log.Fatalln("error writing csv:", err)
	}
}

```

```go
Output:
first_name,last_name,username
Rob,Pike,rob
Ken,Thompson,ken
Robert,Griesemer,gri

```

 Share Format Run

##   Source Files ¶
 View all Source files <https://cs.opensource.google/go/go/+/go1.26.3:src/encoding/csv>

- reader.go <https://cs.opensource.google/go/go/+/go1.26.3:src/encoding/csv/reader.go>
- writer.go <https://cs.opensource.google/go/go/+/go1.26.3:src/encoding/csv/writer.go>

  Click to show internal directories.
  Click to hide internal directories.

  Close

     **?** : This menu   **/** : Search site   **f** or **F** : Jump to   **y** or **Y**  : Canonical URL
  Close
