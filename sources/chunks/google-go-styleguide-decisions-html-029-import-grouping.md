---
source_name: "Google Go Style Guide"
source_url: "https://google.github.io/styleguide/go/"
source_path: "sources/raw/google-go-styleguide/decisions.html"
license_ref: "sources/licenses/google-styleguide-LICENSE.txt"
---

### Import grouping

Imports should be organized into the following groups, in order:

-
Standard library packages

-
Other (project and vendored) packages

-
Protocol Buffer imports (e.g., `fpb "path/to/foo_go_proto"`)

-
Import for side-effects (e.g., `_ "path/to/package"`)

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
