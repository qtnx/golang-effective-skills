---
source_name: "Google Go Style Guide"
source_url: "https://google.github.io/styleguide/go/"
source_path: "sources/raw/google-go-styleguide/best-practices.md"
license_ref: "sources/licenses/google-styleguide-LICENSE.txt"
---

### Designing effective interfaces

1.  **Keep interfaces small:** The larger the interface,
    [the harder it is to implement and to write code that takes advantage of it](https://go-proverbs.github.io/).
    Small interfaces are easier to compose into larger ones if needed.

2.  **Documentation:** Treat every interface as the "user manual" for your
    abstraction. The depth of your documentation should be proportional to the
    interface's cognitive load, not just the count of its methods. Whether an
    interface has ten methods or a single `Write` of
    [io.Writer](https://pkg.go.dev/io#Writer), if a programmer is expected to
    interact with that type, the API must be documented thoroughly.

    *   **Single-method interfaces:** documentation on the type itself is
        usually sufficient (e.g., io.Writer). Explain its contract, edge cases,
        and expected errors.
    *   **Multi-method interfaces:** each individual method requires its own
        documentation.
    *   **Unexported interfaces:** consider documenting them anyway. They are
        often the glue that holds complex internal logic together, and because
        they are invisible to external users, they can easily become mystery
        code for future maintainers (including your future self).

3.  **Accept interfaces, return concrete types:** Returning a concrete type
    allows the caller to use the full functionality of the value without being
    locked into a specific interface abstraction
    [GoTip #49: Accept Interfaces, Return Concrete Types].

There are several common scenarios where returning an interface is the idiomatic
choice:

1.  **Encapsulation:** While interfaces cannot strictly hide exported methods
    (as they remain accessible via type assertions), returning an interface is a
    powerful tool for limiting the default API surface and guiding the caller's
    behavior.. The most common example is the `error` interface; you
    [almost never return a concrete error type](decisions#errors) like
    `*MyCustomError`.

    Consider a `ThrottledReader` that implements `io.Reader` but also has a
    `Refill` method for internal bucket management. Returning the concrete
    `*ThrottledReader` invites the caller to manage the bucket manually, which
    could lead to race conditions or broken rate-limiting logic. By returning an
    interface, you tell the caller that your only job is to consume this reader.
    If you try to cast this back to a `ThrottledReader` to `Refill` the internal
    bucket, you are breaking the contract.

    ```go
    // Good:
    type ThrottledReader struct {
        source     io.Reader
        limit      int  // bytes per second
        balance    int  // current allowance of bytes
        lastRefill time.Time
    }

    // Read implements the io.Reader interface with rate-limiting logic.
    func (t *ThrottledReader) Read(p []byte) (int, error) { ... }

    // Refill manually adds tokens to the bucket.
    // INTERNAL USE ONLY: Calling this from outside breaks the rate limit logic.
    func (t *ThrottledReader) Refill(amount int) {
        t.balance = min(t.balance + amount, t.limit)
    }

    // New returns the io.Reader with rate-limiting.
    func New(r io.Reader, bytesPerSec int) io.Reader {
        return &ThrottledReader{
            source:     r,
            limit:      bytesPerSec,
            balance:    bytesPerSec, // start with a full bucket
            lastRefill: time.Now(),
        }
    }
    ```

    This raises a natural question: if `Refill` is dangerous, why export it at
    all? In complex systems, you often need internal orchestration. For example,
    an `AggregateReader` manages multiple `ThrottledReader` values to ensure
    total bandwidth across all streams stays under a global limit. This
    coordinator needs to call Refill to distribute tokens, but the non-power
    user processing the data should never see that capability.

    **Caution:** Before returning an interface to hide implementation, ask:
    "Would a user calling these extra methods actually break the system's
    integrity or meaningfully limit maintainability?" If the extra details allow
    the user to bypass safety checks, or if exposing the concrete type makes it
    impossible to change the underlying provider later without a breaking
    change, you may return an interface. Do not rotely encapsulate without
    reason.

2.  **Certain patterns:** If a function is designed to return one of several
    different concrete types based on decisions made at runtime, it must return
    an interface. This is commonly true with command, chaining, factory, and
    [strategy](https://en.wikipedia.org/wiki/Strategy_pattern) patterns.
    Consider this code that selects which encoder to use based the requested
    format:

    ```go
    // Good:
    func NewWriter(format string) io.Writer {
        switch format {
        case "json":
            return &jsonWriter{}
        case "xml":
            return &xmlWriter{}
        default:
            return &textWriter{}
        }
    }
    ```

    The following example of a chaining API demonstrates how returning an
    interface enables polymorphic behavior. By allowing callers to use either
    `client.Do(req)` or `client.WithAuth("token").Do(req)`, you can swap
    implementations without breaking the calling code.

    ```go
    // Good:
    type Client interface {
        WithAuth(token string) Client
        Do(req *Request) error
    }
    ```

    These patterns are guidelines, not rules. Avoid forcing an interface if a
    single, robust concrete type can handle the abstraction internally. For
    example, the standard [database/sql](https://pkg.go.dev/database/sql#DB)
    library exports a single concrete `DB` type instead of forcing an interface
    to handle types like `MySQLDB` and `OracleDB`.

3.  <span id="avoiding-circular-dependencies">**Avoiding circular
    dependencies:**</span> If returning a concrete type would require importing
    a package that already imports your current package, you must return an
    interface to break the circular dependency.

    For example:

    ```go
    // Bad:
    package app

    import "myproject/plugin"

    type Config struct {
        APIKey string
    }

    func Start() {
        p := plugin.New()
    }
    ```

    ```go
    // Bad:
    package plugin

    import "myproject/app"  // ERROR: Import cycle!

    func New() *app.Config {
        return &app.Config{APIKey: "secret"}
    }
    ```

    In this case, `plugin`'s `New` cannot return `*app.Config` because it would
    create a circular import. To break this, we use the fact that interfaces are
    satisfied implicitly. We move the "contract" to a neutral place or have the
    producer return an interface that the consumer already understands.

    If `plugin`'s `New` returns an interface instead of the concrete
    `*app.Config` struct, it no longer needs to import package `app`.

    ```go
    package plugin

    type Configurer interface {
        APIKey() string
    }

    type localConfig struct {
        key string
    }

    func (c localConfig) APIKey() string { return c.key }

    // New returns the interface Configurer instead of the concrete app.Config
    func New() Configurer {
        return &localConfig{key: "secret"}
    }
    ```

    ```go
    package app

    import "myproject/plugin"

    func Start() {
        conf := plugin.New()  // 'conf' is now a Configurer interface
        fmt.Println(conf.APIKey())
    }
    ```

    **Caution:** Carefully observe guidance on [Package Size](#package-size).
    Introducing interfaces to break dependency cycles is often a signal of
    improperly structured packages. Consolidated packages are often preferred
    over too many too small packages that fail to stand on their own.

[GoTip #78: Minimal Viable Interfaces]: https://google.github.io/styleguide/go/index.html#gotip
[GoTip #49: Accept Interfaces, Return Concrete Types]: https://google.github.io/styleguide/go/index.html#gotip
[testing RPC]: https://codelabs.developers.google.com/grpc/getting-started-grpc-go#3
[test double]: https://abseil.io/resources/swe-book/html/ch13.html
[public API]: https://abseil.io/resources/swe-book/html/ch12.html#test_via_public_apis
