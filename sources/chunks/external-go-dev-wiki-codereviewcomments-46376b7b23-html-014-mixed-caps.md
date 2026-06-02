---
source_name: "External Linked Documentation"
source_url: "https://go.dev/wiki/CodeReviewComments"
source_path: "sources/raw/external/go-dev-wiki-codereviewcomments-46376b7b23.html"
license_ref: ""
---

# Go Wiki: Go Code Review Comments

## Mixed Caps

See https://go.dev/doc/effective_go#mixed-caps <https://go.dev/doc/effective_go#mixed-caps>. This applies even when it breaks conventions in other languages. For example an unexported constant is `maxLength` not `MaxLength` or `MAX_LENGTH`.

Also see Initialisms.

# Go Wiki: Go Code Review Comments

## Named Result Parameters

Consider what it will look like in godoc. Named result parameters like:

```go
func (n *Node) Parent1() (node *Node) {}
func (n *Node) Parent2() (node *Node, err error) {}

```

will be repetitive in godoc; better to use:

```go
func (n *Node) Parent1() *Node {}
func (n *Node) Parent2() (*Node, error) {}

```

On the other hand, if a function returns two or three parameters of the same type, or if the meaning of a result isn’t clear from context, adding names may be useful in some contexts. Don’t name result parameters just to avoid declaring a var inside the function; that trades off a minor implementation brevity at the cost of unnecessary API verbosity.

```go
func (f *Foo) Location() (float64, float64, error)

```

is less clear than:

```go
// Location returns f's latitude and longitude.
// Negative values mean south and west, respectively.
func (f *Foo) Location() (lat, long float64, err error)

```

Naked returns are okay if the function is a handful of lines. Once it’s a medium sized function, be explicit with your return values. Corollary: it’s not worth it to name result parameters just because it enables you to use naked returns. Clarity of docs is always more important than saving a line or two in your function.

Finally, in some cases you need to name a result parameter in order to change it in a deferred closure. That is always OK.
