---
source_name: "External Linked Documentation"
source_url: "https://dave.cheney.net/2016/04/27/dont-just-check-errors-handle-them-gracefully"
source_path: "sources/raw/external/dave-cheney-net-2016-04-27-dont-just-check-errors-handle-them-gracefully-a37809db60.html"
license_ref: ""
---

# Errors are just values

## Assert errors for behaviour, not type

In a small number of cases, this binary approach to error handling is not sufficient.

For example, interactions with the world outside your process, like network activity, require that the caller investigate the nature of the error to decide if it is reasonable to retry the operation.

In this case rather than asserting the error is a specific type or value, we can assert that the error implements a particular behaviour. Consider this example:

```go
type temporary interface {
        Temporary() bool
}

// IsTemporary returns true if err is temporary.
func IsTemporary(err error) bool {
        te, ok := err.(temporary)
        return ok && te.Temporary()
}
```

We can pass any error to `IsTemporary` to determine if the error could be retried.

If the error does not implement the `temporary` interface; that is, it does not have a `Temporary` method, then then error is not temporary.

If the error does implement `Temporary`, then perhaps the caller can retry the operation if `Temporary` returns `true`.

The key here is this logic can be implemented without importing the package that defines the error or indeed knowing anything about `err`‘s underlying type–we’re simply interested in its behaviour.

# Don’t just check errors, handle them gracefully

This brings me to a second Go proverb that I want to talk about; don’t just check errors, handle them gracefully. Can you suggest some problems with the following piece of code?

```go
func AuthenticateRequest(r *Request) error {
        err := authenticate(r.User)
        if err != nil {
                return err
        }
        return nil
}
```

An obvious suggestion is that the five lines of the function could be replaced with

```go
return authenticate(r.User)
```

But this is the simple stuff that everyone should be catching in code review. More fundamentally the problem with this code is I cannot tell where the original error came from.

If `authenticate` returns an error, then `AuthenticateRequest` will return the error to its caller, who will probably do the same, and so on. At the top of the program the main body of the program will print the error to the screen or a log file, and all that will be printed is: `No such file or directory`.

 There is no information of file and line where the error was generated. There is no stack trace of the call stack leading up to the error. The author of this code will be forced to a long session of bisecting their code to discover which code path trigged the file not found error.

Donovan and Kernighan’s _The Go Programming Language_ recommends that you add context to the error path using `fmt.Errorf`

```go
func AuthenticateRequest(r *Request) error {
        err := authenticate(r.User)
        if err != nil {
                return **fmt.Errorf("authenticate failed: %v", err)**
        }
        return nil
}
```

But as we saw earlier, this pattern is incompatible with the use of sentinel error values or type assertions, because converting the error value to a string, merging it with another string, then converting it back to an error with `fmt.Errorf` breaks equality and destroys any context in the original error.
