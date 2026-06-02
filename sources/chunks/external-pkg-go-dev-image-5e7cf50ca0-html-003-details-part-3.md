---
source_name: "External Linked Documentation"
source_url: "https://pkg.go.dev/image"
source_path: "sources/raw/external/pkg-go-dev-image-5e7cf50ca0.html"
license_ref: ""
---

SubImage returns an image representing the portion of the image p visible through r. The returned value shares pixels with the original image.

```go
type Config struct {
	ColorModel    color.Model
	Width, Height int
}
```

Config holds an image's color model and dimensions.

```go
func DecodeConfig(r io.Reader) (Config, string, error)
```

DecodeConfig decodes the color model and dimensions of an image that has been encoded in a registered format. The string returned is the format name used during format registration. Format registration is typically done by an init function in the codec-specific package.

```go
type Gray struct {
	// Pix holds the image's pixels, as gray values. The pixel at
	// (x, y) starts at Pix[(y-Rect.Min.Y)*Stride + (x-Rect.Min.X)*1].
	Pix []uint8
	// Stride is the Pix stride (in bytes) between vertically adjacent pixels.
	Stride int
	// Rect is the image's bounds.
	Rect Rectangle
}
```

Gray is an in-memory image whose At method returns color.Gray values.

```go
func NewGray(r Rectangle) *Gray
```

NewGray returns a new Gray image with the given bounds.

```go
func (p *Gray) At(x, y int) color.Color
```

```go
func (p *Gray) Bounds() Rectangle
```

```go
func (p *Gray) ColorModel() color.Model
```

```go
func (p *Gray) GrayAt(x, y int) color.Gray
```

```go
func (p *Gray) Opaque() bool
```

Opaque scans the entire image and reports whether it is fully opaque.

```go
func (p *Gray) PixOffset(x, y int) int
```

PixOffset returns the index of the first element of Pix that corresponds to the pixel at (x, y).

```go
func (p *Gray) RGBA64At(x, y int) color.RGBA64
```

```go
func (p *Gray) Set(x, y int, c color.Color)
```

```go
func (p *Gray) SetGray(x, y int, c color.Gray)
```

```go
func (p *Gray) SetRGBA64(x, y int, c color.RGBA64)
```

```go
func (p *Gray) SubImage(r Rectangle) Image
```

SubImage returns an image representing the portion of the image p visible through r. The returned value shares pixels with the original image.

```go
type Gray16 struct {
	// Pix holds the image's pixels, as gray values in big-endian format. The pixel at
	// (x, y) starts at Pix[(y-Rect.Min.Y)*Stride + (x-Rect.Min.X)*2].
	Pix []uint8
	// Stride is the Pix stride (in bytes) between vertically adjacent pixels.
	Stride int
	// Rect is the image's bounds.
	Rect Rectangle
}
```

Gray16 is an in-memory image whose At method returns color.Gray16 values.

```go
func NewGray16(r Rectangle) *Gray16
```

NewGray16 returns a new Gray16 image with the given bounds.

```go
func (p *Gray16) At(x, y int) color.Color
```

```go
func (p *Gray16) Bounds() Rectangle
```

```go
func (p *Gray16) ColorModel() color.Model
```

```go
func (p *Gray16) Gray16At(x, y int) color.Gray16
```

```go
func (p *Gray16) Opaque() bool
```

Opaque scans the entire image and reports whether it is fully opaque.

```go
func (p *Gray16) PixOffset(x, y int) int
```

PixOffset returns the index of the first element of Pix that corresponds to the pixel at (x, y).

```go
func (p *Gray16) RGBA64At(x, y int) color.RGBA64
```

```go
func (p *Gray16) Set(x, y int, c color.Color)
```

```go
func (p *Gray16) SetGray16(x, y int, c color.Gray16)
```

```go
func (p *Gray16) SetRGBA64(x, y int, c color.RGBA64)
```

```go
func (p *Gray16) SubImage(r Rectangle) Image
```

SubImage returns an image representing the portion of the image p visible through r. The returned value shares pixels with the original image.

```go
type Image interface {
	// ColorModel returns the Image's color model.
	ColorModel() color.Model
	// Bounds returns the domain for which At can return non-zero color.
	// The bounds do not necessarily contain the point (0, 0).
	Bounds() Rectangle
	// At returns the color of the pixel at (x, y).
	// At(Bounds().Min.X, Bounds().Min.Y) returns the upper-left pixel of the grid.
	// At(Bounds().Max.X-1, Bounds().Max.Y-1) returns the lower-right one.
	At(x, y int) color.Color
}
```

Image is a finite rectangular grid of color.Color values taken from a color model.

```go
func Decode(r io.Reader) (Image, string, error)
```

Decode decodes an image that has been encoded in a registered format. The string returned is the format name used during format registration. Format registration is typically done by an init function in the codec- specific package.

```go
type NRGBA struct {
	// Pix holds the image's pixels, in R, G, B, A order. The pixel at
	// (x, y) starts at Pix[(y-Rect.Min.Y)*Stride + (x-Rect.Min.X)*4].
	Pix []uint8
	// Stride is the Pix stride (in bytes) between vertically adjacent pixels.
	Stride int
	// Rect is the image's bounds.
	Rect Rectangle
}
```

NRGBA is an in-memory image whose At method returns color.NRGBA values.

```go
func NewNRGBA(r Rectangle) *NRGBA
```

NewNRGBA returns a new NRGBA image with the given bounds.

```go
func (p *NRGBA) At(x, y int) color.Color
```

```go
func (p *NRGBA) Bounds() Rectangle
```

```go
func (p *NRGBA) ColorModel() color.Model
```

```go
func (p *NRGBA) NRGBAAt(x, y int) color.NRGBA
```

```go
func (p *NRGBA) Opaque() bool
```

Opaque scans the entire image and reports whether it is fully opaque.

```go
func (p *NRGBA) PixOffset(x, y int) int
```

PixOffset returns the index of the first element of Pix that corresponds to the pixel at (x, y).

```go
func (p *NRGBA) RGBA64At(x, y int) color.RGBA64
```

```go
func (p *NRGBA) Set(x, y int, c color.Color)
```

```go
func (p *NRGBA) SetNRGBA(x, y int, c color.NRGBA)
```

```go
func (p *NRGBA) SetRGBA64(x, y int, c color.RGBA64)
```

```go
func (p *NRGBA) SubImage(r Rectangle) Image
```

SubImage returns an image representing the portion of the image p visible through r. The returned value shares pixels with the original image.

```go
type NRGBA64 struct {
	// Pix holds the image's pixels, in R, G, B, A order and big-endian format. The pixel at
	// (x, y) starts at Pix[(y-Rect.Min.Y)*Stride + (x-Rect.Min.X)*8].
	Pix []uint8
	// Stride is the Pix stride (in bytes) between vertically adjacent pixels.
	Stride int
	// Rect is the image's bounds.
	Rect Rectangle
}
```

NRGBA64 is an in-memory image whose At method returns color.NRGBA64 values.

```go
func NewNRGBA64(r Rectangle) *NRGBA64
```

NewNRGBA64 returns a new NRGBA64 image with the given bounds.

```go
func (p *NRGBA64) At(x, y int) color.Color
```

```go
func (p *NRGBA64) Bounds() Rectangle
```

```go
func (p *NRGBA64) ColorModel() color.Model
```

```go
func (p *NRGBA64) NRGBA64At(x, y int) color.NRGBA64
```

```go
func (p *NRGBA64) Opaque() bool
```

Opaque scans the entire image and reports whether it is fully opaque.

```go
func (p *NRGBA64) PixOffset(x, y int) int
```

PixOffset returns the index of the first element of Pix that corresponds to the pixel at (x, y).

```go
func (p *NRGBA64) RGBA64At(x, y int) color.RGBA64
```

```go
func (p *NRGBA64) Set(x, y int, c color.Color)
```

```go
func (p *NRGBA64) SetNRGBA64(x, y int, c color.NRGBA64)
```

```go
func (p *NRGBA64) SetRGBA64(x, y int, c color.RGBA64)
```

```go
func (p *NRGBA64) SubImage(r Rectangle) Image
```

SubImage returns an image representing the portion of the image p visible through r. The returned value shares pixels with the original image.

```go
type NYCbCrA struct {
	YCbCr
	A       []uint8
	AStride int
}
```

NYCbCrA is an in-memory image of non-alpha-premultiplied Y'CbCr-with-alpha colors. A and AStride are analogous to the Y and YStride fields of the embedded YCbCr.

```go
func NewNYCbCrA(r Rectangle, subsampleRatio YCbCrSubsampleRatio) *NYCbCrA
```

NewNYCbCrA returns a new NYCbCrA image with the given bounds and subsample ratio.

```go
func (p *NYCbCrA) AOffset(x, y int) int
```

AOffset returns the index of the first element of A that corresponds to the pixel at (x, y).

```go
func (p *NYCbCrA) At(x, y int) color.Color
```

```go
func (p *NYCbCrA) ColorModel() color.Model
```

```go
func (p *NYCbCrA) NYCbCrAAt(x, y int) color.NYCbCrA
```

```go
func (p *NYCbCrA) Opaque() bool
```

Opaque scans the entire image and reports whether it is fully opaque.

```go
func (p *NYCbCrA) RGBA64At(x, y int) color.RGBA64
```

```go
func (p *NYCbCrA) SubImage(r Rectangle) Image
```

SubImage returns an image representing the portion of the image p visible through r. The returned value shares pixels with the original image.

```go
type Paletted struct {
	// Pix holds the image's pixels, as palette indices. The pixel at
	// (x, y) starts at Pix[(y-Rect.Min.Y)*Stride + (x-Rect.Min.X)*1].
	Pix []uint8
	// Stride is the Pix stride (in bytes) between vertically adjacent pixels.
	Stride int
	// Rect is the image's bounds.
	Rect Rectangle
	// Palette is the image's palette.
	Palette color.Palette
}
```

Paletted is an in-memory image of uint8 indices into a given palette.

```go
func NewPaletted(r Rectangle, p color.Palette) *Paletted
```

NewPaletted returns a new Paletted image with the given width, height and palette.

```go
func (p *Paletted) At(x, y int) color.Color
```

```go
func (p *Paletted) Bounds() Rectangle
```

```go
func (p *Paletted) ColorIndexAt(x, y int) uint8
```

```go
func (p *Paletted) ColorModel() color.Model
```

```go
func (p *Paletted) Opaque() bool
```

Opaque scans the entire image and reports whether it is fully opaque.

```go
func (p *Paletted) PixOffset(x, y int) int
```

PixOffset returns the index of the first element of Pix that corresponds to the pixel at (x, y).

```go
func (p *Paletted) RGBA64At(x, y int) color.RGBA64
```

```go
func (p *Paletted) Set(x, y int, c color.Color)
```

```go
func (p *Paletted) SetColorIndex(x, y int, index uint8)
```

```go
func (p *Paletted) SetRGBA64(x, y int, c color.RGBA64)
```

```go
func (p *Paletted) SubImage(r Rectangle) Image
```

SubImage returns an image representing the portion of the image p visible through r. The returned value shares pixels with the original image.

```go
type PalettedImage interface {
	// ColorIndexAt returns the palette index of the pixel at (x, y).
	ColorIndexAt(x, y int) uint8
	Image
}
```
