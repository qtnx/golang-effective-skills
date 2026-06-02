---
source_name: "Uber Go Style Guide"
source_url: "https://github.com/uber-go/guide/blob/master/style.md"
source_path: "sources/raw/uber-go-guide/style.md"
license_ref: "sources/licenses/uber-go-guide-LICENSE.txt"
---

#### Use `var` for Zero Value Structs

When all the fields of a struct are omitted in a declaration, use the `var`
form to declare the struct.

<table>
<thead><tr><th>Bad</th><th>Good</th></tr></thead>
<tbody>
<tr><td>

```go
user := User{}
```

</td><td>

```go
var user User
```

</td></tr>
</tbody></table>

This differentiates zero valued structs from those with non-zero fields
similar to the distinction created for [map initialization](#initializing-maps), and matches how
we prefer to [declare empty slices](https://go.dev/wiki/CodeReviewComments#declaring-empty-slices).
