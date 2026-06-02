---
source_name: "External Linked Documentation"
source_url: "https://go.dev/talks/2014/organizeio.slide"
source_path: "sources/raw/external/go-dev-talks-2014-organizeio-slide-f62aaae46e.html"
license_ref: ""
---

# Organizing Go code

Organizing Go code
# Organizing Go code
 David Crawshaw
## Packages
 2
### Go programs are made up of packages

 All Go source is part of a package.
 Every file begins with a package statement.
 Programs start in package main.

```go
package main

import "fmt"

func main() {
    fmt.Println("Hello, world!")
}

```

 For very small programs, `main` is the only package you need to write.

 The hello world program _imports_ package `fmt`.

 The function `Println` is defined in the fmt package.
 3
### An example package: fmt

```go
// Package fmt implements formatted I/O.
package fmt

// Println formats using the default formats for its
// operands and writes to standard output.
func Println(a ...interface{}) (n int, err error) {
    ...
}

func newPrinter() *pp {
    ...
}
```

 The `Println` function is _exported_. It starts with an upper case
 letter, which means other packages are allowed to call it.

 The `newPrinter` function is _unexported_. It starts with a lower
 case letter, so it can only be used inside the fmt package.
 4
### The shape of a package

 Packages collect related code.

 They can be big or small,
 and may be spread across multiple files.

 All the files in a package live in a single directory.

 The `net/http` package exports more than 100 names. (18 files)
 The `errors` package exports just one. (1 file)
 5
### The name of a package

 Keep package names short and meaningful.
 Don't use underscores, they make package names long.

- `io/ioutil` not `io/util`
- `suffixarray` not `suffix_array`

 Don't overgeneralize. A `util` package could be anything.

 The name of a package is part of its type and function names.
 On its own, type `Buffer` is ambiguous. But users see:

```go
buf := new(bytes.Buffer)
```

 Choose package names carefully.

 Choose good names for users.
 6
### The testing of a package

 Tests are distinguished by file name. Test files end in `_test.go`.

```go
package fmt

import "testing"

var fmtTests = []fmtTest{
    {"%d", 12345, "12345"},
    {"%v", 12345, "12345"},
    {"%t", true, "true"},
}

func TestSprintf(t *testing.T) {
    for _, tt := range fmtTests {
        if s := Sprintf(tt.fmt, tt.val); s != tt.out {
            t.Errorf("...")
        }
    }
}
```

 Test well.
 7
