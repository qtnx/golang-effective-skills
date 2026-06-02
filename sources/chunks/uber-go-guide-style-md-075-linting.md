---
source_name: "Uber Go Style Guide"
source_url: "https://github.com/uber-go/guide/blob/master/style.md"
source_path: "sources/raw/uber-go-guide/style.md"
license_ref: "sources/licenses/uber-go-guide-LICENSE.txt"
---

## Linting

More importantly than any "blessed" set of linters, lint consistently across a
codebase.

We recommend using the following linters at a minimum, because we feel that they
help to catch the most common issues and also establish a high bar for code
quality without being unnecessarily prescriptive:

- [errcheck](https://github.com/kisielk/errcheck) to ensure that errors are handled
- [goimports](https://pkg.go.dev/golang.org/x/tools/cmd/goimports) to format code and manage imports
- [revive](https://github.com/mgechev/revive) to point out common style mistakes
- [govet](https://pkg.go.dev/cmd/vet) to analyze code for common mistakes
- [staticcheck](https://staticcheck.dev) to do various static analysis checks

  > **Note**: [revive](https://github.com/mgechev/revive) is the modern, faster successor to the now-deprecated [golint](https://github.com/golang/lint).
