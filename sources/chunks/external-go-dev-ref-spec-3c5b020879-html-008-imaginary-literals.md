---
source_name: "External Linked Documentation"
source_url: "https://go.dev/ref/spec"
source_path: "sources/raw/external/go-dev-ref-spec-3c5b020879.html"
license_ref: ""
---

## Lexical elements

### Imaginary literals

 An imaginary literal represents the imaginary part of a complex constant. It consists of an integer or floating-point literal followed by the lowercase letter `i`. The value of an imaginary literal is the value of the respective integer or floating-point literal multiplied by the imaginary unit _i_ [Go 1.13]

```go

imaginary_lit = (decimal_digits | int_lit | float_lit) "i" .

```

 For backward compatibility, an imaginary literal's integer part consisting entirely of decimal digits (and possibly underscores) is considered a decimal integer, even if it starts with a leading `0`.

```go

0i
0123i         // == 123i for backward-compatibility
0o123i        // == 0o123 * 1i == 83i
0xabci        // == 0xabc * 1i == 2748i
0.i
2.71828i
1.e+0i
6.67428e-11i
1E6i
.25i
.12345E+5i
0x1p-2i       // == 0x1p-2 * 1i == 0.25i

```
