---
source_name: "External Linked Documentation"
source_url: "https://go.dev/doc/faq"
source_path: "sources/raw/external/go-dev-doc-faq-c6a034d6a5.html"
license_ref: ""
---

## Design

### Will you accept my language change?

People often suggest improvements to the language—the mailing list <https://groups.google.com/group/golang-nuts> contains a rich history of such discussions—but very few of these changes have been accepted.

Although Go is an open source project, the language and libraries are protected by a compatibility promise that prevents changes that break existing programs, at least at the source code level (programs may need to be recompiled occasionally to stay current). If your proposal violates the Go 1 specification we cannot even entertain the idea, regardless of its merit. A future major release of Go may be incompatible with Go 1, but discussions on that topic have only just begun and one thing is certain: there will be very few such incompatibilities introduced in the process. Moreover, the compatibility promise encourages us to provide an automatic path forward for old programs to adapt should that situation arise.

Even if your proposal is compatible with the Go 1 spec, it might not be in the spirit of Go’s design goals. The article _Go at Google: Language Design in the Service of Software Engineering_ explains Go’s origins and the motivation behind its design.
