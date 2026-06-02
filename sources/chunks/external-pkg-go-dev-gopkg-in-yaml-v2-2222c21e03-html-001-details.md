---
source_name: "External Linked Documentation"
source_url: "https://pkg.go.dev/gopkg.in/yaml.v2"
source_path: "sources/raw/external/pkg-go-dev-gopkg-in-yaml-v2-2222c21e03.html"
license_ref: ""
---

yaml package - gopkg.in/yaml.v2 - Go Packages
        The highest tagged major version is v3.
## Details

-     Valid go.mod <https://github.com/go-yaml/yaml/tree/v2.4.0/go.mod> file
 The Go module system was introduced in Go 1.11 and is the official dependency management solution for Go.

-     Redistributable license
 Redistributable licenses place minimal restrictions on how software can be used, modified, and redistributed.

-     Tagged version
Modules with tagged versions give importers more predictable builds.

-     Stable version
When a project reaches major version v1 it is considered stable.

-  Learn more about best practices

## Repository
   github.com/go-yaml/yaml  <https://github.com/go-yaml/yaml>

##   README ¶

### YAML support for the Go language

#### Introduction

The yaml package enables Go programs to comfortably encode and decode YAML values. It was developed within Canonical <https://www.canonical.com> as part of the juju <https://juju.ubuntu.com> project, and is based on a pure Go port of the well-known libyaml <http://pyyaml.org/wiki/LibYAML> C library to parse and generate YAML data quickly and reliably.

#### Compatibility

The yaml package supports most of YAML 1.1 and 1.2, including support for anchors, tags, map merging, etc. Multi-document unmarshalling is not yet implemented, and base-60 floats from YAML 1.1 are purposefully not supported since they're a poor design and are gone in YAML 1.2.

#### Installation and usage

The import path for the package is _gopkg.in/yaml.v2_.

To install it, run:

```go
go get gopkg.in/yaml.v2

```

#### API documentation

If opened in a browser, the import path itself leads to the API documentation:

- https://gopkg.in/yaml.v2 <https://gopkg.in/yaml.v2>

#### API stability

The package API for yaml v2 will remain stable as described in gopkg.in <https://gopkg.in>.

#### License

The yaml package is licensed under the Apache License 2.0. Please see the LICENSE file for details.

#### Example

```go
package main

import (
        "fmt"
        "log"

        "gopkg.in/yaml.v2"
)

var data = `
a: Easy!
b:
  c: 2
  d: [3, 4]
`

// Note: struct fields must be public in order for unmarshal to
// correctly populate the data.
type T struct {
        A string
        B struct {
                RenamedC int   `yaml:"c"`
                D        []int `yaml:",flow"`
        }
}

func main() {
        t := T{}

        err := yaml.Unmarshal([]byte(data), &t)
        if err != nil {
                log.Fatalf("error: %v", err)
        }
        fmt.Printf("--- t:\n%v\n\n", t)

        d, err := yaml.Marshal(&t)
        if err != nil {
                log.Fatalf("error: %v", err)
        }
        fmt.Printf("--- t dump:\n%s\n\n", string(d))

        m := make(map[interface{}]interface{})

        err = yaml.Unmarshal([]byte(data), &m)
        if err != nil {
                log.Fatalf("error: %v", err)
        }
        fmt.Printf("--- m:\n%v\n\n", m)

        d, err = yaml.Marshal(&m)
        if err != nil {
                log.Fatalf("error: %v", err)
        }
        fmt.Printf("--- m dump:\n%s\n\n", string(d))
}

```

This example will generate the following output:

```go
--- t:
{Easy! {2 [3 4]}}

--- t dump:
a: Easy!
b:
  c: 2
  d: [3, 4]

--- m:
map[a:Easy! b:map[c:2 d:[3 4]]]

--- m dump:
a: Easy!
b:
  c: 2
  d:
  - 3
  - 4

```

 Expand ▾ Collapse ▴
