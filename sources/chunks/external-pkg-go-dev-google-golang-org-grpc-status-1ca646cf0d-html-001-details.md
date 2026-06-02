---
source_name: "External Linked Documentation"
source_url: "https://pkg.go.dev/google.golang.org/grpc/status"
source_path: "sources/raw/external/pkg-go-dev-google-golang-org-grpc-status-1ca646cf0d.html"
license_ref: ""
---

status package - google.golang.org/grpc/status - Go Packages
## Details

-     Valid go.mod <https://github.com/grpc/grpc-go/tree/v1.81.1/go.mod> file
 The Go module system was introduced in Go 1.11 and is the official dependency management solution for Go.

-     Redistributable license
 Redistributable licenses place minimal restrictions on how software can be used, modified, and redistributed.

-     Tagged version
Modules with tagged versions give importers more predictable builds.

-     Stable version
When a project reaches major version v1 it is considered stable.

-  Learn more about best practices

## Repository
   github.com/grpc/grpc-go  <https://github.com/grpc/grpc-go>

##   Documentation ¶

Package status implements errors returned by gRPC. These errors are serialized and transmitted on the wire between server and client, and allow for additional data to be transmitted via the Details field in the status proto. gRPC service handlers should return an error created by this package, and gRPC clients should expect a corresponding error to be returned from the RPC call.

This package upholds the invariants that a non-nil error may not contain an OK code, and an OK code must result in a nil error.

-  func Code(err error) codes.Code
-  func Error(c codes.Code, msg string) error
-  func ErrorProto(s *spb.Status) error
-  func Errorf(c codes.Code, format string, a ...any) error
-  type Status
-
-  func Convert(err error) *Status
-  func FromContextError(err error) *Status
-  func FromError(err error) (s *Status, ok bool)
-  func FromProto(s *spb.Status) *Status
-  func New(c codes.Code, msg string) *Status
-  func Newf(c codes.Code, format string, a ...any) *Status

This section is empty.

This section is empty.

```go
func Code(err error) codes.Code
```

Code returns the Code of the error if it is a Status error or if it wraps a Status error. If that is not the case, it returns codes.OK if err is nil, or codes.Unknown otherwise.

```go
func Error(c codes.Code, msg string) error
```

Error returns an error representing c and msg. If c is OK, returns nil.

```go
func ErrorProto(s *spb.Status) error
```

ErrorProto returns an error representing s. If s.Code is OK, returns nil.

```go
func Errorf(c codes.Code, format string, a ...any) error
```

Errorf returns Error(c, fmt.Sprintf(format, a...)).

```go
type Status = status.Status
```

Status references google.golang.org/grpc/internal/status. It represents an RPC status code, message, and details. It is immutable and should be created with New, Newf, or FromProto. https://godoc.org/google.golang.org/grpc/internal/status <https://godoc.org/google.golang.org/grpc/internal/status>

```go
func Convert(err error) *Status
```

Convert is a convenience function which removes the need to handle the boolean return value from FromError.

```go
func FromContextError(err error) *Status
```

FromContextError converts a context error or wrapped context error into a Status. It returns a Status with codes.OK if err is nil, or a Status with codes.Unknown if err is non-nil and not a context error.

```go
func FromError(err error) (s *Status, ok bool)
```

FromError returns a Status representation of err.

-
If err was produced by this package or implements the method `GRPCStatus() *Status` and `GRPCStatus()` does not return nil, or if err wraps a type satisfying this, the Status from `GRPCStatus()` is returned. For wrapped errors, the message returned contains the entire err.Error() text and not just the wrapped status. In that case, ok is true.

-
If err is nil, a Status is returned with codes.OK and no message, and ok is true.

-
If err implements the method `GRPCStatus() *Status` and `GRPCStatus()` returns nil (which maps to Codes.OK), or if err wraps a type satisfying this, a Status is returned with codes.Unknown and err's Error() message, and ok is false.

-
Otherwise, err is an error not compatible with this package. In this case, a Status is returned with codes.Unknown and err's Error() message, and ok is false.

```go
func FromProto(s *spb.Status) *Status
```

FromProto returns a Status representing s.

```go
func New(c codes.Code, msg string) *Status
```

New returns a Status representing c and msg.

```go
func Newf(c codes.Code, format string, a ...any) *Status
```

Newf returns New(c, fmt.Sprintf(format, a...)).

##   Source Files ¶
 View all Source files <https://github.com/grpc/grpc-go/tree/v1.81.1/status>

- status.go <https://github.com/grpc/grpc-go/blob/v1.81.1/status/status.go>

  Click to show internal directories.
  Click to hide internal directories.

  Close

     **?** : This menu   **/** : Search site   **f** or **F** : Jump to   **y** or **Y**  : Canonical URL
  Close
