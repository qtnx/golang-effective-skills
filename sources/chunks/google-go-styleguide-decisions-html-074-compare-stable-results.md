---
source_name: "Google Go Style Guide"
source_url: "https://google.github.io/styleguide/go/"
source_path: "sources/raw/google-go-styleguide/decisions.html"
license_ref: "sources/licenses/google-styleguide-LICENSE.txt"
---

### Compare stable results

Avoid comparing results that may depend on output stability of a package that you do not own. Instead, the test should compare on semantically relevant information that is stable and resistant to changes in dependencies. For functionality that returns a formatted string or serialized bytes, it is generally not safe to assume that the output is stable.

For example, `json.Marshal` can change (and has changed in the past) the specific bytes that it emits. Tests that perform string equality on the JSON string may break if the `json` package changes how it serializes the bytes. Instead, a more robust test would parse the contents of the JSON string and ensure that it is semantically equivalent to some expected data structure.
