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

## Links

-    Report a Vulnerability  <https://go.dev/security/policy>

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

import (
	"fmt"
	"strings"
)

func main() {
	show := func(s, suffix string) {
		before, found := strings.CutSuffix(s, suffix)
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
func EqualFold(s, t string) bool
```

EqualFold reports whether s and t, interpreted as UTF-8 strings, are equal under simple Unicode case-folding, which is a more general form of case-insensitivity.

```go

package main

import (
	"fmt"
	"strings"
)

func main() {
	fmt.Println(strings.EqualFold("Go", "go"))
	fmt.Println(strings.EqualFold("AB", "ab")) // true because comparison uses simple case-folding
	fmt.Println(strings.EqualFold("ß", "ss"))  // false because comparison does not use full case-folding
}

```

```go
Output:
true
true
false

```

 Share Format Run

```go
func Fields(s string) []string
```

Fields splits the string s around each instance of one or more consecutive white space characters, as defined by unicode.IsSpace, returning a slice of substrings of s or an empty slice if s contains only white space. Every element of the returned slice is non-empty. Unlike Split, leading and trailing runs of white space characters are discarded.

```go

package main

import (
	"fmt"
	"strings"
)

func main() {
	fmt.Printf("Fields are: %q", strings.Fields("  foo bar  baz   "))
}

```

```go
Output:
Fields are: ["foo" "bar" "baz"]

```

 Share Format Run

```go
func FieldsFunc(s string, f func(rune) bool) []string
```

FieldsFunc splits the string s at each run of Unicode code points c satisfying f(c) and returns an array of slices of s. If all code points in s satisfy f(c) or the string is empty, an empty slice is returned. Every element of the returned slice is non-empty. Unlike Split, leading and trailing runs of code points satisfying f(c) are discarded.

FieldsFunc makes no guarantees about the order in which it calls f(c) and assumes that f always returns the same value for a given c.

```go

package main

import (
	"fmt"
	"strings"
	"unicode"
)

func main() {
	f := func(c rune) bool {
		return !unicode.IsLetter(c) && !unicode.IsNumber(c)
	}
	fmt.Printf("Fields are: %q", strings.FieldsFunc("  foo1;bar2,baz3...", f))
}

```

```go
Output:
Fields are: ["foo1" "bar2" "baz3"]

```

 Share Format Run

```go
func FieldsFuncSeq(s string, f func(rune) bool) iter.Seq[string]
```

FieldsFuncSeq returns an iterator over substrings of s split around runs of Unicode code points satisfying f(c). The iterator yields the same strings that would be returned by FieldsFunc(s), but without constructing the slice.

```go

package main

import (
	"fmt"
	"strings"
	"unicode"
)

func main() {
	text := "The quick brown fox"
	fmt.Println("Split on whitespace(similar to FieldsSeq):")
	for word := range strings.FieldsFuncSeq(text, unicode.IsSpace) {
		fmt.Printf("%q\n", word)
	}

	mixedText := "abc123def456ghi"
	fmt.Println("\nSplit on digits:")
	for word := range strings.FieldsFuncSeq(mixedText, unicode.IsDigit) {
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
func FieldsSeq(s string) iter.Seq[string]
```

FieldsSeq returns an iterator over substrings of s split around runs of whitespace characters, as defined by unicode.IsSpace. The iterator yields the same strings that would be returned by Fields(s), but without constructing the slice.

```go

package main

import (
	"fmt"
	"strings"
)

func main() {
	text := "The quick brown fox"
	fmt.Println("Split string into fields:")
	for word := range strings.FieldsSeq(text) {
		fmt.Printf("%q\n", word)
	}

	textWithSpaces := "  lots   of   spaces  "
	fmt.Println("\nSplit string with multiple spaces:")
	for word := range strings.FieldsSeq(textWithSpaces) {
		fmt.Printf("%q\n", word)
	}

}

```

```go
Output:
Split string into fields:
"The"
"quick"
"brown"
"fox"

Split string with multiple spaces:
"lots"
"of"
"spaces"

```

 Share Format Run

```go
func HasPrefix(s, prefix string) bool
```

HasPrefix reports whether the string s begins with prefix.

```go

package main

import (
	"fmt"
	"strings"
)

func main() {
	fmt.Println(strings.HasPrefix("Gopher", "Go"))
	fmt.Println(strings.HasPrefix("Gopher", "C"))
	fmt.Println(strings.HasPrefix("Gopher", ""))
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
func HasSuffix(s, suffix string) bool
```

HasSuffix reports whether the string s ends with suffix.

```go

package main

import (
	"fmt"
	"strings"
)

func main() {
	fmt.Println(strings.HasSuffix("Amigo", "go"))
	fmt.Println(strings.HasSuffix("Amigo", "O"))
	fmt.Println(strings.HasSuffix("Amigo", "Ami"))
	fmt.Println(strings.HasSuffix("Amigo", ""))
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
func Index(s, substr string) int
```

Index returns the index of the first instance of substr in s, or -1 if substr is not present in s.

```go

package main

import (
	"fmt"
	"strings"
)

func main() {
	fmt.Println(strings.Index("chicken", "ken"))
	fmt.Println(strings.Index("chicken", "dmr"))
}

```

```go
Output:
4
-1

```

 Share Format Run

```go
func IndexAny(s, chars string) int
```

IndexAny returns the index of the first instance of any Unicode code point from chars in s, or -1 if no Unicode code point from chars is present in s.

```go

package main

import (
	"fmt"
	"strings"
)

func main() {
	fmt.Println(strings.IndexAny("chicken", "aeiouy"))
	fmt.Println(strings.IndexAny("crwth", "aeiouy"))
}

```

```go
Output:
2
-1

```

 Share Format Run

```go
func IndexByte(s string, c byte) int
```

IndexByte returns the index of the first instance of c in s, or -1 if c is not present in s.

```go

package main

import (
	"fmt"
	"strings"
)

func main() {
	fmt.Println(strings.IndexByte("golang", 'g'))
	fmt.Println(strings.IndexByte("gophers", 'h'))
	fmt.Println(strings.IndexByte("golang", 'x'))
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
func IndexFunc(s string, f func(rune) bool) int
```

IndexFunc returns the index into s of the first Unicode code point satisfying f(c), or -1 if none do.

```go

package main

import (
	"fmt"
	"strings"
	"unicode"
)

func main() {
	f := func(c rune) bool {
		return unicode.Is(unicode.Han, c)
	}
	fmt.Println(strings.IndexFunc("Hello, 世界", f))
	fmt.Println(strings.IndexFunc("Hello, world", f))
}

```

```go
Output:
7
-1

```

 Share Format Run

```go
func IndexRune(s string, r rune) int
```

IndexRune returns the index of the first instance of the Unicode code point r, or -1 if rune is not present in s. If r is utf8.RuneError, it returns the first instance of any invalid UTF-8 byte sequence.

```go

package main

import (
	"fmt"
	"strings"
)

func main() {
	fmt.Println(strings.IndexRune("chicken", 'k'))
	fmt.Println(strings.IndexRune("chicken", 'd'))
}

```

```go
Output:
4
-1

```

 Share Format Run

```go
func Join(elems []string, sep string) string
```

Join concatenates the elements of its first argument to create a single string. The separator string sep is placed between elements in the resulting string.

```go

package main

import (
	"fmt"
	"strings"
)

func main() {
	s := []string{"foo", "bar", "baz"}
	fmt.Println(strings.Join(s, ", "))
}

```

```go
Output:
foo, bar, baz

```

 Share Format Run

```go
func LastIndex(s, substr string) int
```

LastIndex returns the index of the last instance of substr in s, or -1 if substr is not present in s.

```go

package main

import (
	"fmt"
	"strings"
)

func main() {
	fmt.Println(strings.Index("go gopher", "go"))
	fmt.Println(strings.LastIndex("go gopher", "go"))
	fmt.Println(strings.LastIndex("go gopher", "rodent"))
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
func LastIndexAny(s, chars string) int
```

LastIndexAny returns the index of the last instance of any Unicode code point from chars in s, or -1 if no Unicode code point from chars is present in s.

```go

package main

import (
	"fmt"
	"strings"
)

func main() {
	fmt.Println(strings.LastIndexAny("go gopher", "go"))
	fmt.Println(strings.LastIndexAny("go gopher", "rodent"))
	fmt.Println(strings.LastIndexAny("go gopher", "fail"))
}

```

```go
Output:
4
8
-1

```

 Share Format Run

```go
func LastIndexByte(s string, c byte) int
```

LastIndexByte returns the index of the last instance of c in s, or -1 if c is not present in s.

```go

package main

import (
	"fmt"
	"strings"
)

func main() {
	fmt.Println(strings.LastIndexByte("Hello, world", 'l'))
	fmt.Println(strings.LastIndexByte("Hello, world", 'o'))
	fmt.Println(strings.LastIndexByte("Hello, world", 'x'))
}

```

```go
Output:
10
8
-1

```

 Share Format Run

```go
func LastIndexFunc(s string, f func(rune) bool) int
```

LastIndexFunc returns the index into s of the last Unicode code point satisfying f(c), or -1 if none do.

```go

package main

import (
	"fmt"
	"strings"
	"unicode"
)

func main() {
	fmt.Println(strings.LastIndexFunc("go 123", unicode.IsNumber))
	fmt.Println(strings.LastIndexFunc("123 go", unicode.IsNumber))
	fmt.Println(strings.LastIndexFunc("go", unicode.IsNumber))
}

```

```go
Output:
5
2
-1

```

 Share Format Run

```go
func Lines(s string) iter.Seq[string]
```

Lines returns an iterator over the newline-terminated lines in the string s. The lines yielded by the iterator include their terminating newlines. If s is empty, the iterator yields no lines at all. If s does not end in a newline, the final yielded line will not end in a newline. It returns a single-use iterator.

```go

package main

import (
	"fmt"
	"strings"
)

func main() {
	text := "Hello\nWorld\nGo Programming\n"
	for line := range strings.Lines(text) {
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
func Map(mapping func(rune) rune, s string) string
```

Map returns a copy of the string s with all its characters modified according to the mapping function. If mapping returns a negative value, the character is dropped from the string with no replacement.

```go

package main

import (
	"fmt"
	"strings"
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
	fmt.Println(strings.Map(rot13, "'Twas brillig and the slithy gopher..."))
}

```

```go
Output:
'Gjnf oevyyvt naq gur fyvgul tbcure...

```

 Share Format Run

```go
func Repeat(s string, count int) string
```

Repeat returns a new string consisting of count copies of the string s.

It panics if count is negative or if the result of (len(s) * count) overflows.

```go

package main

import (
	"fmt"
	"strings"
)

func main() {
	fmt.Println("ba" + strings.Repeat("na", 2))
}

```

```go
Output:
banana

```

 Share Format Run

```go
func Replace(s, old, new string, n int) string
```

Replace returns a copy of the string s with the first n non-overlapping instances of old replaced by new. If old is empty, it matches at the beginning of the string and after each UTF-8 sequence, yielding up to k+1 replacements for a k-rune string. If n < 0, there is no limit on the number of replacements.

```go

package main

import (
	"fmt"
	"strings"
)

func main() {
	fmt.Println(strings.Replace("oink oink oink", "k", "ky", 2))
	fmt.Println(strings.Replace("oink oink oink", "oink", "moo", -1))
}

```

```go
Output:
oinky oinky oink
moo moo moo

```

 Share Format Run

```go
func ReplaceAll(s, old, new string) string
```

ReplaceAll returns a copy of the string s with all non-overlapping instances of old replaced by new. If old is empty, it matches at the beginning of the string and after each UTF-8 sequence, yielding up to k+1 replacements for a k-rune string.

```go

package main

import (
	"fmt"
	"strings"
)

func main() {
	fmt.Println(strings.ReplaceAll("oink oink oink", "oink", "moo"))
}

```

```go
Output:
moo moo moo

```

 Share Format Run

```go
func Split(s, sep string) []string
```

Split slices s into all substrings separated by sep and returns a slice of the substrings between those separators.

If s does not contain sep and sep is not empty, Split returns a slice of length 1 whose only element is s.

If sep is empty, Split splits after each UTF-8 sequence. If both s and sep are empty, Split returns an empty slice.

It is equivalent to SplitN with a count of -1.

To split around the first instance of a separator, see Cut.

```go

package main

import (
	"fmt"
	"strings"
)

func main() {
	fmt.Printf("%q\n", strings.Split("a,b,c", ","))
	fmt.Printf("%q\n", strings.Split("a man a plan a canal panama", "a "))
	fmt.Printf("%q\n", strings.Split(" xyz ", ""))
	fmt.Printf("%q\n", strings.Split("", "Bernardo O'Higgins"))
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
func SplitAfter(s, sep string) []string
```

SplitAfter slices s into all substrings after each instance of sep and returns a slice of those substrings.

If s does not contain sep and sep is not empty, SplitAfter returns a slice of length 1 whose only element is s.

If sep is empty, SplitAfter splits after each UTF-8 sequence. If both s and sep are empty, SplitAfter returns an empty slice.

It is equivalent to SplitAfterN with a count of -1.

```go

package main

import (
	"fmt"
	"strings"
)

func main() {
	fmt.Printf("%q\n", strings.SplitAfter("a,b,c", ","))
}

```

```go
Output:
["a," "b," "c"]

```

 Share Format Run

```go
func SplitAfterN(s, sep string, n int) []string
```

SplitAfterN slices s into substrings after each instance of sep and returns a slice of those substrings.

The count determines the number of substrings to return:

- n > 0: at most n substrings; the last substring will be the unsplit remainder;
- n == 0: the result is nil (zero substrings);
- n < 0: all substrings.

Edge cases for s and sep (for example, empty strings) are handled as described in the documentation for SplitAfter.

```go

package main

import (
	"fmt"
	"strings"
)

func main() {
	fmt.Printf("%q\n", strings.SplitAfterN("a,b,c", ",", 2))
}

```

```go
Output:
["a," "b,c"]

```

 Share Format Run

```go
func SplitAfterSeq(s, sep string) iter.Seq[string]
```

SplitAfterSeq returns an iterator over substrings of s split after each instance of sep. The iterator yields the same strings that would be returned by SplitAfter(s, sep), but without constructing the slice. It returns a single-use iterator.

```go

package main

import (
	"fmt"
	"strings"
)

func main() {
	s := "a,b,c,d"
	for part := range strings.SplitAfterSeq(s, ",") {
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
func SplitN(s, sep string, n int) []string
```

SplitN slices s into substrings separated by sep and returns a slice of the substrings between those separators.

The count determines the number of substrings to return:

- n > 0: at most n substrings; the last substring will be the unsplit remainder;
- n == 0: the result is nil (zero substrings);
- n < 0: all substrings.

Edge cases for s and sep (for example, empty strings) are handled as described in the documentation for Split.

To split around the first instance of a separator, see Cut.

```go

package main

import (
	"fmt"
	"strings"
)

func main() {
	fmt.Printf("%q\n", strings.SplitN("a,b,c", ",", 2))
	z := strings.SplitN("a,b,c", ",", 0)
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
func SplitSeq(s, sep string) iter.Seq[string]
```

SplitSeq returns an iterator over all substrings of s separated by sep. The iterator yields the same strings that would be returned by Split(s, sep), but without constructing the slice. It returns a single-use iterator.

```go

package main

import (
	"fmt"
	"strings"
)

func main() {
	s := "a,b,c,d"
	for part := range strings.SplitSeq(s, ",") {
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
func Title(s string) string
```

Title returns a copy of the string s with all Unicode letters that begin words mapped to their Unicode title case.

Deprecated: The rule Title uses for word boundaries does not handle Unicode punctuation properly. Use golang.org/x/text/cases instead.

```go

package main

import (
	"fmt"
	"strings"
)

func main() {
	// Compare this example to the ToTitle example.
	fmt.Println(strings.Title("her royal highness"))
	fmt.Println(strings.Title("loud noises"))
	fmt.Println(strings.Title("брат"))
}

```

```go
Output:
Her Royal Highness
Loud Noises
Брат

```

 Share Format Run

```go
func ToLower(s string) string
```

ToLower returns s with all Unicode letters mapped to their lower case.

```go

package main

import (
	"fmt"
	"strings"
)

func main() {
	fmt.Println(strings.ToLower("Gopher"))
}

```

```go
Output:
gopher

```

 Share Format Run

```go
func ToLowerSpecial(c unicode.SpecialCase, s string) string
```

ToLowerSpecial returns a copy of the string s with all Unicode letters mapped to their lower case using the case mapping specified by c.

```go

package main

import (
	"fmt"
	"strings"
	"unicode"
)

func main() {
	fmt.Println(strings.ToLowerSpecial(unicode.TurkishCase, "Örnek İş"))
}

```

```go
Output:
örnek iş

```

 Share Format Run

```go
func ToTitle(s string) string
```

ToTitle returns a copy of the string s with all Unicode letters mapped to their Unicode title case.

```go

package main

import (
	"fmt"
	"strings"
)

func main() {
	// Compare this example to the Title example.
	fmt.Println(strings.ToTitle("her royal highness"))
	fmt.Println(strings.ToTitle("loud noises"))
	fmt.Println(strings.ToTitle("брат"))
}

```

```go
Output:
HER ROYAL HIGHNESS
LOUD NOISES
БРАТ

```

 Share Format Run

```go
func ToTitleSpecial(c unicode.SpecialCase, s string) string
```

ToTitleSpecial returns a copy of the string s with all Unicode letters mapped to their Unicode title case, giving priority to the special casing rules.

```go

package main

import (
	"fmt"
	"strings"
	"unicode"
)

func main() {
	fmt.Println(strings.ToTitleSpecial(unicode.TurkishCase, "dünyanın ilk borsa yapısı Aizonai kabul edilir"))
}

```

```go
Output:
DÜNYANIN İLK BORSA YAPISI AİZONAİ KABUL EDİLİR

```

 Share Format Run

```go
func ToUpper(s string) string
```

ToUpper returns s with all Unicode letters mapped to their upper case.

```go

package main

import (
	"fmt"
	"strings"
)

func main() {
	fmt.Println(strings.ToUpper("Gopher"))
}

```

```go
Output:
GOPHER

```

 Share Format Run

```go
func ToUpperSpecial(c unicode.SpecialCase, s string) string
```

ToUpperSpecial returns a copy of the string s with all Unicode letters mapped to their upper case using the case mapping specified by c.

```go

package main

import (
	"fmt"
	"strings"
	"unicode"
)

func main() {
	fmt.Println(strings.ToUpperSpecial(unicode.TurkishCase, "örnek iş"))
}

```

```go
Output:
ÖRNEK İŞ

```

 Share Format Run

```go
func ToValidUTF8(s, replacement string) string
```

ToValidUTF8 returns a copy of the string s with each run of invalid UTF-8 byte sequences replaced by the replacement string, which may be empty.

```go

package main

import (
	"fmt"
	"strings"
)

func main() {
	fmt.Printf("%s\n", strings.ToValidUTF8("abc", "\uFFFD"))
	fmt.Printf("%s\n", strings.ToValidUTF8("a\xffb\xC0\xAFc\xff", ""))
	fmt.Printf("%s\n", strings.ToValidUTF8("\xed\xa0\x80", "abc"))
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
func Trim(s, cutset string) string
```

Trim returns a slice of the string s with all leading and trailing Unicode code points contained in cutset removed.

```go

package main

import (
	"fmt"
	"strings"
)

func main() {
	fmt.Print(strings.Trim("¡¡¡Hello, Gophers!!!", "!¡"))
}

```

```go
Output:
Hello, Gophers

```

 Share Format Run

```go
func TrimFunc(s string, f func(rune) bool) string
```

TrimFunc returns a slice of the string s with all leading and trailing Unicode code points c satisfying f(c) removed.

```go

package main

import (
	"fmt"
	"strings"
	"unicode"
)

func main() {
	fmt.Print(strings.TrimFunc("¡¡¡Hello, Gophers!!!", func(r rune) bool {
		return !unicode.IsLetter(r) && !unicode.IsNumber(r)
	}))
}

```

```go
Output:
Hello, Gophers

```

 Share Format Run

```go
func TrimLeft(s, cutset string) string
```

TrimLeft returns a slice of the string s with all leading Unicode code points contained in cutset removed.

To remove a prefix, use TrimPrefix instead.

```go

package main

import (
	"fmt"
	"strings"
)

func main() {
	fmt.Print(strings.TrimLeft("¡¡¡Hello, Gophers!!!", "!¡"))
}

```

```go
Output:
Hello, Gophers!!!

```

 Share Format Run

```go
func TrimLeftFunc(s string, f func(rune) bool) string
```

TrimLeftFunc returns a slice of the string s with all leading Unicode code points c satisfying f(c) removed.

```go

package main

import (
	"fmt"
	"strings"
	"unicode"
)

func main() {
	fmt.Print(strings.TrimLeftFunc("¡¡¡Hello, Gophers!!!", func(r rune) bool {
		return !unicode.IsLetter(r) && !unicode.IsNumber(r)
	}))
}

```

```go
Output:
Hello, Gophers!!!

```

 Share Format Run

```go
func TrimPrefix(s, prefix string) string
```

TrimPrefix returns s without the provided leading prefix string. If s doesn't start with prefix, s is returned unchanged.

```go

package main

import (
	"fmt"
	"strings"
)

func main() {
	var s = "¡¡¡Hello, Gophers!!!"
	s = strings.TrimPrefix(s, "¡¡¡Hello, ")
	s = strings.TrimPrefix(s, "¡¡¡Howdy, ")
	fmt.Print(s)
}

```

```go
Output:
Gophers!!!

```

 Share Format Run

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
