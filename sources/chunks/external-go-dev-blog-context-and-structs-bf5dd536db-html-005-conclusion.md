---
source_name: "External Linked Documentation"
source_url: "https://go.dev/blog/context-and-structs"
source_path: "sources/raw/external/go-dev-blog-context-and-structs-bf5dd536db.html"
license_ref: ""
---

# The Go Blog

## Conclusion

Context makes it easy to propagate important cross-library and cross-API information down a calling stack. But, it must be used consistently and clearly in order to remain comprehensible, easy to debug, and effective.

When passed as the first argument in a method rather than stored in a struct type, users can take full advantage of its extensibility in order to build a powerful tree of cancellation, deadline, and metadata information through the call stack. And, best of all, its scope is clearly understood when it’s passed in as an argument, leading to clear comprehension and debuggability up and down the stack.

When designing an API with context, remember the advice: pass `context.Context` in as an argument; don’t store it in structs.

# The Go Blog

## Further reading

- Go Concurrency Patterns: Context (2014 blog post)

 **Next article: **Go Developer Survey 2020 Results
 **Previous article: **New module changes in Go 1.16
 **Blog Index**
