---
source_name: "Google Go Style Guide"
source_url: "https://google.github.io/styleguide/go/"
source_path: "sources/raw/google-go-styleguide/best-practices.md"
license_ref: "sources/licenses/google-styleguide-LICENSE.txt"
---

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
