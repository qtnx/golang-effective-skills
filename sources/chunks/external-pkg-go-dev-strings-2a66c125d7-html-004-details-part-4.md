---
source_name: "External Linked Documentation"
source_url: "https://pkg.go.dev/strings"
source_path: "sources/raw/external/pkg-go-dev-strings-2a66c125d7.html"
license_ref: ""
---

```go
func TrimRight(s, cutset string) string
```

TrimRight returns a slice of the string s, with all trailing Unicode code points contained in cutset removed.

To remove a suffix, use TrimSuffix instead.

```go

package main

import (
	"fmt"
	"strings"
)

func main() {
	fmt.Print(strings.TrimRight("¡¡¡Hello, Gophers!!!", "!¡"))
}

```

```go
Output:
¡¡¡Hello, Gophers

```

Share Format Run

```go
func TrimRightFunc(s string, f func(rune) bool) string
```

TrimRightFunc returns a slice of the string s with all trailing Unicode code points c satisfying f(c) removed.

```go

package main

import (
	"fmt"
	"strings"
	"unicode"
)

func main() {
	fmt.Print(strings.TrimRightFunc("¡¡¡Hello, Gophers!!!", func(r rune) bool {
		return !unicode.IsLetter(r) && !unicode.IsNumber(r)
	}))
}

```

```go
Output:
¡¡¡Hello, Gophers

```

Share Format Run

```go
func TrimSpace(s string) string
```

TrimSpace returns a slice (substring) of the string s, with all leading and trailing white space removed, as defined by Unicode.

```go

package main

import (
	"fmt"
	"strings"
)

func main() {
	fmt.Println(strings.TrimSpace(" \t\n Hello, Gophers \n\t\r\n"))
}

```

```go
Output:
Hello, Gophers

```

Share Format Run

```go
func TrimSuffix(s, suffix string) string
```

TrimSuffix returns s without the provided trailing suffix string. If s doesn't end with suffix, s is returned unchanged.

```go

package main

import (
	"fmt"
	"strings"
)

func main() {
	var s = "¡¡¡Hello, Gophers!!!"
	s = strings.TrimSuffix(s, ", Gophers!!!")
	s = strings.TrimSuffix(s, ", Marmots!!!")
	fmt.Print(s)
}

```

```go
Output:
¡¡¡Hello

```

Share Format Run

```go
type Builder struct {
	// contains filtered or unexported fields
}
```

A Builder is used to efficiently build a string using Builder.Write methods. It minimizes memory copying. The zero value is ready to use. Do not copy a non-zero Builder.

```go

package main

import (
	"fmt"
	"strings"
)

func main() {
	var b strings.Builder
	for i := 3; i >= 1; i-- {
		fmt.Fprintf(&b, "%d...", i)
	}
	b.WriteString("ignition")
	fmt.Println(b.String())

}

```

```go
Output:
3...2...1...ignition

```

Share Format Run

```go
func (b *Builder) Cap() int
```

Cap returns the capacity of the builder's underlying byte slice. It is the total space allocated for the string being built and includes any bytes already written.

```go
func (b *Builder) Grow(n int)
```

Grow grows b's capacity, if necessary, to guarantee space for another n bytes. After Grow(n), at least n bytes can be written to b without another allocation. If n is negative, Grow panics.

```go
func (b *Builder) Len() int
```

Len returns the number of accumulated bytes; b.Len() == len(b.String()).

```go
func (b *Builder) Reset()
```

Reset resets the Builder to be empty.

```go
func (b *Builder) String() string
```

String returns the accumulated string.

```go
func (b *Builder) Write(p []byte) (int, error)
```

Write appends the contents of p to b's buffer. Write always returns len(p), nil.

```go
func (b *Builder) WriteByte(c byte) error
```

WriteByte appends the byte c to b's buffer. The returned error is always nil.

```go
func (b *Builder) WriteRune(r rune) (int, error)
```

WriteRune appends the UTF-8 encoding of Unicode code point r to b's buffer. It returns the length of r and a nil error.

```go
func (b *Builder) WriteString(s string) (int, error)
```

WriteString appends the contents of s to b's buffer. It returns the length of s and a nil error.

```go
type Reader struct {
	// contains filtered or unexported fields
}
```

A Reader implements the io.Reader, io.ReaderAt, io.ByteReader, io.ByteScanner, io.RuneReader, io.RuneScanner, io.Seeker, and io.WriterTo interfaces by reading from a string. The zero value for Reader operates like a Reader of an empty string.

```go
func NewReader(s string) *Reader
```

NewReader returns a new Reader reading from s. It is similar to bytes.NewBufferString but more efficient and non-writable.

```go
func (r *Reader) Len() int
```

Len returns the number of bytes of the unread portion of the string.

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
func (r *Reader) Reset(s string)
```

Reset resets the Reader to be reading from s.

```go
func (r *Reader) Seek(offset int64, whence int) (int64, error)
```

Seek implements the io.Seeker interface.

```go
func (r *Reader) Size() int64
```

Size returns the original length of the underlying string. Size is the number of bytes available for reading via Reader.ReadAt. The returned value is always the same and is not affected by calls to any other method.

```go
func (r *Reader) UnreadByte() error
```

UnreadByte implements the io.ByteScanner interface.

```go
func (r *Reader) UnreadRune() error
```

UnreadRune implements the io.RuneScanner interface.

```go
func (r *Reader) WriteTo(w io.Writer) (n int64, err error)
```

WriteTo implements the io.WriterTo interface.

```go
type Replacer struct {
	// contains filtered or unexported fields
}
```

Replacer replaces a list of strings with replacements. It is safe for concurrent use by multiple goroutines.

```go
func NewReplacer(oldnew ...string) *Replacer
```

NewReplacer returns a new Replacer from a list of old, new string pairs. Replacements are performed in the order they appear in the target string, without overlapping matches. The old string comparisons are done in argument order.

NewReplacer panics if given an odd number of arguments.

```go

package main

import (
	"fmt"
	"strings"
)

func main() {
	r := strings.NewReplacer("<", "&lt;", ">", "&gt;")
	fmt.Println(r.Replace("This is <b>HTML</b>!"))
}

```

```go
Output:
This is &lt;b&gt;HTML&lt;/b&gt;!

```

Share Format Run

```go
func (r *Replacer) Replace(s string) string
```

Replace returns a copy of s with all replacements performed.

```go
func (r *Replacer) WriteString(w io.Writer, s string) (n int, err error)
```

WriteString writes s to w with all replacements performed.

##   Source Files ¶
 View all Source files <https://cs.opensource.google/go/go/+/go1.26.3:src/strings>

- builder.go <https://cs.opensource.google/go/go/+/go1.26.3:src/strings/builder.go>
- clone.go <https://cs.opensource.google/go/go/+/go1.26.3:src/strings/clone.go>
- compare.go <https://cs.opensource.google/go/go/+/go1.26.3:src/strings/compare.go>
- iter.go <https://cs.opensource.google/go/go/+/go1.26.3:src/strings/iter.go>
- reader.go <https://cs.opensource.google/go/go/+/go1.26.3:src/strings/reader.go>
- replace.go <https://cs.opensource.google/go/go/+/go1.26.3:src/strings/replace.go>
- search.go <https://cs.opensource.google/go/go/+/go1.26.3:src/strings/search.go>
- strings.go <https://cs.opensource.google/go/go/+/go1.26.3:src/strings/strings.go>

Click to show internal directories.
  Click to hide internal directories.

Close

**?** : This menu   **/** : Search site   **f** or **F** : Jump to   **y** or **Y**  : Canonical URL
  Close
