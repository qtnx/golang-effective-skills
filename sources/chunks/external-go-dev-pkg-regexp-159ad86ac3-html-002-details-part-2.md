---
source_name: "External Linked Documentation"
source_url: "https://go.dev/pkg/regexp/"
source_path: "sources/raw/external/go-dev-pkg-regexp-159ad86ac3.html"
license_ref: ""
---

However, there can be multiple leftmost-longest matches, with different submatch choices, and here this package diverges from POSIX. Among the possible leftmost-longest matches, this package chooses the one that a backtracking search would have found first, while POSIX specifies that the match be chosen to maximize the length of the first subexpression, then the second, and so on from left to right. The POSIX rule is computationally prohibitive and not even well-defined. See https://swtch.com/~rsc/regexp/regexp2.html#posix <https://swtch.com/~rsc/regexp/regexp2.html#posix> for details.

```go
func MustCompile(str string) *Regexp
```

MustCompile is like Compile but panics if the expression cannot be parsed. It simplifies safe initialization of global variables holding compiled regular expressions.

```go
func MustCompilePOSIX(str string) *Regexp
```

MustCompilePOSIX is like CompilePOSIX but panics if the expression cannot be parsed. It simplifies safe initialization of global variables holding compiled regular expressions.

```go
func (re *Regexp) AppendText(b []byte) ([]byte, error)
```

AppendText implements encoding.TextAppender. The output matches that of calling the Regexp.String method.

Note that the output is lossy in some cases: This method does not indicate POSIX regular expressions (i.e. those compiled by calling CompilePOSIX), or those for which the Regexp.Longest method has been called.

```go
func (re *Regexp) Copy() *Regexp
```

Copy returns a new Regexp object copied from re. Calling Regexp.Longest on one copy does not affect another.

Deprecated: In earlier releases, when using a Regexp in multiple goroutines, giving each goroutine its own copy helped to avoid lock contention. As of Go 1.12, using Copy is no longer necessary to avoid lock contention. Copy may still be appropriate if the reason for its use is to make two copies with different Regexp.Longest settings.

```go
func (re *Regexp) Expand(dst []byte, template []byte, src []byte, match []int) []byte
```

Expand appends template to dst and returns the result; during the append, Expand replaces variables in the template with corresponding matches drawn from src. The match slice should have been returned by Regexp.FindSubmatchIndex.

In the template, a variable is denoted by a substring of the form $name or ${name}, where name is a non-empty sequence of letters, digits, and underscores. A purely numeric name like $1 refers to the submatch with the corresponding index; other names refer to capturing parentheses named with the (?P<name>...) syntax. A reference to an out of range or unmatched index or a name that is not present in the regular expression is replaced with an empty slice.

In the $name form, name is taken to be as long as possible: $1x is equivalent to ${1x}, not ${1}x, and, $10 is equivalent to ${10}, not ${1}0.

To insert a literal $ in the output, use $$ in the template.

```go

package main

import (
	"fmt"
	"regexp"
)

func main() {
	content := []byte(`
	# comment line
	option1: value1
	option2: value2

# another comment line
	option3: value3
`)

// Regex pattern captures "key: value" pair from the content.
	pattern := regexp.MustCompile(`(?m)(?P<key>\w+):\s+(?P<value>\w+)$`)

// Template to convert "key: value" to "key=value" by
	// referencing the values captured by the regex pattern.
	template := []byte("$key=$value\n")

result := []byte{}

// For each match of the regex in the content.
	for _, submatches := range pattern.FindAllSubmatchIndex(content, -1) {
		// Apply the captured submatches to the template and append the output
		// to the result.
		result = pattern.Expand(result, template, content, submatches)
	}
	fmt.Println(string(result))
}

```

```go
Output:
option1=value1
option2=value2
option3=value3

```

Share Format Run

```go
func (re *Regexp) ExpandString(dst []byte, template string, src string, match []int) []byte
```

ExpandString is like Regexp.Expand but the template and source are strings. It appends to and returns a byte slice in order to give the calling code control over allocation.

```go

package main

import (
	"fmt"
	"regexp"
)

func main() {
	content := `
	# comment line
	option1: value1
	option2: value2

# another comment line
	option3: value3
`

// Regex pattern captures "key: value" pair from the content.
	pattern := regexp.MustCompile(`(?m)(?P<key>\w+):\s+(?P<value>\w+)$`)

// Template to convert "key: value" to "key=value" by
	// referencing the values captured by the regex pattern.
	template := "$key=$value\n"

result := []byte{}

// For each match of the regex in the content.
	for _, submatches := range pattern.FindAllStringSubmatchIndex(content, -1) {
		// Apply the captured submatches to the template and append the output
		// to the result.
		result = pattern.ExpandString(result, template, content, submatches)
	}
	fmt.Println(string(result))
}

```

```go
Output:
option1=value1
option2=value2
option3=value3

```

Share Format Run

```go
func (re *Regexp) Find(b []byte) []byte
```

Find returns a slice holding the text of the leftmost match in b of the regular expression. A return value of nil indicates no match.

```go

package main

import (
	"fmt"
	"regexp"
)

func main() {
	re := regexp.MustCompile(`foo.?`)
	fmt.Printf("%q\n", re.Find([]byte(`seafood fool`)))

}

```

```go
Output:
"food"

```

Share Format Run

```go
func (re *Regexp) FindAll(b []byte, n int) [][]byte
```

FindAll is the 'All' version of Regexp.Find; it returns a slice of all successive matches of the expression, as defined by the 'All' description in the package comment. A return value of nil indicates no match.

```go

package main

import (
	"fmt"
	"regexp"
)

func main() {
	re := regexp.MustCompile(`foo.?`)
	fmt.Printf("%q\n", re.FindAll([]byte(`seafood fool`), -1))

}

```

```go
Output:
["food" "fool"]

```

Share Format Run

```go
func (re *Regexp) FindAllIndex(b []byte, n int) [][]int
```

FindAllIndex is the 'All' version of Regexp.FindIndex; it returns a slice of all successive matches of the expression, as defined by the 'All' description in the package comment. A return value of nil indicates no match.

```go

package main

import (
	"fmt"
	"regexp"
)

func main() {
	content := []byte("London")
	re := regexp.MustCompile(`o.`)
	fmt.Println(re.FindAllIndex(content, 1))
	fmt.Println(re.FindAllIndex(content, -1))
}

```

```go
Output:
[[1 3]]
[[1 3] [4 6]]

```

Share Format Run

```go
func (re *Regexp) FindAllString(s string, n int) []string
```

FindAllString is the 'All' version of Regexp.FindString; it returns a slice of all successive matches of the expression, as defined by the 'All' description in the package comment. A return value of nil indicates no match.

```go

package main

import (
	"fmt"
	"regexp"
)

func main() {
	re := regexp.MustCompile(`a.`)
	fmt.Println(re.FindAllString("paranormal", -1))
	fmt.Println(re.FindAllString("paranormal", 2))
	fmt.Println(re.FindAllString("graal", -1))
	fmt.Println(re.FindAllString("none", -1))
}

```

```go
Output:
[ar an al]
[ar an]
[aa]
[]

```

Share Format Run

```go
func (re *Regexp) FindAllStringIndex(s string, n int) [][]int
```

FindAllStringIndex is the 'All' version of Regexp.FindStringIndex; it returns a slice of all successive matches of the expression, as defined by the 'All' description in the package comment. A return value of nil indicates no match.

```go
func (re *Regexp) FindAllStringSubmatch(s string, n int) [][]string
```

FindAllStringSubmatch is the 'All' version of Regexp.FindStringSubmatch; it returns a slice of all successive matches of the expression, as defined by the 'All' description in the package comment. A return value of nil indicates no match.

```go

package main

import (
	"fmt"
	"regexp"
)

func main() {
	re := regexp.MustCompile(`a(x*)b`)
	fmt.Printf("%q\n", re.FindAllStringSubmatch("-ab-", -1))
	fmt.Printf("%q\n", re.FindAllStringSubmatch("-axxb-", -1))
	fmt.Printf("%q\n", re.FindAllStringSubmatch("-ab-axb-", -1))
	fmt.Printf("%q\n", re.FindAllStringSubmatch("-axxb-ab-", -1))
}

```

```go
Output:
[["ab" ""]]
[["axxb" "xx"]]
[["ab" ""] ["axb" "x"]]
[["axxb" "xx"] ["ab" ""]]

```

Share Format Run

```go
func (re *Regexp) FindAllStringSubmatchIndex(s string, n int) [][]int
```

FindAllStringSubmatchIndex is the 'All' version of Regexp.FindStringSubmatchIndex; it returns a slice of all successive matches of the expression, as defined by the 'All' description in the package comment. A return value of nil indicates no match.

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
	fmt.Println(re.FindAllStringSubmatchIndex("-ab-", -1))
	fmt.Println(re.FindAllStringSubmatchIndex("-axxb-", -1))
	fmt.Println(re.FindAllStringSubmatchIndex("-ab-axb-", -1))
	fmt.Println(re.FindAllStringSubmatchIndex("-axxb-ab-", -1))
	fmt.Println(re.FindAllStringSubmatchIndex("-foo-", -1))
}

```

```go
Output:
[[1 3 2 2]]
[[1 5 2 4]]
[[1 3 2 2] [4 7 5 6]]
[[1 5 2 4] [6 8 7 7]]
[]

```

Share Format Run

```go
func (re *Regexp) FindAllSubmatch(b []byte, n int) [][][]byte
```

FindAllSubmatch is the 'All' version of Regexp.FindSubmatch; it returns a slice of all successive matches of the expression, as defined by the 'All' description in the package comment. A return value of nil indicates no match.

```go

package main

import (
	"fmt"
	"regexp"
)

func main() {
	re := regexp.MustCompile(`foo(.?)`)
	fmt.Printf("%q\n", re.FindAllSubmatch([]byte(`seafood fool`), -1))

}

```

```go
Output:
[["food" "d"] ["fool" "l"]]

```

Share Format Run

```go
func (re *Regexp) FindAllSubmatchIndex(b []byte, n int) [][]int
```

FindAllSubmatchIndex is the 'All' version of Regexp.FindSubmatchIndex; it returns a slice of all successive matches of the expression, as defined by the 'All' description in the package comment. A return value of nil indicates no match.

```go

package main

import (
	"fmt"
	"regexp"
)

func main() {
	content := []byte(`
	# comment line
	option1: value1
	option2: value2
`)
	// Regex pattern captures "key: value" pair from the content.
	pattern := regexp.MustCompile(`(?m)(?P<key>\w+):\s+(?P<value>\w+)$`)
	allIndexes := pattern.FindAllSubmatchIndex(content, -1)
	for _, loc := range allIndexes {
		fmt.Println(loc)
		fmt.Println(string(content[loc[0]:loc[1]]))
		fmt.Println(string(content[loc[2]:loc[3]]))
		fmt.Println(string(content[loc[4]:loc[5]]))
	}
}

```

```go
Output:
[18 33 18 25 27 33]
option1: value1
option1
value1
[35 50 35 42 44 50]
option2: value2
option2
value2

```

Share Format Run

```go
func (re *Regexp) FindIndex(b []byte) (loc []int)
```

FindIndex returns a two-element slice of integers defining the location of the leftmost match in b of the regular expression. The match itself is at b[loc[0]:loc[1]]. A return value of nil indicates no match.

```go

package main

import (
	"fmt"
	"regexp"
)

func main() {
	content := []byte(`
	# comment line
	option1: value1
	option2: value2
`)
	// Regex pattern captures "key: value" pair from the content.
	pattern := regexp.MustCompile(`(?m)(?P<key>\w+):\s+(?P<value>\w+)$`)

loc := pattern.FindIndex(content)
	fmt.Println(loc)
	fmt.Println(string(content[loc[0]:loc[1]]))
}

```

```go
Output:
[18 33]
option1: value1

```

Share Format Run

```go
func (re *Regexp) FindReaderIndex(r io.RuneReader) (loc []int)
```
