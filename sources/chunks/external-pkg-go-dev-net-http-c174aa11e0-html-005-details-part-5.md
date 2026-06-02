---
source_name: "External Linked Documentation"
source_url: "https://pkg.go.dev/net/http"
source_path: "sources/raw/external/pkg-go-dev-net-http-c174aa11e0.html"
license_ref: ""
---

Available reports the number of requests that may be sent to the connection without blocking. It returns 0 if the connection is closed.

```go
func (cc *ClientConn) Close() error
```

Close closes the connection. Outstanding RoundTrip calls are interrupted.

```go
func (cc *ClientConn) Err() error
```

Err reports any fatal connection errors. It returns nil if the connection is usable. If it returns non-nil, the connection can no longer be used.

```go
func (cc *ClientConn) InFlight() int
```

InFlight reports the number of requests in flight, including reserved requests. It returns 0 if the connection is closed.

```go
func (cc *ClientConn) Release()
```

Release releases an unused concurrency slot reserved by Reserve. If there are no reserved concurrency slots, it has no effect.

```go
func (cc *ClientConn) Reserve() error
```

Reserve reserves a concurrency slot on the connection. If Reserve returns nil, one additional RoundTrip call may be made without waiting for an existing request to complete.

The reserved concurrency slot is accounted as an in-flight request. A successful call to RoundTrip will decrement the Available count and increment the InFlight count.

Each successful call to Reserve should be followed by exactly one call to RoundTrip or Release, which will consume or release the reservation.

If the connection is closed or at its concurrency limit, Reserve returns an error.

```go
func (cc *ClientConn) RoundTrip(req *Request) (*Response, error)
```

RoundTrip implements the RoundTripper interface.

The request is sent on the client connection, regardless of the URL being requested or any proxy settings.

If the connection is at its concurrency limit, RoundTrip waits for the connection to become available before sending the request.

```go
func (cc *ClientConn) SetStateHook(f func(*ClientConn))
```

SetStateHook arranges for f to be called when the state of the connection changes. At most one call to f is made at a time. If the connection's state has changed since it was created, f is called immediately in a separate goroutine. f may be called synchronously from RoundTrip or Response.Body.Close.

If SetStateHook is called multiple times, the new hook replaces the old one. If f is nil, no further calls will be made to f after SetStateHook returns.

f is called when Available increases (more requests may be sent on the connection), InFlight decreases (existing requests complete), or Err begins returning non-nil (the connection is no longer usable).

```go
type CloseNotifier interface {
	// CloseNotify returns a channel that receives at most a
	// single value (true) when the client connection has gone
	// away.
	//
	// CloseNotify may wait to notify until Request.Body has been
	// fully read.
	//
	// After the Handler has returned, there is no guarantee
	// that the channel receives a value.
	//
	// If the protocol is HTTP/1.1 and CloseNotify is called while
	// processing an idempotent request (such as GET) while
	// HTTP/1.1 pipelining is in use, the arrival of a subsequent
	// pipelined request may cause a value to be sent on the
	// returned channel. In practice HTTP/1.1 pipelining is not
	// enabled in browsers and not seen often in the wild. If this
	// is a problem, use HTTP/2 or only use CloseNotify on methods
	// such as POST.
	CloseNotify() <-chan bool
}
```

The CloseNotifier interface is implemented by ResponseWriters which allow detecting when the underlying connection has gone away.

This mechanism can be used to cancel long operations on the server if the client has disconnected before the response is ready.

Deprecated: the CloseNotifier interface predates Go's context package. New code should use Request.Context instead.

```go
type ConnState int
```

A ConnState represents the state of a client connection to a server. It's used by the optional [Server.ConnState] hook.

```go
const (
	// StateNew represents a new connection that is expected to
	// send a request immediately. Connections begin at this
	// state and then transition to either StateActive or
	// StateClosed.
	StateNew ConnState = iota

// StateActive represents a connection that has read 1 or more
	// bytes of a request. The Server.ConnState hook for
	// StateActive fires before the request has entered a handler
	// and doesn't fire again until the request has been
	// handled. After the request is handled, the state
	// transitions to StateClosed, StateHijacked, or StateIdle.
	// For HTTP/2, StateActive fires on the transition from zero
	// to one active request, and only transitions away once all
	// active requests are complete. That means that ConnState
	// cannot be used to do per-request work; ConnState only notes
	// the overall state of the connection.
	StateActive

// StateIdle represents a connection that has finished
	// handling a request and is in the keep-alive state, waiting
	// for a new request. Connections transition from StateIdle
	// to either StateActive or StateClosed.
	StateIdle

// StateHijacked represents a hijacked connection.
	// This is a terminal state. It does not transition to StateClosed.
	StateHijacked

// StateClosed represents a closed connection.
	// This is a terminal state. Hijacked connections do not
	// transition to StateClosed.
	StateClosed
)
```

```go
func (c ConnState) String() string
```

```go
type Cookie struct {

// MaxAge=0 means no 'Max-Age' attribute specified.
	// MaxAge<0 means delete cookie now, equivalently 'Max-Age: 0'
	// MaxAge>0 means Max-Age attribute present and given in seconds
}
```

A Cookie represents an HTTP cookie as sent in the Set-Cookie header of an HTTP response or the Cookie header of an HTTP request.

See https://tools.ietf.org/html/rfc6265 <https://tools.ietf.org/html/rfc6265> for details.

```go
func ParseCookie(line string) ([]*Cookie, error)
```

ParseCookie parses a Cookie header value and returns all the cookies which were set in it. Since the same cookie name can appear multiple times the returned Values can contain more than one value for a given key.

```go
func ParseSetCookie(line string) (*Cookie, error)
```

ParseSetCookie parses a Set-Cookie header value and returns a cookie. It returns an error on syntax error.

```go
func (c *Cookie) String() string
```

String returns the serialization of the cookie for use in a Cookie header (if only Name and Value are set) or a Set-Cookie response header (if other fields are set). If c is nil or c.Name is invalid, the empty string is returned.

```go
func (c *Cookie) Valid() error
```

Valid reports whether the cookie is valid.

```go
type CookieJar interface {
	// given URL.  It may or may not choose to save the cookies, depending
	// on the jar's policy and implementation.
	SetCookies(u *url.URL, cookies []*Cookie)

// It is up to the implementation to honor the standard cookie use
	// restrictions such as in RFC 6265 <https://rfc-editor.org/rfc/rfc6265.html>.
	Cookies(u *url.URL) []*Cookie
}
```

A CookieJar manages storage and use of cookies in HTTP requests.

Implementations of CookieJar must be safe for concurrent use by multiple goroutines.

The net/http/cookiejar package provides a CookieJar implementation.

```go
type CrossOriginProtection struct {
	// contains filtered or unexported fields
}
```

CrossOriginProtection implements protections against Cross-Site Request Forgery (CSRF) <https://developer.mozilla.org/en-US/docs/Web/Security/Attacks/CSRF> by rejecting non-safe cross-origin browser requests.

Cross-origin requests are currently detected with the Sec-Fetch-Site <https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Sec-Fetch-Site> header, available in all browsers since 2023, or by comparing the hostname of the Origin <https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Origin> header with the Host header.

The GET, HEAD, and OPTIONS methods are safe methods <https://developer.mozilla.org/en-US/docs/Glossary/Safe/HTTP> and are always allowed. It's important that applications do not perform any state changing actions due to requests with safe methods.

Requests without Sec-Fetch-Site or Origin headers are currently assumed to be either same-origin or non-browser requests, and are allowed.

The zero value of CrossOriginProtection is valid and has no trusted origins or bypass patterns.

```go

package main

import (
	"io"
	"log"
	"net/http"
	"time"
)

func main() {
	mux := http.NewServeMux()

mux.HandleFunc("/hello", func(w http.ResponseWriter, req *http.Request) {
		io.WriteString(w, "request allowed\n")
	})

srv := http.Server{
		Addr:         ":8080",
		ReadTimeout:  15 * time.Second,
		WriteTimeout: 15 * time.Second,
		// Use CrossOriginProtection.Handler to block all non-safe cross-origin
		// browser requests to mux.
		Handler: http.NewCrossOriginProtection().Handler(mux),
	}

log.Fatal(srv.ListenAndServe())
}

```

```go
Output:

```

Share Format Run

```go
func NewCrossOriginProtection() *CrossOriginProtection
```

NewCrossOriginProtection returns a new CrossOriginProtection value.

```go
func (c *CrossOriginProtection) AddInsecureBypassPattern(pattern string)
```

AddInsecureBypassPattern permits all requests that match the given pattern.

The pattern syntax and precedence rules are the same as ServeMux. Only requests that match the pattern directly are permitted. Those that ServeMux would redirect to a pattern (e.g. after cleaning the path or adding a trailing slash) are not.

AddInsecureBypassPattern panics if the pattern conflicts with one already registered, or if the pattern is syntactically invalid (for example, an improperly formed wildcard).

AddInsecureBypassPattern can be called concurrently with other methods or request handling, and applies to future requests.

```go
func (c *CrossOriginProtection) AddTrustedOrigin(origin string) error
```

AddTrustedOrigin allows all requests with an Origin <https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Origin> header which exactly matches the given value.

Origin header values are of the form "scheme://host[:port]".

AddTrustedOrigin can be called concurrently with other methods or request handling, and applies to future requests.

```go
func (c *CrossOriginProtection) Check(req *Request) error
```

Check applies cross-origin checks to a request. It returns an error if the request should be rejected.

```go
func (c *CrossOriginProtection) Handler(h Handler) Handler
```

Handler returns a handler that applies cross-origin checks before invoking the handler h.

If a request fails cross-origin checks, the request is rejected with a 403 Forbidden status or handled with the handler passed to CrossOriginProtection.SetDenyHandler.

```go
func (c *CrossOriginProtection) SetDenyHandler(h Handler)
```

SetDenyHandler sets a handler to invoke when a request is rejected. The default error handler responds with a 403 Forbidden status.

SetDenyHandler can be called concurrently with other methods or request handling, and applies to future requests.

Check does not call the error handler.

```go
type Dir string
```

A Dir implements FileSystem using the native file system restricted to a specific directory tree.
