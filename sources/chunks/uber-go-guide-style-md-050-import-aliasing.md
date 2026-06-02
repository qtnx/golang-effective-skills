---
source_name: "Uber Go Style Guide"
source_url: "https://github.com/uber-go/guide/blob/master/style.md"
source_path: "sources/raw/uber-go-guide/style.md"
license_ref: "sources/licenses/uber-go-guide-LICENSE.txt"
---

### Import Aliasing

Import aliasing must be used if the package name does not match the last
element of the import path.

```go
import (
  "net/http"

  client "example.com/client-go"
  trace "example.com/trace/v2"
)
```

In all other scenarios, import aliases should be avoided unless there is a
direct conflict between imports.

<table>
<thead><tr><th>Bad</th><th>Good</th></tr></thead>
<tbody>
<tr><td>

```go
import (
  "fmt"
  "os"
  runtimetrace "runtime/trace"

  nettrace "golang.net/x/trace"
)
```

</td><td>

```go
import (
  "fmt"
  "os"
  "runtime/trace"

  nettrace "golang.net/x/trace"
)
```

</td></tr>
</tbody></table>
