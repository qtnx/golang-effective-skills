---
source_name: "Google Go Style Guide"
source_url: "https://google.github.io/styleguide/go/"
source_path: "sources/raw/google-go-styleguide/best-practices.md"
license_ref: "sources/licenses/google-styleguide-LICENSE.txt"
---

### Litmus tests

[APIs using the patterns above](#globals-forms) are unsafe when:

*   Multiple functions interact via global state when executed in the same
    program, despite being otherwise independent (for example, authored by
    different authors in vastly different directories).
*   Independent test cases interact with each other through global state.
*   Users of the API are tempted to swap or replace global state for testing
    purposes, particularly to replace any part of the state with a
    [test double], like a stub, fake, spy, or mock.
*   Users have to consider special ordering requirements when interacting with
    global state: `func init`, whether flags are parsed yet, etc.

Provided the conditions above are avoided, there are a **few limited
circumstances under which these APIs are safe**, namely when any of the
following is true:

*   The global state is logically constant
    ([example](https://github.com/klauspost/compress/blob/290f4cfacb3eff892555a491e3eeb569a48665e7/zstd/snappy.go#L413)).
*   The package's observable behavior is stateless. For example, a public
    function may use a private global variable as a cache, but so long as the
    caller can't distinguish cache hits from misses, the function is stateless.
*   The global state does not bleed into things that are external to the
    program, like sidecar processes or files on a shared filesystem.
*   There is no expectation of predictable behavior
    ([example](https://pkg.go.dev/math/rand)).

> **Note:**
> [Sidecar processes](https://www.oreilly.com/library/view/designing-distributed-systems/9781491983638/ch02.html)
> may **not** strictly be process-local. They can and often are shared with more
> than one application process. Moreover, these sidecars often interact with
> external distributed systems.
>
> Further, the same stateless, idempotent, and local rules in addition to the
> base considerations above would apply to the code of the sidecar process
> itself!

An example of one of these safe situations is
[`package image`](https://pkg.go.dev/image) with its
[`image.RegisterFormat`](https://pkg.go.dev/image#RegisterFormat) function.
Consider the litmus tests from above applied to a typical decoder, like the one
for handling the [PNG](https://pkg.go.dev/image/png) format:

*   Multiple calls to `package image`'s APIs that use the registered decoders
    (for example, `image.Decode`) cannot interfere with one another, similarly
    for tests. The only exception is `image.RegisterFormat`, but that is
    mitigated by the points below.
*   It is extremely unlikely that a user would want to replace a decoder with a
    [test double], as the PNG decoder exemplifies a case in which our codebase's
    preference for real objects applies. However, a user would be more likely to
    replace a decoder with a test double if the decoder statefully interacted
    with operating system resources (for example, the network).
*   Collisions in registration are conceivable, though they are probably rare in
    practice.
*   The decoders are stateless, idempotent, and pure.

<a id="globals-default-instance"></a>
