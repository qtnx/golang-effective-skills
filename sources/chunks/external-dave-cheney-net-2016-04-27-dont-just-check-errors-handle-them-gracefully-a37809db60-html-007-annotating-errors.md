---
source_name: "External Linked Documentation"
source_url: "https://dave.cheney.net/2016/04/27/dont-just-check-errors-handle-them-gracefully"
source_path: "sources/raw/external/dave-cheney-net-2016-04-27-dont-just-check-errors-handle-them-gracefully-a37809db60.html"
license_ref: ""
---

# Errors are just values

## Annotating errors

I’d like to suggest a method to add context to errors, and to do that I’m going to introduce a simple package. The code is online at `github.com/pkg/errors` <https://godoc.org/github.com/pkg/errors>. The errors package has two main functions:

```go
// Wrap annotates cause with a message.
func Wrap(cause error, message string) error
```

The first function is `Wrap`, which takes an error, and a message and produces a new error.

```go
// Cause unwraps an annotated error.
func Cause(err error) error
```

The second function is `Cause`, which takes an error that has possibly been wrapped, and unwraps it to recover the original error.

Using these two functions, we can now annotate any error, and recover the underlying error if we need to inspect it. Consider this example of a function that reads the content of a file into memory.

```go
func ReadFile(path string) ([]byte, error) {
        f, err := os.Open(path)
        if err != nil {
                return nil, **errors.Wrap(err, "open failed")**
        }
        defer f.Close()

        buf, err := ioutil.ReadAll(f)
        if err != nil {
                return nil, **errors.Wrap(err, "read failed")**
        }
        return buf, nil
}
```

We’ll use this function to write a function to read a config file, then call that from `main`.

```go
func ReadConfig() ([]byte, error) {
        home := os.Getenv("HOME")
        config, err := ReadFile(filepath.Join(home, ".settings.xml"))
        return config, **errors.Wrap(err, "could not read config")**
}

func main() {
        _, err := ReadConfig()
        if err != nil {
                **fmt.Println(err)**
                os.Exit(1)
        }
}
```

If the `ReadConfig` code path fails, because we used `errors.Wrap`, we get a nicely annotated error in the K&D style.

```go
could not read config: open failed: open /Users/dfc/.settings.xml: no such file or directory
```

Because `errors.Wrap` produces a stack of errors, we can inspect that stack for additional debugging information. This is the same example again, but this time we replace `fmt.Println` with `errors.Print`

```go
func main() {
        _, err := ReadConfig()
        if err != nil {
                **errors.Print(err)**
                os.Exit(1)
        }
}
```

We’ll get something like this:

```go
readfile.go:27: could not read config
readfile.go:14: open failed
open /Users/dfc/.settings.xml: no such file or directory
```

The first line comes from `ReadConfig`, the second comes from the `os.Open` part of `ReadFile`, and the remainder comes from the `os` package itself, which does not carry location information.

Now we’ve introduced the concept of wrapping errors to produce a stack, we need to talk about the reverse, unwrapping them. This is the domain of the `errors.Cause` function.

```go
// IsTemporary returns true if err is temporary.
func IsTemporary(err error) bool {
        te, ok := **errors.Cause(err)**.(temporary)
        return ok && te.Temporary()
}
```

In operation, whenever you need to check an error matches a specific value or type, you should first recover the original error using the `errors.Cause` function.

# Only handle errors once

Lastly, I want to mention that you should only handle errors once. Handling an error means inspecting the error value, and making a decision.

```go
func Write(w io.Writer, buf []byte) {
        w.Write(buf)
}
```

If you make less than one decision, you’re ignoring the error. As we see here, the error from `w.Write` is being discarded.

But making more than one decision in response to a single error is also problematic.

```go
func Write(w io.Writer, buf []byte) error {
        _, err := w.Write(buf)
        if err != nil {
                // annotated error goes to log file
                **log.Println("unable to write:", err)**

                // unannotated error returned to caller
                **return err**
        }
        return nil
}
```

In this example if an error occurs during `Write`, a line will be written to a log file, noting the file and line that the error occurred, and the error is also returned to the caller, who possibly will log it, and return it, all the way back up to the top of the program.

So you get a stack of duplicate lines in your log file, but at the top of the program you get the original error without any context. Java anyone?

```go
func Write(w io.Write, buf []byte) error {
        _, err := w.Write(buf)
        return **errors.Wrap(err, "write failed")**
}
```

Using the `errors` package gives you the ability to add context to error values, in a way that is inspectable by both a human and a machine.

# Conclusion

In conclusion, errors are part of your package’s public API, treat them with as much care as you would any other part of your public API.

For maximum flexibility I recommend that you try to treat all errors as opaque. In the situations where you cannot do that, assert errors for behaviour, not type or value.

Minimise the number of sentinel error values in your program and convert errors to opaque errors by wrapping them with `errors.Wrap` as soon as they occur.

Finally, use `errors.Cause` to recover the underlying error if you need to inspect it.

### Related posts:

- Constant errors <https://dave.cheney.net/2016/04/07/constant-errors>
- Stack traces and the errors package <https://dave.cheney.net/2016/06/12/stack-traces-and-the-errors-package>
- Inspecting errors <https://dave.cheney.net/2014/12/24/inspecting-errors>
- Errors and Exceptions, redux <https://dave.cheney.net/2015/01/26/errors-and-exceptions-redux>

### Elsewhere

- LinkedIn <https://www.linkedin.com/in/davecheney>
- Serverfault <http://serverfault.com/users/301/dave-cheney>
- Stackoverflow <http://stackoverflow.com/users/6449/dave-cheney>

### Categories

- Economy <https://dave.cheney.net/category/economy>
- Go <https://dave.cheney.net/category/golang>
- Hardware Hacking <https://dave.cheney.net/category/hardware-hacking>
- History <https://dave.cheney.net/category/history>
- Internets of interest <https://dave.cheney.net/category/internets-of-interest>
- Photography <https://dave.cheney.net/category/photography>
- Programming <https://dave.cheney.net/category/programming-2>
- Retrochallenge <https://dave.cheney.net/category/retrochallenge>
- Small ideas <https://dave.cheney.net/category/small-ideas>
- Uncategorized <https://dave.cheney.net/category/uncategorized>
- Useless Trivia <https://dave.cheney.net/category/useless-trivia>

### Archives

- December 2025 <https://dave.cheney.net/2025/12>
- November 2025 <https://dave.cheney.net/2025/11>
- February 2024 <https://dave.cheney.net/2024/02>
- January 2021 <https://dave.cheney.net/2021/01>
- December 2020 <https://dave.cheney.net/2020/12>
- June 2020 <https://dave.cheney.net/2020/06>
- May 2020 <https://dave.cheney.net/2020/05>
- April 2020 <https://dave.cheney.net/2020/04>
- March 2020 <https://dave.cheney.net/2020/03>
- February 2020 <https://dave.cheney.net/2020/02>
- December 2019 <https://dave.cheney.net/2019/12>
- November 2019 <https://dave.cheney.net/2019/11>
- October 2019 <https://dave.cheney.net/2019/10>
- September 2019 <https://dave.cheney.net/2019/09>
- August 2019 <https://dave.cheney.net/2019/08>
- July 2019 <https://dave.cheney.net/2019/07>
- June 2019 <https://dave.cheney.net/2019/06>
- May 2019 <https://dave.cheney.net/2019/05>
- April 2019 <https://dave.cheney.net/2019/04>
- February 2019 <https://dave.cheney.net/2019/02>
- January 2019 <https://dave.cheney.net/2019/01>
- December 2018 <https://dave.cheney.net/2018/12>
- November 2018 <https://dave.cheney.net/2018/11>
- October 2018 <https://dave.cheney.net/2018/10>
- September 2018 <https://dave.cheney.net/2018/09>
- August 2018 <https://dave.cheney.net/2018/08>
- July 2018 <https://dave.cheney.net/2018/07>
- May 2018 <https://dave.cheney.net/2018/05>
- January 2018 <https://dave.cheney.net/2018/01>
- December 2017 <https://dave.cheney.net/2017/12>
- November 2017 <https://dave.cheney.net/2017/11>
- September 2017 <https://dave.cheney.net/2017/09>
- August 2017 <https://dave.cheney.net/2017/08>
- July 2017 <https://dave.cheney.net/2017/07>
- June 2017 <https://dave.cheney.net/2017/06>
- April 2017 <https://dave.cheney.net/2017/04>
- March 2017 <https://dave.cheney.net/2017/03>
- February 2017 <https://dave.cheney.net/2017/02>
- January 2017 <https://dave.cheney.net/2017/01>
- December 2016 <https://dave.cheney.net/2016/12>
- November 2016 <https://dave.cheney.net/2016/11>
- October 2016 <https://dave.cheney.net/2016/10>
- September 2016 <https://dave.cheney.net/2016/09>
- August 2016 <https://dave.cheney.net/2016/08>
- June 2016 <https://dave.cheney.net/2016/06>
- May 2016 <https://dave.cheney.net/2016/05>
- April 2016 <https://dave.cheney.net/2016/04>
- March 2016 <https://dave.cheney.net/2016/03>
- February 2016 <https://dave.cheney.net/2016/02>
- January 2016 <https://dave.cheney.net/2016/01>
- December 2015 <https://dave.cheney.net/2015/12>
- November 2015 <https://dave.cheney.net/2015/11>
- October 2015 <https://dave.cheney.net/2015/10>
- September 2015 <https://dave.cheney.net/2015/09>
- August 2015 <https://dave.cheney.net/2015/08>
- July 2015 <https://dave.cheney.net/2015/07>
- June 2015 <https://dave.cheney.net/2015/06>
- May 2015 <https://dave.cheney.net/2015/05>
- March 2015 <https://dave.cheney.net/2015/03>
- February 2015 <https://dave.cheney.net/2015/02>
- January 2015 <https://dave.cheney.net/2015/01>
- December 2014 <https://dave.cheney.net/2014/12>
- November 2014 <https://dave.cheney.net/2014/11>
- October 2014 <https://dave.cheney.net/2014/10>
- September 2014 <https://dave.cheney.net/2014/09>
- August 2014 <https://dave.cheney.net/2014/08>
- July 2014 <https://dave.cheney.net/2014/07>
- June 2014 <https://dave.cheney.net/2014/06>
- May 2014 <https://dave.cheney.net/2014/05>
- April 2014 <https://dave.cheney.net/2014/04>
- March 2014 <https://dave.cheney.net/2014/03>
- February 2014 <https://dave.cheney.net/2014/02>
- January 2014 <https://dave.cheney.net/2014/01>
- December 2013 <https://dave.cheney.net/2013/12>
- November 2013 <https://dave.cheney.net/2013/11>
- October 2013 <https://dave.cheney.net/2013/10>
- September 2013 <https://dave.cheney.net/2013/09>
- August 2013 <https://dave.cheney.net/2013/08>
- July 2013 <https://dave.cheney.net/2013/07>
- June 2013 <https://dave.cheney.net/2013/06>
- May 2013 <https://dave.cheney.net/2013/05>
- April 2013 <https://dave.cheney.net/2013/04>
- January 2013 <https://dave.cheney.net/2013/01>
- December 2012 <https://dave.cheney.net/2012/12>
- November 2012 <https://dave.cheney.net/2012/11>
- October 2012 <https://dave.cheney.net/2012/10>
- September 2012 <https://dave.cheney.net/2012/09>
- August 2012 <https://dave.cheney.net/2012/08>
- February 2012 <https://dave.cheney.net/2012/02>
- January 2012 <https://dave.cheney.net/2012/01>
- November 2011 <https://dave.cheney.net/2011/11>
- October 2011 <https://dave.cheney.net/2011/10>
- August 2011 <https://dave.cheney.net/2011/08>
- July 2011 <https://dave.cheney.net/2011/07>
- June 2011 <https://dave.cheney.net/2011/06>
- May 2011 <https://dave.cheney.net/2011/05>
- April 2011 <https://dave.cheney.net/2011/04>
- March 2011 <https://dave.cheney.net/2011/03>
- February 2011 <https://dave.cheney.net/2011/02>
- November 2010 <https://dave.cheney.net/2010/11>
- October 2010 <https://dave.cheney.net/2010/10>

### License
  <https://creativecommons.org/licenses/by-nc-sa/4.0/>
This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License <https://creativecommons.org/licenses/by-nc-sa/4.0/>.
