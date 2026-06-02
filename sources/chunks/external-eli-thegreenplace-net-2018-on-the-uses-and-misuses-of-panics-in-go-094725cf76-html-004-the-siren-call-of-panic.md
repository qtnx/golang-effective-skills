---
source_name: "External Linked Documentation"
source_url: "https://eli.thegreenplace.net/2018/on-the-uses-and-misuses-of-panics-in-go/"
source_path: "sources/raw/external/eli-thegreenplace-net-2018-on-the-uses-and-misuses-of-panics-in-go-094725cf76.html"
license_ref: ""
---

## The siren call of panic

Every language feature is destined to be misused; this is just a fact of programming life, and it's not different for Go's panic. This is not to say that all misuses are categorically wrong though, just that the feature ends up being used for goals it was not originally designed to fulfill.

Consider this real example from the scanInt method in fmt/scan.go of the Go (1.10) standard library:

```go
func (s *ss) scanInt(verb rune, bitSize int) int64 {
  if verb == 'c' {
    return s.scanRune(bitSize)
  }
  s.SkipSpace()
  s.notEOF()
  base, digits := s.getBase(verb)
  // ... other code
}

```

Each one of the methods SkipSpace, notEOF and getBase can fail, but where is the error handling? In fact, this package - like several others in the standard library - is using panics for some of its error handling internally. A panic from each of these will be recovered in the public API (like the Token method) and converted to an error. If we had to rewrite this code with explicit error handling, it would be more cumbersome, for sure [2]:

```go
if err := s.SkipSpace(); err != nil {
  return err
}
if err := s.notEOF(); err != nil {
  return err
}
base, digits, err := s.getBase(verb)
if err != nil {
  return err
}
// ... other code

```

Of course, panic is not the only way to solve this. As Rob Pike says, Errors are Values <https://blog.golang.org/errors-are-values> and thus they are programmable, and we could devise some clever way to make the code flow better without using an exception-like escape mechanism. Other languages have useful features that would make it much simpler; for example Rust has the ? operator [3] that propagates an error returned from a given expression automatically, so in a hypothetical syntax we could write:

```go
s.SkipSpace()?
s.notEOF()?
base, digits := s.getBase(verb)?

```

But we don't have this in Go (yet?), so the core Go team made the choice to use panics instead. They even condone this pattern in Effective Go <https://golang.org/doc/effective_go.html#recover>:
  With our recovery pattern in place, the do function (and anything it calls) can get out of any bad situation cleanly by calling panic. We can use that idea to simplify error handling in complex software.
And it's being used in several more places; a few I found with a quick search:

- fmt/scan.go
- json/encode.go
- text/template/parse/parser.go
