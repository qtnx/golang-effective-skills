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

## Repository
   github.com/spf13/cobra  <https://github.com/spf13/cobra>

## Links

-    Open Source Insights  <https://deps.dev/go/github.com%2Fspf13%2Fcobra/v1.10.2>
-    Code Wiki

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

## Commands

Command is the central point of the application. Each interaction that the application supports will be contained in a Command. A command can have children commands and optionally run an action.

In the example above, 'server' is the command.

More about cobra.Command <https://pkg.go.dev/github.com/spf13/cobra#Command>

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

##   Directories ¶
    Show internal   Expand all

      doc

  Click to show internal directories.
  Click to hide internal directories.

  Close

     **?** : This menu   **/** : Search site   **f** or **F** : Jump to   **y** or **Y**  : Canonical URL
  Close
