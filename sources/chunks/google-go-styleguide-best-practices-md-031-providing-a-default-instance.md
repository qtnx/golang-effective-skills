---
source_name: "Google Go Style Guide"
source_url: "https://google.github.io/styleguide/go/"
source_path: "sources/raw/google-go-styleguide/best-practices.md"
license_ref: "sources/licenses/google-styleguide-LICENSE.txt"
---

## Global state

### Providing a default instance

While not recommended, it is acceptable to provide a simplified API that uses
package level state if you need to maximize convenience for the user.

Follow the [litmus tests](#globals-litmus-tests) with these guidelines in such
cases:

1.  The package must offer clients the ability to create isolated instances of
    package types as [described above](#globals-forms).
2.  The public APIs that use global state must be a thin proxy to the previous
    API. A good example of this is
    [`http.Handle`](https://pkg.go.dev/net/http#Handle) internally calling
    [`(*http.ServeMux).Handle`](https://pkg.go.dev/net/http#ServeMux.Handle) on
    the package variable
    [`http.DefaultServeMux`](https://pkg.go.dev/net/http#DefaultServeMux).
3.  This package-level API must only be used by [binary build targets], not
    [libraries], unless the libraries are undertaking a refactoring to support
    dependency passing. Infrastructure libraries that can be imported by other
    packages must not rely on package-level state of the packages they import.

    For example, an infrastructure provider implementing a sidecar that is to be
    shared with other teams using the API from the top should offer an API to
    accommodate this:

    ```go
    // Good:
    package cloudlogger

    func New() *Logger { ... }

    func Register(r *sidecar.Registry, l *Logger) {
      r.Register("Cloud Logging", l)
    }
    ```

4.  This package-level API must [document](#documentation-conventions) and
    enforce its invariants (for example, at which stage in the program's life it
    can be called, whether it can be used concurrently). Further, it must
    provide an API to reset global state to a known-good default (for example,
    to facilitate testing).

[binary build targets]: https://github.com/bazelbuild/rules_go/blob/master/docs/go/core/rules.md#go_binary
[libraries]: https://github.com/bazelbuild/rules_go/blob/master/docs/go/core/rules.md#go_library

See also:

*   [Go Tip #36: Enclosing Package-Level State](https://google.github.io/styleguide/go/index.html#gotip)
*   [Go Tip #80: Dependency Injection Principles](https://google.github.io/styleguide/go/index.html#gotip)

<a id="interfaces"></a>
