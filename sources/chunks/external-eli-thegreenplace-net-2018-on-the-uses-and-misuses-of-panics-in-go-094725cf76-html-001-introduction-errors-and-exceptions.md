---
source_name: "External Linked Documentation"
source_url: "https://eli.thegreenplace.net/2018/on-the-uses-and-misuses-of-panics-in-go/"
source_path: "sources/raw/external/eli-thegreenplace-net-2018-on-the-uses-and-misuses-of-panics-in-go-094725cf76.html"
license_ref: ""
---

On the uses and misuses of panics in Go - Eli Bendersky's website
Go has a unique approach to error handling, with a combination of explicit error values and an exception-like panic mechanism. In this post I'm looking at the philosophical aspects of panic, trying to understand some of the conflicting guidelines coming from the Go team.
Most of all, it's a story of pragmatism in language design, with some musings on the merits and dangers of a pragmatic approach.
## Introduction - errors and exceptions

Many programming languages support exceptions as a standard way of handling errors - for example Java or Python. While certainly convenient, exceptions have many issues as well, which is why they're frowned upon by other languages or their style guides. The main criticism of exceptions is that they introduce a "side channel" for control flow; when reading the code, you also have to keep in mind the path in which exceptions can flow and this makes reasoning about some code very difficult [1].

Let's talk about error handling in Go to make this concrete. I assume you know how "standard" error handling in Go works - it's quite hard to miss! Here's how we open a file:

```go
f, err := os.Open("file.txt")
if err != nil {
  // handle error here
}
// do stuff with f here

```

If the file is missing, say, os.Open will return a non-nil error. In some other languages, errors are done differently. For example, Python's built-in open function will raise an exception if something is wrong:

```go
try:
  with open("file.txt") as f:
    # do stuff with f here
except OSError as err:
  # handle exception err here

```

While error handling via exceptions in Python is consistent, it's also a target of criticism because of its pervasiveness. Even iterators use exceptions to signal the end of a sequence (StopIteration). The main question is "what does _exceptional_ really mean?". Here's a relevant comment by Rob Pike from a mailing list discussion <https://groups.google.com/forum/#!topic/golang-nuts/HOXNBQu5c-Q%5B26-50%5D> where the modern incarnation of Go's panic/recover mechanism is proposed:
  This is exactly the kind of thing the proposal tries to avoid. Panic and recover are not an exception mechanism as usually defined because the usual approach, which ties exceptions to a control structure, encourages fine-grained exception handling that makes code unreadable in practice. There really is a difference between an error and what we call a panic, and we want that difference to matter. Consider Java, in which opening a file can throw an exception. In my experience few things are less exceptional than failing to open a file, and requiring me to write inside-out code to handle such a quotidian operation feels like a Procrustean imposition.
To be objective, exceptions have proponents that scoff at Go's explicit error handling for many reasons. For one, note the _order_ of the code in the two minimal samples above. In Python the primary flow of the program immediately follows the open call, and the error handling is delegated to a later stage (not to mention that in many cases the exception will be caught higher up the call stack and not in this function at all). In Go, on the other hand, error handling comes first and may obscure the main flow of the program. Moreover, Go's error handling is very verbose - this being one of the major criticisms of the language. I'll mention one potential way to address this later in the post.

In addition to Rob's quote above, Go's philosophy towards exceptions is summarized well in the FAQ <https://golang.org/doc/faq#exceptions>:
  We believe that coupling exceptions to a control structure, as in the try-catch-finally idiom, results in convoluted code. It also tends to encourage programmers to label too many ordinary errors, such as failing to open a file, as exceptional.
However, in some cases having an exception-like mechanism is actually useful; in a high-level language like Go it's even essential, I'd say. This is why panic and recover exist.
