---
source_name: "External Linked Documentation"
source_url: "https://pkg.go.dev/github.com/spf13/cobra"
source_path: "sources/raw/external/pkg-go-dev-github-com-spf13-cobra-c48fa3a8d3.html"
license_ref: ""
---

# Overview

cobra package - github.com/spf13/cobra - Go Packages
## Details

-     Valid go.mod <https://github.com/spf13/cobra/tree/v1.10.2/go.mod> file
 The Go module system was introduced in Go 1.11 and is the official dependency management solution for Go.

-     Redistributable license
 Redistributable licenses place minimal restrictions on how software can be used, modified, and redistributed.

-     Tagged version
Modules with tagged versions give importers more predictable builds.

-     Stable version
When a project reaches major version v1 it is considered stable.

-  Learn more about best practices

# Overview

## Repository
   github.com/spf13/cobra  <https://github.com/spf13/cobra>

# Overview

##   README ¶
      <https://cobra.dev>

Cobra is a library for creating powerful modern CLI applications.

Visit Cobra.dev for extensive documentation <https://cobra.dev>

Cobra is used in many Go projects such as Kubernetes <https://kubernetes.io/>, Hugo <https://gohugo.io>, and GitHub CLI <https://github.com/cli/cli> to name a few. This list <https://github.com/spf13/cobra/blob/v1.10.2/site/content/projects_using_cobra.md> contains a more extensive list of projects using Cobra.

 <https://github.com/spf13/cobra/actions?query=workflow%3ATest>  <https://pkg.go.dev/github.com/spf13/cobra>  <https://goreportcard.com/report/github.com/spf13/cobra>  <https://gophers.slack.com/archives/CD3LP1199>
   Supported by:

    <https://www.warp.dev/cobra>
### Warp, the AI terminal for devs <https://www.warp.dev/cobra>

Try Cobra in Warp today <https://www.warp.dev/cobra>

# Overview

Cobra is a library providing a simple interface to create powerful modern CLI interfaces similar to git & go tools.

Cobra provides:

- Easy subcommand-based CLIs: `app server`, `app fetch`, etc.
- Fully POSIX-compliant flags (including short & long versions)
- Nested subcommands
- Global, local and cascading flags
- Intelligent suggestions (`app srver`... did you mean `app server`?)
- Automatic help generation for commands and flags
- Grouping help for subcommands
- Automatic help flag recognition of `-h`, `--help`, etc.
- Automatically generated shell autocomplete for your application (bash, zsh, fish, powershell)
- Automatically generated man pages for your application
- Command aliases so you can change things without breaking them
- The flexibility to define your own help, usage, etc.
- Optional seamless integration with viper <https://github.com/spf13/viper> for 12-factor apps

# Concepts

Cobra is built on a structure of commands, arguments & flags.

**Commands** represent actions, **Args** are things and **Flags** are modifiers for those actions.

The best applications read like sentences when used, and as a result, users intuitively know how to interact with them.

The pattern to follow is `APPNAME VERB NOUN --ADJECTIVE` or `APPNAME COMMAND ARG --FLAG`.

A few good real world examples may better illustrate this point.

In the following example, 'server' is a command, and 'port' is a flag:

```go
hugo server --port=1313

```

In this command we are telling Git to clone the url bare.

```go
git clone URL --bare

```
