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

## Links

-    Report a Vulnerability  <https://go.dev/security/policy>

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

func main() {
	show := func(s, sep string) {
		before, after, found := bytes.Cut([]byte(s), []byte(sep))
		fmt.Printf("Cut(%q, %q) = %q, %q, %v\n", s, sep, before, after, found)
	}
	show("Gopher", "Go")
	show("Gopher", "ph")
	show("Gopher", "er")
	show("Gopher", "Badger")
}

```

```go
Output:
Cut("Gopher", "Go") = "", "pher", true
Cut("Gopher", "ph") = "Go", "er", true
Cut("Gopher", "er") = "Goph", "", true
Cut("Gopher", "Badger") = "Gopher", "", false

```

 Share Format Run

```go
func CutPrefix(s, prefix []byte) (after []byte, found bool)
```

CutPrefix returns s without the provided leading prefix byte slice and reports whether it found the prefix. If s doesn't start with prefix, CutPrefix returns s, false. If prefix is the empty byte slice, CutPrefix returns s, true.

CutPrefix returns slices of the original slice s, not copies.

```go

package main

import (
	"bytes"
	"fmt"
)

func main() {
	show := func(s, prefix string) {
		after, found := bytes.CutPrefix([]byte(s), []byte(prefix))
		fmt.Printf("CutPrefix(%q, %q) = %q, %v\n", s, prefix, after, found)
	}
	show("Gopher", "Go")
	show("Gopher", "ph")
}

```

```go
Output:
CutPrefix("Gopher", "Go") = "pher", true
CutPrefix("Gopher", "ph") = "Gopher", false

```

 Share Format Run

```go
func CutSuffix(s, suffix []byte) (before []byte, found bool)
```

CutSuffix returns s without the provided ending suffix byte slice and reports whether it found the suffix. If s doesn't end with suffix, CutSuffix returns s, false. If suffix is the empty byte slice, CutSuffix returns s, true.

CutSuffix returns slices of the original slice s, not copies.

```go

package main

import (
	"bytes"
	"fmt"
)

func main() {
	show := func(s, suffix string) {
		before, found := bytes.CutSuffix([]byte(s), []byte(suffix))
		fmt.Printf("CutSuffix(%q, %q) = %q, %v\n", s, suffix, before, found)
	}
	show("Gopher", "Go")
	show("Gopher", "er")
}

```

```go
Output:
CutSuffix("Gopher", "Go") = "Gopher", false
CutSuffix("Gopher", "er") = "Goph", true

```

 Share Format Run

```go
func Equal(a, b []byte) bool
```

Equal reports whether a and b are the same length and contain the same bytes. A nil argument is equivalent to an empty slice.

```go

package main

import (
	"bytes"
	"fmt"
)

func main() {
	fmt.Println(bytes.Equal([]byte("Go"), []byte("Go")))
	fmt.Println(bytes.Equal([]byte("Go"), []byte("C++")))
}

```

```go
Output:
true
false

```

 Share Format Run

```go
func EqualFold(s, t []byte) bool
```

EqualFold reports whether s and t, interpreted as UTF-8 strings, are equal under simple Unicode case-folding, which is a more general form of case-insensitivity.

```go

package main

import (
	"bytes"
	"fmt"
)

func main() {
	fmt.Println(bytes.EqualFold([]byte("Go"), []byte("go")))
}

```

```go
Output:
true

```

 Share Format Run

```go
func Fields(s []byte) [][]byte
```

Fields interprets s as a sequence of UTF-8-encoded code points. It splits the slice s around each instance of one or more consecutive white space characters, as defined by unicode.IsSpace, returning a slice of subslices of s or an empty slice if s contains only white space. Every element of the returned slice is non-empty. Unlike Split, leading and trailing runs of white space characters are discarded.

```go

package main

import (
	"bytes"
	"fmt"
)

func main() {
	fmt.Printf("Fields are: %q", bytes.Fields([]byte("  foo bar  baz   ")))
}

```

```go
Output:
Fields are: ["foo" "bar" "baz"]

```

 Share Format Run

```go
func FieldsFunc(s []byte, f func(rune) bool) [][]byte
```

FieldsFunc interprets s as a sequence of UTF-8-encoded code points. It splits the slice s at each run of code points c satisfying f(c) and returns a slice of subslices of s. If all code points in s satisfy f(c), or len(s) == 0, an empty slice is returned. Every element of the returned slice is non-empty. Unlike Split, leading and trailing runs of code points satisfying f(c) are discarded.

FieldsFunc makes no guarantees about the order in which it calls f(c) and assumes that f always returns the same value for a given c.

```go

package main

import (
	"bytes"
	"fmt"
	"unicode"
)

func main() {
	f := func(c rune) bool {
		return !unicode.IsLetter(c) && !unicode.IsNumber(c)
	}
	fmt.Printf("Fields are: %q", bytes.FieldsFunc([]byte("  foo1;bar2,baz3..."), f))
}

```

```go
Output:
Fields are: ["foo1" "bar2" "baz3"]

```

 Share Format Run

```go
func FieldsFuncSeq(s []byte, f func(rune) bool) iter.Seq[[]byte]
```

FieldsFuncSeq returns an iterator over subslices of s split around runs of Unicode code points satisfying f(c). The iterator yields the same subslices that would be returned by FieldsFunc(s), but without constructing a new slice containing the subslices.

```go

package main

import (
	"bytes"
	"fmt"
	"unicode"
)

func main() {
	text := []byte("The quick brown fox")
	fmt.Println("Split on whitespace(similar to FieldsSeq):")
	for word := range bytes.FieldsFuncSeq(text, unicode.IsSpace) {
		fmt.Printf("%q\n", word)
	}

	mixedText := []byte("abc123def456ghi")
	fmt.Println("\nSplit on digits:")
	for word := range bytes.FieldsFuncSeq(mixedText, unicode.IsDigit) {
		fmt.Printf("%q\n", word)
	}

}

```

```go
Output:
Split on whitespace(similar to FieldsSeq):
"The"
"quick"
"brown"
"fox"

Split on digits:
"abc"
"def"
"ghi"

```

 Share Format Run

```go
func FieldsSeq(s []byte) iter.Seq[[]byte]
```

FieldsSeq returns an iterator over subslices of s split around runs of whitespace characters, as defined by unicode.IsSpace. The iterator yields the same subslices that would be returned by Fields(s), but without constructing a new slice containing the subslices.

```go

package main

import (
	"bytes"
	"fmt"
)

func main() {
	text := []byte("The quick brown fox")
	fmt.Println("Split byte slice into fields:")
	for word := range bytes.FieldsSeq(text) {
		fmt.Printf("%q\n", word)
	}

	textWithSpaces := []byte("  lots   of   spaces  ")
	fmt.Println("\nSplit byte slice with multiple spaces:")
	for word := range bytes.FieldsSeq(textWithSpaces) {
		fmt.Printf("%q\n", word)
	}

}

```

```go
Output:
Split byte slice into fields:
"The"
"quick"
"brown"
"fox"

Split byte slice with multiple spaces:
"lots"
"of"
"spaces"

```

 Share Format Run

```go
func HasPrefix(s, prefix []byte) bool
```

HasPrefix reports whether the byte slice s begins with prefix.

```go

package main

import (
	"bytes"
	"fmt"
)

func main() {
	fmt.Println(bytes.HasPrefix([]byte("Gopher"), []byte("Go")))
	fmt.Println(bytes.HasPrefix([]byte("Gopher"), []byte("C")))
	fmt.Println(bytes.HasPrefix([]byte("Gopher"), []byte("")))
}

```

```go
Output:
true
false
true

```

 Share Format Run

```go
func HasSuffix(s, suffix []byte) bool
```

HasSuffix reports whether the byte slice s ends with suffix.

```go

package main

import (
	"bytes"
	"fmt"
)

func main() {
	fmt.Println(bytes.HasSuffix([]byte("Amigo"), []byte("go")))
	fmt.Println(bytes.HasSuffix([]byte("Amigo"), []byte("O")))
	fmt.Println(bytes.HasSuffix([]byte("Amigo"), []byte("Ami")))
	fmt.Println(bytes.HasSuffix([]byte("Amigo"), []byte("")))
}

```

```go
Output:
true
false
false
true

```

 Share Format Run

```go
func Index(s, sep []byte) int
```

Index returns the index of the first instance of sep in s, or -1 if sep is not present in s.

```go

package main

import (
	"bytes"
	"fmt"
)

func main() {
	fmt.Println(bytes.Index([]byte("chicken"), []byte("ken")))
	fmt.Println(bytes.Index([]byte("chicken"), []byte("dmr")))
}

```

```go
Output:
4
-1

```

 Share Format Run

```go
func IndexAny(s []byte, chars string) int
```

IndexAny interprets s as a sequence of UTF-8-encoded Unicode code points. It returns the byte index of the first occurrence in s of any of the Unicode code points in chars. It returns -1 if chars is empty or if there is no code point in common.

```go

package main

import (
	"bytes"
	"fmt"
)

func main() {
	fmt.Println(bytes.IndexAny([]byte("chicken"), "aeiouy"))
	fmt.Println(bytes.IndexAny([]byte("crwth"), "aeiouy"))
}

```

```go
Output:
2
-1

```

 Share Format Run

```go
func IndexByte(b []byte, c byte) int
```

IndexByte returns the index of the first instance of c in b, or -1 if c is not present in b.

```go

package main

import (
	"bytes"
	"fmt"
)

func main() {
	fmt.Println(bytes.IndexByte([]byte("chicken"), byte('k')))
	fmt.Println(bytes.IndexByte([]byte("chicken"), byte('g')))
}

```

```go
Output:
4
-1

```

 Share Format Run

```go
func IndexFunc(s []byte, f func(r rune) bool) int
```

IndexFunc interprets s as a sequence of UTF-8-encoded code points. It returns the byte index in s of the first Unicode code point satisfying f(c), or -1 if none do.

```go

package main

import (
	"bytes"
	"fmt"
	"unicode"
)

func main() {
	f := func(c rune) bool {
		return unicode.Is(unicode.Han, c)
	}
	fmt.Println(bytes.IndexFunc([]byte("Hello, 世界"), f))
	fmt.Println(bytes.IndexFunc([]byte("Hello, world"), f))
}

```

```go
Output:
7
-1

```

 Share Format Run

```go
func IndexRune(s []byte, r rune) int
```

IndexRune interprets s as a sequence of UTF-8-encoded code points. It returns the byte index of the first occurrence in s of the given rune. It returns -1 if rune is not present in s. If r is utf8.RuneError, it returns the first instance of any invalid UTF-8 byte sequence.

```go

package main

import (
	"bytes"
	"fmt"
)

func main() {
	fmt.Println(bytes.IndexRune([]byte("chicken"), 'k'))
	fmt.Println(bytes.IndexRune([]byte("chicken"), 'd'))
}

```

```go
Output:
4
-1

```

 Share Format Run

```go
func Join(s [][]byte, sep []byte) []byte
```

Join concatenates the elements of s to create a new byte slice. The separator sep is placed between elements in the resulting slice.

```go

package main

import (
	"bytes"
	"fmt"
)

func main() {
	s := [][]byte{[]byte("foo"), []byte("bar"), []byte("baz")}
	fmt.Printf("%s", bytes.Join(s, []byte(", ")))
}

```

```go
Output:
foo, bar, baz

```

 Share Format Run

```go
func LastIndex(s, sep []byte) int
```

LastIndex returns the index of the last instance of sep in s, or -1 if sep is not present in s.

```go

package main

import (
	"bytes"
	"fmt"
)

func main() {
	fmt.Println(bytes.Index([]byte("go gopher"), []byte("go")))
	fmt.Println(bytes.LastIndex([]byte("go gopher"), []byte("go")))
	fmt.Println(bytes.LastIndex([]byte("go gopher"), []byte("rodent")))
}

```

```go
Output:
0
3
-1

```

 Share Format Run

```go
func LastIndexAny(s []byte, chars string) int
```

LastIndexAny interprets s as a sequence of UTF-8-encoded Unicode code points. It returns the byte index of the last occurrence in s of any of the Unicode code points in chars. It returns -1 if chars is empty or if there is no code point in common.

```go

package main

import (
	"bytes"
	"fmt"
)

func main() {
	fmt.Println(bytes.LastIndexAny([]byte("go gopher"), "MüQp"))
	fmt.Println(bytes.LastIndexAny([]byte("go 地鼠"), "地大"))
	fmt.Println(bytes.LastIndexAny([]byte("go gopher"), "z,!."))
}

```

```go
Output:
5
3
-1

```

 Share Format Run

```go
func LastIndexByte(s []byte, c byte) int
```

LastIndexByte returns the index of the last instance of c in s, or -1 if c is not present in s.

```go

package main

import (
	"bytes"
	"fmt"
)

func main() {
	fmt.Println(bytes.LastIndexByte([]byte("go gopher"), byte('g')))
	fmt.Println(bytes.LastIndexByte([]byte("go gopher"), byte('r')))
	fmt.Println(bytes.LastIndexByte([]byte("go gopher"), byte('z')))
}

```

```go
Output:
3
8
-1

```

 Share Format Run

```go
func LastIndexFunc(s []byte, f func(r rune) bool) int
```

LastIndexFunc interprets s as a sequence of UTF-8-encoded code points. It returns the byte index in s of the last Unicode code point satisfying f(c), or -1 if none do.

```go

package main

import (
	"bytes"
	"fmt"
	"unicode"
)

func main() {
	fmt.Println(bytes.LastIndexFunc([]byte("go gopher!"), unicode.IsLetter))
	fmt.Println(bytes.LastIndexFunc([]byte("go gopher!"), unicode.IsPunct))
	fmt.Println(bytes.LastIndexFunc([]byte("go gopher!"), unicode.IsNumber))
}

```

```go
Output:
8
9
-1

```

 Share Format Run

```go
func Lines(s []byte) iter.Seq[[]byte]
```

Lines returns an iterator over the newline-terminated lines in the byte slice s. The lines yielded by the iterator include their terminating newlines. If s is empty, the iterator yields no lines at all. If s does not end in a newline, the final yielded line will not end in a newline. It returns a single-use iterator.

```go

package main

import (
	"bytes"
	"fmt"
)

func main() {
	text := []byte("Hello\nWorld\nGo Programming\n")
	for line := range bytes.Lines(text) {
		fmt.Printf("%q\n", line)
	}

}

```

```go
Output:
"Hello\n"
"World\n"
"Go Programming\n"

```

 Share Format Run

```go
func Map(mapping func(r rune) rune, s []byte) []byte
```

Map returns a copy of the byte slice s with all its characters modified according to the mapping function. If mapping returns a negative value, the character is dropped from the byte slice with no replacement. The characters in s and the output are interpreted as UTF-8-encoded code points.

```go

package main

import (
	"bytes"
	"fmt"
)

func main() {
	rot13 := func(r rune) rune {
		switch {
		case r >= 'A' && r <= 'Z':
			return 'A' + (r-'A'+13)%26
		case r >= 'a' && r <= 'z':
			return 'a' + (r-'a'+13)%26
		}
		return r
	}
	fmt.Printf("%s\n", bytes.Map(rot13, []byte("'Twas brillig and the slithy gopher...")))
}

```

```go
Output:
'Gjnf oevyyvt naq gur fyvgul tbcure...

```

 Share Format Run

```go
func Repeat(b []byte, count int) []byte
```

Repeat returns a new byte slice consisting of count copies of b.

It panics if count is negative or if the result of (len(b) * count) overflows.

```go

package main

import (
	"bytes"
	"fmt"
)

func main() {
	fmt.Printf("ba%s", bytes.Repeat([]byte("na"), 2))
}

```

```go
Output:
banana

```

 Share Format Run

```go
func Replace(s, old, new []byte, n int) []byte
```

Replace returns a copy of the slice s with the first n non-overlapping instances of old replaced by new. If old is empty, it matches at the beginning of the slice and after each UTF-8 sequence, yielding up to k+1 replacements for a k-rune slice. If n < 0, there is no limit on the number of replacements.

```go

package main

import (
	"bytes"
	"fmt"
)

func main() {
	fmt.Printf("%s\n", bytes.Replace([]byte("oink oink oink"), []byte("k"), []byte("ky"), 2))
	fmt.Printf("%s\n", bytes.Replace([]byte("oink oink oink"), []byte("oink"), []byte("moo"), -1))
}

```

```go
Output:
oinky oinky oink
moo moo moo

```

 Share Format Run

```go
func ReplaceAll(s, old, new []byte) []byte
```

ReplaceAll returns a copy of the slice s with all non-overlapping instances of old replaced by new. If old is empty, it matches at the beginning of the slice and after each UTF-8 sequence, yielding up to k+1 replacements for a k-rune slice.

```go

package main

import (
	"bytes"
	"fmt"
)

func main() {
	fmt.Printf("%s\n", bytes.ReplaceAll([]byte("oink oink oink"), []byte("oink"), []byte("moo")))
}

```

```go
Output:
moo moo moo

```

 Share Format Run

```go
func Runes(s []byte) []rune
```

Runes interprets s as a sequence of UTF-8-encoded code points. It returns a slice of runes (Unicode code points) equivalent to s.

```go

package main

import (
	"bytes"
	"fmt"
)

func main() {
	rs := bytes.Runes([]byte("go gopher"))
	for _, r := range rs {
		fmt.Printf("%#U\n", r)
	}
}

```

```go
Output:
U+0067 'g'
U+006F 'o'
U+0020 ' '
U+0067 'g'
U+006F 'o'
U+0070 'p'
U+0068 'h'
U+0065 'e'
U+0072 'r'

```

 Share Format Run

```go
func Split(s, sep []byte) [][]byte
```

Split slices s into all subslices separated by sep and returns a slice of the subslices between those separators. If sep is empty, Split splits after each UTF-8 sequence. It is equivalent to SplitN with a count of -1.

To split around the first instance of a separator, see Cut.

```go

package main

import (
	"bytes"
	"fmt"
)

func main() {
	fmt.Printf("%q\n", bytes.Split([]byte("a,b,c"), []byte(",")))
	fmt.Printf("%q\n", bytes.Split([]byte("a man a plan a canal panama"), []byte("a ")))
	fmt.Printf("%q\n", bytes.Split([]byte(" xyz "), []byte("")))
	fmt.Printf("%q\n", bytes.Split([]byte(""), []byte("Bernardo O'Higgins")))
}

```

```go
Output:
["a" "b" "c"]
["" "man " "plan " "canal panama"]
[" " "x" "y" "z" " "]
[""]

```

 Share Format Run

```go
func SplitAfter(s, sep []byte) [][]byte
```

SplitAfter slices s into all subslices after each instance of sep and returns a slice of those subslices. If sep is empty, SplitAfter splits after each UTF-8 sequence. It is equivalent to SplitAfterN with a count of -1.

```go

package main

import (
	"bytes"
	"fmt"
)

func main() {
	fmt.Printf("%q\n", bytes.SplitAfter([]byte("a,b,c"), []byte(",")))
}

```

```go
Output:
["a," "b," "c"]

```

 Share Format Run

```go
func SplitAfterN(s, sep []byte, n int) [][]byte
```

SplitAfterN slices s into subslices after each instance of sep and returns a slice of those subslices. If sep is empty, SplitAfterN splits after each UTF-8 sequence. The count determines the number of subslices to return:

- n > 0: at most n subslices; the last subslice will be the unsplit remainder;
- n == 0: the result is nil (zero subslices);
- n < 0: all subslices.

```go

package main

import (
	"bytes"
	"fmt"
)

func main() {
	fmt.Printf("%q\n", bytes.SplitAfterN([]byte("a,b,c"), []byte(","), 2))
}

```

```go
Output:
["a," "b,c"]

```

 Share Format Run

```go
func SplitAfterSeq(s, sep []byte) iter.Seq[[]byte]
```

SplitAfterSeq returns an iterator over subslices of s split after each instance of sep. The iterator yields the same subslices that would be returned by SplitAfter(s, sep), but without constructing a new slice containing the subslices. It returns a single-use iterator.

```go

package main

import (
	"bytes"
	"fmt"
)

func main() {
	s := []byte("a,b,c,d")
	for part := range bytes.SplitAfterSeq(s, []byte(",")) {
		fmt.Printf("%q\n", part)
	}

}

```

```go
Output:
"a,"
"b,"
"c,"
"d"

```

 Share Format Run

```go
func SplitN(s, sep []byte, n int) [][]byte
```

SplitN slices s into subslices separated by sep and returns a slice of the subslices between those separators. If sep is empty, SplitN splits after each UTF-8 sequence. The count determines the number of subslices to return:

- n > 0: at most n subslices; the last subslice will be the unsplit remainder;
- n == 0: the result is nil (zero subslices);
- n < 0: all subslices.

To split around the first instance of a separator, see Cut.

```go

package main

import (
	"bytes"
	"fmt"
)

func main() {
	fmt.Printf("%q\n", bytes.SplitN([]byte("a,b,c"), []byte(","), 2))
	z := bytes.SplitN([]byte("a,b,c"), []byte(","), 0)
	fmt.Printf("%q (nil = %v)\n", z, z == nil)
}

```

```go
Output:
["a" "b,c"]
[] (nil = true)

```

 Share Format Run

```go
func SplitSeq(s, sep []byte) iter.Seq[[]byte]
```

SplitSeq returns an iterator over all subslices of s separated by sep. The iterator yields the same subslices that would be returned by Split(s, sep), but without constructing a new slice containing the subslices. It returns a single-use iterator.

```go

package main

import (
	"bytes"
	"fmt"
)

func main() {
	s := []byte("a,b,c,d")
	for part := range bytes.SplitSeq(s, []byte(",")) {
		fmt.Printf("%q\n", part)
	}

}

```

```go
Output:
"a"
"b"
"c"
"d"

```

 Share Format Run

```go
func Title(s []byte) []byte
```

Title treats s as UTF-8-encoded bytes and returns a copy with all Unicode letters that begin words mapped to their title case.

Deprecated: The rule Title uses for word boundaries does not handle Unicode punctuation properly. Use golang.org/x/text/cases instead.

```go

package main

import (
	"bytes"
	"fmt"
)

func main() {
	fmt.Printf("%s", bytes.Title([]byte("her royal highness")))
}

```

```go
Output:
Her Royal Highness

```

 Share Format Run

```go
func ToLower(s []byte) []byte
```

ToLower returns a copy of the byte slice s with all Unicode letters mapped to their lower case.

```go

package main

import (
	"bytes"
	"fmt"
)

func main() {
	fmt.Printf("%s", bytes.ToLower([]byte("Gopher")))
}

```

```go
Output:
gopher

```

 Share Format Run

```go
func ToLowerSpecial(c unicode.SpecialCase, s []byte) []byte
```

ToLowerSpecial treats s as UTF-8-encoded bytes and returns a copy with all the Unicode letters mapped to their lower case, giving priority to the special casing rules.

```go

package main

import (
	"bytes"
	"fmt"
	"unicode"
)

func main() {
	str := []byte("AHOJ VÝVOJÁRİ GOLANG")
	totitle := bytes.ToLowerSpecial(unicode.AzeriCase, str)
	fmt.Println("Original : " + string(str))
	fmt.Println("ToLower : " + string(totitle))
}

```

```go
Output:
Original : AHOJ VÝVOJÁRİ GOLANG
ToLower : ahoj vývojári golang

```

 Share Format Run

```go
func ToTitle(s []byte) []byte
```

ToTitle treats s as UTF-8-encoded bytes and returns a copy with all the Unicode letters mapped to their title case.

```go

package main

import (
	"bytes"
	"fmt"
)

func main() {
	fmt.Printf("%s\n", bytes.ToTitle([]byte("loud noises")))
	fmt.Printf("%s\n", bytes.ToTitle([]byte("брат")))
}

```

```go
Output:
LOUD NOISES
БРАТ

```

 Share Format Run

```go
func ToTitleSpecial(c unicode.SpecialCase, s []byte) []byte
```

ToTitleSpecial treats s as UTF-8-encoded bytes and returns a copy with all the Unicode letters mapped to their title case, giving priority to the special casing rules.

```go

package main

import (
	"bytes"
	"fmt"
	"unicode"
)

func main() {
	str := []byte("ahoj vývojári golang")
	totitle := bytes.ToTitleSpecial(unicode.AzeriCase, str)
	fmt.Println("Original : " + string(str))
	fmt.Println("ToTitle : " + string(totitle))
}

```

```go
Output:
Original : ahoj vývojári golang
ToTitle : AHOJ VÝVOJÁRİ GOLANG

```

 Share Format Run

```go
func ToUpper(s []byte) []byte
```

ToUpper returns a copy of the byte slice s with all Unicode letters mapped to their upper case.

```go

package main

import (
	"bytes"
	"fmt"
)

func main() {
	fmt.Printf("%s", bytes.ToUpper([]byte("Gopher")))
}

```

```go
Output:
GOPHER

```

 Share Format Run

```go
func ToUpperSpecial(c unicode.SpecialCase, s []byte) []byte
```

ToUpperSpecial treats s as UTF-8-encoded bytes and returns a copy with all the Unicode letters mapped to their upper case, giving priority to the special casing rules.

```go

package main

import (
	"bytes"
	"fmt"
	"unicode"
)

func main() {
	str := []byte("ahoj vývojári golang")
	totitle := bytes.ToUpperSpecial(unicode.AzeriCase, str)
	fmt.Println("Original : " + string(str))
	fmt.Println("ToUpper : " + string(totitle))
}

```

```go
Output:
Original : ahoj vývojári golang
ToUpper : AHOJ VÝVOJÁRİ GOLANG

```

 Share Format Run

```go
func ToValidUTF8(s, replacement []byte) []byte
```

ToValidUTF8 treats s as UTF-8-encoded bytes and returns a copy with each run of bytes representing invalid UTF-8 replaced with the bytes in replacement, which may be empty.

```go

package main

import (
	"bytes"
	"fmt"
)

func main() {
	fmt.Printf("%s\n", bytes.ToValidUTF8([]byte("abc"), []byte("\uFFFD")))
	fmt.Printf("%s\n", bytes.ToValidUTF8([]byte("a\xffb\xC0\xAFc\xff"), []byte("")))
	fmt.Printf("%s\n", bytes.ToValidUTF8([]byte("\xed\xa0\x80"), []byte("abc")))
}

```

```go
Output:
abc
abc
abc

```

 Share Format Run

```go
func Trim(s []byte, cutset string) []byte
```

Trim returns a subslice of s by slicing off all leading and trailing UTF-8-encoded code points contained in cutset.

```go

package main

import (
	"bytes"
	"fmt"
)

func main() {
	fmt.Printf("[%q]", bytes.Trim([]byte(" !!! Achtung! Achtung! !!! "), "! "))
}

```

```go
Output:
["Achtung! Achtung"]

```

 Share Format Run

```go
func TrimFunc(s []byte, f func(r rune) bool) []byte
```

TrimFunc returns a subslice of s by slicing off all leading and trailing UTF-8-encoded code points c that satisfy f(c).

```go

package main

import (
	"bytes"
	"fmt"
	"unicode"
)

func main() {
	fmt.Println(string(bytes.TrimFunc([]byte("go-gopher!"), unicode.IsLetter)))
	fmt.Println(string(bytes.TrimFunc([]byte("\"go-gopher!\""), unicode.IsLetter)))
	fmt.Println(string(bytes.TrimFunc([]byte("go-gopher!"), unicode.IsPunct)))
	fmt.Println(string(bytes.TrimFunc([]byte("1234go-gopher!567"), unicode.IsNumber)))
}

```

```go
Output:
-gopher!
"go-gopher!"
go-gopher
go-gopher!

```

 Share Format Run

```go
func TrimLeft(s []byte, cutset string) []byte
```

TrimLeft returns a subslice of s by slicing off all leading UTF-8-encoded code points contained in cutset.

```go

package main

import (
	"bytes"
	"fmt"
)

func main() {
	fmt.Print(string(bytes.TrimLeft([]byte("453gopher8257"), "0123456789")))
}

```

```go
Output:
gopher8257

```

 Share Format Run

```go
func TrimLeftFunc(s []byte, f func(r rune) bool) []byte
```

TrimLeftFunc treats s as UTF-8-encoded bytes and returns a subslice of s by slicing off all leading UTF-8-encoded code points c that satisfy f(c).

```go

package main

import (
	"bytes"
	"fmt"
	"unicode"
)

func main() {
	fmt.Println(string(bytes.TrimLeftFunc([]byte("go-gopher"), unicode.IsLetter)))
	fmt.Println(string(bytes.TrimLeftFunc([]byte("go-gopher!"), unicode.IsPunct)))
	fmt.Println(string(bytes.TrimLeftFunc([]byte("1234go-gopher!567"), unicode.IsNumber)))
}

```

```go
Output:
-gopher
go-gopher!
go-gopher!567

```

 Share Format Run

```go
func TrimPrefix(s, prefix []byte) []byte
```

TrimPrefix returns s without the provided leading prefix string. If s doesn't start with prefix, s is returned unchanged.

```go

package main

import (
	"bytes"
	"fmt"
)

func main() {
	var b = []byte("Goodbye,, world!")
	b = bytes.TrimPrefix(b, []byte("Goodbye,"))
	b = bytes.TrimPrefix(b, []byte("See ya,"))
	fmt.Printf("Hello%s", b)
}

```

```go
Output:
Hello, world!

```

 Share Format Run

```go
func TrimRight(s []byte, cutset string) []byte
```

TrimRight returns a subslice of s by slicing off all trailing UTF-8-encoded code points that are contained in cutset.

```go

package main

import (
	"bytes"
	"fmt"
)

func main() {
	fmt.Print(string(bytes.TrimRight([]byte("453gopher8257"), "0123456789")))
}

```

```go
Output:
453gopher

```

 Share Format Run

```go
func TrimRightFunc(s []byte, f func(r rune) bool) []byte
```

TrimRightFunc returns a subslice of s by slicing off all trailing UTF-8-encoded code points c that satisfy f(c).

```go

package main

import (
	"bytes"
	"fmt"
	"unicode"
)

func main() {
	fmt.Println(string(bytes.TrimRightFunc([]byte("go-gopher"), unicode.IsLetter)))
	fmt.Println(string(bytes.TrimRightFunc([]byte("go-gopher!"), unicode.IsPunct)))
	fmt.Println(string(bytes.TrimRightFunc([]byte("1234go-gopher!567"), unicode.IsNumber)))
}

```

```go
Output:
go-
go-gopher
1234go-gopher!

```

 Share Format Run

```go
func TrimSpace(s []byte) []byte
```

TrimSpace returns a subslice of s by slicing off all leading and trailing white space, as defined by Unicode.

```go

package main

import (
	"bytes"
	"fmt"
)

func main() {
	fmt.Printf("%s", bytes.TrimSpace([]byte(" \t\n a lone gopher \n\t\r\n")))
}

```

```go
Output:
a lone gopher

```

 Share Format Run

```go
func TrimSuffix(s, suffix []byte) []byte
```

TrimSuffix returns s without the provided trailing suffix string. If s doesn't end with suffix, s is returned unchanged.

```go

package main

import (
	"bytes"
	"os"
)

func main() {
	var b = []byte("Hello, goodbye, etc!")
	b = bytes.TrimSuffix(b, []byte("goodbye, etc!"))
	b = bytes.TrimSuffix(b, []byte("gopher"))
	b = append(b, bytes.TrimSuffix([]byte("world!"), []byte("x!"))...)
	os.Stdout.Write(b)
}

```

```go
Output:
Hello, world!

```

 Share Format Run

```go
type Buffer struct {
	// contains filtered or unexported fields
}
```

A Buffer is a variable-sized buffer of bytes with Buffer.Read and Buffer.Write methods. The zero value for Buffer is an empty buffer ready to use.

```go

package main

import (
	"bytes"
	"fmt"
	"os"
)

func main() {
	var b bytes.Buffer // A Buffer needs no initialization.
	b.Write([]byte("Hello "))
	fmt.Fprintf(&b, "world!")
	b.WriteTo(os.Stdout)
}

```

```go
Output:
Hello world!

```

 Share Format Run

```go

package main

import (
	"bytes"
	"encoding/base64"
	"io"
	"os"
)

func main() {
	// A Buffer can turn a string or a []byte into an io.Reader.
	buf := bytes.NewBufferString("R29waGVycyBydWxlIQ==")
	dec := base64.NewDecoder(base64.StdEncoding, buf)
	io.Copy(os.Stdout, dec)
}

```

```go
Output:
Gophers rule!

```

 Share Format Run

```go
func NewBuffer(buf []byte) *Buffer
```

NewBuffer creates and initializes a new Buffer using buf as its initial contents. The new Buffer takes ownership of buf, and the caller should not use buf after this call. NewBuffer is intended to prepare a Buffer to read existing data. It can also be used to set the initial size of the internal buffer for writing. To do that, buf should have the desired capacity but a length of zero.

In most cases, new(Buffer) (or just declaring a Buffer variable) is sufficient to initialize a Buffer.

```go
func NewBufferString(s string) *Buffer
```

NewBufferString creates and initializes a new Buffer using string s as its initial contents. It is intended to prepare a buffer to read an existing string.

In most cases, new(Buffer) (or just declaring a Buffer variable) is sufficient to initialize a Buffer.

```go
func (b *Buffer) Available() int
```

Available returns how many bytes are unused in the buffer.

```go
func (b *Buffer) AvailableBuffer() []byte
```

AvailableBuffer returns an empty buffer with b.Available() capacity. This buffer is intended to be appended to and passed to an immediately succeeding Buffer.Write call. The buffer is only valid until the next write operation on b.

```go

package main

import (
	"bytes"
	"os"
	"strconv"
)

func main() {
	var buf bytes.Buffer
	for i := 0; i < 4; i++ {
		b := buf.AvailableBuffer()
		b = strconv.AppendInt(b, int64(i), 10)
		b = append(b, ' ')
		buf.Write(b)
	}
	os.Stdout.Write(buf.Bytes())
}

```

```go
Output:
0 1 2 3

```

 Share Format Run

```go
func (b *Buffer) Bytes() []byte
```

Bytes returns a slice of length b.Len() holding the unread portion of the buffer. The slice is valid for use only until the next buffer modification (that is, only until the next call to a method like Buffer.Read, Buffer.Write, Buffer.Reset, or Buffer.Truncate). The slice aliases the buffer content at least until the next buffer modification, so immediate changes to the slice will affect the result of future reads.

```go

package main

import (
	"bytes"
	"os"
)

func main() {
	buf := bytes.Buffer{}
	buf.Write([]byte{'h', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd'})
	os.Stdout.Write(buf.Bytes())
}

```

```go
Output:
hello world

```

 Share Format Run

```go
func (b *Buffer) Cap() int
```

Cap returns the capacity of the buffer's underlying byte slice, that is, the total space allocated for the buffer's data.

```go

package main

import (
	"bytes"
	"fmt"
)

func main() {
	buf1 := bytes.NewBuffer(make([]byte, 10))
	buf2 := bytes.NewBuffer(make([]byte, 0, 10))
	fmt.Println(buf1.Cap())
	fmt.Println(buf2.Cap())
}

```

```go
Output:
10
10

```

 Share Format Run

```go
func (b *Buffer) Grow(n int)
```

Grow grows the buffer's capacity, if necessary, to guarantee space for another n bytes. After Grow(n), at least n bytes can be written to the buffer without another allocation. If n is negative, Grow will panic. If the buffer can't grow it will panic with ErrTooLarge.

```go

package main

import (
	"bytes"
	"fmt"
)

func main() {
	var b bytes.Buffer
	b.Grow(64)
	bb := b.Bytes()
	b.Write([]byte("64 bytes or fewer"))
	fmt.Printf("%q", bb[:b.Len()])
}

```

```go
Output:
"64 bytes or fewer"

```

 Share Format Run

```go
func (b *Buffer) Len() int
```

Len returns the number of bytes of the unread portion of the buffer; b.Len() == len(b.Bytes()).

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
	fmt.Printf("%d", b.Len())
}

```

```go
Output:
5

```

 Share Format Run

```go
func (b *Buffer) Next(n int) []byte
```

Next returns a slice containing the next n bytes from the buffer, advancing the buffer as if the bytes had been returned by Buffer.Read. If there are fewer than n bytes in the buffer, Next returns the entire buffer. The slice is only valid until the next call to a read or write method.

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
	fmt.Printf("%s\n", b.Next(2))
	fmt.Printf("%s\n", b.Next(2))
	fmt.Printf("%s", b.Next(2))
}

```

```go
Output:
ab
cd
e

```

 Share Format Run

```go
func (b *Buffer) Peek(n int) ([]byte, error)
```

Peek returns the next n bytes without advancing the buffer. If Peek returns fewer than n bytes, it also returns io.EOF. The slice is only valid until the next call to a read or write method. The slice aliases the buffer content at least until the next buffer modification, so immediate changes to the slice will affect the result of future reads.

```go
func (b *Buffer) Read(p []byte) (n int, err error)
```

Read reads the next len(p) bytes from the buffer or until the buffer is drained. The return value n is the number of bytes read. If the buffer has no data to return, err is io.EOF (unless len(p) is zero); otherwise it is nil.

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
