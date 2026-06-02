---
source_name: "Effective Go"
source_url: "https://go.dev/doc/effective_go"
source_path: "sources/raw/effective-go/effective_go.html"
license_ref: "sources/licenses/go-LICENSE.txt"
---

## Data

### Constructors and composite literals

 Sometimes the zero value isn't good enough and an initializing constructor is necessary, as in this example derived from package `os`.

```go

func NewFile(fd int, name string) *File {
    if fd < 0 {
        return nil
    }
    f := new(File)
    f.fd = fd
    f.name = name
    f.dirinfo = nil
    f.nepipe = 0
    return f
}

```

 There's a lot of boilerplate in there. We can simplify it using a _composite literal_, which is an expression that creates a new instance each time it is evaluated.

```go

func NewFile(fd int, name string) *File {
    if fd < 0 {
        return nil
    }
    f := File{fd, name, nil, 0}
    return &f
}

```

 Note that, unlike in C, it's perfectly OK to return the address of a local variable; the storage associated with the variable survives after the function returns. In fact, taking the address of a composite literal allocates a fresh instance each time it is evaluated, so we can combine these last two lines.

```go

    return &File{fd, name, nil, 0}

```

 The fields of a composite literal are laid out in order and must all be present. However, by labeling the elements explicitly as _field_`:`_value_ pairs, the initializers can appear in any order, with the missing ones left as their respective zero values. Thus we could say

```go

    return &File{fd: fd, name: name}

```

 As a limiting case, if a composite literal contains no fields at all, it creates a zero value for the type. The expressions `new(File)` and `&File{}` are equivalent.

 Composite literals can also be created for arrays, slices, and maps, with the field labels being indices or map keys as appropriate. In these examples, the initializations work regardless of the values of `Enone`, `Eio`, and `Einval`, as long as they are distinct.

```go

a := [...]string   {Enone: "no error", Eio: "Eio", Einval: "invalid argument"}
s := []string      {Enone: "no error", Eio: "Eio", Einval: "invalid argument"}
m := map[int]string{Enone: "no error", Eio: "Eio", Einval: "invalid argument"}

```
