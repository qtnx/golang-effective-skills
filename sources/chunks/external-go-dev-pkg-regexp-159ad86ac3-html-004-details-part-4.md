---
source_name: "External Linked Documentation"
source_url: "https://go.dev/pkg/regexp/"
source_path: "sources/raw/external/go-dev-pkg-regexp-159ad86ac3.html"
license_ref: ""
---

```

```go
Output:
true
last => 2
Turing

```

Share Format Run

```go
func (re *Regexp) SubexpNames() []string
```

SubexpNames returns the names of the parenthesized subexpressions in this Regexp. The name for the first sub-expression is names[1], so that if m is a match slice, the name for m[i] is SubexpNames()[i]. Since the Regexp as a whole cannot be named, names[0] is always the empty string. The slice should not be modified.

```go

package main

import (
	"fmt"
	"regexp"
)

func main() {
	re := regexp.MustCompile(`(?P<first>[a-zA-Z]+) (?P<last>[a-zA-Z]+)`)
	fmt.Println(re.MatchString("Alan Turing"))
	fmt.Printf("%q\n", re.SubexpNames())
	reversed := fmt.Sprintf("${%s} ${%s}", re.SubexpNames()[2], re.SubexpNames()[1])
	fmt.Println(reversed)
	fmt.Println(re.ReplaceAllString("Alan Turing", reversed))
}

```

```go
Output:
true
["" "first" "last"]
${last} ${first}
Turing Alan

```

Share Format Run

```go
func (re *Regexp) UnmarshalText(text []byte) error
```

UnmarshalText implements encoding.TextUnmarshaler by calling Compile on the encoded value.

##   Source Files ¶
 View all Source files <https://cs.opensource.google/go/go/+/go1.26.3:src/regexp>

- backtrack.go <https://cs.opensource.google/go/go/+/go1.26.3:src/regexp/backtrack.go>
- exec.go <https://cs.opensource.google/go/go/+/go1.26.3:src/regexp/exec.go>
- onepass.go <https://cs.opensource.google/go/go/+/go1.26.3:src/regexp/onepass.go>
- regexp.go <https://cs.opensource.google/go/go/+/go1.26.3:src/regexp/regexp.go>

##   Directories ¶
    Show internal   Expand all

syntax
 Package syntax parses regular expressions into parse trees and compiles parse trees into programs.

Package syntax parses regular expressions into parse trees and compiles parse trees into programs.

Click to show internal directories.
  Click to hide internal directories.

Close

**?** : This menu   **/** : Search site   **f** or **F** : Jump to   **y** or **Y**  : Canonical URL
  Close
