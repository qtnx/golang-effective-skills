---
source_name: "External Linked Documentation"
source_url: "https://pkg.go.dev/net/http"
source_path: "sources/raw/external/pkg-go-dev-net-http-c174aa11e0.html"
license_ref: ""
---

While the [FileSystem.Open] method takes '/'-separated paths, a Dir's string value is a directory path on the native file system, not a URL, so it is separated by filepath.Separator, which isn't necessarily '/'.

Note that Dir could expose sensitive files and directories. Dir will follow symlinks pointing out of the directory tree, which can be especially dangerous if serving from a directory in which users are able to create arbitrary symlinks. Dir will also allow access to files and directories starting with a period, which could expose sensitive directories like .git or sensitive files like .htpasswd. To exclude files with a leading period, remove the files/directories from the server or create a custom FileSystem implementation.

An empty Dir is treated as ".".

```go
func (d Dir) Open(name string) (File, error)
```

Open implements FileSystem using os.Open, opening files for reading rooted and relative to the directory d.

```go
type File interface {
	io.Closer
	io.Reader
	io.Seeker
	Readdir(count int) ([]fs.FileInfo, error)
	Stat() (fs.FileInfo, error)
}
```

A File is returned by a FileSystem's Open method and can be served by the FileServer implementation.

The methods should behave the same as those on an *os.File.

```go
type FileSystem interface {
	Open(name string) (File, error)
}
```

A FileSystem implements access to a collection of named files. The elements in a file path are separated by slash ('/', U+002F) characters, regardless of host operating system convention. See the FileServer function to convert a FileSystem to a Handler.

This interface predates the fs.FS interface, which can be used instead: the FS adapter function converts an fs.FS to a FileSystem.

```go
func FS(fsys fs.FS) FileSystem
```

FS converts fsys to a FileSystem implementation, for use with FileServer and NewFileTransport. The files provided by fsys must implement io.Seeker.

```go
type Flusher interface {
	// Flush sends any buffered data to the client.
	Flush()
}
```

The Flusher interface is implemented by ResponseWriters that allow an HTTP handler to flush buffered data to the client.

The default HTTP/1.x and HTTP/2 ResponseWriter implementations support Flusher, but ResponseWriter wrappers may not. Handlers should always test for this ability at runtime.

Note that even for ResponseWriters that support Flush, if the client is connected through an HTTP proxy, the buffered data may not reach the client until the response completes.

```go
type HTTP2Config struct {
	// MaxConcurrentStreams optionally specifies the number of
	// concurrent streams that a client may have open at a time.
	// If zero, MaxConcurrentStreams defaults to at least 100.
	//
	// This parameter only applies to Servers.
	MaxConcurrentStreams int

// StrictMaxConcurrentRequests controls whether an HTTP/2 server's
	// concurrency limit should be respected across all connections
	// to that server.
	// If true, new requests sent when a connection's concurrency limit
	// has been exceeded will block until an existing request completes.
	// If false, an additional connection will be opened if all
	// existing connections are at their limit.
	//
	// This parameter only applies to Transports.
	StrictMaxConcurrentRequests bool

// size of the header compression table used for decoding headers sent
	// by the peer.
	// A valid value is less than 4MiB.
	// If zero or invalid, a default value is used.
	MaxDecoderHeaderTableSize int

// header compression table used for sending headers to the peer.
	// A valid value is less than 4MiB.
	// If zero or invalid, a default value is used.
	MaxEncoderHeaderTableSize int

// MaxReadFrameSize optionally specifies the largest frame
	// this endpoint is willing to read.
	// A valid value is between 16KiB and 16MiB, inclusive.
	// If zero or invalid, a default value is used.
	MaxReadFrameSize int

// MaxReceiveBufferPerConnection is the maximum size of the
	// flow control window for data received on a connection.
	// A valid value is at least 64KiB and less than 4MiB.
	// If invalid, a default value is used.
	MaxReceiveBufferPerConnection int

// MaxReceiveBufferPerStream is the maximum size of
	// the flow control window for data received on a stream (request).
	// A valid value is less than 4MiB.
	// If zero or invalid, a default value is used.
	MaxReceiveBufferPerStream int

// SendPingTimeout is the timeout after which a health check using a ping
	// frame will be carried out if no frame is received on a connection.
	// If zero, no health check is performed.
	SendPingTimeout time.Duration

// PingTimeout is the timeout after which a connection will be closed
	// if a response to a ping is not received.
	// If zero, a default of 15 seconds is used.
	PingTimeout time.Duration

// WriteByteTimeout is the timeout after which a connection will be
	// closed if no data can be written to it. The timeout begins when data is
	// available to write, and is extended whenever any bytes are written.
	WriteByteTimeout time.Duration

// PermitProhibitedCipherSuites, if true, permits the use of
	// cipher suites prohibited by the HTTP/2 spec.
	PermitProhibitedCipherSuites bool

// CountError, if non-nil, is called on HTTP/2 errors.
	// It is intended to increment a metric for monitoring.
	// The errType contains only lowercase letters, digits, and underscores
	// (a-z, 0-9, _).
	CountError func(errType string)
}
```

HTTP2Config defines HTTP/2 configuration parameters common to both Transport and Server.

```go
type Handler interface {
	ServeHTTP(ResponseWriter, *Request)
}
```

A Handler responds to an HTTP request.

[Handler.ServeHTTP] should write reply headers and data to the ResponseWriter and then return. Returning signals that the request is finished; it is not valid to use the ResponseWriter or read from the [Request.Body] after or concurrently with the completion of the ServeHTTP call.

Depending on the HTTP client software, HTTP protocol version, and any intermediaries between the client and the Go server, it may not be possible to read from the [Request.Body] after writing to the ResponseWriter. Cautious handlers should read the [Request.Body] first, and then reply.

Except for reading the body, handlers should not modify the provided Request.

If ServeHTTP panics, the server (the caller of ServeHTTP) assumes that the effect of the panic was isolated to the active request. It recovers the panic, logs a stack trace to the server error log, and either closes the network connection or sends an HTTP/2 RST_STREAM, depending on the HTTP protocol. To abort a handler so the client sees an interrupted response but the server doesn't log an error, panic with the value ErrAbortHandler.

```go
func AllowQuerySemicolons(h Handler) Handler
```

AllowQuerySemicolons returns a handler that serves requests by converting any unescaped semicolons in the URL query to ampersands, and invoking the handler h.

This restores the pre-Go 1.17 behavior of splitting query parameters on both semicolons and ampersands. (See golang.org/issue/25192). Note that this behavior doesn't match that of many proxies, and the mismatch can lead to security issues.

AllowQuerySemicolons should be invoked before Request.ParseForm is called.

```go
func FileServer(root FileSystem) Handler
```

FileServer returns a handler that serves HTTP requests with the contents of the file system rooted at root.

As a special case, the returned file server redirects any request ending in "/index.html" to the same path, without the final "index.html".

To use the operating system's file system implementation, use http.Dir:

```go
http.Handle("/", http.FileServer(http.Dir("/tmp")))

```

To use an fs.FS implementation, use http.FileServerFS instead.

```go

package main

import (
	"log"
	"net/http"
)

func main() {
	// Simple static webserver:
	log.Fatal(http.ListenAndServe(":8080", http.FileServer(http.Dir("/usr/share/doc"))))
}

```

```go
Output:

```

Share Format Run

```go

package main

import (
	"io"
	"io/fs"
	"log"
	"net/http"
	"strings"
)

// containsDotFile reports whether name contains a path element starting with a period.
// The name is assumed to be a delimited by forward slashes, as guaranteed
// by the http.FileSystem interface.
func containsDotFile(name string) bool {
	parts := strings.Split(name, "/")
	for _, part := range parts {
		if strings.HasPrefix(part, ".") {
			return true
		}
	}
	return false
}

// dotFileHidingFile is the http.File use in dotFileHidingFileSystem.
// It is used to wrap the Readdir method of http.File so that we can
// remove files and directories that start with a period from its output.
type dotFileHidingFile struct {
	http.File
}

// Readdir is a wrapper around the Readdir method of the embedded File
// that filters out all files that start with a period in their name.
func (f dotFileHidingFile) Readdir(n int) (fis []fs.FileInfo, err error) {
	files, err := f.File.Readdir(n)
	for _, file := range files { // Filters out the dot files
		if !strings.HasPrefix(file.Name(), ".") {
			fis = append(fis, file)
		}
	}
	if err == nil && n > 0 && len(fis) == 0 {
		err = io.EOF
	}
	return
}

// dotFileHidingFileSystem is an http.FileSystem that hides
// hidden "dot files" from being served.
type dotFileHidingFileSystem struct {
	http.FileSystem
}

// Open is a wrapper around the Open method of the embedded FileSystem
// that serves a 403 permission error when name has a file or directory
// with whose name starts with a period in its path.
func (fsys dotFileHidingFileSystem) Open(name string) (http.File, error) {
	if containsDotFile(name) { // If dot file, return 403 response
		return nil, fs.ErrPermission
	}

file, err := fsys.FileSystem.Open(name)
	if err != nil {
		return nil, err
	}
	return dotFileHidingFile{file}, nil
}

func main() {
	fsys := dotFileHidingFileSystem{http.Dir(".")}
	http.Handle("/", http.FileServer(fsys))
	log.Fatal(http.ListenAndServe(":8080", nil))
}

```

```go
Output:

```

Share Format Run

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
func FileServerFS(root fs.FS) Handler
```

FileServerFS returns a handler that serves HTTP requests with the contents of the file system fsys. The files provided by fsys must implement io.Seeker.
