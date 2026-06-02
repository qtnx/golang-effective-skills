---
source_name: "External Linked Documentation"
source_url: "https://abseil.io/resources/swe-book/html/ch13.html"
source_path: "sources/raw/external/abseil-io-resources-swe-book-html-ch13-html-8b9cefb288.html"
license_ref: ""
---

# Test Doubles

## Faking

A _fake_ <https://oreil.ly/rymnI> is a lightweight implementation of an API that behaves similar  to the real implementation but isn’t suitable  for production; for example, an in-memory database. A simple fake presents an example of faking.
  Example 13-7. A simple fake
```go

// Creating the fake is fast and easy.
AuthorizationService **fakeAuthorizationService** =
    new FakeAuthorizationService();
AccessManager accessManager = new AccessManager(**fakeAuthorizationService**):

// Unknown user IDs shouldn’t have access.
assertFalse(accessManager.userHasAccess(USER_ID));

// The user ID should have access after it is added to
// the authorization service.
**fakeAuthorizationService**.addAuthorizedUser(new User(USER_ID));
assertThat(accessManager.userHasAccess(USER_ID)).isTrue();
```

Using a fake is often the ideal technique when you need to use a test double, but a fake might not exist for an object you need to use in a test, and writing one can be challenging because you need to ensure that it has similar behavior to the real implementation, now and in the future.
