---
source_name: "Google Go Style Guide"
source_url: "https://google.github.io/styleguide/go/"
source_path: "sources/raw/google-go-styleguide/decisions.html"
license_ref: "sources/licenses/google-styleguide-LICENSE.txt"
---

### Initialisms

Words in names that are initialisms or acronyms (e.g., `URL` and `NATO`) should have the same case. `URL` should appear as `URL` or `url` (as in `urlPony`, or `URLPony`), never as `Url`. As a general rule, identifiers (e.g., `ID` and `DB`) should also be capitalized similar to their usage in English prose.

- In names with multiple initialisms (e.g. `XMLAPI` because it contains `XML` and `API`), each letter within a given initialism should have the same case, but each initialism in the name does not need to have the same case.
- In names with an initialism containing a lowercase letter (e.g. `DDoS`, `iOS`, `gRPC`), the initialism should appear as it would in standard prose, unless you need to change the first letter for the sake of exportedness. In these cases, the entire initialism should be the same case (e.g. `ddos`, `IOS`, `GRPC`).
     English Usage Scope Correct Incorrect     XML API Exported `XMLAPI` `XmlApi`, `XMLApi`, `XmlAPI`, `XMLapi`   XML API Unexported `xmlAPI` `xmlapi`, `xmlApi`   iOS Exported `IOS` `Ios`, `IoS`   iOS Unexported `iOS` `ios`   gRPC Exported `GRPC` `Grpc`   gRPC Unexported `gRPC` `grpc`   DDoS Exported `DDoS` `DDOS`, `Ddos`   DDoS Unexported `ddos` `dDoS`, `dDOS`   ID Exported `ID` `Id`   ID Unexported `id` `iD`   DB Exported `DB` `Db`   DB Unexported `db` `dB`   Txn Exported `Txn` `TXN`
