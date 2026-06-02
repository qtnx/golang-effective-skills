---
source_name: "External Linked Documentation"
source_url: "https://pkg.go.dev/net/http"
source_path: "sources/raw/external/pkg-go-dev-net-http-c174aa11e0.html"
license_ref: ""
---

View Source <https://cs.opensource.google/go/go/+/go1.26.3:src/net/http/method.go;l=10>
```go
const (
	MethodGet     = "GET"
	MethodHead    = "HEAD"
	MethodPost    = "POST"
	MethodPut     = "PUT"
	MethodPatch   = "PATCH" // RFC 5789 <https://rfc-editor.org/rfc/rfc5789.html>
	MethodDelete  = "DELETE"
	MethodConnect = "CONNECT"
	MethodOptions = "OPTIONS"
	MethodTrace   = "TRACE"
)
```

Common HTTP methods.

Unless otherwise noted, these are defined in RFC 7231 section 4.3 <https://rfc-editor.org/rfc/rfc7231.html#section-4.3>.
  View Source <https://cs.opensource.google/go/go/+/go1.26.3:src/net/http/status.go;l=9>
```go
const (
	StatusContinue           = 100 // RFC 9110 <https://rfc-editor.org/rfc/rfc9110.html>, 15.2.1
	StatusSwitchingProtocols = 101 // RFC 9110 <https://rfc-editor.org/rfc/rfc9110.html>, 15.2.2
	StatusProcessing         = 102 // RFC 2518 <https://rfc-editor.org/rfc/rfc2518.html>, 10.1
	StatusEarlyHints         = 103 // RFC 8297 <https://rfc-editor.org/rfc/rfc8297.html>

StatusOK                   = 200 // RFC 9110 <https://rfc-editor.org/rfc/rfc9110.html>, 15.3.1
	StatusCreated              = 201 // RFC 9110 <https://rfc-editor.org/rfc/rfc9110.html>, 15.3.2
	StatusAccepted             = 202 // RFC 9110 <https://rfc-editor.org/rfc/rfc9110.html>, 15.3.3
	StatusNonAuthoritativeInfo = 203 // RFC 9110 <https://rfc-editor.org/rfc/rfc9110.html>, 15.3.4
	StatusNoContent            = 204 // RFC 9110 <https://rfc-editor.org/rfc/rfc9110.html>, 15.3.5
	StatusResetContent         = 205 // RFC 9110 <https://rfc-editor.org/rfc/rfc9110.html>, 15.3.6
	StatusPartialContent       = 206 // RFC 9110 <https://rfc-editor.org/rfc/rfc9110.html>, 15.3.7
	StatusMultiStatus          = 207 // RFC 4918 <https://rfc-editor.org/rfc/rfc4918.html>, 11.1
	StatusAlreadyReported      = 208 // RFC 5842 <https://rfc-editor.org/rfc/rfc5842.html>, 7.1
	StatusIMUsed               = 226 // RFC 3229 <https://rfc-editor.org/rfc/rfc3229.html>, 10.4.1

StatusMultipleChoices  = 300 // RFC 9110 <https://rfc-editor.org/rfc/rfc9110.html>, 15.4.1
	StatusMovedPermanently = 301 // RFC 9110 <https://rfc-editor.org/rfc/rfc9110.html>, 15.4.2
	StatusFound            = 302 // RFC 9110 <https://rfc-editor.org/rfc/rfc9110.html>, 15.4.3
	StatusSeeOther         = 303 // RFC 9110 <https://rfc-editor.org/rfc/rfc9110.html>, 15.4.4
	StatusNotModified      = 304 // RFC 9110 <https://rfc-editor.org/rfc/rfc9110.html>, 15.4.5
	StatusUseProxy         = 305 // RFC 9110 <https://rfc-editor.org/rfc/rfc9110.html>, 15.4.6

StatusTemporaryRedirect = 307 // RFC 9110 <https://rfc-editor.org/rfc/rfc9110.html>, 15.4.8
	StatusPermanentRedirect = 308 // RFC 9110 <https://rfc-editor.org/rfc/rfc9110.html>, 15.4.9

StatusBadRequest                   = 400 // RFC 9110 <https://rfc-editor.org/rfc/rfc9110.html>, 15.5.1
	StatusUnauthorized                 = 401 // RFC 9110 <https://rfc-editor.org/rfc/rfc9110.html>, 15.5.2
	StatusPaymentRequired              = 402 // RFC 9110 <https://rfc-editor.org/rfc/rfc9110.html>, 15.5.3
	StatusForbidden                    = 403 // RFC 9110 <https://rfc-editor.org/rfc/rfc9110.html>, 15.5.4
	StatusNotFound                     = 404 // RFC 9110 <https://rfc-editor.org/rfc/rfc9110.html>, 15.5.5
	StatusMethodNotAllowed             = 405 // RFC 9110 <https://rfc-editor.org/rfc/rfc9110.html>, 15.5.6
	StatusNotAcceptable                = 406 // RFC 9110 <https://rfc-editor.org/rfc/rfc9110.html>, 15.5.7
	StatusProxyAuthRequired            = 407 // RFC 9110 <https://rfc-editor.org/rfc/rfc9110.html>, 15.5.8
	StatusRequestTimeout               = 408 // RFC 9110 <https://rfc-editor.org/rfc/rfc9110.html>, 15.5.9
	StatusConflict                     = 409 // RFC 9110 <https://rfc-editor.org/rfc/rfc9110.html>, 15.5.10
	StatusGone                         = 410 // RFC 9110 <https://rfc-editor.org/rfc/rfc9110.html>, 15.5.11
	StatusLengthRequired               = 411 // RFC 9110 <https://rfc-editor.org/rfc/rfc9110.html>, 15.5.12
	StatusPreconditionFailed           = 412 // RFC 9110 <https://rfc-editor.org/rfc/rfc9110.html>, 15.5.13
	StatusRequestEntityTooLarge        = 413 // RFC 9110 <https://rfc-editor.org/rfc/rfc9110.html>, 15.5.14
	StatusRequestURITooLong            = 414 // RFC 9110 <https://rfc-editor.org/rfc/rfc9110.html>, 15.5.15
	StatusUnsupportedMediaType         = 415 // RFC 9110 <https://rfc-editor.org/rfc/rfc9110.html>, 15.5.16
	StatusRequestedRangeNotSatisfiable = 416 // RFC 9110 <https://rfc-editor.org/rfc/rfc9110.html>, 15.5.17
	StatusExpectationFailed            = 417 // RFC 9110 <https://rfc-editor.org/rfc/rfc9110.html>, 15.5.18
	StatusTeapot                       = 418 // RFC 9110 <https://rfc-editor.org/rfc/rfc9110.html>, 15.5.19 (Unused)
	StatusMisdirectedRequest           = 421 // RFC 9110 <https://rfc-editor.org/rfc/rfc9110.html>, 15.5.20
	StatusUnprocessableEntity          = 422 // RFC 9110 <https://rfc-editor.org/rfc/rfc9110.html>, 15.5.21
	StatusLocked                       = 423 // RFC 4918 <https://rfc-editor.org/rfc/rfc4918.html>, 11.3
	StatusFailedDependency             = 424 // RFC 4918 <https://rfc-editor.org/rfc/rfc4918.html>, 11.4
	StatusTooEarly                     = 425 // RFC 8470 <https://rfc-editor.org/rfc/rfc8470.html>, 5.2.
	StatusUpgradeRequired              = 426 // RFC 9110 <https://rfc-editor.org/rfc/rfc9110.html>, 15.5.22
	StatusPreconditionRequired         = 428 // RFC 6585 <https://rfc-editor.org/rfc/rfc6585.html>, 3
	StatusTooManyRequests              = 429 // RFC 6585 <https://rfc-editor.org/rfc/rfc6585.html>, 4
	StatusUnavailableForLegalReasons   = 451 // RFC 7725 <https://rfc-editor.org/rfc/rfc7725.html>, 3

StatusInternalServerError           = 500 // RFC 9110 <https://rfc-editor.org/rfc/rfc9110.html>, 15.6.1
	StatusNotImplemented                = 501 // RFC 9110 <https://rfc-editor.org/rfc/rfc9110.html>, 15.6.2
	StatusBadGateway                    = 502 // RFC 9110 <https://rfc-editor.org/rfc/rfc9110.html>, 15.6.3
	StatusServiceUnavailable            = 503 // RFC 9110 <https://rfc-editor.org/rfc/rfc9110.html>, 15.6.4
	StatusGatewayTimeout                = 504 // RFC 9110 <https://rfc-editor.org/rfc/rfc9110.html>, 15.6.5
	StatusHTTPVersionNotSupported       = 505 // RFC 9110 <https://rfc-editor.org/rfc/rfc9110.html>, 15.6.6
	StatusVariantAlsoNegotiates         = 506 // RFC 2295 <https://rfc-editor.org/rfc/rfc2295.html>, 8.1
	StatusInsufficientStorage           = 507 // RFC 4918 <https://rfc-editor.org/rfc/rfc4918.html>, 11.5
	StatusLoopDetected                  = 508 // RFC 5842 <https://rfc-editor.org/rfc/rfc5842.html>, 7.2
	StatusNotExtended                   = 510 // RFC 2774 <https://rfc-editor.org/rfc/rfc2774.html>, 7
	StatusNetworkAuthenticationRequired = 511 // RFC 6585 <https://rfc-editor.org/rfc/rfc6585.html>, 6
)
```

HTTP status codes as registered with IANA. See: https://www.iana.org/assignments/http-status-codes/http-status-codes.xhtml <https://www.iana.org/assignments/http-status-codes/http-status-codes.xhtml>
  View Source <https://cs.opensource.google/go/go/+/go1.26.3:src/net/http/server.go;l=895>
```go

```

DefaultMaxHeaderBytes is the maximum permitted size of the headers in an HTTP request. This can be overridden by setting [Server.MaxHeaderBytes].
  View Source <https://cs.opensource.google/go/go/+/go1.26.3:src/net/http/transport.go;l=61>
```go
const DefaultMaxIdleConnsPerHost = 2
```

DefaultMaxIdleConnsPerHost is the default value of Transport's MaxIdleConnsPerHost.
  View Source <https://cs.opensource.google/go/go/+/go1.26.3:src/net/http/server.go;l=971>
```go
const TimeFormat = "Mon, 02 Jan 2006 15:04:05 GMT"
```

TimeFormat is the time format to use when generating times in HTTP headers. It is like time.RFC1123 but hard-codes GMT as the time zone. The time being formatted must be in UTC for Format to generate the correct format.

For parsing this time format, see ParseTime.
  View Source <https://cs.opensource.google/go/go/+/go1.26.3:src/net/http/server.go;l=525>
```go
const TrailerPrefix = "Trailer:"
```

TrailerPrefix is a magic prefix for [ResponseWriter.Header] map keys that, if present, signals that the map entry is actually for the response trailers, and not the response headers. The prefix is stripped after the ServeHTTP call finishes and the values are sent in the trailers.

This mechanism is intended only for trailers that are not known prior to the headers being written. If the set of trailers is fixed or known before the header is written, the normal Go trailers mechanism is preferred:

```go
https://pkg.go.dev/net/http#ResponseWriter
https://pkg.go.dev/net/http#example-ResponseWriter-Trailers

```

View Source <https://cs.opensource.google/go/go/+/go1.26.3:src/net/http/request.go;l=58>
```go
var (
	// ErrNotSupported indicates that a feature is not supported.
	//
	// It is returned by ResponseController methods to indicate that
	// the handler does not support the method, and by the Push method
	// of Pusher implementations to indicate that HTTP/2 Push support
	// is not available.
	ErrNotSupported = &ProtocolError{"feature not supported"}

// Deprecated: ErrUnexpectedTrailer is no longer returned by
	// anything in the net/http package. Callers should not
	// compare errors against this variable.
	ErrUnexpectedTrailer = &ProtocolError{"trailer header without chunked transfer encoding"}

// ErrMissingBoundary is returned by Request.MultipartReader when the
	// request's Content-Type does not include a "boundary" parameter.
	ErrMissingBoundary = &ProtocolError{"no multipart boundary param in Content-Type"}

// ErrNotMultipart is returned by Request.MultipartReader when the
	// request's Content-Type is not multipart/form-data.
	ErrNotMultipart = &ProtocolError{"request Content-Type isn't multipart/form-data"}

// anything in the net/http package. Callers should not
	// compare errors against this variable.
	ErrHeaderTooLong = &ProtocolError{"header too long"}

// Deprecated: ErrShortBody is no longer returned by
	// anything in the net/http package. Callers should not
	// compare errors against this variable.
	ErrShortBody = &ProtocolError{"entity body too short"}

// Deprecated: ErrMissingContentLength is no longer returned by
	// anything in the net/http package. Callers should not
	// compare errors against this variable.
	ErrMissingContentLength = &ProtocolError{"missing ContentLength in HEAD response"}
)
```

View Source <https://cs.opensource.google/go/go/+/go1.26.3:src/net/http/server.go;l=39>
```go
var (
	// ErrBodyNotAllowed is returned by ResponseWriter.Write calls
	// when the HTTP method or response code does not permit a
	// body.
	ErrBodyNotAllowed = errors.New("http: request method or response status code does not allow body")

// ErrHijacked is returned by ResponseWriter.Write calls when
	// the underlying connection has been hijacked using the
	// Hijacker interface. A zero-byte write on a hijacked
	// connection will return ErrHijacked without any other side
	// effects.
	ErrHijacked = errors.New("http: connection has been hijacked")

// ErrContentLength is returned by ResponseWriter.Write calls
	// when a Handler set a Content-Length response header with a
	// declared size and then attempted to write more bytes than
	// declared.
	ErrContentLength = errors.New("http: wrote more than the declared Content-Length")

// Deprecated: ErrWriteAfterFlush is no longer returned by
	// anything in the net/http package. Callers should not
	// compare errors against this variable.
	ErrWriteAfterFlush = errors.New("unused")
)
```

Errors used by the HTTP server.
  View Source <https://cs.opensource.google/go/go/+/go1.26.3:src/net/http/server.go;l=239>
```go
var (
	// ServerContextKey is a context key. It can be used in HTTP
	// handlers with Context.Value to access the server that
	// started the handler. The associated value will be of
	// type *Server.
	ServerContextKey = &contextKey{"http-server"}

// LocalAddrContextKey is a context key. It can be used in
	// HTTP handlers with Context.Value to access the local
	// address the connection arrived on.
	// The associated value will be of type net.Addr.
	LocalAddrContextKey = &contextKey{"local-addr"}
)
```

View Source <https://cs.opensource.google/go/go/+/go1.26.3:src/net/http/client.go;l=109>
```go
var DefaultClient = &Client{}
```

DefaultClient is the default Client and is used by Get, Head, and Post.
  View Source <https://cs.opensource.google/go/go/+/go1.26.3:src/net/http/server.go;l=2588>
```go
var DefaultServeMux = &defaultServeMux
```

DefaultServeMux is the default ServeMux used by Serve.
  View Source <https://cs.opensource.google/go/go/+/go1.26.3:src/net/http/server.go;l=1873>
```go
var ErrAbortHandler = errors.New("net/http: abort Handler")
```

ErrAbortHandler is a sentinel panic value to abort a handler. While any panic from ServeHTTP aborts the response to the client, panicking with ErrAbortHandler also suppresses logging of a stack trace to the server's error log.
  View Source <https://cs.opensource.google/go/go/+/go1.26.3:src/net/http/transfer.go;l=829>
```go
var ErrBodyReadAfterClose = errors.New("http: invalid Read on closed Body")
```

ErrBodyReadAfterClose is returned when reading a Request or Response Body after the body has been closed. This typically happens when the body is read after an HTTP Handler calls WriteHeader or Write on its ResponseWriter.
  View Source <https://cs.opensource.google/go/go/+/go1.26.3:src/net/http/server.go;l=3797>
```go
var ErrHandlerTimeout = errors.New("http: Handler timeout")
```

ErrHandlerTimeout is returned on ResponseWriter Write calls in handlers which have timed out.
  View Source <https://cs.opensource.google/go/go/+/go1.26.3:src/net/http/transfer.go;l=31>
```go
var ErrLineTooLong = internal.ErrLineTooLong
```

ErrLineTooLong is returned when reading request or response bodies with malformed chunked encoding.
  View Source <https://cs.opensource.google/go/go/+/go1.26.3:src/net/http/request.go;l=41>
```go
var ErrMissingFile = errors.New("http: no such file")
```

ErrMissingFile is returned by FormFile when the provided file field name is either not present in the request or not a file field.
  View Source <https://cs.opensource.google/go/go/+/go1.26.3:src/net/http/request.go;l=442>
```go

```

ErrNoCookie is returned by Request's Cookie method when a cookie is not found.
  View Source <https://cs.opensource.google/go/go/+/go1.26.3:src/net/http/response.go;l=131>
```go
var ErrNoLocation = errors.New("http: no Location header in response")
```

ErrNoLocation is returned by the Response.Location method when no Location header is present.
  View Source <https://cs.opensource.google/go/go/+/go1.26.3:src/net/http/client.go;l=212>
```go
var ErrSchemeMismatch = errors.New("http: server gave HTTP response to HTTPS client")
```

ErrSchemeMismatch is returned when a server returns an HTTP response to an HTTPS client.
  View Source <https://cs.opensource.google/go/go/+/go1.26.3:src/net/http/server.go;l=3392>
```go
var ErrServerClosed = errors.New("http: Server closed")
```

ErrServerClosed is returned by the Server.Serve, ServeTLS, ListenAndServe, and ListenAndServeTLS methods after a call to Server.Shutdown or Server.Close.
  View Source <https://cs.opensource.google/go/go/+/go1.26.3:src/net/http/transport.go;l=866>
```go

```

ErrSkipAltProtocol is a sentinel error value defined by Transport.RegisterProtocol.
  View Source <https://cs.opensource.google/go/go/+/go1.26.3:src/net/http/client.go;l=498>
```go
var ErrUseLastResponse = errors.New("net/http: use last response")
```
