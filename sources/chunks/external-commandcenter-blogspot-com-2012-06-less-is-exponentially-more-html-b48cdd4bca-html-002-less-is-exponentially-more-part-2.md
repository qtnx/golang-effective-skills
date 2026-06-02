---
source_name: "External Linked Documentation"
source_url: "https://commandcenter.blogspot.com/2012/06/less-is-exponentially-more.html"
source_path: "sources/raw/external/commandcenter-blogspot-com-2012-06-less-is-exponentially-more-html-b48cdd4bca.html"
license_ref: ""
---

To be fair he was probably saying in his own way that he really liked what the STL does for him in C++. For the purpose of argument, though, let's take his claim at face value.
 What it says is that he finds writing containers like lists of ints and maps of strings an unbearable burden. I find that an odd claim. I spend very little of my programming time struggling with those issues, even in languages without generic types.
 But more important, what it says is that _types_ are the way to lift that burden. _Types_. Not polymorphic functions or language primitives or helpers of other kinds, but _types_.
 That's the detail that sticks with me.
 Programmers who come to Go from C++ and Java miss the idea of programming with types, particularly inheritance and subclassing and all that. Perhaps I'm a philistine about types but I've never found that model particularly expressive.
 My late friend Alain Fournier once told me that he considered the lowest form of academic work to be taxonomy. And you know what? Type hierarchies are just taxonomy. You need to decide what piece goes in what box, every type's parent, whether A inherits from B or B from A.  Is a sortable array an array that sorts or a sorter represented by an array? If you believe that types address all design issues you must make that decision.
 I believe that's a preposterous way to think about programming. What matters isn't the ancestor relations between things but what they can do for you.
 That, of course, is where interfaces come into Go. But they're part of a bigger picture, the true Go philosophy.
 If C++ and Java are about type hierarchies and the taxonomy of types, Go is about composition.
 Doug McIlroy, the eventual inventor of Unix pipes, wrote in 1964 (!):
  We should have some ways of coupling programs like garden hose--screw in another segment when it becomes necessary to massage data in another way. This is the way of IO also. That is the way of Go also. Go takes that idea and pushes it very far. It is a language of composition and coupling.
 The obvious example is the way interfaces give us the composition of components. It doesn't matter what that thing is, if it implements method M I can just drop it in here.
 Another important example is how concurrency gives us the composition of independently executing computations.
 And there's even an unusual (and very simple) form of type composition: embedding.
 These compositional techniques are what give Go its flavor, which is profoundly different from the flavor of C++ or Java programs.
 ===========
 There's an unrelated aspect of Go's design I'd like to touch upon: Go was designed to help write big programs, written and maintained by big teams.
 There's this idea about "programming in the large" and somehow C++ and Java own that domain. I believe that's just a historical accident, or perhaps an industrial accident. But the widely held belief is that it has something to do with object-oriented design.
 I don't buy that at all. Big software needs methodology to be sure, but not nearly as much as it needs strong dependency management and clean interface abstraction and superb documentation tools, none of which is served well by C++ (although Java does noticeably better).
 We don't know yet, because not enough software has been written in Go, but I'm confident Go will turn out to be a superb language for programming in the large. Time will tell.
 ===========
 Now, to come back to the surprising question that opened my talk:
 Why does Go, a language designed from the ground up for what what C++ is used for, not attract more C++ programmers?
 Jokes aside, I think it's because Go and C++ are profoundly different philosophically.
 C++ is about having it all there at your fingertips. I found this quote on a C++11 FAQ:
  The range of abstractions that C++ can express elegantly, flexibly, and at zero costs compared to hand-crafted specialized code has greatly increased. That way of thinking just isn't the way Go operates. Zero cost isn't a goal, at least not zero CPU cost. Go's claim is that minimizing programmer effort is a more important consideration.
 Go isn't all-encompassing. You don't get everything built in. You don't have precise control of every nuance of execution. For instance, you don't have RAII. Instead you get a garbage collector. You don't even get a memory-freeing function.
 What you're given is a set of powerful but easy to understand, easy to use building blocks from which you can assemble—compose—a solution to your problem. It might not end up quite as fast or as sophisticated or as ideologically motivated as the solution you'd write in some of those other languages, but it'll almost certainly be easier to write, easier to read, easier to understand, easier to maintain, and maybe safer.
 To put it another way, oversimplifying of course:
 Python and Ruby programmers come to Go because they don't have to surrender much expressiveness, but gain performance and get to play with concurrency.
 C++ programmers _don't_ come to Go because they have fought hard to gain exquisite control of their programming domain, and don't want to surrender any of it. To them, software isn't just about getting the job done, it's about doing it a certain way.
 The issue, then, is that Go's success would contradict their world view.
 And we should have realized that from the beginning. People who are excited about C++11's new features are not going to care about a language that has so much less.  Even if, in the end, it offers so much more.
 Thank you.
   Newer Post <https://commandcenter.blogspot.com/2012/09/thank-you-apple.html>   Older Post <https://commandcenter.blogspot.com/2012/04/byte-order-fallacy.html>  Home <https://commandcenter.blogspot.com/>
