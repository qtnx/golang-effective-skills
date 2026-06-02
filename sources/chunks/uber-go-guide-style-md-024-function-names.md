---
source_name: "Uber Go Style Guide"
source_url: "https://github.com/uber-go/guide/blob/master/style.md"
source_path: "sources/raw/uber-go-guide/style.md"
license_ref: "sources/licenses/uber-go-guide-LICENSE.txt"
---

## Style

### Function Names

We follow the Go community's convention of using [MixedCaps for function
names](https://go.dev/doc/effective_go#mixed-caps). An exception is made for test functions, which may contain underscores
for the purpose of grouping related test cases, e.g.,
`TestMyFunction_WhatIsBeingTested`.

## Style

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

## Style

### Function Grouping and Ordering

- Functions should be sorted in rough call order.
- Functions in a file should be grouped by receiver.

Therefore, exported functions should appear first in a file, after
`struct`, `const`, `var` definitions.

A `newXYZ()`/`NewXYZ()` may appear after the type is defined, but before the
rest of the methods on the receiver.

Since functions are grouped by receiver, plain utility functions should appear
towards the end of the file.

<table>
<thead><tr><th>Bad</th><th>Good</th></tr></thead>
<tbody>
<tr><td>

```go
func (s *something) Cost() {
  return calcCost(s.weights)
}

type something struct{ ... }

func calcCost(n []int) int {...}

func (s *something) Stop() {...}

func newSomething() *something {
    return &something{}
}
```

</td><td>

```go
type something struct{ ... }

func newSomething() *something {
    return &something{}
}

func (s *something) Cost() {
  return calcCost(s.weights)
}

func (s *something) Stop() {...}

func calcCost(n []int) int {...}
```

</td></tr>
</tbody></table>
