---
source_name: "External Linked Documentation"
source_url: "https://go.dev/wiki/CodeReviewComments"
source_path: "sources/raw/external/go-dev-wiki-codereviewcomments-46376b7b23.html"
license_ref: ""
---

# Go Wiki: Go Code Review Comments

## Examples

When adding a new package, include examples of intended usage: a runnable Example, or a simple test demonstrating a complete call sequence.

Read more about testable Example() functions <https://go.dev/blog/examples>.

# Go Wiki: Go Code Review Comments

## Goroutine Lifetimes

When you spawn goroutines, make it clear when - or whether - they exit.

Goroutines can leak by blocking on channel sends or receives: the garbage collector will not terminate a goroutine even if the channels it is blocked on are unreachable.

Even when goroutines do not leak, leaving them in-flight when they are no longer needed can cause other subtle and hard-to-diagnose problems. Sends on closed channels panic. Modifying still-in-use inputs “after the result isn’t needed” can still lead to data races. And leaving goroutines in-flight for arbitrarily long can lead to unpredictable memory usage.

Try to keep concurrent code simple enough that goroutine lifetimes are obvious. If that just isn’t feasible, document when and why the goroutines exit.
