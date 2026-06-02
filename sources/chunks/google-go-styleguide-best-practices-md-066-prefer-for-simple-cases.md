---
source_name: "Google Go Style Guide"
source_url: "https://google.github.io/styleguide/go/"
source_path: "sources/raw/google-go-styleguide/best-practices.md"
license_ref: "sources/licenses/google-styleguide-LICENSE.txt"
---

### Prefer "+" for simple cases

Prefer using "+" when concatenating few strings. This method is syntactically
the simplest and requires no import.

```go
// Good:
key := "projectid: " + p
```

<a id="string-concat-fmt"></a>
