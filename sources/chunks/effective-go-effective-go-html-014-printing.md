---
source_name: "Effective Go"
source_url: "https://go.dev/doc/effective_go"
source_path: "sources/raw/effective-go/effective_go.html"
license_ref: "sources/licenses/go-LICENSE.txt"
---

## Data

### Printing

 Formatted printing in Go uses a style similar to C's `printf` family but is richer and more general. The functions live in the `fmt` package and have capitalized names: `fmt.Printf`, `fmt.Fprintf`, `fmt.Sprintf` and so on. The string functions (`Sprintf` etc.) return a string rather than filling in a provided buffer.

 You don't need to provide a format string. For each of `Printf`, `Fprintf` and `Sprintf` there is another pair of functions, for instance `Print` and `Println`. These functions do not take a format string but instead generate a default format for each argument. The `Println` versions also insert a blank between arguments and append a newline to the output while the `Print` versions add blanks only if the operand on neither side is a string. In this example each line produces the same output.

```go

fmt.Printf("Hello %d\n", 23)
fmt.Fprint(os.Stdout, "Hello ", 23, "\n")
fmt.Println("Hello", 23)
fmt.Println(fmt.Sprint("Hello ", 23))

```

 The formatted print functions `fmt.Fprint` and friends take as a first argument any object that implements the `io.Writer` interface; the variables `os.Stdout` and `os.Stderr` are familiar instances.

 Here things start to diverge from C. First, the numeric formats such as `%d` do not take flags for signedness or size; instead, the printing routines use the type of the argument to decide these properties.

```go

var x uint64 = 1<<64 - 1
fmt.Printf("%d %x; %d %x\n", x, x, int64(x), int64(x))

```

 prints

```go

18446744073709551615 ffffffffffffffff; -1 -1

```

 If you just want the default conversion, such as decimal for integers, you can use the catchall format `%v` (for “value”); the result is exactly what `Print` and `Println` would produce. Moreover, that format can print _any_ value, even arrays, slices, structs, and maps. Here is a print statement for the time zone map defined in the previous section.

```go

fmt.Printf("%v\n", timeZone)  // or just fmt.Println(timeZone)

```

 which gives output:

```go

map[CST:-21600 EST:-18000 MST:-25200 PST:-28800 UTC:0]

```

 For maps, `Printf` and friends sort the output lexicographically by key.

 When printing a struct, the modified format `%+v` annotates the fields of the structure with their names, and for any value the alternate format `%#v` prints the value in full Go syntax.

```go

type T struct {
    a int
    b float64
    c string
}
t := &T{ 7, -2.35, "abc\tdef" }
fmt.Printf("%v\n", t)
fmt.Printf("%+v\n", t)
fmt.Printf("%#v\n", t)
fmt.Printf("%#v\n", timeZone)

```

 prints

```go

&{7 -2.35 abc   def}
&{a:7 b:-2.35 c:abc     def}
&main.T{a:7, b:-2.35, c:"abc\tdef"}
map[string]int{"CST":-21600, "EST":-18000, "MST":-25200, "PST":-28800, "UTC":0}

```

 (Note the ampersands.) That quoted string format is also available through `%q` when applied to a value of type `string` or `[]byte`. The alternate format `%#q` will use backquotes instead if possible. (The `%q` format also applies to integers and runes, producing a single-quoted rune constant.) Also, `%x` works on strings, byte arrays and byte slices as well as on integers, generating a long hexadecimal string, and with a space in the format (`% x`) it puts spaces between the bytes.

 Another handy format is `%T`, which prints the _type_ of a value.

```go

fmt.Printf("%T\n", timeZone)

```

 prints

```go

map[string]int

```

 If you want to control the default format for a custom type, all that's required is to define a method with the signature `String() string` on the type. For our simple type `T`, that might look like this.

```go

func (t *T) String() string {
    return fmt.Sprintf("%d/%g/%q", t.a, t.b, t.c)
}
fmt.Printf("%v\n", t)

```

 to print in the format

```go

7/-2.35/"abc\tdef"

```

 (If you need to print _values_ of type `T` as well as pointers to `T`, the receiver for `String` must be of value type; this example used a pointer because that's more efficient and idiomatic for struct types. See the section below on pointers vs. value receivers for more information.)

 Our `String` method is able to call `Sprintf` because the print routines are fully reentrant and can be wrapped this way. There is one important detail to understand about this approach, however: don't construct a `String` method by calling `Sprintf` in a way that will recur into your `String` method indefinitely. This can happen if the `Sprintf` call attempts to print the receiver directly as a string, which in turn will invoke the method again. It's a common and easy mistake to make, as this example shows.

```go

type MyString string

func (m MyString) String() string {
    return fmt.Sprintf("MyString=%s", m) // Error: will recur forever.
}

```

 It's also easy to fix: convert the argument to the basic string type, which does not have the method.

```go

type MyString string
func (m MyString) String() string {
    return fmt.Sprintf("MyString=%s", string(m)) // OK: note conversion.
}

```

 In the initialization section we'll see another technique that avoids this recursion.

 Another printing technique is to pass a print routine's arguments directly to another such routine. The signature of `Printf` uses the type `...interface{}` for its final argument to specify that an arbitrary number of parameters (of arbitrary type) can appear after the format.

```go

func Printf(format string, v ...interface{}) (n int, err error) {

```

 Within the function `Printf`, `v` acts like a variable of type `[]interface{}` but if it is passed to another variadic function, it acts like a regular list of arguments. Here is the implementation of the function `log.Println` we used above. It passes its arguments directly to `fmt.Sprintln` for the actual formatting.

```go

// Println prints to the standard logger in the manner of fmt.Println.
func Println(v ...interface{}) {
    std.Output(2, fmt.Sprintln(v...))  // Output takes parameters (int, string)
}

```

 We write `...` after `v` in the nested call to `Sprintln` to tell the compiler to treat `v` as a list of arguments; otherwise it would just pass `v` as a single slice argument.

 There's even more to printing than we've covered here. See the `godoc` documentation for package `fmt` for the details.

 By the way, a `...` parameter can be of a specific type, for instance `...int` for a min function that chooses the least of a list of integers:

```go

func Min(a ...int) int {
    min := int(^uint(0) >> 1)  // largest int
    for _, i := range a {
        if i < min {
            min = i
        }
    }
    return min
}

```
