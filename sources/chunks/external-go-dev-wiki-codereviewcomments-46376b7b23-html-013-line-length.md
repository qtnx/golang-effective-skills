---
source_name: "External Linked Documentation"
source_url: "https://go.dev/wiki/CodeReviewComments"
source_path: "sources/raw/external/go-dev-wiki-codereviewcomments-46376b7b23.html"
license_ref: ""
---

# Go Wiki: Go Code Review Comments

## Line Length

There is no rigid line length limit in Go code, but avoid uncomfortably long lines. Similarly, don’t add line breaks to keep lines short when they are more readable long–for example, if they are repetitive.

Most of the time when people wrap lines “unnaturally” (in the middle of function calls or function declarations, more or less, say, though some exceptions are around), the wrapping would be unnecessary if they had a reasonable number of parameters and reasonably short variable names. Long lines seem to go with long names, and getting rid of the long names helps a lot.

In other words, break lines because of the semantics of what you’re writing (as a general rule) and not because of the length of the line. If you find that this produces lines that are too long, then change the names or the semantics and you’ll probably get a good result.

This is, actually, exactly the same advice about how long a function should be. There’s no rule “never have a function more than N lines long”, but there is definitely such a thing as too long of a function, and of too repetitive tiny functions, and the solution is to change where the function boundaries are, not to start counting lines.
