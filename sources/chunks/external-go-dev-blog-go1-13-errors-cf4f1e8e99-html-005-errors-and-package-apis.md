---
source_name: "External Linked Documentation"
source_url: "https://go.dev/blog/go1.13-errors"
source_path: "sources/raw/external/go-dev-blog-go1-13-errors-cf4f1e8e99.html"
license_ref: ""
---

# The Go Blog

## Errors and package APIs

A package which returns errors (and most do) should describe what properties of those errors programmers may rely on. A well-designed package will also avoid returning errors with properties that should not be relied upon.

The simplest specification is to say that operations either succeed or fail, returning a nil or non-nil error value respectively. In many cases, no further information is needed.

If we wish a function to return an identifiable error condition, such as “item not found,” we might return an error wrapping a sentinel.

```go
var ErrNotFound = errors.New("not found")

// FetchItem returns the named item.
//
// If no item with the name exists, FetchItem returns an error
// wrapping ErrNotFound.
func FetchItem(name string) (*Item, error) {
    if itemNotFound(name) {
        return nil, fmt.Errorf("%q: %w", name, ErrNotFound)
    }
    // ...
}

```

There are other existing patterns for providing errors which can be semantically examined by the caller, such as directly returning a sentinel value, a specific type, or a value which can be examined with a predicate function.

In all cases, care should be taken not to expose internal details to the user. As we touched on in “Whether to Wrap” above, when you return an error from another package you should convert the error to a form that does not expose the underlying error, unless you are willing to commit to returning that specific error in the future.

```go
f, err := os.Open(filename)
if err != nil {
    // The *os.PathError returned by os.Open is an internal detail.
    // To avoid exposing it to the caller, repackage it as a new
    // error with the same text. We use the %v formatting verb, since
    // %w would permit the caller to unwrap the original *os.PathError.
    return fmt.Errorf("%v", err)
}

```

If a function is defined as returning an error wrapping some sentinel or type, do not return the underlying error directly.

```go
var ErrPermission = errors.New("permission denied")

// DoSomething returns an error wrapping ErrPermission if the user
// does not have permission to do something.
func DoSomething() error {
    if !userHasPermission() {
        // If we return ErrPermission directly, callers might come
        // to depend on the exact error value, writing code like this:
        //
        //     if err := pkg.DoSomething(); err == pkg.ErrPermission { … }
        //
        // This will cause problems if we want to add additional
        // context to the error in the future. To avoid this, we
        // return an error wrapping the sentinel so that users must
        // always unwrap it:
        //
        //     if err := pkg.DoSomething(); errors.Is(err, pkg.ErrPermission) { ... }
        return fmt.Errorf("%w", ErrPermission)
    }
    // ...
}

```

# The Go Blog

## Conclusion

Although the changes we’ve discussed amount to just three functions and a formatting verb, we hope they will go a long way toward improving how errors are handled in Go programs. We expect that wrapping to provide additional context will become commonplace, helping programs to make better decisions and helping programmers to find bugs more quickly.

As Russ Cox said in his GopherCon 2019 keynote, on the path to Go 2 we experiment, simplify and ship. Now that we’ve shipped these changes, we look forward to the experiments that will follow.

 **Next article: **Go Modules: v2 and Beyond
 **Previous article: **Publishing Go Modules
 **Blog Index**
