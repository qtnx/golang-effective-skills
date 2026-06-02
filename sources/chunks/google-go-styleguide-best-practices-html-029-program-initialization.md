---
source_name: "Google Go Style Guide"
source_url: "https://google.github.io/styleguide/go/"
source_path: "sources/raw/google-go-styleguide/best-practices.html"
license_ref: "sources/licenses/google-styleguide-LICENSE.txt"
---

### Program initialization

Program initialization errors (such as bad flags and configuration) should be propagated upward to `main`, which should call `log.Exit` with an error that explains how to fix the error. In these cases, `log.Fatal` should not generally be used, because a stack trace that points at the check is not likely to be as useful as a human-generated, actionable message.
