---
source_name: "External Linked Documentation"
source_url: "https://research.swtch.com/interfaces"
source_path: "sources/raw/external/research-swtch-com-interfaces-8664b07867.html"
license_ref: ""
---

### Usage

Go's interfaces let you use duck typing <http://en.wikipedia.org/wiki/Duck_typing> like you would in a purely dynamic language like Python but still have the compiler catch obvious mistakes like passing an `int` where an object with a `Read` method was expected, or like calling the `Read` method with the wrong number of arguments. To use interfaces, first define the interface type (say, `ReadCloser`):

```go

type ReadCloser interface {
    Read(b []byte) (n int, err os.Error)
    Close()
}

```

and then define your new function as taking a `ReadCloser`. For example, this function calls `Read` repeatedly to get all the data that was requested and then calls `Close`:

```go

func ReadAndClose(r ReadCloser, buf []byte) (n int, err os.Error) {
    for len(buf) > 0 && err == nil {
        var nr int
        nr, err = r.Read(buf)
        n += nr
        buf = buf[nr:]
    }
    r.Close()
    return
}

```

The code that calls `ReadAndClose` can pass a value of any type as long as it has `Read` and `Close` methods with the right signatures. And, unlike in languages like Python, if you pass a value with the wrong type, you get an error at compile time, not run time.

Interfaces aren't restricted to static checking, though. You can check dynamically whether a particular interface value has an additional method. For example:

```go

type Stringer interface {
    String() string
}

func ToString(any interface{}) string {
    if v, ok := any.(Stringer); ok {
        return v.String()
    }
    switch v := any.(type) {
    case int:
        return strconv.Itoa(v)
    case float:
        return strconv.Ftoa(v, 'g', -1)
    }
    return "???"
}

```

The value `any` has static type `interface{}`, meaning no guarantee of any methods at all: it could contain any type. The “comma ok” assignment inside the `if` statement asks whether it is possible to convert `any` to an interface value of type `Stringer`, which has the method `String`. If so, the body of that statement calls the method to obtain a string to return. Otherwise, the `switch` picks off a few basic types before giving up. This is basically a stripped down version of what the fmt package <http://golang.org/pkg/fmt/> does. (The `if` could be replaced by adding `case Stringer:` at the top of the `switch`, but I used a separate statement to draw attention to the check.)

 As a simple example, let's consider a 64-bit integer type with a `String` method that prints the value in binary and a trivial `Get` method:

```go

type Binary uint64

func (i Binary) String() string {
    return strconv.Uitob64(i.Get(), 2)
}

func (i Binary) Get() uint64 {
    return uint64(i)
}

```

A value of type `Binary` can be passed to `ToString`, which will format it using the `String` method, even though the program never says that `Binary` intends to implement `Stringer`. There's no need: the runtime can see that `Binary` has a `String` method, so it implements `Stringer`, even if the author of `Binary` has never heard of `Stringer`.

These examples show that even though all the implicit conversions are checked at compile time, explicit interface-to-interface conversions can inquire about method sets at run time. “Effective Go <http://golang.org/doc/effective_go.html#interfaces>” has more details about and examples of how interface values can be used.
