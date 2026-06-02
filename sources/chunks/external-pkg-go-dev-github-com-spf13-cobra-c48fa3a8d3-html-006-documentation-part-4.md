---
source_name: "External Linked Documentation"
source_url: "https://pkg.go.dev/github.com/spf13/cobra"
source_path: "sources/raw/external/pkg-go-dev-github-com-spf13-cobra-c48fa3a8d3.html"
license_ref: ""
---

# Overview

MarkFlagsMutuallyExclusive marks the given flags with annotations so that Cobra errors if the command is invoked with more than one flag from the given set of flags.

```go
func (c *Command) MarkFlagsOneRequired(flagNames ...string)
```

MarkFlagsOneRequired marks the given flags with annotations so that Cobra errors if the command is invoked without at least one flag from the given set of flags.

```go
func (c *Command) MarkFlagsRequiredTogether(flagNames ...string)
```

MarkFlagsRequiredTogether marks the given flags with annotations so that Cobra errors if the command is invoked with a subset (but not all) of the given flags.

```go
func (c *Command) MarkPersistentFlagDirname(name string) error
```

MarkPersistentFlagDirname instructs the various shell completion implementations to limit completions for the named persistent flag to directory names.

```go
func (c *Command) MarkPersistentFlagFilename(name string, extensions ...string) error
```

MarkPersistentFlagFilename instructs the various shell completion implementations to limit completions for the named persistent flag to the specified file extensions.

```go
func (c *Command) MarkPersistentFlagRequired(name string) error
```

MarkPersistentFlagRequired instructs the various shell completion implementations to prioritize the named persistent flag when performing completion, and causes your command to report an error if invoked without the flag.

```go
func (c *Command) MarkZshCompPositionalArgumentFile(argPosition int, patterns ...string) error
```

MarkZshCompPositionalArgumentFile only worked for zsh and its behavior was not consistent with Bash completion. It has therefore been disabled. Instead, when no other completion is specified, file completion is done by default for every argument. One can disable file completion on a per-argument basis by using ValidArgsFunction and ShellCompDirectiveNoFileComp. To achieve file extension filtering, one can use ValidArgsFunction and ShellCompDirectiveFilterFileExt.

Deprecated

```go
func (c *Command) MarkZshCompPositionalArgumentWords(argPosition int, words ...string) error
```

MarkZshCompPositionalArgumentWords only worked for zsh. It has therefore been disabled. To achieve the same behavior across all shells, one can use ValidArgs (for the first argument only) or ValidArgsFunction for any argument (can include the first one also).

Deprecated

```go
func (c *Command) Name() string
```

Name returns the command's name: the first word in the use line.

```go
func (c *Command) NameAndAliases() string
```

NameAndAliases returns a list of the command name and all aliases

```go
func (c *Command) NamePadding() int
```

NamePadding returns padding for the name.

```go
func (c *Command) NonInheritedFlags() *flag.FlagSet
```

NonInheritedFlags returns all flags which were not inherited from parent commands. This function does not modify the flags of the current command, it's purpose is to return the current state.

```go
func (c *Command) OutOrStderr() io.Writer
```

OutOrStderr returns output to stderr

```go
func (c *Command) OutOrStdout() io.Writer
```

OutOrStdout returns output to stdout.

```go
func (c *Command) Parent() *Command
```

Parent returns a commands parent command.

```go
func (c *Command) ParseFlags(args []string) error
```

ParseFlags parses persistent flag tree and local flags.

```go
func (c *Command) PersistentFlags() *flag.FlagSet
```

PersistentFlags returns the persistent FlagSet specifically set in the current command.

```go
func (c *Command) Print(i ...interface{})
```

Print is a convenience method to Print to the defined output, fallback to Stderr if not set.

```go
func (c *Command) PrintErr(i ...interface{})
```

PrintErr is a convenience method to Print to the defined Err output, fallback to Stderr if not set.

```go
func (c *Command) PrintErrf(format string, i ...interface{})
```

PrintErrf is a convenience method to Printf to the defined Err output, fallback to Stderr if not set.

```go
func (c *Command) PrintErrln(i ...interface{})
```

PrintErrln is a convenience method to Println to the defined Err output, fallback to Stderr if not set.

```go
func (c *Command) Printf(format string, i ...interface{})
```

Printf is a convenience method to Printf to the defined output, fallback to Stderr if not set.

```go
func (c *Command) Println(i ...interface{})
```

Println is a convenience method to Println to the defined output, fallback to Stderr if not set.

```go
func (c *Command) RegisterFlagCompletionFunc(flagName string, f CompletionFunc) error
```

RegisterFlagCompletionFunc should be called to register a function to provide completion for a flag.

You can use pre-defined completion functions such as FixedCompletions or NoFileCompletions, or you can define your own.

```go
func (c *Command) RemoveCommand(cmds ...*Command)
```

RemoveCommand removes one or more commands from a parent command.

```go
func (c *Command) ResetCommands()
```

ResetCommands delete parent, subcommand and help command from c.

```go
func (c *Command) ResetFlags()
```

ResetFlags deletes all flags from command.

```go
func (c *Command) Root() *Command
```

Root finds root command.

```go
func (c *Command) Runnable() bool
```

Runnable determines if the command is itself runnable.

```go
func (c *Command) SetArgs(a []string)
```

SetArgs sets arguments for the command. It is set to os.Args[1:] by default, if desired, can be overridden particularly useful when testing.

```go
func (c *Command) SetCompletionCommandGroupID(groupID string)
```

SetCompletionCommandGroupID sets the group id of the completion command.

```go
func (c *Command) SetContext(ctx context.Context)
```

SetContext sets context for the command. This context will be overwritten by Command.ExecuteContext or Command.ExecuteContextC.

```go
func (c *Command) SetErr(newErr io.Writer)
```

SetErr sets the destination for error messages. If newErr is nil, os.Stderr is used.

```go
func (c *Command) SetErrPrefix(s string)
```

SetErrPrefix sets error message prefix to be used. Application can use it to set custom prefix.

```go
func (c *Command) SetFlagErrorFunc(f func(*Command, error) error)
```

SetFlagErrorFunc sets a function to generate an error when flag parsing fails.

```go
func (c *Command) SetGlobalNormalizationFunc(n func(f *flag.FlagSet, name string) flag.NormalizedName)
```

SetGlobalNormalizationFunc sets a normalization function to all flag sets and also to child commands. The user should not have a cyclic dependency on commands.

```go
func (c *Command) SetHelpCommand(cmd *Command)
```

SetHelpCommand sets help command.

```go
func (c *Command) SetHelpCommandGroupID(groupID string)
```

SetHelpCommandGroupID sets the group id of the help command.

```go
func (c *Command) SetHelpFunc(f func(*Command, []string))
```

SetHelpFunc sets help function. Can be defined by Application.

```go
func (c *Command) SetHelpTemplate(s string)
```

SetHelpTemplate sets help template to be used. Application can use it to set custom template.

```go
func (c *Command) SetIn(newIn io.Reader)
```

SetIn sets the source for input data If newIn is nil, os.Stdin is used.

```go
func (c *Command) SetOut(newOut io.Writer)
```

SetOut sets the destination for usage messages. If newOut is nil, os.Stdout is used.

```go
func (c *Command) SetOutput(output io.Writer)
```

SetOutput sets the destination for usage and error messages. If output is nil, os.Stderr is used.

Deprecated: Use SetOut and/or SetErr instead

```go
func (c *Command) SetUsageFunc(f func(*Command) error)
```

SetUsageFunc sets usage function. Usage can be defined by application.

```go
func (c *Command) SetUsageTemplate(s string)
```

SetUsageTemplate sets usage template. Can be defined by Application.

```go
func (c *Command) SetVersionTemplate(s string)
```

SetVersionTemplate sets version template to be used. Application can use it to set custom template.

```go
func (c *Command) SuggestionsFor(typedName string) []string
```

SuggestionsFor provides suggestions for the typedName.

```go
func (c *Command) Traverse(args []string) (*Command, []string, error)
```

Traverse the command tree to find the command, and parse args for each parent.

```go
func (c *Command) Usage() error
```

Usage puts out the usage for the command. Used when a user provides invalid input. Can be defined by user by overriding UsageFunc.

```go
func (c *Command) UsageFunc() (f func(*Command) error)
```

UsageFunc returns either the function set by SetUsageFunc for this command or a parent, or it returns a default usage function.

```go
func (c *Command) UsagePadding() int
```

UsagePadding return padding for the usage.

```go
func (c *Command) UsageString() string
```

UsageString returns usage string.

```go
func (c *Command) UsageTemplate() string
```

UsageTemplate returns usage template for the command. This function is kept for backwards-compatibility reasons.

```go
func (c *Command) UseLine() string
```

UseLine puts out the full usage for a given command (including parents).

```go
func (c *Command) ValidateArgs(args []string) error
```

```go
func (c *Command) ValidateFlagGroups() error
```

ValidateFlagGroups validates the mutuallyExclusive/oneRequired/requiredAsGroup logic and returns the first error encountered.

```go
func (c *Command) ValidateRequiredFlags() error
```

ValidateRequiredFlags validates all required flags are present and returns an error otherwise

```go
func (c *Command) VersionTemplate() string
```

VersionTemplate return version template for the command. This function is kept for backwards-compatibility reasons.

```go
func (c *Command) VisitParents(fn func(*Command))
```

VisitParents visits all parents of the command and invokes fn on each parent.

```go
type Completion = string
```

Completion is a string that can be used for completions

two formats are supported:

- the completion choice
- the completion choice with a textual description (separated by a TAB).

CompletionWithDesc can be used to create a completion string with a textual description.

Note: Go type alias is used to provide a more descriptive name in the documentation, but any string can be used.

```go
func AppendActiveHelp(compArray []Completion, activeHelpStr string) []Completion
```

AppendActiveHelp adds the specified string to the specified array to be used as ActiveHelp. Such strings will be processed by the completion script and will be shown as ActiveHelp to the user. The array parameter should be the array that will contain the completions. This function can be called multiple times before and/or after completions are added to the array. Each time this function is called with the same array, the new ActiveHelp line will be shown below the previous ones when completion is triggered.

```go
func CompletionWithDesc(choice string, description string) Completion
```

CompletionWithDesc returns a Completion with a description by using the TAB delimited format.

```go
type CompletionFunc = func(cmd *Command, args []string, toComplete string) ([]Completion, ShellCompDirective)
```

CompletionFunc is a function that provides completion results.

```go
func FixedCompletions(choices []Completion, directive ShellCompDirective) CompletionFunc
```

FixedCompletions can be used to create a completion function which always returns the same results.

This method returns a function that satisfies CompletionFunc It can be used with Command.RegisterFlagCompletionFunc and for [Command.ValidArgsFunction].
