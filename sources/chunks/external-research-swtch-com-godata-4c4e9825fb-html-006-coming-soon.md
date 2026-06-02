---
source_name: "External Linked Documentation"
source_url: "https://research.swtch.com/godata"
source_path: "sources/raw/external/research-swtch-com-godata-4c4e9825fb.html"
license_ref: ""
---

# Go Data Structures   Russ Cox

## Coming soon...

This has already gotten a bit long. Interface values, maps, and channels will have to wait for future posts.

-
tivadj <http://www.blogger.com/profile/03184942757622768273> (November 24, 2009 12:57 PM) So what about Go performance comparing to something from C,C++; Java or C#? Expected degrade about -5% ?

-
Dubhead <http://www.blogger.com/profile/06768222333602596397> (November 24, 2009 6:22 PM) Thank you for the article, it re-arranged my understanding of the topic.

Two possible corrections:

In 'Slices', 'x[0:4] is a valid slice expression' should be something like 'if y:=x[1:3], then y[0:4] is valid slice expression'.

In 'new and make' diagram, new(Rect) should be new(Rect1).

-
Artyom Shalkhakov <http://www.blogger.com/profile/08658644954244073101> (November 24, 2009 7:28 PM) You've shown that types in Go prescribe memory layout of data.

I wonder whether it's possible to describe certain invariants using the type system of Go?

-
tav <http://www.blogger.com/profile/08305590711045918911> (November 24, 2009 7:49 PM) This post has been removed by the author.

-
tav <http://www.blogger.com/profile/08305590711045918911> (November 24, 2009 7:51 PM) Hey Russ,

Thanks for such an informative article. As a Python coder coming to Go, I was wondering if you would consider a series of "best Go patterns" for future articles?

I — and probably a good number of others — are fairly clueless when it comes to issues of memory allocation, optimisation, etc. So it would be super helpful to learn better ways of doing things by way of comparison of "good" and "bad" ways of solving the same problem in Go…

In any case, I look forward to your follow-up post on maps, interfaces and channels. Thanks!

-- tav@espians.com

-
Julian Morrison <http://www.blogger.com/profile/01115506275519545033> (November 25, 2009 2:07 AM) What is the utility of disallowing an index beyond the slice, but allowing a new slice up to the capacity? Is it to give something approximating the fill pointer of Java's Buffer interface?

-
Russ Cox <http://swtch.com/~rsc/> (November 29, 2009 10:07 PM) @tivadj: That's certainly the goal. You can look at the shootout site to see real comparisons. Note that what passes for C or C++ in those benchmarks typically has liberal amounts of asm sprinkled in.

@Dubhead: Thanks; fixed.

@Artyom: What kinds of invariants are you wondering about?

@tav: There's already a document that tries to do that: http://golang.org/doc/effective_go.html.

@Julian: see the slices section of http://golang.org/doc/effective_go.html.
It helps catch out-of-bounds errors to disallow
indexing past len, because in most usage, the
data past len does not contain anything useful.

-
Artyom Shalkhakov <http://www.blogger.com/profile/08658644954244073101> (December 3, 2009 11:35 PM) @rsc: For instance, I'd like my compiler to check an array out-of-bounds access for me. There are research prototypes (e.g., ATS), but it would be great to get this one in a practical programming language. :)

-
MikeZ <http://www.blogger.com/profile/07315908327101747020> (December 5, 2009 7:00 AM) A question about garbage collection of strings. Let's say we have a string and a slice of it:

s := "hello" // ptr to "hello"
t := s[2:2] // ptr to "llo"
s = "goodbye" // "hello" now garbage?

What happens to t if the current garbage collector collects after the last assignment to s? Is the current GC smart enough to recognize that t points to the interior of "hello", so "hello" should not be collected?

-
Brian Bulkowski <http://www.blogger.com/profile/05386052998550318388> (December 6, 2009 4:06 PM) I believe the 'shootout' site is a poor measure for what I use languages for. I expect to use strings, hashes, and lists liberally; those tests avoid those structures and concentrate on loops and read and write.

That having been said, shootout claims Go is on the same level as Erlang, and nowhere near C.

I looked at a few of the C programs; none included asm() statements. The binary tree functionality is 20x slower in Go than C.

I'm willing to believe that Go is immature and needs work, but to hear people claim "go is meeting its goals" when it's 20x slower than C (instead of 20 percent slower) steams me.

-
Russ Cox <http://swtch.com/~rsc/> (December 6, 2009 4:51 PM) @Brian:

The binary tree shootout is not a binary tree benchmark. It's a garbage collection benchmark, and Go's garbage collector is pretty slow. On the other hand, it has one, unlike C, and it will get better.

If you look at real computation, instead of libraries, Go is holding its own with equivalent C code. reverse-complement is now pretty much tied with the equivalent C program (not yet on the site, but in the Go repository), mandelbrot is 10% slower, nbody is 50% slower only because it doesn't inline the call to sqrt.

Also, who said Go was meeting its performance goas? I think it's doing pretty well for a rough implementation, but there is plenty of room for improvement and lots of low-hanging fruit.

-
Greg <http://www.blogger.com/profile/00287001698993178575> (April 4, 2011 11:19 PM) really excellent description, thanks Russ.
