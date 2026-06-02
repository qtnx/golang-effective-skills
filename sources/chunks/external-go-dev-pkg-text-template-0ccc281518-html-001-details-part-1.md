---
source_name: "External Linked Documentation"
source_url: "https://go.dev/pkg/text/template/"
source_path: "sources/raw/external/go-dev-pkg-text-template-0ccc281518.html"
license_ref: ""
---

template package - text/template - Go Packages
## Details

-     Valid go.mod <https://cs.opensource.google/go/go/+/go1.26.3:src/go.mod> file
 The Go module system was introduced in Go 1.11 and is the official dependency management solution for Go.

-     Redistributable license
 Redistributable licenses place minimal restrictions on how software can be used, modified, and redistributed.

-     Tagged version
Modules with tagged versions give importers more predictable builds.

-     Stable version
When a project reaches major version v1 it is considered stable.

-  Learn more about best practices

## Repository
   cs.opensource.google/go/go  <https://cs.opensource.google/go/go>

##   Documentation ¶

Package template implements data-driven templates for generating textual output.

To generate HTML output, see html/template, which has the same interface as this package but automatically secures HTML output against certain attacks.

Templates are executed by applying them to a data structure. Annotations in the template refer to elements of the data structure (typically a field of a struct or a key in a map) to control execution and derive values to be displayed. Execution of the template walks the structure and sets the cursor, represented by a period '.' and called "dot", to the value at the current location in the structure as execution proceeds.

The security model used by this package assumes that template authors are trusted. The package does not auto-escape output, so injecting code into a template can lead to arbitrary code execution if the template is executed by an untrusted source.

The input text for a template is UTF-8-encoded text in any format. "Actions"--data evaluations or control structures--are delimited by "{{" and "}}"; all text outside actions is copied to the output unchanged.

Once parsed, a template may be executed safely in parallel, although if parallel executions share a Writer the output may be interleaved.

Here is a trivial example that prints "17 items are made of wool".

```go
type Inventory struct {
	Material string
	Count    uint
}
sweaters := Inventory{"wool", 17}
tmpl, err := template.New("test").Parse("{{.Count}} items are made of {{.Material}}")
if err != nil { panic(err) }
err = tmpl.Execute(os.Stdout, sweaters)
if err != nil { panic(err) }

```

More intricate examples appear below.

#### Text and spaces ¶

By default, all text between actions is copied verbatim when the template is executed. For example, the string " items are made of " in the example above appears on standard output when the program is run.

However, to aid in formatting template source code, if an action's left delimiter (by default "{{") is followed immediately by a minus sign and white space, all trailing white space is trimmed from the immediately preceding text. Similarly, if the right delimiter ("}}") is preceded by white space and a minus sign, all leading white space is trimmed from the immediately following text. In these trim markers, the white space must be present: "{{- 3}}" is like "{{3}}" but trims the immediately preceding text, while "{{-3}}" parses as an action containing the number -3.

For instance, when executing the template whose source is

```go
"{{23 -}} < {{- 45}}"

```

the generated output would be

```go
"23<45"

```

For this trimming, the definition of white space characters is the same as in Go: space, horizontal tab, carriage return, and newline.

#### Actions ¶

Here is the list of actions. "Arguments" and "pipelines" are evaluations of data, defined in detail in the corresponding sections that follow.

```go
{{/* a comment */}}
{{- /* a comment with white space trimmed from preceding and following text */ -}}
	A comment; discarded. May contain newlines.
	Comments do not nest and must start and end at the
	delimiters, as shown here.

{{pipeline}}
	The default textual representation (the same as would be
	printed by fmt.Print) of the value of the pipeline is copied
	to the output.

{{if pipeline}} T1 {{end}}
	If the value of the pipeline is empty, no output is generated;
	otherwise, T1 is executed. The empty values are false, 0, any
	nil pointer or interface value, and any array, slice, map, or
	string of length zero.
	Dot is unaffected.

{{if pipeline}} T1 {{else}} T0 {{end}}
	If the value of the pipeline is empty, T0 is executed;
	otherwise, T1 is executed. Dot is unaffected.

{{if pipeline}} T1 {{else if pipeline}} T0 {{end}}
	To simplify the appearance of if-else chains, the else action
	of an if may include another if directly; the effect is exactly
	the same as writing
		{{if pipeline}} T1 {{else}}{{if pipeline}} T0 {{end}}{{end}}

{{range pipeline}} T1 {{end}}
	The value of the pipeline must be an array, slice, map, iter.Seq,
	iter.Seq2, integer or channel.
	If the value of the pipeline has length zero, nothing is output;
	otherwise, dot is set to the successive elements of the array,
	slice, or map and T1 is executed. If the value is a map and the
	keys are of basic type with a defined order, the elements will be
	visited in sorted key order.

{{range pipeline}} T1 {{else}} T0 {{end}}
	The value of the pipeline must be an array, slice, map, iter.Seq,
	iter.Seq2, integer or channel.
	If the value of the pipeline has length zero, dot is unaffected and
	T0 is executed; otherwise, dot is set to the successive elements
	of the array, slice, or map and T1 is executed.

{{break}}
	The innermost {{range pipeline}} loop is ended early, stopping the
	current iteration and bypassing all remaining iterations.

{{continue}}
	The current iteration of the innermost {{range pipeline}} loop is
	stopped, and the loop starts the next iteration.

{{template "name"}}
	The template with the specified name is executed with nil data.

{{template "name" pipeline}}
	The template with the specified name is executed with dot set
	to the value of the pipeline.

{{block "name" pipeline}} T1 {{end}}
	A block is shorthand for defining a template
		{{define "name"}} T1 {{end}}
	and then executing it in place
		{{template "name" pipeline}}
	The typical use is to define a set of root templates that are
	then customized by redefining the block templates within.

{{with pipeline}} T1 {{end}}
	If the value of the pipeline is empty, no output is generated;
	otherwise, dot is set to the value of the pipeline and T1 is
	executed.

{{with pipeline}} T1 {{else}} T0 {{end}}
	If the value of the pipeline is empty, dot is unaffected and T0
	is executed; otherwise, dot is set to the value of the pipeline
	and T1 is executed.

{{with pipeline}} T1 {{else with pipeline}} T0 {{end}}
	To simplify the appearance of with-else chains, the else action
	of a with may include another with directly; the effect is exactly
	the same as writing
		{{with pipeline}} T1 {{else}}{{with pipeline}} T0 {{end}}{{end}}

```

#### Arguments ¶

An argument is a simple value, denoted by one of the following.

-
A boolean, string, character, integer, floating-point, imaginary or complex constant in Go syntax. These behave like Go's untyped constants. Note that, as in Go, whether a large integer constant overflows when assigned or passed to a function can depend on whether the host machine's ints are 32 or 64 bits.

-
The keyword nil, representing an untyped Go nil.

-
The character '.' (period):

.

The result is the value of dot.

-
A variable name, which is a (possibly empty) alphanumeric string preceded by a dollar sign, such as

$piOver2

or

$

The result is the value of the variable. Variables are described below.

-
The name of a field of the data, which must be a struct, preceded by a period, such as

.Field

The result is the value of the field. Field invocations may be chained:

.Field1.Field2

Fields can also be evaluated on variables, including chaining:

$x.Field1.Field2

-
The name of a key of the data, which must be a map, preceded by a period, such as

.Key

The result is the map element value indexed by the key. Key invocations may be chained and combined with fields to any depth:

.Field1.Key1.Field2.Key2

Although the key must be an alphanumeric identifier, unlike with field names they do not need to start with an upper case letter. Keys can also be evaluated on variables, including chaining:

$x.key1.key2

-
The name of a niladic method of the data, preceded by a period, such as

.Method

The result is the value of invoking the method with dot as the receiver, dot.Method(). Such a method must have one return value (of any type) or two return values, the second of which is an error. If it has two and the returned error is non-nil, execution terminates and an error is returned to the caller as the value of Execute. Method invocations may be chained and combined with fields and keys to any depth:

.Field1.Key1.Method1.Field2.Key2.Method2

Methods can also be evaluated on variables, including chaining:

$x.Method1.Field

-
The name of a niladic function, such as

fun

The result is the value of invoking the function, fun(). The return types and values behave as in methods. Functions and function names are described below.

-
A parenthesized instance of one the above, for grouping. The result may be accessed by a field or map key invocation.

print (.F1 arg1) (.F2 arg2) (.StructValuedMethod "arg").Field

Arguments may evaluate to any type; if they are pointers the implementation automatically indirects to the base type when required. If an evaluation yields a function value, such as a function-valued field of a struct, the function is not invoked automatically, but it can be used as a truth value for an if action and the like. To invoke it, use the call function, defined below.

#### Pipelines ¶

A pipeline is a possibly chained sequence of "commands". A command is a simple value (argument) or a function or method call, possibly with multiple arguments:
