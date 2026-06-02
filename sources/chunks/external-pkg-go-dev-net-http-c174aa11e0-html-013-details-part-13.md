---
source_name: "External Linked Documentation"
source_url: "https://pkg.go.dev/net/http"
source_path: "sources/raw/external/pkg-go-dev-net-http-c174aa11e0.html"
license_ref: ""
---

// ConnContext optionally specifies a function that modifies
	// the context used for a new connection c. The provided ctx
	// is derived from the base context and has a ServerContextKey
	// value.
	ConnContext func(ctx context.Context, c net.Conn) context.Context

// HTTP2 configures HTTP/2 connections.
	HTTP2 *HTTP2Config

// Protocols is the set of protocols accepted by the server.
	//
	// If Protocols includes UnencryptedHTTP2, the server will accept
	// unencrypted HTTP/2 connections. The server can serve both
	// HTTP/1 and unencrypted HTTP/2 on the same address and port.
	//
	// If Protocols is nil, the default is usually HTTP/1 and HTTP/2.
	// If TLSNextProto is non-nil and does not contain an "h2" entry,
	// the default is HTTP/1 only.
	Protocols *Protocols
	// contains filtered or unexported fields
}
```

A Server defines parameters for running an HTTP server. The zero value for Server is a valid configuration.

```go
func (s *Server) Close() error
```

Close immediately closes all active net.Listeners and any connections in state StateNew, StateActive, or StateIdle. For a graceful shutdown, use Server.Shutdown.

Close does not attempt to close (and does not even know about) any hijacked connections, such as WebSockets.

Close returns any error returned from closing the Server's underlying Listener(s).

```go
func (s *Server) ListenAndServe() error
```

ListenAndServe listens on the TCP network address s.Addr and then calls Serve to handle requests on incoming connections. Accepted connections are configured to enable TCP keep-alives.

If s.Addr is blank, ":http" is used.

ListenAndServe always returns a non-nil error. After Server.Shutdown or Server.Close, the returned error is ErrServerClosed.

```go
func (s *Server) ListenAndServeTLS(certFile, keyFile string) error
```

ListenAndServeTLS listens on the TCP network address s.Addr and then calls ServeTLS to handle requests on incoming TLS connections. Accepted connections are configured to enable TCP keep-alives.

Filenames containing a certificate and matching private key for the server must be provided if neither the Server's TLSConfig.Certificates nor TLSConfig.GetCertificate are populated. If the certificate is signed by a certificate authority, the certFile should be the concatenation of the server's certificate, any intermediates, and the CA's certificate.

If s.Addr is blank, ":https" is used.

ListenAndServeTLS always returns a non-nil error. After Server.Shutdown or Server.Close, the returned error is ErrServerClosed.

```go
func (s *Server) RegisterOnShutdown(f func())
```

RegisterOnShutdown registers a function to call on Server.Shutdown. This can be used to gracefully shutdown connections that have undergone ALPN protocol upgrade or that have been hijacked. This function should start protocol-specific graceful shutdown, but should not wait for shutdown to complete.

```go
func (s *Server) Serve(l net.Listener) error
```

Serve accepts incoming connections on the Listener l, creating a new service goroutine for each. The service goroutines read requests and then call s.Handler to reply to them.

HTTP/2 support is only enabled if the Listener returns *tls.Conn connections and they were configured with "h2" in the TLS Config.NextProtos.

Serve always returns a non-nil error and closes l. After Server.Shutdown or Server.Close, the returned error is ErrServerClosed.

```go
func (s *Server) ServeTLS(l net.Listener, certFile, keyFile string) error
```

ServeTLS accepts incoming connections on the Listener l, creating a new service goroutine for each. The service goroutines perform TLS setup and then read requests, calling s.Handler to reply to them.

Files containing a certificate and matching private key for the server must be provided if neither the Server's TLSConfig.Certificates, TLSConfig.GetCertificate nor config.GetConfigForClient are populated. If the certificate is signed by a certificate authority, the certFile should be the concatenation of the server's certificate, any intermediates, and the CA's certificate.

ServeTLS always returns a non-nil error. After Server.Shutdown or Server.Close, the returned error is ErrServerClosed.

```go
func (s *Server) SetKeepAlivesEnabled(v bool)
```

SetKeepAlivesEnabled controls whether HTTP keep-alives are enabled. By default, keep-alives are always enabled. Only very resource-constrained environments or servers in the process of shutting down should disable them.

```go
func (s *Server) Shutdown(ctx context.Context) error
```

Shutdown gracefully shuts down the server without interrupting any active connections. Shutdown works by first closing all open listeners, then closing all idle connections, and then waiting indefinitely for connections to return to idle and then shut down. If the provided context expires before the shutdown is complete, Shutdown returns the context's error, otherwise it returns any error returned from closing the Server's underlying Listener(s).

When Shutdown is called, Serve, ServeTLS, ListenAndServe, and ListenAndServeTLS immediately return ErrServerClosed. Make sure the program doesn't exit and waits instead for Shutdown to return.

Shutdown does not attempt to close nor wait for hijacked connections such as WebSockets. The caller of Shutdown should separately notify such long-lived connections of shutdown and wait for them to close, if desired. See Server.RegisterOnShutdown for a way to register shutdown notification functions.

Once Shutdown has been called on a server, it may not be reused; future calls to methods such as Serve will return ErrServerClosed.

```go

package main

import (
	"context"
	"log"
	"net/http"
	"os"
	"os/signal"
)

func main() {
	var srv http.Server

idleConnsClosed := make(chan struct{})
	go func() {
		sigint := make(chan os.Signal, 1)
		signal.Notify(sigint, os.Interrupt)
		<-sigint

// We received an interrupt signal, shut down.
		if err := srv.Shutdown(context.Background()); err != nil {
			// Error from closing listeners, or context timeout:
			log.Printf("HTTP server Shutdown: %v", err)
		}
		close(idleConnsClosed)
	}()

if err := srv.ListenAndServe(); err != http.ErrServerClosed {
		// Error starting or closing listener:
		log.Fatalf("HTTP server ListenAndServe: %v", err)
	}

<-idleConnsClosed
}

```

```go
Output:

```

Share Format Run

```go
type Transport struct {

// Proxy specifies a function to return a proxy for a given
	// Request. If the function returns a non-nil error, the
	// request is aborted with the provided error.
	//
	// The proxy type is determined by the URL scheme. "http",
	// "https", "socks5", and "socks5h" are supported. If the scheme is empty,
	// "http" is assumed.
	// "socks5" is treated the same as "socks5h".
	//
	// If the proxy URL contains a userinfo subcomponent,
	// the proxy request will pass the username and password
	// in a Proxy-Authorization header.
	//
	// If Proxy is nil or returns a nil *URL, no proxy is used.
	Proxy func(*Request) (*url.URL, error)

// OnProxyConnectResponse is called when the Transport gets an HTTP response from
	// a proxy for a CONNECT request. It's called before the check for a 200 OK response.
	// If it returns an error, the request fails with that error.
	OnProxyConnectResponse func(ctx context.Context, proxyURL *url.URL, connectReq *Request, connectRes *Response) error

// DialContext specifies the dial function for creating unencrypted TCP connections.
	// If DialContext is nil (and the deprecated Dial below is also nil),
	// then the transport dials using package net.
	//
	// DialContext runs concurrently with calls to RoundTrip.
	// A RoundTrip call that initiates a dial may end up using
	// a connection dialed previously when the earlier connection
	// becomes idle before the later DialContext completes.
	DialContext func(ctx context.Context, network, addr string) (net.Conn, error)

// Dial specifies the dial function for creating unencrypted TCP connections.
	//
	// Dial runs concurrently with calls to RoundTrip.
	// A RoundTrip call that initiates a dial may end up using
	// a connection dialed previously when the earlier connection
	// becomes idle before the later Dial completes.
	//
	// Deprecated: Use DialContext instead, which allows the transport
	// to cancel dials as soon as they are no longer needed.
	// If both are set, DialContext takes priority.
	Dial func(network, addr string) (net.Conn, error)

// DialTLSContext specifies an optional dial function for creating
	// TLS connections for non-proxied HTTPS requests.
	//
	// If DialTLSContext is nil (and the deprecated DialTLS below is also nil),
	// DialContext and TLSClientConfig are used.
	//
	// If DialTLSContext is set, the Dial and DialContext hooks are not used for HTTPS
	// requests and the TLSClientConfig and TLSHandshakeTimeout
	// are ignored. The returned net.Conn is assumed to already be
	// past the TLS handshake.
	DialTLSContext func(ctx context.Context, network, addr string) (net.Conn, error)

// DialTLS specifies an optional dial function for creating
	// TLS connections for non-proxied HTTPS requests.
	//
	// Deprecated: Use DialTLSContext instead, which allows the transport
	// to cancel dials as soon as they are no longer needed.
	// If both are set, DialTLSContext takes priority.
	DialTLS func(network, addr string) (net.Conn, error)

// TLSClientConfig specifies the TLS configuration to use with
	// tls.Client.
	// If nil, the default configuration is used.
	// If non-nil, HTTP/2 support may not be enabled by default.
	TLSClientConfig *tls.Config

// TLSHandshakeTimeout specifies the maximum amount of time to
	// wait for a TLS handshake. Zero means no timeout.
	TLSHandshakeTimeout time.Duration

// DisableKeepAlives, if true, disables HTTP keep-alives and
	// will only use the connection to the server for a single
	// HTTP request.
	//
	// This is unrelated to the similarly named TCP keep-alives.
	DisableKeepAlives bool

// DisableCompression, if true, prevents the Transport from
	// requesting compression with an "Accept-Encoding: gzip"
	// request header when the Request contains no existing
	// Accept-Encoding value. If the Transport requests gzip on
	// its own and gets a gzipped response, it's transparently
	// decoded in the Response.Body. However, if the user
	// explicitly requested gzip it is not automatically
	// uncompressed.
	DisableCompression bool

// MaxIdleConns controls the maximum number of idle (keep-alive)
	// connections across all hosts. Zero means no limit.
	MaxIdleConns int

// MaxIdleConnsPerHost, if non-zero, controls the maximum idle
	// (keep-alive) connections to keep per-host. If zero,
	// DefaultMaxIdleConnsPerHost is used.
	MaxIdleConnsPerHost int

// MaxConnsPerHost optionally limits the total number of
	// connections per host, including connections in the dialing,
	// active, and idle states. On limit violation, dials will block.
	//
	// Zero means no limit.
	MaxConnsPerHost int
