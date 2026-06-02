---
source_name: "External Linked Documentation"
source_url: "https://pkg.go.dev/net/http"
source_path: "sources/raw/external/pkg-go-dev-net-http-c174aa11e0.html"
license_ref: ""
---

```go
type ResponseWriter interface {
	// [ResponseWriter.WriteHeader]. The [Header] map also is the mechanism with which
	// [Handler] implementations can set HTTP trailers.
	//
	// Changing the header map after a call to [ResponseWriter.WriteHeader] (or
	// [ResponseWriter.Write]) has no effect unless the HTTP status code was of the
	// 1xx class or the modified headers are trailers.
	//
	// There are two ways to set Trailers. The preferred way is to
	// predeclare in the headers which trailers you will later
	// send by setting the "Trailer" header to the names of the
	// trailer keys which will come later. In this case, those
	// keys of the Header map are treated as if they were
	// trailers. See the example. The second way, for trailer
	// keys not known to the [Handler] until after the first [ResponseWriter.Write],
	// is to prefix the [Header] map keys with the [TrailerPrefix]
	// constant value.
	//
	// To suppress automatic response headers (such as "Date"), set
	// their value to nil.
	Header() Header

// Write writes the data to the connection as part of an HTTP reply.
	//
	// If [ResponseWriter.WriteHeader] has not yet been called, Write calls
	// WriteHeader(http.StatusOK) before writing the data. If the Header
	// does not contain a Content-Type line, Write adds a Content-Type set
	// to the result of passing the initial 512 bytes of written data to
	// [DetectContentType]. Additionally, if the total size of all written
	// data is under a few KB and there are no Flush calls, the
	// Content-Length header is added automatically.
	//
	// Depending on the HTTP protocol version and the client, calling
	// Write or WriteHeader may prevent future reads on the
	// Request.Body. For HTTP/1.x requests, handlers should read any
	// needed request body data before writing the response. Once the
	// headers have been flushed (due to either an explicit Flusher.Flush
	// call or writing enough data to trigger a flush), the request body
	// may be unavailable. For HTTP/2 requests, the Go HTTP server permits
	// handlers to continue to read the request body while concurrently
	// writing the response. However, such behavior may not be supported
	// by all HTTP/2 clients. Handlers should read before writing if
	// possible to maximize compatibility.
	Write([]byte) (int, error)

// status code.
	//
	// If WriteHeader is not called explicitly, the first call to Write
	// will trigger an implicit WriteHeader(http.StatusOK).
	// Thus explicit calls to WriteHeader are mainly used to
	// send error codes or 1xx informational responses.
	//
	// The provided code must be a valid HTTP 1xx-5xx status code.
	// Any number of 1xx headers may be written, followed by at most
	// one 2xx-5xx header. 1xx headers are sent immediately, but 2xx-5xx
	// headers may be buffered. Use the Flusher interface to send
	// buffered data. The header map is cleared when 2xx-5xx headers are
	// sent, but not with 1xx headers.
	//
	// The server will automatically send a 100 (Continue) header
	// on the first read from the request body if the request has
	// an "Expect: 100-continue" header.
	WriteHeader(statusCode int)
}
```

A ResponseWriter interface is used by an HTTP handler to construct an HTTP response.

A ResponseWriter may not be used after [Handler.ServeHTTP] has returned.

HTTP Trailers are a set of key/value pairs like headers that come after the HTTP response, instead of before.

```go

package main

import (
	"io"
	"net/http"
)

func main() {
	mux := http.NewServeMux()
	mux.HandleFunc("/sendstrailers", func(w http.ResponseWriter, req *http.Request) {
		// Before any call to WriteHeader or Write, declare
		// the trailers you will set during the HTTP
		// response. These three headers are actually sent in
		// the trailer.
		w.Header().Set("Trailer", "AtEnd1, AtEnd2")
		w.Header().Add("Trailer", "AtEnd3")

w.Header().Set("Content-Type", "text/plain; charset=utf-8") // normal header
		w.WriteHeader(http.StatusOK)

w.Header().Set("AtEnd1", "value 1")
		io.WriteString(w, "This HTTP response has both headers before this text and trailers at the end.\n")
		w.Header().Set("AtEnd2", "value 2")
		w.Header().Set("AtEnd3", "value 3") // These will appear as trailers.
	})
}

```

```go
Output:

```

Share Format Run

```go
type RoundTripper interface {
	// RoundTrip executes a single HTTP transaction, returning
	// a Response for the provided Request.
	//
	// RoundTrip should not attempt to interpret the response. In
	// particular, RoundTrip must return err == nil if it obtained
	// a response, regardless of the response's HTTP status code.
	// A non-nil err should be reserved for failure to obtain a
	// response. Similarly, RoundTrip should not attempt to
	// handle higher-level protocol details such as redirects,
	// authentication, or cookies.
	//
	// RoundTrip should not modify the request, except for
	// consuming and closing the Request's Body. RoundTrip may
	// read fields of the request in a separate goroutine. Callers
	// should not mutate or reuse the request until the Response's
	// Body has been closed.
	//
	// RoundTrip must always close the body, including on errors,
	// but depending on the implementation may do so in a separate
	// goroutine even after RoundTrip returns. This means that
	// callers wanting to reuse the body for subsequent requests
	// must arrange to wait for the Close call before doing so.
	//
	// The Request's URL and Header fields must be initialized.
	RoundTrip(*Request) (*Response, error)
}
```

RoundTripper is an interface representing the ability to execute a single HTTP transaction, obtaining the Response for a given Request.

A RoundTripper must be safe for concurrent use by multiple goroutines.

```go
var DefaultTransport RoundTripper = &Transport{
	Proxy: ProxyFromEnvironment,
	DialContext: defaultTransportDialContext(&net.Dialer{
		Timeout:   30 * time.Second,
		KeepAlive: 30 * time.Second,
	}),
	ForceAttemptHTTP2:     true,
	MaxIdleConns:          100,
	IdleConnTimeout:       90 * time.Second,
	TLSHandshakeTimeout:   10 * time.Second,
	ExpectContinueTimeout: 1 * time.Second,
}
```

DefaultTransport is the default implementation of Transport and is used by DefaultClient. It establishes network connections as needed and caches them for reuse by subsequent calls. It uses HTTP proxies as directed by the environment variables HTTP_PROXY, HTTPS_PROXY and NO_PROXY (or the lowercase versions thereof).

```go
func NewFileTransport(fs FileSystem) RoundTripper
```

NewFileTransport returns a new RoundTripper, serving the provided FileSystem. The returned RoundTripper ignores the URL host in its incoming requests, as well as most other properties of the request.

The typical use case for NewFileTransport is to register the "file" protocol with a Transport, as in:

```go
t := &http.Transport{}
t.RegisterProtocol("file", http.NewFileTransport(http.Dir("/")))
c := &http.Client{Transport: t}
res, err := c.Get("file:///etc/passwd")
...

```

```go
func NewFileTransportFS(fsys fs.FS) RoundTripper
```

NewFileTransportFS returns a new RoundTripper, serving the provided file system fsys. The returned RoundTripper ignores the URL host in its incoming requests, as well as most other properties of the request. The files provided by fsys must implement io.Seeker.

The typical use case for NewFileTransportFS is to register the "file" protocol with a Transport, as in:

```go
fsys := os.DirFS("/")
t := &http.Transport{}
t.RegisterProtocol("file", http.NewFileTransportFS(fsys))
c := &http.Client{Transport: t}
res, err := c.Get("file:///etc/passwd")
...

```

```go
type SameSite int
```

SameSite allows a server to define a cookie attribute making it impossible for the browser to send this cookie along with cross-site requests. The main goal is to mitigate the risk of cross-origin information leakage, and provide some protection against cross-site request forgery attacks.

See https://tools.ietf.org/html/draft-ietf-httpbis-cookie-same-site-00 <https://tools.ietf.org/html/draft-ietf-httpbis-cookie-same-site-00> for details.

```go
const (
	SameSiteDefaultMode SameSite = iota + 1
	SameSiteLaxMode
	SameSiteStrictMode
	SameSiteNoneMode
)
```

```go
type ServeMux struct {
	// contains filtered or unexported fields
}
```

ServeMux is an HTTP request multiplexer. It matches the URL of each incoming request against a list of registered patterns and calls the handler for the pattern that most closely matches the URL.

#### Patterns ¶

Patterns can match the method, host and path of a request. Some examples:

- "/index.html" matches the path "/index.html" for any host and method.
- "GET /static/" matches a GET request whose path begins with "/static/".
- "example.com/" matches any request to the host "example.com".
- "example.com/{$}" matches requests with host "example.com" and path "/".
- "/b/{bucket}/o/{objectname...}" matches paths whose first segment is "b" and whose third segment is "o". The name "bucket" denotes the second segment and "objectname" denotes the remainder of the path.

In general, a pattern looks like

```go
[METHOD ][HOST]/[PATH]

```

All three parts are optional; "/" is a valid pattern. If METHOD is present, it must be followed by at least one space or tab.

Literal (that is, non-wildcard) parts of a pattern match the corresponding parts of a request case-sensitively.

A pattern with no method matches every method. A pattern with the method GET matches both GET and HEAD requests. Otherwise, the method must match exactly.

A pattern with no host matches every host. A pattern with a host matches URLs on that host only.

A path can include wildcard segments of the form {NAME} or {NAME...}. For example, "/b/{bucket}/o/{objectname...}". The wildcard name must be a valid Go identifier. Wildcards must be full path segments: they must be preceded by a slash and followed by either a slash or the end of the string. For example, "/b_{bucket}" is not a valid pattern.

Normally a wildcard matches only a single path segment, ending at the next literal slash (not %2F) in the request URL. But if the "..." is present, then the wildcard matches the remainder of the URL path, including slashes. (Therefore it is invalid for a "..." wildcard to appear anywhere but at the end of a pattern.) The match for a wildcard can be obtained by calling Request.PathValue with the wildcard's name. A trailing slash in a path acts as an anonymous "..." wildcard.

The special wildcard {$} matches only the end of the URL. For example, the pattern "/{$}" matches only the path "/", whereas the pattern "/" matches every path.
