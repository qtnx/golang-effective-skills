---
source_name: "Google Go Style Guide"
source_url: "https://google.github.io/styleguide/go/"
source_path: "sources/raw/google-go-styleguide/best-practices.md"
license_ref: "sources/licenses/google-styleguide-LICENSE.txt"
---

### Logging errors

Functions sometimes need to tell an external system about an error without
propagating it to their callers. Logging is an obvious choice here; but be
conscious of what and how you log errors.

*   Like [good test failure messages], log messages should clearly express what
    went wrong and help the maintainer by including relevant information to
    diagnose the problem.

*   Avoid duplication. If you return an error, it's usually better not to log it
    yourself but rather let the caller handle it. The caller can choose to log
    the error, or perhaps rate-limit logging using [`rate.Sometimes`]. Other
    options include attempting recovery or even [stopping the program]. In any
    case, giving the caller control helps avoid logspam.

    The downside to this approach, however, is that any logging is written using
    the caller's line coordinates.

*   Be careful with [PII]. Many log sinks are not appropriate destinations for
    sensitive end-user information.

*   Use `log.Error` sparingly. ERROR level logging causes a flush and is more
    expensive than lower logging levels. This can have serious performance
    impact on your code. When deciding between error and warning levels,
    consider the best practice that messages at the error level should be
    actionable rather than "more serious" than a warning.

*   Inside Google, we have monitoring systems that can be set up for more
    effective alerting than writing to a log file and hoping someone notices it.
    This is similar but not identical to the standard library
    [package `expvar`].

[good test failure messages]: https://google.github.io/styleguide/go/decisions#useful-test-failures
[stopping the program]: #checks-and-panics
[`rate.Sometimes`]: https://pkg.go.dev/golang.org/x/time/rate#Sometimes
[PII]: https://en.wikipedia.org/wiki/Personal_data
[package `expvar`]: https://pkg.go.dev/expvar

<a id="vlog"></a>
