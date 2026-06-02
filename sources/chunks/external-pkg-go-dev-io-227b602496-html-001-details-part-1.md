---
source_name: "External Linked Documentation"
source_url: "https://pkg.go.dev/io"
source_path: "sources/raw/external/pkg-go-dev-io-227b602496.html"
license_ref: ""
---

io package - io - Go Packages
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

Package io provides basic interfaces to I/O primitives. Its primary job is to wrap existing implementations of such primitives, such as those in package os, into shared public interfaces that abstract the functionality, plus some other related primitives.

Because these interfaces and primitives wrap lower-level operations with various implementations, unless otherwise informed clients should not assume they are safe for parallel execution.

- Constants
- Variables
-  func Copy(dst Writer, src Reader) (written int64, err error)
-  func CopyBuffer(dst Writer, src Reader, buf []byte) (written int64, err error)
-  func CopyN(dst Writer, src Reader, n int64) (written int64, err error)
-  func Pipe() (*PipeReader, *PipeWriter)
-  func ReadAll(r Reader) ([]byte, error)
-  func ReadAtLeast(r Reader, buf []byte, min int) (n int, err error)
-  func ReadFull(r Reader, buf []byte) (n int, err error)
-  func WriteString(w Writer, s string) (n int, err error)
-  type ByteReader
-  type ByteScanner
-  type ByteWriter
-  type Closer
-  type LimitedReader
-
-  func (l *LimitedReader) Read(p []byte) (n int, err error)

-  type OffsetWriter
-
-  func NewOffsetWriter(w WriterAt, off int64) *OffsetWriter

-
-  func (o *OffsetWriter) Seek(offset int64, whence int) (int64, error)
-  func (o *OffsetWriter) Write(p []byte) (n int, err error)
-  func (o *OffsetWriter) WriteAt(p []byte, off int64) (n int, err error)

-  type PipeReader
-
-  func (r *PipeReader) Close() error
-  func (r *PipeReader) CloseWithError(err error) error
-  func (r *PipeReader) Read(data []byte) (n int, err error)

-  type PipeWriter
-
-  func (w *PipeWriter) Close() error
-  func (w *PipeWriter) CloseWithError(err error) error
-  func (w *PipeWriter) Write(data []byte) (n int, err error)

-  type ReadCloser
-
-  func NopCloser(r Reader) ReadCloser

-  type ReadSeekCloser
-  type ReadSeeker
-  type ReadWriteCloser
-  type ReadWriteSeeker
-  type ReadWriter
-  type Reader
-
-  func LimitReader(r Reader, n int64) Reader
-  func MultiReader(readers ...Reader) Reader
-  func TeeReader(r Reader, w Writer) Reader

-  type ReaderAt
-  type ReaderFrom
-  type RuneReader
-  type RuneScanner
-  type SectionReader
-
-  func NewSectionReader(r ReaderAt, off int64, n int64) *SectionReader

-
-  func (s *SectionReader) Outer() (r ReaderAt, off int64, n int64)
-  func (s *SectionReader) Read(p []byte) (n int, err error)
-  func (s *SectionReader) ReadAt(p []byte, off int64) (n int, err error)
-  func (s *SectionReader) Seek(offset int64, whence int) (int64, error)
-  func (s *SectionReader) Size() int64

-  type Seeker
-  type StringWriter
-  type WriteCloser
-  type WriteSeeker
-  type Writer
-
-  func MultiWriter(writers ...Writer) Writer

-  type WriterAt
-  type WriterTo

- Copy
- CopyBuffer
- CopyN
- LimitReader
- MultiReader
- MultiWriter
- Pipe
- ReadAll
- ReadAtLeast
- ReadFull
- SectionReader
- SectionReader.Read
- SectionReader.ReadAt
- SectionReader.Seek
- SectionReader.Size
- TeeReader
- WriteString

View Source <https://cs.opensource.google/go/go/+/go1.26.3:src/io/io.go;l=21>
```go
const (
	SeekStart   = 0 // seek relative to the origin of the file
	SeekCurrent = 1 // seek relative to the current offset
	SeekEnd     = 2 // seek relative to the end
)
```

Seek whence values.

View Source <https://cs.opensource.google/go/go/+/go1.26.3:src/io/io.go;l=44>
```go
var EOF = errors.New("EOF")
```

EOF is the error returned by Read when no more input is available. (Read must return EOF itself, not an error wrapping EOF, because callers will test for EOF using ==.) Functions should return EOF only to signal a graceful end of input. If the EOF occurs unexpectedly in a structured data stream, the appropriate error is either ErrUnexpectedEOF or some other error giving more detail.
  View Source <https://cs.opensource.google/go/go/+/go1.26.3:src/io/pipe.go;l=36>
```go
var ErrClosedPipe = errors.New("io: read/write on closed pipe")
```

ErrClosedPipe is the error used for read or write operations on a closed pipe.
  View Source <https://cs.opensource.google/go/go/+/go1.26.3:src/io/io.go;l=53>
```go
var ErrNoProgress = errors.New("multiple Read calls return no data or error")
```

ErrNoProgress is returned by some clients of a Reader when many calls to Read have failed to return any data or error, usually the sign of a broken Reader implementation.
  View Source <https://cs.opensource.google/go/go/+/go1.26.3:src/io/io.go;l=35>
```go
var ErrShortBuffer = errors.New("short buffer")
```

ErrShortBuffer means that a read required a longer buffer than was provided.
  View Source <https://cs.opensource.google/go/go/+/go1.26.3:src/io/io.go;l=29>
```go
var ErrShortWrite = errors.New("short write")
```

ErrShortWrite means that a write accepted fewer bytes than requested but failed to return an explicit error.
  View Source <https://cs.opensource.google/go/go/+/go1.26.3:src/io/io.go;l=48>
```go
var ErrUnexpectedEOF = errors.New("unexpected EOF")
```

ErrUnexpectedEOF means that EOF was encountered in the middle of reading a fixed-size block or data structure.

```go
func Copy(dst Writer, src Reader) (written int64, err error)
```

Copy copies from src to dst until either EOF is reached on src or an error occurs. It returns the number of bytes copied and the first error encountered while copying, if any.

A successful Copy returns err == nil, not err == EOF. Because Copy is defined to read from src until EOF, it does not treat an EOF from Read as an error to be reported.

If src implements WriterTo, the copy is implemented by calling src.WriteTo(dst). Otherwise, if dst implements ReaderFrom, the copy is implemented by calling dst.ReadFrom(src).

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

if _, err := io.Copy(os.Stdout, r); err != nil {
		log.Fatal(err)
	}

}

```

```go
Output:
some io.Reader stream to be read

```

Share Format Run

```go
func CopyBuffer(dst Writer, src Reader, buf []byte) (written int64, err error)
```

CopyBuffer is identical to Copy except that it stages through the provided buffer (if one is required) rather than allocating a temporary one. If buf is nil, one is allocated; otherwise if it has zero length, CopyBuffer panics.

If either src implements WriterTo or dst implements ReaderFrom, buf will not be used to perform the copy.

```go

package main

import (
	"io"
	"log"
	"os"
	"strings"
)

func main() {
	r1 := strings.NewReader("first reader\n")
	r2 := strings.NewReader("second reader\n")
	buf := make([]byte, 8)

// buf is used here...
	if _, err := io.CopyBuffer(os.Stdout, r1, buf); err != nil {
		log.Fatal(err)
	}

// ... reused here also. No need to allocate an extra buffer.
	if _, err := io.CopyBuffer(os.Stdout, r2, buf); err != nil {
		log.Fatal(err)
	}

}

```

```go
Output:
first reader
second reader

```

Share Format Run

```go
func CopyN(dst Writer, src Reader, n int64) (written int64, err error)
```

CopyN copies n bytes (or until an error) from src to dst. It returns the number of bytes copied and the earliest error encountered while copying. On return, written == n if and only if err == nil.

If dst implements ReaderFrom, the copy is implemented using it.

```go

package main

import (
	"io"
	"log"
	"os"
	"strings"
)

func main() {
	r := strings.NewReader("some io.Reader stream to be read")

if _, err := io.CopyN(os.Stdout, r, 4); err != nil {
		log.Fatal(err)
	}

}

```

```go
Output:
some

```

Share Format Run

```go
func Pipe() (*PipeReader, *PipeWriter)
```

Pipe creates a synchronous in-memory pipe. It can be used to connect code expecting an io.Reader with code expecting an io.Writer.

Reads and Writes on the pipe are matched one to one except when multiple Reads are needed to consume a single Write. That is, each Write to the PipeWriter blocks until it has satisfied one or more Reads from the PipeReader that fully consume the written data. The data is copied directly from the Write to the corresponding Read (or Reads); there is no internal buffering.

It is safe to call Read and Write in parallel with each other or with Close. Parallel calls to Read and parallel calls to Write are also safe: the individual calls will be gated sequentially.

```go

package main

import (
	"fmt"
	"io"
	"log"
	"os"
)

func main() {
	r, w := io.Pipe()

go func() {
		fmt.Fprint(w, "some io.Reader stream to be read\n")
		w.Close()
	}()

if _, err := io.Copy(os.Stdout, r); err != nil {
		log.Fatal(err)
	}

}

```

```go
Output:
some io.Reader stream to be read

```

Share Format Run

```go
func ReadAll(r Reader) ([]byte, error)
```

ReadAll reads from r until an error or EOF and returns the data it read. A successful call returns err == nil, not err == EOF. Because ReadAll is defined to read from src until EOF, it does not treat an EOF from Read as an error to be reported.

```go

package main

import (
	"fmt"
	"io"
	"log"
	"strings"
)

func main() {
	r := strings.NewReader("Go is a general-purpose language designed with systems programming in mind.")

b, err := io.ReadAll(r)
	if err != nil {
		log.Fatal(err)
	}

fmt.Printf("%s", b)

}

```

```go
Output:
Go is a general-purpose language designed with systems programming in mind.

```

Share Format Run

```go
func ReadAtLeast(r Reader, buf []byte, min int) (n int, err error)
```
