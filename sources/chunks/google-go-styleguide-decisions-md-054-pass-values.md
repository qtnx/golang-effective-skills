---
source_name: "Google Go Style Guide"
source_url: "https://google.github.io/styleguide/go/"
source_path: "sources/raw/google-go-styleguide/decisions.md"
license_ref: "sources/licenses/google-styleguide-LICENSE.txt"
---

### Pass values

<a id="TOC-PassValues"></a>

Do not pass pointers as function arguments just to save a few bytes. If a
function reads its argument `x` only as `*x` throughout, then the argument
shouldn't be a pointer. Common instances of this include passing a pointer to a
string (`*string`) or a pointer to an interface value (`*io.Reader`). In both
cases, the value itself is a fixed size and can be passed directly.

This advice does not apply to large structs, or even small structs that may
increase in size. In particular, protocol buffer messages should generally be
handled by pointer rather than by value. The pointer type satisfies the
`proto.Message` interface (accepted by `proto.Marshal`, `protocmp.Transform`,
etc.), and protocol buffer messages can be quite large and often grow larger
over time.

<a id="receiver-type"></a>
