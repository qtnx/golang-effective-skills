---
source_name: "External Linked Documentation"
source_url: "https://pkg.go.dev/github.com/spf13/cobra"
source_path: "sources/raw/external/pkg-go-dev-github-com-spf13-cobra-c48fa3a8d3.html"
license_ref: ""
---

# Overview

## Commands

Command is the central point of the application. Each interaction that the application supports will be contained in a Command. A command can have children commands and optionally run an action.

In the example above, 'server' is the command.

More about cobra.Command <https://pkg.go.dev/github.com/spf13/cobra#Command>

# Overview

## Flags

A flag is a way to modify the behavior of a command. Cobra supports fully POSIX-compliant flags as well as the Go flag package <https://golang.org/pkg/flag/>. A Cobra command can define flags that persist through to children commands and flags that are only available to that command.

In the example above, 'port' is the flag.

Flag functionality is provided by the pflag library <https://github.com/spf13/pflag>, a fork of the flag standard library which maintains the same interface while adding POSIX compliance.

# Installing

Using Cobra is easy. First, use `go get` to install the latest version of the library.

```go
go get -u github.com/spf13/cobra@latest

```

Next, include Cobra in your application:

```go
import "github.com/spf13/cobra"

```

# Usage

`cobra-cli` is a command line program to generate cobra applications and command files. It will bootstrap your application scaffolding to rapidly develop a Cobra-based application. It is the easiest way to incorporate Cobra into your application.

It can be installed by running:

```go
go install github.com/spf13/cobra-cli@latest

```

For complete details on using the Cobra-CLI generator, please read The Cobra Generator README <https://github.com/spf13/cobra-cli/blob/main/README.md>

For complete details on using the Cobra library, please read The Cobra User Guide <https://github.com/spf13/cobra/blob/v1.10.2/site/content/user_guide.md>.

# License

Cobra is released under the Apache 2.0 license. See LICENSE.txt <https://github.com/spf13/cobra/blob/v1.10.2/LICENSE.txt>

 Expand ▾ Collapse ▴
