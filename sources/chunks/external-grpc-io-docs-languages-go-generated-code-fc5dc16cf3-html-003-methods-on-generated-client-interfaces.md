---
source_name: "External Linked Documentation"
source_url: "https://grpc.io/docs/languages/go/generated-code/"
source_path: "sources/raw/external/grpc-io-docs-languages-go-generated-code-fc5dc16cf3.html"
license_ref: ""
---

# Generated-code reference

## Methods on generated client interfaces

For client side usage, each `service Bar` in the `.proto` file also results in the function: `func BarClient(cc *grpc.ClientConn) BarClient`, which returns a concrete implementation of the `BarClient` interface (this concrete implementation also lives in the generated `.pb.go` file).

### Unary Methods

These methods have the following signature on the generated client stub:

`(ctx context.Context, in *RequestMsg, opts ...grpc.CallOption) (*ResponseMsg, error)`

In this context, `RequestMsg` is the single request from client to server, and `ResponseMsg` contains the response sent back from the server.

### Server-Streaming methods

These methods have the following signature on the generated client stub:

`Foo(ctx context.Context, in *RequestMsg, opts ...grpc.CallOption) (grpc.ServerStreamingClient[*ResponseMsg], error)`

In this context, `grpc.ServerStreamingClient`__ <https://pkg.go.dev/google.golang.org/grpc#ServerStreamingClient> represents the client side of server-to-client stream of `ResponseMsg` messages.

Refer to `grpc.ServerStreamingClient`__ <https://pkg.go.dev/google.golang.org/grpc#ServerStreamingClient> documentation for detailed usage information.

### Client-Streaming methods

These methods have the following signature on the generated client stub:

`Foo(ctx context.Context, opts ...grpc.CallOption) (grpc.ClientStreamingClient[*RequestMsg, *ResponseMsg], error)`

In this context, `grpc.ClientStreamingClient`__ <https://pkg.go.dev/google.golang.org/grpc#ClientStreamingClient> represents the client side of client-to-server stream of `RequestMsg` messages. It can be used both to send the client-to-server message stream and to receive the single server response message.

Refer to `grpc.ClientStreamingClient`__ <https://pkg.go.dev/google.golang.org/grpc#ClientStreamingClient> documentation for detailed usage information.

### Bidi-Streaming methods

These methods have the following signature on the generated client stub:

`Foo(ctx context.Context, opts ...grpc.CallOption) (grpc.BidiStreamingClient[*RequestMsg, *ResponseMsg], error)`

In this context, `grpc.BidiStreamingClient`__ <https://pkg.go.dev/google.golang.org/grpc#BidiStreamingClient> represents both the client-to-server and server-to-client message streams.

Refer to `grpc.BidiStreamingClient`__ <https://pkg.go.dev/google.golang.org/grpc#BidiStreamingClient> documentation for detailed usage information.

# Generated-code reference

## Packages and Namespaces

When the `protoc` compiler is invoked with `--go_out=plugins=grpc:`, the `proto package` to Go package translation works the same as when the `protoc-gen-go` plugin is used without the `grpc` plugin.

So, for example, if `foo.proto` declares itself to be in `package foo`, then the generated `foo.pb.go` file will also be in the Go `package foo`.
Last modified November 12, 2024: generated-code: update to include stream generics (#1365) (3df8b27) <https://github.com/grpc/grpc.io/commit/3df8b272bb516ca7bae89708d059e12661917254>

__ View page source <https://github.com/grpc/grpc.io/tree/main/content/en/docs/languages/go/generated-code.md> __ Edit this page <https://github.com/grpc/grpc.io/edit/main/content/en/docs/languages/go/generated-code.md> __ Create child page <https://github.com/grpc/grpc.io/new/main/content/en/docs/languages/go/generated-code.md?filename=change-me.md&value=---%0Atitle%3A+%22Long+Page+Title%22%0AlinkTitle%3A+%22Short+Nav+Title%22%0Aweight%3A+100%0Adescription%3A+%3E-%0A+++++Page+description+for+heading+and+indexes.%0A---%0A%0A%23%23+Heading%0A%0AEdit+this+template+to+create+your+new+page.%0A%0A%2A+Give+it+a+good+name%2C+ending+in+%60.md%60+-+e.g.+%60getting-started.md%60%0A%2A+Edit+the+%22front+matter%22+section+at+the+top+of+the+page+%28weight+controls+how+its+ordered+amongst+other+pages+in+the+same+directory%3B+lowest+number+first%29.%0A%2A+Add+a+good+commit+message+at+the+bottom+of+the+page+%28%3C80+characters%3B+use+the+extended+description+field+for+more+detail%29.%0A%2A+Create+a+new+branch+so+you+can+preview+your+new+file+and+request+a+review+via+Pull+Request.%0A> __ Create documentation issue <https://github.com/grpc/grpc.io/issues/new?title=Generated-code%20reference> __ Create project issue <https://github.com/grpc/grpc.io/issues/new>
