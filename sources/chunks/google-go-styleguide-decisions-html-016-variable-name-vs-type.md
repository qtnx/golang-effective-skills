---
source_name: "Google Go Style Guide"
source_url: "https://google.github.io/styleguide/go/"
source_path: "sources/raw/google-go-styleguide/decisions.html"
license_ref: "sources/licenses/google-styleguide-LICENSE.txt"
---

#### Variable name vs. type

The compiler always knows the type of a variable, and in most cases it is also clear to the reader what type a variable is by how it is used. It is only necessary to clarify the type of a variable if its value appears twice in the same scope.
    Repetitive Name Better Name     `var numUsers int` `var users int`   `var nameString string` `var name string`   `var primaryProject *Project` `var primary *Project`
If the value appears in multiple forms, this can be clarified either with an extra word like `raw` and `parsed` or with the underlying representation:

```go
// Good:
limitRaw := r.FormValue("limit")
limit, err := strconv.Atoi(limitRaw)

```

```go
// Good:
limitStr := r.FormValue("limit")
limit, err := strconv.Atoi(limitStr)

```
