---
source_name: "External Linked Documentation"
source_url: "https://go.dev/pkg/regexp/"
source_path: "sources/raw/external/go-dev-pkg-regexp-159ad86ac3.html"
license_ref: ""
---

regexp package - regexp - Go Packages
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

Package regexp implements regular expression search.

The syntax of the regular expressions accepted is the same general syntax used by Perl, Python, and other languages. More precisely, it is the syntax accepted by RE2 and described at https://golang.org/s/re2syntax <https://golang.org/s/re2syntax>, except for \C. For an overview of the syntax, see the regexp/syntax package.

The regexp implementation provided by this package is guaranteed to run in time linear in the size of the input. (This is a property not guaranteed by most open source implementations of regular expressions.) For more information about this property, see https://swtch.com/~rsc/regexp/regexp1.html <https://swtch.com/~rsc/regexp/regexp1.html> or any book about automata theory.

All characters are UTF-8-encoded code points. Following utf8.DecodeRune, each byte of an invalid UTF-8 sequence is treated as if it encoded utf8.RuneError (U+FFFD).

There are 16 methods of Regexp that match a regular expression and identify the matched text. Their names are matched by this regular expression:

```go
Find(All)?(String)?(Submatch)?(Index)?

```

If 'All' is present, the routine matches successive non-overlapping matches of the entire expression. Empty matches abutting a preceding match are ignored. The return value is a slice containing the successive return values of the corresponding non-'All' routine. These routines take an extra integer argument, n. If n >= 0, the function returns at most n matches/submatches; otherwise, it returns all of them.

If 'String' is present, the argument is a string; otherwise it is a slice of bytes; return values are adjusted as appropriate.

If 'Submatch' is present, the return value is a slice identifying the successive submatches of the expression. Submatches are matches of parenthesized subexpressions (also known as capturing groups) within the regular expression, numbered from left to right in order of opening parenthesis. Submatch 0 is the match of the entire expression, submatch 1 is the match of the first parenthesized subexpression, and so on.

If 'Index' is present, matches and submatches are identified by byte index pairs within the input string: result[2*n:2*n+2] identifies the indexes of the nth submatch. The pair for n==0 identifies the match of the entire expression. If 'Index' is not present, the match is identified by the text of the match/submatch. If an index is negative or text is nil, it means that subexpression did not match any string in the input. For 'String' versions an empty string means either no match or an empty match.

There is also a subset of the methods that can be applied to text read from an io.RuneReader: Regexp.MatchReader, Regexp.FindReaderIndex, Regexp.FindReaderSubmatchIndex.

This set may grow. Note that regular expression matches may need to examine text beyond the text returned by a match, so the methods that match text from an io.RuneReader may read arbitrarily far into the input before returning.

(There are a few other methods that do not match this pattern.)

```go

package main

import (
	"fmt"
	"regexp"
)

func main() {
	// Compile the expression once, usually at init time.
	// Use raw strings to avoid having to quote the backslashes.
	var validID = regexp.MustCompile(`^[a-z]+\[[0-9]+\]$`)

fmt.Println(validID.MatchString("adam[23]"))
	fmt.Println(validID.MatchString("eve[7]"))
	fmt.Println(validID.MatchString("Job[48]"))
	fmt.Println(validID.MatchString("snakey"))
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

-  func Match(pattern string, b []byte) (matched bool, err error)
-  func MatchReader(pattern string, r io.RuneReader) (matched bool, err error)
-  func MatchString(pattern string, s string) (matched bool, err error)
-  func QuoteMeta(s string) string
-  type Regexp
-
-  func Compile(expr string) (*Regexp, error)
-  func CompilePOSIX(expr string) (*Regexp, error)
-  func MustCompile(str string) *Regexp
-  func MustCompilePOSIX(str string) *Regexp

-
-  func (re *Regexp) AppendText(b []byte) ([]byte, error)
-  func (re *Regexp) Copy() *Regexpdeprecated
-  func (re *Regexp) Expand(dst []byte, template []byte, src []byte, match []int) []byte
-  func (re *Regexp) ExpandString(dst []byte, template string, src string, match []int) []byte
-  func (re *Regexp) Find(b []byte) []byte
-  func (re *Regexp) FindAll(b []byte, n int) [][]byte
-  func (re *Regexp) FindAllIndex(b []byte, n int) [][]int
-  func (re *Regexp) FindAllString(s string, n int) []string
-  func (re *Regexp) FindAllStringIndex(s string, n int) [][]int
-  func (re *Regexp) FindAllStringSubmatch(s string, n int) [][]string
-  func (re *Regexp) FindAllStringSubmatchIndex(s string, n int) [][]int
-  func (re *Regexp) FindAllSubmatch(b []byte, n int) [][][]byte
-  func (re *Regexp) FindAllSubmatchIndex(b []byte, n int) [][]int
-  func (re *Regexp) FindIndex(b []byte) (loc []int)
-  func (re *Regexp) FindReaderIndex(r io.RuneReader) (loc []int)
-  func (re *Regexp) FindReaderSubmatchIndex(r io.RuneReader) []int
-  func (re *Regexp) FindString(s string) string
-  func (re *Regexp) FindStringIndex(s string) (loc []int)
-  func (re *Regexp) FindStringSubmatch(s string) []string
-  func (re *Regexp) FindStringSubmatchIndex(s string) []int
-  func (re *Regexp) FindSubmatch(b []byte) [][]byte
-  func (re *Regexp) FindSubmatchIndex(b []byte) []int
-  func (re *Regexp) LiteralPrefix() (prefix string, complete bool)
-  func (re *Regexp) Longest()
-  func (re *Regexp) MarshalText() ([]byte, error)
-  func (re *Regexp) Match(b []byte) bool
-  func (re *Regexp) MatchReader(r io.RuneReader) bool
-  func (re *Regexp) MatchString(s string) bool
-  func (re *Regexp) NumSubexp() int
-  func (re *Regexp) ReplaceAll(src, repl []byte) []byte
-  func (re *Regexp) ReplaceAllFunc(src []byte, repl func([]byte) []byte) []byte
-  func (re *Regexp) ReplaceAllLiteral(src, repl []byte) []byte
-  func (re *Regexp) ReplaceAllLiteralString(src, repl string) string
-  func (re *Regexp) ReplaceAllString(src, repl string) string
-  func (re *Regexp) ReplaceAllStringFunc(src string, repl func(string) string) string
-  func (re *Regexp) Split(s string, n int) []string
-  func (re *Regexp) String() string
-  func (re *Regexp) SubexpIndex(name string) int
-  func (re *Regexp) SubexpNames() []string
-  func (re *Regexp) UnmarshalText(text []byte) error

- Package
- Match
- MatchString
- QuoteMeta
- Regexp.Expand
- Regexp.ExpandString
- Regexp.Find
- Regexp.FindAll
- Regexp.FindAllIndex
- Regexp.FindAllString
- Regexp.FindAllStringSubmatch
- Regexp.FindAllStringSubmatchIndex
- Regexp.FindAllSubmatch
- Regexp.FindAllSubmatchIndex
- Regexp.FindIndex
- Regexp.FindString
- Regexp.FindStringIndex
- Regexp.FindStringSubmatch
- Regexp.FindSubmatch
- Regexp.FindSubmatchIndex
- Regexp.Longest
- Regexp.Match
- Regexp.MatchString
- Regexp.NumSubexp
- Regexp.ReplaceAll
- Regexp.ReplaceAllLiteralString
- Regexp.ReplaceAllString
- Regexp.ReplaceAllStringFunc
- Regexp.Split
- Regexp.SubexpIndex
- Regexp.SubexpNames

This section is empty.

This section is empty.

```go
func Match(pattern string, b []byte) (matched bool, err error)
```

Match reports whether the byte slice b contains any match of the regular expression pattern. More complicated queries need to use Compile and the full Regexp interface.

```go

package main

import (
	"fmt"
	"regexp"
)

func main() {
	matched, err := regexp.Match(`foo.*`, []byte(`seafood`))
	fmt.Println(matched, err)
	matched, err = regexp.Match(`bar.*`, []byte(`seafood`))
	fmt.Println(matched, err)
	matched, err = regexp.Match(`a(b`, []byte(`seafood`))
	fmt.Println(matched, err)

}

```

```go
Output:
true <nil>
false <nil>
false error parsing regexp: missing closing ): `a(b`

```

Share Format Run

```go
func MatchReader(pattern string, r io.RuneReader) (matched bool, err error)
```

MatchReader reports whether the text returned by the io.RuneReader contains any match of the regular expression pattern. More complicated queries need to use Compile and the full Regexp interface.

```go
func MatchString(pattern string, s string) (matched bool, err error)
```

MatchString reports whether the string s contains any match of the regular expression pattern. More complicated queries need to use Compile and the full Regexp interface.

```go

package main

import (
	"fmt"
	"regexp"
)

func main() {
	matched, err := regexp.MatchString(`foo.*`, "seafood")
	fmt.Println(matched, err)
	matched, err = regexp.MatchString(`bar.*`, "seafood")
	fmt.Println(matched, err)
	matched, err = regexp.MatchString(`a(b`, "seafood")
	fmt.Println(matched, err)
}

```

```go
Output:
true <nil>
false <nil>
false error parsing regexp: missing closing ): `a(b`

```

Share Format Run

```go
func QuoteMeta(s string) string
```

QuoteMeta returns a string that escapes all regular expression metacharacters inside the argument text; the returned string is a regular expression matching the literal text.

```go

package main

import (
	"fmt"
	"regexp"
)

func main() {
	fmt.Println(regexp.QuoteMeta(`Escaping symbols like: .+*?()|[]{}^$`))
}

```

```go
Output:
Escaping symbols like: \.\+\*\?\(\)\|\[\]\{\}\^\$

```

Share Format Run

```go
type Regexp struct {
	// contains filtered or unexported fields
}
```

Regexp is the representation of a compiled regular expression. A Regexp is safe for concurrent use by multiple goroutines, except for configuration methods, such as Regexp.Longest.

```go
func Compile(expr string) (*Regexp, error)
```

Compile parses a regular expression and returns, if successful, a Regexp object that can be used to match against text.

When matching against text, the regexp returns a match that begins as early as possible in the input (leftmost), and among those it chooses the one that a backtracking search would have found first. This so-called leftmost-first matching is the same semantics that Perl, Python, and other implementations use, although this package implements it without the expense of backtracking. For POSIX leftmost-longest matching, see CompilePOSIX.

```go
func CompilePOSIX(expr string) (*Regexp, error)
```

CompilePOSIX is like Compile but restricts the regular expression to POSIX ERE (egrep) syntax and changes the match semantics to leftmost-longest.

That is, when matching against text, the regexp returns a match that begins as early as possible in the input (leftmost), and among those it chooses a match that is as long as possible. This so-called leftmost-longest matching is the same semantics that early regular expression implementations used and that POSIX specifies.
