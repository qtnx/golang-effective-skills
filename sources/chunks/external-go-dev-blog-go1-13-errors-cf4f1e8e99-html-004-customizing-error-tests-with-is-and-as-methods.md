---
source_name: "External Linked Documentation"
source_url: "https://go.dev/blog/go1.13-errors"
source_path: "sources/raw/external/go-dev-blog-go1-13-errors-cf4f1e8e99.html"
license_ref: ""
---

# The Go Blog

## Customizing error tests with Is and As methods

The `errors.Is` function examines each error in a chain for a match with a target value. By default, an error matches the target if the two are equal. In addition, an error in the chain may declare that it matches a target by implementing an `Is` _method_.

As an example, consider this error inspired by the Upspin error package <https://commandcenter.blogspot.com/2017/12/error-handling-in-upspin.html> which compares an error against a template, considering only fields which are non-zero in the template:

```go
type Error struct {
    Path string
    User string
}

func (e *Error) Is(target error) bool {
    t, ok := target.(*Error)
    if !ok {
        return false
    }
    return (e.Path == t.Path || t.Path == "") &&
           (e.User == t.User || t.User == "")
}

if errors.Is(err, &Error{User: "someuser"}) {
    // err's User field is "someuser".
}

```

The `errors.As` function similarly consults an `As` method when present.
