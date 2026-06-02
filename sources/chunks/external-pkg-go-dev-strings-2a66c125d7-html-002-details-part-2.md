---
source_name: "External Linked Documentation"
source_url: "https://pkg.go.dev/strings"
source_path: "sources/raw/external/pkg-go-dev-strings-2a66c125d7.html"
license_ref: ""
---

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
