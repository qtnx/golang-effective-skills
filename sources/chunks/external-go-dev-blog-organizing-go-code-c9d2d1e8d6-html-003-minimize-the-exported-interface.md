---
source_name: "External Linked Documentation"
source_url: "https://go.dev/blog/organizing-go-code"
source_path: "sources/raw/external/go-dev-blog-organizing-go-code-c9d2d1e8d6.html"
license_ref: ""
---

# The Go Blog

## Minimize the exported interface

Your code is likely composed of many small pieces of useful code, and so it is tempting to expose much of that functionality in your package’s exported interface. Resist that urge!

The larger the interface you provide, the more you must support. Users will quickly come to depend on every type, function, variable, and constant you export, creating an implicit contract that you must honor in perpetuity or risk breaking your users’ programs. In preparing Go 1 we carefully reviewed the standard library’s exported interfaces and removed the parts we weren’t ready to commit to. You should take similar care when distributing your own libraries.

If in doubt, leave it out!
