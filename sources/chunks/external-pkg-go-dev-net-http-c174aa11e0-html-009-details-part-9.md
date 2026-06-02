---
source_name: "External Linked Documentation"
source_url: "https://pkg.go.dev/net/http"
source_path: "sources/raw/external/pkg-go-dev-net-http-c174aa11e0.html"
license_ref: ""
---

// Response is the redirect response which caused this request
	// to be created. This field is only populated during client
	// redirects.
	Response *Response

// Pattern is the [ServeMux] pattern that matched the request.
	// It is empty if the request was not matched against a pattern.
	Pattern string
	// contains filtered or unexported fields
}
```

A Request represents an HTTP request received by a server or to be sent by a client.

The field semantics differ slightly between client and server usage. In addition to the notes on the fields below, see the documentation for Request.Write and RoundTripper.

```go
func NewRequest(method, url string, body io.Reader) (*Request, error)
```

NewRequest wraps NewRequestWithContext using context.Background.

```go
func NewRequestWithContext(ctx context.Context, method, url string, body io.Reader) (*Request, error)
```

NewRequestWithContext returns a new Request given a method, URL, and optional body.

If the provided body is also an io.Closer, the returned [Request.Body] is set to body and will be closed (possibly asynchronously) by the Client methods Do, Post, and PostForm, and Transport.RoundTrip.

NewRequestWithContext returns a Request suitable for use with Client.Do or Transport.RoundTrip. To create a request for use with testing a Server Handler, either use the net/http/httptest.NewRequest function, use ReadRequest, or manually update the Request fields. For an outgoing client request, the context controls the entire lifetime of a request and its response: obtaining a connection, sending the request, and reading the response headers and body. See the Request type's documentation for the difference between inbound and outbound request fields.

If body is of type *bytes.Buffer, *bytes.Reader, or *strings.Reader, the returned request's ContentLength is set to its exact value (instead of -1), GetBody is populated (so 307 and 308 redirects can replay the body), and Body is set to NoBody if the ContentLength is 0.

```go
func ReadRequest(b *bufio.Reader) (*Request, error)
```

ReadRequest reads and parses an incoming request from b.

ReadRequest is a low-level function and should only be used for specialized applications; most code should use the Server to read requests and handle them via the Handler interface. ReadRequest only supports HTTP/1.x requests. For HTTP/2, use golang.org/x/net/http2.

```go
func (r *Request) AddCookie(c *Cookie)
```

AddCookie adds a cookie to the request. Per RFC 6265 section 5.4 <https://rfc-editor.org/rfc/rfc6265.html#section-5.4>, AddCookie does not attach more than one Cookie header field. That means all cookies, if any, are written into the same line, separated by semicolon. AddCookie only sanitizes c's name and value, and does not sanitize a Cookie header already present in the request.

```go
func (r *Request) BasicAuth() (username, password string, ok bool)
```

BasicAuth returns the username and password provided in the request's Authorization header, if the request uses HTTP Basic Authentication. See RFC 2617, Section 2 <https://rfc-editor.org/rfc/rfc2617.html#section-2>.

```go
func (r *Request) Clone(ctx context.Context) *Request
```

Clone returns a deep copy of r with its context changed to ctx. The provided ctx must be non-nil.

Clone only makes a shallow copy of the Body field.

For an outgoing client request, the context controls the entire lifetime of a request and its response: obtaining a connection, sending the request, and reading the response headers and body.

```go
func (r *Request) Context() context.Context
```

Context returns the request's context. To change the context, use Request.Clone or Request.WithContext.

The returned context is always non-nil; it defaults to the background context.

For outgoing client requests, the context controls cancellation.

For incoming server requests, the context is canceled when the client's connection closes, the request is canceled (with HTTP/2), or when the ServeHTTP method returns.

```go
func (r *Request) Cookie(name string) (*Cookie, error)
```

Cookie returns the named cookie provided in the request or ErrNoCookie if not found. If multiple cookies match the given name, only one cookie will be returned.

```go
func (r *Request) Cookies() []*Cookie
```

Cookies parses and returns the HTTP cookies sent with the request.

```go
func (r *Request) CookiesNamed(name string) []*Cookie
```

CookiesNamed parses and returns the named HTTP cookies sent with the request or an empty slice if none matched.

```go
func (r *Request) FormFile(key string) (multipart.File, *multipart.FileHeader, error)
```

FormFile returns the first file for the provided form key. FormFile calls Request.ParseMultipartForm and Request.ParseForm if necessary.

```go
func (r *Request) FormValue(key string) string
```

FormValue returns the first value for the named component of the query. The precedence order:

- application/x-www-form-urlencoded form body (POST, PUT, PATCH only)
- query parameters (always)
- multipart/form-data form body (always)

FormValue calls Request.ParseMultipartForm and Request.ParseForm if necessary and ignores any errors returned by these functions. If key is not present, FormValue returns the empty string. To access multiple values of the same key, call ParseForm and then inspect [Request.Form] directly.

```go
func (r *Request) MultipartReader() (*multipart.Reader, error)
```

MultipartReader returns a MIME multipart reader if this is a multipart/form-data or a multipart/mixed POST request, else returns nil and an error. Use this function instead of Request.ParseMultipartForm to process the request body as a stream.

```go
func (r *Request) ParseForm() error
```

ParseForm populates r.Form and r.PostForm.

For all requests, ParseForm parses the raw query from the URL and updates r.Form.

For POST, PUT, and PATCH requests, it also reads the request body, parses it as a form and puts the results into both r.PostForm and r.Form. Request body parameters take precedence over URL query string values in r.Form.

If the request Body's size has not already been limited by MaxBytesReader, the size is capped at 10MB.

For other HTTP methods, or when the Content-Type is not application/x-www-form-urlencoded, the request Body is not read, and r.PostForm is initialized to a non-nil, empty value.

Request.ParseMultipartForm calls ParseForm automatically. ParseForm is idempotent.

```go
func (r *Request) ParseMultipartForm(maxMemory int64) error
```

ParseMultipartForm parses a request body as multipart/form-data. The whole request body is parsed and up to a total of maxMemory bytes of its file parts are stored in memory, with the remainder stored on disk in temporary files. ParseMultipartForm calls Request.ParseForm if necessary. If ParseForm returns an error, ParseMultipartForm returns it but also continues parsing the request body. After one call to ParseMultipartForm, subsequent calls have no effect.

```go
func (r *Request) PathValue(name string) string
```

PathValue returns the value for the named path wildcard in the ServeMux pattern that matched the request. It returns the empty string if the request was not matched against a pattern or there is no such wildcard in the pattern.

```go
func (r *Request) PostFormValue(key string) string
```

PostFormValue returns the first value for the named component of the POST, PUT, or PATCH request body. URL query parameters are ignored. PostFormValue calls Request.ParseMultipartForm and Request.ParseForm if necessary and ignores any errors returned by these functions. If key is not present, PostFormValue returns the empty string.

```go
func (r *Request) ProtoAtLeast(major, minor int) bool
```

ProtoAtLeast reports whether the HTTP protocol used in the request is at least major.minor.

```go
func (r *Request) Referer() string
```

Referer returns the referring URL, if sent in the request.

Referer is misspelled as in the request itself, a mistake from the earliest days of HTTP. This value can also be fetched from the Header map as Header["Referer"]; the benefit of making it available as a method is that the compiler can diagnose programs that use the alternate (correct English) spelling req.Referrer() but cannot diagnose programs that use Header["Referrer"].

```go
func (r *Request) SetBasicAuth(username, password string)
```

SetBasicAuth sets the request's Authorization header to use HTTP Basic Authentication with the provided username and password.

With HTTP Basic Authentication the provided username and password are not encrypted. It should generally only be used in an HTTPS request.

The username may not contain a colon. Some protocols may impose additional requirements on pre-escaping the username and password. For instance, when used with OAuth2, both arguments must be URL encoded first with url.QueryEscape.

```go
func (r *Request) SetPathValue(name, value string)
```

SetPathValue sets name to value, so that subsequent calls to r.PathValue(name) return value.

```go
func (r *Request) UserAgent() string
```

UserAgent returns the client's User-Agent, if sent in the request.

```go
func (r *Request) WithContext(ctx context.Context) *Request
```

WithContext returns a shallow copy of r with its context changed to ctx. The provided ctx must be non-nil.

For outgoing client request, the context controls the entire lifetime of a request and its response: obtaining a connection, sending the request, and reading the response headers and body.

To create a new request with a context, use NewRequestWithContext. To make a deep copy of a request with a new context, use Request.Clone.

```go
func (r *Request) Write(w io.Writer) error
```

Write writes an HTTP/1.1 request, which is the header and body, in wire format. This method consults the following fields of the request:

```go
Host
URL
Method (defaults to "GET")
Header
ContentLength
TransferEncoding
Body

```

If Body is present, Content-Length is <= 0 and [Request.TransferEncoding] hasn't been set to "identity", Write adds "Transfer-Encoding: chunked" to the header. Body is closed after it is sent.

```go
func (r *Request) WriteProxy(w io.Writer) error
```

WriteProxy is like Request.Write but writes the request in the form expected by an HTTP proxy. In particular, Request.WriteProxy writes the initial Request-URI line of the request with an absolute URI, per section 5.3 of RFC 7230 <https://rfc-editor.org/rfc/rfc7230.html>, including the scheme and host. In either case, WriteProxy also writes a Host header, using either r.Host or r.URL.Host.

```go
type Response struct {
	Status     string // e.g. "200 OK"
	StatusCode int    // e.g. 200
	Proto      string // e.g. "HTTP/1.0"
	ProtoMajor int    // e.g. 1
	ProtoMinor int    // e.g. 0
