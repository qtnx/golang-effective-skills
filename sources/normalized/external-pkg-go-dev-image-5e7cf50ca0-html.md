image package - image - Go Packages

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

## Links

-    Report a Vulnerability  <https://go.dev/security/policy>

##   Documentation ¶

Package image implements a basic 2-D image library.

The fundamental interface is called Image. An Image contains colors, which are described in the image/color package.

Values of the Image interface are created either by calling functions such as NewRGBA and NewPaletted, or by calling Decode on an io.Reader containing image data in a format such as GIF, JPEG or PNG. Decoding any particular image format requires the prior registration of a decoder function. Registration is typically automatic as a side effect of initializing that format's package so that, to decode a PNG image, it suffices to have

```go
import _ "image/png"

```

in a program's main package. The _ means to import a package purely for its initialization side effects.

See "The Go image package" for more details: https://golang.org/doc/articles/image_package.html <https://golang.org/doc/articles/image_package.html>

#### Security Considerations ¶

The image package can be used to parse arbitrarily large images, which can cause resource exhaustion on machines which do not have enough memory to store them. When operating on arbitrary images, DecodeConfig should be called before Decode, so that the program can decide whether the image, as defined in the returned header, can be safely decoded with the available resources. A call to Decode which produces an extremely large image, as defined in the header returned by DecodeConfig, is not considered a security issue, regardless of whether the image is itself malformed or not. A call to DecodeConfig which returns a header which does not match the image returned by Decode may be considered a security issue, and should be reported per the Go Security Policy <https://go.dev/security/policy>.

```go

package main

import (
	"encoding/base64"
	"fmt"
	"image"
	"log"
	"strings"

	// Package image/jpeg is not used explicitly in the code below,
	// but is imported for its initialization side-effect, which allows
	// image.Decode to understand JPEG formatted images. Uncomment these
	// two lines to also understand GIF and PNG images:
	// _ "image/gif"
	// _ "image/png"
	_ "image/jpeg"
)

func main() {
	// Decode the JPEG data. If reading from file, create a reader with
	//
	// reader, err := os.Open("testdata/video-001.q50.420.jpeg")
	// if err != nil {
	//     log.Fatal(err)
	// }
	// defer reader.Close()
	reader := base64.NewDecoder(base64.StdEncoding, strings.NewReader(data))
	m, _, err := image.Decode(reader)
	if err != nil {
		log.Fatal(err)
	}
	bounds := m.Bounds()

	// Calculate a 16-bin histogram for m's red, green, blue and alpha components.
	//
	// An image's bounds do not necessarily start at (0, 0), so the two loops start
	// at bounds.Min.Y and bounds.Min.X. Looping over Y first and X second is more
	// likely to result in better memory access patterns than X first and Y second.
	var histogram [16][4]int
	for y := bounds.Min.Y; y < bounds.Max.Y; y++ {
		for x := bounds.Min.X; x < bounds.Max.X; x++ {
			r, g, b, a := m.At(x, y).RGBA()
			// A color's RGBA method returns values in the range [0, 65535].
			// Shifting by 12 reduces this to the range [0, 15].
			histogram[r>>12][0]++
			histogram[g>>12][1]++
			histogram[b>>12][2]++
			histogram[a>>12][3]++
		}
	}

	// Print the results.
	fmt.Printf("%-14s %6s %6s %6s %6s\n", "bin", "red", "green", "blue", "alpha")
	for i, x := range histogram {
		fmt.Printf("0x%04x-0x%04x: %6d %6d %6d %6d\n", i<<12, (i+1)<<12-1, x[0], x[1], x[2], x[3])
	}
}

const data = `
/9j/4AAQSkZJRgABAQIAHAAcAAD/2wBDABALDA4MChAODQ4SERATGCgaGBYWGDEjJR0oOjM9PDkzODdA
SFxOQERXRTc4UG1RV19iZ2hnPk1xeXBkeFxlZ2P/2wBDARESEhgVGC8aGi9jQjhCY2NjY2NjY2NjY2Nj
Y2NjY2NjY2NjY2NjY2NjY2NjY2NjY2NjY2NjY2NjY2NjY2NjY2P/wAARCABnAJYDASIAAhEBAxEB/8QA
HwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIh
MUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVW
V1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXG
x8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQF
BgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAV
YnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOE
hYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq
8vP09fb3+Pn6/9oADAMBAAIRAxEAPwDlwKMD0pwzSiuK57QzGDxS7D6in8Y5ximnAPUfSlcq4m3ilUYp
2OKXHvRcVxnTtS7c07HNFK4DQPakC4PNOA+tOx70XAjK/So5gBGP94fzqfvUVx/qxx/EP51UXqRP4WSE
cmgjilP3jSEZqS0IO/NGDnpUiocDg/McDjvV6HTPOdVWYgsM5KcfzzQ2JySM2jp6VYu7SWzmMUwG4cgj
kMPUVBjjtTGtRu0Zopw+lFFxhinrGzuqqMsxAA9yaXFSRv5cqSEcIwYj6GpuZ30O30fSLKzhUpbpNMv3
5XGTn29BV28jt7pPLuIVljPBBFVreYx+VbqAjycgt3x14zRcNOxGyVFHQkIc/wA61exyKLbuzjdZ046d
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
`

```

```go
Output:
bin               red  green   blue  alpha
0x0000-0x0fff:    362    793   7245      0
0x1000-0x1fff:    648   2963   1036      0
0x2000-0x2fff:   1072   2301    977      0
0x3000-0x3fff:    819   2266    982      0
0x4000-0x4fff:    537   1303    541      0
0x5000-0x5fff:    321    964    261      0
0x6000-0x6fff:    321    375    177      0
0x7000-0x7fff:    599    278    213      0
0x8000-0x8fff:   3478    228    275      0
0x9000-0x9fff:   2260    233    328      0
0xa000-0xafff:    921    282    374      0
0xb000-0xbfff:    322    335    395      0
0xc000-0xcfff:    228    388    299      0
0xd000-0xdfff:    261    415    277      0
0xe000-0xefff:    516    423    297      0
0xf000-0xffff:   2785   1903   1773  15450

```

 Share Format Run

```go

package main

import (
	"encoding/base64"
	"fmt"
	"image"
	"log"
	"strings"

	// Package image/jpeg is not used explicitly in the code below,
	// but is imported for its initialization side-effect, which allows
	// image.Decode to understand JPEG formatted images. Uncomment these
	// two lines to also understand GIF and PNG images:
	// _ "image/gif"
	// _ "image/png"
	_ "image/jpeg"
)

func main() {
	reader := base64.NewDecoder(base64.StdEncoding, strings.NewReader(data))
	config, format, err := image.DecodeConfig(reader)
	if err != nil {
		log.Fatal(err)
	}
	fmt.Println("Width:", config.Width, "Height:", config.Height, "Format:", format)
}

const data = `
/9j/4AAQSkZJRgABAQIAHAAcAAD/2wBDABALDA4MChAODQ4SERATGCgaGBYWGDEjJR0oOjM9PDkzODdA
SFxOQERXRTc4UG1RV19iZ2hnPk1xeXBkeFxlZ2P/2wBDARESEhgVGC8aGi9jQjhCY2NjY2NjY2NjY2Nj
Y2NjY2NjY2NjY2NjY2NjY2NjY2NjY2NjY2NjY2NjY2NjY2NjY2P/wAARCABnAJYDASIAAhEBAxEB/8QA
HwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIh
MUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVW
V1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXG
x8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQF
BgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAV
YnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOE
hYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq
8vP09fb3+Pn6/9oADAMBAAIRAxEAPwDlwKMD0pwzSiuK57QzGDxS7D6in8Y5ximnAPUfSlcq4m3ilUYp
2OKXHvRcVxnTtS7c07HNFK4DQPakC4PNOA+tOx70XAjK/So5gBGP94fzqfvUVx/qxx/EP51UXqRP4WSE
cmgjilP3jSEZqS0IO/NGDnpUiocDg/McDjvV6HTPOdVWYgsM5KcfzzQ2JySM2jp6VYu7SWzmMUwG4cgj
kMPUVBjjtTGtRu0Zopw+lFFxhinrGzuqqMsxAA9yaXFSRv5cqSEcIwYj6GpuZ30O30fSLKzhUpbpNMv3
5XGTn29BV28jt7pPLuIVljPBBFVreYx+VbqAjycgt3x14zRcNOxGyVFHQkIc/wA61exyKLbuzjdZ046d
ftEuTEw3Rk9SPT8P8Kpbea3tchbyVae4JkjbbGpGdwOM89Af6ViFTWUtGdcXoM2+woK1JtpNtTcoZt+l
Jt7ZqTbRtouFyPFRXI/c9D94fzqzioLsfuD/ALw/nVReqIn8LJCOTSY+tSMOTmkIpXLRu+F0t5pJxPHG
wjjUAuBjJJz1+laD6Pai+WaK9SBX6puzn6ZP+NV/Dkdtc6ZNbyAFwxLAHDYPv6VoQ21nPNEEiQGEFRtk
Gf0NaWTOeW7Of8QwGG4MRZnEbYXPJwRnOR0zWNXW+KrqBLUWi5EjbWCgcAA9c/gRXKYqZaGlK/LqMH0F
FLtHvRSNiYD2pSDTgpp6p0ywUHoTULXYxcktzrdCf7Xo8LP/AKyEmMNjJ46dfbFWJ5TDGNwB9lFUvDV9
YrbfYGbyrjcWG88S57g+vtV26ZIvMlumKwwjLZ6V0WfU54yTvYwtbubea2WNWbzg4bYQeBgj8OtYeKhj
u4y2HQxqxOD1xzxmrWAQCCGB6EGsaikndmsJxeiYzBo280/Z7UbayuaXGY5oIp+2lx9KLjIsVDeD/Rj/
ALy/zq1t96r3y4tT/vL/ADq4P3kRP4WSleTSFKkkKoCW4GaqNcMxIjXj1pxjKT0FKrGC1Nrw3vGrKkYz
5kTAr6455/HH510UdwPtRgWCbzF5+YYUf4Vwun39xpmoR3qASMmQUJwGU9Rnt/8AWrpbrxhb8/ZdOmaQ
gAGZwFH5ZJrpVKVlY5ZYhN6kXiu2eO/ikZlIljAAB5yM549OawSOOlPuLqe+umuLqTfM4OSOAo7ADsKh
hl/cRsTuJHPv7mlKi3sVTxNtGP20VJhThgSQaK52mnZnUqsWrpkyeUrr5pABOAPU1AGaXUCWJISHGPfP
P8qL7BiKnsMg46H3qrbzupbj5mPTPTpXVSglG551SpzSsXJ4/MBUgYIxyKpySyGBYJriV1D7kRpCVH4V
bSeNJ4xchni3DeqnBI+td7F4b0mKIRjT45VbktJlzk455+n6VtYzv2PNwFZWBHBGKVJDGVC54/nXQeMN
NttLNkba1jgWVWDmM8bhg4/nzXLSSbXVj6fyNKUdNRp21RtIRJGrjuM0u3FQ2DbodvcEkfQmrW2vLqLl
k0ejCXNFMj2/jQV9qkxSYNRcsZiq2oI32N2CkhWXJxwOe9XMcVt6hoPn6dFaW0wgRpNzvKDlz6+/0rai
ryv2Jm9LHJai+ZRGCBjnr71ErdAxAY9B611t1Y2cunbbaOQ3FvKZI3UqGlZMbiWwfcfhV231iwvLSM3U
lt5Uq52TuZG+hGMA12xXJGxxzjzybOQtNOvb5j9ktZJhnBIHyg+5PFX38JayqK/2eLJIBUTgkDA9q7ex
itrSHFpGsUbndhRgc+g7VNIyfZJAoJZUbb3I46CtFJMylBo8sdWhmYMuCnylc9wef5VUT7+1chc5NS7h
sUZO5RtIPUH3pkBDOxxxmqM9TQtn+WilhHfHaik43KTG3Z4IyPyrNVjGCsZ+dmwv6V3cXhSG8sYpJLud
JJIwxChdoJGcYx/Wkg8DafA4knvLiQr/ALqj+VQpKw3FtnFFfvbiSMgZJ6/jXp2n3d9cQRBTFsKD96EP
oOxPU/8A68VVtbbRtMVntbePKDLTSHJH/Aj/AEqHTvE66rq72VugMMcbSGTnL4wMAfjT5n0HyW3L+s6b
baxaJBdzN+7bcrxkAhun0rz3VNCv7e7lgigknWI43xLu6jjIHTjtXqfkpPGVYsBkghTikgsYIN/lhgXb
cxLkknp/ShczQ7xtY8vtEmhkj8yGRBuCnehUcnHcVtmwfJ/fQ8e7f/E12txZW91C0U6b42xlST2OR/Ko
Bo1gM/uW55/1jf41nOipu7LhV5FZHIGzI6zwj/vr/Ck+yr3uYf8Ax7/CutbQdMb71tn/ALaN/jSf8I/p
X/PoP++2/wAan6rAr6wzkWt0II+1Rc/7Lf4Vd1eeCSKBbdZDdShYoiZNoyfY10P/AAj2lf8APmP++2/x
oPh/SjKspsozIuNrZORjp3qo0FHYPb3OZt7ae3SzjuItsiRSAgnccl/UA+3Q1yNjKLR4ZZYY5VD7tkv3
WwO/+e1evPp9nI257aJm6bioz1z1+tY+s6Hplnot9PbWMMcqwOFcLyOO1bJWMZSTOPHi+9w3mosrlyd2
9lCj02g9P/1e9a3hzxAbl2ikZRcdQueHHt7j864Y8Z4I4oRzG6urFWU5BHBB7HNJxTFGbR6he6Vpmtgm
eLy5zwZI/lb8fX8azIvBUUTHdfSFP4QsYB/HNZ+k+KEnRY75hHOvAk6K/v7H9K6yyvlnQBmDZ6GsnzR0
N0oy1RzOtaN/Y1tHNFO06u+zYy4I4Jzx9KKveJblXuordSGES5b6n/62PzorKVdp2LjQTVyWz8UWEWlq
jSgyxfJt6EgdDzWTdeLIZGO7zHI/hVajGmWWP+PWL8qwlAIURrhpMAHHJA71pRcZrToZzcoEuo6heakA
GHk245CZ6/X1qPTLq40q+W5t2QybSpDAkEEc55/zilk5k2r91eKhLDzWz2rpsczbbuemeD76fUNG865I
MiysmQMZAAwa3a5j4ftu0ByP+fh/5CulkLLG7INzhSVHqe1Fh3uOoqn9qQQxyhndmHIxwOmSR2xQ13KD
KoiBZOV9JBnt707MVy5RWdNdy7wRGf3bfMinnO1jg+vY03WXLaJO3mhQ20b0zwpYf0qlG7S7icrJs08U
VwumgC+YiQyeVtZH567hzj8aSL949oGhE/2v5pJCDkksQwBHC4/+vXQ8LZ2uYxxCavY7us/xCcaBfn0h
b+VP0bnSrb94ZMJgOecj1rl/GfidUE2k2gy5+SeQjgA/wj3rlas2jdao48qrjLAGkSKPk4Gc1WMj92I+
lIJnU8OfxPWo5inBokmtQTmM4OOh71b0q6vbFmWCbaxHyqQGAP0PT8KhSTzVyo5ocSKA5VfTOTmqsmRd
pl99XjPzThzK3zOeOSeveirNmkgg/fIpYsTkYORxRXmzlTjJqx6EVUcU7mhkKCzdAK59QI9zYxtG1fYU
UVtgtmY4nZEa8Ak9aqFv3rfSiiu1nMeifDv/AJF+T/r4f+QrqqKKQwzQenNFFMCOKFIgNuThdoJ5OPSk
ubeK6t3gnXdG4wwziiii/UTKMOg6dbzJLFE4dSCP3rEdeOM8805tDsGMvySgSsS6rM6gk9eAcUUVftZt
3uyVGNthuq3Eei6DK8H7sRR7YuMgHtXkc8rzTNLM26RyWY+p70UVnLY0iEsUipG7rhZBlDkc1HgYoorM
0HwyBXGeRjmrcUhMg2ghezd//rUUVcTKW5s2jZtY/QDaOKKKK8ip8bPRj8KP/9k=
`

```

```go
Output:

```

 Share Format Run

- Variables
-  func RegisterFormat(name, magic string, decode func(io.Reader) (Image, error), ...)
-  type Alpha
-
-  func NewAlpha(r Rectangle) *Alpha

-
-  func (p *Alpha) AlphaAt(x, y int) color.Alpha
-  func (p *Alpha) At(x, y int) color.Color
-  func (p *Alpha) Bounds() Rectangle
-  func (p *Alpha) ColorModel() color.Model
-  func (p *Alpha) Opaque() bool
-  func (p *Alpha) PixOffset(x, y int) int
-  func (p *Alpha) RGBA64At(x, y int) color.RGBA64
-  func (p *Alpha) Set(x, y int, c color.Color)
-  func (p *Alpha) SetAlpha(x, y int, c color.Alpha)
-  func (p *Alpha) SetRGBA64(x, y int, c color.RGBA64)
-  func (p *Alpha) SubImage(r Rectangle) Image

-  type Alpha16
-
-  func NewAlpha16(r Rectangle) *Alpha16

-
-  func (p *Alpha16) Alpha16At(x, y int) color.Alpha16
-  func (p *Alpha16) At(x, y int) color.Color
-  func (p *Alpha16) Bounds() Rectangle
-  func (p *Alpha16) ColorModel() color.Model
-  func (p *Alpha16) Opaque() bool
-  func (p *Alpha16) PixOffset(x, y int) int
-  func (p *Alpha16) RGBA64At(x, y int) color.RGBA64
-  func (p *Alpha16) Set(x, y int, c color.Color)
-  func (p *Alpha16) SetAlpha16(x, y int, c color.Alpha16)
-  func (p *Alpha16) SetRGBA64(x, y int, c color.RGBA64)
-  func (p *Alpha16) SubImage(r Rectangle) Image

-  type CMYK
-
-  func NewCMYK(r Rectangle) *CMYK

-
-  func (p *CMYK) At(x, y int) color.Color
-  func (p *CMYK) Bounds() Rectangle
-  func (p *CMYK) CMYKAt(x, y int) color.CMYK
-  func (p *CMYK) ColorModel() color.Model
-  func (p *CMYK) Opaque() bool
-  func (p *CMYK) PixOffset(x, y int) int
-  func (p *CMYK) RGBA64At(x, y int) color.RGBA64
-  func (p *CMYK) Set(x, y int, c color.Color)
-  func (p *CMYK) SetCMYK(x, y int, c color.CMYK)
-  func (p *CMYK) SetRGBA64(x, y int, c color.RGBA64)
-  func (p *CMYK) SubImage(r Rectangle) Image

-  type Config
-
-  func DecodeConfig(r io.Reader) (Config, string, error)

-  type Gray
-
-  func NewGray(r Rectangle) *Gray

-
-  func (p *Gray) At(x, y int) color.Color
-  func (p *Gray) Bounds() Rectangle
-  func (p *Gray) ColorModel() color.Model
-  func (p *Gray) GrayAt(x, y int) color.Gray
-  func (p *Gray) Opaque() bool
-  func (p *Gray) PixOffset(x, y int) int
-  func (p *Gray) RGBA64At(x, y int) color.RGBA64
-  func (p *Gray) Set(x, y int, c color.Color)
-  func (p *Gray) SetGray(x, y int, c color.Gray)
-  func (p *Gray) SetRGBA64(x, y int, c color.RGBA64)
-  func (p *Gray) SubImage(r Rectangle) Image

-  type Gray16
-
-  func NewGray16(r Rectangle) *Gray16

-
-  func (p *Gray16) At(x, y int) color.Color
-  func (p *Gray16) Bounds() Rectangle
-  func (p *Gray16) ColorModel() color.Model
-  func (p *Gray16) Gray16At(x, y int) color.Gray16
-  func (p *Gray16) Opaque() bool
-  func (p *Gray16) PixOffset(x, y int) int
-  func (p *Gray16) RGBA64At(x, y int) color.RGBA64
-  func (p *Gray16) Set(x, y int, c color.Color)
-  func (p *Gray16) SetGray16(x, y int, c color.Gray16)
-  func (p *Gray16) SetRGBA64(x, y int, c color.RGBA64)
-  func (p *Gray16) SubImage(r Rectangle) Image

-  type Image
-
-  func Decode(r io.Reader) (Image, string, error)

-  type NRGBA
-
-  func NewNRGBA(r Rectangle) *NRGBA

-
-  func (p *NRGBA) At(x, y int) color.Color
-  func (p *NRGBA) Bounds() Rectangle
-  func (p *NRGBA) ColorModel() color.Model
-  func (p *NRGBA) NRGBAAt(x, y int) color.NRGBA
-  func (p *NRGBA) Opaque() bool
-  func (p *NRGBA) PixOffset(x, y int) int
-  func (p *NRGBA) RGBA64At(x, y int) color.RGBA64
-  func (p *NRGBA) Set(x, y int, c color.Color)
-  func (p *NRGBA) SetNRGBA(x, y int, c color.NRGBA)
-  func (p *NRGBA) SetRGBA64(x, y int, c color.RGBA64)
-  func (p *NRGBA) SubImage(r Rectangle) Image

-  type NRGBA64
-
-  func NewNRGBA64(r Rectangle) *NRGBA64

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

```go
func (p *YCbCr) YOffset(x, y int) int
```

YOffset returns the index of the first element of Y that corresponds to the pixel at (x, y).

```go
type YCbCrSubsampleRatio int
```

YCbCrSubsampleRatio is the chroma subsample ratio used in a YCbCr image.

```go
const (
	YCbCrSubsampleRatio444 YCbCrSubsampleRatio = iota
	YCbCrSubsampleRatio422
	YCbCrSubsampleRatio420
	YCbCrSubsampleRatio440
	YCbCrSubsampleRatio411
	YCbCrSubsampleRatio410
)
```

```go
func (s YCbCrSubsampleRatio) String() string
```

##   Source Files ¶
 View all Source files <https://cs.opensource.google/go/go/+/go1.26.3:src/image>

- format.go <https://cs.opensource.google/go/go/+/go1.26.3:src/image/format.go>
- geom.go <https://cs.opensource.google/go/go/+/go1.26.3:src/image/geom.go>
- image.go <https://cs.opensource.google/go/go/+/go1.26.3:src/image/image.go>
- names.go <https://cs.opensource.google/go/go/+/go1.26.3:src/image/names.go>
- ycbcr.go <https://cs.opensource.google/go/go/+/go1.26.3:src/image/ycbcr.go>

##   Directories ¶
    Show internal   Expand all

        color
 Package color implements a basic color library.

  Package color implements a basic color library.    palette  Package palette provides standard color palettes.

  Package palette provides standard color palettes.    draw
 Package draw provides image composition functions.

  Package draw provides image composition functions.    gif
 Package gif implements a GIF image decoder and encoder.

  Package gif implements a GIF image decoder and encoder.      internal      imageutil  Package imageutil contains code shared by image-related packages.

  Package imageutil contains code shared by image-related packages.    jpeg
 Package jpeg implements a JPEG image decoder and encoder.

  Package jpeg implements a JPEG image decoder and encoder.    png
 Package png implements a PNG image decoder and encoder.

  Package png implements a PNG image decoder and encoder.

  Click to show internal directories.
  Click to hide internal directories.

  Close

     **?** : This menu   **/** : Search site   **f** or **F** : Jump to   **y** or **Y**  : Canonical URL
  Close
