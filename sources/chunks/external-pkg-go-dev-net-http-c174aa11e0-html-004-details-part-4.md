---
source_name: "External Linked Documentation"
source_url: "https://pkg.go.dev/net/http"
source_path: "sources/raw/external/pkg-go-dev-net-http-c174aa11e0.html"
license_ref: ""
---

ServeFileFS replies to the request with the contents of the named file or directory from the file system fsys. The files provided by fsys must implement io.Seeker.

If the provided name is constructed from user input, it should be sanitized before calling ServeFileFS.

As a precaution, ServeFileFS will reject requests where r.URL.Path contains a ".." path element; this protects against callers who might unsafely use filepath.Join on r.URL.Path without sanitizing it and then use that filepath.Join result as the name argument.

As another special case, ServeFileFS redirects any request where r.URL.Path ends in "/index.html" to the same path, without the final "index.html". To avoid such redirects either modify the path or use ServeContent.

Outside of those two special cases, ServeFileFS does not use r.URL.Path for selecting the file or directory to serve; only the file or directory provided in the name argument is used.

```go
func ServeTLS(l net.Listener, handler Handler, certFile, keyFile string) error
```

ServeTLS accepts incoming HTTPS connections on the listener l, creating a new service goroutine for each. The service goroutines read requests and then call handler to reply to them.

The handler is typically nil, in which case DefaultServeMux is used.

Additionally, files containing a certificate and matching private key for the server must be provided. If the certificate is signed by a certificate authority, the certFile should be the concatenation of the server's certificate, any intermediates, and the CA's certificate.

ServeTLS always returns a non-nil error.

```go
func SetCookie(w ResponseWriter, cookie *Cookie)
```

SetCookie adds a Set-Cookie header to the provided ResponseWriter's headers. The provided cookie must have a valid Name. Invalid cookies may be silently dropped.

```go
func StatusText(code int) string
```

StatusText returns a text for the HTTP status code. It returns the empty string if the code is unknown.

```go
type Client struct {
	// Transport specifies the mechanism by which individual
	// HTTP requests are made.
	// If nil, DefaultTransport is used.
	Transport RoundTripper

// CheckRedirect specifies the policy for handling redirects.
	// If CheckRedirect is not nil, the client calls it before
	// following an HTTP redirect. The arguments req and via are
	// the upcoming request and the requests made already, oldest
	// first. If CheckRedirect returns an error, the Client's Get
	// method returns both the previous Response (with its Body
	// closed) and CheckRedirect's error (wrapped in a url.Error)
	// instead of issuing the Request req.
	// As a special case, if CheckRedirect returns ErrUseLastResponse,
	// then the most recent response is returned with its body
	// unclosed, along with a nil error.
	//
	// If CheckRedirect is nil, the Client uses its default policy,
	// which is to stop after 10 consecutive requests.
	CheckRedirect func(req *Request, via []*Request) error

// Jar specifies the cookie jar.
	//
	// The Jar is used to insert relevant cookies into every
	// outbound Request and is updated with the cookie values
	// of every inbound Response. The Jar is consulted for every
	// redirect that the Client follows.
	//
	// If Jar is nil, cookies are only sent if they are explicitly
	// set on the Request.
	Jar CookieJar

// Timeout specifies a time limit for requests made by this
	// Client. The timeout includes connection time, any
	// redirects, and reading the response body. The timer remains
	// running after Get, Head, Post, or Do return and will
	// interrupt reading of the Response.Body.
	//
	// A Timeout of zero means no timeout.
	//
	// The Client cancels requests to the underlying Transport
	// as if the Request's Context ended.
	//
	// For compatibility, the Client will also use the deprecated
	// CancelRequest method on Transport if found. New
	// RoundTripper implementations should use the Request's Context
	// for cancellation instead of implementing CancelRequest.
	Timeout time.Duration
}
```

A Client is an HTTP client. Its zero value (DefaultClient) is a usable client that uses DefaultTransport.

The [Client.Transport] typically has internal state (cached TCP connections), so Clients should be reused instead of created as needed. Clients are safe for concurrent use by multiple goroutines.

A Client is higher-level than a RoundTripper (such as Transport) and additionally handles HTTP details such as cookies and redirects.

When following redirects, the Client will forward all headers set on the initial Request except:

- when forwarding sensitive headers like "Authorization", "WWW-Authenticate", and "Cookie" to untrusted targets. These headers will be ignored when following a redirect to a domain that is not a subdomain match or exact match of the initial domain. For example, a redirect from "foo.com" to either "foo.com" or "sub.foo.com" will forward the sensitive headers, but a redirect to "bar.com" will not.
- when forwarding the "Cookie" header with a non-nil cookie Jar. Since each redirect may mutate the state of the cookie jar, a redirect may possibly alter a cookie set in the initial request. When forwarding the "Cookie" header, any mutated cookies will be omitted, with the expectation that the Jar will insert those mutated cookies with the updated values (assuming the origin matches). If Jar is nil, the initial cookies are forwarded without change.

```go
func (c *Client) CloseIdleConnections()
```

CloseIdleConnections closes any connections on its Transport which were previously connected from previous requests but are now sitting idle in a "keep-alive" state. It does not interrupt any connections currently in use.

If [Client.Transport] does not have a Client.CloseIdleConnections method then this method does nothing.

```go
func (c *Client) Do(req *Request) (*Response, error)
```

Do sends an HTTP request and returns an HTTP response, following policy (such as redirects, cookies, auth) as configured on the client.

An error is returned if caused by client policy (such as CheckRedirect), or failure to speak HTTP (such as a network connectivity problem). A non-2xx status code doesn't cause an error.

If the returned error is nil, the Response will contain a non-nil Body which the user is expected to close. If the Body is not both read to EOF and closed, the Client's underlying RoundTripper (typically Transport) may not be able to re-use a persistent TCP connection to the server for a subsequent "keep-alive" request.

The request Body, if non-nil, will be closed by the underlying Transport, even on errors. The Body may be closed asynchronously after Do returns.

On error, any Response can be ignored. A non-nil Response with a non-nil error only occurs when CheckRedirect fails, and even then the returned [Response.Body] is already closed.

Generally Get, Post, or PostForm will be used instead of Do.

If the server replies with a redirect, the Client first uses the CheckRedirect function to determine whether the redirect should be followed. If permitted, a 301, 302, or 303 redirect causes subsequent requests to use HTTP method GET (or HEAD if the original request was HEAD), with no body. A 307 or 308 redirect preserves the original HTTP method and body, provided that the [Request.GetBody] function is defined. The NewRequest function automatically sets GetBody for common standard library body types.

Any returned error will be of type *url.Error. The url.Error value's Timeout method will report true if the request timed out.

```go
func (c *Client) Get(url string) (resp *Response, err error)
```

Get issues a GET to the specified URL. If the response is one of the following redirect codes, Get follows the redirect after calling the [Client.CheckRedirect] function:

```go
301 (Moved Permanently)
302 (Found)
303 (See Other)
307 (Temporary Redirect)
308 (Permanent Redirect)

```

An error is returned if the [Client.CheckRedirect] function fails or if there was an HTTP protocol error. A non-2xx response doesn't cause an error. Any returned error will be of type *url.Error. The url.Error value's Timeout method will report true if the request timed out.

When err is nil, resp always contains a non-nil resp.Body. Caller should close resp.Body when done reading from it.

To make a request with custom headers, use NewRequest and Client.Do.

To make a request with a specified context.Context, use NewRequestWithContext and Client.Do.

```go
func (c *Client) Head(url string) (resp *Response, err error)
```

Head issues a HEAD to the specified URL. If the response is one of the following redirect codes, Head follows the redirect after calling the [Client.CheckRedirect] function:

```go
301 (Moved Permanently)
302 (Found)
303 (See Other)
307 (Temporary Redirect)
308 (Permanent Redirect)

```

To make a request with a specified context.Context, use NewRequestWithContext and Client.Do.

```go
func (c *Client) Post(url, contentType string, body io.Reader) (resp *Response, err error)
```

Post issues a POST to the specified URL.

Caller should close resp.Body when done reading from it.

If the provided body is an io.Closer, it is closed after the request.

To set custom headers, use NewRequest and Client.Do.

To make a request with a specified context.Context, use NewRequestWithContext and Client.Do.

See the Client.Do method documentation for details on how redirects are handled.

```go
func (c *Client) PostForm(url string, data url.Values) (resp *Response, err error)
```

PostForm issues a POST to the specified URL, with data's keys and values URL-encoded as the request body.

The Content-Type header is set to application/x-www-form-urlencoded. To set other headers, use NewRequest and Client.Do.

When err is nil, resp always contains a non-nil resp.Body. Caller should close resp.Body when done reading from it.

See the Client.Do method documentation for details on how redirects are handled.

To make a request with a specified context.Context, use NewRequestWithContext and Client.Do.

```go
type ClientConn struct {
	// contains filtered or unexported fields
}
```

A ClientConn is a client connection to an HTTP server.

Unlike a Transport, a ClientConn represents a single connection. Most users should use a Transport rather than creating client connections directly.

```go
func (cc *ClientConn) Available() int
```
