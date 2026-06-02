---
source_name: "External Linked Documentation"
source_url: "https://pkg.go.dev/github.com/spf13/cobra"
source_path: "sources/raw/external/pkg-go-dev-github-com-spf13-cobra-c48fa3a8d3.html"
license_ref: ""
---

# Overview

CompDebugln prints the specified string with a newline at the end to the same file as where the completion script prints its logs. Such logs are only printed when the user has set the environment variable BASH_COMP_DEBUG_FILE to the path of some file to be used.

```go
func CompError(msg string)
```

CompError prints the specified completion message to stderr.

```go
func CompErrorln(msg string)
```

CompErrorln prints the specified completion message to stderr with a newline at the end.

```go
func Eq(a interface{}, b interface{}) bool
```

Eq takes two types and checks whether they are equal. Supported types are int and string. Unsupported types will panic.

```go
func GetActiveHelpConfig(cmd *Command) string
```

GetActiveHelpConfig returns the value of the ActiveHelp environment variable <PROGRAM>_ACTIVE_HELP where <PROGRAM> is the name of the root command in upper case, with all non-ASCII-alphanumeric characters replaced by `_`. It will always return "0" if the global environment variable COBRA_ACTIVE_HELP is set to "0".

```go
func Gt(a interface{}, b interface{}) bool
```

Gt takes two types and checks whether the first type is greater than the second. In case of types Arrays, Chans, Maps and Slices, Gt will compare their lengths. Ints are compared directly while strings are first parsed as ints and then compared.

```go
func MarkFlagCustom(flags *pflag.FlagSet, name string, f string) error
```

MarkFlagCustom adds the BashCompCustom annotation to the named flag, if it exists. The bash completion script will call the bash function f for the flag.

This will only work for bash completion. It is recommended to instead use c.RegisterFlagCompletionFunc(...) which allows to register a Go function which will work across all shells.

```go
func MarkFlagDirname(flags *pflag.FlagSet, name string) error
```

MarkFlagDirname instructs the various shell completion implementations to limit completions for the named flag to directory names.

```go
func MarkFlagFilename(flags *pflag.FlagSet, name string, extensions ...string) error
```

MarkFlagFilename instructs the various shell completion implementations to limit completions for the named flag to the specified file extensions.

```go
func MarkFlagRequired(flags *pflag.FlagSet, name string) error
```

MarkFlagRequired instructs the various shell completion implementations to prioritize the named flag when performing completion, and causes your command to report an error if invoked without the flag.

```go
func NoArgs(cmd *Command, args []string) error
```

NoArgs returns an error if any args are included.

```go
func NoFileCompletions(cmd *Command, args []string, toComplete string) ([]Completion, ShellCompDirective)
```

NoFileCompletions can be used to disable file completion for commands that should not trigger file completions.

This method satisfies CompletionFunc. It can be used with Command.RegisterFlagCompletionFunc and for [Command.ValidArgsFunction].

```go
func OnFinalize(y ...func())
```

OnFinalize sets the passed functions to be run when each command's Execute method is terminated.

```go
func OnInitialize(y ...func())
```

OnInitialize sets the passed functions to be run when each command's Execute method is called.

```go
func OnlyValidArgs(cmd *Command, args []string) error
```

OnlyValidArgs returns an error if there are any positional args that are not in the `ValidArgs` field of `Command`

```go
func WriteStringAndCheck(b io.StringWriter, s string)
```

WriteStringAndCheck writes a string into a buffer, and checks if the error is not nil.

```go
type Command struct {
	// Use is the one-line usage message.
	// Recommended syntax is as follows:
	//   [ ] identifies an optional argument. Arguments that are not enclosed in brackets are required.
	//   ... indicates that you can specify multiple values for the previous argument.
	//   |   indicates mutually exclusive information. You can use the argument to the left of the separator or the
	//       argument to the right of the separator. You cannot use both arguments in a single use of the command.
	//   { } delimits a set of mutually exclusive arguments when one of the arguments is required. If the arguments are
	//       optional, they are enclosed in brackets ([ ]).
	// Example: add [-F file | -D dir]... [-f format] profile
	Use string

// Aliases is an array of aliases that can be used instead of the first word in Use.
	Aliases []string

// SuggestFor is an array of command names for which this command will be suggested -
	// similar to aliases but only suggests.
	SuggestFor []string

// Short is the short description shown in the 'help' output.
	Short string

// The group id under which this subcommand is grouped in the 'help' output of its parent.
	GroupID string

// Long is the long message shown in the 'help <this-command>' output.
	Long string

// Example is examples of how to use the command.
	Example string

// ValidArgs is list of all valid non-flag arguments that are accepted in shell completions
	ValidArgs []Completion
	// ValidArgsFunction is an optional function that provides valid non-flag arguments for shell completion.
	// It is a dynamic version of using ValidArgs.
	// Only one of ValidArgs and ValidArgsFunction can be used for a command.
	ValidArgsFunction CompletionFunc

// Expected arguments
	Args PositionalArgs

// ArgAliases is List of aliases for ValidArgs.
	// These are not suggested to the user in the shell completion,
	// but accepted if entered manually.
	ArgAliases []string

// BashCompletionFunction is custom bash functions used by the legacy bash autocompletion generator.
	// For portability with other shells, it is recommended to instead use ValidArgsFunction
	BashCompletionFunction string

// Deprecated defines, if this command is deprecated and should print this string when used.
	Deprecated string

// Annotations are key/value pairs that can be used by applications to identify or
	// group commands or set special options.
	Annotations map[string]string

// Version defines the version for this command. If this value is non-empty and the command does not
	// define a "version" flag, a "version" boolean flag will be added to the command and, if specified,
	// will print content of the "Version" variable. A shorthand "v" flag will also be added if the
	// command does not define one.
	Version string

// The *Run functions are executed in the following order:
	//   * PersistentPreRun()
	//   * PreRun()
	//   * Run()
	//   * PostRun()
	//   * PersistentPostRun()
	// All functions get the same args, the arguments after the command name.
	// The *PreRun and *PostRun functions will only be executed if the Run function of the current
	// command has been declared.
	//
	// PersistentPreRun: children of this command will inherit and execute.
	PersistentPreRun func(cmd *Command, args []string)
	// PersistentPreRunE: PersistentPreRun but returns an error.
	PersistentPreRunE func(cmd *Command, args []string) error
	// PreRun: children of this command will not inherit.
	PreRun func(cmd *Command, args []string)
	// PreRunE: PreRun but returns an error.
	PreRunE func(cmd *Command, args []string) error
	// Run: Typically the actual work function. Most commands will only implement this.
	Run func(cmd *Command, args []string)
	// RunE: Run but returns an error.
	RunE func(cmd *Command, args []string) error
	// PostRun: run after the Run command.
	PostRun func(cmd *Command, args []string)
	// PostRunE: PostRun but returns an error.
	PostRunE func(cmd *Command, args []string) error
	// PersistentPostRun: children of this command will inherit and execute after PostRun.
	PersistentPostRun func(cmd *Command, args []string)
	// PersistentPostRunE: PersistentPostRun but returns an error.
	PersistentPostRunE func(cmd *Command, args []string) error

// FParseErrWhitelist flag parse errors to be ignored
	FParseErrWhitelist FParseErrWhitelist

// CompletionOptions is a set of options to control the handling of shell completion
	CompletionOptions CompletionOptions

// TraverseChildren parses flags on all parents before executing child command.
	TraverseChildren bool

// Hidden defines, if this command is hidden and should NOT show up in the list of available commands.
	Hidden bool

// SilenceErrors is an option to quiet errors down stream.
	SilenceErrors bool

// SilenceUsage is an option to silence usage when an error occurs.
	SilenceUsage bool

// DisableFlagParsing disables the flag parsing.
	// If this is true all flags will be passed to the command as arguments.
	DisableFlagParsing bool

// DisableAutoGenTag defines, if gen tag ("Auto generated by spf13/cobra...")
	// will be printed by generating docs for this command.
	DisableAutoGenTag bool

// DisableFlagsInUseLine will disable the addition of [flags] to the usage
	// line of a command when printing help or generating docs
	DisableFlagsInUseLine bool

// DisableSuggestions disables the suggestions based on Levenshtein distance
	// that go along with 'unknown command' messages.
	DisableSuggestions bool

// SuggestionsMinimumDistance defines minimum levenshtein distance to display suggestions.
	// Must be > 0.
	SuggestionsMinimumDistance int
	// contains filtered or unexported fields
}
```

Command is just that, a command for your application. E.g. 'go run ...' - 'run' is the command. Cobra requires you to define the usage and description as part of your command definition to ensure usability.

```go
func (c *Command) AddCommand(cmds ...*Command)
```

AddCommand adds one or more commands to this parent command.

```go
func (c *Command) AddGroup(groups ...*Group)
```

AddGroup adds one or more command groups to this parent command.

```go
func (c *Command) AllChildCommandsHaveGroup() bool
```

AllChildCommandsHaveGroup returns if all subcommands are assigned to a group

```go
func (c *Command) ArgsLenAtDash() int
```

ArgsLenAtDash will return the length of c.Flags().Args at the moment when a -- was found during args parsing.

```go
func (c *Command) CalledAs() string
```

CalledAs returns the command name or alias that was used to invoke this command or an empty string if the command has not been called.

```go
func (c *Command) CommandPath() string
```

CommandPath returns the full path to this command.

```go
func (c *Command) CommandPathPadding() int
```

CommandPathPadding return padding for the command path.

```go
func (c *Command) Commands() []*Command
```

Commands returns a sorted slice of child commands.

```go
func (c *Command) ContainsGroup(groupID string) bool
```

ContainsGroup return if groupID exists in the list of command groups.

```go
func (c *Command) Context() context.Context
```
