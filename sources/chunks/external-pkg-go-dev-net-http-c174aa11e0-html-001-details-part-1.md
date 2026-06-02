---
source_name: "External Linked Documentation"
source_url: "https://pkg.go.dev/net/http"
source_path: "sources/raw/external/pkg-go-dev-net-http-c174aa11e0.html"
license_ref: ""
---

http package - net/http - Go Packages
## Details

-     Valid go.mod <https://cs.opensource.google/go/go/+/go1.26.3:src/go.mod> file
 The Go module system was introduced in Go 1.11 and is the official dependency management solution for Go.

-     Redistributable license
 Redistributable licenses place minimal restrictions on how software can be used, modified, and redistributed.

-     Tagged version
Modules with tagged versions give importers more predictable builds.

-     Stable version
When a project reaches major version v1 it is considered stable.

-  Learn more about best practices

## Repository
   cs.opensource.google/go/go  <https://cs.opensource.google/go/go>

##   Documentation ¶
   Rendered for <https://go.dev/about#build-context>  linux/amd64 windows/amd64 darwin/amd64 js/wasm

Package http provides HTTP client and server implementations.

Get, Head, Post, and PostForm make HTTP (or HTTPS) requests:

```go
resp, err := http.Get("http://example.com/")
...
resp, err := http.Post("http://example.com/upload", "image/jpeg", &buf)
...
resp, err := http.PostForm("http://example.com/form",
	url.Values{"key": {"Value"}, "id": {"123"}})

```

The caller must close the response body when finished with it:

```go
resp, err := http.Get("http://example.com/")
if err != nil {
	// handle error
}
defer resp.Body.Close()
body, err := io.ReadAll(resp.Body)
// ...

```

#### Clients and Transports ¶

For control over HTTP client headers, redirect policy, and other settings, create a Client:

```go
client := &http.Client{
	CheckRedirect: redirectPolicyFunc,
}

resp, err := client.Get("http://example.com")
// ...

req, err := http.NewRequest("GET", "http://example.com", nil)
// ...
req.Header.Add("If-None-Match", `W/"wyzzy"`)
resp, err := client.Do(req)
// ...

```

For control over proxies, TLS configuration, keep-alives, compression, and other settings, create a Transport:

```go
tr := &http.Transport{
	MaxIdleConns:       10,
	IdleConnTimeout:    30 * time.Second,
	DisableCompression: true,
}
client := &http.Client{Transport: tr}
resp, err := client.Get("https://example.com")

```

Clients and Transports are safe for concurrent use by multiple goroutines and for efficiency should only be created once and re-used.

#### Servers ¶

ListenAndServe starts an HTTP server with a given address and handler. The handler is usually nil, which means to use DefaultServeMux. Handle and HandleFunc add handlers to DefaultServeMux:

```go
http.Handle("/foo", fooHandler)

http.HandleFunc("/bar", func(w http.ResponseWriter, r *http.Request) {
	fmt.Fprintf(w, "Hello, %q", html.EscapeString(r.URL.Path))
})

log.Fatal(http.ListenAndServe(":8080", nil))

```

More control over the server's behavior is available by creating a custom Server:

```go
s := &http.Server{
	Addr:           ":8080",
	Handler:        myHandler,
	ReadTimeout:    10 * time.Second,
	WriteTimeout:   10 * time.Second,
	MaxHeaderBytes: 1 << 20,
}
log.Fatal(s.ListenAndServe())

```

#### HTTP/2 ¶

The http package has transparent support for the HTTP/2 protocol.

Server and DefaultTransport automatically enable HTTP/2 support when using HTTPS. Transport does not enable HTTP/2 by default.

To enable or disable support for HTTP/1, HTTP/2, and/or unencrypted HTTP/2, see the [Server.Protocols] and [Transport.Protocols] configuration fields.

To configure advanced HTTP/2 features, see the [Server.HTTP2] and [Transport.HTTP2] configuration fields.

Alternatively, the following GODEBUG settings are currently supported:

```go
GODEBUG=http2client=0  # disable HTTP/2 client support
GODEBUG=http2server=0  # disable HTTP/2 server support
GODEBUG=http2debug=1   # enable verbose HTTP/2 debug logs
GODEBUG=http2debug=2   # ... even more verbose, with frame dumps

```

The "omithttp2" build tag may be used to disable the HTTP/2 implementation contained in the http package.

- Constants
- Variables
-  func CanonicalHeaderKey(s string) string
-  func DetectContentType(data []byte) string
-  func Error(w ResponseWriter, error string, code int)
-  func Handle(pattern string, handler Handler)
-  func HandleFunc(pattern string, handler func(ResponseWriter, *Request))
-  func ListenAndServe(addr string, handler Handler) error
-  func ListenAndServeTLS(addr, certFile, keyFile string, handler Handler) error
-  func MaxBytesReader(w ResponseWriter, r io.ReadCloser, n int64) io.ReadCloser
-  func NotFound(w ResponseWriter, r *Request)
-  func ParseHTTPVersion(vers string) (major, minor int, ok bool)
-  func ParseTime(text string) (t time.Time, err error)
-  func ProxyFromEnvironment(req *Request) (*url.URL, error)
-  func ProxyURL(fixedURL *url.URL) func(*Request) (*url.URL, error)
-  func Redirect(w ResponseWriter, r *Request, url string, code int)
-  func Serve(l net.Listener, handler Handler) error
-  func ServeContent(w ResponseWriter, req *Request, name string, modtime time.Time, ...)
-  func ServeFile(w ResponseWriter, r *Request, name string)
-  func ServeFileFS(w ResponseWriter, r *Request, fsys fs.FS, name string)
-  func ServeTLS(l net.Listener, handler Handler, certFile, keyFile string) error
-  func SetCookie(w ResponseWriter, cookie *Cookie)
-  func StatusText(code int) string
-  type Client
-
-  func (c *Client) CloseIdleConnections()
-  func (c *Client) Do(req *Request) (*Response, error)
-  func (c *Client) Get(url string) (resp *Response, err error)
-  func (c *Client) Head(url string) (resp *Response, err error)
-  func (c *Client) Post(url, contentType string, body io.Reader) (resp *Response, err error)
-  func (c *Client) PostForm(url string, data url.Values) (resp *Response, err error)

-  type ClientConn
-
-  func (cc *ClientConn) Available() int
-  func (cc *ClientConn) Close() error
-  func (cc *ClientConn) Err() error
-  func (cc *ClientConn) InFlight() int
-  func (cc *ClientConn) Release()
-  func (cc *ClientConn) Reserve() error
-  func (cc *ClientConn) RoundTrip(req *Request) (*Response, error)
-  func (cc *ClientConn) SetStateHook(f func(*ClientConn))

-  type CloseNotifierdeprecated
-  type ConnState
-
-  func (c ConnState) String() string

-  type Cookie
-
-  func ParseCookie(line string) ([]*Cookie, error)
-  func ParseSetCookie(line string) (*Cookie, error)

-
-  func (c *Cookie) String() string
-  func (c *Cookie) Valid() error

-  type CookieJar
-  type CrossOriginProtection
-
-  func NewCrossOriginProtection() *CrossOriginProtection

-
-  func (c *CrossOriginProtection) AddInsecureBypassPattern(pattern string)
-  func (c *CrossOriginProtection) AddTrustedOrigin(origin string) error
-  func (c *CrossOriginProtection) Check(req *Request) error
-  func (c *CrossOriginProtection) Handler(h Handler) Handler
-  func (c *CrossOriginProtection) SetDenyHandler(h Handler)

-  type Dir
-
-  func (d Dir) Open(name string) (File, error)

-  type File
-  type FileSystem
-
-  func FS(fsys fs.FS) FileSystem

-  type Flusher
-  type HTTP2Config
-  type Handler
-
-  func AllowQuerySemicolons(h Handler) Handler
-  func FileServer(root FileSystem) Handler
-  func FileServerFS(root fs.FS) Handler
-  func MaxBytesHandler(h Handler, n int64) Handler
-  func NotFoundHandler() Handler
-  func RedirectHandler(url string, code int) Handler
-  func StripPrefix(prefix string, h Handler) Handler
-  func TimeoutHandler(h Handler, dt time.Duration, msg string) Handler

-  type HandlerFunc
-
-  func (f HandlerFunc) ServeHTTP(w ResponseWriter, r *Request)

-  type Header
-
-  func (h Header) Add(key, value string)
-  func (h Header) Clone() Header
-  func (h Header) Del(key string)
-  func (h Header) Get(key string) string
-  func (h Header) Set(key, value string)
-  func (h Header) Values(key string) []string
-  func (h Header) Write(w io.Writer) error
-  func (h Header) WriteSubset(w io.Writer, exclude map[string]bool) error

-  type Hijacker
-  type MaxBytesError
-
-  func (e *MaxBytesError) Error() string

-  type ProtocolErrordeprecated
-
-  func (pe *ProtocolError) Error() string
-  func (pe *ProtocolError) Is(err error) bool

-  type Protocols
-
-  func (p Protocols) HTTP1() bool
-  func (p Protocols) HTTP2() bool
-  func (p *Protocols) SetHTTP1(ok bool)
-  func (p *Protocols) SetHTTP2(ok bool)
-  func (p *Protocols) SetUnencryptedHTTP2(ok bool)
-  func (p Protocols) String() string
-  func (p Protocols) UnencryptedHTTP2() bool

-  type PushOptions
-  type Pusher
-  type Request
-
-  func NewRequest(method, url string, body io.Reader) (*Request, error)
-  func NewRequestWithContext(ctx context.Context, method, url string, body io.Reader) (*Request, error)
-  func ReadRequest(b *bufio.Reader) (*Request, error)

-
-  func (r *Request) AddCookie(c *Cookie)
-  func (r *Request) BasicAuth() (username, password string, ok bool)
-  func (r *Request) Clone(ctx context.Context) *Request
-  func (r *Request) Context() context.Context
-  func (r *Request) Cookie(name string) (*Cookie, error)
-  func (r *Request) Cookies() []*Cookie
-  func (r *Request) CookiesNamed(name string) []*Cookie
-  func (r *Request) FormFile(key string) (multipart.File, *multipart.FileHeader, error)
-  func (r *Request) FormValue(key string) string
-  func (r *Request) MultipartReader() (*multipart.Reader, error)
-  func (r *Request) ParseForm() error
-  func (r *Request) ParseMultipartForm(maxMemory int64) error
-  func (r *Request) PathValue(name string) string
-  func (r *Request) PostFormValue(key string) string
-  func (r *Request) ProtoAtLeast(major, minor int) bool
-  func (r *Request) Referer() string
-  func (r *Request) SetBasicAuth(username, password string)
-  func (r *Request) SetPathValue(name, value string)
-  func (r *Request) UserAgent() string
-  func (r *Request) WithContext(ctx context.Context) *Request
-  func (r *Request) Write(w io.Writer) error
-  func (r *Request) WriteProxy(w io.Writer) error

-  type Response
-
-  func Get(url string) (resp *Response, err error)
-  func Head(url string) (resp *Response, err error)
-  func Post(url, contentType string, body io.Reader) (resp *Response, err error)
-  func PostForm(url string, data url.Values) (resp *Response, err error)
-  func ReadResponse(r *bufio.Reader, req *Request) (*Response, error)

-
-  func (r *Response) Cookies() []*Cookie
-  func (r *Response) Location() (*url.URL, error)
-  func (r *Response) ProtoAtLeast(major, minor int) bool
-  func (r *Response) Write(w io.Writer) error

-  type ResponseController
-
-  func NewResponseController(rw ResponseWriter) *ResponseController

-
-  func (c *ResponseController) EnableFullDuplex() error
-  func (c *ResponseController) Flush() error
-  func (c *ResponseController) Hijack() (net.Conn, *bufio.ReadWriter, error)
-  func (c *ResponseController) SetReadDeadline(deadline time.Time) error
-  func (c *ResponseController) SetWriteDeadline(deadline time.Time) error

-  type ResponseWriter
-  type RoundTripper
-
-  func NewFileTransport(fs FileSystem) RoundTripper
-  func NewFileTransportFS(fsys fs.FS) RoundTripper

-  type SameSite
-  type ServeMux
-
-  func NewServeMux() *ServeMux

-
-  func (mux *ServeMux) Handle(pattern string, handler Handler)
-  func (mux *ServeMux) HandleFunc(pattern string, handler func(ResponseWriter, *Request))
-  func (mux *ServeMux) Handler(r *Request) (h Handler, pattern string)
-  func (mux *ServeMux) ServeHTTP(w ResponseWriter, r *Request)

-  type Server
-
-  func (s *Server) Close() error
-  func (s *Server) ListenAndServe() error
-  func (s *Server) ListenAndServeTLS(certFile, keyFile string) error
-  func (s *Server) RegisterOnShutdown(f func())
-  func (s *Server) Serve(l net.Listener) error
-  func (s *Server) ServeTLS(l net.Listener, certFile, keyFile string) error
-  func (s *Server) SetKeepAlivesEnabled(v bool)
-  func (s *Server) Shutdown(ctx context.Context) error

-  type Transport
-
-  func (t *Transport) CancelRequest(req *Request)deprecated
-  func (t *Transport) Clone() *Transport
-  func (t *Transport) CloseIdleConnections()
-  func (t *Transport) NewClientConn(ctx context.Context, scheme, address string) (*ClientConn, error)
-  func (t *Transport) RegisterProtocol(scheme string, rt RoundTripper)
-  func (t *Transport) RoundTrip(req *Request) (*Response, error)

- CrossOriginProtection
- FileServer
- FileServer (DotFileHiding)
- FileServer (StripPrefix)
- Get
- Handle
- HandleFunc
- Hijacker
- ListenAndServe
- ListenAndServeTLS
- NotFoundHandler
- Protocols (Http1)
- Protocols (Http1or2)
- ResponseWriter (Trailers)
- ServeMux.Handle
- Server.Shutdown
- StripPrefix
