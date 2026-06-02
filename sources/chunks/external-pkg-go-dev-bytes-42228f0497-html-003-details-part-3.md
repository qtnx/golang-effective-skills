---
source_name: "External Linked Documentation"
source_url: "https://pkg.go.dev/bytes"
source_path: "sources/raw/external/pkg-go-dev-bytes-42228f0497.html"
license_ref: ""
---

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
