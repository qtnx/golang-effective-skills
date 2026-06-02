---
source_name: "External Linked Documentation"
source_url: "https://commandcenter.blogspot.com/2012/06/less-is-exponentially-more.html"
source_path: "sources/raw/external/commandcenter-blogspot-com-2012-06-less-is-exponentially-more-html-b48cdd4bca.html"
license_ref: ""
---

command center: Less is exponentially more

###  Less is exponentially more

 Here is the text of the talk I gave at the Go SF meeting in June, 2012.

 This is a personal talk. I do not speak for anyone else on the Go team here, although I want to acknowledge right up front that the team is what made and continues to make Go happen. I'd also like to thank the Go SF organizers for giving me the opportunity to talk to you.

 I was asked a few weeks ago, "What was the biggest surprise you encountered rolling out Go?" I knew the answer instantly: Although we expected C++ programmers to see Go as an alternative, instead most Go programmers come from languages like Python and Ruby. Very few come from C++.

 We—Ken, Robert and myself—were C++ programmers when we designed a new language to solve the problems that we thought needed to be solved for the kind of software we wrote. It seems almost paradoxical that other C++ programmers don't seem to care.

 I'd like to talk today about what prompted us to create Go, and why the result should not have surprised us like this. I promise this will be more about Go than about C++, and that if you don't know C++ you'll be able to follow along.

 The answer can be summarized like this: Do you think less is more, or less is less?

 Here is a metaphor, in the form of a true story.  Bell Labs centers were originally assigned three-letter numbers: 111 for Physics Research, 127 for Computing Sciences Research, and so on. In the early 1980s a memo came around announcing that as our understanding of research had grown, it had become necessary to add another digit so we could better characterize our work. So our center became 1127. Ron Hardin joked, half-seriously, that if we really understood our world better, we could drop a digit and go down from 127 to just 27. Of course management didn't get the joke, nor were they expected to, but I think there's wisdom in it. Less can be more. The better you understand, the pithier you can be.

 Keep that idea in mind.

 Back around September 2007, I was doing some minor but central work on an enormous Google C++ program, one you've all interacted with, and my compilations were taking about 45 minutes on our huge distributed compile cluster. An announcement came around that there was going to be a talk presented by a couple of Google employees serving on the C++ standards committee. They were going to tell us what was coming in C++0x, as it was called at the time. (It's now known as C++11).

 In the span of an hour at that talk we heard about something like 35 new features that were being planned. In fact there were many more, but only 35 were described in the talk. Some of the features were minor, of course, but the ones in the talk were at least significant enough to call out. Some were very subtle and hard to understand, like rvalue references, while others are especially C++-like, such as variadic templates, and some others are just crazy, like user-defined literals.

 At this point I asked myself a question: Did the C++ committee really believe that was wrong with C++ was that it didn't have enough features? Surely, in a variant of Ron Hardin's joke, it would be a greater achievement to simplify the language rather than to add to it. Of course, that's ridiculous, but keep the idea in mind.

 Just a few months before that C++ talk I had given a talk myself, which you can see on YouTube <https://www.youtube.com/watch?v=hB05UFqOtFA>, about a toy concurrent language I had built way back in the 1980s. That language was called Newsqueak <http://swtch.com/~rsc/thread/newsqueak.pdf> and of course it is a precursor to Go.

 I gave that talk because there were ideas in Newsqueak that I missed in my work at Google and I had been thinking about them again.  I was convinced they would make it easier to write server code and Google could really benefit from that.

 I actually tried and failed to find a way to bring the ideas to C++. It was too difficult to couple the concurrent operations with C++'s control structures, and in turn that made it too hard to see the real advantages. Plus C++ just made it all seem too cumbersome, although I admit I was never truly facile in the language. So I abandoned the idea.

 But the C++0x talk got me thinking again.  One thing that really bothered me—and I think Ken and Robert as well—was the new C++ memory model with atomic types. It just felt wrong to put such a microscopically-defined set of details into an already over-burdened type system. It also seemed short-sighted, since it's likely that hardware will change significantly in the next decade and it would be unwise to couple the language too tightly to today's hardware.

 We returned to our offices after the talk. I started another compilation, turned my chair around to face Robert, and started asking pointed questions. Before the compilation was done, we'd roped Ken in and had decided to do something. We did not want to be writing in C++ forever, and we—me especially—wanted to have concurrency at my fingertips when writing Google code. We also wanted to address the problem of "programming in the large" head on, about which more later.

 We wrote on the white board a bunch of stuff that we wanted, desiderata if you will. We thought big, ignoring detailed syntax and semantics and focusing on the big picture.

 I still have a fascinating mail thread from that week. Here are a couple of excerpts:

 Robert: _Starting point: C, fix some obvious flaws, remove crud, add a few missing features._

 Rob: _name: 'go'.  you can invent reasons for this name but it has nice properties. it's short, easy to type. tools: goc, gol, goa.  if there's an interactive debugger/interpreter it could just be called 'go'.  the suffix is .go._

 Robert: _Empty interfaces: interface {}. These are implemented by all interfaces, and thus this could take the place of void*._

 We didn't figure it all out right away. For instance, it took us over a year to figure out arrays and slices. But a significant amount of the flavor of the language emerged in that first couple of days.

 Notice that Robert said C was the starting point, not C++. I'm not certain but I believe he meant C proper, especially because Ken was there. But it's also true that, in the end, we didn't really start from C. We built from scratch, borrowing only minor things like operators and brace brackets and a few common keywords. (And of course we also borrowed ideas from other languages we knew.) In any case, I see now that we reacted to C++ by going back down to basics, breaking it all down and starting over. We weren't trying to design a better C++, or even a better C. It was to be a better language overall for the kind of software we cared about.

 In the end of course it came out quite different from either C or C++. More different even than many realize. I made a list of significant simplifications in Go over C and C++:

- regular syntax (don't need a symbol table to parse)

- garbage collection (only)

- no header files

- explicit dependencies

- no circular dependencies

- constants are just numbers

- int and int32 are distinct types

- letter case sets visibility

- methods for any type (no classes)

- no subtype inheritance (no subclasses)

- package-level initialization and well-defined order of initialization

- files compiled together in a package

- package-level globals presented in any order

- no arithmetic conversions (constants help)

- interfaces are implicit (no "implements" declaration)

- embedding (no promotion to superclass)

- methods are declared as functions (no special location)

- methods are just functions

- interfaces are just methods (no data)

- methods match by name only (not by type)

- no constructors or destructors

- postincrement and postdecrement are statements, not expressions

- no preincrement or predecrement

- assignment is not an expression

- evaluation order defined in assignment, function call (no "sequence point")

- no pointer arithmetic

- memory is always zeroed

- legal to take address of local variable

- no "this" in methods

- segmented stacks

- no const or other type annotations

- no templates

- no exceptions

- builtin string, slice, map

- array bounds checking

 And yet, with that long list of simplifications and missing pieces, Go is, I believe, more expressive than C or C++. Less can be more.

 But you can't take out everything. You need building blocks such as an idea about how types behave, and syntax that works well in practice, and some ineffable thing that makes libraries interoperate well.

 We also added some things that were not in C or C++, like slices and maps, composite literals, expressions at the top level of the file (which is a huge thing that mostly goes unremarked), reflection, garbage collection, and so on. Concurrency, too, naturally.

 One thing that is conspicuously absent is of course a type hierarchy. Allow me to be rude about that for a minute.

 Early in the rollout of Go I was told by someone that he could not imagine working in a language without generic types. As I have reported elsewhere, I found that an odd remark.
