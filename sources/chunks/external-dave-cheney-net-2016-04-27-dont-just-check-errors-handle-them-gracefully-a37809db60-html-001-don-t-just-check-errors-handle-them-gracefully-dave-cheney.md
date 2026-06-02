---
source_name: "External Linked Documentation"
source_url: "https://dave.cheney.net/2016/04/27/dont-just-check-errors-handle-them-gracefully"
source_path: "sources/raw/external/dave-cheney-net-2016-04-27-dont-just-check-errors-handle-them-gracefully-a37809db60.html"
license_ref: ""
---

# Errors are just values

Don’t just check errors, handle them gracefully | Dave Cheney
This post is an extract from my presentation at the recent GoCon spring conference <http://gocon.connpass.com/event/27521/> in Tokyo, Japan.
# Errors are just values
I’ve spent a lot of time thinking about the best way to handle errors in Go programs. I really wanted there to be a single way to do error handling, something that we could teach all Go programmers by rote, just as we might teach mathematics, or the alphabet.
However, I have concluded that there is no single way to handle errors. Instead, I believe Go’s error handling can be classified into the three core strategies.
# Sentinel errors
The first category of error handling is what I call _sentinel errors_.
```go
if err == ErrSomething { … }
```
The name descends from the practice in computer programming of using a specific value to signify that no further processing is possible. So to with Go, we use specific values to signify an error.
Examples include values like `io.EOF` or low level errors like the constants in the `syscall` package, like `syscall.ENOENT`.
There are even sentinel errors that signify that an error _did not_ occur, like `go/build.NoGoError`, and `path/filepath.SkipDir` from `path/filepath.Walk`.``
Using sentinel values is the least flexible error handling strategy, as the caller must compare the result to predeclared value using the equality operator. This presents a problem when you want to provide more context, as returning a different error would will break the equality check.
Even something as well meaning as using `fmt.Errorf` to add some context to the error will defeat the caller’s equality test. Instead the caller will be forced to look at the output of the `error`‘s `Error` method to see if it matches a specific string.
