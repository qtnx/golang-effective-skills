---
source_name: "External Linked Documentation"
source_url: "https://pkg.go.dev/net/http"
source_path: "sources/raw/external/pkg-go-dev-net-http-c174aa11e0.html"
license_ref: ""
---

// IdleConnTimeout is the maximum amount of time an idle
	// (keep-alive) connection will remain idle before closing
	// itself.
	// Zero means no limit.
	IdleConnTimeout time.Duration

// time to wait for a server's response headers after fully
	// writing the request (including its body, if any). This
	// time does not include the time to read the response body.
	ResponseHeaderTimeout time.Duration

// ExpectContinueTimeout, if non-zero, specifies the amount of
	// time to wait for a server's first response headers after fully
	// writing the request headers if the request has an
	// "Expect: 100-continue" header. Zero means no timeout and
	// causes the body to be sent immediately, without
	// waiting for the server to approve.
	// This time does not include the time to send the request header.
	ExpectContinueTimeout time.Duration

// TLSNextProto specifies how the Transport switches to an
	// alternate protocol (such as HTTP/2) after a TLS ALPN
	// protocol negotiation. If Transport dials a TLS connection
	// with a non-empty protocol name and TLSNextProto contains a
	// map entry for that key (such as "h2"), then the func is
	// called with the request's authority (such as "example.com"
	// or "example.com:1234") and the TLS connection. The function
	// must return a RoundTripper that then handles the request.
	// If TLSNextProto is not nil, HTTP/2 support is not enabled
	// automatically.
	//
	// Historically, TLSNextProto was used to disable HTTP/2 support.
	// The Transport.Protocols field now provides a simpler way to do this.
	TLSNextProto map[string]func(authority string, c *tls.Conn) RoundTripper

// proxies during CONNECT requests.
	// To set the header dynamically, see GetProxyConnectHeader.
	ProxyConnectHeader Header

// headers to send to proxyURL during a CONNECT request to the
	// ip:port target.
	// If it returns an error, the Transport's RoundTrip fails with
	// that error. It can return (nil, nil) to not add headers.
	// If GetProxyConnectHeader is non-nil, ProxyConnectHeader is
	// ignored.
	GetProxyConnectHeader func(ctx context.Context, proxyURL *url.URL, target string) (Header, error)

// response bytes are allowed in the server's response
	// header.
	//
	// Zero means to use a default limit.
	MaxResponseHeaderBytes int64

// WriteBufferSize specifies the size of the write buffer used
	// when writing to the transport.
	// If zero, a default (currently 4KB) is used.
	WriteBufferSize int

// ReadBufferSize specifies the size of the read buffer used
	// when reading from the transport.
	// If zero, a default (currently 4KB) is used.
	ReadBufferSize int

// ForceAttemptHTTP2 controls whether HTTP/2 is enabled when a non-zero
	// Dial, DialTLS, or DialContext func or TLSClientConfig is provided.
	// By default, use of any those fields conservatively disables HTTP/2.
	// To use a custom dialer or TLS config and still attempt HTTP/2
	// upgrades, set this to true.
	ForceAttemptHTTP2 bool

// HTTP2 configures HTTP/2 connections.
	HTTP2 *HTTP2Config

// Protocols is the set of protocols supported by the transport.
	//
	// If Protocols includes UnencryptedHTTP2 and does not include HTTP1,
	// the transport will use unencrypted HTTP/2 for requests for http:// URLs.
	//
	// If Protocols is nil, the default is usually HTTP/1 only.
	// If ForceAttemptHTTP2 is true, or if TLSNextProto contains an "h2" entry,
	// the default is HTTP/1 and HTTP/2.
	Protocols *Protocols
	// contains filtered or unexported fields
}
```

Transport is an implementation of RoundTripper that supports HTTP, HTTPS, and HTTP proxies (for either HTTP or HTTPS with CONNECT).

By default, Transport caches connections for future re-use. This may leave many open connections when accessing many hosts. This behavior can be managed using Transport.CloseIdleConnections method and the [Transport.MaxIdleConnsPerHost] and [Transport.DisableKeepAlives] fields.

Transports should be reused instead of created as needed. Transports are safe for concurrent use by multiple goroutines.

A Transport is a low-level primitive for making HTTP and HTTPS requests. For high-level functionality, such as cookies and redirects, see Client.

Transport uses HTTP/1.1 for HTTP URLs and either HTTP/1.1 or HTTP/2 for HTTPS URLs, depending on whether the server supports HTTP/2, and how the Transport is configured. The DefaultTransport supports HTTP/2. To explicitly enable HTTP/2 on a transport, set [Transport.Protocols].

Responses with status codes in the 1xx range are either handled automatically (100 expect-continue) or ignored. The one exception is HTTP status code 101 (Switching Protocols), which is considered a terminal status and returned by Transport.RoundTrip. To see the ignored 1xx responses, use the httptrace trace package's ClientTrace.Got1xxResponse.

Transport only retries a request upon encountering a network error if the connection has already been used successfully and if the request is idempotent and either has no body or has its [Request.GetBody] defined. HTTP requests are considered idempotent if they have HTTP methods GET, HEAD, OPTIONS, or TRACE; or if their Header map contains an "Idempotency-Key" or "X-Idempotency-Key" entry. If the idempotency key value is a zero-length slice, the request is treated as idempotent but the header is not sent on the wire.

```go
func (t *Transport) CancelRequest(req *Request)
```

CancelRequest cancels an in-flight request by closing its connection. CancelRequest should only be called after Transport.RoundTrip has returned.

Deprecated: Use Request.WithContext to create a request with a cancelable context instead. CancelRequest cannot cancel HTTP/2 requests. This may become a no-op in a future release of Go.

```go
func (t *Transport) Clone() *Transport
```

Clone returns a deep copy of t's exported fields.

```go
func (t *Transport) CloseIdleConnections()
```

CloseIdleConnections closes any connections which were previously connected from previous requests but are now sitting idle in a "keep-alive" state. It does not interrupt any connections currently in use.

```go
func (t *Transport) NewClientConn(ctx context.Context, scheme, address string) (*ClientConn, error)
```

NewClientConn creates a new client connection to the given address.

If scheme is "http", the connection is unencrypted. If scheme is "https", the connection uses TLS.

The protocol used for the new connection is determined by the scheme, Transport.Protocols configuration field, and protocols supported by the server. See Transport.Protocols for more details.

If Transport.Proxy is set and indicates that a request sent to the given address should use a proxy, the new connection uses that proxy.

NewClientConn always creates a new connection, even if the Transport has an existing cached connection to the given host.

The new connection is not added to the Transport's connection cache, and will not be used by Transport.RoundTrip. It does not count against the MaxIdleConns and MaxConnsPerHost limits.

The caller is responsible for closing the new connection.

```go
func (t *Transport) RegisterProtocol(scheme string, rt RoundTripper)
```

RegisterProtocol registers a new protocol with scheme. The Transport will pass requests using the given scheme to rt. It is rt's responsibility to simulate HTTP request semantics.

RegisterProtocol can be used by other packages to provide implementations of protocol schemes like "ftp" or "file".

If rt.RoundTrip returns ErrSkipAltProtocol, the Transport will handle the Transport.RoundTrip itself for that one request, as if the protocol were not registered.

```go
func (t *Transport) RoundTrip(req *Request) (*Response, error)
```

RoundTrip implements the RoundTripper interface.

For higher-level HTTP client support (such as handling of cookies and redirects), see Get, Post, and the Client type.

Like the RoundTripper interface, the error types returned by RoundTrip are unspecified.
