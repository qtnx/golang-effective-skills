---
source_name: "External Linked Documentation"
source_url: "https://pkg.go.dev/strings"
source_path: "sources/raw/external/pkg-go-dev-strings-2a66c125d7.html"
license_ref: ""
---

strings package - strings - Go Packages
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

Package strings implements simple functions to manipulate UTF-8 encoded strings.

For information about UTF-8 strings in Go, see https://blog.golang.org/strings <https://blog.golang.org/strings>.

-  func Clone(s string) string
-  func Compare(a, b string) int
-  func Contains(s, substr string) bool
-  func ContainsAny(s, chars string) bool
-  func ContainsFunc(s string, f func(rune) bool) bool
-  func ContainsRune(s string, r rune) bool
-  func Count(s, substr string) int
-  func Cut(s, sep string) (before, after string, found bool)
-  func CutPrefix(s, prefix string) (after string, found bool)
-  func CutSuffix(s, suffix string) (before string, found bool)
-  func EqualFold(s, t string) bool
-  func Fields(s string) []string
-  func FieldsFunc(s string, f func(rune) bool) []string
-  func FieldsFuncSeq(s string, f func(rune) bool) iter.Seq[string]
-  func FieldsSeq(s string) iter.Seq[string]
-  func HasPrefix(s, prefix string) bool
-  func HasSuffix(s, suffix string) bool
-  func Index(s, substr string) int
-  func IndexAny(s, chars string) int
-  func IndexByte(s string, c byte) int
-  func IndexFunc(s string, f func(rune) bool) int
-  func IndexRune(s string, r rune) int
-  func Join(elems []string, sep string) string
-  func LastIndex(s, substr string) int
-  func LastIndexAny(s, chars string) int
-  func LastIndexByte(s string, c byte) int
-  func LastIndexFunc(s string, f func(rune) bool) int
-  func Lines(s string) iter.Seq[string]
-  func Map(mapping func(rune) rune, s string) string
-  func Repeat(s string, count int) string
-  func Replace(s, old, new string, n int) string
-  func ReplaceAll(s, old, new string) string
-  func Split(s, sep string) []string
-  func SplitAfter(s, sep string) []string
-  func SplitAfterN(s, sep string, n int) []string
-  func SplitAfterSeq(s, sep string) iter.Seq[string]
-  func SplitN(s, sep string, n int) []string
-  func SplitSeq(s, sep string) iter.Seq[string]
-  func Title(s string) stringdeprecated
-  func ToLower(s string) string
-  func ToLowerSpecial(c unicode.SpecialCase, s string) string
-  func ToTitle(s string) string
-  func ToTitleSpecial(c unicode.SpecialCase, s string) string
-  func ToUpper(s string) string
-  func ToUpperSpecial(c unicode.SpecialCase, s string) string
-  func ToValidUTF8(s, replacement string) string
-  func Trim(s, cutset string) string
-  func TrimFunc(s string, f func(rune) bool) string
-  func TrimLeft(s, cutset string) string
-  func TrimLeftFunc(s string, f func(rune) bool) string
-  func TrimPrefix(s, prefix string) string
-  func TrimRight(s, cutset string) string
-  func TrimRightFunc(s string, f func(rune) bool) string
-  func TrimSpace(s string) string
-  func TrimSuffix(s, suffix string) string
-  type Builder
-
-  func (b *Builder) Cap() int
-  func (b *Builder) Grow(n int)
-  func (b *Builder) Len() int
-  func (b *Builder) Reset()
-  func (b *Builder) String() string
-  func (b *Builder) Write(p []byte) (int, error)
-  func (b *Builder) WriteByte(c byte) error
-  func (b *Builder) WriteRune(r rune) (int, error)
-  func (b *Builder) WriteString(s string) (int, error)

-  type Reader
-
-  func NewReader(s string) *Reader

-
-  func (r *Reader) Len() int
-  func (r *Reader) Read(b []byte) (n int, err error)
-  func (r *Reader) ReadAt(b []byte, off int64) (n int, err error)
-  func (r *Reader) ReadByte() (byte, error)
-  func (r *Reader) ReadRune() (ch rune, size int, err error)
-  func (r *Reader) Reset(s string)
-  func (r *Reader) Seek(offset int64, whence int) (int64, error)
-  func (r *Reader) Size() int64
-  func (r *Reader) UnreadByte() error
-  func (r *Reader) UnreadRune() error
-  func (r *Reader) WriteTo(w io.Writer) (n int64, err error)

-  type Replacer
-
-  func NewReplacer(oldnew ...string) *Replacer

-
-  func (r *Replacer) Replace(s string) string
-  func (r *Replacer) WriteString(w io.Writer, s string) (n int, err error)

- Builder
- Clone
- Compare
- Contains
- ContainsAny
- ContainsFunc
- ContainsRune
- Count
- Cut
- CutPrefix
- CutSuffix
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
- NewReplacer
- Repeat
- Replace
- ReplaceAll
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

This section is empty.

This section is empty.

```go
func Clone(s string) string
```

Clone returns a fresh copy of s. It guarantees to make a copy of s into a new allocation, which can be important when retaining only a small substring of a much larger string. Using Clone can help such programs use less memory. Of course, since using Clone makes a copy, overuse of Clone can make programs use more memory. Clone should typically be used only rarely, and only when profiling indicates that it is needed. For strings of length zero the string "" will be returned and no allocation is made.

```go

package main

import (
	"fmt"
	"strings"
	"unsafe"
)

func main() {
	s := "abc"
	clone := strings.Clone(s)
	fmt.Println(s == clone)
	fmt.Println(unsafe.StringData(s) == unsafe.StringData(clone))
}

```

```go
Output:
true
false

```

Share Format Run

```go
func Compare(a, b string) int
```

Compare returns an integer comparing two strings lexicographically. The result will be 0 if a == b, -1 if a < b, and +1 if a > b.

Use Compare when you need to perform a three-way comparison (with slices.SortFunc, for example). It is usually clearer and always faster to use the built-in string comparison operators ==, <, >, and so on.

```go

package main

import (
	"fmt"
	"strings"
)

func main() {
	fmt.Println(strings.Compare("a", "b"))
	fmt.Println(strings.Compare("a", "a"))
	fmt.Println(strings.Compare("b", "a"))
}

```

```go
Output:
-1
0
1

```

Share Format Run

```go
func Contains(s, substr string) bool
```

Contains reports whether substr is within s.

```go

package main

import (
	"fmt"
	"strings"
)

func main() {
	fmt.Println(strings.Contains("seafood", "foo"))
	fmt.Println(strings.Contains("seafood", "bar"))
	fmt.Println(strings.Contains("seafood", ""))
	fmt.Println(strings.Contains("", ""))
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
func ContainsAny(s, chars string) bool
```

ContainsAny reports whether any Unicode code points in chars are within s.

```go

package main

import (
	"fmt"
	"strings"
)

func main() {
	fmt.Println(strings.ContainsAny("team", "i"))
	fmt.Println(strings.ContainsAny("fail", "ui"))
	fmt.Println(strings.ContainsAny("ure", "ui"))
	fmt.Println(strings.ContainsAny("failure", "ui"))
	fmt.Println(strings.ContainsAny("foo", ""))
	fmt.Println(strings.ContainsAny("", ""))
}

```

```go
Output:
false
true
true
true
false
false

```

Share Format Run

```go
func ContainsFunc(s string, f func(rune) bool) bool
```

ContainsFunc reports whether any Unicode code points r within s satisfy f(r).

```go

package main

import (
	"fmt"
	"strings"
)

func main() {
	f := func(r rune) bool {
		return r == 'a' || r == 'e' || r == 'i' || r == 'o' || r == 'u'
	}
	fmt.Println(strings.ContainsFunc("hello", f))
	fmt.Println(strings.ContainsFunc("rhythms", f))
}

```

```go
Output:
true
false

```

Share Format Run

```go
func ContainsRune(s string, r rune) bool
```

ContainsRune reports whether the Unicode code point r is within s.

```go

package main

import (
	"fmt"
	"strings"
)

func main() {
	// Finds whether a string contains a particular Unicode code point.
	// The code point for the lowercase letter "a", for example, is 97.
	fmt.Println(strings.ContainsRune("aardvark", 97))
	fmt.Println(strings.ContainsRune("timeout", 97))
}

```

```go
Output:
true
false

```

Share Format Run

```go
func Count(s, substr string) int
```

Count counts the number of non-overlapping instances of substr in s. If substr is an empty string, Count returns 1 + the number of Unicode code points in s.

```go

package main

import (
	"fmt"
	"strings"
)

func main() {
	fmt.Println(strings.Count("cheese", "e"))
	fmt.Println(strings.Count("five", "")) // before & after each rune
}

```

```go
Output:
3
5

```

Share Format Run

```go
func Cut(s, sep string) (before, after string, found bool)
```

Cut slices s around the first instance of sep, returning the text before and after sep. The found result reports whether sep appears in s. If sep does not appear in s, cut returns s, "", false.

```go

package main

import (
	"fmt"
	"strings"
)

func main() {
	show := func(s, sep string) {
		before, after, found := strings.Cut(s, sep)
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
func CutPrefix(s, prefix string) (after string, found bool)
```

CutPrefix returns s without the provided leading prefix string and reports whether it found the prefix. If s doesn't start with prefix, CutPrefix returns s, false. If prefix is the empty string, CutPrefix returns s, true.

```go

package main

import (
	"fmt"
	"strings"
)

func main() {
	show := func(s, prefix string) {
		after, found := strings.CutPrefix(s, prefix)
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
func CutSuffix(s, suffix string) (before string, found bool)
```

CutSuffix returns s without the provided ending suffix string and reports whether it found the suffix. If s doesn't end with suffix, CutSuffix returns s, false. If suffix is the empty string, CutSuffix returns s, true.

```go

package main
