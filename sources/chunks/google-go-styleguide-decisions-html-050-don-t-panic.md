---
source_name: "Google Go Style Guide"
source_url: "https://google.github.io/styleguide/go/"
source_path: "sources/raw/google-go-styleguide/decisions.html"
license_ref: "sources/licenses/google-styleguide-LICENSE.txt"
---

### Don’t panic

Do not use `panic` for normal error handling. Instead, use `error` and multiple return values. See the Effective Go section on errors.

Within `package main` and initialization code, consider `log.Exit` for errors that should terminate the program (e.g., invalid configuration), as in many of these cases a stack trace will not help the reader. Please note that `log.Exit` calls `os.Exit` and any deferred functions will not be run.

For errors that indicate “impossible” conditions, namely bugs that should always be caught during code review and/or testing, a function may reasonably return an error or call `log.Fatal`.

Also see when panic is acceptable.

**Note:** `log.Fatalf` is not the standard library log. See [#logging].
