---
source_name: "External Linked Documentation"
source_url: "https://pkg.go.dev/bytes"
source_path: "sources/raw/external/pkg-go-dev-bytes-42228f0497.html"
license_ref: ""
---

func main() {
	var b bytes.Buffer
	b.Grow(64)
	b.Write([]byte("abcde"))
	rdbuf := make([]byte, 1)
	n, err := b.Read(rdbuf)
	if err != nil {
		panic(err)
	}
	fmt.Println(n)
	fmt.Println(b.String())
	fmt.Println(string(rdbuf))
}

```

```go
Output:
1
bcde
a

```

Share Format Run

```go
func (b *Buffer) ReadByte() (byte, error)
```

ReadByte reads and returns the next byte from the buffer. If no byte is available, it returns error io.EOF.

```go

package main

import (
	"bytes"
	"fmt"
)

func main() {
	var b bytes.Buffer
	b.Grow(64)
	b.Write([]byte("abcde"))
	c, err := b.ReadByte()
	if err != nil {
		panic(err)
	}
	fmt.Println(c)
	fmt.Println(b.String())
}

```

```go
Output:
97
bcde

```

Share Format Run

```go
func (b *Buffer) ReadBytes(delim byte) (line []byte, err error)
```

ReadBytes reads until the first occurrence of delim in the input, returning a slice containing the data up to and including the delimiter. If ReadBytes encounters an error before finding a delimiter, it returns the data read before the error and the error itself (often io.EOF). ReadBytes returns err != nil if and only if the returned data does not end in delim.

```go
func (b *Buffer) ReadFrom(r io.Reader) (n int64, err error)
```

ReadFrom reads data from r until EOF and appends it to the buffer, growing the buffer as needed. The return value n is the number of bytes read. Any error except io.EOF encountered during the read is also returned. If the buffer becomes too large, ReadFrom will panic with ErrTooLarge.

```go
func (b *Buffer) ReadRune() (r rune, size int, err error)
```

ReadRune reads and returns the next UTF-8-encoded Unicode code point from the buffer. If no bytes are available, the error returned is io.EOF. If the bytes are an erroneous UTF-8 encoding, it consumes one byte and returns U+FFFD, 1.

```go
func (b *Buffer) ReadString(delim byte) (line string, err error)
```

ReadString reads until the first occurrence of delim in the input, returning a string containing the data up to and including the delimiter. If ReadString encounters an error before finding a delimiter, it returns the data read before the error and the error itself (often io.EOF). ReadString returns err != nil if and only if the returned data does not end in delim.

```go
func (b *Buffer) Reset()
```

Reset resets the buffer to be empty, but it retains the underlying storage for use by future writes. Reset is the same as Buffer.Truncate(0).

```go
func (b *Buffer) String() string
```

String returns the contents of the unread portion of the buffer as a string. If the Buffer is a nil pointer, it returns "<nil>".

To build strings more efficiently, see the strings.Builder type.

```go
func (b *Buffer) Truncate(n int)
```

Truncate discards all but the first n unread bytes from the buffer but continues to use the same allocated storage. It panics if n is negative or greater than the length of the buffer.

```go
func (b *Buffer) UnreadByte() error
```

UnreadByte unreads the last byte returned by the most recent successful read operation that read at least one byte. If a write has happened since the last read, if the last read returned an error, or if the read read zero bytes, UnreadByte returns an error.

```go
func (b *Buffer) UnreadRune() error
```

UnreadRune unreads the last rune returned by Buffer.ReadRune. If the most recent read or write operation on the buffer was not a successful Buffer.ReadRune, UnreadRune returns an error. (In this regard it is stricter than Buffer.UnreadByte, which will unread the last byte from any read operation.)

```go
func (b *Buffer) Write(p []byte) (n int, err error)
```

Write appends the contents of p to the buffer, growing the buffer as needed. The return value n is the length of p; err is always nil. If the buffer becomes too large, Write will panic with ErrTooLarge.

```go
func (b *Buffer) WriteByte(c byte) error
```

WriteByte appends the byte c to the buffer, growing the buffer as needed. The returned error is always nil, but is included to match bufio.Writer's WriteByte. If the buffer becomes too large, WriteByte will panic with ErrTooLarge.

```go
func (b *Buffer) WriteRune(r rune) (n int, err error)
```

WriteRune appends the UTF-8 encoding of Unicode code point r to the buffer, returning its length and an error, which is always nil but is included to match bufio.Writer's WriteRune. The buffer is grown as needed; if it becomes too large, WriteRune will panic with ErrTooLarge.

```go
func (b *Buffer) WriteString(s string) (n int, err error)
```

WriteString appends the contents of s to the buffer, growing the buffer as needed. The return value n is the length of s; err is always nil. If the buffer becomes too large, WriteString will panic with ErrTooLarge.

```go
func (b *Buffer) WriteTo(w io.Writer) (n int64, err error)
```

WriteTo writes data to w until the buffer is drained or an error occurs. The return value n is the number of bytes written; it always fits into an int, but it is int64 to match the io.WriterTo interface. Any error encountered during the write is also returned.

```go
type Reader struct {
	// contains filtered or unexported fields
}
```

A Reader implements the io.Reader, io.ReaderAt, io.WriterTo, io.Seeker, io.ByteScanner, and io.RuneScanner interfaces by reading from a byte slice. Unlike a Buffer, a Reader is read-only and supports seeking. The zero value for Reader operates like a Reader of an empty slice.

```go
func NewReader(b []byte) *Reader
```

NewReader returns a new Reader reading from b.

```go
func (r *Reader) Len() int
```

Len returns the number of bytes of the unread portion of the slice.

```go

package main

import (
	"bytes"
	"fmt"
)

func main() {
	fmt.Println(bytes.NewReader([]byte("Hi!")).Len())
	fmt.Println(bytes.NewReader([]byte("こんにちは!")).Len())
}

```

```go
Output:
3
16

```

Share Format Run

```go
func (r *Reader) Read(b []byte) (n int, err error)
```

Read implements the io.Reader interface.

```go
func (r *Reader) ReadAt(b []byte, off int64) (n int, err error)
```

ReadAt implements the io.ReaderAt interface.

```go
func (r *Reader) ReadByte() (byte, error)
```

ReadByte implements the io.ByteReader interface.

```go
func (r *Reader) ReadRune() (ch rune, size int, err error)
```

ReadRune implements the io.RuneReader interface.

```go
func (r *Reader) Reset(b []byte)
```

Reset resets the Reader to be reading from b.

```go
func (r *Reader) Seek(offset int64, whence int) (int64, error)
```

Seek implements the io.Seeker interface.

```go
func (r *Reader) Size() int64
```

Size returns the original length of the underlying byte slice. Size is the number of bytes available for reading via Reader.ReadAt. The result is unaffected by any method calls except Reader.Reset.

```go
func (r *Reader) UnreadByte() error
```

UnreadByte complements Reader.ReadByte in implementing the io.ByteScanner interface.

```go
func (r *Reader) UnreadRune() error
```

UnreadRune complements Reader.ReadRune in implementing the io.RuneScanner interface.

```go
func (r *Reader) WriteTo(w io.Writer) (n int64, err error)
```

WriteTo implements the io.WriterTo interface.

##   Source Files ¶
 View all Source files <https://cs.opensource.google/go/go/+/go1.26.3:src/bytes>

- buffer.go <https://cs.opensource.google/go/go/+/go1.26.3:src/bytes/buffer.go>
- bytes.go <https://cs.opensource.google/go/go/+/go1.26.3:src/bytes/bytes.go>
- iter.go <https://cs.opensource.google/go/go/+/go1.26.3:src/bytes/iter.go>
- reader.go <https://cs.opensource.google/go/go/+/go1.26.3:src/bytes/reader.go>

Click to show internal directories.
  Click to hide internal directories.

Close

**?** : This menu   **/** : Search site   **f** or **F** : Jump to   **y** or **Y**  : Canonical URL
  Close
