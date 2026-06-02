---
source_name: "External Linked Documentation"
source_url: "https://eli.thegreenplace.net/2018/on-the-uses-and-misuses-of-panics-in-go/"
source_path: "sources/raw/external/eli-thegreenplace-net-2018-on-the-uses-and-misuses-of-panics-in-go-094725cf76.html"
license_ref: ""
---

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
