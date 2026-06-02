---
source_name: "External Linked Documentation"
source_url: "https://pkg.go.dev/image/jpeg"
source_path: "sources/raw/external/pkg-go-dev-image-jpeg-5abe70d7d6.html"
license_ref: ""
---

jpeg package - image/jpeg - Go Packages
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

Package jpeg implements a JPEG image decoder and encoder.

JPEG is defined in ITU-T T.81: https://www.w3.org/Graphics/JPEG/itu-t81.pdf <https://www.w3.org/Graphics/JPEG/itu-t81.pdf>.

- Constants
-  func Decode(r io.Reader) (image.Image, error)
-  func DecodeConfig(r io.Reader) (image.Config, error)
-  func Encode(w io.Writer, m image.Image, o *Options) error
-  type FormatError
-
-  func (e FormatError) Error() string

-  type Options
-  type Readerdeprecated
-  type UnsupportedError
-
-  func (e UnsupportedError) Error() string

   View Source <https://cs.opensource.google/go/go/+/go1.26.3:src/image/jpeg/writer.go;l=565>
```go
const DefaultQuality = 75
```

DefaultQuality is the default quality encoding parameter.

This section is empty.

```go
func Decode(r io.Reader) (image.Image, error)
```

Decode reads a JPEG image from r and returns it as an image.Image.

```go
func DecodeConfig(r io.Reader) (image.Config, error)
```

DecodeConfig returns the color model and dimensions of a JPEG image without decoding the entire image.

```go
func Encode(w io.Writer, m image.Image, o *Options) error
```

Encode writes the Image m to w in JPEG 4:2:0 baseline format with the given options. Default parameters are used if a nil *Options is passed.

```go
type FormatError string
```

A FormatError reports that the input is not a valid JPEG.

```go
func (e FormatError) Error() string
```

```go
type Options struct {
	Quality int
}
```

Options are the encoding parameters. Quality ranges from 1 to 100 inclusive, higher is better.

```go
type Reader interface {
	io.ByteReader
	io.Reader
}
```

Deprecated: Reader is not used by the image/jpeg package and should not be used by others. It is kept for compatibility.

```go
type UnsupportedError string
```

An UnsupportedError reports that the input uses a valid but unimplemented JPEG feature.

```go
func (e UnsupportedError) Error() string
```

##   Source Files ¶
 View all Source files <https://cs.opensource.google/go/go/+/go1.26.3:src/image/jpeg>

- dct.go <https://cs.opensource.google/go/go/+/go1.26.3:src/image/jpeg/dct.go>
- huffman.go <https://cs.opensource.google/go/go/+/go1.26.3:src/image/jpeg/huffman.go>
- reader.go <https://cs.opensource.google/go/go/+/go1.26.3:src/image/jpeg/reader.go>
- scan.go <https://cs.opensource.google/go/go/+/go1.26.3:src/image/jpeg/scan.go>
- writer.go <https://cs.opensource.google/go/go/+/go1.26.3:src/image/jpeg/writer.go>

  Click to show internal directories.
  Click to hide internal directories.

  Close

     **?** : This menu   **/** : Search site   **f** or **F** : Jump to   **y** or **Y**  : Canonical URL
  Close
