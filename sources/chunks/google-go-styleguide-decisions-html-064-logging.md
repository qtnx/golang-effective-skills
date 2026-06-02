---
source_name: "Google Go Style Guide"
source_url: "https://google.github.io/styleguide/go/"
source_path: "sources/raw/google-go-styleguide/decisions.html"
license_ref: "sources/licenses/google-styleguide-LICENSE.txt"
---

### Logging

Go programs in the Google codebase use a variant of the standard `log` package. It has a similar but more powerful interface and interoperates well with internal Google systems. An open source version of this library is available as package `glog`, and open source Google projects may use that, but this guide refers to it as `log` throughout.

**Note:** For abnormal program exits, this library uses `log.Fatal` to abort with a stacktrace, and `log.Exit` to stop without one. There is no `log.Panic` function as in the standard library.

**Tip:** `log.Info(v)` is equivalent `log.Infof("%v", v)`, and the same goes for other logging levels. Prefer the non-formatting version when you have no formatting to do.

See also:

- Best practices on logging errors and custom verbosity levels
- When and how to use the log package to stop the program
