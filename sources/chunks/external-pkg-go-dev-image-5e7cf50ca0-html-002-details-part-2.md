---
source_name: "External Linked Documentation"
source_url: "https://pkg.go.dev/image"
source_path: "sources/raw/external/pkg-go-dev-image-5e7cf50ca0.html"
license_ref: ""
---

-
-  func (p *NRGBA64) At(x, y int) color.Color
-  func (p *NRGBA64) Bounds() Rectangle
-  func (p *NRGBA64) ColorModel() color.Model
-  func (p *NRGBA64) NRGBA64At(x, y int) color.NRGBA64
-  func (p *NRGBA64) Opaque() bool
-  func (p *NRGBA64) PixOffset(x, y int) int
-  func (p *NRGBA64) RGBA64At(x, y int) color.RGBA64
-  func (p *NRGBA64) Set(x, y int, c color.Color)
-  func (p *NRGBA64) SetNRGBA64(x, y int, c color.NRGBA64)
-  func (p *NRGBA64) SetRGBA64(x, y int, c color.RGBA64)
-  func (p *NRGBA64) SubImage(r Rectangle) Image

-  type NYCbCrA
-
-  func NewNYCbCrA(r Rectangle, subsampleRatio YCbCrSubsampleRatio) *NYCbCrA

-
-  func (p *NYCbCrA) AOffset(x, y int) int
-  func (p *NYCbCrA) At(x, y int) color.Color
-  func (p *NYCbCrA) ColorModel() color.Model
-  func (p *NYCbCrA) NYCbCrAAt(x, y int) color.NYCbCrA
-  func (p *NYCbCrA) Opaque() bool
-  func (p *NYCbCrA) RGBA64At(x, y int) color.RGBA64
-  func (p *NYCbCrA) SubImage(r Rectangle) Image

-  type Paletted
-
-  func NewPaletted(r Rectangle, p color.Palette) *Paletted

-
-  func (p *Paletted) At(x, y int) color.Color
-  func (p *Paletted) Bounds() Rectangle
-  func (p *Paletted) ColorIndexAt(x, y int) uint8
-  func (p *Paletted) ColorModel() color.Model
-  func (p *Paletted) Opaque() bool
-  func (p *Paletted) PixOffset(x, y int) int
-  func (p *Paletted) RGBA64At(x, y int) color.RGBA64
-  func (p *Paletted) Set(x, y int, c color.Color)
-  func (p *Paletted) SetColorIndex(x, y int, index uint8)
-  func (p *Paletted) SetRGBA64(x, y int, c color.RGBA64)
-  func (p *Paletted) SubImage(r Rectangle) Image

-  type PalettedImage
-  type Point
-
-  func Pt(X, Y int) Point

-
-  func (p Point) Add(q Point) Point
-  func (p Point) Div(k int) Point
-  func (p Point) Eq(q Point) bool
-  func (p Point) In(r Rectangle) bool
-  func (p Point) Mod(r Rectangle) Point
-  func (p Point) Mul(k int) Point
-  func (p Point) String() string
-  func (p Point) Sub(q Point) Point

-  type RGBA
-
-  func NewRGBA(r Rectangle) *RGBA

-
-  func (p *RGBA) At(x, y int) color.Color
-  func (p *RGBA) Bounds() Rectangle
-  func (p *RGBA) ColorModel() color.Model
-  func (p *RGBA) Opaque() bool
-  func (p *RGBA) PixOffset(x, y int) int
-  func (p *RGBA) RGBA64At(x, y int) color.RGBA64
-  func (p *RGBA) RGBAAt(x, y int) color.RGBA
-  func (p *RGBA) Set(x, y int, c color.Color)
-  func (p *RGBA) SetRGBA(x, y int, c color.RGBA)
-  func (p *RGBA) SetRGBA64(x, y int, c color.RGBA64)
-  func (p *RGBA) SubImage(r Rectangle) Image

-  type RGBA64
-
-  func NewRGBA64(r Rectangle) *RGBA64

-
-  func (p *RGBA64) At(x, y int) color.Color
-  func (p *RGBA64) Bounds() Rectangle
-  func (p *RGBA64) ColorModel() color.Model
-  func (p *RGBA64) Opaque() bool
-  func (p *RGBA64) PixOffset(x, y int) int
-  func (p *RGBA64) RGBA64At(x, y int) color.RGBA64
-  func (p *RGBA64) Set(x, y int, c color.Color)
-  func (p *RGBA64) SetRGBA64(x, y int, c color.RGBA64)
-  func (p *RGBA64) SubImage(r Rectangle) Image

-  type RGBA64Image
-  type Rectangle
-
-  func Rect(x0, y0, x1, y1 int) Rectangle

-
-  func (r Rectangle) Add(p Point) Rectangle
-  func (r Rectangle) At(x, y int) color.Color
-  func (r Rectangle) Bounds() Rectangle
-  func (r Rectangle) Canon() Rectangle
-  func (r Rectangle) ColorModel() color.Model
-  func (r Rectangle) Dx() int
-  func (r Rectangle) Dy() int
-  func (r Rectangle) Empty() bool
-  func (r Rectangle) Eq(s Rectangle) bool
-  func (r Rectangle) In(s Rectangle) bool
-  func (r Rectangle) Inset(n int) Rectangle
-  func (r Rectangle) Intersect(s Rectangle) Rectangle
-  func (r Rectangle) Overlaps(s Rectangle) bool
-  func (r Rectangle) RGBA64At(x, y int) color.RGBA64
-  func (r Rectangle) Size() Point
-  func (r Rectangle) String() string
-  func (r Rectangle) Sub(p Point) Rectangle
-  func (r Rectangle) Union(s Rectangle) Rectangle

-  type Uniform
-
-  func NewUniform(c color.Color) *Uniform

-
-  func (c *Uniform) At(x, y int) color.Color
-  func (c *Uniform) Bounds() Rectangle
-  func (c *Uniform) ColorModel() color.Model
-  func (c *Uniform) Convert(color.Color) color.Color
-  func (c *Uniform) Opaque() bool
-  func (c *Uniform) RGBA() (r, g, b, a uint32)
-  func (c *Uniform) RGBA64At(x, y int) color.RGBA64

-  type YCbCr
-
-  func NewYCbCr(r Rectangle, subsampleRatio YCbCrSubsampleRatio) *YCbCr

-
-  func (p *YCbCr) At(x, y int) color.Color
-  func (p *YCbCr) Bounds() Rectangle
-  func (p *YCbCr) COffset(x, y int) int
-  func (p *YCbCr) ColorModel() color.Model
-  func (p *YCbCr) Opaque() bool
-  func (p *YCbCr) RGBA64At(x, y int) color.RGBA64
-  func (p *YCbCr) SubImage(r Rectangle) Image
-  func (p *YCbCr) YCbCrAt(x, y int) color.YCbCr
-  func (p *YCbCr) YOffset(x, y int) int

-  type YCbCrSubsampleRatio
-
-  func (s YCbCrSubsampleRatio) String() string

- Package
- Package (DecodeConfig)

This section is empty.

View Source <https://cs.opensource.google/go/go/+/go1.26.3:src/image/names.go;l=11>
```go
var (
	// Black is an opaque black uniform image.
	Black = NewUniform(color.Black)
	// White is an opaque white uniform image.
	White = NewUniform(color.White)
	// Transparent is a fully transparent uniform image.
	Transparent = NewUniform(color.Transparent)
	// Opaque is a fully opaque uniform image.
	Opaque = NewUniform(color.Opaque)
)
```

View Source <https://cs.opensource.google/go/go/+/go1.26.3:src/image/format.go;l=16>
```go
var ErrFormat = errors.New("image: unknown format")
```

ErrFormat indicates that decoding encountered an unknown format.

```go
func RegisterFormat(name, magic string, decode func(io.Reader) (Image, error), decodeConfig func(io.Reader) (Config, error))
```

RegisterFormat registers an image format for use by Decode. Name is the name of the format, like "jpeg" or "png". Magic is the magic prefix that identifies the format's encoding. The magic string can contain "?" wildcards that each match any one byte. Decode is the function that decodes the encoded image. DecodeConfig is the function that decodes just its configuration.

```go
type Alpha struct {
	// Pix holds the image's pixels, as alpha values. The pixel at
	// (x, y) starts at Pix[(y-Rect.Min.Y)*Stride + (x-Rect.Min.X)*1].
	Pix []uint8
	// Stride is the Pix stride (in bytes) between vertically adjacent pixels.
	Stride int
	// Rect is the image's bounds.
	Rect Rectangle
}
```

Alpha is an in-memory image whose At method returns color.Alpha values.

```go
func NewAlpha(r Rectangle) *Alpha
```

NewAlpha returns a new Alpha image with the given bounds.

```go
func (p *Alpha) AlphaAt(x, y int) color.Alpha
```

```go
func (p *Alpha) At(x, y int) color.Color
```

```go
func (p *Alpha) Bounds() Rectangle
```

```go
func (p *Alpha) ColorModel() color.Model
```

```go
func (p *Alpha) Opaque() bool
```

Opaque scans the entire image and reports whether it is fully opaque.

```go
func (p *Alpha) PixOffset(x, y int) int
```

PixOffset returns the index of the first element of Pix that corresponds to the pixel at (x, y).

```go
func (p *Alpha) RGBA64At(x, y int) color.RGBA64
```

```go
func (p *Alpha) Set(x, y int, c color.Color)
```

```go
func (p *Alpha) SetAlpha(x, y int, c color.Alpha)
```

```go
func (p *Alpha) SetRGBA64(x, y int, c color.RGBA64)
```

```go
func (p *Alpha) SubImage(r Rectangle) Image
```

SubImage returns an image representing the portion of the image p visible through r. The returned value shares pixels with the original image.

```go
type Alpha16 struct {
	// Pix holds the image's pixels, as alpha values in big-endian format. The pixel at
	// (x, y) starts at Pix[(y-Rect.Min.Y)*Stride + (x-Rect.Min.X)*2].
	Pix []uint8
	// Stride is the Pix stride (in bytes) between vertically adjacent pixels.
	Stride int
	// Rect is the image's bounds.
	Rect Rectangle
}
```

Alpha16 is an in-memory image whose At method returns color.Alpha16 values.

```go
func NewAlpha16(r Rectangle) *Alpha16
```

NewAlpha16 returns a new Alpha16 image with the given bounds.

```go
func (p *Alpha16) Alpha16At(x, y int) color.Alpha16
```

```go
func (p *Alpha16) At(x, y int) color.Color
```

```go
func (p *Alpha16) Bounds() Rectangle
```

```go
func (p *Alpha16) ColorModel() color.Model
```

```go
func (p *Alpha16) Opaque() bool
```

Opaque scans the entire image and reports whether it is fully opaque.

```go
func (p *Alpha16) PixOffset(x, y int) int
```

PixOffset returns the index of the first element of Pix that corresponds to the pixel at (x, y).

```go
func (p *Alpha16) RGBA64At(x, y int) color.RGBA64
```

```go
func (p *Alpha16) Set(x, y int, c color.Color)
```

```go
func (p *Alpha16) SetAlpha16(x, y int, c color.Alpha16)
```

```go
func (p *Alpha16) SetRGBA64(x, y int, c color.RGBA64)
```

```go
func (p *Alpha16) SubImage(r Rectangle) Image
```

SubImage returns an image representing the portion of the image p visible through r. The returned value shares pixels with the original image.

```go
type CMYK struct {
	// Pix holds the image's pixels, in C, M, Y, K order. The pixel at
	// (x, y) starts at Pix[(y-Rect.Min.Y)*Stride + (x-Rect.Min.X)*4].
	Pix []uint8
	// Stride is the Pix stride (in bytes) between vertically adjacent pixels.
	Stride int
	// Rect is the image's bounds.
	Rect Rectangle
}
```

CMYK is an in-memory image whose At method returns color.CMYK values.

```go
func NewCMYK(r Rectangle) *CMYK
```

NewCMYK returns a new CMYK image with the given bounds.

```go
func (p *CMYK) At(x, y int) color.Color
```

```go
func (p *CMYK) Bounds() Rectangle
```

```go
func (p *CMYK) CMYKAt(x, y int) color.CMYK
```

```go
func (p *CMYK) ColorModel() color.Model
```

```go
func (p *CMYK) Opaque() bool
```

Opaque scans the entire image and reports whether it is fully opaque.

```go
func (p *CMYK) PixOffset(x, y int) int
```

PixOffset returns the index of the first element of Pix that corresponds to the pixel at (x, y).

```go
func (p *CMYK) RGBA64At(x, y int) color.RGBA64
```

```go
func (p *CMYK) Set(x, y int, c color.Color)
```

```go
func (p *CMYK) SetCMYK(x, y int, c color.CMYK)
```

```go
func (p *CMYK) SetRGBA64(x, y int, c color.RGBA64)
```

```go
func (p *CMYK) SubImage(r Rectangle) Image
```
