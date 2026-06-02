---
source_name: "External Linked Documentation"
source_url: "https://go.dev/doc/faq"
source_path: "sources/raw/external/go-dev-doc-faq-c6a034d6a5.html"
license_ref: ""
---

# Frequently Asked Questions (FAQ)

## Performance

### Why does Go perform badly on benchmark X?

One of Go’s design goals is to approach the performance of C for comparable programs, yet on some benchmarks it does quite poorly, including several in golang.org/x/exp/shootout <https://go.googlesource.com/exp/+/master/shootout/>. The slowest depend on libraries for which versions of comparable performance are not available in Go. For instance, pidigits.go <https://go.googlesource.com/exp/+/master/shootout/pidigits.go> depends on a multi-precision math package, and the C versions, unlike Go’s, use GMP <https://gmplib.org/> (which is written in optimized assembler). Benchmarks that depend on regular expressions (regex-dna.go <https://go.googlesource.com/exp/+/master/shootout/regex-dna.go>, for instance) are essentially comparing Go’s native regexp package to mature, highly optimized regular expression libraries like PCRE.

Benchmark games are won by extensive tuning and the Go versions of most of the benchmarks need attention. If you measure truly comparable C and Go programs (reverse-complement.go <https://go.googlesource.com/exp/+/master/shootout/reverse-complement.go> is one example), you’ll see the two languages are much closer in raw performance than this suite would indicate.

Still, there is room for improvement. The compilers are good but could be better, many libraries need major performance work, and the garbage collector isn’t fast enough yet. (Even if it were, taking care not to generate unnecessary garbage can have a huge effect.)

In any case, Go can often be very competitive. There has been significant improvement in the performance of many programs as the language and tools have developed. See the blog post about profiling Go programs for an informative example. It’s quite old but still contains helpful information.
