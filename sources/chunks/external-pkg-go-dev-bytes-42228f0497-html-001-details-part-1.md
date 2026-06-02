---
source_name: "External Linked Documentation"
source_url: "https://pkg.go.dev/bytes"
source_path: "sources/raw/external/pkg-go-dev-bytes-42228f0497.html"
license_ref: ""
---

bytes package - bytes - Go Packages
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
   Rendered for <https://go.dev/about#build-context>  linux/amd64 windows/amd64 darwin/amd64 js/wasm

Package bytes implements functions for the manipulation of byte slices. It is analogous to the facilities of the strings package.

- Constants
- Variables
-  func Clone(b []byte) []byte
-  func Compare(a, b []byte) int
-  func Contains(b, subslice []byte) bool
-  func ContainsAny(b []byte, chars string) bool
-  func ContainsFunc(b []byte, f func(rune) bool) bool
-  func ContainsRune(b []byte, r rune) bool
-  func Count(s, sep []byte) int
-  func Cut(s, sep []byte) (before, after []byte, found bool)
-  func CutPrefix(s, prefix []byte) (after []byte, found bool)
-  func CutSuffix(s, suffix []byte) (before []byte, found bool)
-  func Equal(a, b []byte) bool
-  func EqualFold(s, t []byte) bool
-  func Fields(s []byte) [][]byte
-  func FieldsFunc(s []byte, f func(rune) bool) [][]byte
-  func FieldsFuncSeq(s []byte, f func(rune) bool) iter.Seq[[]byte]
-  func FieldsSeq(s []byte) iter.Seq[[]byte]
-  func HasPrefix(s, prefix []byte) bool
-  func HasSuffix(s, suffix []byte) bool
-  func Index(s, sep []byte) int
-  func IndexAny(s []byte, chars string) int
-  func IndexByte(b []byte, c byte) int
-  func IndexFunc(s []byte, f func(r rune) bool) int
-  func IndexRune(s []byte, r rune) int
-  func Join(s [][]byte, sep []byte) []byte
-  func LastIndex(s, sep []byte) int
-  func LastIndexAny(s []byte, chars string) int
-  func LastIndexByte(s []byte, c byte) int
-  func LastIndexFunc(s []byte, f func(r rune) bool) int
-  func Lines(s []byte) iter.Seq[[]byte]
-  func Map(mapping func(r rune) rune, s []byte) []byte
-  func Repeat(b []byte, count int) []byte
-  func Replace(s, old, new []byte, n int) []byte
-  func ReplaceAll(s, old, new []byte) []byte
-  func Runes(s []byte) []rune
-  func Split(s, sep []byte) [][]byte
-  func SplitAfter(s, sep []byte) [][]byte
-  func SplitAfterN(s, sep []byte, n int) [][]byte
-  func SplitAfterSeq(s, sep []byte) iter.Seq[[]byte]
-  func SplitN(s, sep []byte, n int) [][]byte
-  func SplitSeq(s, sep []byte) iter.Seq[[]byte]
-  func Title(s []byte) []bytedeprecated
-  func ToLower(s []byte) []byte
-  func ToLowerSpecial(c unicode.SpecialCase, s []byte) []byte
-  func ToTitle(s []byte) []byte
-  func ToTitleSpecial(c unicode.SpecialCase, s []byte) []byte
-  func ToUpper(s []byte) []byte
-  func ToUpperSpecial(c unicode.SpecialCase, s []byte) []byte
-  func ToValidUTF8(s, replacement []byte) []byte
-  func Trim(s []byte, cutset string) []byte
-  func TrimFunc(s []byte, f func(r rune) bool) []byte
-  func TrimLeft(s []byte, cutset string) []byte
-  func TrimLeftFunc(s []byte, f func(r rune) bool) []byte
-  func TrimPrefix(s, prefix []byte) []byte
-  func TrimRight(s []byte, cutset string) []byte
-  func TrimRightFunc(s []byte, f func(r rune) bool) []byte
-  func TrimSpace(s []byte) []byte
-  func TrimSuffix(s, suffix []byte) []byte
-  type Buffer
-
-  func NewBuffer(buf []byte) *Buffer
-  func NewBufferString(s string) *Buffer

-
-  func (b *Buffer) Available() int
-  func (b *Buffer) AvailableBuffer() []byte
-  func (b *Buffer) Bytes() []byte
-  func (b *Buffer) Cap() int
-  func (b *Buffer) Grow(n int)
-  func (b *Buffer) Len() int
-  func (b *Buffer) Next(n int) []byte
-  func (b *Buffer) Peek(n int) ([]byte, error)
-  func (b *Buffer) Read(p []byte) (n int, err error)
-  func (b *Buffer) ReadByte() (byte, error)
-  func (b *Buffer) ReadBytes(delim byte) (line []byte, err error)
-  func (b *Buffer) ReadFrom(r io.Reader) (n int64, err error)
-  func (b *Buffer) ReadRune() (r rune, size int, err error)
-  func (b *Buffer) ReadString(delim byte) (line string, err error)
-  func (b *Buffer) Reset()
-  func (b *Buffer) String() string
-  func (b *Buffer) Truncate(n int)
-  func (b *Buffer) UnreadByte() error
-  func (b *Buffer) UnreadRune() error
-  func (b *Buffer) Write(p []byte) (n int, err error)
-  func (b *Buffer) WriteByte(c byte) error
-  func (b *Buffer) WriteRune(r rune) (n int, err error)
-  func (b *Buffer) WriteString(s string) (n int, err error)
-  func (b *Buffer) WriteTo(w io.Writer) (n int64, err error)

-  type Reader
-
-  func NewReader(b []byte) *Reader

-
-  func (r *Reader) Len() int
-  func (r *Reader) Read(b []byte) (n int, err error)
-  func (r *Reader) ReadAt(b []byte, off int64) (n int, err error)
-  func (r *Reader) ReadByte() (byte, error)
-  func (r *Reader) ReadRune() (ch rune, size int, err error)
-  func (r *Reader) Reset(b []byte)
-  func (r *Reader) Seek(offset int64, whence int) (int64, error)
-  func (r *Reader) Size() int64
-  func (r *Reader) UnreadByte() error
-  func (r *Reader) UnreadRune() error
-  func (r *Reader) WriteTo(w io.Writer) (n int64, err error)

- Buffer
- Buffer (Reader)
- Buffer.AvailableBuffer
- Buffer.Bytes
- Buffer.Cap
- Buffer.Grow
- Buffer.Len
- Buffer.Next
- Buffer.Read
- Buffer.ReadByte
- Clone
- Compare
- Compare (Search)
- Contains
- ContainsAny
- ContainsFunc
- ContainsRune
- Count
- Cut
- CutPrefix
- CutSuffix
- Equal
- EqualFold
- Fields
- FieldsFunc
- FieldsFuncSeq
- FieldsSeq
- HasPrefix
- HasSuffix
- Index
- IndexAny
- IndexByte
- IndexFunc
- IndexRune
- Join
- LastIndex
- LastIndexAny
- LastIndexByte
- LastIndexFunc
- Lines
- Map
- Reader.Len
- Repeat
- Replace
- ReplaceAll
- Runes
- Split
- SplitAfter
- SplitAfterN
- SplitAfterSeq
- SplitN
- SplitSeq
- Title
- ToLower
- ToLowerSpecial
- ToTitle
- ToTitleSpecial
- ToUpper
- ToUpperSpecial
- ToValidUTF8
- Trim
- TrimFunc
- TrimLeft
- TrimLeftFunc
- TrimPrefix
- TrimRight
- TrimRightFunc
- TrimSpace
- TrimSuffix

View Source <https://cs.opensource.google/go/go/+/go1.26.3:src/bytes/buffer.go;l=218>
```go
const MinRead = 512
```

MinRead is the minimum slice size passed to a Buffer.Read call by Buffer.ReadFrom. As long as the Buffer has at least MinRead bytes beyond what is required to hold the contents of r, Buffer.ReadFrom will not grow the underlying buffer.

View Source <https://cs.opensource.google/go/go/+/go1.26.3:src/bytes/buffer.go;l=50>
```go
var ErrTooLarge = errors.New("bytes.Buffer: too large")
```

ErrTooLarge is passed to panic if memory cannot be allocated to store data in a buffer.

```go
func Clone(b []byte) []byte
```

Clone returns a copy of b[:len(b)]. The result may have additional unused capacity. Clone(nil) returns nil.

```go

package main

import (
	"bytes"
	"fmt"
)

func main() {
	b := []byte("abc")
	clone := bytes.Clone(b)
	fmt.Printf("%s\n", clone)
	clone[0] = 'd'
	fmt.Printf("%s\n", b)
	fmt.Printf("%s\n", clone)
}

```

```go
Output:
abc
abc
dbc

```

Share Format Run

```go
func Compare(a, b []byte) int
```

Compare returns an integer comparing two byte slices lexicographically. The result will be 0 if a == b, -1 if a < b, and +1 if a > b. A nil argument is equivalent to an empty slice.

```go

package main

import (
	"bytes"
)

func main() {
	// Interpret Compare's result by comparing it to zero.
	var a, b []byte
	if bytes.Compare(a, b) < 0 {
		// a less b
	}
	if bytes.Compare(a, b) <= 0 {
		// a less or equal b
	}
	if bytes.Compare(a, b) > 0 {
		// a greater b
	}
	if bytes.Compare(a, b) >= 0 {
		// a greater or equal b
	}

// Prefer Equal to Compare for equality comparisons.
	if bytes.Equal(a, b) {
		// a equal b
	}
	if !bytes.Equal(a, b) {
		// a not equal b
	}
}

```

```go
Output:

```

Share Format Run

```go
func Contains(b, subslice []byte) bool
```

Contains reports whether subslice is within b.

```go

package main

import (
	"bytes"
	"fmt"
)

func main() {
	fmt.Println(bytes.Contains([]byte("seafood"), []byte("foo")))
	fmt.Println(bytes.Contains([]byte("seafood"), []byte("bar")))
	fmt.Println(bytes.Contains([]byte("seafood"), []byte("")))
	fmt.Println(bytes.Contains([]byte(""), []byte("")))
}

```

```go
Output:
true
false
true
true

```

Share Format Run

```go
func ContainsAny(b []byte, chars string) bool
```

ContainsAny reports whether any of the UTF-8-encoded code points in chars are within b.

```go

package main

import (
	"bytes"
	"fmt"
)

func main() {
	fmt.Println(bytes.ContainsAny([]byte("I like seafood."), "fÄo!"))
	fmt.Println(bytes.ContainsAny([]byte("I like seafood."), "去是伟大的."))
	fmt.Println(bytes.ContainsAny([]byte("I like seafood."), ""))
	fmt.Println(bytes.ContainsAny([]byte(""), ""))
}

```

```go
Output:
true
true
false
false

```

Share Format Run

```go
func ContainsFunc(b []byte, f func(rune) bool) bool
```

ContainsFunc reports whether any of the UTF-8-encoded code points r within b satisfy f(r).

```go

package main

import (
	"bytes"
	"fmt"
)

func main() {
	f := func(r rune) bool {
		return r >= 'a' && r <= 'z'
	}
	fmt.Println(bytes.ContainsFunc([]byte("HELLO"), f))
	fmt.Println(bytes.ContainsFunc([]byte("World"), f))
}

```

```go
Output:
false
true

```

Share Format Run

```go
func ContainsRune(b []byte, r rune) bool
```

ContainsRune reports whether the rune is contained in the UTF-8-encoded byte slice b.

```go

package main

import (
	"bytes"
	"fmt"
)

func main() {
	fmt.Println(bytes.ContainsRune([]byte("I like seafood."), 'f'))
	fmt.Println(bytes.ContainsRune([]byte("I like seafood."), 'ö'))
	fmt.Println(bytes.ContainsRune([]byte("去是伟大的!"), '大'))
	fmt.Println(bytes.ContainsRune([]byte("去是伟大的!"), '!'))
	fmt.Println(bytes.ContainsRune([]byte(""), '@'))
}

```

```go
Output:
true
false
true
true
false

```

Share Format Run

```go
func Count(s, sep []byte) int
```

Count counts the number of non-overlapping instances of sep in s. If sep is an empty slice, Count returns 1 + the number of UTF-8-encoded code points in s.

```go

package main

import (
	"bytes"
	"fmt"
)

func main() {
	fmt.Println(bytes.Count([]byte("cheese"), []byte("e")))
	fmt.Println(bytes.Count([]byte("five"), []byte(""))) // before & after each rune
}

```

```go
Output:
3
5

```

Share Format Run

```go
func Cut(s, sep []byte) (before, after []byte, found bool)
```

Cut slices s around the first instance of sep, returning the text before and after sep. The found result reports whether sep appears in s. If sep does not appear in s, cut returns s, nil, false.

Cut returns slices of the original slice s, not copies.

```go

package main

import (
	"bytes"
	"fmt"
)
