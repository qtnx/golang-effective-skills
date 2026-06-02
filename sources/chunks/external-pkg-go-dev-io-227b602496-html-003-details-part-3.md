---
source_name: "External Linked Documentation"
source_url: "https://pkg.go.dev/io"
source_path: "sources/raw/external/pkg-go-dev-io-227b602496.html"
license_ref: ""
---

if _, err := io.Copy(os.Stdout, lr); err != nil {
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
func MultiReader(readers ...Reader) Reader
```

MultiReader returns a Reader that's the logical concatenation of the provided input readers. They're read sequentially. Once all inputs have returned EOF, Read will return EOF. If any of the readers return a non-nil, non-EOF error, Read will return that error.

```go

package main

import (
	"io"
	"log"
	"os"
	"strings"
)

func main() {
	r1 := strings.NewReader("first reader ")
	r2 := strings.NewReader("second reader ")
	r3 := strings.NewReader("third reader\n")
	r := io.MultiReader(r1, r2, r3)

if _, err := io.Copy(os.Stdout, r); err != nil {
		log.Fatal(err)
	}

}

```

```go
Output:
first reader second reader third reader

```

Share Format Run

```go
func TeeReader(r Reader, w Writer) Reader
```

TeeReader returns a Reader that writes to w what it reads from r. All reads from r performed through it are matched with corresponding writes to w. There is no internal buffering - the write must complete before the read completes. Any error encountered while writing is reported as a read error.

```go

package main

import (
	"io"
	"log"
	"os"
	"strings"
)

func main() {
	var r io.Reader = strings.NewReader("some io.Reader stream to be read\n")

r = io.TeeReader(r, os.Stdout)

// Everything read from r will be copied to stdout.
	if _, err := io.ReadAll(r); err != nil {
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
type ReaderAt interface {
	ReadAt(p []byte, off int64) (n int, err error)
}
```

ReaderAt is the interface that wraps the basic ReadAt method.

ReadAt reads len(p) bytes into p starting at offset off in the underlying input source. It returns the number of bytes read (0 <= n <= len(p)) and any error encountered.

When ReadAt returns n < len(p), it returns a non-nil error explaining why more bytes were not returned. In this respect, ReadAt is stricter than Read.

Even if ReadAt returns n < len(p), it may use all of p as scratch space during the call. If some data is available but not len(p) bytes, ReadAt blocks until either all the data is available or an error occurs. In this respect ReadAt is different from Read.

If the n = len(p) bytes returned by ReadAt are at the end of the input source, ReadAt may return either err == EOF or err == nil.

If ReadAt is reading from an input source with a seek offset, ReadAt should not affect nor be affected by the underlying seek offset.

Clients of ReadAt can execute parallel ReadAt calls on the same input source.

Implementations must not retain p.

```go
type ReaderFrom interface {
	ReadFrom(r Reader) (n int64, err error)
}
```

ReaderFrom is the interface that wraps the ReadFrom method.

ReadFrom reads data from r until EOF or error. The return value n is the number of bytes read. Any error except EOF encountered during the read is also returned.

The Copy function uses ReaderFrom if available.

```go
type RuneReader interface {
	ReadRune() (r rune, size int, err error)
}
```

RuneReader is the interface that wraps the ReadRune method.

ReadRune reads a single encoded Unicode character and returns the rune and its size in bytes. If no character is available, err will be set.

```go
type RuneScanner interface {
	RuneReader
	UnreadRune() error
}
```

RuneScanner is the interface that adds the UnreadRune method to the basic ReadRune method.

UnreadRune causes the next call to ReadRune to return the last rune read. If the last operation was not a successful call to ReadRune, UnreadRune may return an error, unread the last rune read (or the rune prior to the last-unread rune), or (in implementations that support the Seeker interface) seek to the start of the rune before the current offset.

```go
type SectionReader struct {
	// contains filtered or unexported fields
}
```

SectionReader implements Read, Seek, and ReadAt on a section of an underlying ReaderAt.

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
	s := io.NewSectionReader(r, 5, 17)

if _, err := io.Copy(os.Stdout, s); err != nil {
		log.Fatal(err)
	}

}

```

```go
Output:
io.Reader stream

```

Share Format Run

```go
func NewSectionReader(r ReaderAt, off int64, n int64) *SectionReader
```

NewSectionReader returns a SectionReader that reads from r starting at offset off and stops with EOF after n bytes.

```go
func (s *SectionReader) Outer() (r ReaderAt, off int64, n int64)
```

Outer returns the underlying ReaderAt and offsets for the section.

The returned values are the same that were passed to NewSectionReader when the SectionReader was created.

```go
func (s *SectionReader) Read(p []byte) (n int, err error)
```

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
	s := io.NewSectionReader(r, 5, 17)

buf := make([]byte, 9)
	if _, err := s.Read(buf); err != nil {
		log.Fatal(err)
	}

fmt.Printf("%s\n", buf)

}

```

```go
Output:
io.Reader

```

Share Format Run

```go
func (s *SectionReader) ReadAt(p []byte, off int64) (n int, err error)
```

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
	s := io.NewSectionReader(r, 5, 17)

buf := make([]byte, 6)
	if _, err := s.ReadAt(buf, 10); err != nil {
		log.Fatal(err)
	}

fmt.Printf("%s\n", buf)

}

```

```go
Output:
stream

```

Share Format Run

```go
func (s *SectionReader) Seek(offset int64, whence int) (int64, error)
```

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
	s := io.NewSectionReader(r, 5, 17)

if _, err := s.Seek(10, io.SeekStart); err != nil {
		log.Fatal(err)
	}

if _, err := io.Copy(os.Stdout, s); err != nil {
		log.Fatal(err)
	}

}

```

```go
Output:
stream

```

Share Format Run

```go
func (s *SectionReader) Size() int64
```

Size returns the size of the section in bytes.

```go

package main

import (
	"fmt"
	"io"
	"strings"
)

func main() {
	r := strings.NewReader("some io.Reader stream to be read\n")
	s := io.NewSectionReader(r, 5, 17)

fmt.Println(s.Size())

}

```

```go
Output:
17

```

Share Format Run

```go
type Seeker interface {
	Seek(offset int64, whence int) (int64, error)
}
```

Seeker is the interface that wraps the basic Seek method.

Seek sets the offset for the next Read or Write to offset, interpreted according to whence: SeekStart means relative to the start of the file, SeekCurrent means relative to the current offset, and SeekEnd means relative to the end (for example, offset = -2 specifies the penultimate byte of the file). Seek returns the new offset relative to the start of the file or an error, if any.

Seeking to an offset before the start of the file is an error. Seeking to any positive offset may be allowed, but if the new offset exceeds the size of the underlying object the behavior of subsequent I/O operations is implementation-dependent.

```go
type StringWriter interface {
	WriteString(s string) (n int, err error)
}
```

StringWriter is the interface that wraps the WriteString method.

```go
type WriteCloser interface {
	Writer
	Closer
}
```

WriteCloser is the interface that groups the basic Write and Close methods.

```go
type WriteSeeker interface {
	Writer
	Seeker
}
```

WriteSeeker is the interface that groups the basic Write and Seek methods.

```go
type Writer interface {
	Write(p []byte) (n int, err error)
}
```

Writer is the interface that wraps the basic Write method.

Write writes len(p) bytes from p to the underlying data stream. It returns the number of bytes written from p (0 <= n <= len(p)) and any error encountered that caused the write to stop early. Write must return a non-nil error if it returns n < len(p). Write must not modify the slice data, even temporarily.

Implementations must not retain p.

```go
var Discard Writer = discard{}
```

Discard is a Writer on which all Write calls succeed without doing anything.

```go
func MultiWriter(writers ...Writer) Writer
```

MultiWriter creates a writer that duplicates its writes to all the provided writers, similar to the Unix tee(1) command.

Each write is written to each listed writer, one at a time. If a listed writer returns an error, that overall write operation stops and returns the error; it does not continue down the list.

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

var buf1, buf2 strings.Builder
	w := io.MultiWriter(&buf1, &buf2)

if _, err := io.Copy(w, r); err != nil {
		log.Fatal(err)
	}

fmt.Print(buf1.String())
	fmt.Print(buf2.String())

}

```

```go
Output:
some io.Reader stream to be read
some io.Reader stream to be read

```

Share Format Run

```go
type WriterAt interface {
	WriteAt(p []byte, off int64) (n int, err error)
}
```

WriterAt is the interface that wraps the basic WriteAt method.

WriteAt writes len(p) bytes from p to the underlying data stream at offset off. It returns the number of bytes written from p (0 <= n <= len(p)) and any error encountered that caused the write to stop early. WriteAt must return a non-nil error if it returns n < len(p).

If WriteAt is writing to a destination with a seek offset, WriteAt should not affect nor be affected by the underlying seek offset.

Clients of WriteAt can execute parallel WriteAt calls on the same destination if the ranges do not overlap.

Implementations must not retain p.

```go
type WriterTo interface {
	WriteTo(w Writer) (n int64, err error)
}
```

WriterTo is the interface that wraps the WriteTo method.
