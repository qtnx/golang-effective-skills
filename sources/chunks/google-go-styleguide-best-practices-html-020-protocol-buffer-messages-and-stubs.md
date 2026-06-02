---
source_name: "Google Go Style Guide"
source_url: "https://google.github.io/styleguide/go/"
source_path: "sources/raw/google-go-styleguide/best-practices.html"
license_ref: "sources/licenses/google-styleguide-LICENSE.txt"
---

### Protocol Buffer Messages and Stubs

Proto library imports are treated differently than standard Go imports due to their cross-language nature. The convention for renamed proto imports are based on the rule that generated the package:

- The `pb` suffix is generally used for `go_proto_library` rules.
- The `grpc` suffix is generally used for `go_grpc_library` rules.

Often a single word describing the package is used:

```go
// Good:
import (
    foopb "path/to/package/foo_service_go_proto"
    foogrpc "path/to/package/foo_service_go_grpc"
)

```

Follow the style guidance for package names. Prefer whole words. Short names are good, but avoid ambiguity. When in doubt, use the proto package name up to _go with a pb suffix:

```go
// Good:
import (
    pushqueueservicepb "path/to/package/push_queue_service_go_proto"
)

```

**Note:** Previous guidance encouraged very short names such as “xpb” or even just “pb”. New code should prefer more descriptive names. Existing code which uses short names should not be used as an example, but does not need to be changed.
