---
source_name: "External Linked Documentation"
source_url: "https://go.dev/blog/go1.13-errors"
source_path: "sources/raw/external/go-dev-blog-go1-13-errors-cf4f1e8e99.html"
license_ref: ""
---

# The Go Blog

## Errors before Go 1.13

### Examining errors

Go errors are values. Programs make decisions based on those values in a few ways. The most common is to compare an error to `nil` to see if an operation failed.

```go
if err != nil {
    // something went wrong
}

```

Sometimes we compare an error to a known _sentinel_ value, to see if a specific error has occurred.

```go
var ErrNotFound = errors.New("not found")

if err == ErrNotFound {
    // something wasn't found
}

```

An error value may be of any type which satisfies the language-defined `error` interface. A program can use a type assertion or type switch to view an error value as a more specific type.

```go
type NotFoundError struct {
    Name string
}

func (e *NotFoundError) Error() string { return e.Name + ": not found" }

if e, ok := err.(*NotFoundError); ok {
    // e.Name wasn't found
}

```

### Adding information

Frequently a function passes an error up the call stack while adding information to it, like a brief description of what was happening when the error occurred. A simple way to do this is to construct a new error that includes the text of the previous one:

```go
if err != nil {
    return fmt.Errorf("decompress %v: %v", name, err)
}

```

Creating a new error with `fmt.Errorf` discards everything from the original error except the text. As we saw above with `QueryError`, we may sometimes want to define a new error type that contains the underlying error, preserving it for inspection by code. Here is `QueryError` again:

```go
type QueryError struct {
    Query string
    Err   error
}

```

Programs can look inside a `*QueryError` value to make decisions based on the underlying error. You’ll sometimes see this referred to as “unwrapping” the error.

```go
if e, ok := err.(*QueryError); ok && e.Err == ErrPermission {
    // query failed because of a permission problem
}

```

The `os.PathError` type in the standard library is another example of one error which contains another.
