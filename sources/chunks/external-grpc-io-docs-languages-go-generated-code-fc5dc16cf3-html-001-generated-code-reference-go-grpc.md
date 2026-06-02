---
source_name: "External Linked Documentation"
source_url: "https://grpc.io/docs/languages/go/generated-code/"
source_path: "sources/raw/external/grpc-io-docs-languages-go-generated-code-fc5dc16cf3.html"
license_ref: ""
---

# Generated-code reference

Generated-code reference | Go | gRPC
# Generated-code reference
# Generated-code reference
This page describes the code generated when compiling `.proto` files with `protoc`, using the `protoc-gen-go-grpc` grpc plugin__ <https://pkg.go.dev/google.golang.org/grpc/cmd/protoc-gen-go-grpc>. This latest version of generated code uses generics by default. If you’re working with older generated code that doesn’t use generics, you can find the relevant documentation here. While we encourage using this latest version with generics, you can temporarily revert to the old behavior by setting the `useGenericStreams` flag to `false`.
You can find out how to define a gRPC service in a `.proto` file in Service definition.
**Thread-safety**: note that client-side RPC invocations and server-side RPC handlers _are thread-safe_ and are meant to be run on concurrent goroutines. But also note that for _individual streams_, incoming and outgoing data is bi-directional but serial; so e.g. _individual streams_ do not support _concurrent reads_ or _concurrent writes_ (but reads are safely concurrent _with_ writes).
