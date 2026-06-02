---
source_name: "External Linked Documentation"
source_url: "https://research.swtch.com/godata"
source_path: "sources/raw/external/research-swtch-com-godata-4c4e9825fb.html"
license_ref: ""
---

# Go Data Structures   Russ Cox

## Strings

With those preliminaries, we can move on to more interesting data types.

(The gray arrows denote pointers that are present in the implementation but not directly visible in programs.)

A `string` is represented in memory as a 2-word structure containing a pointer to the string data and a length. Because the `string` is immutable, it is safe for multiple strings to share the same storage, so slicing <http://www.blogger.com/post-edit.g?blogID=8082954141980125536&postID=65253524121904390> `s` results in a new 2-word structure with a potentially different pointer and length that still refers to the same byte sequence. This means that slicing can be done without allocation or copying, making string slices as efficient as passing around explicit indexes.

(As an aside, there is a well-known gotcha <http://bugs.sun.com/bugdatabase/view_bug.do?bug_id=4513622> in Java and other languages that when you slice a string to save a small piece, the reference to the original keeps the entire original string in memory even though only a small amount is still needed. Go has this gotcha too. The alternative, which we tried and rejected <http://code.google.com/p/go/source/detail?r=70fa38e5a5bb>, is to make string slicing so expensive—an allocation and a copy—that most programs avoid it.)
