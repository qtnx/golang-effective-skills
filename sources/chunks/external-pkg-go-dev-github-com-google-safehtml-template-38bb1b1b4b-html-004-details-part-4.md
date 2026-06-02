---
source_name: "External Linked Documentation"
source_url: "https://pkg.go.dev/github.com/google/safehtml/template"
source_path: "sources/raw/external/pkg-go-dev-github-com-google-safehtml-template-38bb1b1b4b.html"
license_ref: ""
---

func main() {
	// Here we load the helpers from two template files with the following contents:
	// 		testdata/helpers_t1.tmpl: `{{define "T1"}}T1 invokes T2: ({{template "T2"}}){{end}}`
	// 		testdata/helpers_t2.tmpl: `{{define "T2"}}This is T2{{end}}`
	// Note that ParseGlob only accepts an untyped string constant.
	templates := template.Must(template.ParseGlob("testdata/helpers_*.tmpl"))
	// Add one driver template to the bunch; we do this with an explicit template definition.
	_, err := templates.Parse("{{define `driver1`}}Driver 1 calls T1: ({{template `T1`}})\n{{end}}")
	if err != nil {
		log.Fatal("parsing driver1: ", err)
	}
	// Add another driver template.
	_, err = templates.Parse("{{define `driver2`}}Driver 2 calls T2: ({{template `T2`}})\n{{end}}")
	if err != nil {
		log.Fatal("parsing driver2: ", err)
	}
	// We load all the templates before execution. This package does not require
	// that behavior but html/template's escaping does, so it's a good habit.
	err = templates.ExecuteTemplate(os.Stdout, "driver1", nil)
	if err != nil {
		log.Fatalf("driver1 execution: %s", err)
	}
	err = templates.ExecuteTemplate(os.Stdout, "driver2", nil)
	if err != nil {
		log.Fatalf("driver2 execution: %s", err)
	}
}

```

```go
Output:
Driver 1 calls T1: (T1 invokes T2: (This is T2))
Driver 2 calls T2: (This is T2)

```

Share Format Run

Here we demonstrate loading a set of templates from files in different directories

```go

package main

import (
	"log"
	"os"

"github.com/google/safehtml/template"
)

func main() {
	// Here we load two template files from different directories with the following contents:
	// 		testdata/dir1/parsefiles_t1.tmpl: `T1 invokes T2: ({{template "T2"}})`
	// 		testdata/dir2/parsefiles_t2.tmpl: `{{define "T2"}}This is T2{{end}}`
	// Note that ParseFiles only accepts an untyped string constants.
	tmpl := template.Must(template.ParseFiles("testdata/dir1/parsefiles_t1.tmpl", "testdata/dir2/parsefiles_t2.tmpl"))

err := tmpl.Execute(os.Stdout, nil)
	if err != nil {
		log.Fatalf("template execution: %s", err)
	}
}

```

```go
Output:
T1 invokes T2: (This is T2)

```

Share Format Run

This example demonstrates how to use one group of driver templates with distinct sets of helper templates.

```go

package main

import (
	"log"
	"os"

"github.com/google/safehtml/template"
)

func main() {
	// Here we load the helpers from two template files with the following contents:
	// 		testdata/share_t0.tmpl: "T0 ({{.}} version) invokes T1: ({{template `T1`}})\n"
	// 		testdata/share_t1.tmpl: `{{define "T1"}}T1 invokes T2: ({{template "T2"}}){{end}}`
	// Note that ParseGlob only accepts an untyped string constant.
	drivers := template.Must(template.ParseGlob("testdata/share_*.tmpl"))

// We must define an implementation of the T2 template. First we clone
	// the drivers, then add a definition of T2 to the template name space.

// 1. Clone the helper set to create a new name space from which to run them.
	first, err := drivers.Clone()
	if err != nil {
		log.Fatal("cloning helpers: ", err)
	}
	// 2. Define T2, version A, and parse it.
	_, err = first.Parse("{{define `T2`}}T2, version A{{end}}")
	if err != nil {
		log.Fatal("parsing T2: ", err)
	}

// Now repeat the whole thing, using a different version of T2.
	// 1. Clone the drivers.
	second, err := drivers.Clone()
	if err != nil {
		log.Fatal("cloning drivers: ", err)
	}
	// 2. Define T2, version B, and parse it.
	_, err = second.Parse("{{define `T2`}}T2, version B{{end}}")
	if err != nil {
		log.Fatal("parsing T2: ", err)
	}

// Execute the templates in the reverse order to verify the
	// first is unaffected by the second.
	err = second.ExecuteTemplate(os.Stdout, "share_t0.tmpl", "second")
	if err != nil {
		log.Fatalf("second execution: %s", err)
	}
	err = first.ExecuteTemplate(os.Stdout, "share_t0.tmpl", "first")
	if err != nil {
		log.Fatalf("first: execution: %s", err)
	}

}

```

```go
Output:
T0 (second version) invokes T1: (T1 invokes T2: (T2, version B))
T0 (first version) invokes T1: (T1 invokes T2: (T2, version A))

```

Share Format Run

```go
func Must(t *Template, err error) *Template
```

Must is a helper that wraps a call to a function returning (*Template, error) and panics if the error is non-nil. It is intended for use in variable initializations such as

```go
var t = template.Must(template.New("name").Parse("html"))

```

```go
func New(name string) *Template
```

New allocates a new HTML template with the given name.

```go
func ParseFS(tfs TrustedFS, patterns ...string) (*Template, error)
```

ParseFS is like ParseFiles or ParseGlob but reads from the TrustedFS instead of the host operating system's file system. It accepts a list of glob patterns. (Note that most file names serve as glob patterns matching only themselves.)

The same behaviors listed for ParseFiles() apply to ParseFS too (e.g. using the base name of the file as the template name).

```go
func ParseFiles(filenames ...stringConstant) (*Template, error)
```

ParseFiles creates a new Template and parses the template definitions from the named files. The returned template's name will have the (base) name and (parsed) contents of the first file. There must be at least one file. If an error occurs, parsing stops and the returned *Template is nil.

When parsing multiple files with the same name in different directories, the last one mentioned will be the one that results. For instance, ParseFiles("a/foo", "b/foo") stores "b/foo" as the template named "foo", while "a/foo" is unavailable.

To guarantee that filepaths, and thus template bodies, are never controlled by an attacker, filenames must be untyped string constants, which are always under programmer control.

```go
func ParseFilesFromTrustedSources(filenames ...TrustedSource) (*Template, error)
```

ParseFilesFromTrustedSources creates a new Template and parses the template definitions from the named files. The returned template's name will have the (base) name and (parsed) contents of the first file. There must be at least one file. If an error occurs, parsing stops and the returned *Template is nil.

When parsing multiple files with the same name in different directories, the last one mentioned will be the one that results. For instance, ParseFiles("a/foo", "b/foo") stores "b/foo" as the template named "foo", while "a/foo" is unavailable.

To guarantee that filepaths, and thus template bodies, are never controlled by an attacker, filenames must be trusted sources, which are always under programmer or application control.

```go
func ParseGlob(pattern stringConstant) (*Template, error)
```

ParseGlob creates a new Template and parses the template definitions from the files identified by the pattern, which must match at least one file. The returned template will have the (base) name and (parsed) contents of the first file matched by the pattern. ParseGlob is equivalent to calling ParseFiles with the list of files matched by the pattern.

To guarantee that the pattern, and thus the template bodies, is never controlled by an attacker, pattern must be an untyped string constant, which is always under programmer control.

```go
func ParseGlobFromTrustedSource(pattern TrustedSource) (*Template, error)
```

ParseGlobFromTrustedSource creates a new Template and parses the template definitions from the files identified by the pattern, which must match at least one file. The returned template will have the (base) name and (parsed) contents of the first file matched by the pattern. ParseGlobFromTrustedSource is equivalent to calling ParseFilesFromTrustedSources with the list of files matched by the pattern.

To guarantee that the pattern, and thus the template bodies, is never controlled by an attacker, pattern must be a trusted source, which is always under programmer or application control.

```go
func (t *Template) CSPCompatible() *Template
```

CSPCompatible causes this template to check template text for Content Security Policy (CSP) compatibility. The template will return errors at execution time if inline event handler attribute names or javascript: URIs are found in template text.

For example, the following templates will cause errors:

```go
<span onclick="doThings();">A thing.</span> // inline event handler "onclick"
<a href="javascript:linkClicked()">foo</a>  // javascript: URI present

```

```go
func (t *Template) Clone() (*Template, error)
```

Clone returns a duplicate of the template, including all associated templates. The actual representation is not copied, but the name space of associated templates is, so further calls to Parse in the copy will add templates to the copy but not to the original. Clone can be used to prepare common templates and use them with variant definitions for other templates by adding the variants after the clone is made.

It returns an error if t has already been executed.

```go
func (t *Template) DefinedTemplates() string
```

DefinedTemplates returns a string listing the defined templates, prefixed by the string "; defined templates are: ". If there are none, it returns the empty string. Used to generate an error message.

```go
func (t *Template) Delims(left, right string) *Template
```

Delims sets the action delimiters to the specified strings, to be used in subsequent calls to Parse, ParseFiles, or ParseGlob. Nested template definitions will inherit the settings. An empty delimiter stands for the corresponding default: {{ or }}. The return value is the template, so calls can be chained.

```go
func (t *Template) Execute(wr io.Writer, data interface{}) error
```

Execute applies a parsed template to the specified data object, writing the output to wr. If an error occurs executing the template or writing its output, execution stops, but partial results may already have been written to the output writer. A template may be executed safely in parallel, although if parallel executions share a Writer the output may be interleaved.

```go
func (t *Template) ExecuteTemplate(wr io.Writer, name string, data interface{}) error
```

ExecuteTemplate applies the template associated with t that has the given name to the specified data object and writes the output to wr. If an error occurs executing the template or writing its output, execution stops, but partial results may already have been written to the output writer. A template may be executed safely in parallel, although if parallel executions share a Writer the output may be interleaved.

```go
func (t *Template) ExecuteTemplateToHTML(name string, data interface{}) (safehtml.HTML, error)
```

ExecuteTemplateToHTML applies the template associated with t that has the given name to the specified data object and returns the output as a safehtml.HTML value. A template may be executed safely in parallel.

```go
func (t *Template) ExecuteToHTML(data interface{}) (safehtml.HTML, error)
```
