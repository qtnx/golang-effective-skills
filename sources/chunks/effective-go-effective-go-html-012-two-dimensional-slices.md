---
source_name: "Effective Go"
source_url: "https://go.dev/doc/effective_go"
source_path: "sources/raw/effective-go/effective_go.html"
license_ref: "sources/licenses/go-LICENSE.txt"
---

## Data

### Two-dimensional slices

 Go's arrays and slices are one-dimensional. To create the equivalent of a 2D array or slice, it is necessary to define an array-of-arrays or slice-of-slices, like this:

```go

type Transform [3][3]float64  // A 3x3 array, really an array of arrays.
type LinesOfText [][]byte     // A slice of byte slices.

```

 Because slices are variable-length, it is possible to have each inner slice be a different length. That can be a common situation, as in our `LinesOfText` example: each line has an independent length.

```go

text := LinesOfText{
    []byte("Now is the time"),
    []byte("for all good gophers"),
    []byte("to bring some fun to the party."),
}

```

 Sometimes it's necessary to allocate a 2D slice, a situation that can arise when processing scan lines of pixels, for instance. There are two ways to achieve this. One is to allocate each slice independently; the other is to allocate a single array and point the individual slices into it. Which to use depends on your application. If the slices might grow or shrink, they should be allocated independently to avoid overwriting the next line; if not, it can be more efficient to construct the object with a single allocation. For reference, here are sketches of the two methods. First, a line at a time:

```go

// Allocate the top-level slice.
picture := make([][]uint8, YSize) // One row per unit of y.
// Loop over the rows, allocating the slice for each row.
for i := range picture {
    picture[i] = make([]uint8, XSize)
}

```

 And now as one allocation, sliced into lines:

```go

// Allocate the top-level slice, the same as before.
picture := make([][]uint8, YSize) // One row per unit of y.
// Allocate one large slice to hold all the pixels.
pixels := make([]uint8, XSize*YSize) // Has type []uint8 even though picture is [][]uint8.
// Loop over the rows, slicing each row from the front of the remaining pixels slice.
for i := range picture {
    picture[i], pixels = pixels[:XSize], pixels[XSize:]
}

```
