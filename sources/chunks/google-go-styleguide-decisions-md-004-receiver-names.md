---
source_name: "Google Go Style Guide"
source_url: "https://google.github.io/styleguide/go/"
source_path: "sources/raw/google-go-styleguide/decisions.md"
license_ref: "sources/licenses/google-styleguide-LICENSE.txt"
---

## Naming

### Receiver names

<a id="TOC-ReceiverNames"></a>

[Receiver] variable names must be:

*   Short (usually one or two letters in length)
*   Abbreviations for the type itself
*   Applied consistently to every receiver for that type
*   Not an underscore; omit the name if it is unused

Long Name                   | Better Name
--------------------------- | -------------------------
`func (tray Tray)`          | `func (t Tray)`
`func (info *ResearchInfo)` | `func (ri *ResearchInfo)`
`func (this *ReportWriter)` | `func (w *ReportWriter)`
`func (self *Scanner)`      | `func (s *Scanner)`

[Receiver]: https://golang.org/ref/spec#Method_declarations

<a id="constant-names"></a>

## Naming

### Constant names

Constant names must use [MixedCaps] like all other names in Go. ([Exported]
constants start with uppercase, while unexported constants start with
lowercase.) This applies even when it breaks conventions in other languages.
Constant names should not be a derivative of their values and should instead
explain what the value denotes.

```go
// Good:
const MaxPacketSize = 512

const (
    ExecuteBit = 1 << iota
    WriteBit
    ReadBit
)
```

[MixedCaps]: guide#mixed-caps
[Exported]: https://tour.golang.org/basics/3

Do not use non-MixedCaps constant names or constants with a `K` prefix.

```go
// Bad:
const MAX_PACKET_SIZE = 512
const kMaxBufferSize = 1024
const KMaxUsersPergroup = 500
```

Name constants based on their role, not their values. If a constant does not
have a role apart from its value, then it is unnecessary to define it as a
constant.

```go
// Bad:
const Twelve = 12

const (
    UserNameColumn = "username"
    GroupColumn    = "group"
)
```

<a id="initialisms"></a>
