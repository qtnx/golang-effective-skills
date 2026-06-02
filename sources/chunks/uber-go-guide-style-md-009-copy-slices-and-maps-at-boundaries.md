---
source_name: "Uber Go Style Guide"
source_url: "https://github.com/uber-go/guide/blob/master/style.md"
source_path: "sources/raw/uber-go-guide/style.md"
license_ref: "sources/licenses/uber-go-guide-LICENSE.txt"
---

### Copy Slices and Maps at Boundaries

Slices and maps contain pointers to the underlying data so be wary of scenarios
when they need to be copied.
