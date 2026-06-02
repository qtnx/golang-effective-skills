---
source_name: "Google Go Style Guide"
source_url: "https://google.github.io/styleguide/go/"
source_path: "sources/raw/google-go-styleguide/index.md"
license_ref: "sources/licenses/google-styleguide-LICENSE.txt"
---

# Go Style
https://google.github.io/styleguide/go
[Best practices](best-practices)
<a id="about"></a>
## About

The Go Style Guide and accompanying documents codify the current best approaches
for writing readable and idiomatic Go. Adherence to the Style Guide is not
intended to be absolute, and these documents will never be exhaustive. Our
intention is to minimize the guesswork of writing readable Go so that newcomers
to the language can avoid common mistakes. The Style Guide also serves to unify
the style guidance given by anyone reviewing Go code at Google.

Document            | Link                                                  | Primary Audience    | [Normative] | [Canonical]
------------------- | ----------------------------------------------------- | ------------------- | ----------- | -----------
**Style Guide**     | https://google.github.io/styleguide/go/guide          | Everyone            | Yes         | Yes
**Style Decisions** | https://google.github.io/styleguide/go/decisions      | Readability Mentors | Yes         | No
**Best Practices**  | https://google.github.io/styleguide/go/best-practices | Anyone interested   | No          | No

[Normative]: #normative
[Canonical]: #canonical

<a id="docs"></a>

### Documents

1.  The **[Style Guide](https://google.github.io/styleguide/go/guide)** outlines
    the foundation of Go style at Google. This document is definitive and is
    used as the basis for the recommendations in Style Decisions and Best
    Practices.

1.  **[Style Decisions](https://google.github.io/styleguide/go/decisions)** is a
    more verbose document that summarizes decisions on specific style points and
    discusses the reasoning behind the decisions where appropriate.

    These decisions may occasionally change based on new data, new language
    features, new libraries, or emerging patterns, but it is not expected that
    individual Go programmers at Google should keep up-to-date with this
    document.

1.  **[Best Practices](https://google.github.io/styleguide/go/best-practices)**
    documents some of the patterns that have evolved over time that solve common
    problems, read well, and are robust to code maintenance needs.

    These best practices are not canonical, but Go programmers at Google are
    encouraged to use them where possible to keep the codebase uniform and
    consistent.

These documents intend to:

*   Agree on a set of principles for weighing alternate styles
*   Codify settled matters of Go style
*   Document and provide canonical examples for Go idioms
*   Document the pros and cons of various style decisions
*   Help minimize surprises in Go readability reviews
*   Help readability mentors use consistent terminology and guidance

These documents do **not** intend to:

*   Be an exhaustive list of comments that can be given in a readability review
*   List all of the rules everyone is expected to remember and follow at all
    times
*   Replace good judgment in the use of language features and style
*   Justify large-scale changes to get rid of style differences

There will always be differences from one Go programmer to another and from one
team's codebase to another. However, it is in the best interest of Google and
Alphabet that our codebase be as consistent as possible. (See
[guide](guide#consistency) for more on consistency.) To that end, feel free to
make style improvements as you see fit, but you do not need to nit-pick every
violation of the Style Guide that you find. In particular, these documents may
change over time, and that is no reason to cause extra churn in existing
codebases; it suffices to write new code using the latest best practices and
address nearby issues over time.

It is important to recognize that issues of style are inherently personal and
that there are always inherent trade-offs. Much of the guidance in these
documents is subjective, but just like with `gofmt`, there is significant value
in the uniformity they provide. As such, style recommendations will not be
changed without due discourse, Go programmers at Google are encouraged to follow
the style guide even where they might disagree.

<a id="definitions"></a>
