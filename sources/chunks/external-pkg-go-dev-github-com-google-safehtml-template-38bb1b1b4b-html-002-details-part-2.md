---
source_name: "External Linked Documentation"
source_url: "https://pkg.go.dev/github.com/google/safehtml/template"
source_path: "sources/raw/external/pkg-go-dev-github-com-google-safehtml-template-38bb1b1b4b.html"
license_ref: ""
---

Even if X is a safehtml.URL or safehtml.TrustedResourceURL value, which remains unchanged after _sanitizeTrustedResourceURLOrURL, X will still be URL-normalized and HTML-escaped. Likewise, Y will still be HTML-escaped even if its string form is left unchanged by _sanitizeIdentifier.

#### Substitutions in URLs ¶

Values of any type may be substituted into attribute values in URL and TrustedResourceURL sanitization contexts only if the action is preceded by a safe URL prefix. For example, in

```go
<q cite="http://www.foo.com/{{ .PathComponent }}">foo</q>

```

Since "http://www.foo.com/ <http://www.foo.com/>" is a safe URL prefix, PathComponent can safely be interpolated into this URL sanitization context after URL normalization. Similarly, in

```go
<script src="https://www.bar.com/{{ .PathComponent }}"></script>

```

Since "https://www.bar.com/ <https://www.bar.com/>" is a safe TrustedResourceURL prefix, PathComponent can safely be interpolated into this TrustedResourceURL sanitization context after URL escaping. Substitutions after a safe TrustedResourceURL prefix are escaped instead of normalized to prevent the injection of any new URL components, including additional path components. URL escaping also takes place in URL sanitization contexts where the substitutions occur in the query or fragment part of the URL, such as in:

```go
<a href="/foo?q={{ .Query }}&hl={{ .LangCode }}">Link</a>

```

A URL prefix is considered safe in a URL sanitization context if it does not end in an incomplete HTML character reference (e.g. https&#1) or incomplete percent-encoding character triplet (e.g. /fo%6), does not contain whitespace or control characters, and one of the following is true:

- The prefix has a safe scheme (i.e. http, https, mailto, or ftp).
- The prefix has the data scheme with base64 encoding and an allowed audio, image, or video MIME type (e.g. data:img/jpeg;base64, data:video/mp4;base64).
- The prefix has no scheme at all, and cannot be interpreted as a scheme prefix (e.g. /path).

A URL prefix is considered safe in a TrustedResourceURL sanitization context if it does not end in an incomplete HTML character reference (e.g. https&#1) or incomplete percent-encoding character triplet (e.g. /fo%6), does not contain white space or control characters, and one of the following is true:

- The prefix has the https scheme and contains a domain name (e.g. https://www.foo.com <https://www.foo.com>).
- The prefix is scheme-relative and contains a domain name (e.g. //www.foo.com/).
- The prefix is path-absolute and contains a path (e.g. /path).
- The prefix is "about:blank".

```go

package main

import (
	"log"
	"os"

"github.com/google/safehtml/template"
)

func main() {
	const tpl = `
<!DOCTYPE html>
<html>
	<head>
		<meta charset="UTF-8">
		<title>{{.Title}}</title>
	</head>
	<body>
		{{range .Items}}<div>{{ . }}</div>{{else}}<div><strong>no rows</strong></div>{{end}}
	</body>
</html>`

check := func(err error) {
		if err != nil {
			log.Fatal(err)
		}
	}
	t, err := template.New("webpage").Parse(tpl)
	check(err)

data := struct {
		Title string
		Items []string
	}{
		Title: "My page",
		Items: []string{
			"My photos",
			"My blog",
		},
	}

err = t.Execute(os.Stdout, data)
	check(err)

noItems := struct {
		Title string
		Items []string
	}{
		Title: "My another page",
		Items: []string{},
	}

err = t.Execute(os.Stdout, noItems)
	check(err)

}

```

```go
Output:
<!DOCTYPE html>
<html>
	<head>
		<meta charset="UTF-8">
		<title>My page</title>
	</head>
	<body>
		<div>My photos</div><div>My blog</div>
	</body>
</html>
<!DOCTYPE html>
<html>
	<head>
		<meta charset="UTF-8">
		<title>My another page</title>
	</head>
	<body>
		<div><strong>no rows</strong></div>
	</body>
</html>

```

Share Format Run

```go

package main

import (
	"log"
	"os"

"github.com/google/safehtml/template"
)

func main() {
	t := template.Must(template.New("foo").Parse(`<a href="{{ .X }}">{{ .Y }}</a>`))
	renderHTML := func(x, y string) {
		if err := t.Execute(os.Stdout, struct{ X, Y string }{x, y}); err != nil {
			log.Fatal(err)
		}
	}
	renderHTML("javascript:evil()", "</a><script>alert('pwned')</script><a>")
}

```

```go
Output:
<a href="about:invalid#zGoSafez">&lt;/a&gt;&lt;script&gt;alert(&#39;pwned&#39;)&lt;/script&gt;&lt;a&gt;</a>

```

Share Format Run

Using safehtml.Script to safely inject script content

```go

package main

import (
	"os"

"github.com/google/safehtml"
	"github.com/google/safehtml/template"
)

type MyPageData struct {
	Message string
	Script  safehtml.Script
}

var tmplMyPage = template.Must(template.New("myPage").Parse(
	`<strong>{{.Message}}</strong>` +
		// include scripts for page render
		`<script>{{.Script}}</script>`,
))

// Using safehtml.Script to safely inject script content
func main() {
	err := tmplMyPage.Execute(os.Stdout, MyPageData{
		Message: "welcome to my cool website!!",
		Script:  safehtml.ScriptFromConstant(`alert("hello world!")`),
	})

if err != nil {
		panic(err)
	}

}

```

```go
Output:
<strong>welcome to my cool website!!</strong><script>alert("hello world!")</script>

```

Share Format Run

-  func IsTrue(val interface{}) (truth, ok bool)
-  func MustParseAndExecuteToHTML(text stringConstant) safehtml.HTML
-  type Error
-
-  func (e *Error) Error() string

-  type ErrorCode
-  type FuncMap
-  type Template
-
-  func Must(t *Template, err error) *Template
-  func New(name string) *Template
-  func ParseFS(tfs TrustedFS, patterns ...string) (*Template, error)
-  func ParseFiles(filenames ...stringConstant) (*Template, error)
-  func ParseFilesFromTrustedSources(filenames ...TrustedSource) (*Template, error)
-  func ParseGlob(pattern stringConstant) (*Template, error)
-  func ParseGlobFromTrustedSource(pattern TrustedSource) (*Template, error)

-
-  func (t *Template) CSPCompatible() *Template
-  func (t *Template) Clone() (*Template, error)
-  func (t *Template) DefinedTemplates() string
-  func (t *Template) Delims(left, right string) *Template
-  func (t *Template) Execute(wr io.Writer, data interface{}) error
-  func (t *Template) ExecuteTemplate(wr io.Writer, name string, data interface{}) error
-  func (t *Template) ExecuteTemplateToHTML(name string, data interface{}) (safehtml.HTML, error)
-  func (t *Template) ExecuteToHTML(data interface{}) (safehtml.HTML, error)
-  func (t *Template) Funcs(funcMap FuncMap) *Template
-  func (t *Template) Lookup(name string) *Template
-  func (t *Template) Name() string
-  func (t *Template) New(name string) *Template
-  func (t *Template) Option(opt ...string) *Template
-  func (t *Template) Parse(text stringConstant) (*Template, error)
-  func (t *Template) ParseFS(tfs TrustedFS, patterns ...string) (*Template, error)
-  func (t *Template) ParseFiles(filenames ...stringConstant) (*Template, error)
-  func (t *Template) ParseFilesFromTrustedSources(filenames ...TrustedSource) (*Template, error)
-  func (t *Template) ParseFromTrustedTemplate(tmpl TrustedTemplate) (*Template, error)
-  func (t *Template) ParseGlob(pattern stringConstant) (*Template, error)
-  func (t *Template) ParseGlobFromTrustedSource(pattern TrustedSource) (*Template, error)
-  func (t *Template) Templates() []*Template

-  type TrustedFS
-
-  func TrustedFSFromEmbed(fsys embed.FS) TrustedFS
-  func TrustedFSFromTrustedSource(ts TrustedSource) TrustedFS

-
-  func (tf TrustedFS) Sub(dir TrustedSource) (TrustedFS, error)

-  type TrustedSource
-
-  func TrustedSourceFromConstant(src stringConstant) TrustedSource
-  func TrustedSourceFromConstantDir(dir stringConstant, src TrustedSource, filename string) (TrustedSource, error)
-  func TrustedSourceFromEnvVar(key stringConstant) TrustedSource
-  func TrustedSourceFromFlag(value flag.Value) TrustedSource
-  func TrustedSourceJoin(elem ...TrustedSource) TrustedSource

-
-  func (t TrustedSource) String() string

-  type TrustedTemplate
-
-  func MakeTrustedTemplate(tmpl stringConstant) TrustedTemplate

-
-  func (t TrustedTemplate) String() string

- Package
- Package (Autosanitization)
- Package (Script)
- Template (Block)
- Template (Glob)
- Template (Helpers)
- Template (Parsefiles)
- Template (Share)

This section is empty.

This section is empty.

```go
func IsTrue(val interface{}) (truth, ok bool)
```

IsTrue reports whether the value is 'true', in the sense of not the zero of its type, and whether the value has a meaningful truth value. This is the definition of truth used by if and other such actions.

```go
func MustParseAndExecuteToHTML(text stringConstant) safehtml.HTML
```

MustParseAndExecuteToHTML is a helper that returns the safehtml.HTML value produced by parsing text as a template body and executing it with no data. Any errors encountered parsing or executing the template are fatal. This function is intended to produce safehtml.HTML values from static HTML snippets such as

```go
html := MustParseAndExecuteToHTML("<b>Important</b>")

```

To guarantee that the template body is never controlled by an attacker, text must be an untyped string constant, which is always under programmer control.

```go
type Error struct {
	// ErrorCode describes the kind of error.
	ErrorCode ErrorCode
	// Node is the node that caused the problem, if known.
	// If not nil, it overrides Name and Line.
	Node parse.Node
	// Name is the name of the template in which the error was encountered.
	Name string
	// Line is the line number of the error in the template source or 0.
	Line int
	// Description is a human-readable description of the problem.
	Description string
}
```

Error describes a problem encountered during template Escaping.

```go
func (e *Error) Error() string
```

```go
type ErrorCode int
```

ErrorCode is a code for a kind of error.

```go
const (
	// OK indicates the lack of an error.
	OK ErrorCode = iota

// ErrAmbigContext: "... appears in an ambiguous context within a URL"
	// Example:
	//   <a href="
	//      {{if .C}}
	//        /path/
	//      {{else}}
	//        /search?q=
	//      {{end}}
	//      {{.X}}
	//   ">
	// Discussion:
	//   {{.X}} is in an ambiguous URL context since, depending on {{.C}},
	//  it may be either a URL suffix or a query parameter.
	//   Moving {{.X}} into the condition removes the ambiguity:
	//   <a href="{{if .C}}/path/{{.X}}{{else}}/search?q={{.X}}">
	ErrAmbigContext

// ErrBadHTML: "expected space, attr name, or end of tag, but got ...",
	//   "... in unquoted attr", "... in attribute name"
	// Example:
	//   <a href = /search?q=foo>
	//   <href=foo>
	//   <form na<e=...>
	//   <option selected<
	// Discussion:
	//   This is often due to a typo in an HTML element, but some runes
	//   are banned in tag names, attribute names, and unquoted attribute
	//   values because they can tickle parser ambiguities.
	//   Quoting all attributes is the best policy.
	ErrBadHTML

// ErrBranchEnd: "{{if}} branches end in different contexts"
	// Example:
	//   {{if .C}}<a href="{{end}}{{.X}}
	// Discussion:
	//   Package html/template statically examines each path through an
	//   {{if}}, {{range}}, or {{with}} to escape any following pipelines.
	//   The example is ambiguous since {{.X}} might be an HTML text node,
	//   or a URL prefix in an HTML attribute. The context of {{.X}} is
	//   used to figure out how to escape it, but that context depends on
	//   the run-time value of {{.C}} which is not statically known.
	//
	//   The problem is usually something like missing quotes or angle
	//   brackets, or can be avoided by refactoring to put the two contexts
	//   into different branches of an if, range or with. If the problem
	//   is in a {{range}} over a collection that should never be empty,
	//   adding a dummy {{else}} can help.
	ErrBranchEnd
