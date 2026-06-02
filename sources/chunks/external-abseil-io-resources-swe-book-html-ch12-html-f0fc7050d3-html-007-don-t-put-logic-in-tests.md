---
source_name: "External Linked Documentation"
source_url: "https://abseil.io/resources/swe-book/html/ch12.html"
source_path: "sources/raw/external/abseil-io-resources-swe-book-html-ch12-html-f0fc7050d3.html"
license_ref: ""
---

# Unit Testing

## Don’t Put Logic in Tests

Clear tests are trivially correct upon inspection; that is, it is obvious that a test is doing the correct thing just from glancing at it.   This is possible in test code because each test needs to handle only a particular set of inputs, whereas production code must be generalized to handle any input.  For production code, we’re able to write tests that ensure complex logic is correct. But test code doesn’t have that luxury—if you feel like you need to write a test to verify your test, something has gone wrong!

Complexity is most often introduced in the form of _logic_. Logic is defined via the imperative parts of programming languages such as operators, loops, and conditionals.  When a piece of code contains logic, you need to do a bit of mental computation to determine its result instead of just reading it off of the screen.  It doesn’t take much logic to make a test more difficult to reason about. For example, does the test in Logic concealing a bug look correct to you <https://oreil.ly/yJDqh>?
  Example 12-15. Logic concealing a bug
```go

@Test
public void shouldNavigateToAlbumsPage() {
  String baseUrl = "http://photos.google.com/";
  Navigator nav = new Navigator(baseUrl);
  nav.goToAlbumPage();
  assertThat(nav.getCurrentUrl()).isEqualTo(baseUrl + "/albums");
}
```

There’s not much logic here: really just one string concatenation. But if we simplify the test by removing that one bit of logic, a bug immediately becomes clear, as demonstrated in A test without logic reveals the bug.
  Example 12-16. A test without logic reveals the bug
```go

@Test
public void shouldNavigateToPhotosPage() {
  Navigator nav = new Navigator("http://photos.google.com/");
  nav.goToPhotosPage();
  assertThat(nav.getCurrentUrl()))
      .isEqualTo("http://photos.google.com//albums"); // Oops!
}
```

When the whole string is written out, we can see right away that we’re expecting two slashes in the URL instead of just one. If the production code made a similar mistake, this test would fail to detect a bug. Duplicating the base URL was a small price to pay for making the test more descriptive and meaningful (see the discussion of DAMP versus DRY tests later in this chapter).

If humans are bad at spotting bugs from string concatenation, we’re even worse at spotting bugs that come from more sophisticated programming constructs like loops and conditionals. The lesson is clear: in test code, stick to straight-line code over clever logic, and consider tolerating some duplication when it makes the test more descriptive and meaningful. We’ll discuss ideas around duplication and code sharing later in this chapter.
