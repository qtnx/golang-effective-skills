---
source_name: "External Linked Documentation"
source_url: "https://pkg.go.dev/github.com/spf13/cobra"
source_path: "sources/raw/external/pkg-go-dev-github-com-spf13-cobra-c48fa3a8d3.html"
license_ref: ""
---

# Overview

##   Documentation ¶
   Rendered for <https://go.dev/about#build-context>  linux/amd64 windows/amd64 darwin/amd64 js/wasm

Package cobra is a commander providing a simple interface to create powerful modern CLI interfaces. In addition to providing an interface, Cobra simultaneously provides a controller to organize your application code.

- Constants
- Variables
-  func AddTemplateFunc(name string, tmplFunc interface{})
-  func AddTemplateFuncs(tmplFuncs template.FuncMap)
-  func ArbitraryArgs(cmd *Command, args []string) error
-  func CheckErr(msg interface{})
-  func CompDebug(msg string, printToStdErr bool)
-  func CompDebugln(msg string, printToStdErr bool)
-  func CompError(msg string)
-  func CompErrorln(msg string)
-  func Eq(a interface{}, b interface{}) bool
-  func GetActiveHelpConfig(cmd *Command) string
-  func Gt(a interface{}, b interface{}) bool
-  func MarkFlagCustom(flags *pflag.FlagSet, name string, f string) error
-  func MarkFlagDirname(flags *pflag.FlagSet, name string) error
-  func MarkFlagFilename(flags *pflag.FlagSet, name string, extensions ...string) error
-  func MarkFlagRequired(flags *pflag.FlagSet, name string) error
-  func NoArgs(cmd *Command, args []string) error
-  func NoFileCompletions(cmd *Command, args []string, toComplete string) ([]Completion, ShellCompDirective)
-  func OnFinalize(y ...func())
-  func OnInitialize(y ...func())
-  func OnlyValidArgs(cmd *Command, args []string) error
-  func WriteStringAndCheck(b io.StringWriter, s string)
-  type Command
-
-  func (c *Command) AddCommand(cmds ...*Command)
-  func (c *Command) AddGroup(groups ...*Group)
-  func (c *Command) AllChildCommandsHaveGroup() bool
-  func (c *Command) ArgsLenAtDash() int
-  func (c *Command) CalledAs() string
-  func (c *Command) CommandPath() string
-  func (c *Command) CommandPathPadding() int
-  func (c *Command) Commands() []*Command
-  func (c *Command) ContainsGroup(groupID string) bool
-  func (c *Command) Context() context.Context
-  func (c *Command) DebugFlags()
-  func (c *Command) DisplayName() string
-  func (c *Command) ErrOrStderr() io.Writer
-  func (c *Command) ErrPrefix() string
-  func (c *Command) Execute() error
-  func (c *Command) ExecuteC() (cmd *Command, err error)
-  func (c *Command) ExecuteContext(ctx context.Context) error
-  func (c *Command) ExecuteContextC(ctx context.Context) (*Command, error)
-  func (c *Command) Find(args []string) (*Command, []string, error)
-  func (c *Command) Flag(name string) (flag *flag.Flag)
-  func (c *Command) FlagErrorFunc() (f func(*Command, error) error)
-  func (c *Command) Flags() *flag.FlagSet
-  func (c *Command) GenBashCompletion(w io.Writer) error
-  func (c *Command) GenBashCompletionFile(filename string) error
-  func (c *Command) GenBashCompletionFileV2(filename string, includeDesc bool) error
-  func (c *Command) GenBashCompletionV2(w io.Writer, includeDesc bool) error
-  func (c *Command) GenFishCompletion(w io.Writer, includeDesc bool) error
-  func (c *Command) GenFishCompletionFile(filename string, includeDesc bool) error
-  func (c *Command) GenPowerShellCompletion(w io.Writer) error
-  func (c *Command) GenPowerShellCompletionFile(filename string) error
-  func (c *Command) GenPowerShellCompletionFileWithDesc(filename string) error
-  func (c *Command) GenPowerShellCompletionWithDesc(w io.Writer) error
-  func (c *Command) GenZshCompletion(w io.Writer) error
-  func (c *Command) GenZshCompletionFile(filename string) error
-  func (c *Command) GenZshCompletionFileNoDesc(filename string) error
-  func (c *Command) GenZshCompletionNoDesc(w io.Writer) error
-  func (c *Command) GetFlagCompletionFunc(flagName string) (CompletionFunc, bool)
-  func (c *Command) GlobalNormalizationFunc() func(f *flag.FlagSet, name string) flag.NormalizedName
-  func (c *Command) Groups() []*Group
-  func (c *Command) HasAlias(s string) bool
-  func (c *Command) HasAvailableFlags() bool
-  func (c *Command) HasAvailableInheritedFlags() bool
-  func (c *Command) HasAvailableLocalFlags() bool
-  func (c *Command) HasAvailablePersistentFlags() bool
-  func (c *Command) HasAvailableSubCommands() bool
-  func (c *Command) HasExample() bool
-  func (c *Command) HasFlags() bool
-  func (c *Command) HasHelpSubCommands() bool
-  func (c *Command) HasInheritedFlags() bool
-  func (c *Command) HasLocalFlags() bool
-  func (c *Command) HasParent() bool
-  func (c *Command) HasPersistentFlags() bool
-  func (c *Command) HasSubCommands() bool
-  func (c *Command) Help() error
-  func (c *Command) HelpFunc() func(*Command, []string)
-  func (c *Command) HelpTemplate() string
-  func (c *Command) InOrStdin() io.Reader
-  func (c *Command) InheritedFlags() *flag.FlagSet
-  func (c *Command) InitDefaultCompletionCmd(args ...string)
-  func (c *Command) InitDefaultHelpCmd()
-  func (c *Command) InitDefaultHelpFlag()
-  func (c *Command) InitDefaultVersionFlag()
-  func (c *Command) IsAdditionalHelpTopicCommand() bool
-  func (c *Command) IsAvailableCommand() bool
-  func (c *Command) LocalFlags() *flag.FlagSet
-  func (c *Command) LocalNonPersistentFlags() *flag.FlagSet
-  func (c *Command) MarkFlagCustom(name string, f string) error
-  func (c *Command) MarkFlagDirname(name string) error
-  func (c *Command) MarkFlagFilename(name string, extensions ...string) error
-  func (c *Command) MarkFlagRequired(name string) error
-  func (c *Command) MarkFlagsMutuallyExclusive(flagNames ...string)
-  func (c *Command) MarkFlagsOneRequired(flagNames ...string)
-  func (c *Command) MarkFlagsRequiredTogether(flagNames ...string)
-  func (c *Command) MarkPersistentFlagDirname(name string) error
-  func (c *Command) MarkPersistentFlagFilename(name string, extensions ...string) error
-  func (c *Command) MarkPersistentFlagRequired(name string) error
-  func (c *Command) MarkZshCompPositionalArgumentFile(argPosition int, patterns ...string) error
-  func (c *Command) MarkZshCompPositionalArgumentWords(argPosition int, words ...string) error
-  func (c *Command) Name() string
-  func (c *Command) NameAndAliases() string
-  func (c *Command) NamePadding() int
-  func (c *Command) NonInheritedFlags() *flag.FlagSet
-  func (c *Command) OutOrStderr() io.Writer
-  func (c *Command) OutOrStdout() io.Writer
-  func (c *Command) Parent() *Command
-  func (c *Command) ParseFlags(args []string) error
-  func (c *Command) PersistentFlags() *flag.FlagSet
-  func (c *Command) Print(i ...interface{})
-  func (c *Command) PrintErr(i ...interface{})
-  func (c *Command) PrintErrf(format string, i ...interface{})
-  func (c *Command) PrintErrln(i ...interface{})
-  func (c *Command) Printf(format string, i ...interface{})
-  func (c *Command) Println(i ...interface{})
-  func (c *Command) RegisterFlagCompletionFunc(flagName string, f CompletionFunc) error
-  func (c *Command) RemoveCommand(cmds ...*Command)
-  func (c *Command) ResetCommands()
-  func (c *Command) ResetFlags()
-  func (c *Command) Root() *Command
-  func (c *Command) Runnable() bool
-  func (c *Command) SetArgs(a []string)
-  func (c *Command) SetCompletionCommandGroupID(groupID string)
-  func (c *Command) SetContext(ctx context.Context)
-  func (c *Command) SetErr(newErr io.Writer)
-  func (c *Command) SetErrPrefix(s string)
-  func (c *Command) SetFlagErrorFunc(f func(*Command, error) error)
-  func (c *Command) SetGlobalNormalizationFunc(n func(f *flag.FlagSet, name string) flag.NormalizedName)
-  func (c *Command) SetHelpCommand(cmd *Command)
-  func (c *Command) SetHelpCommandGroupID(groupID string)
-  func (c *Command) SetHelpFunc(f func(*Command, []string))
-  func (c *Command) SetHelpTemplate(s string)
-  func (c *Command) SetIn(newIn io.Reader)
-  func (c *Command) SetOut(newOut io.Writer)
-  func (c *Command) SetOutput(output io.Writer)deprecated
-  func (c *Command) SetUsageFunc(f func(*Command) error)
-  func (c *Command) SetUsageTemplate(s string)
-  func (c *Command) SetVersionTemplate(s string)
-  func (c *Command) SuggestionsFor(typedName string) []string
-  func (c *Command) Traverse(args []string) (*Command, []string, error)
-  func (c *Command) Usage() error
-  func (c *Command) UsageFunc() (f func(*Command) error)
-  func (c *Command) UsagePadding() int
-  func (c *Command) UsageString() string
-  func (c *Command) UsageTemplate() string
-  func (c *Command) UseLine() string
-  func (c *Command) ValidateArgs(args []string) error
-  func (c *Command) ValidateFlagGroups() error
-  func (c *Command) ValidateRequiredFlags() error
-  func (c *Command) VersionTemplate() string
-  func (c *Command) VisitParents(fn func(*Command))

-  type Completion
-
-  func AppendActiveHelp(compArray []Completion, activeHelpStr string) []Completion
-  func CompletionWithDesc(choice string, description string) Completion

-  type CompletionFunc
-
-  func FixedCompletions(choices []Completion, directive ShellCompDirective) CompletionFunc

-  type CompletionOptions
-
-  func (receiver *CompletionOptions) SetDefaultShellCompDirective(directive ShellCompDirective)

-  type FParseErrWhitelist
-  type Group
-  type PositionalArgs
-
-  func ExactArgs(n int) PositionalArgs
-  func ExactValidArgs(n int) PositionalArgsdeprecated
-  func MatchAll(pargs ...PositionalArgs) PositionalArgs
-  func MaximumNArgs(n int) PositionalArgs
-  func MinimumNArgs(n int) PositionalArgs
-  func RangeArgs(min int, max int) PositionalArgs

-  type ShellCompDirective
-  type SliceValue

View Source <https://github.com/spf13/cobra/blob/v1.10.2/bash_completions.go#L29>
```go
const (
	BashCompFilenameExt     = "cobra_annotation_bash_completion_filename_extensions"
	BashCompCustom          = "cobra_annotation_bash_completion_custom"
	BashCompOneRequiredFlag = "cobra_annotation_bash_completion_one_required_flag"
	BashCompSubdirsInDir    = "cobra_annotation_bash_completion_subdirs_in_dir"
)
```

Annotations for Bash completion.
  View Source <https://github.com/spf13/cobra/blob/v1.10.2/command.go#L33>
```go
const (
	FlagSetByCobraAnnotation     = "cobra_annotation_flag_set_by_cobra"
	CommandDisplayNameAnnotation = "cobra_annotation_command_display_name"
)
```

View Source <https://github.com/spf13/cobra/blob/v1.10.2/completions.go#L28>
```go
const (
	// ShellCompRequestCmd is the name of the hidden command that is used to request
	// completion results from the program.  It is used by the shell completion scripts.
	ShellCompRequestCmd = "__complete"
	// ShellCompNoDescRequestCmd is the name of the hidden command that is used to request
	// completion results without their description.  It is used by the shell completion scripts.
	ShellCompNoDescRequestCmd = "__completeNoDesc"
)
```

View Source <https://github.com/spf13/cobra/blob/v1.10.2/cobra.go#L62>
```go
var EnableCaseInsensitive = defaultCaseInsensitive
```

EnableCaseInsensitive allows case-insensitive commands names. (case sensitive by default)
  View Source <https://github.com/spf13/cobra/blob/v1.10.2/cobra.go#L59>
```go
var EnableCommandSorting = defaultCommandSorting
```

EnableCommandSorting controls sorting of the slice of commands, which is turned on by default. To disable sorting, set it to false.
  View Source <https://github.com/spf13/cobra/blob/v1.10.2/cobra.go#L55>
```go
var EnablePrefixMatching = defaultPrefixMatching
```

EnablePrefixMatching allows setting automatic prefix matching. Automatic prefix matching can be a dangerous thing to automatically enable in CLI tools. Set this to true to enable it.
  View Source <https://github.com/spf13/cobra/blob/v1.10.2/cobra.go#L66>
```go
var EnableTraverseRunHooks = defaultTraverseRunHooks
```

EnableTraverseRunHooks executes persistent pre-run and post-run hooks from all parents. By default this is disabled, which means only the first run hook to be found is executed.
  View Source <https://github.com/spf13/cobra/blob/v1.10.2/cobra.go#L81>
```go
var MousetrapDisplayDuration = 5 * time.Second
```

MousetrapDisplayDuration controls how long the MousetrapHelpText message is displayed on Windows if the CLI is started from explorer.exe. Set to 0 to wait for the return key to be pressed. To disable the mousetrap, just set MousetrapHelpText to blank string (""). Works only on Microsoft Windows.
  View Source <https://github.com/spf13/cobra/blob/v1.10.2/cobra.go#L72>
```go
var MousetrapHelpText = `This is a command line tool.

You need to open cmd.exe and run it from there.
`
```

MousetrapHelpText enables an information splash screen on Windows if the CLI is started from explorer.exe. To disable the mousetrap, just set this variable to blank string (""). Works only on Microsoft Windows.

```go
func AddTemplateFunc(name string, tmplFunc interface{})
```

AddTemplateFunc adds a template function that's available to Usage and Help template generation.

```go
func AddTemplateFuncs(tmplFuncs template.FuncMap)
```

AddTemplateFuncs adds multiple template functions that are available to Usage and Help template generation.

```go
func ArbitraryArgs(cmd *Command, args []string) error
```

ArbitraryArgs never returns an error.

```go
func CheckErr(msg interface{})
```

CheckErr prints the msg with the prefix 'Error:' and exits with error code 1. If the msg is nil, it does nothing.

```go
func CompDebug(msg string, printToStdErr bool)
```

CompDebug prints the specified string to the same file as where the completion script prints its logs. Note that completion printouts should never be on stdout as they would be wrongly interpreted as actual completion choices by the completion script.

```go
func CompDebugln(msg string, printToStdErr bool)
```
