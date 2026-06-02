---
source_name: "Uber Go Style Guide"
source_url: "https://github.com/uber-go/guide/blob/master/style.md"
source_path: "sources/raw/uber-go-guide/style.md"
license_ref: "sources/licenses/uber-go-guide-LICENSE.txt"
---

### Package Names

When naming packages, choose a name that is:

- All lower-case. No capitals or underscores.
- Does not need to be renamed using named imports at most call sites.
- Short and succinct. Remember that the name is identified in full at every call
  site.
- Not plural. For example, `net/url`, not `net/urls`.
- Not "common", "util", "shared", or "lib". These are bad, uninformative names.

See also [Package Names](https://go.dev/blog/package-names) and [Style guideline for Go packages](https://rakyll.org/style-packages/).
