---
source_name: "External Linked Documentation"
source_url: "https://go.dev/ref/spec"
source_path: "sources/raw/external/go-dev-ref-spec-3c5b020879.html"
license_ref: ""
---

## Expressions

-  If all types in `C`'s type set have the same underlying type `U`, and `P` has a known type argument `A`, `U` and `A` must unify loosely.
-  Similarly, if all types in `C`'s type set are channel types with the same element type and non-conflicting channel directions, and `P` has a known type argument `A`, the most restrictive channel type in `C`'s type set and `A` must unify loosely.
-  If `P` does not have a known type argument and `C` contains exactly one type term `T` that is not an underlying (tilde) type, unification adds the mapping `P ➞ T` to the map.
-  If `C` does not have a type `U` as described above and `P` has a known type argument `A`, `A` must have all methods of `C`, if any, and corresponding method types must unify exactly.

When solving type equations from type constraints, solving one equation may infer additional type arguments, which in turn may enable solving other equations that depend on those type arguments. Type inference repeats type unification as long as new type arguments are inferred.
