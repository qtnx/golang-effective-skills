---
source_name: "External Linked Documentation"
source_url: "https://go.dev/doc/tutorial/generics"
source_path: "sources/raw/external/go-dev-doc-tutorial-generics-36804f0219.html"
license_ref: ""
---

# Tutorial: Getting started with generics

## Prerequisites

- **An installation of Go 1.18 or later.** For installation instructions, see Installing Go.
- **A tool to edit your code.** Any text editor you have will work fine.
- **A command terminal.** Go works well using any terminal on Linux and Mac, and on PowerShell or cmd in Windows.

# Tutorial: Getting started with generics

## Create a folder for your code

To begin, create a folder for the code you’ll write.

-
Open a command prompt and change to your home directory.

On Linux or Mac:

```go
$ cd

```

On Windows:

```go
C:\> cd %HOMEPATH%

```

The rest of the tutorial will show a $ as the prompt. The commands you use will work on Windows too.

-
From the command prompt, create a directory for your code called generics.

```go
$ mkdir generics
$ cd generics

```

-
Create a module to hold your code.

Run the `go mod init` command, giving it your new code’s module path.

```go
$ go mod init example/generics
go: creating new go.mod: module example/generics

```

**Note:** For production code, you’d specify a module path that’s more specific to your own needs. For more, be sure to see Managing dependencies.

Next, you’ll add some simple code to work with maps.
