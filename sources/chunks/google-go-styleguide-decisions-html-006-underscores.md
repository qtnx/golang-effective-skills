---
source_name: "Google Go Style Guide"
source_url: "https://google.github.io/styleguide/go/"
source_path: "sources/raw/google-go-styleguide/decisions.html"
license_ref: "sources/licenses/google-styleguide-LICENSE.txt"
---

### Underscores

Names in Go should in general not contain underscores. There are three exceptions to this principle:

- Package names that are only imported by generated code may contain underscores. See package names for more detail around how to choose multi-word package names.
- Test, Benchmark and Example function names within `*_test.go` files may include underscores.
- Low-level libraries that interoperate with the operating system or cgo may reuse identifiers, as is done in `syscall`. This is expected to be very rare in most codebases.

**Note:** Filenames of source code are not Go identifiers and do not have to follow these conventions. They may contain underscores.
