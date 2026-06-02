---
source_name: "Uber Go Style Guide"
source_url: "https://github.com/uber-go/guide/blob/master/style.md"
source_path: "sources/raw/uber-go-guide/style.md"
license_ref: "sources/licenses/uber-go-guide-LICENSE.txt"
---

## Guidelines

### Errors

#### Error Types

There are few options for declaring errors.
Consider the following before picking the option best suited for your use case.

- Does the caller need to match the error so that they can handle it?
  If yes, we must support the [`errors.Is`](https://pkg.go.dev/errors#Is) or [`errors.As`](https://pkg.go.dev/errors#As) functions
  by declaring a top-level error variable or a custom type.
- Is the error message a static string,
  or is it a dynamic string that requires contextual information?
  For the former, we can use [`errors.New`](https://pkg.go.dev/errors#New), but for the latter we must
  use [`fmt.Errorf`](https://pkg.go.dev/fmt#Errorf) or a custom error type.
- Are we propagating a new error returned by a downstream function?
  If so, see the [section on error wrapping](#error-wrapping).

| Error matching? | Error Message | Guidance                                                           |
|-----------------|---------------|--------------------------------------------------------------------|
| No              | static        | [`errors.New`](https://pkg.go.dev/errors#New)                      |
| No              | dynamic       | [`fmt.Errorf`](https://pkg.go.dev/fmt#Errorf)                      |
| Yes             | static        | top-level `var` with [`errors.New`](https://pkg.go.dev/errors#New) |
| Yes             | dynamic       | custom `error` type                                                |

For example,
use [`errors.New`](https://pkg.go.dev/errors#New) for an error with a static string.
Export this error as a variable to support matching it with `errors.Is`
if the caller needs to match and handle this error.

<table>
<thead><tr><th>No error matching</th><th>Error matching</th></tr></thead>
<tbody>
<tr><td>

```go
// package foo

func Open() error {
  return errors.New("could not open")
}

// package bar

if err := foo.Open(); err != nil {
  // Can't handle the error.
  panic("unknown error")
}
```

</td><td>

```go
// package foo

var ErrCouldNotOpen = errors.New("could not open")

func Open() error {
  return ErrCouldNotOpen
}

// package bar

if err := foo.Open(); err != nil {
  if errors.Is(err, foo.ErrCouldNotOpen) {
    // handle the error
  } else {
    panic("unknown error")
  }
}
```

</td></tr>
</tbody></table>

For an error with a dynamic string,
use [`fmt.Errorf`](https://pkg.go.dev/fmt#Errorf) if the caller does not need to match it,
and a custom `error` if the caller does need to match it.

<table>
<thead><tr><th>No error matching</th><th>Error matching</th></tr></thead>
<tbody>
<tr><td>

```go
// package foo

func Open(file string) error {
  return fmt.Errorf("file %q not found", file)
}

// package bar

if err := foo.Open("testfile.txt"); err != nil {
  // Can't handle the error.
  panic("unknown error")
}
```

</td><td>

```go
// package foo

type NotFoundError struct {
  File string
}

func (e *NotFoundError) Error() string {
  return fmt.Sprintf("file %q not found", e.File)
}

func Open(file string) error {
  return &NotFoundError{File: file}
}

// package bar

if err := foo.Open("testfile.txt"); err != nil {
  var notFound *NotFoundError
  if errors.As(err, &notFound) {
    // handle the error
  } else {
    panic("unknown error")
  }
}
```

</td></tr>
</tbody></table>

Note that if you export error variables or types from a package,
they will become part of the public API of the package.

#### Error Wrapping

There are three main options for propagating errors if a call fails:

- return the original error as-is
- add context with `fmt.Errorf` and the `%w` verb
- add context with `fmt.Errorf` and the `%v` verb

Return the original error as-is if there is no additional context to add.
This maintains the original error type and message.
This is well suited for cases when the underlying error message
has sufficient information to track down where it came from.

Otherwise, add context to the error message where possible
so that instead of a vague error such as "connection refused",
you get more useful errors such as "call service foo: connection refused".

Use `fmt.Errorf` to add context to your errors,
picking between the `%w` or `%v` verbs
based on whether the caller should be able to
match and extract the underlying cause.

- Use `%w` if the caller should have access to the underlying error.
  This is a good default for most wrapped errors,
  but be aware that callers may begin to rely on this behavior.
  So for cases where the wrapped error is a known `var` or type,
  document and test it as part of your function's contract.
- Use `%v` to obfuscate the underlying error.
  Callers will be unable to match it,
  but you can switch to `%w` in the future if needed.

When adding context to returned errors, keep the context succinct by avoiding
phrases like "failed to", which state the obvious and pile up as the error
percolates up through the stack:

<table>
<thead><tr><th>Bad</th><th>Good</th></tr></thead>
<tbody>
<tr><td>

```go
s, err := store.New()
if err != nil {
    return fmt.Errorf(
        "failed to create new store: %w", err)
}
```

</td><td>

```go
s, err := store.New()
if err != nil {
    return fmt.Errorf(
        "new store: %w", err)
}
```

</td></tr><tr><td>

```plain
failed to x: failed to y: failed to create new store: the error
```

</td><td>

```plain
x: y: new store: the error
```

</td></tr>
</tbody></table>

However once the error is sent to another system, it should be clear the
message is an error (e.g. an `err` tag or "Failed" prefix in logs).

See also [Don't just check errors, handle them gracefully](https://dave.cheney.net/2016/04/27/dont-just-check-errors-handle-them-gracefully).

#### Error Naming

For error values stored as global variables,
use the prefix `Err` or `err` depending on whether they're exported.
This guidance supersedes the [Prefix Unexported Globals with _](#prefix-unexported-globals-with-_).

```go
var (
  // The following two errors are exported
  // so that users of this package can match them
  // with errors.Is.

  ErrBrokenLink = errors.New("link is broken")
  ErrCouldNotOpen = errors.New("could not open")

  // This error is not exported because
  // we don't want to make it part of our public API.
  // We may still use it inside the package
  // with errors.Is.

  errNotFound = errors.New("not found")
)
```

For custom error types, use the suffix `Error` instead.

```go
// Similarly, this error is exported
// so that users of this package can match it
// with errors.As.

type NotFoundError struct {
  File string
}

func (e *NotFoundError) Error() string {
  return fmt.Sprintf("file %q not found", e.File)
}

// And this error is not exported because
// we don't want to make it part of the public API.
// We can still use it inside the package
// with errors.As.

type resolveError struct {
  Path string
}

func (e *resolveError) Error() string {
  return fmt.Sprintf("resolve %q", e.Path)
}
```

#### Handle Errors Once

When a caller receives an error from a callee,
it can handle it in a variety of different ways
depending on what it knows about the error.

These include, but not are limited to:

- if the callee contract defines specific errors,
  matching the error with `errors.Is` or `errors.As`
  and handling the branches differently
- if the error is recoverable,
  logging the error and degrading gracefully
- if the error represents a domain-specific failure condition,
  returning a well-defined error
- returning the error, either [wrapped](#error-wrapping) or verbatim

Regardless of how the caller handles the error,
it should typically handle each error only once.
The caller should not, for example, log the error and then return it,
because *its* callers may handle the error as well.

For example, consider the following cases:

<table>
<thead><tr><th>Description</th><th>Code</th></tr></thead>
<tbody>
<tr><td>

**Bad**: Log the error and return it

Callers further up the stack will likely take a similar action with the error.
Doing so makes a lot of noise in the application logs for little value.

</td><td>

```go
u, err := getUser(id)
if err != nil {
  // BAD: See description
  log.Printf("Could not get user %q: %v", id, err)
  return err
}
```

</td></tr>
<tr><td>

**Good**: Wrap the error and return it

Callers further up the stack will handle the error.
Use of `%w` ensures they can match the error with `errors.Is` or `errors.As`
if relevant.

</td><td>

```go
u, err := getUser(id)
if err != nil {
  return fmt.Errorf("get user %q: %w", id, err)
}
```

</td></tr>
<tr><td>

**Good**: Log the error and degrade gracefully

If the operation isn't strictly necessary,
we can provide a degraded but unbroken experience
by recovering from it.

</td><td>

```go
if err := emitMetrics(); err != nil {
  // Failure to write metrics should not
  // break the application.
  log.Printf("Could not emit metrics: %v", err)
}

```

</td></tr>
<tr><td>

**Good**: Match the error and degrade gracefully

If the callee defines a specific error in its contract,
and the failure is recoverable,
match on that error case and degrade gracefully.
For all other cases, wrap the error and return it.

Callers further up the stack will handle other errors.

</td><td>

```go
tz, err := getUserTimeZone(id)
if err != nil {
  if errors.Is(err, ErrUserNotFound) {
    // User doesn't exist. Use UTC.
    tz = time.UTC
  } else {
    return fmt.Errorf("get user %q: %w", id, err)
  }
}
```

</td></tr>
</tbody></table>
