---
source_name: "Google Go Style Guide"
source_url: "https://google.github.io/styleguide/go/"
source_path: "sources/raw/google-go-styleguide/best-practices.md"
license_ref: "sources/licenses/google-styleguide-LICENSE.txt"
---

## Complex command-line interfaces

Some programs wish to present users with a rich command-line interface that
includes sub-commands. For example, `kubectl create`, `kubectl run`, and many
other sub-commands are all provided by the program `kubectl`. There are at least
the following libraries in common use for achieving this.

If you don't have a preference or other considerations are equal, [subcommands]
is recommended, since it is the simplest and is easy to use correctly. However,
if you need different features that it doesn't provide, pick one of the other
options.

*   **[cobra]**

    *   Flag convention: getopt
    *   Common outside the Google codebase.
    *   Many extra features.
    *   Pitfalls in usage (see below).

*   **[subcommands]**

    *   Flag convention: Go
    *   Simple and easy to use correctly.
    *   Recommended if you don't need extra features.

**Warning**: cobra command functions should use `cmd.Context()` to obtain a
context rather than creating their own root context with `context.Background`.
Code that uses the subcommands package already receives the correct context as a
function parameter.

You are not required to place each subcommand in a separate package, and it is
often not necessary to do so. Apply the same considerations about package
boundaries as in any Go codebase. If your code can be used both as a library and
as a binary, it is usually beneficial to separate the CLI code and the library,
making the CLI just one more of its clients. (This is not specific to CLIs that
have subcommands, but is mentioned here because it is a common place where it
comes up.)

[subcommands]: https://pkg.go.dev/github.com/google/subcommands
[cobra]: https://pkg.go.dev/github.com/spf13/cobra

<a id="tests"></a>
