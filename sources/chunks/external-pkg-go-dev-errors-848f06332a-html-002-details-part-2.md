---
source_name: "External Linked Documentation"
source_url: "https://pkg.go.dev/errors"
source_path: "sources/raw/external/pkg-go-dev-errors-848f06332a.html"
license_ref: ""
---

```go
Output:
Error equals fs.ErrPermission: false
Error is fs.ErrPermission: true

```

Share Format Run

```go
func Join(errs ...error) error
```

Join returns an error that wraps the given errors. Any nil error values are discarded. Join returns nil if every value in errs is nil. The error formats as the concatenation of the strings obtained by calling the Error method of each element of errs, with a newline between each string.

A non-nil error returned by Join implements the Unwrap() []error method. The errors may be inspected with Is and As.

```go

package main

import (
	"errors"
	"fmt"
)

func main() {
	err1 := errors.New("err1")
	err2 := errors.New("err2")
	err := errors.Join(err1, err2)
	fmt.Println(err)
	if errors.Is(err, err1) {
		fmt.Println("err is err1")
	}
	if errors.Is(err, err2) {
		fmt.Println("err is err2")
	}
	fmt.Println(err.(interface{ Unwrap() []error }).Unwrap())
}

```

```go
Output:
err1
err2
err is err1
err is err2
[err1 err2]

```

Share Format Run

```go
func New(text string) error
```

New returns an error that formats as the given text. Each call to New returns a distinct error value even if the text is identical.

```go

package main

import (
	"errors"
	"fmt"
)

func main() {
	err := errors.New("emit macho dwarf: elf header corrupted")
	if err != nil {
		fmt.Print(err)
	}
}

```

```go
Output:
emit macho dwarf: elf header corrupted

```

Share Format Run

The fmt package's Errorf function lets us use the package's formatting features to create descriptive error messages.

```go

package main

import (
	"fmt"
)

func main() {
	const name, id = "bimmler", 17
	err := fmt.Errorf("user %q (id %d) not found", name, id)
	if err != nil {
		fmt.Print(err)
	}
}

```

```go
Output:
user "bimmler" (id 17) not found

```

Share Format Run

Each call to errors.New returns an unique instance of the error, even if the arguments are the same. To match against errors created by errors.New, declare a sentinel error and reuse it.

```go

package main

import (
	"errors"
	"fmt"
)

func OopsNew() error {
	return errors.New("an error")
}

var ErrSentinel = errors.New("an error")

func OopsSentinel() error {
	return ErrSentinel
}

func main() {
	err1 := OopsNew()
	err2 := OopsNew()
	fmt.Println("Errors using distinct errors.New calls:")
	fmt.Printf("Is(%q, %q) = %v\n", err1, err2, errors.Is(err1, err2))

err3 := OopsSentinel()
	err4 := OopsSentinel()
	fmt.Println()
	fmt.Println("Errors using a sentinel error:")
	fmt.Printf("Is(%q, %q) = %v\n", err3, err4, errors.Is(err3, err4))

}

```

```go
Output:
Errors using distinct errors.New calls:
Is("an error", "an error") = false

Errors using a sentinel error:
Is("an error", "an error") = true

```

Share Format Run

```go
func Unwrap(err error) error
```

Unwrap returns the result of calling the Unwrap method on err, if err's type contains an Unwrap method returning error. Otherwise, Unwrap returns nil.

Unwrap only calls a method of the form "Unwrap() error". In particular Unwrap does not unwrap errors returned by Join.

```go

package main

import (
	"errors"
	"fmt"
)

func main() {
	err1 := errors.New("error1")
	err2 := fmt.Errorf("error2: [%w]", err1)
	fmt.Println(err2)
	fmt.Println(errors.Unwrap(err2))
}

```

```go
Output:
error2: [error1]
error1

```

Share Format Run

This section is empty.

##   Source Files ¶
 View all Source files <https://cs.opensource.google/go/go/+/go1.26.3:src/errors>

- errors.go <https://cs.opensource.google/go/go/+/go1.26.3:src/errors/errors.go>
- join.go <https://cs.opensource.google/go/go/+/go1.26.3:src/errors/join.go>
- wrap.go <https://cs.opensource.google/go/go/+/go1.26.3:src/errors/wrap.go>

Click to show internal directories.
  Click to hide internal directories.

Close

**?** : This menu   **/** : Search site   **f** or **F** : Jump to   **y** or **Y**  : Canonical URL
  Close
