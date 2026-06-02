---
source_name: "Effective Go"
source_url: "https://go.dev/doc/effective_go"
source_path: "sources/raw/effective-go/effective_go.html"
license_ref: "sources/licenses/go-LICENSE.txt"
---

## Interfaces and other types

### Generality

 If a type exists only to implement an interface and will never have exported methods beyond that interface, there is no need to export the type itself. Exporting just the interface makes it clear the value has no interesting behavior beyond what is described in the interface. It also avoids the need to repeat the documentation on every instance of a common method.

 In such cases, the constructor should return an interface value rather than the implementing type. As an example, in the hash libraries both `crc32.NewIEEE` and `adler32.New` return the interface type `hash.Hash32`. Substituting the CRC-32 algorithm for Adler-32 in a Go program requires only changing the constructor call; the rest of the code is unaffected by the change of algorithm.

 A similar approach allows the streaming cipher algorithms in the various `crypto` packages to be separated from the block ciphers they chain together. The `Block` interface in the `crypto/cipher` package specifies the behavior of a block cipher, which provides encryption of a single block of data. Then, by analogy with the `bufio` package, cipher packages that implement this interface can be used to construct streaming ciphers, represented by the `Stream` interface, without knowing the details of the block encryption.

 The `crypto/cipher` interfaces look like this:

```go

type Block interface {
    BlockSize() int
    Encrypt(dst, src []byte)
    Decrypt(dst, src []byte)
}

type Stream interface {
    XORKeyStream(dst, src []byte)
}

```

 Here's the definition of the counter mode (CTR) stream, which turns a block cipher into a streaming cipher; notice that the block cipher's details are abstracted away:

```go

// NewCTR returns a Stream that encrypts/decrypts using the given Block in
// counter mode. The length of iv must be the same as the Block's block size.
func NewCTR(block Block, iv []byte) Stream

```

 `NewCTR` applies not just to one specific encryption algorithm and data source but to any implementation of the `Block` interface and any `Stream`. Because they return interface values, replacing CTR encryption with other encryption modes is a localized change. The constructor calls must be edited, but because the surrounding code must treat the result only as a `Stream`, it won't notice the difference.
