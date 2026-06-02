---
source_name: "Google Go Style Guide"
source_url: "https://google.github.io/styleguide/go/"
source_path: "sources/raw/google-go-styleguide/decisions.md"
license_ref: "sources/licenses/google-styleguide-LICENSE.txt"
---

## Naming

### Getters

<a id="TOC-Getters"></a>

Function and method names should not use a `Get` or `get` prefix, unless the
underlying concept uses the word "get" (e.g. an HTTP GET). Prefer starting the
name with the noun directly, for example use `Counts` over `GetCounts`.

If the function involves performing a complex computation or executing a remote
call, a different word like `Compute` or `Fetch` can be used in place of `Get`,
to make it clear to a reader that the function call may take time and could
block or fail.

<a id="variable-names"></a>

## Naming

### Variable names

<a id="TOC-VariableNames"></a>

The general rule of thumb is that the length of a name should be proportional to
the size of its scope and inversely proportional to the number of times that it
is used within that scope. A variable created at file scope may require multiple
words, whereas a variable scoped to a single inner block may be a single word or
even just a character or two, to keep the code clear and avoid extraneous
information.

Here is a rough baseline. These numeric guidelines are not strict rules. Apply
judgement based on context, [clarity], and [concision].

*   A small scope is one in which one or two small operations are performed, say
    1-7 lines.
*   A medium scope is a few small or one large operation, say 8-15 lines.
*   A large scope is one or a few large operations, say 15-25 lines.
*   A very large scope is anything that spans more than a page (say, more than
    25 lines).

[clarity]: guide#clarity
[concision]: guide#concision

A name that might be perfectly clear (e.g., `c` for a counter) within a small
scope could be insufficient in a larger scope and would require clarification to
remind the reader of its purpose further along in the code. A scope in which
there are many variables, or variables that represent similar values or
concepts, may necessitate longer variable names than the scope suggests.

The specificity of the concept can also help to keep a variable's name concise.
For example, assuming there is only a single database in use, a short variable
name like `db` that might normally be reserved for very small scopes may remain
perfectly clear even if the scope is very large. In this case, a single word
`database` is likely acceptable based on the size of the scope, but is not
required as `db` is a very common shortening for the word with few alternate
interpretations.

The name of a local variable should reflect what it contains and how it is being
used in the current context, rather than where the value originated. For
example, it is often the case that the best local variable name is not the same
as the struct or protocol buffer field name.

In general:

*   Single-word names like `count` or `options` are a good starting point.
*   Additional words can be added to disambiguate similar names, for example
    `userCount` and `projectCount`.
*   Do not simply drop letters to save typing. For example `Sandbox` is
    preferred over `Sbx`, particularly for exported names.
*   Omit [types and type-like words] from most variable names.
    *   For a number, `userCount` is a better name than `numUsers` or
        `usersInt`.
    *   For a slice, `users` is a better name than `userSlice`.
    *   It is acceptable to include a type-like qualifier if there are two
        versions of a value in scope, for example you might have an input stored
        in `ageString` and use `age` for the parsed value.
*   Omit words that are clear from the [surrounding context]. For example, in
    the implementation of a `UserCount` method, a local variable called
    `userCount` is probably redundant; `count`, `users`, or even `c` are just as
    readable.

[types and type-like words]: #repetitive-with-type
[surrounding context]: #repetitive-in-context

<a id="v"></a>

#### Single-letter variable names

Single-letter variable names can be a useful tool to minimize
[repetition](#repetition), but can also make code needlessly opaque. Limit their
use to instances where the full word is obvious and where it would be repetitive
for it to appear in place of the single-letter variable.

In general:

*   For a [method receiver variable], a one-letter or two-letter name is
    preferred.
*   Using familiar variable names for common types is often helpful:
    *   `r` for an `io.Reader` or `*http.Request`
    *   `w` for an `io.Writer` or `http.ResponseWriter`
*   Single-letter identifiers are acceptable as integer loop variables,
    particularly for indices (e.g., `i`) and coordinates (e.g., `x` and `y`).
*   Abbreviations can be acceptable loop identifiers when the scope is short,
    for example `for _, n := range nodes { ... }`.

[method receiver variable]: #receiver-names

<a id="repetition"></a>
