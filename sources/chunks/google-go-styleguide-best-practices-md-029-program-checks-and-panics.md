---
source_name: "Google Go Style Guide"
source_url: "https://google.github.io/styleguide/go/"
source_path: "sources/raw/google-go-styleguide/best-practices.md"
license_ref: "sources/licenses/google-styleguide-LICENSE.txt"
---

### Program checks and panics

As stated in the [decision against panics], standard error handling should be
structured around error return values. Libraries should prefer returning an
error to the caller rather than aborting the program, especially for transient
errors.

It is occasionally necessary to perform consistency checks on an invariant and
terminate the program if it is violated. In general, this is only done when a
failure of the invariant check means that the internal state has become
unrecoverable. The most reliable way to do this in the Google codebase is to
call `log.Fatal`. Using `panic` in these cases is not reliable, because it is
possible for deferred functions to deadlock or further corrupt internal or
external state.

Similarly, resist the temptation to recover panics to avoid crashes, as doing so
can result in propagating a corrupted state. The further you are from the panic,
the less you know about the state of the program, which could be holding locks
or other resources. The program can then develop other unexpected failure modes
that can make the problem even more difficult to diagnose. Instead of trying to
handle unexpected panics in code, use monitoring tools to surface unexpected
failures and fix related bugs with a high priority.

**Note:** The standard [`net/http` server] violates this advice and recovers
panics from request handlers. Consensus among experienced Go engineers is that
this was a historical mistake. If you sample server logs from application
servers in other languages, it is common to find large stacktraces that are left
unhandled. Avoid this pitfall in your servers.

[decision against panics]: https://google.github.io/styleguide/go/decisions#dont-panic
[`net/http` server]: https://pkg.go.dev/net/http#Server

<a id="when-to-panic"></a>
