---
source_name: "Effective Go"
source_url: "https://go.dev/doc/effective_go"
source_path: "sources/raw/effective-go/effective_go.html"
license_ref: "sources/licenses/go-LICENSE.txt"
---

## Data

### Arrays

 Arrays are useful when planning the detailed layout of memory and sometimes can help avoid allocation, but primarily they are a building block for slices, the subject of the next section. To lay the foundation for that topic, here are a few words about arrays.

 There are major differences between the ways arrays work in Go and C. In Go,

-  Arrays are values. Assigning one array to another copies all the elements.
-  In particular, if you pass an array to a function, it will receive a _copy_ of the array, not a pointer to it.
-  The size of an array is part of its type. The types `[10]int` and `[20]int` are distinct.

 The value property can be useful but also expensive; if you want C-like behavior and efficiency, you can pass a pointer to the array.

```go

func Sum(a *[3]float64) (sum float64) {
    for _, v := range *a {
        sum += v
    }
    return
}

array := [...]float64{7.0, 8.5, 9.1}
x := Sum(&array)  // Note the explicit address-of operator

```

 But even this style isn't idiomatic Go. Use slices instead.
