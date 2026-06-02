---
source_name: "External Linked Documentation"
source_url: "https://go.dev/blog/go1.13-errors"
source_path: "sources/raw/external/go-dev-blog-go1-13-errors-cf4f1e8e99.html"
license_ref: ""
---

# The Go Blog

## Errors in Go 1.13

### The Unwrap method

Go 1.13 introduces new features to the `errors` and `fmt` standard library packages to simplify working with errors that contain other errors. The most significant of these is a convention rather than a change: an error which contains another may implement an `Unwrap` method returning the underlying error. If `e1.Unwrap()` returns `e2`, then we say that `e1` _wraps_ `e2`, and that you can _unwrap_ `e1` to get `e2`.

Following this convention, we can give the `QueryError` type above an `Unwrap` method that returns its contained error:

```go
func (e *QueryError) Unwrap() error { return e.Err }

```

The result of unwrapping an error may itself have an `Unwrap` method; we call the sequence of errors produced by repeated unwrapping the _error chain_.

### Examining errors with Is and As

The Go 1.13 `errors` package includes two new functions for examining errors: `Is` and `As`.

The `errors.Is` function compares an error to a value.

```go
// Similar to:
//   if err == ErrNotFound { … }
if errors.Is(err, ErrNotFound) {
    // something wasn't found
}

```

The `As` function tests whether an error is a specific type.

```go
// Similar to:
//   if e, ok := err.(*QueryError); ok { … }
var e *QueryError
// Note: *QueryError is the type of the error.
if errors.As(err, &e) {
    // err is a *QueryError, and e is set to the error's value
}

```

In the simplest case, the `errors.Is` function behaves like a comparison to a sentinel error, and the `errors.As` function behaves like a type assertion. When operating on wrapped errors, however, these functions consider all the errors in a chain. Let’s look again at the example from above of unwrapping a `QueryError` to examine the underlying error:

```go
if e, ok := err.(*QueryError); ok && e.Err == ErrPermission {
    // query failed because of a permission problem
}

```

Using the `errors.Is` function, we can write this as:

```go
if errors.Is(err, ErrPermission) {
    // err, or some error that it wraps, is a permission problem
}

```

The `errors` package also includes a new `Unwrap` function which returns the result of calling an error’s `Unwrap` method, or `nil` when the error has no `Unwrap` method. It is usually better to use `errors.Is` or `errors.As`, however, since these functions will examine the entire chain in a single call.

Note: although it may feel odd to take a pointer to a pointer, in this case it is correct. Think of it instead as taking a pointer to a value of the error type; it so happens in this case that the returned error is a pointer type.

### Wrapping errors with %w

As mentioned earlier, it is common to use the `fmt.Errorf` function to add additional information to an error.

```go
if err != nil {
    return fmt.Errorf("decompress %v: %v", name, err)
}

```

In Go 1.13, the `fmt.Errorf` function supports a new `%w` verb. When this verb is present, the error returned by `fmt.Errorf` will have an `Unwrap` method returning the argument of `%w`, which must be an error. In all other ways, `%w` is identical to `%v`.

```go
if err != nil {
    // Return an error which unwraps to err.
    return fmt.Errorf("decompress %v: %w", name, err)
}

```

Wrapping an error with `%w` makes it available to `errors.Is` and `errors.As`:

```go
err := fmt.Errorf("access denied: %w", ErrPermission)
...
if errors.Is(err, ErrPermission) ...

```

### Whether to Wrap

When adding additional context to an error, either with `fmt.Errorf` or by implementing a custom type, you need to decide whether the new error should wrap the original. There is no single answer to this question; it depends on the context in which the new error is created. Wrap an error to expose it to callers. Do not wrap an error when doing so would expose implementation details.

As one example, imagine a `Parse` function which reads a complex data structure from an `io.Reader`. If an error occurs, we wish to report the line and column number at which it occurred. If the error occurs while reading from the `io.Reader`, we will want to wrap that error to allow inspection of the underlying problem. Since the caller provided the `io.Reader` to the function, it makes sense to expose the error produced by it.

In contrast, a function which makes several calls to a database probably should not return an error which unwraps to the result of one of those calls. If the database used by the function is an implementation detail, then exposing these errors is a violation of abstraction. For example, if the `LookupUser` function of your package `pkg` uses Go’s `database/sql` package, then it may encounter a `sql.ErrNoRows` error. If you return that error with `fmt.Errorf("accessing DB: %v", err)` then a caller cannot look inside to find the `sql.ErrNoRows`. But if the function instead returns `fmt.Errorf("accessing DB: %w", err)`, then a caller could reasonably write

```go
err := pkg.LookupUser(...)
if errors.Is(err, sql.ErrNoRows) …

```

At that point, the function must always return `sql.ErrNoRows` if you don’t want to break your clients, even if you switch to a different database package. In other words, wrapping an error makes that error part of your API. If you don’t want to commit to supporting that error as part of your API in the future, you shouldn’t wrap the error.

It’s important to remember that whether you wrap or not, the error text will be the same. A _person_ trying to understand the error will have the same information either way; the choice to wrap is about whether to give _programs_ additional information so they can make more informed decisions, or to withhold that information to preserve an abstraction layer.
