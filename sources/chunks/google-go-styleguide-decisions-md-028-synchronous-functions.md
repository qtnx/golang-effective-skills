---
source_name: "Google Go Style Guide"
source_url: "https://google.github.io/styleguide/go/"
source_path: "sources/raw/google-go-styleguide/decisions.md"
license_ref: "sources/licenses/google-styleguide-LICENSE.txt"
---

## Language

### Synchronous functions

<a id="TOC-SynchronousFunctions"></a>

Synchronous functions return their results directly and finish any callbacks or
channel operations before returning. Prefer synchronous functions over
asynchronous functions.

Synchronous functions keep goroutines localized within a call. This helps to
reason about their lifetimes, and avoid leaks and data races. Synchronous
functions are also easier to test, since the caller can pass an input and check
the output without the need for polling or synchronization.

If necessary, the caller can add concurrency by calling the function in a
separate goroutine. However, it is quite difficult (sometimes impossible) to
remove unnecessary concurrency at the caller side.

See also:

*   "Rethinking Classical Concurrency Patterns", talk by Bryan Mills:
    [slides][rethinking-slides], [video][rethinking-video]

<a id="type-aliases"></a>

## Language

### Type aliases

<a id="TOC-TypeAliases"></a>

Use a *type definition*, `type T1 T2`, to define a new type. Use a
[*type alias*], `type T1 = T2`, to refer to an existing type without defining a
new type. Type aliases are rare; their primary use is to aid migrating packages
to new source code locations. Don't use type aliasing when it is not needed.

[*type alias*]: http://golang.org/ref/spec#Type_declarations

<a id="use-percent-q"></a>
