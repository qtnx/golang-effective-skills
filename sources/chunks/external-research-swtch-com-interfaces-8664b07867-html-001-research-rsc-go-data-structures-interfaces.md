---
source_name: "External Linked Documentation"
source_url: "https://research.swtch.com/interfaces"
source_path: "sources/raw/external/research-swtch-com-interfaces-8664b07867.html"
license_ref: ""
---

research!rsc: Go Data Structures: Interfaces
# Go Data Structures: Interfaces   Russ Cox
 December 1, 2009
 _research.swtch.com/interfaces_
  Posted on Tuesday, December 1, 2009.
Go's interfaces—static, checked at compile time, dynamic when asked for—are, for me, the most exciting part of Go from a language design point of view. If I could export one feature of Go into other languages, it would be interfaces.
 This post is my take on the implementation of interface values in the “gc” compilers: 6g, 8g, and 5g. Over at Airs, Ian Lance Taylor has written two <http://www.airs.com/blog/archives/277> posts <http://www.airs.com/blog/archives/276> about the implementation of interface values in `gccgo`. The implementations are more alike than different: the biggest difference is that this post has pictures.
Before looking at the implementation, let's get a sense of what it must support.
