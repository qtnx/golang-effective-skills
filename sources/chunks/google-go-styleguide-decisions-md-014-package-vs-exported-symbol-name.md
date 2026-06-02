---
source_name: "Google Go Style Guide"
source_url: "https://google.github.io/styleguide/go/"
source_path: "sources/raw/google-go-styleguide/decisions.md"
license_ref: "sources/licenses/google-styleguide-LICENSE.txt"
---

#### Package vs. exported symbol name

When naming exported symbols, the name of the package is always visible outside
your package, so redundant information between the two should be reduced or
eliminated. If a package exports only one type and it is named after the package
itself, the canonical name for the constructor is `New` if one is required.

> **Examples:** Repetitive Name -> Better Name
>
> *   `widget.NewWidget` -> `widget.New`
> *   `widget.NewWidgetWithName` -> `widget.NewWithName`
> *   `db.LoadFromDatabase` -> `db.Load`
> *   `goatteleportutil.CountGoatsTeleported` -> `gtutil.CountGoatsTeleported`
>     or `goatteleport.Count`
> *   `myteampb.MyTeamMethodRequest` -> `mtpb.MyTeamMethodRequest` or
>     `myteampb.MethodRequest`

<a id="repetitive-with-type"></a>
