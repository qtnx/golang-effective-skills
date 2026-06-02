---
source_name: "Uber Go Style Guide"
source_url: "https://github.com/uber-go/guide/blob/master/style.md"
source_path: "sources/raw/uber-go-guide/style.md"
license_ref: "sources/licenses/uber-go-guide-LICENSE.txt"
---

### Prefer Specifying Container Capacity

Specify container capacity where possible in order to allocate memory for the
container up front. This minimizes subsequent allocations (by copying and
resizing of the container) as elements are added.
