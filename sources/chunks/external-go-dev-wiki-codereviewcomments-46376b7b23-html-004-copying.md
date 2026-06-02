---
source_name: "External Linked Documentation"
source_url: "https://go.dev/wiki/CodeReviewComments"
source_path: "sources/raw/external/go-dev-wiki-codereviewcomments-46376b7b23.html"
license_ref: ""
---

# Go Wiki: Go Code Review Comments

## Copying

To avoid unexpected aliasing, be careful when copying a struct from another package. For example, the bytes.Buffer type contains a `[]byte` slice. If you copy a `Buffer`, the slice in the copy may alias the array in the original, causing subsequent method calls to have surprising effects.

In general, do not copy a value of type `T` if its methods are associated with the pointer type, `*T`.

# Go Wiki: Go Code Review Comments

## Crypto Rand

Do not use package `math/rand` <https://pkg.go.dev/math/rand> or `math/rand/v2` <https://pkg.go.dev/math/rand/v2> to generate keys, even throwaway ones. Seeded with `Time.Nanoseconds()` <https://pkg.go.dev/time#Time.Nanosecond>, there are just a few bits of entropy. Instead, use `crypto/rand.Reader` <https://pkg.go.dev/crypto/rand#pkg-variables>. If you need text, use `crypto/rand.Text` <https://pkg.go.dev/crypto/rand#Text>, or alternatively, encode random bytes with `encoding/hex` <https://pkg.go.dev/encoding/hex> or `encoding/base64` <https://pkg.go.dev/encoding/base64>.

```go
import (
    "crypto/rand"
    "fmt"
)

func Key() string {
  return rand.Text()
}

```
