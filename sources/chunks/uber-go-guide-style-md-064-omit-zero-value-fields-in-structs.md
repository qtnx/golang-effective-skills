---
source_name: "Uber Go Style Guide"
source_url: "https://github.com/uber-go/guide/blob/master/style.md"
source_path: "sources/raw/uber-go-guide/style.md"
license_ref: "sources/licenses/uber-go-guide-LICENSE.txt"
---

#### Omit Zero Value Fields in Structs

When initializing structs with field names, omit fields that have zero values
unless they provide meaningful context. Otherwise, let Go set these to zero
values automatically.

<table>
<thead><tr><th>Bad</th><th>Good</th></tr></thead>
<tbody>
<tr><td>

```go
user := User{
  FirstName: "John",
  LastName: "Doe",
  MiddleName: "",
  Admin: false,
}
```

</td><td>

```go
user := User{
  FirstName: "John",
  LastName: "Doe",
}
```

</td></tr>
</tbody></table>

This helps reduce noise for readers by omitting values that are default in
that context. Only meaningful values are specified.

Include zero values where field names provide meaningful context. For example,
test cases in [Test Tables](#test-tables) can benefit from names of fields
even when they are zero-valued.

```go
tests := []struct{
  give string
  want int
}{
  {give: "0", want: 0},
  // ...
}
```
