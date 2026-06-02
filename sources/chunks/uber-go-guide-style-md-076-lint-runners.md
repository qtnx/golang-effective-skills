---
source_name: "Uber Go Style Guide"
source_url: "https://github.com/uber-go/guide/blob/master/style.md"
source_path: "sources/raw/uber-go-guide/style.md"
license_ref: "sources/licenses/uber-go-guide-LICENSE.txt"
---

### Lint Runners

We recommend [golangci-lint](https://github.com/golangci/golangci-lint) as the go-to lint runner for Go code, largely due
to its performance in larger codebases and ability to configure and use many
canonical linters at once. This repo has an example [.golangci.yml](https://github.com/uber-go/guide/blob/master/.golangci.yml) config file
with recommended linters and settings.

golangci-lint has [various linters](https://golangci-lint.run/usage/linters/) available for use. The above linters are
recommended as a base set, and we encourage teams to add any additional linters
that make sense for their projects.
