---
source_name: "External Linked Documentation"
source_url: "https://pkg.go.dev/strings"
source_path: "sources/raw/external/pkg-go-dev-strings-2a66c125d7.html"
license_ref: ""
---

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
