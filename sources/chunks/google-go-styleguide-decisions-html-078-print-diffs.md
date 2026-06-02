---
source_name: "Google Go Style Guide"
source_url: "https://google.github.io/styleguide/go/"
source_path: "sources/raw/google-go-styleguide/decisions.html"
license_ref: "sources/licenses/google-styleguide-LICENSE.txt"
---

### Print diffs

If your function returns large output then it can be hard for someone reading the failure message to find the differences when your test fails. Instead of printing both the returned value and the wanted value, make a diff.

To compute diffs for such values, `cmp.Diff` is preferred, particularly for new tests and new code, but other tools may be used. See types of equality for guidance regarding the strengths and weaknesses of each function.

-
`cmp.Diff`

-
`pretty.Compare`

You can use the `diff` package to compare multi-line strings or lists of strings. You can use this as a building block for other kinds of diffs.

Add some text to your failure message explaining the direction of the diff.

-
Something like `diff (-want +got)` is good when you’re using the `cmp`, `pretty`, and `diff` packages (if you pass `(want, got)` to the function), because the `-` and `+` that you add to your format string will match the `-` and `+` that actually appear at the beginning of the diff lines. If you pass `(got, want)` to your function, the correct key would be `(-got +want)` instead.

-
The `messagediff` package uses a different output format, so the message `diff (want -> got)` is appropriate when you’re using it (if you pass `(want, got)` to the function), because the direction of the arrow will match the direction of the arrow in the “modified” lines.

The diff will span multiple lines, so you should print a newline before you print the diff.
