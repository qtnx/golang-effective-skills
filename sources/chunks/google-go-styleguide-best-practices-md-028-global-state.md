---
source_name: "Google Go Style Guide"
source_url: "https://google.github.io/styleguide/go/"
source_path: "sources/raw/google-go-styleguide/best-practices.md"
license_ref: "sources/licenses/google-styleguide-LICENSE.txt"
---

## Global state
Libraries should not force their clients to use APIs that rely on
[global state](https://en.wikipedia.org/wiki/Global_variable). They are advised
not to expose APIs or export
[package level](https://go.dev/ref/spec#TopLevelDecl) variables that control
behavior for all clients as parts of their API. The rest of the section uses
"global" and "package level state" synonymously.
Instead, if your functionality maintains state, allow your clients to create and
use instance values.
**Important:** While this guidance is applicable to all developers, it is most
critical for infrastructure providers who offer libraries, integrations, and
services to other teams.
```go
// Good:
// Package sidecar manages subprocesses that provide features for applications.
package sidecar
type Registry struct { plugins map[string]*Plugin }
func New() *Registry { return &Registry{plugins: make(map[string]*Plugin)} }
func (r *Registry) Register(name string, p *Plugin) error { ... }
```
Your users will instantiate the data they need (a `*sidecar.Registry`) and then
pass it as an explicit dependency:
```go
// Good:
package main
func main() {
  sidecars := sidecar.New()
  if err := sidecars.Register("Cloud Logger", cloudlogger.New()); err != nil {
    log.Exitf("Could not setup cloud logger: %v", err)
  }
  cfg := &myapp.Config{Sidecars: sidecars}
  myapp.Run(context.Background(), cfg)
}
```
There are different approaches to migrating existing code to support dependency
passing. The main one you will use is passing dependencies as parameters to
constructors, functions, methods, or struct fields on the call chain.
See also:
*   [Go Tip #5: Slimming Your Client Libraries](https://google.github.io/styleguide/go/index.html#gotip)
*   [Go Tip #24: Use Case-Specific Constructions](https://google.github.io/styleguide/go/index.html#gotip)
*   [Go Tip #40: Improving Time Testability with Function Parameters](https://google.github.io/styleguide/go/index.html#gotip)
*   [Go Tip #41: Identify Function Call Parameters](https://google.github.io/styleguide/go/index.html#gotip)
*   [Go Tip #44: Improving Time Testability with Struct Fields](https://google.github.io/styleguide/go/index.html#gotip)
*   [Go Tip #80: Dependency Injection Principles](https://google.github.io/styleguide/go/index.html#gotip)
APIs that do not support explicit dependency passing become fragile as the
number of clients increases:
```go
// Bad:
package sidecar
var registry = make(map[string]*Plugin)
func Register(name string, p *Plugin) error { /* registers plugin in registry */ }
```
Consider what happens in the case of tests exercising code that transitively
relies on a sidecar for cloud logging.
```go
// Bad:
package app
import (
  "cloudlogger"
  "sidecar"
  "testing"
)
func TestEndToEnd(t *testing.T) {
  // The system under test (SUT) relies on a sidecar for a production cloud
  // logger already being registered.
  ... // Exercise SUT and check invariants.
}
func TestRegression_NetworkUnavailability(t *testing.T) {
  // We had an outage because of a network partition that rendered the cloud
  // logger inoperative, so we added a regression test to exercise the SUT with
  // a test double that simulates network unavailability with the logger.
  sidecar.Register("cloudlogger", cloudloggertest.UnavailableLogger)
  ... // Exercise SUT and check invariants.
}
func TestRegression_InvalidUser(t *testing.T) {
  // The system under test (SUT) relies on a sidecar for a production cloud
  // logger already being registered.
  //
  // Oops. cloudloggertest.UnavailableLogger is still registered from the
  // previous test.
  ... // Exercise SUT and check invariants.
}
```
Go tests are executed sequentially by default, so the tests above run as:
1.  `TestEndToEnd`
2.  `TestRegression_NetworkUnavailability`, which overrides the default value of
    cloudlogger
3.  `TestRegression_InvalidUser`, which requires the default value of
    cloudlogger registered in `package sidecar`
This creates an order-dependent test case, which breaks running with test
filters, and prevents tests from running in parallel or being sharded.
Using global state poses problems that lack easy answers for you and the API's
clients:
*   What happens if a client needs to use different and separately operating
    sets of `Plugin`s (for example, to support multiple servers) in the same
    process space?
*   What happens if a client wants to replace a registered `Plugin` with an
    alternative implementation in a test, like a [test double]?
    What happens if a client's tests require hermeticity between instances of a
    `Plugin`, or between all of the plugins registered?
*   What happens if multiple clients `Register` a `Plugin` under the same name?
    Which one wins, if any?
    How should errors be [handled](decisions#handle-errors)? If the code panics
    or calls `log.Fatal`, will that always be
    [appropriate for all places in which API would be called](decisions#dont-panic)?
    Can a client verify it doesn't do something bad before doing so?
*   Are there certain stages in a program's startup phases or lifetime during
    which `Register` can be called and when it can't?
    What happens if `Register` is called at the wrong time? A client could call
    `Register` in [`func init`](https://go.dev/ref/spec#Package_initialization),
    before flags are parsed, or after `main`. The stage at which a function is
    called affects error handling. If the author of an API assumes the API is
    *only* called during program initialization without the requirement that it
    is, the assumption may nudge the author to design error handling to
    [abort the program](best-practices#program-init) by modeling the API as a
    `Must`-like function. Aborting is not appropriate for general-purpose
    library functions that can be used at any stage.
*   What if the client's and the designer's concurrency needs are mismatched?
See also:
*   [Go Tip #36: Enclosing Package-Level State](https://google.github.io/styleguide/go/index.html#gotip)
*   [Go Tip #71: Reducing Parallel Test Flakiness](https://google.github.io/styleguide/go/index.html#gotip)
*   [Go Tip #80: Dependency Injection Principles](https://google.github.io/styleguide/go/index.html#gotip)
*   Error Handling:
    [Look Before You Leap](https://docs.python.org/3/glossary.html#term-LBYL)
    versus
    [Easier to Ask for Forgiveness than Permission](https://docs.python.org/3/glossary.html#term-EAFP)
*   [Unit Testing Practices on Public APIs]
Global state has cascading effects on the
[health of the Google codebase](guide.md#maintainability). Global state should
be approached with **extreme scrutiny**.
[Global state comes in several forms](#globals-forms), and you can use a few
[litmus tests to identify when it is safe](#globals-litmus-tests).
[Unit Testing Practices on Public APIs]: index.md#unit-testing-practices
<a id="globals-forms"></a>
