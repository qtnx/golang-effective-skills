---
source_name: "External Linked Documentation"
source_url: "https://pkg.go.dev/bytes"
source_path: "sources/raw/external/pkg-go-dev-bytes-42228f0497.html"
license_ref: ""
---

```go
func ToUpperSpecial(c unicode.SpecialCase, s []byte) []byte
```

ToUpperSpecial treats s as UTF-8-encoded bytes and returns a copy with all the Unicode letters mapped to their upper case, giving priority to the special casing rules.

```go

package main

import (
	"bytes"
	"fmt"
	"unicode"
)

func main() {
	str := []byte("ahoj vývojári golang")
	totitle := bytes.ToUpperSpecial(unicode.AzeriCase, str)
	fmt.Println("Original : " + string(str))
	fmt.Println("ToUpper : " + string(totitle))
}

```

```go
Output:
Original : ahoj vývojári golang
ToUpper : AHOJ VÝVOJÁRİ GOLANG

```

Share Format Run

```go
func ToValidUTF8(s, replacement []byte) []byte
```

ToValidUTF8 treats s as UTF-8-encoded bytes and returns a copy with each run of bytes representing invalid UTF-8 replaced with the bytes in replacement, which may be empty.

```go

package main

import (
	"bytes"
	"fmt"
)

func main() {
	fmt.Printf("%s\n", bytes.ToValidUTF8([]byte("abc"), []byte("\uFFFD")))
	fmt.Printf("%s\n", bytes.ToValidUTF8([]byte("a\xffb\xC0\xAFc\xff"), []byte("")))
	fmt.Printf("%s\n", bytes.ToValidUTF8([]byte("\xed\xa0\x80"), []byte("abc")))
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
func Trim(s []byte, cutset string) []byte
```

Trim returns a subslice of s by slicing off all leading and trailing UTF-8-encoded code points contained in cutset.

```go

package main

import (
	"bytes"
	"fmt"
)

func main() {
	fmt.Printf("[%q]", bytes.Trim([]byte(" !!! Achtung! Achtung! !!! "), "! "))
}

```

```go
Output:
["Achtung! Achtung"]

```

Share Format Run

```go
func TrimFunc(s []byte, f func(r rune) bool) []byte
```

TrimFunc returns a subslice of s by slicing off all leading and trailing UTF-8-encoded code points c that satisfy f(c).

```go

package main

import (
	"bytes"
	"fmt"
	"unicode"
)

func main() {
	fmt.Println(string(bytes.TrimFunc([]byte("go-gopher!"), unicode.IsLetter)))
	fmt.Println(string(bytes.TrimFunc([]byte("\"go-gopher!\""), unicode.IsLetter)))
	fmt.Println(string(bytes.TrimFunc([]byte("go-gopher!"), unicode.IsPunct)))
	fmt.Println(string(bytes.TrimFunc([]byte("1234go-gopher!567"), unicode.IsNumber)))
}

```

```go
Output:
-gopher!
"go-gopher!"
go-gopher
go-gopher!

```

Share Format Run

```go
func TrimLeft(s []byte, cutset string) []byte
```

TrimLeft returns a subslice of s by slicing off all leading UTF-8-encoded code points contained in cutset.

```go

package main

import (
	"bytes"
	"fmt"
)

func main() {
	fmt.Print(string(bytes.TrimLeft([]byte("453gopher8257"), "0123456789")))
}

```

```go
Output:
gopher8257

```

Share Format Run

```go
func TrimLeftFunc(s []byte, f func(r rune) bool) []byte
```

TrimLeftFunc treats s as UTF-8-encoded bytes and returns a subslice of s by slicing off all leading UTF-8-encoded code points c that satisfy f(c).

```go

package main

import (
	"bytes"
	"fmt"
	"unicode"
)

func main() {
	fmt.Println(string(bytes.TrimLeftFunc([]byte("go-gopher"), unicode.IsLetter)))
	fmt.Println(string(bytes.TrimLeftFunc([]byte("go-gopher!"), unicode.IsPunct)))
	fmt.Println(string(bytes.TrimLeftFunc([]byte("1234go-gopher!567"), unicode.IsNumber)))
}

```

```go
Output:
-gopher
go-gopher!
go-gopher!567

```

Share Format Run

```go
func TrimPrefix(s, prefix []byte) []byte
```

TrimPrefix returns s without the provided leading prefix string. If s doesn't start with prefix, s is returned unchanged.

```go

package main

import (
	"bytes"
	"fmt"
)

func main() {
	var b = []byte("Goodbye,, world!")
	b = bytes.TrimPrefix(b, []byte("Goodbye,"))
	b = bytes.TrimPrefix(b, []byte("See ya,"))
	fmt.Printf("Hello%s", b)
}

```

```go
Output:
Hello, world!

```

Share Format Run

```go
func TrimRight(s []byte, cutset string) []byte
```

TrimRight returns a subslice of s by slicing off all trailing UTF-8-encoded code points that are contained in cutset.

```go

package main

import (
	"bytes"
	"fmt"
)

func main() {
	fmt.Print(string(bytes.TrimRight([]byte("453gopher8257"), "0123456789")))
}

```

```go
Output:
453gopher

```

Share Format Run

```go
func TrimRightFunc(s []byte, f func(r rune) bool) []byte
```

TrimRightFunc returns a subslice of s by slicing off all trailing UTF-8-encoded code points c that satisfy f(c).

```go

package main

import (
	"bytes"
	"fmt"
	"unicode"
)

func main() {
	fmt.Println(string(bytes.TrimRightFunc([]byte("go-gopher"), unicode.IsLetter)))
	fmt.Println(string(bytes.TrimRightFunc([]byte("go-gopher!"), unicode.IsPunct)))
	fmt.Println(string(bytes.TrimRightFunc([]byte("1234go-gopher!567"), unicode.IsNumber)))
}

```

```go
Output:
go-
go-gopher
1234go-gopher!

```

Share Format Run

```go
func TrimSpace(s []byte) []byte
```

TrimSpace returns a subslice of s by slicing off all leading and trailing white space, as defined by Unicode.

```go

package main

import (
	"bytes"
	"fmt"
)

func main() {
	fmt.Printf("%s", bytes.TrimSpace([]byte(" \t\n a lone gopher \n\t\r\n")))
}

```

```go
Output:
a lone gopher

```

Share Format Run

```go
func TrimSuffix(s, suffix []byte) []byte
```

TrimSuffix returns s without the provided trailing suffix string. If s doesn't end with suffix, s is returned unchanged.

```go

package main

import (
	"bytes"
	"os"
)

func main() {
	var b = []byte("Hello, goodbye, etc!")
	b = bytes.TrimSuffix(b, []byte("goodbye, etc!"))
	b = bytes.TrimSuffix(b, []byte("gopher"))
	b = append(b, bytes.TrimSuffix([]byte("world!"), []byte("x!"))...)
	os.Stdout.Write(b)
}

```

```go
Output:
Hello, world!

```

Share Format Run

```go
type Buffer struct {
	// contains filtered or unexported fields
}
```

A Buffer is a variable-sized buffer of bytes with Buffer.Read and Buffer.Write methods. The zero value for Buffer is an empty buffer ready to use.

```go

package main

import (
	"bytes"
	"fmt"
	"os"
)

func main() {
	var b bytes.Buffer // A Buffer needs no initialization.
	b.Write([]byte("Hello "))
	fmt.Fprintf(&b, "world!")
	b.WriteTo(os.Stdout)
}

```

```go
Output:
Hello world!

```

Share Format Run

```go

package main

import (
	"bytes"
	"encoding/base64"
	"io"
	"os"
)

func main() {
	// A Buffer can turn a string or a []byte into an io.Reader.
	buf := bytes.NewBufferString("R29waGVycyBydWxlIQ==")
	dec := base64.NewDecoder(base64.StdEncoding, buf)
	io.Copy(os.Stdout, dec)
}

```

```go
Output:
Gophers rule!

```

Share Format Run

```go
func NewBuffer(buf []byte) *Buffer
```

NewBuffer creates and initializes a new Buffer using buf as its initial contents. The new Buffer takes ownership of buf, and the caller should not use buf after this call. NewBuffer is intended to prepare a Buffer to read existing data. It can also be used to set the initial size of the internal buffer for writing. To do that, buf should have the desired capacity but a length of zero.

In most cases, new(Buffer) (or just declaring a Buffer variable) is sufficient to initialize a Buffer.

```go
func NewBufferString(s string) *Buffer
```

NewBufferString creates and initializes a new Buffer using string s as its initial contents. It is intended to prepare a buffer to read an existing string.

In most cases, new(Buffer) (or just declaring a Buffer variable) is sufficient to initialize a Buffer.

```go
func (b *Buffer) Available() int
```

Available returns how many bytes are unused in the buffer.

```go
func (b *Buffer) AvailableBuffer() []byte
```

AvailableBuffer returns an empty buffer with b.Available() capacity. This buffer is intended to be appended to and passed to an immediately succeeding Buffer.Write call. The buffer is only valid until the next write operation on b.

```go

package main

import (
	"bytes"
	"os"
	"strconv"
)

func main() {
	var buf bytes.Buffer
	for i := 0; i < 4; i++ {
		b := buf.AvailableBuffer()
		b = strconv.AppendInt(b, int64(i), 10)
		b = append(b, ' ')
		buf.Write(b)
	}
	os.Stdout.Write(buf.Bytes())
}

```

```go
Output:
0 1 2 3

```

Share Format Run

```go
func (b *Buffer) Bytes() []byte
```

Bytes returns a slice of length b.Len() holding the unread portion of the buffer. The slice is valid for use only until the next buffer modification (that is, only until the next call to a method like Buffer.Read, Buffer.Write, Buffer.Reset, or Buffer.Truncate). The slice aliases the buffer content at least until the next buffer modification, so immediate changes to the slice will affect the result of future reads.

```go

package main

import (
	"bytes"
	"os"
)

func main() {
	buf := bytes.Buffer{}
	buf.Write([]byte{'h', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd'})
	os.Stdout.Write(buf.Bytes())
}

```

```go
Output:
hello world

```

Share Format Run

```go
func (b *Buffer) Cap() int
```

Cap returns the capacity of the buffer's underlying byte slice, that is, the total space allocated for the buffer's data.

```go

package main

import (
	"bytes"
	"fmt"
)

func main() {
	buf1 := bytes.NewBuffer(make([]byte, 10))
	buf2 := bytes.NewBuffer(make([]byte, 0, 10))
	fmt.Println(buf1.Cap())
	fmt.Println(buf2.Cap())
}

```

```go
Output:
10
10

```

Share Format Run

```go
func (b *Buffer) Grow(n int)
```

Grow grows the buffer's capacity, if necessary, to guarantee space for another n bytes. After Grow(n), at least n bytes can be written to the buffer without another allocation. If n is negative, Grow will panic. If the buffer can't grow it will panic with ErrTooLarge.

```go

package main

import (
	"bytes"
	"fmt"
)

func main() {
	var b bytes.Buffer
	b.Grow(64)
	bb := b.Bytes()
	b.Write([]byte("64 bytes or fewer"))
	fmt.Printf("%q", bb[:b.Len()])
}

```

```go
Output:
"64 bytes or fewer"

```

Share Format Run

```go
func (b *Buffer) Len() int
```

Len returns the number of bytes of the unread portion of the buffer; b.Len() == len(b.Bytes()).

```go

package main

import (
	"bytes"
	"fmt"
)

func main() {
	var b bytes.Buffer
	b.Grow(64)
	b.Write([]byte("abcde"))
	fmt.Printf("%d", b.Len())
}

```

```go
Output:
5

```

Share Format Run

```go
func (b *Buffer) Next(n int) []byte
```

Next returns a slice containing the next n bytes from the buffer, advancing the buffer as if the bytes had been returned by Buffer.Read. If there are fewer than n bytes in the buffer, Next returns the entire buffer. The slice is only valid until the next call to a read or write method.

```go

package main

import (
	"bytes"
	"fmt"
)

func main() {
	var b bytes.Buffer
	b.Grow(64)
	b.Write([]byte("abcde"))
	fmt.Printf("%s\n", b.Next(2))
	fmt.Printf("%s\n", b.Next(2))
	fmt.Printf("%s", b.Next(2))
}

```

```go
Output:
ab
cd
e

```

Share Format Run

```go
func (b *Buffer) Peek(n int) ([]byte, error)
```

Peek returns the next n bytes without advancing the buffer. If Peek returns fewer than n bytes, it also returns io.EOF. The slice is only valid until the next call to a read or write method. The slice aliases the buffer content at least until the next buffer modification, so immediate changes to the slice will affect the result of future reads.

```go
func (b *Buffer) Read(p []byte) (n int, err error)
```

Read reads the next len(p) bytes from the buffer or until the buffer is drained. The return value n is the number of bytes read. If the buffer has no data to return, err is io.EOF (unless len(p) is zero); otherwise it is nil.

```go

package main

import (
	"bytes"
	"fmt"
)
