---
source_name: "External Linked Documentation"
source_url: "https://go.dev/pkg/regexp/"
source_path: "sources/raw/external/go-dev-pkg-regexp-159ad86ac3.html"
license_ref: ""
---

FindReaderIndex returns a two-element slice of integers defining the location of the leftmost match of the regular expression in text read from the io.RuneReader. The match text was found in the input stream at byte offset loc[0] through loc[1]-1. A return value of nil indicates no match.

```go
func (re *Regexp) FindReaderSubmatchIndex(r io.RuneReader) []int
```

FindReaderSubmatchIndex returns a slice holding the index pairs identifying the leftmost match of the regular expression of text read by the io.RuneReader, and the matches, if any, of its subexpressions, as defined by the 'Submatch' and 'Index' descriptions in the package comment. A return value of nil indicates no match.

```go
func (re *Regexp) FindString(s string) string
```

FindString returns a string holding the text of the leftmost match in s of the regular expression. If there is no match, the return value is an empty string, but it will also be empty if the regular expression successfully matches an empty string. Use Regexp.FindStringIndex or Regexp.FindStringSubmatch if it is necessary to distinguish these cases.

```go

package main

import (
	"fmt"
	"regexp"
)

func main() {
	re := regexp.MustCompile(`foo.?`)
	fmt.Printf("%q\n", re.FindString("seafood fool"))
	fmt.Printf("%q\n", re.FindString("meat"))
}

```

```go
Output:
"food"
""

```

Share Format Run

```go
func (re *Regexp) FindStringIndex(s string) (loc []int)
```

FindStringIndex returns a two-element slice of integers defining the location of the leftmost match in s of the regular expression. The match itself is at s[loc[0]:loc[1]]. A return value of nil indicates no match.

```go

package main

import (
	"fmt"
	"regexp"
)

func main() {
	re := regexp.MustCompile(`ab?`)
	fmt.Println(re.FindStringIndex("tablett"))
	fmt.Println(re.FindStringIndex("foo") == nil)
}

```

```go
Output:
[1 3]
true

```

Share Format Run

```go
func (re *Regexp) FindStringSubmatch(s string) []string
```

FindStringSubmatch returns a slice of strings holding the text of the leftmost match of the regular expression in s and the matches, if any, of its subexpressions, as defined by the 'Submatch' description in the package comment. A return value of nil indicates no match.

```go

package main

import (
	"fmt"
	"regexp"
)

func main() {
	re := regexp.MustCompile(`a(x*)b(y|z)c`)
	fmt.Printf("%q\n", re.FindStringSubmatch("-axxxbyc-"))
	fmt.Printf("%q\n", re.FindStringSubmatch("-abzc-"))
}

```

```go
Output:
["axxxbyc" "xxx" "y"]
["abzc" "" "z"]

```

Share Format Run

```go
func (re *Regexp) FindStringSubmatchIndex(s string) []int
```

FindStringSubmatchIndex returns a slice holding the index pairs identifying the leftmost match of the regular expression in s and the matches, if any, of its subexpressions, as defined by the 'Submatch' and 'Index' descriptions in the package comment. A return value of nil indicates no match.

```go
func (re *Regexp) FindSubmatch(b []byte) [][]byte
```

FindSubmatch returns a slice of slices holding the text of the leftmost match of the regular expression in b and the matches, if any, of its subexpressions, as defined by the 'Submatch' descriptions in the package comment. A return value of nil indicates no match.

```go

package main

import (
	"fmt"
	"regexp"
)

func main() {
	re := regexp.MustCompile(`foo(.?)`)
	fmt.Printf("%q\n", re.FindSubmatch([]byte(`seafood fool`)))

}

```

```go
Output:
["food" "d"]

```

Share Format Run

```go
func (re *Regexp) FindSubmatchIndex(b []byte) []int
```

FindSubmatchIndex returns a slice holding the index pairs identifying the leftmost match of the regular expression in b and the matches, if any, of its subexpressions, as defined by the 'Submatch' and 'Index' descriptions in the package comment. A return value of nil indicates no match.

```go

package main

import (
	"fmt"
	"regexp"
)

func main() {
	re := regexp.MustCompile(`a(x*)b`)
	// Indices:
	//    01234567   012345678
	//    -ab-axb-   -axxb-ab-
	fmt.Println(re.FindSubmatchIndex([]byte("-ab-")))
	fmt.Println(re.FindSubmatchIndex([]byte("-axxb-")))
	fmt.Println(re.FindSubmatchIndex([]byte("-ab-axb-")))
	fmt.Println(re.FindSubmatchIndex([]byte("-axxb-ab-")))
	fmt.Println(re.FindSubmatchIndex([]byte("-foo-")))
}

```

```go
Output:
[1 3 2 2]
[1 5 2 4]
[1 3 2 2]
[1 5 2 4]
[]

```

Share Format Run

```go
func (re *Regexp) LiteralPrefix() (prefix string, complete bool)
```

LiteralPrefix returns a literal string that must begin any match of the regular expression re. It returns the boolean true if the literal string comprises the entire regular expression.

```go
func (re *Regexp) Longest()
```

Longest makes future searches prefer the leftmost-longest match. That is, when matching against text, the regexp returns a match that begins as early as possible in the input (leftmost), and among those it chooses a match that is as long as possible. This method modifies the Regexp and may not be called concurrently with any other methods.

```go

package main

import (
	"fmt"
	"regexp"
)

func main() {
	re := regexp.MustCompile(`a(|b)`)
	fmt.Println(re.FindString("ab"))
	re.Longest()
	fmt.Println(re.FindString("ab"))
}

```

```go
Output:
a
ab

```

Share Format Run

```go
func (re *Regexp) MarshalText() ([]byte, error)
```

MarshalText implements encoding.TextMarshaler. The output matches that of calling the Regexp.AppendText method.

See Regexp.AppendText for more information.

```go
func (re *Regexp) Match(b []byte) bool
```

Match reports whether the byte slice b contains any match of the regular expression re.

```go

package main

import (
	"fmt"
	"regexp"
)

func main() {
	re := regexp.MustCompile(`foo.?`)
	fmt.Println(re.Match([]byte(`seafood fool`)))
	fmt.Println(re.Match([]byte(`something else`)))

}

```

```go
Output:
true
false

```

Share Format Run

```go
func (re *Regexp) MatchReader(r io.RuneReader) bool
```

MatchReader reports whether the text returned by the io.RuneReader contains any match of the regular expression re.

```go
func (re *Regexp) MatchString(s string) bool
```

MatchString reports whether the string s contains any match of the regular expression re.

```go

package main

import (
	"fmt"
	"regexp"
)

func main() {
	re := regexp.MustCompile(`(gopher){2}`)
	fmt.Println(re.MatchString("gopher"))
	fmt.Println(re.MatchString("gophergopher"))
	fmt.Println(re.MatchString("gophergophergopher"))
}

```

```go
Output:
false
true
true

```

Share Format Run

```go
func (re *Regexp) NumSubexp() int
```

NumSubexp returns the number of parenthesized subexpressions in this Regexp.

```go

package main

import (
	"fmt"
	"regexp"
)

func main() {
	re0 := regexp.MustCompile(`a.`)
	fmt.Printf("%d\n", re0.NumSubexp())

re := regexp.MustCompile(`(.*)((a)b)(.*)a`)
	fmt.Println(re.NumSubexp())
}

```

```go
Output:
0
4

```

Share Format Run

```go
func (re *Regexp) ReplaceAll(src, repl []byte) []byte
```

ReplaceAll returns a copy of src, replacing matches of the Regexp with the replacement text repl. Inside repl, $ signs are interpreted as in Regexp.Expand.

```go

package main

import (
	"fmt"
	"regexp"
)

func main() {
	re := regexp.MustCompile(`a(x*)b`)
	fmt.Printf("%s\n", re.ReplaceAll([]byte("-ab-axxb-"), []byte("T")))
	fmt.Printf("%s\n", re.ReplaceAll([]byte("-ab-axxb-"), []byte("$1")))
	fmt.Printf("%s\n", re.ReplaceAll([]byte("-ab-axxb-"), []byte("$1W")))
	fmt.Printf("%s\n", re.ReplaceAll([]byte("-ab-axxb-"), []byte("${1}W")))

re2 := regexp.MustCompile(`a(?P<1W>x*)b`)
	fmt.Printf("%s\n", re2.ReplaceAll([]byte("-ab-axxb-"), []byte("$1W")))
	fmt.Printf("%s\n", re2.ReplaceAll([]byte("-ab-axxb-"), []byte("${1}W")))

}

```

```go
Output:
-T-T-
--xx-
---
-W-xxW-
--xx-
-W-xxW-

```

Share Format Run

```go
func (re *Regexp) ReplaceAllFunc(src []byte, repl func([]byte) []byte) []byte
```

ReplaceAllFunc returns a copy of src in which all matches of the Regexp have been replaced by the return value of function repl applied to the matched byte slice. The replacement returned by repl is substituted directly, without using Regexp.Expand.

```go
func (re *Regexp) ReplaceAllLiteral(src, repl []byte) []byte
```

ReplaceAllLiteral returns a copy of src, replacing matches of the Regexp with the replacement bytes repl. The replacement repl is substituted directly, without using Regexp.Expand.

```go
func (re *Regexp) ReplaceAllLiteralString(src, repl string) string
```

ReplaceAllLiteralString returns a copy of src, replacing matches of the Regexp with the replacement string repl. The replacement repl is substituted directly, without using Regexp.Expand.

```go

package main

import (
	"fmt"
	"regexp"
)

func main() {
	re := regexp.MustCompile(`a(x*)b`)
	fmt.Println(re.ReplaceAllLiteralString("-ab-axxb-", "T"))
	fmt.Println(re.ReplaceAllLiteralString("-ab-axxb-", "$1"))
	fmt.Println(re.ReplaceAllLiteralString("-ab-axxb-", "${1}"))
}

```

```go
Output:
-T-T-
-$1-$1-
-${1}-${1}-

```

Share Format Run

```go
func (re *Regexp) ReplaceAllString(src, repl string) string
```

ReplaceAllString returns a copy of src, replacing matches of the Regexp with the replacement string repl. Inside repl, $ signs are interpreted as in Regexp.Expand.

```go

package main

import (
	"fmt"
	"regexp"
)

func main() {
	re := regexp.MustCompile(`a(x*)b`)
	fmt.Println(re.ReplaceAllString("-ab-axxb-", "T"))
	fmt.Println(re.ReplaceAllString("-ab-axxb-", "$1"))
	fmt.Println(re.ReplaceAllString("-ab-axxb-", "$1W"))
	fmt.Println(re.ReplaceAllString("-ab-axxb-", "${1}W"))

re2 := regexp.MustCompile(`a(?P<1W>x*)b`)
	fmt.Printf("%s\n", re2.ReplaceAllString("-ab-axxb-", "$1W"))
	fmt.Println(re.ReplaceAllString("-ab-axxb-", "${1}W"))

}

```

```go
Output:
-T-T-
--xx-
---
-W-xxW-
--xx-
-W-xxW-

```

Share Format Run

```go
func (re *Regexp) ReplaceAllStringFunc(src string, repl func(string) string) string
```

ReplaceAllStringFunc returns a copy of src in which all matches of the Regexp have been replaced by the return value of function repl applied to the matched substring. The replacement returned by repl is substituted directly, without using Regexp.Expand.

```go

package main

import (
	"fmt"
	"regexp"
	"strings"
)

func main() {
	re := regexp.MustCompile(`[^aeiou]`)
	fmt.Println(re.ReplaceAllStringFunc("seafood fool", strings.ToUpper))
}

```

```go
Output:
SeaFooD FooL

```

Share Format Run

```go
func (re *Regexp) Split(s string, n int) []string
```

Split slices s into substrings separated by the expression and returns a slice of the substrings between those expression matches.

The slice returned by this method consists of all the substrings of s not contained in the slice returned by Regexp.FindAllString. When called on an expression that contains no metacharacters, it is equivalent to strings.SplitN.

Example:

```go
s := regexp.MustCompile("a*").Split("abaabaccadaaae", 5)
// s: ["", "b", "b", "c", "cadaaae"]

```

The count determines the number of substrings to return:

- n > 0: at most n substrings; the last substring will be the unsplit remainder;
- n == 0: the result is nil (zero substrings);
- n < 0: all substrings.

```go

package main

import (
	"fmt"
	"regexp"
)

func main() {
	a := regexp.MustCompile(`a`)
	fmt.Println(a.Split("banana", -1))
	fmt.Println(a.Split("banana", 0))
	fmt.Println(a.Split("banana", 1))
	fmt.Println(a.Split("banana", 2))
	zp := regexp.MustCompile(`z+`)
	fmt.Println(zp.Split("pizza", -1))
	fmt.Println(zp.Split("pizza", 0))
	fmt.Println(zp.Split("pizza", 1))
	fmt.Println(zp.Split("pizza", 2))
}

```

```go
Output:
[b n n ]
[]
[banana]
[b nana]
[pi a]
[]
[pizza]
[pi a]

```

Share Format Run

```go
func (re *Regexp) String() string
```

String returns the source text used to compile the regular expression.

```go
func (re *Regexp) SubexpIndex(name string) int
```

SubexpIndex returns the index of the first subexpression with the given name, or -1 if there is no subexpression with that name.

Note that multiple subexpressions can be written using the same name, as in (?P<bob>a+)(?P<bob>b+), which declares two subexpressions named "bob". In this case, SubexpIndex returns the index of the leftmost such subexpression in the regular expression.

```go

package main

import (
	"fmt"
	"regexp"
)

func main() {
	re := regexp.MustCompile(`(?P<first>[a-zA-Z]+) (?P<last>[a-zA-Z]+)`)
	fmt.Println(re.MatchString("Alan Turing"))
	matches := re.FindStringSubmatch("Alan Turing")
	lastIndex := re.SubexpIndex("last")
	fmt.Printf("last => %d\n", lastIndex)
	fmt.Println(matches[lastIndex])
}
