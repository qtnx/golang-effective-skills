---
source_name: "External Linked Documentation"
source_url: "https://go.dev/doc/fuzz"
source_path: "sources/raw/external/go-dev-doc-fuzz-ee5f17aa89.html"
license_ref: ""
---

# Go Fuzzing

## Resources

- **Tutorial**:
- Try out the tutorial for fuzzing with Go for a deep dive into the new concepts.
- For a shorter, introductory tutorial of fuzzing with Go, please see the blog post.

- **Documentation**:
- The `testing` <https://pkg.go.dev//testing#hdr-Fuzzing> package docs describes the `testing.F` type which is used when writing fuzz tests.
- The `cmd/go` <https://pkg.go.dev/cmd/go> package docs describe the flags associated with fuzzing.

- **Technical details**:
- Design draft
- Proposal

# Go Fuzzing

## Glossary

 **corpus entry:** An input in the corpus which can be used while fuzzing. This can be a specially-formatted file, or a call to `(*testing.F).Add <https://pkg.go.dev/testing#F.Add>`.

 **coverage guidance:** A method of fuzzing which uses expansions in code coverage to determine which corpus entries are worth keeping for future use.

 **failing input:** A failing input is a corpus entry that will cause an error or panic when run against the fuzz target.

 **fuzz target:** The function of the fuzz test which is executed for corpus entries and generated values while fuzzing. It is provided to the fuzz test by passing the function to `(*testing.F).Fuzz <https://pkg.go.dev/testing#F.Fuzz>`.

 **fuzz test:** A function in a test file of the form `func FuzzXxx(*testing.F)` which can be used for fuzzing.

 **fuzzing:** A type of automated testing which continuously manipulates inputs to a program to find issues such as bugs or vulnerabilities to which the code may be susceptible.

 **fuzzing arguments:** The types which will be passed to the fuzz target, and mutated by the mutator.

 **fuzzing engine:** A tool that manages fuzzing, including maintaining the corpus, invoking the mutator, identifying new coverage, and reporting failures.

 **generated corpus:** A corpus which is maintained by the fuzzing engine over time while fuzzing to keep track of progress. It is stored in `$GOCACHE`/fuzz. These entries are only used while fuzzing.

 **mutator:** A tool used while fuzzing which randomly manipulates corpus entries before passing them to a fuzz target.

 **package:** A collection of source files in the same directory that are compiled together. See the Packages section in the Go Language Specification.

 **seed corpus:** A user-provided corpus for a fuzz test which can be used to guide the fuzzing engine. It is composed of the corpus entries provided by f.Add calls within the fuzz test, and the files in the testdata/fuzz/{FuzzTestName} directory within the package. These entries are run by default with `go test`, whether fuzzing or not.

 **test file:** A file of the format xxx_test.go that may contain tests, benchmarks, examples and fuzz tests.

 **vulnerability:** A security-sensitive weakness in code which can be exploited by an attacker.

# Go Fuzzing

## Feedback

If you experience any problems or have an idea for a feature, please file an issue.

For discussion and general feedback about the feature, you can also participate in the #fuzzing channel <https://gophers.slack.com/archives/CH5KV1AKE> in Gophers Slack.
