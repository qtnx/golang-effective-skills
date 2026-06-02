---
source_name: "External Linked Documentation"
source_url: "https://pkg.go.dev/bytes"
source_path: "sources/raw/external/pkg-go-dev-bytes-42228f0497.html"
license_ref: ""
---

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
