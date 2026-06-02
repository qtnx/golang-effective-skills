---
source_name: "Uber Go Style Guide"
source_url: "https://github.com/uber-go/guide/blob/master/style.md"
source_path: "sources/raw/uber-go-guide/style.md"
license_ref: "sources/licenses/uber-go-guide-LICENSE.txt"
---

#### Use `time.Time` and `time.Duration` with external systems

Use `time.Duration` and `time.Time` in interactions with external systems when
possible. For example:

- Command-line flags: [`flag`](https://pkg.go.dev/flag) supports `time.Duration` via
  [`time.ParseDuration`](https://pkg.go.dev/time#ParseDuration)
- JSON: [`encoding/json`](https://pkg.go.dev/encoding/json) supports encoding `time.Time` as an [RFC 3339](https://tools.ietf.org/html/rfc3339)
  string via its [`UnmarshalJSON` method](https://pkg.go.dev/time#Time.UnmarshalJSON)
- SQL: [`database/sql`](https://pkg.go.dev/database/sql) supports converting `DATETIME` or `TIMESTAMP` columns
  into `time.Time` and back if the underlying driver supports it
- YAML: [`gopkg.in/yaml.v2`](https://pkg.go.dev/gopkg.in/yaml.v2) supports `time.Time` as an [RFC 3339](https://tools.ietf.org/html/rfc3339) string, and
  `time.Duration` via [`time.ParseDuration`](https://pkg.go.dev/time#ParseDuration).

When it is not possible to use `time.Duration` in these interactions, use
`int` or `float64` and include the unit in the name of the field.

For example, since `encoding/json` does not support `time.Duration`, the unit
is included in the name of the field.

<table>
<thead><tr><th>Bad</th><th>Good</th></tr></thead>
<tbody>
<tr><td>

```go
// {"interval": 2}
type Config struct {
  Interval int `json:"interval"`
}
```

</td><td>

```go
// {"intervalMillis": 2000}
type Config struct {
  IntervalMillis int `json:"intervalMillis"`
}
```

</td></tr>
</tbody></table>

When it is not possible to use `time.Time` in these interactions, unless an
alternative is agreed upon, use `string` and format timestamps as defined in
[RFC 3339](https://tools.ietf.org/html/rfc3339). This format is used by default by [`Time.UnmarshalText`](https://pkg.go.dev/time#Time.UnmarshalText) and is
available for use in `Time.Format` and `time.Parse` via [`time.RFC3339`](https://pkg.go.dev/time#RFC3339).

Although this tends to not be a problem in practice, keep in mind that the
`"time"` package does not support parsing timestamps with leap seconds
([8728](https://github.com/golang/go/issues/8728)), nor does it account for leap seconds in calculations ([15190](https://github.com/golang/go/issues/15190)). If
you compare two instants of time, the difference will not include the leap
seconds that may have occurred between those two instants.
