---
source_name: "Google Go Style Guide"
source_url: "https://google.github.io/styleguide/go/"
source_path: "sources/raw/google-go-styleguide/best-practices.md"
license_ref: "sources/licenses/google-styleguide-LICENSE.txt"
---

# Go Style Best Practices
[Best practices](best-practices)
**Note:** This is part of a series of documents that outline [Go Style](index)
at Google. This document is **neither [normative](index#normative) nor
[canonical](index#canonical)**, and is an auxiliary document to the
[core style guide](guide). See [the overview](index#about) for more information.
<a id="about"></a>
## About

This file documents **guidance about how to best apply the Go Style Guide**.
This guidance is intended for common situations that arise frequently, but may
not apply in every circumstance. Where possible, multiple alternative approaches
are discussed along with the considerations that go into the decision about when
and when not to apply them.

See [the overview](index#about) for the full set of Style Guide documents.

<a id="naming"></a>

## Naming
<a id="function-names"></a>
### Function and method names

<a id="function-name-repetition"></a>

#### Avoid repetition

When choosing the name for a function or method, consider the context in which
the name will be read. Consider the following recommendations to avoid excess
[repetition](decisions#repetition) at the call site:

*   The following can generally be omitted from function and method names:

    *   The types of the inputs and outputs (when there is no collision)
    *   The type of a method's receiver
    *   Whether an input or output is a pointer

*   For functions, do not
    [repeat the name of the package](decisions#repetitive-with-package).

    ```go
    // Bad:
    package yamlconfig

    func ParseYAMLConfig(input string) (*Config, error)
    ```

    ```go
    // Good:
    package yamlconfig

    func Parse(input string) (*Config, error)
    ```

*   For methods, do not repeat the name of the method receiver.

    ```go
    // Bad:
    func (c *Config) WriteConfigTo(w io.Writer) (int64, error)
    ```

    ```go
    // Good:
    func (c *Config) WriteTo(w io.Writer) (int64, error)
    ```

*   Do not repeat the names of variables passed as parameters.

    ```go
    // Bad:
    func OverrideFirstWithSecond(dest, source *Config) error
    ```

    ```go
    // Good:
    func Override(dest, source *Config) error
    ```

*   Do not repeat the names and types of the return values.

    ```go
    // Bad:
    func TransformToJSON(input *Config) *jsonconfig.Config
    ```

    ```go
    // Good:
    func Transform(input *Config) *jsonconfig.Config
    ```

When it is necessary to disambiguate functions of a similar name, it is
acceptable to include extra information.

```go
// Good:
func (c *Config) WriteTextTo(w io.Writer) (int64, error)
func (c *Config) WriteBinaryTo(w io.Writer) (int64, error)
```

<a id="function-name-conventions"></a>

#### Naming conventions

There are some other common conventions when choosing names for functions and
methods:

*   Functions that return something are given noun-like names.

    ```go
    // Good:
    func (c *Config) JobName(key string) (value string, ok bool)
    ```

    A corollary of this is that function and method names should
    [avoid the prefix `Get`](decisions#getters).

    ```go
    // Bad:
    func (c *Config) GetJobName(key string) (value string, ok bool)
    ```

*   Functions that do something are given verb-like names.

    ```go
    // Good:
    func (c *Config) WriteDetail(w io.Writer) (int64, error)
    ```

*   Identical functions that differ only by the types involved include the name
    of the type at the end of the name.

    ```go
    // Good:
    func ParseInt(input string) (int, error)
    func ParseInt64(input string) (int64, error)
    func AppendInt(buf []byte, value int) []byte
    func AppendInt64(buf []byte, value int64) []byte
    ```

    If there is a clear "primary" version, the type can be omitted from the name
    for that version:

    ```go
    // Good:
    func (c *Config) Marshal() ([]byte, error)
    func (c *Config) MarshalText() (string, error)
    ```

<a id="naming-doubles"></a>
