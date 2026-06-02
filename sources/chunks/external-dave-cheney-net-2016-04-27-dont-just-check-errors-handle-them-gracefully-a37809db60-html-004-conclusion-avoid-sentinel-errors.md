---
source_name: "External Linked Documentation"
source_url: "https://dave.cheney.net/2016/04/27/dont-just-check-errors-handle-them-gracefully"
source_path: "sources/raw/external/dave-cheney-net-2016-04-27-dont-just-check-errors-handle-them-gracefully-a37809db60.html"
license_ref: ""
---

# Errors are just values

## Conclusion: avoid sentinel errors

So, my advice is to avoid using sentinel error values in the code you write. There are a few cases where they are used in the standard library, but this is not a pattern that you should emulate.

If someone asks you to export an error value from your package, you should politely decline and instead suggest an alternative method, such as the ones I will discuss next.

# Error types

Error types are the second form of Go error handling I want to discuss.

```go
if err, ok := err.(SomeType); ok { … }
```

An error type is a type that you create that implements the error interface. In this example, the `MyError` type tracks the file and line, as well as a message explaining what happened.

```go
type MyError struct {
        Msg string
        File string
        Line int
}

func (e *MyError) Error() string {
        return fmt.Sprintf("%s:%d: %s”, e.File, e.Line, e.Msg)
}

return &MyError{"Something happened", “server.go", 42}
```

Because `MyError error` is a type, callers can use type assertion to extract the extra context from the error.

```go
err := something()
switch err := err.(type) {
case nil:
        // call succeeded, nothing to do
case *MyError:
        fmt.Println(“error occurred on line:”, err.Line)
default:
// unknown error
}
```

A big improvement of error types over error values is their ability to wrap an underlying error to provide more context.

An excellent example of this is the `os.PathError` type which annotates the underlying error with the operation it was trying to perform, and the file it was trying to use.

```go
// PathError records an error and the operation
// and file path that caused it.
type PathError struct {
        Op   string
        Path string
        **Err  error // the cause**
}

func (e *PathError) Error() string
```
