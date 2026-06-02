---
source_name: "External Linked Documentation"
source_url: "https://go.dev/blog/context-and-structs"
source_path: "sources/raw/external/go-dev-blog-context-and-structs-bf5dd536db.html"
license_ref: ""
---

# The Go Blog

## Exception to the rule: preserving backwards compatibility

When Go 1.7 — which introduced context.Context — was released, a large number of APIs had to add context support in backwards compatible ways. For example, `net/http`’s `Client` methods, like `Get` and `Do`, were excellent candidates for context. Each external request sent with these methods would benefit from having the deadline, cancellation, and metadata support that came with `context.Context`.

There are two approaches for adding support for `context.Context` in backwards compatible ways: including a context in a struct, as we’ll see in a moment, and duplicating functions, with duplicates accepting `context.Context` and having `Context` as their function name suffix. The duplicate approach should be preferred over the context-in-struct, and is further discussed in Keeping your modules compatible. However, in some cases it’s impractical: for example, if your API exposes a large number of functions, then duplicating them all might be infeasible.

The `net/http` package chose the context-in-struct approach, which provides a useful case study. Let’s look at `net/http`’s `Do`. Prior to the introduction of `context.Context`, `Do` was defined as follows:

```go
// Do sends an HTTP request and returns an HTTP response [...]
func (c *Client) Do(req *Request) (*Response, error)

```

After Go 1.7, `Do` might have looked like the following, if not for the fact that it would break backwards compatibility:

```go
// Do sends an HTTP request and returns an HTTP response [...]
func (c *Client) Do(ctx context.Context, req *Request) (*Response, error)

```

But, preserving the backwards compatibility and adhering to the Go 1 promise of compatibility is crucial for the standard library. So, instead, the maintainers chose to add a `context.Context` on the `http.Request` struct in order to allow support `context.Context` without breaking backwards compatibility:

```go
// A Request represents an HTTP request received by a server or to be sent by a client.
// ...
type Request struct {
  ctx context.Context

  // ...
}

// NewRequestWithContext returns a new Request given a method, URL, and optional
// body.
// [...]
// The given ctx is used for the lifetime of the Request.
func NewRequestWithContext(ctx context.Context, method, url string, body io.Reader) (*Request, error) {
  // Simplified for brevity of this article.
  return &Request{
    ctx: ctx,
    // ...
  }
}

// Do sends an HTTP request and returns an HTTP response [...]
func (c *Client) Do(req *Request) (*Response, error)

```

When retrofitting your API to support context, it may make sense to add a `context.Context` to a struct, as above. However, remember to first consider duplicating your functions, which allows retrofitting `context.Context` in a backwards compatibility without sacrificing utility and comprehension. For example:

```go
// Call uses context.Background internally; to specify the context, use
// CallContext.
func (c *Client) Call() error {
  return c.CallContext(context.Background())
}

func (c *Client) CallContext(ctx context.Context) error {
  // ...
}

```
