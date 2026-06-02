---
source_name: "External Linked Documentation"
source_url: "https://pkg.go.dev/net/http"
source_path: "sources/raw/external/pkg-go-dev-net-http-c174aa11e0.html"
license_ref: ""
---

As a special case, the returned file server redirects any request ending in "/index.html" to the same path, without the final "index.html".

```go
http.Handle("/", http.FileServerFS(fsys))

```

```go
func MaxBytesHandler(h Handler, n int64) Handler
```

MaxBytesHandler returns a Handler that runs h with its ResponseWriter and [Request.Body] wrapped by a MaxBytesReader.

```go
func NotFoundHandler() Handler
```

NotFoundHandler returns a simple request handler that replies to each request with a “404 page not found” reply.

```go

package main

import (
	"fmt"
	"log"
	"net/http"
)

func newPeopleHandler() http.Handler {
	return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		fmt.Fprintln(w, "This is the people handler.")
	})
}

func main() {
	mux := http.NewServeMux()

// Create sample handler to returns 404
	mux.Handle("/resources", http.NotFoundHandler())

// Create sample handler that returns 200
	mux.Handle("/resources/people/", newPeopleHandler())

log.Fatal(http.ListenAndServe(":8080", mux))
}

```

```go
Output:

```

Share Format Run

```go
func RedirectHandler(url string, code int) Handler
```

RedirectHandler returns a request handler that redirects each request it receives to the given url using the given status code.

The provided code should be in the 3xx range and is usually StatusMovedPermanently, StatusFound or StatusSeeOther.

```go
func StripPrefix(prefix string, h Handler) Handler
```

StripPrefix returns a handler that serves HTTP requests by removing the given prefix from the request URL's Path (and RawPath if set) and invoking the handler h. StripPrefix handles a request for a path that doesn't begin with prefix by replying with an HTTP 404 not found error. The prefix must match exactly: if the prefix in the request contains escaped characters the reply is also an HTTP 404 not found error.

```go

package main

import (
	"net/http"
)

func main() {
	// To serve a directory on disk (/tmp) under an alternate URL
	// path (/tmpfiles/), use StripPrefix to modify the request
	// URL's path before the FileServer sees it:
	http.Handle("/tmpfiles/", http.StripPrefix("/tmpfiles/", http.FileServer(http.Dir("/tmp"))))
}

```

```go
Output:

```

Share Format Run

```go
func TimeoutHandler(h Handler, dt time.Duration, msg string) Handler
```

TimeoutHandler returns a Handler that runs h with the given time limit.

The new Handler calls h.ServeHTTP to handle each request, but if a call runs for longer than its time limit, the handler responds with a 503 Service Unavailable error and the given message in its body. (If msg is empty, a suitable default message will be sent.) After such a timeout, writes by h to its ResponseWriter will return ErrHandlerTimeout.

TimeoutHandler supports the Pusher interface but does not support the Hijacker or Flusher interfaces.

```go
type HandlerFunc func(ResponseWriter, *Request)
```

The HandlerFunc type is an adapter to allow the use of ordinary functions as HTTP handlers. If f is a function with the appropriate signature, HandlerFunc(f) is a Handler that calls f.

```go
func (f HandlerFunc) ServeHTTP(w ResponseWriter, r *Request)
```

ServeHTTP calls f(w, r).

```go
type Header map[string][]string
```

A Header represents the key-value pairs in an HTTP header.

The keys should be in canonical form, as returned by CanonicalHeaderKey.

```go
func (h Header) Add(key, value string)
```

Add adds the key, value pair to the header. It appends to any existing values associated with key. The key is case insensitive; it is canonicalized by CanonicalHeaderKey.

```go
func (h Header) Clone() Header
```

Clone returns a copy of h or nil if h is nil.

```go
func (h Header) Del(key string)
```

Del deletes the values associated with key. The key is case insensitive; it is canonicalized by CanonicalHeaderKey.

```go
func (h Header) Get(key string) string
```

Get gets the first value associated with the given key. If there are no values associated with the key, Get returns "". It is case insensitive; textproto.CanonicalMIMEHeaderKey is used to canonicalize the provided key. Get assumes that all keys are stored in canonical form. To use non-canonical keys, access the map directly.

```go
func (h Header) Set(key, value string)
```

Set sets the header entries associated with key to the single element value. It replaces any existing values associated with key. The key is case insensitive; it is canonicalized by textproto.CanonicalMIMEHeaderKey. To use non-canonical keys, assign to the map directly.

```go
func (h Header) Values(key string) []string
```

Values returns all values associated with the given key. It is case insensitive; textproto.CanonicalMIMEHeaderKey is used to canonicalize the provided key. To use non-canonical keys, access the map directly. The returned slice is not a copy.

```go
func (h Header) Write(w io.Writer) error
```

Write writes a header in wire format.

```go
func (h Header) WriteSubset(w io.Writer, exclude map[string]bool) error
```

WriteSubset writes a header in wire format. If exclude is not nil, keys where exclude[key] == true are not written. Keys are not canonicalized before checking the exclude map.

```go
type Hijacker interface {
	// Hijack lets the caller take over the connection.
	// After a call to Hijack the HTTP server library
	// will not do anything else with the connection.
	//
	// It becomes the caller's responsibility to manage
	// and close the connection.
	//
	// The returned net.Conn may have read or write deadlines
	// already set, depending on the configuration of the
	// Server. It is the caller's responsibility to set
	// or clear those deadlines as needed.
	//
	// The returned bufio.Reader may contain unprocessed buffered
	// data from the client.
	//
	// After a call to Hijack, the original Request.Body must not
	// be used. The original Request's Context remains valid and
	// is not canceled until the Request's ServeHTTP method
	// returns.
	Hijack() (net.Conn, *bufio.ReadWriter, error)
}
```

The Hijacker interface is implemented by ResponseWriters that allow an HTTP handler to take over the connection.

The default ResponseWriter for HTTP/1.x connections supports Hijacker, but HTTP/2 connections intentionally do not. ResponseWriter wrappers may also not support Hijacker. Handlers should always test for this ability at runtime.

```go

package main

import (
	"fmt"
	"log"
	"net/http"
)

func main() {
	http.HandleFunc("/hijack", func(w http.ResponseWriter, r *http.Request) {
		hj, ok := w.(http.Hijacker)
		if !ok {
			http.Error(w, "webserver doesn't support hijacking", http.StatusInternalServerError)
			return
		}
		conn, bufrw, err := hj.Hijack()
		if err != nil {
			http.Error(w, err.Error(), http.StatusInternalServerError)
			return
		}
		// Don't forget to close the connection:
		defer conn.Close()
		bufrw.WriteString("Now we're speaking raw TCP. Say hi: ")
		bufrw.Flush()
		s, err := bufrw.ReadString('\n')
		if err != nil {
			log.Printf("error reading string: %v", err)
			return
		}
		fmt.Fprintf(bufrw, "You said: %q\nBye.\n", s)
		bufrw.Flush()
	})
}

```

```go
Output:

```

Share Format Run

```go
type MaxBytesError struct {
	Limit int64
}
```

MaxBytesError is returned by MaxBytesReader when its read limit is exceeded.

```go
func (e *MaxBytesError) Error() string
```

```go
type ProtocolError struct {
	ErrorString string
}
```

ProtocolError represents an HTTP protocol error.

Deprecated: Not all errors in the http package related to protocol errors are of type ProtocolError.

```go
func (pe *ProtocolError) Error() string
```

```go
func (pe *ProtocolError) Is(err error) bool
```

Is lets http.ErrNotSupported match errors.ErrUnsupported.

```go
type Protocols struct {
	// contains filtered or unexported fields
}
```

Protocols is a set of HTTP protocols. The zero value is an empty set of protocols.

The supported protocols are:

-
HTTP1 is the HTTP/1.0 and HTTP/1.1 protocols. HTTP1 is supported on both unsecured TCP and secured TLS connections.

-
HTTP2 is the HTTP/2 protcol over a TLS connection.

-
UnencryptedHTTP2 is the HTTP/2 protocol over an unsecured TCP connection.

```go

package main

import (
	"log"
	"net/http"
)

func main() {
	srv := http.Server{
		Addr: ":8443",
	}

// Serve only HTTP/1.
	srv.Protocols = new(http.Protocols)
	srv.Protocols.SetHTTP1(true)

log.Fatal(srv.ListenAndServeTLS("cert.pem", "key.pem"))
}

```

```go
Output:

```

Share Format Run

```go

package main

import (
	"log"
	"net/http"
)

func main() {
	t := http.DefaultTransport.(*http.Transport).Clone()

// Use either HTTP/1 and HTTP/2.
	t.Protocols = new(http.Protocols)
	t.Protocols.SetHTTP1(true)
	t.Protocols.SetHTTP2(true)

cli := &http.Client{Transport: t}
	res, err := cli.Get("http://www.google.com/robots.txt")
	if err != nil {
		log.Fatal(err)
	}
	res.Body.Close()
}

```

```go
Output:

```

Share Format Run

```go
func (p Protocols) HTTP1() bool
```

HTTP1 reports whether p includes HTTP/1.

```go
func (p Protocols) HTTP2() bool
```

HTTP2 reports whether p includes HTTP/2.

```go
func (p *Protocols) SetHTTP1(ok bool)
```

SetHTTP1 adds or removes HTTP/1 from p.

```go
func (p *Protocols) SetHTTP2(ok bool)
```

SetHTTP2 adds or removes HTTP/2 from p.

```go
func (p *Protocols) SetUnencryptedHTTP2(ok bool)
```

SetUnencryptedHTTP2 adds or removes unencrypted HTTP/2 from p.

```go
func (p Protocols) String() string
```

```go
func (p Protocols) UnencryptedHTTP2() bool
```

UnencryptedHTTP2 reports whether p includes unencrypted HTTP/2.

```go
type PushOptions struct {
	// Method specifies the HTTP method for the promised request.
	// If set, it must be "GET" or "HEAD". Empty means "GET".
	Method string

// include HTTP/2 pseudo header fields like ":path" and ":scheme",
	// which will be added automatically.
	Header Header
}
```

PushOptions describes options for [Pusher.Push].
