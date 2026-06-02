---
source_name: "External Linked Documentation"
source_url: "https://pkg.go.dev/io"
source_path: "sources/raw/external/pkg-go-dev-io-227b602496.html"
license_ref: ""
---

ReadAtLeast reads from r into buf until it has read at least min bytes. It returns the number of bytes copied and an error if fewer bytes were read. The error is EOF only if no bytes were read. If an EOF happens after reading fewer than min bytes, ReadAtLeast returns ErrUnexpectedEOF. If min is greater than the length of buf, ReadAtLeast returns ErrShortBuffer. On return, n >= min if and only if err == nil. If r returns an error having read at least min bytes, the error is dropped.

```go

package main

import (
	"fmt"
	"io"
	"log"
	"strings"
)

func main() {
	r := strings.NewReader("some io.Reader stream to be read\n")

buf := make([]byte, 14)
	if _, err := io.ReadAtLeast(r, buf, 4); err != nil {
		log.Fatal(err)
	}
	fmt.Printf("%s\n", buf)

// buffer smaller than minimal read size.
	shortBuf := make([]byte, 3)
	if _, err := io.ReadAtLeast(r, shortBuf, 4); err != nil {
		fmt.Println("error:", err)
	}

// minimal read size bigger than io.Reader stream
	longBuf := make([]byte, 64)
	if _, err := io.ReadAtLeast(r, longBuf, 64); err != nil {
		fmt.Println("error:", err)
	}

}

```

```go
Output:
some io.Reader
error: short buffer
error: unexpected EOF

```

Share Format Run

```go
func ReadFull(r Reader, buf []byte) (n int, err error)
```

ReadFull reads exactly len(buf) bytes from r into buf. It returns the number of bytes copied and an error if fewer bytes were read. The error is EOF only if no bytes were read. If an EOF happens after reading some but not all the bytes, ReadFull returns ErrUnexpectedEOF. On return, n == len(buf) if and only if err == nil. If r returns an error having read at least len(buf) bytes, the error is dropped.

```go

package main

import (
	"fmt"
	"io"
	"log"
	"strings"
)

func main() {
	r := strings.NewReader("some io.Reader stream to be read\n")

buf := make([]byte, 4)
	if _, err := io.ReadFull(r, buf); err != nil {
		log.Fatal(err)
	}
	fmt.Printf("%s\n", buf)

// minimal read size bigger than io.Reader stream
	longBuf := make([]byte, 64)
	if _, err := io.ReadFull(r, longBuf); err != nil {
		fmt.Println("error:", err)
	}

}

```

```go
Output:
some
error: unexpected EOF

```

Share Format Run

```go
func WriteString(w Writer, s string) (n int, err error)
```

WriteString writes the contents of the string s to w, which accepts a slice of bytes. If w implements StringWriter, [StringWriter.WriteString] is invoked directly. Otherwise, [Writer.Write] is called exactly once.

```go

package main

import (
	"io"
	"log"
	"os"
)

func main() {
	if _, err := io.WriteString(os.Stdout, "Hello World"); err != nil {
		log.Fatal(err)
	}

}

```

```go
Output:
Hello World

```

Share Format Run

```go
type ByteReader interface {
	ReadByte() (byte, error)
}
```

ByteReader is the interface that wraps the ReadByte method.

ReadByte reads and returns the next byte from the input or any error encountered. If ReadByte returns an error, no input byte was consumed, and the returned byte value is undefined.

ReadByte provides an efficient interface for byte-at-time processing. A Reader that does not implement ByteReader can be wrapped using bufio.NewReader to add this method.

```go
type ByteScanner interface {
	ByteReader
	UnreadByte() error
}
```

ByteScanner is the interface that adds the UnreadByte method to the basic ReadByte method.

UnreadByte causes the next call to ReadByte to return the last byte read. If the last operation was not a successful call to ReadByte, UnreadByte may return an error, unread the last byte read (or the byte prior to the last-unread byte), or (in implementations that support the Seeker interface) seek to one byte before the current offset.

```go
type ByteWriter interface {
	WriteByte(c byte) error
}
```

ByteWriter is the interface that wraps the WriteByte method.

```go
type Closer interface {
	Close() error
}
```

Closer is the interface that wraps the basic Close method.

The behavior of Close after the first call is undefined. Specific implementations may document their own behavior.

```go
type LimitedReader struct {
	R Reader // underlying reader
	N int64  // max bytes remaining
}
```

A LimitedReader reads from R but limits the amount of data returned to just N bytes. Each call to Read updates N to reflect the new amount remaining. Read returns EOF when N <= 0 or when the underlying R returns EOF.

```go
func (l *LimitedReader) Read(p []byte) (n int, err error)
```

```go
type OffsetWriter struct {
	// contains filtered or unexported fields
}
```

An OffsetWriter maps writes at offset base to offset base+off in the underlying writer.

```go
func NewOffsetWriter(w WriterAt, off int64) *OffsetWriter
```

NewOffsetWriter returns an OffsetWriter that writes to w starting at offset off.

```go
func (o *OffsetWriter) Seek(offset int64, whence int) (int64, error)
```

```go
func (o *OffsetWriter) Write(p []byte) (n int, err error)
```

```go
func (o *OffsetWriter) WriteAt(p []byte, off int64) (n int, err error)
```

```go
type PipeReader struct {
	// contains filtered or unexported fields
}
```

A PipeReader is the read half of a pipe.

```go
func (r *PipeReader) Close() error
```

Close closes the reader; subsequent writes to the write half of the pipe will return the error ErrClosedPipe.

```go
func (r *PipeReader) CloseWithError(err error) error
```

CloseWithError closes the reader; subsequent writes to the write half of the pipe will return the error err.

CloseWithError never overwrites the previous error if it exists and always returns nil.

```go
func (r *PipeReader) Read(data []byte) (n int, err error)
```

Read implements the standard Read interface: it reads data from the pipe, blocking until a writer arrives or the write end is closed. If the write end is closed with an error, that error is returned as err; otherwise err is EOF.

```go
type PipeWriter struct {
	// contains filtered or unexported fields
}
```

A PipeWriter is the write half of a pipe.

```go
func (w *PipeWriter) Close() error
```

Close closes the writer; subsequent reads from the read half of the pipe will return no bytes and EOF.

```go
func (w *PipeWriter) CloseWithError(err error) error
```

CloseWithError closes the writer; subsequent reads from the read half of the pipe will return no bytes and the error err, or EOF if err is nil.

CloseWithError never overwrites the previous error if it exists and always returns nil.

```go
func (w *PipeWriter) Write(data []byte) (n int, err error)
```

Write implements the standard Write interface: it writes data to the pipe, blocking until one or more readers have consumed all the data or the read end is closed. If the read end is closed with an error, that err is returned as err; otherwise err is ErrClosedPipe.

```go
type ReadCloser interface {
	Reader
	Closer
}
```

ReadCloser is the interface that groups the basic Read and Close methods.

```go
func NopCloser(r Reader) ReadCloser
```

NopCloser returns a ReadCloser with a no-op Close method wrapping the provided Reader r. If r implements WriterTo, the returned ReadCloser will implement WriterTo by forwarding calls to r.

```go
type ReadSeekCloser interface {
	Reader
	Seeker
	Closer
}
```

ReadSeekCloser is the interface that groups the basic Read, Seek and Close methods.

```go
type ReadSeeker interface {
	Reader
	Seeker
}
```

ReadSeeker is the interface that groups the basic Read and Seek methods.

```go
type ReadWriteCloser interface {
	Reader
	Writer
	Closer
}
```

ReadWriteCloser is the interface that groups the basic Read, Write and Close methods.

```go
type ReadWriteSeeker interface {
	Reader
	Writer
	Seeker
}
```

ReadWriteSeeker is the interface that groups the basic Read, Write and Seek methods.

```go
type ReadWriter interface {
	Reader
	Writer
}
```

ReadWriter is the interface that groups the basic Read and Write methods.

```go
type Reader interface {
	Read(p []byte) (n int, err error)
}
```

Reader is the interface that wraps the basic Read method.

Read reads up to len(p) bytes into p. It returns the number of bytes read (0 <= n <= len(p)) and any error encountered. Even if Read returns n < len(p), it may use all of p as scratch space during the call. If some data is available but not len(p) bytes, Read conventionally returns what is available instead of waiting for more.

When Read encounters an error or end-of-file condition after successfully reading n > 0 bytes, it returns the number of bytes read. It may return the (non-nil) error from the same call or return the error (and n == 0) from a subsequent call. An instance of this general case is that a Reader returning a non-zero number of bytes at the end of the input stream may return either err == EOF or err == nil. The next Read should return 0, EOF.

Callers should always process the n > 0 bytes returned before considering the error err. Doing so correctly handles I/O errors that happen after reading some bytes and also both of the allowed EOF behaviors.

If len(p) == 0, Read should always return n == 0. It may return a non-nil error if some error condition is known, such as EOF.

Implementations of Read are discouraged from returning a zero byte count with a nil error, except when len(p) == 0. Callers should treat a return of 0 and nil as indicating that nothing happened; in particular it does not indicate EOF.

Implementations must not retain p.

```go
func LimitReader(r Reader, n int64) Reader
```

LimitReader returns a Reader that reads from r but stops with EOF after n bytes. The underlying implementation is a *LimitedReader.

```go

package main

import (
	"io"
	"log"
	"os"
	"strings"
)

func main() {
	r := strings.NewReader("some io.Reader stream to be read\n")
	lr := io.LimitReader(r, 4)
