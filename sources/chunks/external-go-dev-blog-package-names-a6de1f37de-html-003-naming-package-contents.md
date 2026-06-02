---
source_name: "External Linked Documentation"
source_url: "https://go.dev/blog/package-names"
source_path: "sources/raw/external/go-dev-blog-package-names-a6de1f37de.html"
license_ref: ""
---

# The Go Blog

## Naming package contents

A package name and its contents’ names are coupled, since client code uses them together. When designing a package, take the client’s point of view.

**Avoid repetition.** Since client code uses the package name as a prefix when referring to the package contents, the names for those contents need not repeat the package name. The HTTP server provided by the `http` package is called `Server`, not `HTTPServer`. Client code refers to this type as `http.Server`, so there is no ambiguity.

**Simplify function names.** When a function in package pkg returns a value of type `pkg.Pkg` (or `*pkg.Pkg`), the function name can often omit the type name without confusion:

```go
start := time.Now()                                  // start is a time.Time
t, err := time.Parse(time.Kitchen, "6:06PM")         // t is a time.Time
ctx = context.WithTimeout(ctx, 10*time.Millisecond)  // ctx is a context.Context
ip, ok := userip.FromContext(ctx)                    // ip is a net.IP

```

A function named `New` in package `pkg` returns a value of type `pkg.Pkg`. This is a standard entry point for client code using that type:

```go
 q := list.New()  // q is a *list.List

```

When a function returns a value of type `pkg.T`, where `T` is not `Pkg`, the function name may include `T` to make client code easier to understand. A common situation is a package with multiple New-like functions:

```go
d, err := time.ParseDuration("10s")  // d is a time.Duration
elapsed := time.Since(start)         // elapsed is a time.Duration
ticker := time.NewTicker(d)          // ticker is a *time.Ticker
timer := time.NewTimer(d)            // timer is a *time.Timer

```

Types in different packages can have the same name, because from the client’s point of view such names are discriminated by the package name. For example, the standard library includes several types named `Reader`, including `jpeg.Reader`, `bufio.Reader`, and `csv.Reader`. Each package name fits with `Reader` to yield a good type name.

If you cannot come up with a package name that’s a meaningful prefix for the package’s contents, the package abstraction boundary may be wrong. Write code that uses your package as a client would, and restructure your packages if the result seems poor. This approach will yield packages that are easier for clients to understand and for the package developers to maintain.
