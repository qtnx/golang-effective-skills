template package - github.com/google/safehtml/template - Go Packages

## Details

-     Valid go.mod <https://github.com/google/safehtml/tree/v0.1.0/go.mod> file
 The Go module system was introduced in Go 1.11 and is the official dependency management solution for Go.

-     Redistributable license
 Redistributable licenses place minimal restrictions on how software can be used, modified, and redistributed.

-     Tagged version
Modules with tagged versions give importers more predictable builds.

-     Stable version
When a project reaches major version v1 it is considered stable.

-  Learn more about best practices

## Repository
   github.com/google/safehtml  <https://github.com/google/safehtml>

## Links

-    Open Source Insights  <https://deps.dev/go/github.com%2Fgoogle%2Fsafehtml/v0.1.0>

##   Documentation ¶

Package template (safehtml/template) implements data-driven templates for generating HTML output safe against code injection. It provides an interface similar to that of package html/template, but produces HTML output that is more secure. Therefore, it should be used instead of html/template to render HTML.

The documentation here focuses on the security features of the package. For information about how to program the templates themselves, see the documentation for text/template.

#### Basic usage ¶

This package provides an API almost identical to that of text/template and html/template to parse and execute HTML templates safely.

```go
tmpl := template.Must(template.New("name").Parse(`<div>Hello {{.}}</div>`))
err := tmpl.Execute(out, data)

```

If successful, out will contain code-injection-safe HTML. Otherwise, err's string representation will describe the error that occurred.

Elements of data might be modified at run time before being included in out, or rejected completely if such a conversion is not possible. Pass values of appropriate types from package safehtml to ensure that they are included in the template's HTML output in their expected form. More details are provided below in "Contextual autosanitization" and "Sanitization contexts".

#### Security improvements ¶

safehtml/template produces HTML more resistant to code injection than html/template because it:

- Allows values of types only from package safehtml to bypass run-time sanitization. These types represent values that are known---by construction or by run-time sanitization---to be safe for use in various HTML contexts without being processed by certain sanitization functions.
- Does not attempt to escape CSS or JavaScript. Instead of attempting to parse and escape these complex languages, safehtml/template allows values of only the appropriate types from package safehtml (e.g. safehtml.Style, safehtml.Script) to be used in these contexts, since they are already guaranteed to be safe.
- Emits an error if user data is interpolated in unsafe contexts, such as within disallowed elements or unquoted attribute values.
- Only loads templates from trusted sources. This ensures that the contents of the template are always under programmer control. More details are provided below in "Trusted template sources".
- Differentiates between URLs that load code and those that do not. URLs in the former category must be supplied to the template as values of type safehtml.TrustedResourceURL, whose type contract promises that the URL identifies a trustworthy resource. URLs in the latter category can be sanitized at run time.

#### Threat model ¶

safehtml/template assumes that programmers are trustworthy. Therefore, data fully under programmer control, such as string literals, are considered safe. The types from package safehtml are designed around this same assumption, so their type contracts are trusted by this package.

safehtml/template considers all other data values untrustworthy and conservatively assumes that such values could result in a code-injection vulnerability if included verbatim in HTML.

#### Trusted template sources ¶

safehtml/template loads templates only from trusted sources. Therefore, template text, file paths, and file patterns passed to Parse* functions and methods must be entirely under programmer control.

This constraint is enforced by using unexported string types for the parameters of Parse* functions and methods, such as trustedFilePattern for ParseGlob. The only values that may be assigned to these types (and thus provided as arguments) are untyped string constants such as string literals, which are always under programmer control.

#### Contextual autosanitization ¶

Code injection vulnerabilities, such as cross-site scripting (XSS), occur when untrusted data values are embedded in a HTML document. For example,

```go
import "text/template"
...
var t = template.Must(template.New("foo").Parse(`<a href="{{ .X }}">{{ .Y }}</a>`))
func renderHTML(x, y string) string {
  var out bytes.Buffer
  err := t.Execute(&out, struct{ X, Y string }{x, y})
  // Error checking elided
  return out.String()
}

```

If x and y originate from user-provided data, an attacker who controls these strings could arrange for them to contain the following values:

```go
x = "javascript:evil()"
y = "</a><script>alert('pwned')</script><a>"

```

which will cause renderHTML to return the following unsafe HTML:

```go
<a href="javascript:evil()"></a><script>alert('pwned')</script><a></a>

```

To prevent such vulnerabilities, untrusted data must be sanitized before being included in HTML. A sanitization function takes untrusted data and returns a string that will not create a code-injection vulnerability in the destination context. The function might return the input unchanged if it deems it safe, escape special runes in the input's string representation to prevent them from triggering undesired state changes in the HTML parser, or entirely replace the input by an innocuous string (also known as "filtering"). If none of these conversions are possible, the sanitization function aborts template processing.

safehtml/template contextually autosanitizes untrusted data by adding appropriate sanitization functions to template actions to ensure that the action output is safe to include in the HTML context in which the action appears. For example, in

```go
import "safehtml/template"
...
var t = template.Must(template.New("foo").Parse(`<a href="{{ .X }}">{{ .Y }}</a>`))
func renderHTML(x, y string) string {
  var out bytes.Buffer
  err := t.Execute(&out, struct{ X, Y string }{x, y})
  // Error checking elided
  return out.String()
}

```

the contextual autosanitizer rewrites the template to

```go
<a href="{{ .X | _sanitizeTrustedResourceURLOrURL | _sanitizeHTML }}">{{ .Y | _sanitizeHTML }}</a>

```

so that the template produces the following safe, sanitized HTML output (split across multiple lines for clarity):

```go
<a href="about:invalid#zGoSafez">
&lt;/a&gt;&lt;script&gt;alert(&#39;pwned&#39;)&lt;/script&gt;&lt;a&gt;
</a>

```

Similar template systems such as html/template, Soy, and Angular, refer to this functionality as "contextual autoescaping". safehtml/template uses the term "autosanitization" instead of "autoescaping" since "sanitization" broadly captures the operations of escaping and filtering.

#### Sanitization contexts ¶

The types of sanitization functions inserted into an action depend on the action's sanitization context, which is determined by its surrounding text. The following table describes these sanitization contexts.

```go
+--------------------+----------------------------------+------------------------------+-----------------------+
| Context            | Examples                         | Safe types                   | Run-time sanitizer    |
|--------------------+----------------------------------+------------------------------+-----------------------+
| HTMLContent        | Hello {{.}}                      | safehtml.HTML                | safehtml.HTMLEscaped  |
|                    | <title>{{.}}</title>             |                              |                       |
+--------------------------------------------------------------------------------------------------------------+
| HTMLValOnly        | <iframe srcdoc="{{.}}"></iframe> | safehtml.HTML*               | N/A                   |
+--------------------------------------------------------------------------------------------------------------+
| URL                | <q cite="{{.}}">Cite</q>         | safehtml.URL                 | safehtml.URLSanitized |
+--------------------------------------------------------------------------------------------------------------+
| URL or             | <a href="{{.}}">Link</a>         | safehtml.URL                 | safehtml.URLSanitized |
| TrustedResourceURL |                                  | safehtml.TrustedResourceURL  |                       |
+--------------------------------------------------------------------------------------------------------------+
| TrustedResourceURL | <script src="{{.}}"></script>    | safehtml.TrustedResourceURL† | N/A                   |
+--------------------------------------------------------------------------------------------------------------+
| Script             | <script>{{.}}</script>           | safehtml.Script*             | N/A                   |
+--------------------------------------------------------------------------------------------------------------+
| Style              | <p style="{{.}}">Paragraph</p>   | safehtml.Style*              | N/A                   |
+--------------------------------------------------------------------------------------------------------------+
| Stylesheet         | <style>{{.}}</style>             | safehtml.StyleSheet*         | N/A                   |
+--------------------------------------------------------------------------------------------------------------+
| Identifier         | <h1 id="{{.}}">Hello</h1>        | safehtml.Identifier*         | N/A                   |
+--------------------------------------------------------------------------------------------------------------+
| Enumerated value   | <a target="{{.}}">Link</a>       | Allowed string values        | N/A                   |
|                    |                                  | ("_self" or "_blank" for     |                       |
|                    |                                  | the given example)           |                       |
+--------------------------------------------------------------------------------------------------------------+
| None               | <h1 class="{{.}}">Hello</h1>     | N/A (any type allowed)       | N/A (any type         |
|                    |                                  |                              |      allowed)         |
+--------------------+----------------------------------+------------------------------+-----------------------+
 *: Values only of this type are allowed in this context. Other values will trigger a run-time error.
 †: If the action is a prefix of the attribute value, values only of this type are allowed.
    Otherwise, values of any type are allowed. See "Substitutions in URLs" for more details.

```

For each context, the function named in "Run-time sanitizer" is called to sanitize the output of the action. However, if the action outputs a value of any of the types listed in "Safe types", the run-time sanitizer is not called. For example, in

```go
<title>{{ .X }}</title>

```

if X is a string value, a HTML sanitizer that calls safehtml.HTMLEscaped will be added to the action to sanitize X.

```go
// _sanitizeHTML calls safehtml.HTMLEscaped.
<title>{{ .X | _sanitizeHTML }}</title>

```

However, if X is a safehtml.HTML value, _sanitizeHTML will not change its value, since safehtml.HTML values are already safe to use in HTML contexts. Therefore, the string contents of X will bypass context-specific sanitization (in this case, HTML escaping) and appear unchanged in the template's HTML output. Note that in attribute value contexts, HTML escaping will always take place, whether or not context-specific sanitization is performed. More details can be found at the end of this section.

In certain contexts, the autosanitizer allows values only of that context's "Safe types". Any other values will trigger an error and abort template processing. For example, the template

```go
<style>{{ .X }}</style>

```

triggers a run-time error if X is not a safehtml.StyleSheet. Otherwise, the string form of X will appear unchanged in the output. The only exception to this behavior is in TrustedResourceURL sanitization contexts, where actions may output data of any type if the action occurs after a safe attribute value prefix. More details can be found below in "Substitutions in URLs".

#### Unconditional sanitization ¶

In attribute value contexts, action outputs are always HTML-escaped after context-specific sanitization to ensure that the attribute values cannot change change the structure of the surrounding HTML tag. In URL or TrustedResourceURL sanitization contexts, action outputs are additionally URL-normalized to reduce the likelihood of downstream URL-parsing bugs. For example, the template

```go
<a href="{{ .X }}">Link</a>
<p id="{{ .Y }}">Text</p>

```

is rewritten by the autosanitizer into

```go
// _sanitizeHTML calls safehtml.HTMLEscaped.
<a href="{{ .X | _sanitizeTrustedResourceURLOrURL | _normalizeURL | _sanitizeHTML }}">Link</a>
<p id="{{ .Y | _sanitizeIdentifier | _sanitizeHTML }}">Text</p>

```

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

	// ErrEndContext: "... ends in a non-text context: ..."
	// Examples:
	//   <div
	//   <div title="no close quote>
	//   <script>f()
	// Discussion:
	//   Executed templates should produce a DocumentFragment of HTML.
	//   Templates that end without closing tags will trigger this error.
	//   Templates that should not be used in an HTML context or that
	//   produce incomplete Fragments should not be executed directly.
	//
	//   {{define "main"}} <script>{{template "helper"}}</script> {{end}}
	//   {{define "helper"}} document.write(' <div title=" ') {{end}}
	//
	//   "helper" does not produce a valid document fragment, so should
	//   not be Executed directly.
	ErrEndContext

	// ErrNoSuchTemplate: "no such template ..."
	// Examples:
	//   {{define "main"}}<div {{template "attrs"}}>{{end}}
	//   {{define "attrs"}}href="{{.URL}}"{{end}}
	// Discussion:
	//   Package html/template looks through template calls to compute the
	//   context.
	//   Here the {{.URL}} in "attrs" must be treated as a URL when called
	//   from "main", but you will get this error if "attrs" is not defined
	//   when "main" is parsed.
	ErrNoSuchTemplate

	// ErrOutputContext: "cannot compute output context for template ..."
	// Examples:
	//   {{define "t"}}{{if .T}}{{template "t" .T}}{{end}}{{.H}}",{{end}}
	// Discussion:
	//   A recursive template does not end in the same context in which it
	//   starts, and a reliable output context cannot be computed.
	//   Look for typos in the named template.
	//   If the template should not be called in the named start context,
	//   look for calls to that template in unexpected contexts.
	//   Maybe refactor recursive templates to not be recursive.
	ErrOutputContext

	// ErrPartialCharset: "unfinished JS regexp charset in ..."
	// Example:
	//     <script>var pattern = /foo[{{.Chars}}]/</script>
	// Discussion:
	//   Package html/template does not support interpolation into regular
	//   expression literal character sets.
	ErrPartialCharset

	// ErrPartialEscape: "unfinished escape sequence in ..."
	// Example:
	//   <script>alert("\{{.X}}")</script>
	// Discussion:
	//   Package html/template does not support actions following a
	//   backslash.
	//   This is usually an error and there are better solutions; for
	//   example
	//     <script>alert("{{.X}}")</script>
	//   should work, and if {{.X}} is a partial escape sequence such as
	//   "xA0", mark the whole sequence as safe content: JSStr(`\xA0`)
	ErrPartialEscape

	// ErrRangeLoopReentry: "on range loop re-entry: ..."
	// Example:
	//   <script>var x = [{{range .}}'{{.}},{{end}}]</script>
	// Discussion:
	//   If an iteration through a range would cause it to end in a
	//   different context than an earlier pass, there is no single context.
	//   In the example, there is missing a quote, so it is not clear
	//   whether {{.}} is meant to be inside a JS string or in a JS value
	//   context. The second iteration would produce something like
	//
	//     <script>var x = ['firstValue,'secondValue]</script>
	ErrRangeLoopReentry

	// ErrSlashAmbig: '/' could start a division or regexp.
	// Example:
	//   <script>
	//     {{if .C}}var x = 1{{end}}
	//     /-{{.N}}/i.test(x) ? doThis : doThat();
	//   </script>
	// Discussion:
	//   The example above could produce `var x = 1/-2/i.test(s)...`
	//   in which the first '/' is a mathematical division operator or it
	//   could produce `/-2/i.test(s)` in which the first '/' starts a
	//   regexp literal.
	//   Look for missing semicolons inside branches, and maybe add
	//   parentheses to make it clear which interpretation you intend.
	ErrSlashAmbig

	// ErrPredefinedEscaper: "predefined escaper ... disallowed in template"
	// Example:
	//   <div class={{. | html}}>Hello<div>
	// Discussion:
	//   Package html/template already contextually escapes all pipelines to
	//   produce HTML output safe against code injection. Manually escaping
	//   pipeline output using the predefined escapers "html" or "urlquery" is
	//   unnecessary, and may affect the correctness or safety of the escaped
	//   pipeline output in Go 1.8 and earlier.
	//
	//   In most cases, such as the given example, this error can be resolved by
	//   simply removing the predefined escaper from the pipeline and letting the
	//   contextual autoescaper handle the escaping of the pipeline. In other
	//   instances, where the predefined escaper occurs in the middle of a
	//   pipeline where subsequent commands expect escaped input, e.g.
	//     {{.X | html | makeALink}}
	//   where makeALink does
	//     return `<a href="`+input+`">link</a>`
	//   consider refactoring the surrounding template to make use of the
	//   contextual autoescaper, i.e.
	//     <a href="{{.X}}">link</a>
	//
	//   To ease migration to Go 1.9 and beyond, "html" and "urlquery" will
	//   continue to be allowed as the last command in a pipeline. However, if the
	//   pipeline occurs in an unquoted attribute value context, "html" is
	//   disallowed. Avoid using "html" and "urlquery" entirely in new templates.
	ErrPredefinedEscaper

	// ErrEscapeAction: "cannot escape action ..."
	// Discussion:
	//   Error returned while escaping an action using EscaperForContext.
	//   Refer to error message for more details.
	// TODO: remove this error type and replace it with more informative sanitization errors.
	ErrEscapeAction

	// ErrCSPCompatibility: `"javascript:" URI disallowed for CSP compatibility`,
	//   "inline event handler ... is disallowed for CSP compatibility
	// Examples:
	//   <span onclick="doThings();">A thing.</span>
	//   <a href="javascript:linkClicked()">foo</a>
	// Discussion:
	//   Inline event handlers (onclick="...", onerror="...") and
	//   <a href="javascript:..."> links can be used to run scripts,
	//   so an attacker who finds an XSS bug could inject such HTML
	//   and execute malicious JavaScript. These patterns must be
	//   refactored into safer alternatives for compatibility with
	//   Content Security Policy (CSP).
	//
	//   For example, the following HTML that contains an inline event handler:
	//     <script> function doThings() { ... } </script>
	//     <span onclick="doThings();">A thing.</span>
	//   can be refactored into:
	//     <span id="things">A thing.</span>
	//     <script nonce="${nonce}">
	//     document.addEventListener('DOMContentLoaded', function () {
	//       document.getElementById('things')
	//               .addEventListener('click', function doThings() { ... });
	//     });
	//     </script>
	//
	//   Likewise, the following HTML containng a javascript: URI:
	//     <a href="javascript:linkClicked()">foo</a>
	//   can be refactored into:
	//     <a id="foo">foo</a>
	//     <script nonce="${nonce}">
	//     document.addEventListener('DOMContentLoaded', function () {
	//       document.getElementById('foo')
	//               .addEventListener('click', linkClicked);
	//     });
	//     </script>
	ErrCSPCompatibility
	// All JS templates inside script literals have to be balanced; otherwise a concatenation such as
	// <script>alert(`x{{.data}}`</script> can contain XSS if data contains user-controlled escaped strings (e.g. as JSON).
	ErrUnbalancedJsTemplate
)
```

We define codes for each error that manifests while escaping templates, but escaped templates may also fail at runtime.

Output: "ZgotmplZ" Example:

```go
<img src="{{.X}}">
where {{.X}} evaluates to `javascript:...`

```

Discussion:

```go
"ZgotmplZ" is a special value that indicates that unsafe content reached a
CSS or URL context at runtime. The output of the example will be
  <img src="#ZgotmplZ">
If the data comes from a trusted source, use content types to exempt it
from filtering: URL(`javascript:...`).

```

```go
type FuncMap map[string]interface{}
```

FuncMap is the type of the map defining the mapping from names to functions. Each function must have either a single return value, or two return values of which the second has type error. In that case, if the second (error) argument evaluates to non-nil during execution, execution terminates and Execute returns that error. FuncMap has the same base type as FuncMap in "text/template", copied here so clients need not import "text/template".

```go
type Template struct {

	// The underlying template's parse tree, updated to be HTML-safe.
	Tree *parse.Tree
	// contains filtered or unexported fields
}
```

Template is a specialized Template from "text/template" that produces a safe HTML document fragment.

```go

package main

import (
	"log"
	"os"
	"strings"

	"github.com/google/safehtml/template"
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

Here we demonstrate loading a set of templates from a directory.

```go

package main

import (
	"log"
	"os"

	"github.com/google/safehtml/template"
)

func main() {
	// Here we load three template files with the following contents:
	// 		testdata/glob_t0.tmpl: `T0 invokes T1: ({{template "T1"}})`
	// 		testdata/glob_t1.tmpl: `{{define "T1"}}T1 invokes T2: ({{template "T2"}}){{end}}`
	// 		testdata/glob_t2.tmpl: `{{define "T2"}}This is T2{{end}}`
	// Note that ParseGlob only accepts an untyped string constant.
	// glob_t0.tmpl is the first name matched, so it becomes the starting template,
	// the value returned by ParseGlob.
	tmpl := template.Must(template.ParseGlob("testdata/glob_*.tmpl"))

	err := tmpl.Execute(os.Stdout, nil)
	if err != nil {
		log.Fatalf("template execution: %s", err)
	}
}

```

```go
Output:
T0 invokes T1: (T1 invokes T2: (This is T2))

```

 Share Format Run

This example demonstrates one way to share some templates and use them in different contexts. In this variant we add multiple driver templates by hand to an existing bundle of templates.

```go

package main

import (
	"log"
	"os"

	"github.com/google/safehtml/template"
)

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

ExecuteToHTML applies a parsed template to the specified data object, returning the output as a safehtml.HTML value. A template may be executed safely in parallel.

```go
func (t *Template) Funcs(funcMap FuncMap) *Template
```

Funcs adds the elements of the argument map to the template's function map. It must be called before the template is parsed. It panics if a value in the map is not a function with appropriate return type. However, it is legal to overwrite elements of the map. The return value is the template, so calls can be chained.

```go
func (t *Template) Lookup(name string) *Template
```

Lookup returns the template with the given name that is associated with t, or nil if there is no such template.

```go
func (t *Template) Name() string
```

Name returns the name of the template.

```go
func (t *Template) New(name string) *Template
```

New allocates a new HTML template associated with the given one and with the same delimiters. The association, which is transitive, allows one template to invoke another with a {{template}} action.

If a template with the given name already exists, the new HTML template will replace it. The existing template will be reset and disassociated with t.

```go
func (t *Template) Option(opt ...string) *Template
```

Option sets options for the template. Options are described by strings, either a simple string or "key=value". There can be at most one equals sign in an option string. If the option string is unrecognized or otherwise invalid, Option panics.

Known options:

missingkey: Control the behavior during execution if a map is indexed with a key that is not present in the map.

```go
"missingkey=default" or "missingkey=invalid"
	The default behavior: Do nothing and continue execution.
	If printed, the result of the index operation is the string
	"<no value>".
"missingkey=zero"
	The operation returns the zero value for the map type's element.
"missingkey=error"
	Execution stops immediately with an error.

```

```go
func (t *Template) Parse(text stringConstant) (*Template, error)
```

Parse parses text as a template body for t. Named template definitions ({{define ...}} or {{block ...}} statements) in text define additional templates associated with t and are removed from the definition of t itself.

Templates can be redefined in successive calls to Parse, before the first use of Execute on t or any associated template. A template definition with a body containing only white space and comments is considered empty and will not replace an existing template's body. This allows using Parse to add new named template definitions without overwriting the main template body.

To guarantee that the template body is never controlled by an attacker, text must be an untyped string constant, which is always under programmer control.

```go
func (t *Template) ParseFS(tfs TrustedFS, patterns ...string) (*Template, error)
```

ParseFS is like ParseFiles or ParseGlob but reads from the TrustedFS instead of the host operating system's file system. It accepts a list of glob patterns. (Note that most file names serve as glob patterns matching only themselves.)

The same behaviors listed for ParseFiles() apply to ParseFS too (e.g. using the base name of the file as the template name).

```go
func (t *Template) ParseFiles(filenames ...stringConstant) (*Template, error)
```

ParseFiles parses the named files and associates the resulting templates with t. If an error occurs, parsing stops and the returned template is nil; otherwise it is t. There must be at least one file.

When parsing multiple files with the same name in different directories, the last one mentioned will be the one that results.

ParseFiles returns an error if t or any associated template has already been executed.

To guarantee that filepaths, and thus template bodies, are never controlled by an attacker, filenames must be untyped string constants, which are always under programmer control.

```go
func (t *Template) ParseFilesFromTrustedSources(filenames ...TrustedSource) (*Template, error)
```

ParseFilesFromTrustedSources parses the named files and associates the resulting templates with t. If an error occurs, parsing stops and the returned template is nil; otherwise it is t. There must be at least one file.

When parsing multiple files with the same name in different directories, the last one mentioned will be the one that results.

ParseFilesFromTrustedSources returns an error if t or any associated template has already been executed.

To guarantee that filepaths, and thus template bodies, are never controlled by an attacker, filenames must be trusted sources, which are always under programmer or application control.

```go
func (t *Template) ParseFromTrustedTemplate(tmpl TrustedTemplate) (*Template, error)
```

ParseFromTrustedTemplate parses tmpl as a template body for t. Named template definitions ({{define ...}} or {{block ...}} statements) in text define additional templates associated with t and are removed from the definition of t itself.

Templates can be redefined in successive calls to ParseFromTrustedTemplate, before the first use of Execute on t or any associated template. A template definition with a body containing only white space and comments is considered empty and will not replace an existing template's body. This allows using ParseFromTrustedTemplate to add new named template definitions without overwriting the main template body.

To guarantee that the template body is never controlled by an attacker, tmpl is a TrustedTemplate, which is always under programmer control.

```go
func (t *Template) ParseGlob(pattern stringConstant) (*Template, error)
```

ParseGlob parses the template definitions in the files identified by the pattern and associates the resulting templates with t. The pattern is processed by filepath.Glob and must match at least one file. ParseGlob is equivalent to calling t.ParseFiles with the list of files matched by the pattern.

When parsing multiple files with the same name in different directories, the last one mentioned will be the one that results.

ParseGlob returns an error if t or any associated template has already been executed.

To guarantee that the pattern, and thus the template bodies, is never controlled by an attacker, pattern must be an untyped string constant, which is always under programmer control.

```go
func (t *Template) ParseGlobFromTrustedSource(pattern TrustedSource) (*Template, error)
```

ParseGlobFromTrustedSource parses the template definitions in the files identified by the pattern and associates the resulting templates with t. The pattern is processed by filepath.Glob and must match at least one file. ParseGlob is equivalent to calling t.ParseFiles with the list of files matched by the pattern.

When parsing multiple files with the same name in different directories, the last one mentioned will be the one that results.

ParseGlobFromTrustedSource returns an error if t or any associated template has already been executed.

To guarantee that the pattern, and thus the template bodies, is never controlled by an attacker, pattern must be a trusted source, which is always under programmer or application control.

```go
func (t *Template) Templates() []*Template
```

Templates returns a slice of the templates associated with t, including t itself.

```go
type TrustedFS struct {
	// contains filtered or unexported fields
}
```

A TrustedFS is an immutable type referencing a filesystem (fs.FS) under application control.

In order to ensure that an attacker cannot influence the TrustedFS value, a TrustedFS can be instantiated in only two ways. One way is from an embed.FS with TrustedFSFromEmbed. It is assumed that embedded filesystems are under the programmer's control. The other way is from a TrustedSource using TrustedFSFromTrustedSource, in which case the guarantees and caveats of TrustedSource apply.

```go
func TrustedFSFromEmbed(fsys embed.FS) TrustedFS
```

TrustedFSFromEmbed constructs a TrustedFS from an embed.FS.

```go
func TrustedFSFromTrustedSource(ts TrustedSource) TrustedFS
```

TrustedFSFromTrustedSource constructs a TrustedFS from the string in the TrustedSource, which should refer to a directory.

```go
func (tf TrustedFS) Sub(dir TrustedSource) (TrustedFS, error)
```

Sub returns a TrustedFS at a subdirectory of the receiver. It works by calling fs.Sub on the receiver's fs.FS.

```go
type TrustedSource struct {
	// contains filtered or unexported fields
}
```

A TrustedSource is an immutable string-like type referencing trusted template files under application control. It can be passed to template-parsing functions and methods to safely load templates without the risk of untrusted template execution.

In order to ensure that an attacker cannot influence the TrustedSource value, a TrustedSource can be instantiated only from untyped string constants, command-line flags, and other application-controlled strings, but never from arbitrary string values potentially representing untrusted user input.

Note that TrustedSource's constructors cannot truly guarantee that the templates it references are not attacker-controlled; it can guarantee only that the path to the template itself is under application control. Users of these constructors must ensure themselves that TrustedSource never references attacker-controlled files or directories that contain such files.

```go
func TrustedSourceFromConstant(src stringConstant) TrustedSource
```

TrustedSourceFromConstant constructs a TrustedSource with its underlying src set to the given src, which must be an untyped string constant.

No runtime validation or sanitization is performed on src; being under application control, it is simply assumed to comply with the TrustedSource type contract.

```go
func TrustedSourceFromConstantDir(dir stringConstant, src TrustedSource, filename string) (TrustedSource, error)
```

TrustedSourceFromConstantDir constructs a TrustedSource calling path/filepath.Join on an application-controlled directory path, which must be an untyped string constant, a TrustedSource, and a dynamic filename. It returns an error if filename contains filepath or list separators, since this might cause the resulting path to reference a file outside of the given directory.

dir or src may be empty if either of these path segments are not required.

```go
func TrustedSourceFromEnvVar(key stringConstant) TrustedSource
```

TrustedSourceFromEnvVar is a wrapper around os.Getenv that returns a TrustedSource containing the value of the environment variable named by the key. It returns the value, which will be empty if the variable is not present. To distinguish between an empty value and an unset value, use os.LookupEnv.

In a server setting, environment variables are part of the application's deployment configuration and are hence considered application-controlled.

```go
func TrustedSourceFromFlag(value flag.Value) TrustedSource
```

TrustedSourceFromFlag returns a TrustedSource containing the string representation of the retrieved value of the flag.

In a server setting, flags are part of the application's deployment configuration and are hence considered application-controlled.

```go
func TrustedSourceJoin(elem ...TrustedSource) TrustedSource
```

TrustedSourceJoin is a wrapper around path/filepath.Join that returns a TrustedSource formed by joining the given path elements into a single path, adding an OS-specific path separator if necessary.

```go
func (t TrustedSource) String() string
```

String returns the string form of the TrustedSource.

```go
type TrustedTemplate struct {
	// contains filtered or unexported fields
}
```

A TrustedTemplate is an immutable string-like type containing a safehtml/template template body. It can be safely loaded as template text without the risk of untrusted template execution.

In order to ensure that an attacker cannot influence the TrustedTemplate value, a TrustedTemplate can be instantiated only from untyped string constants, and never from arbitrary string values potentially representing untrusted user input.

```go
func MakeTrustedTemplate(tmpl stringConstant) TrustedTemplate
```

MakeTrustedTemplate constructs a TrustedTemplate with its underlying tmpl set to the given tmpl, which must be an untyped string constant.

No runtime validation or sanitization is performed on tmpl; being under application control, it is simply assumed to comply with the TrustedTemplate type contract.

```go
func (t TrustedTemplate) String() string
```

String returns the string form of the TrustedTemplate.

##   Source Files ¶
 View all Source files <https://github.com/google/safehtml/tree/v0.1.0/template>

- context.go <https://github.com/google/safehtml/blob/v0.1.0/template/context.go>
- delim_string.go <https://github.com/google/safehtml/blob/v0.1.0/template/delim_string.go>
- doc.go <https://github.com/google/safehtml/blob/v0.1.0/template/doc.go>
- error.go <https://github.com/google/safehtml/blob/v0.1.0/template/error.go>
- escape.go <https://github.com/google/safehtml/blob/v0.1.0/template/escape.go>
- init.go <https://github.com/google/safehtml/blob/v0.1.0/template/init.go>
- sanitize.go <https://github.com/google/safehtml/blob/v0.1.0/template/sanitize.go>
- sanitizers.go <https://github.com/google/safehtml/blob/v0.1.0/template/sanitizers.go>
- state_string.go <https://github.com/google/safehtml/blob/v0.1.0/template/state_string.go>
- template.go <https://github.com/google/safehtml/blob/v0.1.0/template/template.go>
- transition.go <https://github.com/google/safehtml/blob/v0.1.0/template/transition.go>
- trustedfs.go <https://github.com/google/safehtml/blob/v0.1.0/template/trustedfs.go>
- trustedsource.go <https://github.com/google/safehtml/blob/v0.1.0/template/trustedsource.go>
- trustedtemplate.go <https://github.com/google/safehtml/blob/v0.1.0/template/trustedtemplate.go>
- url.go <https://github.com/google/safehtml/blob/v0.1.0/template/url.go>

##   Directories ¶
    Show internal   Expand all

      uncheckedconversions
 Package uncheckedconversions provides functions to create values of safehtml/template types from plain strings.

  Package uncheckedconversions provides functions to create values of safehtml/template types from plain strings.

  Click to show internal directories.
  Click to hide internal directories.

  Close

     **?** : This menu   **/** : Search site   **f** or **F** : Jump to   **y** or **Y**  : Canonical URL
  Close
