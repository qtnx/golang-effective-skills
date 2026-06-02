---
source_name: "External Linked Documentation"
source_url: "https://dave.cheney.net/2016/04/27/dont-just-check-errors-handle-them-gracefully"
source_path: "sources/raw/external/dave-cheney-net-2016-04-27-dont-just-check-errors-handle-them-gracefully-a37809db60.html"
license_ref: ""
---

# Errors are just values

## Problems with error types

So the caller can use a type assertion or type switch, error types must be made public.

If your code implements an interface whose contract requires a specific error type, all implementors of that interface need to depend on the package that defines the error type.

This intimate knowledge of a package’s types creates a strong coupling with the caller, making for a brittle API.

# Errors are just values

## Conclusion: avoid error types

While error types are better than sentinel error values, because they can capture more context about what went wrong, error types share many of the problems of error values.

So again my advice is to avoid error types, or at least, avoid making them part of your public API.

# Opaque errors

Now we come to the third category of error handling. In my opinion this is the most flexible error handling strategy as it requires the least coupling between your code and caller.

I call this style opaque error handling, because while you know an error occurred, you don’t have the ability to see inside the error. As the caller, all you know about the result of the operation is that it worked, or it didn’t.

This is all there is to opaque error handling–just return the error without assuming anything about its contents. If you adopt this position, then error handling can become significantly more useful as a debugging aid.

```go
import “github.com/quux/bar”

func fn() error {
        x, err := bar.Foo()
        **if err != nil {
                return err
        }**
        // use x
}
```

For example, `Foo`‘s contract makes no guarantees about what it will return in the context of an error. The author of `Foo` is now free to annotate errors that pass through it with additional context without breaking its contract with the caller.
