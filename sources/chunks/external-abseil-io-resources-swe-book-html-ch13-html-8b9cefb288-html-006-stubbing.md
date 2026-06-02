---
source_name: "External Linked Documentation"
source_url: "https://abseil.io/resources/swe-book/html/ch13.html"
source_path: "sources/raw/external/abseil-io-resources-swe-book-html-ch13-html-8b9cefb288.html"
license_ref: ""
---

# Test Doubles

## Stubbing

_Stubbing_ <https://oreil.ly/gmShS> is the process of giving behavior to a function that otherwise has no behavior on its own—you specify to the function exactly what values to return (that is, you _stub_ the return values).  

Stubbing illustrates stubbing.  The `when(...).thenReturn(...)` method calls from the Mockito mocking framework specify the behavior of the `lookupUser()` method.
  Example 13-8. Stubbing
```go

// Pass in a test double that was created by a mocking framework.
AccessManager accessManager = new AccessManager(**mockAuthorizationService**):

// The user ID shouldn’t have access if null is returned.
when(**mockAuthorizationService**.lookupUser(USER_ID)).thenReturn(null);
assertThat(accessManager.userHasAccess(USER_ID)).isFalse();

// The user ID should have access if a non-null value is returned.
when(**mockAuthorizationService**.lookupUser(USER_ID)).thenReturn(USER);
assertThat(accessManager.userHasAccess(USER_ID)).isTrue();
```

Stubbing is typically done  through mocking frameworks to reduce boilerplate that would otherwise be needed for manually creating new classes that hardcode return values.

Although stubbing can be a quick and simple technique to apply, it has limitations, which we’ll discuss later in this chapter.
