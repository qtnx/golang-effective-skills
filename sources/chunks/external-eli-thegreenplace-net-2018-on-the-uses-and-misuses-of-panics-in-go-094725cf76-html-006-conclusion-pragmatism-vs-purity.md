---
source_name: "External Linked Documentation"
source_url: "https://eli.thegreenplace.net/2018/on-the-uses-and-misuses-of-panics-in-go/"
source_path: "sources/raw/external/eli-thegreenplace-net-2018-on-the-uses-and-misuses-of-panics-in-go-094725cf76.html"
license_ref: ""
---

## Conclusion - pragmatism vs. purity

It's not my intention to attack the Go standard library developers here. As I've mentioned, I fully see why panics are attractive in some cases where call stacks are deep and sequences of error-signaling operations are common. I really hope Go will introduce some syntax that will make propagating an error easier, which would render this discussion moot.

Sometimes, it's better to be pragmatic than a zealot. If a certain language feature is really helpful in solving a problem, even outside of its classical domain of use, it may be better to use it than to ardently sticking to principles and ending up with convoluted code. Kind-of like my old defense of using goto for error handling in C <https://eli.thegreenplace.net/2009/04/27/using-goto-for-error-handling-in-c>. The Go guidelines are clear and the restrictions on recover are craftily placed - even when used for control flow in parsers, it's much harder to misuse than classical exceptions.

Interestingly, when this problem first drew my attention I was looking into the source of the json/encode.go package. It turns out that it was recently fixed to use classical error handling <https://go-review.googlesource.com/c/go/+/98440>! Yes, some code turned more verbose, from:

```go
if destring {
  switch qv := d.valueQuoted().(type) {
    case nil:
      d.literalStore(nullLiteral, subv, false)
    case string:
      d.literalStore([]byte(qv), subv, true)
    // ... other code

```

To:

```go
if destring {
  q, err := d.valueQuoted()
  if err != nil {
    return err
  }
  switch qv := q.(type) {
  case nil:
    if err := d.literalStore(nullLiteral, subv, false); err != nil {
      return err
    }
  case string:
    if err := d.literalStore([]byte(qv), subv, true); err != nil {
      return err
    }

```

But overall it's not _that_ bad and certainly wouldn't look unfamiliar to a Go coder. And it gives me hope :-)
     [1]C++'s set of exception safety guarantees <https://en.wikipedia.org/wiki/Exception_safety> is a good example of some of the complexities involved.      [2]If you spend some time reading the mailing list discussion where the recover mechanism was proposed <https://groups.google.com/forum/#!topic/golang-nuts/HOXNBQu5c-Q%5B26-50%5D>, you'll find Russ Cox mentioning a similar issue with parsing a binary stream and how to propagate errors through the process.      [3]Even C++ has a similar pattern that you will find in some codebases where a standard return type is used. Macros commonly named ASSIGN_OR_RETURN are popular in C++ code released by Google and show up in other places like LLVM.

 For comments, please send me __ an email.
