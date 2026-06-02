---
source_name: "Google Go Style Guide"
source_url: "https://google.github.io/styleguide/go/"
source_path: "sources/raw/google-go-styleguide/best-practices.html"
license_ref: "sources/licenses/google-styleguide-LICENSE.txt"
---

#### Errors

Document significant error sentinel values or error types that your functions return to callers so that callers can anticipate what types of conditions they can handle in their code.

```go
// Good:
package os

// Read reads up to len(b) bytes from the File and stores them in b. It returns
// the number of bytes read and any error encountered.
//
// At end of file, Read returns 0, io.EOF.
func (*File) Read(b []byte) (n int, err error) {

```

When a function returns a specific error type, correctly note whether the error is a pointer receiver or not:

```go
// Good:
package os

type PathError struct {
    Op   string
    Path string
    Err  error
}

// Chdir changes the current working directory to the named directory.
//
// If there is an error, it will be of type *PathError.
func Chdir(dir string) error {

```

Documenting whether the values returned are pointer receivers enables callers to correctly compare the errors using `errors.Is`, `errors.As`, and `package cmp`. This is because a non-pointer value is not equivalent to a pointer value.

**Note:** In the `Chdir` example, the return type is written as `error` rather than `*PathError` due to how nil interface values work.

Document overall error conventions in the package’s documentation when the behavior is applicable to most errors found in the package:

```go
// Good:
// Package os provides a platform-independent interface to operating system
// functionality.
//
// Often, more information is available within the error. For example, if a
// call that takes a file name fails, such as Open or Stat, the error will
// include the failing file name when printed and will be of type *PathError,
// which may be unpacked for more information.
package os

```

Thoughtful application of these approaches can add extra information to errors without much effort and help callers avoid adding redundant annotations.

See also:

- Go Tip #106: Error Naming Conventions
- Go Tip #89: When to Use Canonical Status Codes as Errors
