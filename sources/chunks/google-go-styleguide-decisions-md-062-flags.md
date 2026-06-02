---
source_name: "Google Go Style Guide"
source_url: "https://google.github.io/styleguide/go/"
source_path: "sources/raw/google-go-styleguide/decisions.md"
license_ref: "sources/licenses/google-styleguide-LICENSE.txt"
---

### Flags

<a id="TOC-Flags"></a>

Go programs in the Google codebase use an internal variant of the
[standard `flag` package]. It has a similar interface but interoperates well
with internal Google systems. Flag names in Go binaries should prefer to use
underscores to separate words, though the variables that hold a flag's value
should follow the standard Go name style ([mixed caps]). Specifically, the flag
name should be in snake case, and the variable name should be the equivalent
name in camel case.

```go
// Good:
var (
    pollInterval = flag.Duration("poll_interval", time.Minute, "Interval to use for polling.")
)
```

```go
// Bad:
var (
    poll_interval = flag.Int("pollIntervalSeconds", 60, "Interval to use for polling in seconds.")
)
```

Flags must only be defined in `package main` or equivalent.

General-purpose packages should be configured using Go APIs, not by punching
through to the command-line interface; don't let importing a library export new
flags as a side effect. That is, prefer explicit function arguments or struct
field assignment or much less frequently and under the strictest of scrutiny
exported global variables. In the extremely rare case that it is necessary to
break this rule, the flag name must clearly indicate the package that it
configures.

If your flags are global variables, place them in their own `var` group,
following the imports section.

There is additional discussion around best practices for creating [complex CLIs]
with subcommands.

See also:

*   [Tip of the Week #45: Avoid Flags, Especially in Library Code][totw-45]
*   [Go Tip #10: Configuration Structs and Flags](https://google.github.io/styleguide/go/index.html#gotip)
*   [Go Tip #80: Dependency Injection Principles](https://google.github.io/styleguide/go/index.html#gotip)

[standard `flag` package]: https://golang.org/pkg/flag/
[mixed caps]: guide#mixed-caps
[complex CLIs]: best-practices#complex-clis
[totw-45]: https://abseil.io/tips/45

<a id="logging"></a>
