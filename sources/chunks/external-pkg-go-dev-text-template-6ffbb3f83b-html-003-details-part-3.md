---
source_name: "External Linked Documentation"
source_url: "https://pkg.go.dev/text/template"
source_path: "sources/raw/external/pkg-go-dev-text-template-6ffbb3f83b.html"
license_ref: ""
---

-
-  func (t *Template) AddParseTree(name string, tree *parse.Tree) (*Template, error)
-  func (t *Template) Clone() (*Template, error)
-  func (t *Template) DefinedTemplates() string
-  func (t *Template) Delims(left, right string) *Template
-  func (t *Template) Execute(wr io.Writer, data any) error
-  func (t *Template) ExecuteTemplate(wr io.Writer, name string, data any) error
-  func (t *Template) Funcs(funcMap FuncMap) *Template
-  func (t *Template) Lookup(name string) *Template
-  func (t *Template) Name() string
-  func (t *Template) New(name string) *Template
-  func (t *Template) Option(opt ...string) *Template
-  func (t *Template) Parse(text string) (*Template, error)
-  func (t *Template) ParseFS(fsys fs.FS, patterns ...string) (*Template, error)
-  func (t *Template) ParseFiles(filenames ...string) (*Template, error)
-  func (t *Template) ParseGlob(pattern string) (*Template, error)
-  func (t *Template) Templates() []*Template

- Template
- Template (Block)
- Template (Func)
- Template (Funcs)
- Template (Glob)
- Template (Helpers)
- Template (If)
- Template (Share)

This section is empty.

This section is empty.

```go
func HTMLEscape(w io.Writer, b []byte)
```

HTMLEscape writes to w the escaped HTML equivalent of the plain text data b.

```go
func HTMLEscapeString(s string) string
```

HTMLEscapeString returns the escaped HTML equivalent of the plain text data s.

```go
func HTMLEscaper(args ...any) string
```

HTMLEscaper returns the escaped HTML equivalent of the textual representation of its arguments.

```go
func IsTrue(val any) (truth, ok bool)
```

IsTrue reports whether the value is 'true', in the sense of not the zero of its type, and whether the value has a meaningful truth value. This is the definition of truth used by if and other such actions.

```go
func JSEscape(w io.Writer, b []byte)
```

JSEscape writes to w the escaped JavaScript equivalent of the plain text data b.

```go
func JSEscapeString(s string) string
```

JSEscapeString returns the escaped JavaScript equivalent of the plain text data s.

```go
func JSEscaper(args ...any) string
```

JSEscaper returns the escaped JavaScript equivalent of the textual representation of its arguments.

```go
func URLQueryEscaper(args ...any) string
```

URLQueryEscaper returns the escaped value of the textual representation of its arguments in a form suitable for embedding in a URL query.

```go
type ExecError struct {
	Name string // Name of template.
	Err  error  // Pre-formatted error.
}
```

ExecError is the custom error type returned when Execute has an error evaluating its template. (If a write error occurs, the actual error is returned; it will not be of type ExecError.)

```go
func (e ExecError) Error() string
```

```go
func (e ExecError) Unwrap() error
```

```go
type FuncMap map[string]any
```

FuncMap is the type of the map defining the mapping from names to functions. Each function must have either a single return value, or two return values of which the second has type error. In that case, if the second (error) return value evaluates to non-nil during execution, execution terminates and Execute returns that error.

Errors returned by Execute wrap the underlying error; call errors.AsType to unwrap them.

When template execution invokes a function with an argument list, that list must be assignable to the function's parameter types. Functions meant to apply to arguments of arbitrary type can use parameters of type interface{} or of type reflect.Value. Similarly, functions meant to return a result of arbitrary type can return interface{} or reflect.Value.

```go
type Template struct {
	*parse.Tree
	// contains filtered or unexported fields
}
```

Template is the representation of a parsed template. The *parse.Tree field is exported only for use by html/template and should be treated as unexported by all other clients.

```go

package main

import (
	"log"
	"os"
	"text/template"
)

func main() {
	// Define a template.
	const letter = `
Dear {{.Name}},
{{if .Attended}}
It was a pleasure to see you at the wedding.
{{- else}}
It is a shame you couldn't make it to the wedding.
{{- end}}
{{with .Gift -}}
Thank you for the lovely {{.}}.
{{end}}
Best wishes,
Josie
`

// Prepare some data to insert into the template.
	type Recipient struct {
		Name, Gift string
		Attended   bool
	}
	var recipients = []Recipient{
		{"Aunt Mildred", "bone china tea set", true},
		{"Uncle John", "moleskin pants", false},
		{"Cousin Rodney", "", false},
	}

// Create a new template and parse the letter into it.
	t := template.Must(template.New("letter").Parse(letter))

// Execute the template for each recipient.
	for _, r := range recipients {
		err := t.Execute(os.Stdout, r)
		if err != nil {
			log.Println("executing template:", err)
		}
	}

}

```

```go
Output:
Dear Aunt Mildred,

It was a pleasure to see you at the wedding.
Thank you for the lovely bone china tea set.

Best wishes,
Josie

Dear Uncle John,

It is a shame you couldn't make it to the wedding.
Thank you for the lovely moleskin pants.

Best wishes,
Josie

Dear Cousin Rodney,

It is a shame you couldn't make it to the wedding.

Best wishes,
Josie

```

Share Format Run

```go

package main

import (
	"log"
	"os"
	"strings"
	"text/template"
)

func main() {
	const (
		master  = `Names:{{block "list" .}}{{"\n"}}{{range .}}{{println "-" .}}{{end}}{{end}}`
		overlay = `{{define "list"}} {{join . ", "}}{{end}} `
	)
	var (
		funcs     = template.FuncMap{"join": strings.Join}
		guardians = []string{"Gamora", "Groot", "Nebula", "Rocket", "Star-Lord"}
	)
	masterTmpl, err := template.New("master").Funcs(funcs).Parse(master)
	if err != nil {
		log.Fatal(err)
	}
	overlayTmpl, err := template.Must(masterTmpl.Clone()).Parse(overlay)
	if err != nil {
		log.Fatal(err)
	}
	if err := masterTmpl.Execute(os.Stdout, guardians); err != nil {
		log.Fatal(err)
	}
	if err := overlayTmpl.Execute(os.Stdout, guardians); err != nil {
		log.Fatal(err)
	}
}

```

```go
Output:
Names:
- Gamora
- Groot
- Nebula
- Rocket
- Star-Lord
Names: Gamora, Groot, Nebula, Rocket, Star-Lord

```

Share Format Run

This example demonstrates a custom function to process template text. It installs the strings.Title function and uses it to Make Title Text Look Good In Our Template's Output.

```go

package main

import (
	"log"
	"os"
	"strings"
	"text/template"
)

func main() {
	// First we create a FuncMap with which to register the function.
	funcMap := template.FuncMap{
		// The name "title" is what the function will be called in the template text.
		"title": strings.Title,
	}

// A simple template definition to test our function.
	// We print the input text several ways:
	// - the original
	// - title-cased
	// - title-cased and then printed with %q
	// - printed with %q and then title-cased.
	const templateText = `
Input: {{printf "%q" .}}
Output 0: {{title .}}
Output 1: {{title . | printf "%q"}}
Output 2: {{printf "%q" . | title}}
`

// Create a template, add the function map, and parse the text.
	tmpl, err := template.New("titleTest").Funcs(funcMap).Parse(templateText)
	if err != nil {
		log.Fatalf("parsing: %s", err)
	}

// Run the template to verify the output.
	err = tmpl.Execute(os.Stdout, "the go programming language")
	if err != nil {
		log.Fatalf("execution: %s", err)
	}

}

```

```go
Output:
Input: "the go programming language"
Output 0: The Go Programming Language
Output 1: "The Go Programming Language"
Output 2: "The Go Programming Language"

```

Share Format Run

This example demonstrates registering two custom template functions and how to overwite one of the functions after the template has been parsed. Overwriting can be used, for example, to alter the operation of cloned templates.

```go

package main

import (
	"log"
	"os"
	"strings"
	"text/template"
)

func main() {

// Define a simple template to test the functions.
	const tmpl = `{{ . | lower | repeat }}`

// Define the template funcMap with two functions.
	var funcMap = template.FuncMap{
		"lower":  strings.ToLower,
		"repeat": func(s string) string { return strings.Repeat(s, 2) },
	}

// Define a New template, add the funcMap using Funcs and then Parse
	// the template.
	parsedTmpl, err := template.New("t").Funcs(funcMap).Parse(tmpl)
	if err != nil {
		log.Fatal(err)
	}
	if err := parsedTmpl.Execute(os.Stdout, "ABC\n"); err != nil {
		log.Fatal(err)
	}

// [Funcs] must be called before a template is parsed to add
	// functions to the template. [Funcs] can also be used after a
	// template is parsed to overwrite template functions.
	//
	// Here the function identified by "repeat" is overwritten.
	parsedTmpl.Funcs(template.FuncMap{
		"repeat": func(s string) string { return strings.Repeat(s, 3) },
	})
	if err := parsedTmpl.Execute(os.Stdout, "DEF\n"); err != nil {
		log.Fatal(err)
	}
}

```

```go
Output:
abc
abc
def
def
def

```

Share Format Run

Here we demonstrate loading a set of templates from a directory.

```go

package main

import (
	"io"
	"log"
	"os"
	"path/filepath"
	"text/template"
)

// templateFile defines the contents of a template to be stored in a file, for testing.
type templateFile struct {
	name     string
	contents string
}

func createTestDir(files []templateFile) string {
	dir, err := os.MkdirTemp("", "template")
	if err != nil {
		log.Fatal(err)
	}
	for _, file := range files {
		f, err := os.Create(filepath.Join(dir, file.name))
		if err != nil {
			log.Fatal(err)
		}
		defer f.Close()
		_, err = io.WriteString(f, file.contents)
		if err != nil {
			log.Fatal(err)
		}
	}
	return dir
}

func main() {
	// Here we create a temporary directory and populate it with our sample
	// template definition files; usually the template files would already
	// exist in some location known to the program.
	dir := createTestDir([]templateFile{
		// T0.tmpl is a plain template file that just invokes T1.
		{"T0.tmpl", `T0 invokes T1: ({{template "T1"}})`},
		// T1.tmpl defines a template, T1 that invokes T2.
		{"T1.tmpl", `{{define "T1"}}T1 invokes T2: ({{template "T2"}}){{end}}`},
		// T2.tmpl defines a template T2.
		{"T2.tmpl", `{{define "T2"}}This is T2{{end}}`},
	})
	// Clean up after the test; another quirk of running as an example.
	defer os.RemoveAll(dir)

// pattern is the glob pattern used to find all the template files.
	pattern := filepath.Join(dir, "*.tmpl")

// Here starts the example proper.
	// T0.tmpl is the first name matched, so it becomes the starting template,
	// the value returned by ParseGlob.
	tmpl := template.Must(template.ParseGlob(pattern))
