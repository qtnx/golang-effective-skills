---
source_name: "External Linked Documentation"
source_url: "https://pkg.go.dev/net/http"
source_path: "sources/raw/external/pkg-go-dev-net-http-c174aa11e0.html"
license_ref: ""
---

For matching, both pattern paths and incoming request paths are unescaped segment by segment. So, for example, the path "/a%2Fb/100%25" is treated as having two segments, "a/b" and "100%". The pattern "/a%2fb/" matches it, but the pattern "/a/b/" does not.

#### Precedence ¶

If two or more patterns match a request, then the most specific pattern takes precedence. A pattern P1 is more specific than P2 if P1 matches a strict subset of P2’s requests; that is, if P2 matches all the requests of P1 and more. If neither is more specific, then the patterns conflict. There is one exception to this rule, for backwards compatibility: if two patterns would otherwise conflict and one has a host while the other does not, then the pattern with the host takes precedence. If a pattern passed to ServeMux.Handle or ServeMux.HandleFunc conflicts with another pattern that is already registered, those functions panic.

As an example of the general rule, "/images/thumbnails/" is more specific than "/images/", so both can be registered. The former matches paths beginning with "/images/thumbnails/" and the latter will match any other path in the "/images/" subtree.

As another example, consider the patterns "GET /" and "/index.html": both match a GET request for "/index.html", but the former pattern matches all other GET and HEAD requests, while the latter matches any request for "/index.html" that uses a different method. The patterns conflict.

#### Trailing-slash redirection ¶

Consider a ServeMux with a handler for a subtree, registered using a trailing slash or "..." wildcard. If the ServeMux receives a request for the subtree root without a trailing slash, it redirects the request by adding the trailing slash. This behavior can be overridden with a separate registration for the path without the trailing slash or "..." wildcard. For example, registering "/images/" causes ServeMux to redirect a request for "/images" to "/images/", unless "/images" has been registered separately.

#### Request sanitizing ¶

ServeMux also takes care of sanitizing the URL request path and the Host header, stripping the port number and redirecting any request containing . or .. segments or repeated slashes to an equivalent, cleaner URL. Escaped path elements such as "%2e" for "." and "%2f" for "/" are preserved and aren't considered separators for request routing.

#### Compatibility ¶

The pattern syntax and matching behavior of ServeMux changed significantly in Go 1.22. To restore the old behavior, set the GODEBUG environment variable to "httpmuxgo121=1". This setting is read once, at program startup; changes during execution will be ignored.

The backwards-incompatible changes include:

- Wildcards are just ordinary literal path segments in 1.21. For example, the pattern "/{x}" will match only that path in 1.21, but will match any one-segment path in 1.22.
- In 1.21, no pattern was rejected, unless it was empty or conflicted with an existing pattern. In 1.22, syntactically invalid patterns will cause ServeMux.Handle and ServeMux.HandleFunc to panic. For example, in 1.21, the patterns "/{" and "/a{x}" match themselves, but in 1.22 they are invalid and will cause a panic when registered.
- In 1.22, each segment of a pattern is unescaped; this was not done in 1.21. For example, in 1.22 the pattern "/%61" matches the path "/a" ("%61" being the URL escape sequence for "a"), but in 1.21 it would match only the path "/%2561" (where "%25" is the escape for the percent sign).
- When matching patterns to paths, in 1.22 each segment of the path is unescaped; in 1.21, the entire path is unescaped. This change mostly affects how paths with %2F escapes adjacent to slashes are treated. See https://go.dev/issue/21955 <https://go.dev/issue/21955> for details.

```go
func NewServeMux() *ServeMux
```

NewServeMux allocates and returns a new ServeMux.

```go
func (mux *ServeMux) Handle(pattern string, handler Handler)
```

Handle registers the handler for the given pattern. If the given pattern conflicts with one that is already registered or if the pattern is invalid, Handle panics.

See ServeMux for details on valid patterns and conflict rules.

```go

package main

import (
	"fmt"
	"net/http"
)

type apiHandler struct{}

func (apiHandler) ServeHTTP(http.ResponseWriter, *http.Request) {}

func main() {
	mux := http.NewServeMux()
	mux.Handle("/api/", apiHandler{})
	mux.HandleFunc("/", func(w http.ResponseWriter, req *http.Request) {
		// The "/" pattern matches everything, so we need to check
		// that we're at the root here.
		if req.URL.Path != "/" {
			http.NotFound(w, req)
			return
		}
		fmt.Fprintf(w, "Welcome to the home page!")
	})
}

```

```go
Output:

```

Share Format Run

```go
func (mux *ServeMux) HandleFunc(pattern string, handler func(ResponseWriter, *Request))
```

HandleFunc registers the handler function for the given pattern. If the given pattern conflicts with one that is already registered or if the pattern is invalid, HandleFunc panics.

See ServeMux for details on valid patterns and conflict rules.

```go
func (mux *ServeMux) Handler(r *Request) (h Handler, pattern string)
```

Handler returns the handler to use for the given request, consulting r.Method, r.Host, and r.URL.Path. It always returns a non-nil handler. If the path is not in its canonical form, the handler will be an internally-generated handler that redirects to the canonical path. If the host contains a port, it is ignored when matching handlers.

The path and host are used unchanged for CONNECT requests.

Handler also returns the registered pattern that matches the request or, in the case of internally-generated redirects, the path that will match after following the redirect.

If there is no registered handler that applies to the request, Handler returns a “page not found” or “method not supported” handler and an empty pattern.

Handler does not modify its argument. In particular, it does not populate named path wildcards, so r.PathValue will always return the empty string.

```go
func (mux *ServeMux) ServeHTTP(w ResponseWriter, r *Request)
```

ServeHTTP dispatches the request to the handler whose pattern most closely matches the request URL.

```go
type Server struct {
	// Addr optionally specifies the TCP address for the server to listen on,
	// in the form "host:port". If empty, ":http" (port 80) is used.
	// The service names are defined in RFC 6335 <https://rfc-editor.org/rfc/rfc6335.html> and assigned by IANA.
	// See net.Dial for details of the address format.
	Addr string

Handler Handler // handler to invoke, http.DefaultServeMux if nil

// DisableGeneralOptionsHandler, if true, passes "OPTIONS *" requests to the Handler,
	// otherwise responds with 200 OK and Content-Length: 0.
	DisableGeneralOptionsHandler bool

// TLSConfig optionally provides a TLS configuration for use
	// by ServeTLS and ListenAndServeTLS. Note that this value is
	// cloned by ServeTLS and ListenAndServeTLS, so it's not
	// possible to modify the configuration with methods like
	// tls.Config.SetSessionTicketKeys. To use
	// SetSessionTicketKeys, use Server.Serve with a TLS Listener
	// instead.
	TLSConfig *tls.Config

// ReadTimeout is the maximum duration for reading the entire
	// request, including the body. A zero or negative value means
	// there will be no timeout.
	//
	// Because ReadTimeout does not let Handlers make per-request
	// decisions on each request body's acceptable deadline or
	// upload rate, most users will prefer to use
	// ReadHeaderTimeout. It is valid to use them both.
	ReadTimeout time.Duration

// request headers. The connection's read deadline is reset
	// after reading the headers and the Handler can decide what
	// is considered too slow for the body. If zero, the value of
	// ReadTimeout is used. If negative, or if zero and ReadTimeout
	// is zero or negative, there is no timeout.
	ReadHeaderTimeout time.Duration

// WriteTimeout is the maximum duration before timing out
	// writes of the response. It is reset whenever a new
	// request's header is read. Like ReadTimeout, it does not
	// let Handlers make decisions on a per-request basis.
	// A zero or negative value means there will be no timeout.
	WriteTimeout time.Duration

// IdleTimeout is the maximum amount of time to wait for the
	// next request when keep-alives are enabled. If zero, the value
	// of ReadTimeout is used. If negative, or if zero and ReadTimeout
	// is zero or negative, there is no timeout.
	IdleTimeout time.Duration

// server will read parsing the request header's keys and
	// values, including the request line. It does not limit the
	// size of the request body.
	// If zero, DefaultMaxHeaderBytes is used.
	MaxHeaderBytes int

// TLSNextProto optionally specifies a function to take over
	// ownership of the provided TLS connection when an ALPN
	// protocol upgrade has occurred. The map key is the protocol
	// name negotiated. The Handler argument should be used to
	// handle HTTP requests and will initialize the Request's TLS
	// and RemoteAddr if not already set. The connection is
	// automatically closed when the function returns.
	// If TLSNextProto is not nil, HTTP/2 support is not enabled
	// automatically.
	//
	// Historically, TLSNextProto was used to disable HTTP/2 support.
	// The Server.Protocols field now provides a simpler way to do this.
	TLSNextProto map[string]func(*Server, *tls.Conn, Handler)

// ConnState specifies an optional callback function that is
	// called when a client connection changes state. See the
	// ConnState type and associated constants for details.
	ConnState func(net.Conn, ConnState)

// ErrorLog specifies an optional logger for errors accepting
	// connections, unexpected behavior from handlers, and
	// underlying FileSystem errors.
	// If nil, logging is done via the log package's standard logger.
	ErrorLog *log.Logger

// BaseContext optionally specifies a function that returns
	// the base context for incoming requests on this server.
	// The provided Listener is the specific Listener that's
	// about to start accepting requests.
	// If BaseContext is nil, the default is context.Background().
	// If non-nil, it must return a non-nil context.
	BaseContext func(net.Listener) context.Context
