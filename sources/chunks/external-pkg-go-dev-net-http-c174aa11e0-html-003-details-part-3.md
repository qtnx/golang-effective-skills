---
source_name: "External Linked Documentation"
source_url: "https://pkg.go.dev/net/http"
source_path: "sources/raw/external/pkg-go-dev-net-http-c174aa11e0.html"
license_ref: ""
---

ErrUseLastResponse can be returned by Client.CheckRedirect hooks to control how redirects are processed. If returned, the next request is not sent and the most recent response is returned with its body unclosed.
  View Source <https://cs.opensource.google/go/go/+/go1.26.3:src/net/http/http.go;l=173>
```go
var NoBody = noBody{}
```

NoBody is an io.ReadCloser with no bytes. Read always returns EOF and Close always returns nil. It can be used in an outgoing client request to explicitly signal that a request has zero bytes. An alternative, however, is to simply set [Request.Body] to nil.

```go
func CanonicalHeaderKey(s string) string
```

CanonicalHeaderKey returns the canonical format of the header key s. The canonicalization converts the first letter and any letter following a hyphen to upper case; the rest are converted to lowercase. For example, the canonical key for "accept-encoding" is "Accept-Encoding". If s contains a space or invalid header field bytes, it is returned without modifications.

```go
func DetectContentType(data []byte) string
```

DetectContentType implements the algorithm described at https://mimesniff.spec.whatwg.org/ <https://mimesniff.spec.whatwg.org/> to determine the Content-Type of the given data. It considers at most the first 512 bytes of data. DetectContentType always returns a valid MIME type: if it cannot determine a more specific one, it returns "application/octet-stream".

```go
func Error(w ResponseWriter, error string, code int)
```

Error replies to the request with the specified error message and HTTP code. It does not otherwise end the request; the caller should ensure no further writes are done to w. The error message should be plain text.

Error deletes the Content-Length header, sets Content-Type to “text/plain; charset=utf-8”, and sets X-Content-Type-Options to “nosniff”. This configures the header properly for the error message, in case the caller had set it up expecting a successful output.

```go
func Handle(pattern string, handler Handler)
```

Handle registers the handler for the given pattern in DefaultServeMux. The documentation for ServeMux explains how patterns are matched.

```go

package main

import (
	"fmt"
	"log"
	"net/http"
	"sync"
)

type countHandler struct {
	mu sync.Mutex // guards n
	n  int
}

func (h *countHandler) ServeHTTP(w http.ResponseWriter, r *http.Request) {
	h.mu.Lock()
	defer h.mu.Unlock()
	h.n++
	fmt.Fprintf(w, "count is %d\n", h.n)
}

func main() {
	http.Handle("/count", new(countHandler))
	log.Fatal(http.ListenAndServe(":8080", nil))
}

```

```go
Output:

```

Share Format Run

```go
func HandleFunc(pattern string, handler func(ResponseWriter, *Request))
```

HandleFunc registers the handler function for the given pattern in DefaultServeMux. The documentation for ServeMux explains how patterns are matched.

```go

package main

import (
	"io"
	"log"
	"net/http"
)

func main() {
	h1 := func(w http.ResponseWriter, _ *http.Request) {
		io.WriteString(w, "Hello from a HandleFunc #1!\n")
	}
	h2 := func(w http.ResponseWriter, _ *http.Request) {
		io.WriteString(w, "Hello from a HandleFunc #2!\n")
	}

http.HandleFunc("/", h1)
	http.HandleFunc("/endpoint", h2)

log.Fatal(http.ListenAndServe(":8080", nil))
}

```

```go
Output:

```

Share Format Run

```go
func ListenAndServe(addr string, handler Handler) error
```

ListenAndServe listens on the TCP network address addr and then calls Serve with handler to handle requests on incoming connections. Accepted connections are configured to enable TCP keep-alives.

The handler is typically nil, in which case DefaultServeMux is used.

ListenAndServe always returns a non-nil error.

```go

package main

import (
	"io"
	"log"
	"net/http"
)

func main() {
	// Hello world, the web server

helloHandler := func(w http.ResponseWriter, req *http.Request) {
		io.WriteString(w, "Hello, world!\n")
	}

http.HandleFunc("/hello", helloHandler)
	log.Fatal(http.ListenAndServe(":8080", nil))
}

```

```go
Output:

```

Share Format Run

```go
func ListenAndServeTLS(addr, certFile, keyFile string, handler Handler) error
```

ListenAndServeTLS acts identically to ListenAndServe, except that it expects HTTPS connections. Additionally, files containing a certificate and matching private key for the server must be provided. If the certificate is signed by a certificate authority, the certFile should be the concatenation of the server's certificate, any intermediates, and the CA's certificate.

```go

package main

import (
	"io"
	"log"
	"net/http"
)

func main() {
	http.HandleFunc("/", func(w http.ResponseWriter, req *http.Request) {
		io.WriteString(w, "Hello, TLS!\n")
	})

// One can use generate_cert.go in crypto/tls to generate cert.pem and key.pem.
	log.Printf("About to listen on 8443. Go to https://127.0.0.1:8443/")
	err := http.ListenAndServeTLS(":8443", "cert.pem", "key.pem", nil)
	log.Fatal(err)
}

```

```go
Output:

```

Share Format Run

```go
func MaxBytesReader(w ResponseWriter, r io.ReadCloser, n int64) io.ReadCloser
```

MaxBytesReader is similar to io.LimitReader but is intended for limiting the size of incoming request bodies. In contrast to io.LimitReader, MaxBytesReader's result is a ReadCloser, returns a non-nil error of type *MaxBytesError for a Read beyond the limit, and closes the underlying reader when its Close method is called.

MaxBytesReader prevents clients from accidentally or maliciously sending a large request and wasting server resources. If possible, it tells the ResponseWriter to close the connection after the limit has been reached.

```go
func NotFound(w ResponseWriter, r *Request)
```

NotFound replies to the request with an HTTP 404 not found error.

```go
func ParseHTTPVersion(vers string) (major, minor int, ok bool)
```

ParseHTTPVersion parses an HTTP version string according to RFC 7230, section 2.6 <https://rfc-editor.org/rfc/rfc7230.html#section-2.6>. "HTTP/1.0" returns (1, 0, true). Note that strings without a minor version, such as "HTTP/2", are not valid.

```go
func ParseTime(text string) (t time.Time, err error)
```

ParseTime parses a time header (such as the Date: header), trying each of the three formats allowed by HTTP/1.1: TimeFormat, time.RFC850, and time.ANSIC.

```go
func ProxyFromEnvironment(req *Request) (*url.URL, error)
```

ProxyFromEnvironment returns the URL of the proxy to use for a given request, as indicated by the environment variables HTTP_PROXY, HTTPS_PROXY and NO_PROXY (or the lowercase versions thereof). Requests use the proxy from the environment variable matching their scheme, unless excluded by NO_PROXY.

The environment values may be either a complete URL or a "host[:port]", in which case the "http" scheme is assumed. An error is returned if the value is a different form.

A nil URL and nil error are returned if no proxy is defined in the environment, or a proxy should not be used for the given request, as defined by NO_PROXY.

As a special case, if req.URL.Host is "localhost" (with or without a port number), then a nil URL and nil error will be returned.

```go
func ProxyURL(fixedURL *url.URL) func(*Request) (*url.URL, error)
```

ProxyURL returns a proxy function (for use in a Transport) that always returns the same URL.

```go
func Redirect(w ResponseWriter, r *Request, url string, code int)
```

Redirect replies to the request with a redirect to url, which may be a path relative to the request path. Any non-ASCII characters in url will be percent-encoded, but existing percent encodings will not be changed.

The provided code should be in the 3xx range and is usually StatusMovedPermanently, StatusFound or StatusSeeOther.

If the Content-Type header has not been set, Redirect sets it to "text/html; charset=utf-8" and writes a small HTML body. Setting the Content-Type header to any value, including nil, disables that behavior.

```go
func Serve(l net.Listener, handler Handler) error
```

Serve accepts incoming HTTP connections on the listener l, creating a new service goroutine for each. The service goroutines read requests and then call handler to reply to them.

The handler is typically nil, in which case DefaultServeMux is used.

HTTP/2 support is only enabled if the Listener returns *tls.Conn connections and they were configured with "h2" in the TLS Config.NextProtos.

Serve always returns a non-nil error.

```go
func ServeContent(w ResponseWriter, req *Request, name string, modtime time.Time, content io.ReadSeeker)
```

ServeContent replies to the request using the content in the provided ReadSeeker. The main benefit of ServeContent over io.Copy is that it handles Range requests properly, sets the MIME type, and handles If-Match, If-Unmodified-Since, If-None-Match, If-Modified-Since, and If-Range requests.

If the response's Content-Type header is not set, ServeContent first tries to deduce the type from name's file extension and, if that fails, falls back to reading the first block of the content and passing it to DetectContentType. The name is otherwise unused; in particular it can be empty and is never sent in the response.

If modtime is not the zero time or Unix epoch, ServeContent includes it in a Last-Modified header in the response. If the request includes an If-Modified-Since header, ServeContent uses modtime to decide whether the content needs to be sent at all.

The content's Seek method must work: ServeContent uses a seek to the end of the content to determine its size. Note that *os.File implements the io.ReadSeeker interface.

If the caller has set w's ETag header formatted per RFC 7232, section 2.3 <https://rfc-editor.org/rfc/rfc7232.html#section-2.3>, ServeContent uses it to handle requests using If-Match, If-None-Match, or If-Range.

If an error occurs when serving the request (for example, when handling an invalid range request), ServeContent responds with an error message. By default, ServeContent strips the Cache-Control, Content-Encoding, ETag, and Last-Modified headers from error responses. The GODEBUG setting httpservecontentkeepheaders=1 causes ServeContent to preserve these headers.

```go
func ServeFile(w ResponseWriter, r *Request, name string)
```

ServeFile replies to the request with the contents of the named file or directory.

If the provided file or directory name is a relative path, it is interpreted relative to the current directory and may ascend to parent directories. If the provided name is constructed from user input, it should be sanitized before calling ServeFile.

As a precaution, ServeFile will reject requests where r.URL.Path contains a ".." path element; this protects against callers who might unsafely use filepath.Join on r.URL.Path without sanitizing it and then use that filepath.Join result as the name argument.

As another special case, ServeFile redirects any request where r.URL.Path ends in "/index.html" to the same path, without the final "index.html". To avoid such redirects either modify the path or use ServeContent.

Outside of those two special cases, ServeFile does not use r.URL.Path for selecting the file or directory to serve; only the file or directory provided in the name argument is used.

```go
func ServeFileFS(w ResponseWriter, r *Request, fsys fs.FS, name string)
```
