---
source_name: "Google Go Style Guide"
source_url: "https://google.github.io/styleguide/go/"
source_path: "sources/raw/google-go-styleguide/decisions.md"
license_ref: "sources/licenses/google-styleguide-LICENSE.txt"
---

#### Field names

Struct literals must specify **field names** for types defined outside the
current package.

*   Include field names for types from other packages.

    ```go
    // Good:
    // https://pkg.go.dev/encoding/csv#Reader
    r := csv.Reader{
      Comma: ',',
      Comment: '#',
      FieldsPerRecord: 4,
    }
    ```

    The position of fields in a struct and the full set of fields (both of which
    are necessary to get right when field names are omitted) are not usually
    considered to be part of a struct's public API; specifying the field name is
    needed to avoid unnecessary coupling.

    ```go
    // Bad:
    r := csv.Reader{',', '#', 4, false, false, false, false}
    ```

*   For package-local types, field names are optional.

    ```go
    // Good:
    okay := Type{42}
    also := internalType{4, 2}
    ```

    Field names should still be used if it makes the code clearer, and it is
    very common to do so. For example, a struct with a large number of fields
    should almost always be initialized with field names.

    <!-- TODO: Maybe a better example here that doesn't have many fields. -->

    ```go
    // Good:
    okay := StructWithLotsOfFields{
      field1: 1,
      field2: "two",
      field3: 3.14,
      field4: true,
    }
    ```

<a id="literal-matching-braces"></a>
