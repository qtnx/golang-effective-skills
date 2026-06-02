---
source_name: "External Linked Documentation"
source_url: "https://go.dev/design/43651-type-parameters"
source_path: "sources/raw/external/go-dev-design-43651-type-parameters-8b418b79f1.html"
license_ref: ""
---

## Design

### Constraints

Let‘s make our example slightly more complicated. Let’s turn it into a function that converts a slice of any type into a `[]string` by calling a `String` method on each element.

```go
// This function is INVALID.
func Stringify[T any](s []T) (ret []string) {
	for _, v := range s {
		ret = append(ret, v.String()) // INVALID
	}
	return ret
}

```

This might seem OK at first glance, but in this example `v` has type `T`, and `T` can be any type. This means that `T` need not have a `String` method. So the call to `v.String()` is invalid.

Naturally, the same issue arises in other languages that support generic programming. In C++, for example, a generic function (in C++ terms, a function template) can call any method on a value of generic type. That is, in the C++ approach, calling `v.String()` is fine. If the function is called with a type argument that does not have a `String` method, the error is reported when compiling the call to `v.String` with that type argument. These errors can be lengthy, as there may be several layers of generic function calls before the error occurs, all of which must be reported to understand what went wrong.

The C++ approach would be a poor choice for Go. One reason is the style of the language. In Go we don't refer to names, such as, in this case, `String`, and hope that they exist. Go resolves all names to their declarations when they are seen.

Another reason is that Go is designed to support programming at scale. We must consider the case in which the generic function definition (`Stringify`, above) and the call to the generic function (not shown, but perhaps in some other package) are far apart. In general, all generic code expects the type arguments to meet certain requirements. We refer to these requirements as _constraints_ (other languages have similar ideas known as type bounds or trait bounds or concepts). In this case, the constraint is pretty obvious: the type has to have a `String() string` method. In other cases it may be much less obvious.

We don‘t want to derive the constraints from whatever `Stringify` happens to do (in this case, call the `String` method). If we did, a minor change to `Stringify` might change the constraints. That would mean that a minor change could cause code far away, that calls the function, to unexpectedly break. It’s fine for `Stringify` to deliberately change its constraints, and force callers to change. What we want to avoid is `Stringify` changing its constraints accidentally.

This means that the constraints must set limits on both the type arguments passed by the caller and the code in the generic function. The caller may only pass type arguments that satisfy the constraints. The generic function may only use those values in ways that are permitted by the constraints. This is an important rule that we believe should apply to any attempt to define generic programming in Go: generic code can only use operations that its type arguments are known to implement.
