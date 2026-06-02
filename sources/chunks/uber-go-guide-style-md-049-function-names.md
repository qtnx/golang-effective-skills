---
source_name: "Uber Go Style Guide"
source_url: "https://github.com/uber-go/guide/blob/master/style.md"
source_path: "sources/raw/uber-go-guide/style.md"
license_ref: "sources/licenses/uber-go-guide-LICENSE.txt"
---

### Function Names

We follow the Go community's convention of using [MixedCaps for function
names](https://go.dev/doc/effective_go#mixed-caps). An exception is made for test functions, which may contain underscores
for the purpose of grouping related test cases, e.g.,
`TestMyFunction_WhatIsBeingTested`.
