---
source_name: "Google Go Style Guide"
source_url: "https://google.github.io/styleguide/go/"
source_path: "sources/raw/google-go-styleguide/best-practices.html"
license_ref: "sources/licenses/google-styleguide-LICENSE.txt"
---

#### Acceptance testing

Such testing is referred to as acceptance testing. The premise of this kind of testing is that the person using the test does not know every last detail of what goes on in the test; they just hand the inputs over to the testing facility to do the work. This can be thought of as a form of inversion of control.

In a typical Go test, the test function controls the program flow, and the no assert and test functions guidance encourages you to keep it that way. This section explains how to author support for these tests in a way that is consistent with Go style.

Before diving into how, consider an example from `io/fs`, excerpted below:

```go
type FS interface {
    Open(name string) (File, error)
}

```

While there exist well-known implementations of `fs.FS`, a Go developer may be expected to author one. To help validate the user-implemented `fs.FS` is correct, a generic library has been provided in `testing/fstest` called `fstest.TestFS`. This API treats the implementation as a blackbox to make sure it upholds the most basic parts of the `io/fs` contract.
