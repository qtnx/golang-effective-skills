---
source_name: "Google Go Style Guide"
source_url: "https://google.github.io/styleguide/go/"
source_path: "sources/raw/google-go-styleguide/guide.html"
license_ref: "sources/licenses/google-styleguide-LICENSE.txt"
---

### Formatting

All Go source files must conform to the format outputted by the `gofmt` tool. This format is enforced by a presubmit check in the Google codebase. Generated code should generally also be formatted (e.g., by using `format.Source`), as it is also browsable in Code Search.
