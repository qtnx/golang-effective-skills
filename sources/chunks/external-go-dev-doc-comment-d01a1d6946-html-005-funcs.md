---
source_name: "External Linked Documentation"
source_url: "https://go.dev/doc/comment"
source_path: "sources/raw/external/go-dev-doc-comment-d01a1d6946.html"
license_ref: ""
---

# Go Doc Comments

## Funcs

A function’s doc comment should explain what the function returns or, for functions called for side effects, what it does. Named parameters and results can be referred to directly in the comment, without any special syntax like backquotes. (A consequence of this convention is that names like `a`, which might be mistaken for ordinary words, are typically avoided.) For example:

```go
package strconv

// Quote returns a double-quoted Go string literal representing s.
// The returned string uses Go escape sequences (\t, \n, \xFF, \u0100)
// for control characters and non-printable characters as defined by IsPrint.
func Quote(s string) string {
    ...
}

```

And:

```go
package os

// Exit causes the current program to exit with the given status code.
// Conventionally, code zero indicates success, non-zero an error.
// The program terminates immediately; deferred functions are not run.
//
// For portability, the status code should be in the range [0, 125].
func Exit(code int) {
    ...
}

```

Doc comments typically use the phrase “reports whether” to describe functions that return a boolean. The phrase “or not” is unnecessary. For example:

```go
package strings

// HasPrefix reports whether the string s begins with prefix.
func HasPrefix(s, prefix string) bool

```

If a doc comment needs to explain multiple results, naming the results can make the doc comment more understandable, even if the names are not used in the body of the function. For example:

```go
package io

// Copy copies from src to dst until either EOF is reached
// on src or an error occurs. It returns the total number of bytes
// written and the first error encountered while copying, if any.
//
// A successful Copy returns err == nil, not err == EOF.
// Because Copy is defined to read from src until EOF, it does
// not treat an EOF from Read as an error to be reported.
func Copy(dst Writer, src Reader) (n int64, err error) {
    ...
}

```

Conversely, when the results don’t need to be named in the doc comment, they are usually omitted in the code as well, like in the `Quote` example above, to avoid cluttering the presentation.

These rules all apply both to plain functions and to methods. For methods, using the same receiver name avoids needless variation when listing all the methods of a type:

```go
$ go doc bytes.Buffer
package bytes // import "bytes"

type Buffer struct {
    // Has unexported fields.
}
    A Buffer is a variable-sized buffer of bytes with Read and Write methods.
    The zero value for Buffer is an empty buffer ready to use.

func NewBuffer(buf []byte) *Buffer
func NewBufferString(s string) *Buffer
func (b *Buffer) Bytes() []byte
func (b *Buffer) Cap() int
func (b *Buffer) Grow(n int)
func (b *Buffer) Len() int
func (b *Buffer) Next(n int) []byte
func (b *Buffer) Read(p []byte) (n int, err error)
func (b *Buffer) ReadByte() (byte, error)
...

```

This example also shows that top-level functions returning a type `T` or pointer `*T`, perhaps with an additional error result, are shown alongside the type `T` and its methods, under the assumption that they are `T`’s constructors.

By default, programmers can assume that a top-level function is safe to call from multiple goroutines; this fact need not be stated explicitly.

On the other hand, as noted in the previous section, using an instance of a type in any way, including calling a method, is typically assumed to be restricted to a single goroutine at a time. If the methods that are safe for concurrent use are not documented in the type’s doc comment, they should be documented in per-method comments. For example:

```go
package sql

// Close returns the connection to the connection pool.
// All operations after a Close will return with ErrConnDone.
// Close is safe to call concurrently with other operations and will
// block until all other operations finish. It may be useful to first
// cancel any used context and then call Close directly after.
func (c *Conn) Close() error {
    ...
}

```

Note that function and method doc comments focus on what the operation returns or does, detailing what the caller needs to know. Special cases can be particularly important to document. For example:

```go
package math

// Sqrt returns the square root of x.
//
// Special cases are:
//
//  Sqrt(+Inf) = +Inf
//  Sqrt(±0) = ±0
//  Sqrt(x < 0) = NaN
//  Sqrt(NaN) = NaN
func Sqrt(x float64) float64 {
    ...
}

```

Doc comments should not explain internal details such as the algorithm used in the current implementation. Those are best left to comments inside the function body. It may be appropriate to give asymptotic time or space bounds when that detail is particularly important to callers. For example:

```go
package sort

// Sort sorts data in ascending order as determined by the Less method.
// It makes one call to data.Len to determine n and O(n*log(n)) calls to
// data.Less and data.Swap. The sort is not guaranteed to be stable.
func Sort(data Interface) {
    ...
}

```

Because this doc comment makes no mention of which sorting algorithm is used, it is easier to change the implementation to use a different algorithm in the future.
