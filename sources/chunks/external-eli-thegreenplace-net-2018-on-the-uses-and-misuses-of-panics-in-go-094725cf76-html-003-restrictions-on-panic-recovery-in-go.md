---
source_name: "External Linked Documentation"
source_url: "https://eli.thegreenplace.net/2018/on-the-uses-and-misuses-of-panics-in-go/"
source_path: "sources/raw/external/eli-thegreenplace-net-2018-on-the-uses-and-misuses-of-panics-in-go-094725cf76.html"
license_ref: ""
---

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
