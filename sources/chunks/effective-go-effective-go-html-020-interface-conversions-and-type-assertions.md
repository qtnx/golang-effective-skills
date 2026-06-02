---
source_name: "Effective Go"
source_url: "https://go.dev/doc/effective_go"
source_path: "sources/raw/effective-go/effective_go.html"
license_ref: "sources/licenses/go-LICENSE.txt"
---

## Interfaces and other types

### Interface conversions and type assertions

 Type switches are a form of conversion: they take an interface and, for each case in the switch, in a sense convert it to the type of that case. Here's a simplified version of how the code under `fmt.Printf` turns a value into a string using a type switch. If it's already a string, we want the actual string value held by the interface, while if it has a `String` method we want the result of calling the method.

```go

type Stringer interface {
    String() string
}

var value interface{} // Value provided by caller.
switch str := value.(type) {
case string:
    return str
case Stringer:
    return str.String()
}

```

 The first case finds a concrete value; the second converts the interface into another interface. It's perfectly fine to mix types this way.

 What if there's only one type we care about? If we know the value holds a `string` and we just want to extract it? A one-case type switch would do, but so would a _type assertion_. A type assertion takes an interface value and extracts from it a value of the specified explicit type. The syntax borrows from the clause opening a type switch, but with an explicit type rather than the `type` keyword:

```go

value.(typeName)

```

 and the result is a new value with the static type `typeName`. That type must either be the concrete type held by the interface, or a second interface type that the value can be converted to. To extract the string we know is in the value, we could write:

```go

str := value.(string)

```

 But if it turns out that the value does not contain a string, the program will crash with a run-time error. To guard against that, use the "comma, ok" idiom to test, safely, whether the value is a string:

```go

str, ok := value.(string)
if ok {
    fmt.Printf("string value is: %q\n", str)
} else {
    fmt.Printf("value is not a string\n")
}

```

 If the type assertion fails, `str` will still exist and be of type string, but it will have the zero value, an empty string.

 As an illustration of the capability, here's an `if`-`else` statement that's equivalent to the type switch that opened this section.

```go

if str, ok := value.(string); ok {
    return str
} else if str, ok := value.(Stringer); ok {
    return str.String()
}

```
