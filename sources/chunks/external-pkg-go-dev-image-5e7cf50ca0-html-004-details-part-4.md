---
source_name: "External Linked Documentation"
source_url: "https://pkg.go.dev/image"
source_path: "sources/raw/external/pkg-go-dev-image-5e7cf50ca0.html"
license_ref: ""
---

PalettedImage is an image whose colors may come from a limited palette. If m is a PalettedImage and m.ColorModel() returns a color.Palette p, then m.At(x, y) should be equivalent to p[m.ColorIndexAt(x, y)]. If m's color model is not a color.Palette, then ColorIndexAt's behavior is undefined.

```go
type Point struct {
	X, Y int
}
```

A Point is an X, Y coordinate pair. The axes increase right and down.

```go
var ZP Point
```

ZP is the zero Point.

Deprecated: Use a literal image.Point instead.

```go
func Pt(X, Y int) Point
```

Pt is shorthand for Point{X, Y}.

```go
func (p Point) Add(q Point) Point
```

Add returns the vector p+q.

```go
func (p Point) Div(k int) Point
```

Div returns the vector p/k.

```go
func (p Point) Eq(q Point) bool
```

Eq reports whether p and q are equal.

```go
func (p Point) In(r Rectangle) bool
```

In reports whether p is in r.

```go
func (p Point) Mod(r Rectangle) Point
```

Mod returns the point q in r such that p.X-q.X is a multiple of r's width and p.Y-q.Y is a multiple of r's height.

```go
func (p Point) Mul(k int) Point
```

Mul returns the vector p*k.

```go
func (p Point) String() string
```

String returns a string representation of p like "(3,4)".

```go
func (p Point) Sub(q Point) Point
```

Sub returns the vector p-q.

```go
type RGBA struct {
	// Pix holds the image's pixels, in R, G, B, A order. The pixel at
	// (x, y) starts at Pix[(y-Rect.Min.Y)*Stride + (x-Rect.Min.X)*4].
	Pix []uint8
	// Stride is the Pix stride (in bytes) between vertically adjacent pixels.
	Stride int
	// Rect is the image's bounds.
	Rect Rectangle
}
```

RGBA is an in-memory image whose At method returns color.RGBA values.

```go
func NewRGBA(r Rectangle) *RGBA
```

NewRGBA returns a new RGBA image with the given bounds.

```go
func (p *RGBA) At(x, y int) color.Color
```

```go
func (p *RGBA) Bounds() Rectangle
```

```go
func (p *RGBA) ColorModel() color.Model
```

```go
func (p *RGBA) Opaque() bool
```

Opaque scans the entire image and reports whether it is fully opaque.

```go
func (p *RGBA) PixOffset(x, y int) int
```

PixOffset returns the index of the first element of Pix that corresponds to the pixel at (x, y).

```go
func (p *RGBA) RGBA64At(x, y int) color.RGBA64
```

```go
func (p *RGBA) RGBAAt(x, y int) color.RGBA
```

```go
func (p *RGBA) Set(x, y int, c color.Color)
```

```go
func (p *RGBA) SetRGBA(x, y int, c color.RGBA)
```

```go
func (p *RGBA) SetRGBA64(x, y int, c color.RGBA64)
```

```go
func (p *RGBA) SubImage(r Rectangle) Image
```

SubImage returns an image representing the portion of the image p visible through r. The returned value shares pixels with the original image.

```go
type RGBA64 struct {
	// Pix holds the image's pixels, in R, G, B, A order and big-endian format. The pixel at
	// (x, y) starts at Pix[(y-Rect.Min.Y)*Stride + (x-Rect.Min.X)*8].
	Pix []uint8
	// Stride is the Pix stride (in bytes) between vertically adjacent pixels.
	Stride int
	// Rect is the image's bounds.
	Rect Rectangle
}
```

RGBA64 is an in-memory image whose At method returns color.RGBA64 values.

```go
func NewRGBA64(r Rectangle) *RGBA64
```

NewRGBA64 returns a new RGBA64 image with the given bounds.

```go
func (p *RGBA64) At(x, y int) color.Color
```

```go
func (p *RGBA64) Bounds() Rectangle
```

```go
func (p *RGBA64) ColorModel() color.Model
```

```go
func (p *RGBA64) Opaque() bool
```

Opaque scans the entire image and reports whether it is fully opaque.

```go
func (p *RGBA64) PixOffset(x, y int) int
```

PixOffset returns the index of the first element of Pix that corresponds to the pixel at (x, y).

```go
func (p *RGBA64) RGBA64At(x, y int) color.RGBA64
```

```go
func (p *RGBA64) Set(x, y int, c color.Color)
```

```go
func (p *RGBA64) SetRGBA64(x, y int, c color.RGBA64)
```

```go
func (p *RGBA64) SubImage(r Rectangle) Image
```

SubImage returns an image representing the portion of the image p visible through r. The returned value shares pixels with the original image.

```go
type RGBA64Image interface {
	// RGBA64At returns the RGBA64 color of the pixel at (x, y). It is
	// equivalent to calling At(x, y).RGBA() and converting the resulting
	// 32-bit return values to a color.RGBA64, but it can avoid allocations
	// from converting concrete color types to the color.Color interface type.
	RGBA64At(x, y int) color.RGBA64
	Image
}
```

RGBA64Image is an Image whose pixels can be converted directly to a color.RGBA64.

```go
type Rectangle struct {
	Min, Max Point
}
```

A Rectangle contains the points with Min.X <= X < Max.X, Min.Y <= Y < Max.Y. It is well-formed if Min.X <= Max.X and likewise for Y. Points are always well-formed. A rectangle's methods always return well-formed outputs for well-formed inputs.

A Rectangle is also an Image whose bounds are the rectangle itself. At returns color.Opaque for points in the rectangle and color.Transparent otherwise.

```go
var ZR Rectangle
```

ZR is the zero Rectangle.

Deprecated: Use a literal image.Rectangle instead.

```go
func Rect(x0, y0, x1, y1 int) Rectangle
```

Rect is shorthand for Rectangle{Pt(x0, y0), Pt(x1, y1)}. The returned rectangle has minimum and maximum coordinates swapped if necessary so that it is well-formed.

```go
func (r Rectangle) Add(p Point) Rectangle
```

Add returns the rectangle r translated by p.

```go
func (r Rectangle) At(x, y int) color.Color
```

At implements the Image interface.

```go
func (r Rectangle) Bounds() Rectangle
```

Bounds implements the Image interface.

```go
func (r Rectangle) Canon() Rectangle
```

Canon returns the canonical version of r. The returned rectangle has minimum and maximum coordinates swapped if necessary so that it is well-formed.

```go
func (r Rectangle) ColorModel() color.Model
```

ColorModel implements the Image interface.

```go
func (r Rectangle) Dx() int
```

Dx returns r's width.

```go
func (r Rectangle) Dy() int
```

Dy returns r's height.

```go
func (r Rectangle) Empty() bool
```

Empty reports whether the rectangle contains no points.

```go
func (r Rectangle) Eq(s Rectangle) bool
```

Eq reports whether r and s contain the same set of points. All empty rectangles are considered equal.

```go
func (r Rectangle) In(s Rectangle) bool
```

In reports whether every point in r is in s.

```go
func (r Rectangle) Inset(n int) Rectangle
```

Inset returns the rectangle r inset by n, which may be negative. If either of r's dimensions is less than 2*n then an empty rectangle near the center of r will be returned.

```go
func (r Rectangle) Intersect(s Rectangle) Rectangle
```

Intersect returns the largest rectangle contained by both r and s. If the two rectangles do not overlap then the zero rectangle will be returned.

```go
func (r Rectangle) Overlaps(s Rectangle) bool
```

Overlaps reports whether r and s have a non-empty intersection.

```go
func (r Rectangle) RGBA64At(x, y int) color.RGBA64
```

RGBA64At implements the RGBA64Image interface.

```go
func (r Rectangle) Size() Point
```

Size returns r's width and height.

```go
func (r Rectangle) String() string
```

String returns a string representation of r like "(3,4)-(6,5)".

```go
func (r Rectangle) Sub(p Point) Rectangle
```

Sub returns the rectangle r translated by -p.

```go
func (r Rectangle) Union(s Rectangle) Rectangle
```

Union returns the smallest rectangle that contains both r and s.

```go
type Uniform struct {
	C color.Color
}
```

Uniform is an infinite-sized Image of uniform color. It implements the color.Color, color.Model, and Image interfaces.

```go
func NewUniform(c color.Color) *Uniform
```

NewUniform returns a new Uniform image of the given color.

```go
func (c *Uniform) At(x, y int) color.Color
```

```go
func (c *Uniform) Bounds() Rectangle
```

```go
func (c *Uniform) ColorModel() color.Model
```

```go
func (c *Uniform) Convert(color.Color) color.Color
```

```go
func (c *Uniform) Opaque() bool
```

Opaque scans the entire image and reports whether it is fully opaque.

```go
func (c *Uniform) RGBA() (r, g, b, a uint32)
```

```go
func (c *Uniform) RGBA64At(x, y int) color.RGBA64
```

```go
type YCbCr struct {
	Y, Cb, Cr      []uint8
	YStride        int
	CStride        int
	SubsampleRatio YCbCrSubsampleRatio
	Rect           Rectangle
}
```

YCbCr is an in-memory image of Y'CbCr colors. There is one Y sample per pixel, but each Cb and Cr sample can span one or more pixels. YStride is the Y slice index delta between vertically adjacent pixels. CStride is the Cb and Cr slice index delta between vertically adjacent pixels that map to separate chroma samples. It is not an absolute requirement, but YStride and len(Y) are typically multiples of 8, and:

```go
For 4:4:4, CStride == YStride/1 && len(Cb) == len(Cr) == len(Y)/1.
For 4:2:2, CStride == YStride/2 && len(Cb) == len(Cr) == len(Y)/2.
For 4:2:0, CStride == YStride/2 && len(Cb) == len(Cr) == len(Y)/4.
For 4:4:0, CStride == YStride/1 && len(Cb) == len(Cr) == len(Y)/2.
For 4:1:1, CStride == YStride/4 && len(Cb) == len(Cr) == len(Y)/4.
For 4:1:0, CStride == YStride/4 && len(Cb) == len(Cr) == len(Y)/8.

```

```go
func NewYCbCr(r Rectangle, subsampleRatio YCbCrSubsampleRatio) *YCbCr
```

NewYCbCr returns a new YCbCr image with the given bounds and subsample ratio.

```go
func (p *YCbCr) At(x, y int) color.Color
```

```go
func (p *YCbCr) Bounds() Rectangle
```

```go
func (p *YCbCr) COffset(x, y int) int
```

COffset returns the index of the first element of Cb or Cr that corresponds to the pixel at (x, y).

```go
func (p *YCbCr) ColorModel() color.Model
```

```go
func (p *YCbCr) Opaque() bool
```

```go
func (p *YCbCr) RGBA64At(x, y int) color.RGBA64
```

```go
func (p *YCbCr) SubImage(r Rectangle) Image
```

SubImage returns an image representing the portion of the image p visible through r. The returned value shares pixels with the original image.

```go
func (p *YCbCr) YCbCrAt(x, y int) color.YCbCr
```
