---
source_name: "Google Go Style Guide"
source_url: "https://google.github.io/styleguide/go/"
source_path: "sources/raw/google-go-styleguide/best-practices.md"
license_ref: "sources/licenses/google-styleguide-LICENSE.txt"
---

## Global state

### Major forms of package state APIs

Several of the most common problematic API forms are enumerated below:

*   Top-level variables irrespective of whether they are exported.

    ```go
    // Bad:
    package logger

    // Sinks manages the default output sources for this package's logging API.  This
    // variable should be set at package initialization time and never thereafter.
    var Sinks []Sink
    ```

    See the [litmus tests](#globals-litmus-tests) to know when these are safe.

*   The
    [service locator pattern](https://en.wikipedia.org/wiki/Service_locator_pattern).
    See the [first example](#globals). The service locator pattern itself is not
    problematic, rather the locator being defined as global.

*   Registries for
    [callbacks](https://en.wikipedia.org/wiki/Callback_\(computer_programming\))
    and similar behaviors.

    ```go
    // Bad:
    package health

    var unhealthyFuncs []func

    func OnUnhealthy(f func()) {
      unhealthyFuncs = append(unhealthyFuncs, f)
    }
    ```

*   Thick-Client singletons for things like backends, storage, data access
    layers, and other system resources. These often pose additional problems
    with service reliability.

    ```go
    // Bad:
    package useradmin

    var client pb.UserAdminServiceClientInterface

    func Client() *pb.UserAdminServiceClient {
        if client == nil {
            client = ...  // Set up client.
        }
        return client
    }
    ```

> **Note:** Many legacy APIs in the Google codebase do not follow this guidance;
> in fact, some Go standard libraries allow for configuration via global values.
> Nevertheless, the legacy API's contravention of this guidance
> **[should not be used as precedent](guide#local-consistency)** for continuing
> the pattern.
>
> It is better to invest in proper API design today than pay for redesigning
> later.

<a id="globals-litmus-tests"></a>
