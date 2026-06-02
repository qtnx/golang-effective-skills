---
source_name: "Google Go Style Guide"
source_url: "https://google.github.io/styleguide/go/"
source_path: "sources/raw/google-go-styleguide/best-practices.html"
license_ref: "sources/licenses/google-styleguide-LICENSE.txt"
---

#### Custom verbosity levels

Use verbose logging (`log.V`) to your advantage. Verbose logging can be useful for development and tracing. Establishing a convention around verbosity levels can be helpful. For example:

- Write a small amount of extra information at `V(1)`
- Trace more information in `V(2)`
- Dump large internal states in `V(3)`

To minimize the cost of verbose logging, you should ensure not to accidentally call expensive functions even when `log.V` is turned off. `log.V` offers two APIs. The more convenient one carries the risk of this accidental expense. When in doubt, use the slightly more verbose style.

```go
// Good:
for _, sql := range queries {
  log.V(1).Infof("Handling %v", sql)
  if log.V(2) {
    log.Infof("Handling %v", sql.Explain())
  }
  sql.Run(...)
}

```

```go
// Bad:
// sql.Explain called even when this log is not printed.
log.V(2).Infof("Handling %v", sql.Explain())

```
