---
source_name: "External Linked Documentation"
source_url: "https://pkg.go.dev/github.com/google/subcommands"
source_path: "sources/raw/external/pkg-go-dev-github-com-google-subcommands-221a8be968.html"
license_ref: ""
---

##   Documentation ¶

Package subcommands implements a simple way for a single command to have many subcommands, each of which takes arguments and so forth.

-  func ImportantFlag(name string)
-  func Register(cmd Command, group string)
-  type Command
-
-  func Alias(alias string, cmd Command) Command
-  func CommandsCommand() Command
-  func FlagsCommand() Command
-  func HelpCommand() Command

-  type CommandGroup
-
-  func (g CommandGroup) Len() int
-  func (g CommandGroup) Less(i, j int) bool
-  func (g *CommandGroup) Name() string
-  func (g CommandGroup) Swap(i, j int)

-  type Commander
-
-  func NewCommander(topLevelFlags *flag.FlagSet, name string) *Commander

-
-  func (cdr *Commander) CommandsCommand() Command
-  func (cdr *Commander) Execute(ctx context.Context, args ...interface{}) ExitStatus
-  func (cdr *Commander) FlagsCommand() Command
-  func (cdr *Commander) HelpCommand() Command
-  func (cdr *Commander) ImportantFlag(name string)
-  func (cdr *Commander) Name() string
-  func (cdr *Commander) Register(cmd Command, group string)
-  func (cdr *Commander) VisitAll(fn func(*flag.Flag))
-  func (cdr *Commander) VisitAllImportant(fn func(*flag.Flag))
-  func (cdr *Commander) VisitCommands(fn func(*CommandGroup, Command))
-  func (cdr *Commander) VisitGroups(fn func(*CommandGroup))

-  type ExitStatus
-
-  func Execute(ctx context.Context, args ...interface{}) ExitStatus

This section is empty.

This section is empty.

```go
func ImportantFlag(name string)
```

ImportantFlag marks a top-level flag as important, which means it will be printed out as part of the output of an ordinary "help" subcommand. (All flags, important or not, are printed by the "flags" subcommand.) It is a wrapper around DefaultCommander.ImportantFlag.

```go
func Register(cmd Command, group string)
```

Register adds a subcommand to the supported subcommands in the specified group. (Help output is sorted and arranged by group name.) The empty string is an acceptable group name; such subcommands are explained first before named groups. It is a wrapper around DefaultCommander.Register.

```go
type Command interface {
	// Name returns the name of the command.
	Name() string

	// Synopsis returns a short string (less than one line) describing the command.
	Synopsis() string

	// Usage returns a long string explaining the command and giving usage
	// information.
	Usage() string

	// SetFlags adds the flags for this command to the specified set.
	SetFlags(*flag.FlagSet)

	// Execute executes the command and returns an ExitStatus.
	Execute(ctx context.Context, f *flag.FlagSet, args ...interface{}) ExitStatus
}
```

A Command represents a single command.

```go
func Alias(alias string, cmd Command) Command
```

Alias returns a Command alias which implements a "commands" subcommand.

```go
func CommandsCommand() Command
```

CommandsCommand returns Command which implements a "commands" subcommand.

```go
func FlagsCommand() Command
```

FlagsCommand returns a Command which implements "flags" for the DefaultCommander. Use Register(FlagsCommand(), <group>) for it to be recognized.

```go
func HelpCommand() Command
```

HelpCommand returns a Command which implements "help" for the DefaultCommander. Use Register(HelpCommand(), <group>) for it to be recognized.

```go
type CommandGroup struct {
	// contains filtered or unexported fields
}
```

A CommandGroup represents a set of commands about a common topic.

```go
func (g CommandGroup) Len() int
```

Sorting of the commands within a group.

```go
func (g CommandGroup) Less(i, j int) bool
```

```go
func (g *CommandGroup) Name() string
```

Name returns the group name

```go
func (g CommandGroup) Swap(i, j int)
```

```go
type Commander struct {
	Explain        func(io.Writer)                // A function to print a top level usage explanation. Can be overridden.
	ExplainGroup   func(io.Writer, *CommandGroup) // A function to print a command group's usage explanation. Can be overridden.
	ExplainCommand func(io.Writer, Command)       // A function to print a command usage explanation. Can be overridden.

	Output io.Writer // Output specifies where the commander should write its output (default: os.Stdout).
	Error  io.Writer // Error specifies where the commander should write its error (default: os.Stderr).
	// contains filtered or unexported fields
}
```

A Commander represents a set of commands.

```go
var DefaultCommander *Commander
```

DefaultCommander is the default commander using flag.CommandLine for flags and os.Args[0] for the command name.

```go
func NewCommander(topLevelFlags *flag.FlagSet, name string) *Commander
```

NewCommander returns a new commander with the specified top-level flags and command name. The Usage function for the topLevelFlags will be set as well.

```go
func (cdr *Commander) CommandsCommand() Command
```

CommandsCommand returns Command which implements a "commands" subcommand.

```go
func (cdr *Commander) Execute(ctx context.Context, args ...interface{}) ExitStatus
```

Execute should be called once the top-level-flags on a Commander have been initialized. It finds the correct subcommand and executes it, and returns an ExitStatus with the result. On a usage error, an appropriate message is printed to os.Stderr, and ExitUsageError is returned. The additional args are provided as-is to the Execute method of the selected Command.

```go
func (cdr *Commander) FlagsCommand() Command
```

FlagsCommand returns a Command which implements a "flags" subcommand.

```go
func (cdr *Commander) HelpCommand() Command
```

HelpCommand returns a Command which implements a "help" subcommand.

```go
func (cdr *Commander) ImportantFlag(name string)
```

ImportantFlag marks a top-level flag as important, which means it will be printed out as part of the output of an ordinary "help" subcommand. (All flags, important or not, are printed by the "flags" subcommand.)

```go
func (cdr *Commander) Name() string
```

Name returns the commander's name

```go
func (cdr *Commander) Register(cmd Command, group string)
```

Register adds a subcommand to the supported subcommands in the specified group. (Help output is sorted and arranged by group name.) The empty string is an acceptable group name; such subcommands are explained first before named groups.

```go
func (cdr *Commander) VisitAll(fn func(*flag.Flag))
```

VisitAll visits the top level flags in lexicographical order, calling fn for each. It visits all flags, even those not set.

```go
func (cdr *Commander) VisitAllImportant(fn func(*flag.Flag))
```

VisitAllImportant visits the important top level flags in lexicographical order, calling fn for each. It visits all flags, even those not set.

```go
func (cdr *Commander) VisitCommands(fn func(*CommandGroup, Command))
```

VisitCommands visits each command in registered order grouped by command group in lexicographical order, calling fn for each.

```go
func (cdr *Commander) VisitGroups(fn func(*CommandGroup))
```

VisitGroups visits each command group in lexicographical order, calling fn for each.

```go
type ExitStatus int
```

An ExitStatus represents a Posix exit status that a subcommand expects to be returned to the shell.

```go
const (
	ExitSuccess ExitStatus = iota
	ExitFailure
	ExitUsageError
)
```

```go
func Execute(ctx context.Context, args ...interface{}) ExitStatus
```

Execute should be called once the default flags have been initialized by flag.Parse. It finds the correct subcommand and executes it, and returns an ExitStatus with the result. On a usage error, an appropriate message is printed to os.Stderr, and ExitUsageError is returned. The additional args are provided as-is to the Execute method of the selected Command. It is a wrapper around DefaultCommander.Execute.

##   Source Files ¶
 View all Source files <https://github.com/google/subcommands/tree/v1.2.0>

- subcommands.go <https://github.com/google/subcommands/blob/v1.2.0/subcommands.go>

  Click to show internal directories.
  Click to hide internal directories.

  Close

     **?** : This menu   **/** : Search site   **f** or **F** : Jump to   **y** or **Y**  : Canonical URL
  Close
