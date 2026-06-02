---
source_name: "External Linked Documentation"
source_url: "https://go.dev/doc/fuzz"
source_path: "sources/raw/external/go-dev-doc-fuzz-ee5f17aa89.html"
license_ref: ""
---

# Go Fuzzing

Go Fuzzing - The Go Programming Language
# Go Fuzzing
Go supports fuzzing in its standard toolchain beginning in Go 1.18. Native Go fuzz tests are supported by OSS-Fuzz <https://google.github.io/oss-fuzz/getting-started/new-project-guide/go-lang/#native-go-fuzzing-support>.
**Try out the tutorial for fuzzing with Go.**
## Overview

Fuzzing is a type of automated testing which continuously manipulates inputs to a program to find bugs. Go fuzzing uses coverage guidance to intelligently walk through the code being fuzzed to find and report failures to the user. Since it can reach edge cases which humans often miss, fuzz testing can be particularly valuable for finding security exploits and vulnerabilities.

Below is an example of a fuzz test, highlighting its main components.

# Go Fuzzing

## Writing fuzz tests

### Requirements

Below are rules that fuzz tests must follow.

- A fuzz test must be a function named like `FuzzXxx`, which accepts only a `*testing.F`, and has no return value.
- Fuzz tests must be in *_test.go files to run.
- A fuzz target must be a method call to `(*testing.F).Fuzz <https://pkg.go.dev/testing#F.Fuzz>` which accepts a `*testing.T` as the first parameter, followed by the fuzzing arguments. There is no return value.
- There must be exactly one fuzz target per fuzz test.
- All seed corpus entries must have types which are identical to the fuzzing arguments, in the same order. This is true for calls to `(*testing.F).Add <https://pkg.go.dev/testing#F.Add>` and any corpus files in the testdata/fuzz directory of the fuzz test.
- The fuzzing arguments can only be the following types:
- `string`, `[]byte`
- `int`, `int8`, `int16`, `int32`/`rune`, `int64`
- `uint`, `uint8`/`byte`, `uint16`, `uint32`, `uint64`
- `float32`, `float64`
- `bool`

### Suggestions

Below are suggestions that will help you get the most out of fuzzing.

- Fuzz targets should be fast and deterministic so the fuzzing engine can work efficiently, and new failures and code coverage can be easily reproduced.
- Since the fuzz target is invoked in parallel across multiple workers and in nondeterministic order, the state of a fuzz target should not persist past the end of each call, and the behavior of a fuzz target should not depend on global state.
