---
source_name: "Google Go Style Guide"
source_url: "https://google.github.io/styleguide/go/"
source_path: "sources/raw/google-go-styleguide/guide.md"
license_ref: "sources/licenses/google-styleguide-LICENSE.txt"
---

# Go Style Guide
[Best practices](best-practices)
**Note:** This is part of a series of documents that outline [Go Style](index)
at Google. This document is **[normative](index#normative) and
[canonical](index#canonical)**. See [the overview](index#about) for more
information.
<a id="principles"></a>
## Style principles
There are a few overarching principles that summarize how to think about writing
readable Go code. The following are attributes of readable code, in order of
importance:
1.  **[Clarity]**: The code's purpose and rationale is clear to the reader.
1.  **[Simplicity]**: The code accomplishes its goal in the simplest way
    possible.
1.  **[Concision]**: The code has a high signal-to-noise ratio.
1.  **[Maintainability]**: The code is written such that it can be easily
    maintained.
1.  **[Consistency]**: The code is consistent with the broader Google codebase.
[Clarity]: #clarity
[Simplicity]: #simplicity
[Concision]: #concision
[Maintainability]: #maintainability
[Consistency]: #consistency
<a id="clarity"></a>
