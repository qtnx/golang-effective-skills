---
source_name: "Google Go Style Guide"
source_url: "https://google.github.io/styleguide/go/"
source_path: "sources/raw/google-go-styleguide/best-practices.md"
license_ref: "sources/licenses/google-styleguide-LICENSE.txt"
---

## Documentation
<a id="documentation-conventions"></a>
### Conventions

This section augments the decisions document's [commentary] section.

Go code that is documented in familiar style is easier to read and less likely
to be misused than something misdocumented or not documented at all. Runnable
[examples] show up in Godoc and Code Search and are an excellent way of
explaining how to use your code.

[examples]: decisions#examples

<a id="documentation-conventions-params"></a>

#### Parameters and configuration

Not every parameter must be enumerated in the documentation. This applies to:

*   function and method parameters
*   struct fields
*   APIs for options

Document the error-prone or non-obvious fields and parameters by saying why they
are interesting.

In the following snippet, the highlighted commentary adds little useful
information to the reader:

```go
// Bad:
// Sprintf formats according to a format specifier and returns the resulting
// string.
//
// format is the format, and data is the interpolation data.
func Sprintf(format string, data ...any) string
```

However, this snippet demonstrates a code scenario similar to the previous where
the commentary instead states something non-obvious or materially helpful to the
reader:

```go
// Good:
// Sprintf formats according to a format specifier and returns the resulting
// string.
//
// The provided data is used to interpolate the format string. If the data does
// not match the expected format verbs or the amount of data does not satisfy
// the format specification, the function will inline warnings about formatting
// errors into the output string as described by the Format errors section
// above.
func Sprintf(format string, data ...any) string
```

Consider your likely audience in choosing what to document and at what depth.
Maintainers, newcomers to the team, external users, and even yourself six months
in the future may appreciate slightly different information from what is on your
mind when you first come to write your docs.

See also:

*   [GoTip #41: Identify Function Call Parameters]
*   [GoTip #51: Patterns for Configuration]

[commentary]: decisions#commentary
[GoTip #41: Identify Function Call Parameters]: https://google.github.io/styleguide/go/index.html#gotip
[GoTip #51: Patterns for Configuration]: https://google.github.io/styleguide/go/index.html#gotip

<a id="documentation-conventions-contexts"></a>

#### Contexts

It is implied that the cancellation of a context argument interrupts the
function it is provided to. If the function can return an error, conventionally
it is `ctx.Err()`.

This fact does not need to be restated:

```go
// Bad:
// Run executes the worker's run loop.
//
// The method will process work until the context is cancelled and accordingly
// returns an error.
func (Worker) Run(ctx context.Context) error
```

Because that is implied, the following is better:

```go
// Good:
// Run executes the worker's run loop.
func (Worker) Run(ctx context.Context) error
```

Where context behavior is different or non-obvious, it should be expressly
documented if any of the following are true.

*   The function returns an error other than `ctx.Err()` when the context is
    cancelled:

    ```go
    // Good:
    // Run executes the worker's run loop.
    //
    // If the context is cancelled, Run returns a nil error.
    func (Worker) Run(ctx context.Context) error
    ```

*   The function has other mechanisms that may interrupt it or affect lifetime:

    ```go
    // Good:
    // Run executes the worker's run loop.
    //
    // Run processes work until the context is cancelled or Stop is called.
    // Context cancellation is handled asynchronously internally: run may return
    // before all work has stopped. The Stop method is synchronous and waits
    // until all operations from the run loop finish. Use Stop for graceful
    // shutdown.
    func (Worker) Run(ctx context.Context) error

    func (Worker) Stop()
    ```

*   The function has special expectations about context lifetime, lineage, or
    attached values:

    ```go
    // Good:
    // NewReceiver starts receiving messages sent to the specified queue.
    // The context should not have a deadline.
    func NewReceiver(ctx context.Context) *Receiver

    // Principal returns a human-readable name of the party who made the call.
    // The context must have a value attached to it from security.NewContext.
    func Principal(ctx context.Context) (name string, ok bool)
    ```

    **Warning:** Avoid designing APIs that make such demands (like contexts not
    having deadlines) from their callers. The above is only an example of how to
    document this if it cannot be avoided, not an endorsement of the pattern.

<a id="documentation-conventions-concurrency"></a>

#### Concurrency

Go users assume that conceptually read-only operations are safe for concurrent
use and do not require extra synchronization.

The extra remark about concurrency can safely be removed in this Godoc:

```go
// Len returns the number of bytes of the unread portion of the buffer;
// b.Len() == len(b.Bytes()).
//
// It is safe to be called concurrently by multiple goroutines.
func (*Buffer) Len() int
```

Mutating operations, however, are not assumed to be safe for concurrent use and
require the user to consider synchronization.

Similarly, the extra remark about concurrency can safely be removed here:

```go
// Grow grows the buffer's capacity.
//
// It is not safe to be called concurrently by multiple goroutines.
func (*Buffer) Grow(n int)
```

Documentation is strongly encouraged if any of the following are true.

*   It is unclear whether the operation is read-only or mutating:

    ```go
    // Good:
    package lrucache

    // Lookup returns the data associated with the key from the cache.
    //
    // This operation is not safe for concurrent use.
    func (*Cache) Lookup(key string) (data []byte, ok bool)
    ```

    Why? A cache hit when looking up the key mutate a LRU cache internally. How
    this is implemented may not be obvious to all readers.

*   Synchronization is provided by the API:

    ```go
    // Good:
    package fortune_go_proto

    // NewFortuneTellerClient returns an *rpc.Client for the FortuneTeller service.
    // It is safe for simultaneous use by multiple goroutines.
    func NewFortuneTellerClient(cc *rpc.ClientConn) *FortuneTellerClient
    ```

    Why? Stubby provides synchronization.

    **Note:** If the API is a type and the API provides synchronization in
    entirety, conventionally only the type definition documents the semantics.

*   The API consumes user-implemented types of interfaces, and the interface's
    consumer has particular concurrency requirements:

    ```go
    // Good:
    package health

    // A Watcher reports the health of some entity (usually a backend service).
    //
    // Watcher methods are safe for simultaneous use by multiple goroutines.
    type Watcher interface {
        // Watch sends true on the passed-in channel when the Watcher's
        // status has changed.
        Watch(changed chan<- bool) (unwatch func())

        // Health returns nil if the entity being watched is healthy, or a
        // non-nil error explaining why the entity is not healthy.
        Health() error
    }
    ```

    Why? Whether an API is safe for use by multiple goroutines is part of its
    contract.

<a id="documentation-conventions-cleanup"></a>

#### Cleanup

Document any explicit cleanup requirements that the API has. Otherwise, callers
won't use the API correctly, leading to resource leaks and other possible bugs.

Call out cleanups that are up to the caller:

```go
// Good:
// NewTicker returns a new Ticker containing a channel that will send the
// current time on the channel after each tick.
//
// Call Stop to release the Ticker's associated resources when done.
func NewTicker(d Duration) *Ticker

func (*Ticker) Stop()
```

If it is potentially unclear how to clean up the resources, explain how:

```go
// Good:
// Get issues a GET to the specified URL.
//
// When err is nil, resp always contains a non-nil resp.Body.
// Caller should close resp.Body when done reading from it.
//
//    resp, err := http.Get("http://example.com/")
//    if err != nil {
//        // handle error
//    }
//    defer resp.Body.Close()
//    body, err := io.ReadAll(resp.Body)
func (c *Client) Get(url string) (resp *Response, err error)
```

See also:

*   [GoTip #110: Don’t Mix Exit With Defer]

[GoTip #110: Don’t Mix Exit With Defer]: https://google.github.io/styleguide/go/index.html#gotip

<a id="documentation-conventions-errors"></a>

#### Errors

Document significant error sentinel values or error types that your functions
return to callers so that callers can anticipate what types of conditions they
can handle in their code.

```go
// Good:
package os

// Read reads up to len(b) bytes from the File and stores them in b. It returns
// the number of bytes read and any error encountered.
//
// At end of file, Read returns 0, io.EOF.
func (*File) Read(b []byte) (n int, err error) {
```

When a function returns a specific error type, correctly note whether the error
is a pointer receiver or not:

```go
// Good:
package os

type PathError struct {
    Op   string
    Path string
    Err  error
}

// Chdir changes the current working directory to the named directory.
//
// If there is an error, it will be of type *PathError.
func Chdir(dir string) error {
```

Documenting whether the values returned are pointer receivers enables callers to
correctly compare the errors using [`errors.Is`], [`errors.As`], and
[`package cmp`]. This is because a non-pointer value is not equivalent to a
pointer value.

**Note:** In the `Chdir` example, the return type is written as `error` rather
than `*PathError` due to
[how nil interface values work](https://go.dev/doc/faq#nil_error).

Document overall error conventions in the
[package's documentation](decisions#package-comments) when the behavior is
applicable to most errors found in the package:

```go
// Good:
// Package os provides a platform-independent interface to operating system
// functionality.
//
// Often, more information is available within the error. For example, if a
// call that takes a file name fails, such as Open or Stat, the error will
// include the failing file name when printed and will be of type *PathError,
// which may be unpacked for more information.
package os
```

Thoughtful application of these approaches can add
[extra information to errors](#error-extra-info) without much effort and help
callers avoid adding redundant annotations.

See also:

*   [Go Tip #106: Error Naming Conventions](https://google.github.io/styleguide/go/index.html#gotip)
*   [Go Tip #89: When to Use Canonical Status Codes as Errors](https://google.github.io/styleguide/go/index.html#gotip)

<a id="documentation-preview"></a>
