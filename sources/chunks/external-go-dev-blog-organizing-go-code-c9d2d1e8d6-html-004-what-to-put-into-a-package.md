---
source_name: "External Linked Documentation"
source_url: "https://go.dev/blog/organizing-go-code"
source_path: "sources/raw/external/go-dev-blog-organizing-go-code-c9d2d1e8d6.html"
license_ref: ""
---

# The Go Blog

## What to put into a package

It is easy to just throw everything into a “grab bag” package, but this dilutes the meaning of the package name (as it must encompass a lot of functionality) and forces the users of small parts of the package to compile and link a lot of unrelated code.

On the other hand, it is also easy to go overboard in splitting your code into small packages, in which case you will likely become bogged down in interface design, rather than just getting the job done.

Look to the Go standard libraries as a guide. Some of its packages are large and some are small. For instance, the http package comprises 17 go source files (excluding tests) and exports 109 identifiers, and the hash package consists of one file that exports just three declarations. There is no hard and fast rule; both approaches are appropriate given their context.

With that said, package main is often larger than other packages. Complex commands contain a lot of code that is of little use outside the context of the executable, and often it’s simpler to just keep it all in the one place. For instance, the go tool is more than 12000 lines spread across 34 files.

# The Go Blog

## Document your code

Good documentation is an essential quality of usable and maintainable code. Read the Godoc: documenting Go code article to learn how to write good doc comments.

 **Next article: **Go updates in App Engine 1.7.1
 **Previous article: **Gccgo in GCC 4.7.1
 **Blog Index**
