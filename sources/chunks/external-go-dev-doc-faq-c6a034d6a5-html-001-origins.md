---
source_name: "External Linked Documentation"
source_url: "https://go.dev/doc/faq"
source_path: "sources/raw/external/go-dev-doc-faq-c6a034d6a5.html"
license_ref: ""
---

# Frequently Asked Questions (FAQ)

Frequently Asked Questions (FAQ) - The Go Programming Language
# Frequently Asked Questions (FAQ)
## Origins

### What is the purpose of the project?

At the time of Go’s inception in 2007 the programming world was different from today. Production software was usually written in C++ or Java, GitHub did not exist, most computers were not yet multiprocessors, and other than Visual Studio and Eclipse there were few IDEs or other high-level tools available at all, let alone for free on the Internet.

Meanwhile, we had become frustrated by the undue complexity required to build large software projects with the languages we were using and their associated build systems. Computers had become enormously quicker since languages such as C, C++ and Java were first developed but the act of programming had not itself advanced nearly as much. Also, it was clear that multiprocessors were becoming universal but most languages offered little help to program them efficiently and safely.

We decided to take a step back and think about what major issues were going to dominate software engineering in the years ahead as technology developed, and how a new language might help address them. For instance, the rise of multicore CPUs argued that a language should provide first-class support for some sort of concurrency or parallelism. And to make resource management tractable in a large concurrent program, garbage collection, or at least some sort of safe automatic memory management was required.

These considerations led to a series of discussions <https://commandcenter.blogspot.com/2017/09/go-ten-years-and-climbing.html> from which Go arose, first as a set of ideas and desiderata, then as a language. An overarching goal was that Go do more to help the working programmer by enabling tooling, automating mundane tasks such as code formatting, and removing obstacles to working on large code bases.

A much more expansive description of the goals of Go and how they are met, or at least approached, is available in the article, Go at Google: Language Design in the Service of Software Engineering.

### What is the history of the project?

Robert Griesemer, Rob Pike and Ken Thompson started sketching the goals for a new language on the white board on September 21, 2007. Within a few days the goals had settled into a plan to do something and a fair idea of what it would be. Design continued part-time in parallel with unrelated work. By January 2008, Ken had started work on a compiler with which to explore ideas; it generated C code as its output. By mid-year the language had become a full-time project and had settled enough to attempt a production compiler. In May 2008, Ian Taylor independently started on a GCC front end for Go using the draft specification. Russ Cox joined in late 2008 and helped move the language and libraries from prototype to reality.

Go became a public open source project on November 10, 2009. Countless people from the community have contributed ideas, discussions, and code.

There are now millions of Go programmers—gophers—around the world, and there are more every day. Go’s success has far exceeded our expectations.

### What’s the origin of the gopher mascot?

The mascot and logo were designed by Renée French <https://reneefrench.blogspot.com>, who also designed Glenda <https://9p.io/plan9/glenda.html>, the Plan 9 bunny. A blog post about the gopher explains how it was derived from one she used for a WFMU <https://wfmu.org/> T-shirt design some years ago. The logo and mascot are covered by the Creative Commons Attribution 4.0 <https://creativecommons.org/licenses/by/4.0/> license.

The gopher has a model sheet illustrating his characteristics and how to represent them correctly. The model sheet was first shown in a talk <https://www.youtube.com/watch?v=4rw_B4yY69k> by Renée at Gophercon in 2016. He has unique features; he’s the _Go gopher_, not just any old gopher.

### Is the language called Go or Golang?

The language is called Go. The “golang” moniker arose because the web site was originally _golang.org_. (There was no _.dev_ domain then.) Many use the golang name, though, and it is handy as a label. For instance, the social media tag for the language is “#golang”. The language’s name is just plain Go, regardless.

A side note: Although the official logo has two capital letters, the language name is written Go, not GO.

### Why did you create a new language?

Go was born out of frustration with existing languages and environments for the work we were doing at Google. Programming had become too difficult and the choice of languages was partly to blame. One had to choose either efficient compilation, efficient execution, or ease of programming; all three were not available in the same mainstream language. Programmers who could were choosing ease over safety and efficiency by moving to dynamically typed languages such as Python and JavaScript rather than C++ or, to a lesser extent, Java.

We were not alone in our concerns. After many years with a pretty quiet landscape for programming languages, Go was among the first of several new languages—Rust, Elixir, Swift, and more—that have made programming language development an active, almost mainstream field again.

Go addressed these issues by attempting to combine the ease of programming of an interpreted, dynamically typed language with the efficiency and safety of a statically typed, compiled language. It also aimed to be better adapted to current hardware, with support for networked and multicore computing. Finally, working with Go is intended to be _fast_: it should take at most a few seconds to build a large executable on a single computer. Meeting these goals led us to rethink some of the programming approaches from our current languages, leading to: a compositional rather than hierarchical type system; support for concurrency and garbage collection; rigid specification of dependencies; and so on. These cannot be handled well by libraries or tools; a new language was called for.

The article Go at Google discusses the background and motivation behind the design of the Go language, as well as providing more detail about many of the answers presented in this FAQ.

### What are Go’s ancestors?

Go is mostly in the C family (basic syntax), with significant input from the Pascal/Modula/Oberon family (declarations, packages), plus some ideas from languages inspired by Tony Hoare’s CSP, such as Newsqueak and Limbo (concurrency). However, it is a new language across the board. In every respect the language was designed by thinking about what programmers do and how to make programming, at least the kind of programming we do, more effective, which means more fun.

### What are the guiding principles in the design?

When Go was designed, Java and C++ were the most commonly used languages for writing servers, at least at Google. We felt that these languages required too much bookkeeping and repetition. Some programmers reacted by moving towards more dynamic, fluid languages like Python, at the cost of efficiency and type safety. We felt it should be possible to have the efficiency, the safety, and the fluidity in a single language.

Go attempts to reduce the amount of typing in both senses of the word. Throughout its design, we have tried to reduce clutter and complexity. There are no forward declarations and no header files; everything is declared exactly once. Initialization is expressive, automatic, and easy to use. Syntax is clean and light on keywords. Repetition (`foo.Foo* myFoo = new(foo.Foo)`) is reduced by simple type derivation using the `:=` declare-and-initialize construct. And perhaps most radically, there is no type hierarchy: types just _are_, they don’t have to announce their relationships. These simplifications allow Go to be expressive yet comprehensible without sacrificing productivity.

Another important principle is to keep the concepts orthogonal. Methods can be implemented for any type; structures represent data while interfaces represent abstraction; and so on. Orthogonality makes it easier to understand what happens when things combine.
