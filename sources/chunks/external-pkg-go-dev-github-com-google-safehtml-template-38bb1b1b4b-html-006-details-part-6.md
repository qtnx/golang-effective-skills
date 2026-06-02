---
source_name: "External Linked Documentation"
source_url: "https://pkg.go.dev/github.com/google/safehtml/template"
source_path: "sources/raw/external/pkg-go-dev-github-com-google-safehtml-template-38bb1b1b4b.html"
license_ref: ""
---

```go
func TrustedSourceFromFlag(value flag.Value) TrustedSource
```

TrustedSourceFromFlag returns a TrustedSource containing the string representation of the retrieved value of the flag.

In a server setting, flags are part of the application's deployment configuration and are hence considered application-controlled.

```go
func TrustedSourceJoin(elem ...TrustedSource) TrustedSource
```

TrustedSourceJoin is a wrapper around path/filepath.Join that returns a TrustedSource formed by joining the given path elements into a single path, adding an OS-specific path separator if necessary.

```go
func (t TrustedSource) String() string
```

String returns the string form of the TrustedSource.

```go
type TrustedTemplate struct {
	// contains filtered or unexported fields
}
```

A TrustedTemplate is an immutable string-like type containing a safehtml/template template body. It can be safely loaded as template text without the risk of untrusted template execution.

In order to ensure that an attacker cannot influence the TrustedTemplate value, a TrustedTemplate can be instantiated only from untyped string constants, and never from arbitrary string values potentially representing untrusted user input.

```go
func MakeTrustedTemplate(tmpl stringConstant) TrustedTemplate
```

MakeTrustedTemplate constructs a TrustedTemplate with its underlying tmpl set to the given tmpl, which must be an untyped string constant.

No runtime validation or sanitization is performed on tmpl; being under application control, it is simply assumed to comply with the TrustedTemplate type contract.

```go
func (t TrustedTemplate) String() string
```

String returns the string form of the TrustedTemplate.
