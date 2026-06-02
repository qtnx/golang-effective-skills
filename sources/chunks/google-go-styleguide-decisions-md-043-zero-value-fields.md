---
source_name: "Google Go Style Guide"
source_url: "https://google.github.io/styleguide/go/"
source_path: "sources/raw/google-go-styleguide/decisions.md"
license_ref: "sources/licenses/google-styleguide-LICENSE.txt"
---

#### Zero-value fields

[Zero-value] fields may be omitted from struct literals when clarity is not lost
as a result.

Well-designed APIs often employ zero-value construction for enhanced
readability. For example, omitting the three zero-value fields from the
following struct draws attention to the only option that is being specified.

[Zero-value]: https://golang.org/ref/spec#The_zero_value

```go
// Bad:
import (
  "github.com/golang/leveldb"
  "github.com/golang/leveldb/db"
)

ldb := leveldb.Open("/my/table", &db.Options{
    BlockSize: 1<<16,
    ErrorIfDBExists: true,

    // These fields all have their zero values.
    BlockRestartInterval: 0,
    Comparer: nil,
    Compression: nil,
    FileSystem: nil,
    FilterPolicy: nil,
    MaxOpenFiles: 0,
    WriteBufferSize: 0,
    VerifyChecksums: false,
})
```

```go
// Good:
import (
  "github.com/golang/leveldb"
  "github.com/golang/leveldb/db"
)

ldb := leveldb.Open("/my/table", &db.Options{
    BlockSize: 1<<16,
    ErrorIfDBExists: true,
})
```

Structs within table-driven tests often benefit from [explicit field names],
especially when the test struct is not trivial. This allows the author to omit
the zero-valued fields entirely when the fields in question are not related to
the test case. For example, successful test cases should omit any error-related
or failure-related fields. In cases where the zero value is necessary to
understand the test case, such as testing for zero or `nil` inputs, the field
names should be specified.

[explicit field names]: #literal-field-names

**Concise**

```go
tests := []struct {
    input      string
    wantPieces []string
    wantErr    error
}{
    {
        input:      "1.2.3.4",
        wantPieces: []string{"1", "2", "3", "4"},
    },
    {
        input:   "hostname",
        wantErr: ErrBadHostname,
    },
}
```

**Explicit**

```go
tests := []struct {
    input    string
    wantIPv4 bool
    wantIPv6 bool
    wantErr  bool
}{
    {
        input:    "1.2.3.4",
        wantIPv4: true,
        wantIPv6: false,
    },
    {
        input:    "1:2::3:4",
        wantIPv4: false,
        wantIPv6: true,
    },
    {
        input:    "hostname",
        wantIPv4: false,
        wantIPv6: false,
        wantErr:  true,
    },
}
```

<a id="nil-slices"></a>
