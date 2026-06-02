---
source_name: "Effective Go"
source_url: "https://go.dev/doc/effective_go"
source_path: "sources/raw/effective-go/effective_go.html"
license_ref: "sources/licenses/go-LICENSE.txt"
---

## Data

### Append

 Now we have the missing piece we needed to explain the design of the `append` built-in function. The signature of `append` is different from our custom `Append` function above. Schematically, it's like this:

```go

func append(slice []_T_, elements ..._T_) []_T_

```

 where _T_ is a placeholder for any given type. You can't actually write a function in Go where the type `T` is determined by the caller. That's why `append` is built in: it needs support from the compiler.

 What `append` does is append the elements to the end of the slice and return the result. The result needs to be returned because, as with our hand-written `Append`, the underlying array may change. This simple example

```go

x := []int{1,2,3}
x = append(x, 4, 5, 6)
fmt.Println(x)

```

 prints `[1 2 3 4 5 6]`. So `append` works a little like `Printf`, collecting an arbitrary number of arguments.

 But what if we wanted to do what our `Append` does and append a slice to a slice? Easy: use `...` at the call site, just as we did in the call to `Output` above. This snippet produces identical output to the one above.

```go

x := []int{1,2,3}
y := []int{4,5,6}
x = append(x, y...)
fmt.Println(x)

```

 Without that `...`, it wouldn't compile because the types would be wrong; `y` is not of type `int`.
