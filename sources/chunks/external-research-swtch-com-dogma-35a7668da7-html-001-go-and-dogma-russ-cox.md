---
source_name: "External Linked Documentation"
source_url: "https://research.swtch.com/dogma"
source_path: "sources/raw/external/research-swtch-com-dogma-35a7668da7.html"
license_ref: ""
---

# Go and Dogma   Russ Cox

research!rsc: Go and Dogma
# Go and Dogma   Russ Cox
 January 9, 2017
 _research.swtch.com/dogma_
  Posted on Monday, January 9, 2017.

 [_Cross-posting from last year’s Go contributors AMA <https://www.reddit.com/r/golang/comments/46bd5h/ama_we_are_the_go_contributors_ask_us_anything/d05yyde/?context=3&st=ixq5hjko&sh=7affd469> on Reddit, because it’s still important to remember._]
 One of the perks of working on Go these past years has been the chance to have many great discussions with other language designers and implementers, for example about how well various design decisions worked out or the common problems of implementing what look like very different languages (for example both Go and Haskell need some kind of “green threads”, so there are more shared runtime challenges than you might expect). In one such conversation, when I was talking to a group of early Lisp hackers, one of them pointed out that these discussions are basically never dogmatic. Designers and implementers remember working through the good arguments on both sides of a particular decision, and they’re often eager to hear about someone else’s experience with what happens when you make that decision differently. Contrast that kind of discussion with the heated arguments or overly zealous statements you sometimes see from users of the same languages. There’s a real disconnect, possibly because the users don’t have the experience of weighing the arguments on both sides and don’t realize how easily a particular decision might have gone the other way.
 Language design and implementation is engineering. We make decisions using evaluations of costs and benefits or, if we must, using predictions of those based on past experience. I think we have an important responsibility to explain both sides of a particular decision, to make clear that the arguments for an alternate decision are actually good ones that we weighed and balanced, and to avoid the suggestion that particular design decisions approach dogma. I hope the Reddit AMA <https://www.reddit.com/r/golang/comments/46bd5h/ama_we_are_the_go_contributors_ask_us_anything/d05yyde/?context=3&st=ixq5hjko&sh=7affd469> as well as discussion on golang-nuts <https://groups.google.com/group/golang-nuts> or StackOverflow <http://stackoverflow.com/questions/tagged/go> or the Go Forum <https://forum.golangbridge.org/> or at conferences <https://golang.org/wiki/Conferences> help with that.
 But we need help from everyone. Remember that none of the decisions in Go are infallible; they’re just our best attempts at the time we made them, not wisdom received on stone tablets. If someone asks why Go does X instead of Y, please try to present the engineering reasons fairly, including for Y, and avoid argument solely by appeal to authority. It’s too easy to fall into the “well that’s just not how it’s done here” trap. And now that I know about and watch for that trap, I see it in nearly every technical community, although some more than others.
