---
source_name: "Google Go Style Guide"
source_url: "https://google.github.io/styleguide/go/"
source_path: "sources/raw/google-go-styleguide/decisions.md"
license_ref: "sources/licenses/google-styleguide-LICENSE.txt"
---

### Import grouping

Imports should be organized into the following groups, in order:

1.  Standard library packages

1.  Other (project and vendored) packages

1.  Protocol Buffer imports (e.g., `fpb "path/to/foo_go_proto"`)

1.  Import for [side-effects](https://go.dev/doc/effective_go#blank_import)
    (e.g., `_ "path/to/package"`)

```go
// Good:
package main

import (
    "fmt"
    "hash/adler32"
    "os"

    "github.com/dsnet/compress/flate"
    "golang.org/x/text/encoding"
    "google.golang.org/protobuf/proto"

    foopb "myproj/foo/proto/proto"

    _ "myproj/rpc/protocols/dial"
    _ "myproj/security/auth/authhooks"
)
```

<a id="import-blank"></a>
