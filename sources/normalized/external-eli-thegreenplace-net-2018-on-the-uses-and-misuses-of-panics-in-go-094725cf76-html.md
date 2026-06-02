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

## The need to occasionally panic

Go is a _safe_ language with run-time checks for some serious programming errors. For example, when you try to access a slice out of bounds, the result is not undefined behavior. Rather, the Go runtime will _panic_. For example, this minimal program:

```go
package main

import (
  "fmt"
)

func main() {
  s := make([]string, 3)
  fmt.Println(s[5])
}

```

Will die with a runtime error followed by a stack trace:

```go
panic: runtime error: index out of range

goroutine 1 [running]:
main.main()
  /tmp/sandbox209906601/main.go:9 +0x40

```

Other common things that panic include accessing nil structure fields through pointers, closing an already-closed channel, etc. What are the alternatives to panicking here? We _could_ make slice access return a result, err pair, and we could also make slice element assignment a function that potentially returns an error, but this would result in cumbersome code. Imagine rewriting this snippet, where foo, bar and baz are all slices of strings:

```go
foo[i] = bar[i] + baz[i]

```

Into something like:

```go
br, err := bar[i]
if err != nil {
  return err
}
bz, err := baz[i]
if err != nil {
  return err
}
err := assign_slice_element(foo, i, br + bz)
if err != nil {
  return err
}

```

Looks like fun? Nope. Different languages handle this in different ways: Python and Java throw an exception if i points out of bounds in either of the slices/lists/arrays. C will emit code without bounds checking, with a good chance of accessing/trampling the wrong memory area, crashing the process or exposing it to security vulnerabilities. C++ takes the middle way, with some "performance oriented" modes that are unsafe and other modes (std::vector::at) that could throw an exception.

Since the verbosity of the rewritten snippet above is unacceptable, Go chose to have _panics_, which is an exception-like mechanism reserved for _truly exceptional conditions_ such as bugs in the code.

This isn't restricted to built-ins; user code can also panic if needed. Sometimes code encounters errors that can only mean something went horribly wrong - a bug, or some key invariant being violated. For example, a switch case that just can't happen in the current context. The panic function exists for just such cases; it's morally equivalent to Python's raise and C++'s throw. That said, subtle but powerful restrictions on how exceptions are caught make Go's exception handling unique.

## Restrictions on panic recovery in Go

When a panic is not caught/recovered anywhere in the calling stack, it will end up crashing the program with a stack dump, as shown above. This behavior is pretty useful for debugging, but not ideal in realistic scenarios. If we're writing a server that serves many clients, we don't want it to immediately crash because of an internal bug in some data parsing library it's using. It would be much better to catch such an error, log it, and keep serving other clients. Go's recover function can help with that. Here's a code sample from Effective Go <https://golang.org/doc/effective_go.html> demonstrating this:

```go
func server(workChan <-chan *Work) {
    for work := range workChan {
        go safelyDo(work)
    }
}

func safelyDo(work *Work) {
    defer func() {
        if err := recover(); err != nil {
            log.Println("work failed:", err)
        }
    }()
    do(work)
}

```

Even though Go's panic and recover resemble exceptions at first glance, they come with some important and deliberate limitations that makes them less prone to common problems with exception-heavy code. Here's another quote from the FAQ:
  Go also has a couple of built-in functions to signal and recover from truly exceptional conditions. The recovery mechanism is executed only as part of a function's state being torn down after an error, which is sufficient to handle catastrophe but requires no extra control structures and, when used well, can result in clean error-handling code.
Rob Pike's quote from the thread I linked to earlier is also relevant:
  Our proposal instead ties the handling to a function - a dying function - and thereby, deliberately, makes it harder to use. We want you think of panics as, well, panics! They are rare events that very few functions should ever need to think about. If you want to protect your code, one or two recover calls should do it for the whole program. If you're already worrying about discriminating different kinds of panics, you've lost sight of the ball.
The specific limitation is that recover can only be called in a defer code block, which cannot return control to an arbitrary point, but can only do clean-ups and tweak the function's return values. The Python file-opening exception handling shown above can't work in Go - we can't just catch OSError and try to open another file (or create the file we failed to open) without significant restructuring of the code.

This limitation is coupled with an important coding guideline - keep panics within package boundaries. It's a good practice for packages not to panic in their public interfaces. Rather, the public-facing functions and methods should recover from panics internally and translate them to error messages. This makes panics friendlier to use, though high-availability servers will still likely want to have outer recovers installed just in case.

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

## But isn't this... wrong?

I empathize with folks lured by the siren, its call is strong here! But I also can't shake off the feeling that this goes against the principles designed into the language. In the quote shown above Rob Pike says:
  In my experience few things are less exceptional than failing to open a file
But what is less exceptional than running into an unexpected character while parsing? Isn't it the most common kind of error a parser encounters? Pike goes on to say:
  We want you think of panics as, well, panics! They are rare events that very few functions should ever need to think about.
But is a parsing error rare? And very many functions in fmt/scan.go have to "think about" panics because that's what they use for signaling errors!
  If you're already worrying about discriminating different kinds of panics, you've lost sight of the ball.
But here is errorHandler from fmt/scan.go:

```go
func errorHandler(errp *error) {
  if e := recover(); e != nil {
    if se, ok := e.(scanError); ok { // catch local error
      *errp = se.err
    } else if eof, ok := e.(error); ok && eof == io.EOF { // out of input
      *errp = eof
    } else {
      panic(e)
    }
  }
}

```

Is this not "worrying about discriminating different kinds of panics"?

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
