---
source_name: "External Linked Documentation"
source_url: "https://pkg.go.dev/net/http"
source_path: "sources/raw/external/pkg-go-dev-net-http-c174aa11e0.html"
license_ref: ""
---

// headers with the same key, they may be concatenated, with comma
	// delimiters.  (RFC 7230, section 3.2.2 <https://rfc-editor.org/rfc/rfc7230.html#section-3.2.2> requires that multiple headers
	// be semantically equivalent to a comma-delimited sequence.) When
	// Header values are duplicated by other fields in this struct (e.g.,
	// ContentLength, TransferEncoding, Trailer), the field values are
	// authoritative.
	//
	// Keys in the map are canonicalized (see CanonicalHeaderKey).
	Header Header

// Body represents the response body.
	//
	// The response body is streamed on demand as the Body field
	// is read. If the network connection fails or the server
	// terminates the response, Body.Read calls return an error.
	//
	// The http Client and Transport guarantee that Body is always
	// non-nil, even on responses without a body or responses with
	// a zero-length body. It is the caller's responsibility to
	// close Body. The default HTTP client's Transport may not
	// reuse HTTP/1.x "keep-alive" TCP connections if the Body is
	// not read to completion and closed.
	//
	// The Body is automatically dechunked if the server replied
	// with a "chunked" Transfer-Encoding.
	//
	// As of Go 1.12, the Body will also implement io.Writer
	// on a successful "101 Switching Protocols" response,
	// as used by WebSockets and HTTP/2's "h2c" mode.
	Body io.ReadCloser

// ContentLength records the length of the associated content. The
	// value -1 indicates that the length is unknown. Unless Request.Method
	// is "HEAD", values >= 0 indicate that the given number of bytes may
	// be read from Body.
	ContentLength int64

// Contains transfer encodings from outer-most to inner-most. Value is
	// nil, means that "identity" encoding is used.
	TransferEncoding []string

// Close records whether the header directed that the connection be
	// closed after reading Body. The value is advice for clients: neither
	// ReadResponse nor Response.Write ever closes a connection.
	Close bool

// Uncompressed reports whether the response was sent compressed but
	// was decompressed by the http package. When true, reading from
	// Body yields the uncompressed content instead of the compressed
	// content actually set from the server, ContentLength is set to -1,
	// and the "Content-Length" and "Content-Encoding" fields are deleted
	// from the responseHeader. To get the original response from
	// the server, set Transport.DisableCompression to true.
	Uncompressed bool

// Trailer maps trailer keys to values in the same
	// format as Header.
	//
	// The Trailer initially contains only nil values, one for
	// each key specified in the server's "Trailer" header
	// value. Those values are not added to Header.
	//
	// Trailer must not be accessed concurrently with Read calls
	// on the Body.
	//
	// After Body.Read has returned io.EOF, Trailer will contain
	// any trailer values sent by the server.
	Trailer Header

// Request is the request that was sent to obtain this Response.
	// Request's Body is nil (having already been consumed).
	// This is only populated for Client requests.
	Request *Request

// TLS contains information about the TLS connection on which the
	// response was received. It is nil for unencrypted responses.
	// The pointer is shared between responses and should not be
	// modified.
	TLS *tls.ConnectionState
}
```

Response represents the response from an HTTP request.

The Client and Transport return Responses from servers once the response headers have been received. The response body is streamed on demand as the Body field is read.

```go
func Get(url string) (resp *Response, err error)
```

Get issues a GET to the specified URL. If the response is one of the following redirect codes, Get follows the redirect, up to a maximum of 10 redirects:

```go
301 (Moved Permanently)
302 (Found)
303 (See Other)
307 (Temporary Redirect)
308 (Permanent Redirect)

```

An error is returned if there were too many redirects or if there was an HTTP protocol error. A non-2xx response doesn't cause an error. Any returned error will be of type *url.Error. The url.Error value's Timeout method will report true if the request timed out.

When err is nil, resp always contains a non-nil resp.Body. Caller should close resp.Body when done reading from it.

Get is a wrapper around DefaultClient.Get.

To make a request with custom headers, use NewRequest and DefaultClient.Do.

To make a request with a specified context.Context, use NewRequestWithContext and DefaultClient.Do.

```go

package main

import (
	"fmt"
	"io"
	"log"
	"net/http"
)

func main() {
	res, err := http.Get("http://www.google.com/robots.txt")
	if err != nil {
		log.Fatal(err)
	}
	body, err := io.ReadAll(res.Body)
	res.Body.Close()
	if res.StatusCode > 299 {
		log.Fatalf("Response failed with status code: %d and\nbody: %s\n", res.StatusCode, body)
	}
	if err != nil {
		log.Fatal(err)
	}
	fmt.Printf("%s", body)
}

```

```go
Output:

```

Share Format Run

```go
func Head(url string) (resp *Response, err error)
```

Head issues a HEAD to the specified URL. If the response is one of the following redirect codes, Head follows the redirect, up to a maximum of 10 redirects:

```go
301 (Moved Permanently)
302 (Found)
303 (See Other)
307 (Temporary Redirect)
308 (Permanent Redirect)

```

Head is a wrapper around DefaultClient.Head.

To make a request with a specified context.Context, use NewRequestWithContext and DefaultClient.Do.

```go
func Post(url, contentType string, body io.Reader) (resp *Response, err error)
```

Post issues a POST to the specified URL.

Caller should close resp.Body when done reading from it.

If the provided body is an io.Closer, it is closed after the request.

Post is a wrapper around DefaultClient.Post.

To set custom headers, use NewRequest and DefaultClient.Do.

See the Client.Do method documentation for details on how redirects are handled.

To make a request with a specified context.Context, use NewRequestWithContext and DefaultClient.Do.

```go
func PostForm(url string, data url.Values) (resp *Response, err error)
```

PostForm issues a POST to the specified URL, with data's keys and values URL-encoded as the request body.

The Content-Type header is set to application/x-www-form-urlencoded. To set other headers, use NewRequest and DefaultClient.Do.

When err is nil, resp always contains a non-nil resp.Body. Caller should close resp.Body when done reading from it.

PostForm is a wrapper around DefaultClient.PostForm.

See the Client.Do method documentation for details on how redirects are handled.

To make a request with a specified context.Context, use NewRequestWithContext and DefaultClient.Do.

```go
func ReadResponse(r *bufio.Reader, req *Request) (*Response, error)
```

ReadResponse reads and returns an HTTP response from r. The req parameter optionally specifies the Request that corresponds to this Response. If nil, a GET request is assumed. Clients must call resp.Body.Close when finished reading resp.Body. After that call, clients can inspect resp.Trailer to find key/value pairs included in the response trailer.

```go
func (r *Response) Cookies() []*Cookie
```

Cookies parses and returns the cookies set in the Set-Cookie headers.

```go
func (r *Response) Location() (*url.URL, error)
```

Location returns the URL of the response's "Location" header, if present. Relative redirects are resolved relative to [Response.Request]. ErrNoLocation is returned if no Location header is present.

```go
func (r *Response) ProtoAtLeast(major, minor int) bool
```

ProtoAtLeast reports whether the HTTP protocol used in the response is at least major.minor.

```go
func (r *Response) Write(w io.Writer) error
```

Write writes r to w in the HTTP/1.x server response format, including the status line, headers, body, and optional trailer.

This method consults the following fields of the response r:

```go
StatusCode
ProtoMajor
ProtoMinor
Request.Method
TransferEncoding
Trailer
Body
ContentLength
Header, values for non-canonical keys will have unpredictable behavior

```

The Response Body is closed after it is sent.

```go
type ResponseController struct {
	// contains filtered or unexported fields
}
```

A ResponseController is used by an HTTP handler to control the response.

A ResponseController may not be used after the [Handler.ServeHTTP] method has returned.

```go
func NewResponseController(rw ResponseWriter) *ResponseController
```

NewResponseController creates a ResponseController for a request.

The ResponseWriter should be the original value passed to the [Handler.ServeHTTP] method, or have an Unwrap method returning the original ResponseWriter.

If the ResponseWriter implements any of the following methods, the ResponseController will call them as appropriate:

```go
Flush()
FlushError() error // alternative Flush returning an error
Hijack() (net.Conn, *bufio.ReadWriter, error)
SetReadDeadline(deadline time.Time) error
SetWriteDeadline(deadline time.Time) error
EnableFullDuplex() error

```

If the ResponseWriter does not support a method, ResponseController returns an error matching ErrNotSupported.

```go
func (c *ResponseController) EnableFullDuplex() error
```

EnableFullDuplex indicates that the request handler will interleave reads from [Request.Body] with writes to the ResponseWriter.

For HTTP/1 requests, the Go HTTP server by default consumes any unread portion of the request body before beginning to write the response, preventing handlers from concurrently reading from the request and writing the response. Calling EnableFullDuplex disables this behavior and permits handlers to continue to read from the request while concurrently writing the response.

For HTTP/2 requests, the Go HTTP server always permits concurrent reads and responses.

```go
func (c *ResponseController) Flush() error
```

Flush flushes buffered data to the client.

```go
func (c *ResponseController) Hijack() (net.Conn, *bufio.ReadWriter, error)
```

Hijack lets the caller take over the connection. See the Hijacker interface for details.

```go
func (c *ResponseController) SetReadDeadline(deadline time.Time) error
```

SetReadDeadline sets the deadline for reading the entire request, including the body. Reads from the request body after the deadline has been exceeded will return an error. A zero value means no deadline.

Setting the read deadline after it has been exceeded will not extend it.

```go
func (c *ResponseController) SetWriteDeadline(deadline time.Time) error
```

SetWriteDeadline sets the deadline for writing the response. Writes to the response body after the deadline has been exceeded will not block, but may succeed if the data has been buffered. A zero value means no deadline.

Setting the write deadline after it has been exceeded will not extend it.
