---
source_name: "External Linked Documentation"
source_url: "https://pkg.go.dev/github.com/spf13/cobra"
source_path: "sources/raw/external/pkg-go-dev-github-com-spf13-cobra-c48fa3a8d3.html"
license_ref: ""
---

# Overview

Context returns underlying command context. If command was executed with ExecuteContext or the context was set with SetContext, the previously set context will be returned. Otherwise, nil is returned.

Notice that a call to Execute and ExecuteC will replace a nil context of a command with a context.Background, so a background context will be returned by Context after one of these functions has been called.

```go
func (c *Command) DebugFlags()
```

DebugFlags used to determine which flags have been assigned to which commands and which persist.

```go
func (c *Command) DisplayName() string
```

DisplayName returns the name to display in help text. Returns command Name() If CommandDisplayNameAnnoation is not set

```go
func (c *Command) ErrOrStderr() io.Writer
```

ErrOrStderr returns output to stderr

```go
func (c *Command) ErrPrefix() string
```

ErrPrefix return error message prefix for the command

```go
func (c *Command) Execute() error
```

Execute uses the args (os.Args[1:] by default) and run through the command tree finding appropriate matches for commands and then corresponding flags.

```go
func (c *Command) ExecuteC() (cmd *Command, err error)
```

ExecuteC executes the command.

```go
func (c *Command) ExecuteContext(ctx context.Context) error
```

ExecuteContext is the same as Execute(), but sets the ctx on the command. Retrieve ctx by calling cmd.Context() inside your *Run lifecycle or ValidArgs functions.

```go
func (c *Command) ExecuteContextC(ctx context.Context) (*Command, error)
```

ExecuteContextC is the same as ExecuteC(), but sets the ctx on the command. Retrieve ctx by calling cmd.Context() inside your *Run lifecycle or ValidArgs functions.

```go
func (c *Command) Find(args []string) (*Command, []string, error)
```

Find the target command given the args and command tree Meant to be run on the highest node. Only searches down.

```go
func (c *Command) Flag(name string) (flag *flag.Flag)
```

Flag climbs up the command tree looking for matching flag.

```go
func (c *Command) FlagErrorFunc() (f func(*Command, error) error)
```

FlagErrorFunc returns either the function set by SetFlagErrorFunc for this command or a parent, or it returns a function which returns the original error.

```go
func (c *Command) Flags() *flag.FlagSet
```

Flags returns the complete FlagSet that applies to this command (local and persistent declared here and by all parents).

```go
func (c *Command) GenBashCompletion(w io.Writer) error
```

GenBashCompletion generates bash completion file and writes to the passed writer.

```go
func (c *Command) GenBashCompletionFile(filename string) error
```

GenBashCompletionFile generates bash completion file.

```go
func (c *Command) GenBashCompletionFileV2(filename string, includeDesc bool) error
```

GenBashCompletionFileV2 generates Bash completion version 2.

```go
func (c *Command) GenBashCompletionV2(w io.Writer, includeDesc bool) error
```

GenBashCompletionV2 generates Bash completion file version 2 and writes it to the passed writer.

```go
func (c *Command) GenFishCompletion(w io.Writer, includeDesc bool) error
```

GenFishCompletion generates fish completion file and writes to the passed writer.

```go
func (c *Command) GenFishCompletionFile(filename string, includeDesc bool) error
```

GenFishCompletionFile generates fish completion file.

```go
func (c *Command) GenPowerShellCompletion(w io.Writer) error
```

GenPowerShellCompletion generates powershell completion file without descriptions and writes it to the passed writer.

```go
func (c *Command) GenPowerShellCompletionFile(filename string) error
```

GenPowerShellCompletionFile generates powershell completion file without descriptions.

```go
func (c *Command) GenPowerShellCompletionFileWithDesc(filename string) error
```

GenPowerShellCompletionFileWithDesc generates powershell completion file with descriptions.

```go
func (c *Command) GenPowerShellCompletionWithDesc(w io.Writer) error
```

GenPowerShellCompletionWithDesc generates powershell completion file with descriptions and writes it to the passed writer.

```go
func (c *Command) GenZshCompletion(w io.Writer) error
```

GenZshCompletion generates zsh completion file including descriptions and writes it to the passed writer.

```go
func (c *Command) GenZshCompletionFile(filename string) error
```

GenZshCompletionFile generates zsh completion file including descriptions.

```go
func (c *Command) GenZshCompletionFileNoDesc(filename string) error
```

GenZshCompletionFileNoDesc generates zsh completion file without descriptions.

```go
func (c *Command) GenZshCompletionNoDesc(w io.Writer) error
```

GenZshCompletionNoDesc generates zsh completion file without descriptions and writes it to the passed writer.

```go
func (c *Command) GetFlagCompletionFunc(flagName string) (CompletionFunc, bool)
```

GetFlagCompletionFunc returns the completion function for the given flag of the command, if available.

```go
func (c *Command) GlobalNormalizationFunc() func(f *flag.FlagSet, name string) flag.NormalizedName
```

GlobalNormalizationFunc returns the global normalization function or nil if it doesn't exist.

```go
func (c *Command) Groups() []*Group
```

Groups returns a slice of child command groups.

```go
func (c *Command) HasAlias(s string) bool
```

HasAlias determines if a given string is an alias of the command.

```go
func (c *Command) HasAvailableFlags() bool
```

HasAvailableFlags checks if the command contains any flags (local plus persistent from the entire structure) which are not hidden or deprecated.

```go
func (c *Command) HasAvailableInheritedFlags() bool
```

HasAvailableInheritedFlags checks if the command has flags inherited from its parent command which are not hidden or deprecated.

```go
func (c *Command) HasAvailableLocalFlags() bool
```

HasAvailableLocalFlags checks if the command has flags specifically declared locally which are not hidden or deprecated.

```go
func (c *Command) HasAvailablePersistentFlags() bool
```

HasAvailablePersistentFlags checks if the command contains persistent flags which are not hidden or deprecated.

```go
func (c *Command) HasAvailableSubCommands() bool
```

HasAvailableSubCommands determines if a command has available sub commands that need to be shown in the usage/help default template under 'available commands'.

```go
func (c *Command) HasExample() bool
```

HasExample determines if the command has example.

```go
func (c *Command) HasFlags() bool
```

HasFlags checks if the command contains any flags (local plus persistent from the entire structure).

```go
func (c *Command) HasHelpSubCommands() bool
```

HasHelpSubCommands determines if a command has any available 'help' sub commands that need to be shown in the usage/help default template under 'additional help topics'.

```go
func (c *Command) HasInheritedFlags() bool
```

HasInheritedFlags checks if the command has flags inherited from its parent command.

```go
func (c *Command) HasLocalFlags() bool
```

HasLocalFlags checks if the command has flags specifically declared locally.

```go
func (c *Command) HasParent() bool
```

HasParent determines if the command is a child command.

```go
func (c *Command) HasPersistentFlags() bool
```

HasPersistentFlags checks if the command contains persistent flags.

```go
func (c *Command) HasSubCommands() bool
```

HasSubCommands determines if the command has children commands.

```go
func (c *Command) Help() error
```

Help puts out the help for the command. Used when a user calls help [command]. Can be defined by user by overriding HelpFunc.

```go
func (c *Command) HelpFunc() func(*Command, []string)
```

HelpFunc returns either the function set by SetHelpFunc for this command or a parent, or it returns a function with default help behavior.

```go
func (c *Command) HelpTemplate() string
```

HelpTemplate return help template for the command. This function is kept for backwards-compatibility reasons.

```go
func (c *Command) InOrStdin() io.Reader
```

InOrStdin returns input to stdin

```go
func (c *Command) InheritedFlags() *flag.FlagSet
```

InheritedFlags returns all flags which were inherited from parent commands. This function does not modify the flags of the current command, it's purpose is to return the current state.

```go
func (c *Command) InitDefaultCompletionCmd(args ...string)
```

InitDefaultCompletionCmd adds a default 'completion' command to c. This function will do nothing if any of the following is true: 1- the feature has been explicitly disabled by the program, 2- c has no subcommands (to avoid creating one), 3- c already has a 'completion' command provided by the program.

```go
func (c *Command) InitDefaultHelpCmd()
```

InitDefaultHelpCmd adds default help command to c. It is called automatically by executing the c or by calling help and usage. If c already has help command or c has no subcommands, it will do nothing.

```go
func (c *Command) InitDefaultHelpFlag()
```

InitDefaultHelpFlag adds default help flag to c. It is called automatically by executing the c or by calling help and usage. If c already has help flag, it will do nothing.

```go
func (c *Command) InitDefaultVersionFlag()
```

InitDefaultVersionFlag adds default version flag to c. It is called automatically by executing the c. If c already has a version flag, it will do nothing. If c.Version is empty, it will do nothing.

```go
func (c *Command) IsAdditionalHelpTopicCommand() bool
```

IsAdditionalHelpTopicCommand determines if a command is an additional help topic command; additional help topic command is determined by the fact that it is NOT runnable/hidden/deprecated, and has no sub commands that are runnable/hidden/deprecated. Concrete example: https://github.com/spf13/cobra/issues/393#issuecomment-282741924 <https://github.com/spf13/cobra/issues/393#issuecomment-282741924>.

```go
func (c *Command) IsAvailableCommand() bool
```

IsAvailableCommand determines if a command is available as a non-help command (this includes all non deprecated/hidden commands).

```go
func (c *Command) LocalFlags() *flag.FlagSet
```

LocalFlags returns the local FlagSet specifically set in the current command. This function does not modify the flags of the current command, it's purpose is to return the current state.

```go
func (c *Command) LocalNonPersistentFlags() *flag.FlagSet
```

LocalNonPersistentFlags are flags specific to this command which will NOT persist to subcommands. This function does not modify the flags of the current command, it's purpose is to return the current state.

```go
func (c *Command) MarkFlagCustom(name string, f string) error
```

MarkFlagCustom adds the BashCompCustom annotation to the named flag, if it exists. The bash completion script will call the bash function f for the flag.

This will only work for bash completion. It is recommended to instead use c.RegisterFlagCompletionFunc(...) which allows to register a Go function which will work across all shells.

```go
func (c *Command) MarkFlagDirname(name string) error
```

MarkFlagDirname instructs the various shell completion implementations to limit completions for the named flag to directory names.

```go
func (c *Command) MarkFlagFilename(name string, extensions ...string) error
```

MarkFlagFilename instructs the various shell completion implementations to limit completions for the named flag to the specified file extensions.

```go
func (c *Command) MarkFlagRequired(name string) error
```

MarkFlagRequired instructs the various shell completion implementations to prioritize the named flag when performing completion, and causes your command to report an error if invoked without the flag.

```go
func (c *Command) MarkFlagsMutuallyExclusive(flagNames ...string)
```
