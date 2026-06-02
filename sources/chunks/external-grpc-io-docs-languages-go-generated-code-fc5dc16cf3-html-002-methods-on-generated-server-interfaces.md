---
source_name: "External Linked Documentation"
source_url: "https://grpc.io/docs/languages/go/generated-code/"
source_path: "sources/raw/external/grpc-io-docs-languages-go-generated-code-fc5dc16cf3.html"
license_ref: ""
---

# Generated-code reference

## Methods on generated server interfaces

On the server side, each `service Bar` in the `.proto` file results in the function:

`func RegisterBarServer(s *grpc.Server, srv BarServer)`

The application can define a concrete implementation of the `BarServer` interface and register it with a `grpc.Server` instance (before starting the server instance) by using this function.

### Unary methods

These methods have the following signature on the generated service interface:

`Foo(context.Context, *RequestMsg) (*ResponseMsg, error)`

In this context, `RequestMsg` is the protobuf message sent from the client, and `ResponseMsg` is the protobuf message sent back from the server.

### Server-streaming methods

These methods have the following signature on the generated service interface: `Foo(*RequestMsg, grpc.ServerStreamingServer[*ResponseMsg]) error`

In this context, `RequestMsg` is the single request from the client, and `grpc.ServerStreamingServer`__ <https://pkg.go.dev/google.golang.org/grpc#ServerStreamingServer> represents the server side of server-to-client stream of response type `ResponseMsg`.

Refer to `grpc.ServerStreamingServer`__ <https://pkg.go.dev/google.golang.org/grpc#ServerStreamingServer> documentation for detailed usage information.

### Client-streaming methods

These methods have the following signature on the generated service interface:

`Foo(grpc.ClientStreamingServer[*RequestMsg, *ResponseMsg]) error`

Where `RequestMsg` is the message type of the stream, sent from client-to-server and `ResponseMsg` is the type of response from server to client.

In this context, `grpc.ClientStreamingServer`__ <https://pkg.go.dev/google.golang.org/grpc#ClientStreamingServer> can be used both to read the client-to-server message stream and to send the single server response message.

Refer to `grpc.ClientStreamingServer`__ <https://pkg.go.dev/google.golang.org/grpc#ClientStreamingServer> documentation for detailed usage information.

### Bidi-streaming methods

These methods have the following signature on the generated service interface:

`Foo(grpc.BidiStreamingServer[*RequestMsg, *ResponseMsg]) error`

Where `RequestMsg` is the message type of the stream, sent from client-to-server and `ResponseMsg` is the type of stream from server-to-client.

In this context, `grpc.BidiStreamingServer`__ <https://pkg.go.dev/google.golang.org/grpc#BidiStreamingServer> can be used to access both the client-to-server message stream and the server-to-client message stream.

Refer to `grpc.BidiStreamingServer`__ <https://pkg.go.dev/google.golang.org/grpc#BidiStreamingServer> documentation for detailed usage information.
