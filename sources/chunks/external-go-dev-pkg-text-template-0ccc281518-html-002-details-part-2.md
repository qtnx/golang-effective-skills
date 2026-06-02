---
source_name: "External Linked Documentation"
source_url: "https://go.dev/pkg/text/template/"
source_path: "sources/raw/external/go-dev-pkg-text-template-0ccc281518.html"
license_ref: ""
---

```go
Argument
	The result is the value of evaluating the argument.
.Method [Argument...]
	The method can be alone or the last element of a chain but,
	unlike methods in the middle of a chain, it can take arguments.
	The result is the value of calling the method with the
	arguments:
		dot.Method(Argument1, etc.)
functionName [Argument...]
	The result is the value of calling the function associated
	with the name:
		function(Argument1, etc.)
	Functions and function names are described below.

```

A pipeline may be "chained" by separating a sequence of commands with pipeline characters '|'. In a chained pipeline, the result of each command is passed as the last argument of the following command. The output of the final command in the pipeline is the value of the pipeline.

The output of a command will be either one value or two values, the second of which has type error. If that second value is present and evaluates to non-nil, execution terminates and the error is returned to the caller of Execute.

#### Variables ¶

A pipeline inside an action may initialize a variable to capture the result. The initialization has syntax

```go
$variable := pipeline

```

where $variable is the name of the variable. An action that declares a variable produces no output.

Variables previously declared can also be assigned, using the syntax

```go
$variable = pipeline

```

If a "range" action initializes a variable, the variable is set to the successive elements of the iteration. Also, a "range" may declare two variables, separated by a comma:

```go
range $index, $element := pipeline

```

in which case $index and $element are set to the successive values of the array/slice index or map key and element, respectively. Note that if there is only one variable, it is assigned the element; this is opposite to the convention in Go range clauses.

A variable's scope extends to the "end" action of the control structure ("if", "with", or "range") in which it is declared, or to the end of the template if there is no such control structure. A template invocation does not inherit variables from the point of its invocation.

When execution begins, $ is set to the data argument passed to Execute, that is, to the starting value of dot.

#### Examples ¶

Here are some example one-line templates demonstrating pipelines and variables. All produce the quoted word "output":

```go
{{"\"output\""}}
	A string constant.
{{`"output"`}}
	A raw string constant.
{{printf "%q" "output"}}
	A function call.
{{"output" | printf "%q"}}
	A function call whose final argument comes from the previous
	command.
{{printf "%q" (print "out" "put")}}
	A parenthesized argument.
{{"put" | printf "%s%s" "out" | printf "%q"}}
	A more elaborate call.
{{"output" | printf "%s" | printf "%q"}}
	A longer chain.
{{with "output"}}{{printf "%q" .}}{{end}}
	A with action using dot.
{{with $x := "output" | printf "%q"}}{{$x}}{{end}}
	A with action that creates and uses a variable.
{{with $x := "output"}}{{printf "%q" $x}}{{end}}
	A with action that uses the variable in another action.
{{with $x := "output"}}{{$x | printf "%q"}}{{end}}
	The same, but pipelined.

```

#### Functions ¶

During execution functions are found in two function maps: first in the template, then in the global function map. By default, no functions are defined in the template but the Funcs method can be used to add them.

Predefined global functions are named as follows.

```go
and
	Returns the boolean AND of its arguments by returning the
	first empty argument or the last argument. That is,
	"and x y" behaves as "if x then y else x."
	Evaluation proceeds through the arguments left to right
	and returns when the result is determined.
call
	Returns the result of calling the first argument, which
	must be a function, with the remaining arguments as parameters.
	Thus "call .X.Y 1 2" is, in Go notation, dot.X.Y(1, 2) where
	Y is a func-valued field, map entry, or the like.
	The first argument must be the result of an evaluation
	that yields a value of function type (as distinct from
	a predefined function such as print). The function must
	return either one or two result values, the second of which
	is of type error. If the arguments don't match the function
	or the returned error value is non-nil, execution stops.
html
	Returns the escaped HTML equivalent of the textual
	representation of its arguments. This function is unavailable
	in html/template, with a few exceptions.
index
	Returns the result of indexing its first argument by the
	following arguments. Thus "index x 1 2 3" is, in Go syntax,
	x[1][2][3]. Each indexed item must be a map, slice, or array.
slice
	slice returns the result of slicing its first argument by the
	remaining arguments. Thus "slice x 1 2" is, in Go syntax, x[1:2],
	while "slice x" is x[:], "slice x 1" is x[1:], and "slice x 1 2 3"
	is x[1:2:3]. The first argument must be a string, slice, or array.
js
	Returns the escaped JavaScript equivalent of the textual
	representation of its arguments.
len
	Returns the integer length of its argument.
not
	Returns the boolean negation of its single argument.
or
	Returns the boolean OR of its arguments by returning the
	first non-empty argument or the last argument, that is,
	"or x y" behaves as "if x then x else y".
	Evaluation proceeds through the arguments left to right
	and returns when the result is determined.
print
	An alias for fmt.Sprint
printf
	An alias for fmt.Sprintf
println
	An alias for fmt.Sprintln
urlquery
	Returns the escaped value of the textual representation of
	its arguments in a form suitable for embedding in a URL query.
	This function is unavailable in html/template, with a few
	exceptions.

```

The boolean functions take any zero value to be false and a non-zero value to be true.

There is also a set of binary comparison operators defined as functions:

```go
eq
	Returns the boolean truth of arg1 == arg2
ne
	Returns the boolean truth of arg1 != arg2
lt
	Returns the boolean truth of arg1 < arg2
le
	Returns the boolean truth of arg1 <= arg2
gt
	Returns the boolean truth of arg1 > arg2
ge
	Returns the boolean truth of arg1 >= arg2

```

For simpler multi-way equality tests, eq (only) accepts two or more arguments and compares the second and subsequent to the first, returning in effect

```go
arg1==arg2 || arg1==arg3 || arg1==arg4 ...

```

(Unlike with || in Go, however, eq is a function call and all the arguments will be evaluated.)

The comparison functions work on any values whose type Go defines as comparable. For basic types such as integers, the rules are relaxed: size and exact type are ignored, so any integer value, signed or unsigned, may be compared with any other integer value. (The arithmetic value is compared, not the bit pattern, so all negative integers are less than all unsigned integers.) However, as usual, one may not compare an int with a float32 and so on.

#### Associated templates ¶

Each template is named by a string specified when it is created. Also, each template is associated with zero or more other templates that it may invoke by name; such associations are transitive and form a name space of templates.

A template may use a template invocation to instantiate another associated template; see the explanation of the "template" action above. The name must be that of a template associated with the template that contains the invocation.

#### Nested template definitions ¶

When parsing a template, another template may be defined and associated with the template being parsed. Template definitions must appear at the top level of the template, much like global variables in a Go program.

The syntax of such definitions is to surround each template declaration with a "define" and "end" action.

The define action names the template being created by providing a string constant. Here is a simple example:

```go
{{define "T1"}}ONE{{end}}
{{define "T2"}}TWO{{end}}
{{define "T3"}}{{template "T1"}} {{template "T2"}}{{end}}
{{template "T3"}}

```

This defines two templates, T1 and T2, and a third T3 that invokes the other two when it is executed. Finally it invokes T3. If executed this template will produce the text

```go
ONE TWO

```

By construction, a template may reside in only one association. If it's necessary to have a template addressable from multiple associations, the template definition must be parsed multiple times to create distinct *Template values, or must be copied with Template.Clone or Template.AddParseTree.

Parse may be called multiple times to assemble the various associated templates; see ParseFiles, ParseGlob, Template.ParseFiles and Template.ParseGlob for simple ways to parse related templates stored in files.

A template may be executed directly or through Template.ExecuteTemplate, which executes an associated template identified by name. To invoke our example above, we might write,

```go
err := tmpl.Execute(os.Stdout, "no data needed")
if err != nil {
	log.Fatalf("execution failed: %s", err)
}

```

or to invoke a particular template explicitly by name,

```go
err := tmpl.ExecuteTemplate(os.Stdout, "T2", "no data needed")
if err != nil {
	log.Fatalf("execution failed: %s", err)
}

```

-  func HTMLEscape(w io.Writer, b []byte)
-  func HTMLEscapeString(s string) string
-  func HTMLEscaper(args ...any) string
-  func IsTrue(val any) (truth, ok bool)
-  func JSEscape(w io.Writer, b []byte)
-  func JSEscapeString(s string) string
-  func JSEscaper(args ...any) string
-  func URLQueryEscaper(args ...any) string
-  type ExecError
-
-  func (e ExecError) Error() string
-  func (e ExecError) Unwrap() error

-  type FuncMap
-  type Template
-
-  func Must(t *Template, err error) *Template
-  func New(name string) *Template
-  func ParseFS(fsys fs.FS, patterns ...string) (*Template, error)
-  func ParseFiles(filenames ...string) (*Template, error)
-  func ParseGlob(pattern string) (*Template, error)
