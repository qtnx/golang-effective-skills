---
source_name: "Google Go Style Guide"
source_url: "https://google.github.io/styleguide/go/"
source_path: "sources/raw/google-go-styleguide/decisions.md"
license_ref: "sources/licenses/google-styleguide-LICENSE.txt"
---

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
