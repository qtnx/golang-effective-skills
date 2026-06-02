---
source_name: "Google Go Style Guide"
source_url: "https://google.github.io/styleguide/go/"
source_path: "sources/raw/google-go-styleguide/guide.html"
license_ref: "sources/licenses/google-styleguide-LICENSE.txt"
---

### Local consistency

Where the style guide has nothing to say about a particular point of style, authors are free to choose the style that they prefer, unless the code in close proximity (usually within the same file or package, but sometimes within a team or project directory) has taken a consistent stance on the issue.

Examples of **valid** local style considerations:

- Use of `%s` or `%v` for formatted printing of errors
- Usage of buffered channels in lieu of mutexes

Examples of **invalid** local style considerations:

- Line length restrictions for code
- Use of assertion-based testing libraries

If the local style disagrees with the style guide but the readability impact is limited to one file, it will generally be surfaced in a code review for which a consistent fix would be outside the scope of the CL in question. At that point, it is appropriate to file a bug to track the fix.

If a change would worsen an existing style deviation, expose it in more API surfaces, expand the number of files in which the deviation is present, or introduce an actual bug, then local consistency is no longer a valid justification for violating the style guide for new code. In these cases, it is appropriate for the author to clean up the existing codebase in the same CL, perform a refactor in advance of the current CL, or find an alternative that at least does not make the local problem worse.
   This site is open source. Improve this page.
