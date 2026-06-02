---
source_name: "External Linked Documentation"
source_url: "https://go.dev/blog/subtests"
source_path: "sources/raw/external/go-dev-blog-subtests-0e125eccbd.html"
license_ref: ""
---

# The Go Blog

## Conclusion

Go 1.7’s addition of subtests and sub-benchmarks allows you to write structured tests and benchmarks in a natural way that blends nicely into the existing tools. One way to think about this is that earlier versions of the testing package had a 1-level hierarchy: the package-level test was structured as a set of individual tests and benchmarks. Now that structure has been extended to those individual tests and benchmarks, recursively. In fact, in the implementation, the top-level tests and benchmarks are tracked as if they were subtests and sub-benchmarks of an implicit master test and benchmark: the treatment really is the same at all levels.

The ability for tests to define this structure enables fine-grained execution of specific test cases, shared setup and teardown, and better control over test parallelism. We are excited to see what other uses people find. Enjoy.

 **Next article: **Introducing HTTP Tracing
 **Previous article: **Smaller Go 1.7 binaries
 **Blog Index**
