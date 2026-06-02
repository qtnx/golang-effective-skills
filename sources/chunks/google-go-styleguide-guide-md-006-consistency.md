---
source_name: "Google Go Style Guide"
source_url: "https://google.github.io/styleguide/go/"
source_path: "sources/raw/google-go-styleguide/guide.md"
license_ref: "sources/licenses/google-styleguide-LICENSE.txt"
---

# Go Style Guide

### Consistency

Consistent code is code that looks, feels, and behaves like similar code
throughout the broader codebase, within the context of a team or package, and
even within a single file.

Consistency concerns do not override any of the principles above, but if a tie
must be broken, it is often beneficial to break it in favor of consistency.

Consistency within a package is often the most immediately important level of
consistency. It can be very jarring if the same problem is approached in
multiple ways throughout a package, or if the same concept has many names within
a file. However, even this should not override documented style principles or
global consistency.

<a id="core"></a>

# Go Style Guide

## Core guidelines

These guidelines collect the most important aspects of Go style that all Go code
is expected to follow. We expect that these principles be learned and followed
by the time readability is granted. These are not expected to change frequently,
and new additions will have to clear a high bar.

The guidelines below expand on the recommendations in [Effective Go], which
provide a common baseline for Go code across the entire community.

[Effective Go]: https://go.dev/doc/effective_go

<a id="formatting"></a>

### Formatting

All Go source files must conform to the format outputted by the `gofmt` tool.
This format is enforced by a presubmit check in the Google codebase.
[Generated code] should generally also be formatted (e.g., by using
[`format.Source`]), as it is also browsable in Code Search.

[Generated code]: https://docs.bazel.build/versions/main/be/general.html#genrule
[`format.Source`]: https://pkg.go.dev/go/format#Source

<a id="mixed-caps"></a>

### MixedCaps

Go source code uses `MixedCaps` or `mixedCaps` (camel case) rather than
underscores (snake case) when writing multi-word names.

This applies even when it breaks conventions in other languages. For example, a
constant is `MaxLength` (not `MAX_LENGTH`) if exported and `maxLength` (not
`max_length`) if unexported.

Local variables are considered [unexported] for the purpose of choosing the
initial capitalization.

[unexported]: https://go.dev/ref/spec#Exported_identifiers

<a id="line-length"></a>

### Line length

There is no fixed line length for Go source code. If a line feels too long,
prefer refactoring instead of splitting it. If it is already as short as it is
practical for it to be, the line should be allowed to remain long.

Do not split a line:

*   Before an [indentation change](decisions#indentation-confusion) (e.g.,
    function declaration, conditional)
*   To make a long string (e.g., a URL) fit into multiple shorter lines

<a id="naming"></a>

### Naming

Naming is more art than science. In Go, names tend to be somewhat shorter than
in many other languages, but the same [general guidelines] apply. Names should:

*   Not feel [repetitive](decisions#repetition) when they are used
*   Take the context into consideration
*   Not repeat concepts that are already clear

You can find more specific guidance on naming in [decisions](decisions#naming).

[general guidelines]: https://testing.googleblog.com/2017/10/code-health-identifiernamingpostforworl.html

<a id="local-consistency"></a>

### Local consistency

Where the style guide has nothing to say about a particular point of style,
authors are free to choose the style that they prefer, unless the code in close
proximity (usually within the same file or package, but sometimes within a team
or project directory) has taken a consistent stance on the issue.

Examples of **valid** local style considerations:

*   Use of `%s` or `%v` for formatted printing of errors
*   Usage of buffered channels in lieu of mutexes

Examples of **invalid** local style considerations:

*   Line length restrictions for code
*   Use of assertion-based testing libraries

If the local style disagrees with the style guide but the readability impact is
limited to one file, it will generally be surfaced in a code review for which a
consistent fix would be outside the scope of the CL in question. At that point,
it is appropriate to file a bug to track the fix.

If a change would worsen an existing style deviation, expose it in more API
surfaces, expand the number of files in which the deviation is present, or
introduce an actual bug, then local consistency is no longer a valid
justification for violating the style guide for new code. In these cases, it is
appropriate for the author to clean up the existing codebase in the same CL,
perform a refactor in advance of the current CL, or find an alternative that at
least does not make the local problem worse.
