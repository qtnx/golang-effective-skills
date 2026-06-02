---
source_name: "External Linked Documentation"
source_url: "https://pkg.go.dev/github.com/spf13/cobra"
source_path: "sources/raw/external/pkg-go-dev-github-com-spf13-cobra-c48fa3a8d3.html"
license_ref: ""
---

# Overview

```go
type CompletionOptions struct {
	// DisableDefaultCmd prevents Cobra from creating a default 'completion' command
	DisableDefaultCmd bool
	// DisableNoDescFlag prevents Cobra from creating the '--no-descriptions' flag
	// for shells that support completion descriptions
	DisableNoDescFlag bool
	// DisableDescriptions turns off all completion descriptions for shells
	// that support them
	DisableDescriptions bool
	// HiddenDefaultCmd makes the default 'completion' command hidden
	HiddenDefaultCmd bool
	// DefaultShellCompDirective sets the ShellCompDirective that is returned
	// if no special directive can be determined
	DefaultShellCompDirective *ShellCompDirective
}
```

CompletionOptions are the options to control shell completion

```go
func (receiver *CompletionOptions) SetDefaultShellCompDirective(directive ShellCompDirective)
```

```go
type FParseErrWhitelist flag.ParseErrorsAllowlist
```

FParseErrWhitelist configures Flag parse errors to be ignored

```go
type Group struct {
	ID    string
	Title string
}
```

Group Structure to manage groups for commands

```go
type PositionalArgs func(cmd *Command, args []string) error
```

```go
func ExactArgs(n int) PositionalArgs
```

ExactArgs returns an error if there are not exactly n args.

```go
func ExactValidArgs(n int) PositionalArgs
```

ExactValidArgs returns an error if there are not exactly N positional args OR there are any positional args that are not in the `ValidArgs` field of `Command`

Deprecated: use MatchAll(ExactArgs(n), OnlyValidArgs) instead

```go
func MatchAll(pargs ...PositionalArgs) PositionalArgs
```

MatchAll allows combining several PositionalArgs to work in concert.

```go
func MaximumNArgs(n int) PositionalArgs
```

MaximumNArgs returns an error if there are more than N args.

```go
func MinimumNArgs(n int) PositionalArgs
```

MinimumNArgs returns an error if there is not at least N args.

```go
func RangeArgs(min int, max int) PositionalArgs
```

RangeArgs returns an error if the number of args is not within the expected range.

```go
type ShellCompDirective int
```

ShellCompDirective is a bit map representing the different behaviors the shell can be instructed to have once completions have been provided.

```go
const (
	// ShellCompDirectiveError indicates an error occurred and completions should be ignored.
	ShellCompDirectiveError ShellCompDirective = 1 << iota

// ShellCompDirectiveNoSpace indicates that the shell should not add a space
	// after the completion even if there is a single completion provided.
	ShellCompDirectiveNoSpace

// ShellCompDirectiveNoFileComp indicates that the shell should not provide
	// file completion even when no completion is provided.
	ShellCompDirectiveNoFileComp

// ShellCompDirectiveFilterFileExt indicates that the provided completions
	// should be used as file extension filters.
	// For flags, using Command.MarkFlagFilename() and Command.MarkPersistentFlagFilename()
	// is a shortcut to using this directive explicitly.  The BashCompFilenameExt
	// annotation can also be used to obtain the same behavior for flags.
	ShellCompDirectiveFilterFileExt

// ShellCompDirectiveFilterDirs indicates that only directory names should
	// be provided in file completion.  To request directory names within another
	// directory, the returned completions should specify the directory within
	// which to search.  The BashCompSubdirsInDir annotation can be used to
	// obtain the same behavior but only for flags.
	ShellCompDirectiveFilterDirs

// ShellCompDirectiveKeepOrder indicates that the shell should preserve the order
	// in which the completions are provided
	ShellCompDirectiveKeepOrder

// ShellCompDirectiveDefault indicates to let the shell perform its default
	// behavior after completions have been provided.
	// This one must be last to avoid messing up the iota count.
	ShellCompDirectiveDefault ShellCompDirective = 0
)
```

```go
type SliceValue interface {
	// GetSlice returns the flag value list as an array of strings.
	GetSlice() []string
}
```

SliceValue is a reduced version of pflag.SliceValue. It is used to detect flags that accept multiple values and therefore can provide completion multiple times.

# Overview

##   Source Files ¶
 View all Source files <https://github.com/spf13/cobra/tree/v1.10.2>

- active_help.go <https://github.com/spf13/cobra/blob/v1.10.2/active_help.go>
- args.go <https://github.com/spf13/cobra/blob/v1.10.2/args.go>
- bash_completions.go <https://github.com/spf13/cobra/blob/v1.10.2/bash_completions.go>
- bash_completionsV2.go <https://github.com/spf13/cobra/blob/v1.10.2/bash_completionsV2.go>
- cobra.go <https://github.com/spf13/cobra/blob/v1.10.2/cobra.go>
- command.go <https://github.com/spf13/cobra/blob/v1.10.2/command.go>
- command_notwin.go <https://github.com/spf13/cobra/blob/v1.10.2/command_notwin.go>
- completions.go <https://github.com/spf13/cobra/blob/v1.10.2/completions.go>
- fish_completions.go <https://github.com/spf13/cobra/blob/v1.10.2/fish_completions.go>
- flag_groups.go <https://github.com/spf13/cobra/blob/v1.10.2/flag_groups.go>
- powershell_completions.go <https://github.com/spf13/cobra/blob/v1.10.2/powershell_completions.go>
- shell_completions.go <https://github.com/spf13/cobra/blob/v1.10.2/shell_completions.go>
- zsh_completions.go <https://github.com/spf13/cobra/blob/v1.10.2/zsh_completions.go>

# Overview

##   Directories ¶
    Show internal   Expand all

doc

Click to show internal directories.
  Click to hide internal directories.

Close

**?** : This menu   **/** : Search site   **f** or **F** : Jump to   **y** or **Y**  : Canonical URL
  Close
