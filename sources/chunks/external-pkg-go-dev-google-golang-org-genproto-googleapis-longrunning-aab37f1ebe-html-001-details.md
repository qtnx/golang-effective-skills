---
source_name: "External Linked Documentation"
source_url: "https://pkg.go.dev/google.golang.org/genproto/googleapis/longrunning"
source_path: "sources/raw/external/pkg-go-dev-google-golang-org-genproto-googleapis-longrunning-aab37f1ebe.html"
license_ref: ""
---

longrunning package - google.golang.org/genproto/googleapis/longrunning - Go Packages
## Details

-     Valid go.mod <https://github.com/googleapis/go-genproto/tree/3dc84a4a5aaa/go.mod> file
 The Go module system was introduced in Go 1.11 and is the official dependency management solution for Go.

-     Redistributable license
 Redistributable licenses place minimal restrictions on how software can be used, modified, and redistributed.

-     Tagged version
Modules with tagged versions give importers more predictable builds.

-     Stable version
When a project reaches major version v1 it is considered stable.

-  Learn more about best practices

## Repository
   github.com/googleapis/go-genproto  <https://github.com/googleapis/go-genproto>

##   Documentation ¶

Package longrunning aliases all exported identifiers in package "cloud.google.com/go/longrunning/autogen/longrunningpb".

Deprecated: Please use types in: cloud.google.com/go/longrunning/autogen/longrunningpb. Please read https://github.com/googleapis/google-cloud-go/blob/main/migration.md <https://github.com/googleapis/google-cloud-go/blob/main/migration.md> for more details.

- Variables
-  func RegisterOperationsServer(s *grpc.Server, srv OperationsServer)deprecated
-  type CancelOperationRequestdeprecated
-  type DeleteOperationRequestdeprecated
-  type GetOperationRequestdeprecated
-  type ListOperationsRequestdeprecated
-  type ListOperationsResponsedeprecated
-  type Operationdeprecated
-  type OperationInfodeprecated
-  type Operation_Error
-  type Operation_Response
-  type OperationsClientdeprecated
-
-  func NewOperationsClient(cc grpc.ClientConnInterface) OperationsClientdeprecated

-  type OperationsServerdeprecated
-  type UnimplementedOperationsServerdeprecated
-  type WaitOperationRequestdeprecated

This section is empty.

    View Source <https://github.com/googleapis/go-genproto/blob/3dc84a4a5aaa/googleapis/longrunning/alias.go#L31>
```go
var (
	E_OperationInfo                          = src.E_OperationInfo
	File_google_longrunning_operations_proto = src.File_google_longrunning_operations_proto
)
```

Deprecated: Please use vars in: cloud.google.com/go/longrunning/autogen/longrunningpb

```go
func RegisterOperationsServer(s *grpc.Server, srv OperationsServer)
```

Deprecated: Please use funcs in: cloud.google.com/go/longrunning/autogen/longrunningpb

```go
type CancelOperationRequest = src.CancelOperationRequest
```

The request message for [Operations.CancelOperation][google.longrunning.Operations.CancelOperation].

Deprecated: Please use types in: cloud.google.com/go/longrunning/autogen/longrunningpb

```go
type DeleteOperationRequest = src.DeleteOperationRequest
```

The request message for [Operations.DeleteOperation][google.longrunning.Operations.DeleteOperation].

Deprecated: Please use types in: cloud.google.com/go/longrunning/autogen/longrunningpb

```go
type GetOperationRequest = src.GetOperationRequest
```

The request message for [Operations.GetOperation][google.longrunning.Operations.GetOperation].

Deprecated: Please use types in: cloud.google.com/go/longrunning/autogen/longrunningpb

```go
type ListOperationsRequest = src.ListOperationsRequest
```

The request message for [Operations.ListOperations][google.longrunning.Operations.ListOperations].

Deprecated: Please use types in: cloud.google.com/go/longrunning/autogen/longrunningpb

```go
type ListOperationsResponse = src.ListOperationsResponse
```

The response message for [Operations.ListOperations][google.longrunning.Operations.ListOperations].

Deprecated: Please use types in: cloud.google.com/go/longrunning/autogen/longrunningpb

```go
type Operation = src.Operation
```

This resource represents a long-running operation that is the result of a network API call.

Deprecated: Please use types in: cloud.google.com/go/longrunning/autogen/longrunningpb

```go
type OperationInfo = src.OperationInfo
```

A message representing the message types used by a long-running operation. Example: rpc LongRunningRecognize(LongRunningRecognizeRequest) returns (google.longrunning.Operation) { option (google.longrunning.operation_info) = { response_type: "LongRunningRecognizeResponse" metadata_type: "LongRunningRecognizeMetadata" }; }

Deprecated: Please use types in: cloud.google.com/go/longrunning/autogen/longrunningpb

```go
type Operation_Error = src.Operation_Error
```

```go
type Operation_Response = src.Operation_Response
```

```go
type OperationsClient = src.OperationsClient
```

OperationsClient is the client API for Operations service. For semantics around ctx use and closing/ending streaming RPCs, please refer to https://godoc.org/google.golang.org/grpc#ClientConn.NewStream <https://godoc.org/google.golang.org/grpc#ClientConn.NewStream>.

Deprecated: Please use types in: cloud.google.com/go/longrunning/autogen/longrunningpb

```go
func NewOperationsClient(cc grpc.ClientConnInterface) OperationsClient
```

Deprecated: Please use funcs in: cloud.google.com/go/longrunning/autogen/longrunningpb

```go
type OperationsServer = src.OperationsServer
```

OperationsServer is the server API for Operations service.

Deprecated: Please use types in: cloud.google.com/go/longrunning/autogen/longrunningpb

```go
type UnimplementedOperationsServer = src.UnimplementedOperationsServer
```

UnimplementedOperationsServer can be embedded to have forward compatible implementations.

Deprecated: Please use types in: cloud.google.com/go/longrunning/autogen/longrunningpb

```go
type WaitOperationRequest = src.WaitOperationRequest
```

The request message for [Operations.WaitOperation][google.longrunning.Operations.WaitOperation].

Deprecated: Please use types in: cloud.google.com/go/longrunning/autogen/longrunningpb

##   Source Files ¶
 View all Source files <https://github.com/googleapis/go-genproto/tree/3dc84a4a5aaa/googleapis/longrunning>

- alias.go <https://github.com/googleapis/go-genproto/blob/3dc84a4a5aaa/googleapis/longrunning/alias.go>

  Click to show internal directories.
  Click to hide internal directories.

  Close

     **?** : This menu   **/** : Search site   **f** or **F** : Jump to   **y** or **Y**  : Canonical URL
  Close
