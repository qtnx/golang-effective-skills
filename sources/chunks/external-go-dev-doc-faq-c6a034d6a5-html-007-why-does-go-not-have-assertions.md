---
source_name: "External Linked Documentation"
source_url: "https://go.dev/doc/faq"
source_path: "sources/raw/external/go-dev-doc-faq-c6a034d6a5.html"
license_ref: ""
---

## Design

### Why does Go not have assertions?

Go doesn’t provide assertions. They are undeniably convenient, but our experience has been that programmers use them as a crutch to avoid thinking about proper error handling and reporting. Proper error handling means that servers continue to operate instead of crashing after a non-fatal error. Proper error reporting means that errors are direct and to the point, saving the programmer from interpreting a large crash trace. Precise errors are particularly important when the programmer seeing the errors is not familiar with the code.

We understand that this is a point of contention. There are many things in the Go language and libraries that differ from modern practices, simply because we feel it’s sometimes worth trying a different approach.
