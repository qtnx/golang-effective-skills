---
source_name: "External Linked Documentation"
source_url: "https://go.dev/doc/faq"
source_path: "sources/raw/external/go-dev-doc-faq-c6a034d6a5.html"
license_ref: ""
---

## Types

### Why is my nil error value not equal to nil?

Under the covers, interfaces are implemented as two elements, a type `T` and a value `V`. `V` is a concrete value such as an `int`, `struct` or pointer, never an interface itself, and has type `T`. For instance, if we store the `int` value 3 in an interface, the resulting interface value has, schematically, (`T=int`, `V=3`). The value `V` is also known as the interface’s _dynamic_ value, since a given interface variable might hold different values `V` (and corresponding types `T`) during the execution of the program.

An interface value is `nil` only if the `V` and `T` are both unset, (`T=nil`, `V` is not set), In particular, a `nil` interface will always hold a `nil` type. If we store a `nil` pointer of type `*int` inside an interface value, the inner type will be `*int` regardless of the value of the pointer: (`T=*int`, `V=nil`). Such an interface value will therefore be non-`nil` _even when the pointer value `V` inside is_ `nil`.

This situation can be confusing, and arises when a `nil` value is stored inside an interface value such as an `error` return:

```go
func returnsError() error {
    var p *MyError = nil
    if bad() {
        p = ErrBad
    }
    return p // Will always return a non-nil error.
}

```

If all goes well, the function returns a `nil` `p`, so the return value is an `error` interface value holding (`T=*MyError`, `V=nil`). This means that if the caller compares the returned error to `nil`, it will always look as if there was an error even if nothing bad happened. To return a proper `nil` `error` to the caller, the function must return an explicit `nil`:

```go
func returnsError() error {
    if bad() {
        return ErrBad
    }
    return nil
}

```

It’s a good idea for functions that return errors always to use the `error` type in their signature (as we did above) rather than a concrete type such as `*MyError`, to help guarantee the error is created correctly. As an example, `os.Open` returns an `error` even though, if not `nil`, it’s always of concrete type `*os.PathError`.

Similar situations to those described here can arise whenever interfaces are used. Just keep in mind that if any concrete value has been stored in the interface, the interface will not be `nil`. For more information, see The Laws of Reflection.
