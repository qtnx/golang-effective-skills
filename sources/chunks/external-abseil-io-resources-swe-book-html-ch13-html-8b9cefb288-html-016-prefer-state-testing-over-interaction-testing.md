---
source_name: "External Linked Documentation"
source_url: "https://abseil.io/resources/swe-book/html/ch13.html"
source_path: "sources/raw/external/abseil-io-resources-swe-book-html-ch13-html-8b9cefb288.html"
license_ref: ""
---

# Test Doubles

## Prefer State Testing Over Interaction Testing

In contrast to interaction  testing, it is preferred  to test code through _state testing_ <https://oreil.ly/k3hSR>.

With state testing, you call the system under test and validate that either the correct value was returned or that some other state in the system under test was properly changed. State testing presents an example of state testing.
  Example 13-15. State testing
```go

@Test public void sortNumbers() {
  NumberSorter **numberSorter** = new NumberSorter(**quicksort**, **bubbleSort**);
  // Call the system under test.
  List **sortedList** = **numberSorter**.sortNumbers(newList(3, 1, 2));
  // Validate that the returned list is sorted. It doesn’t matter which
  // sorting algorithm is used, as long as the right result was returned.
  assertThat(**sortedList**).isEqualTo(newList(1, 2, 3));
}
```

Interaction testing illustrates a similar test scenario but instead uses interaction testing. Note how it’s impossible for this test to determine that the numbers are actually sorted, because the test doubles don’t know how to sort the numbers—all it can tell you is that the system under test tried to sort the numbers.
  Example 13-16. Interaction testing
```go

@Test public void sortNumbers_quicksortIsUsed() {
  // Pass in test doubles that were created by a mocking framework.
  NumberSorter **numberSorter** =
      new NumberSorter(**mockQuicksort**, **mockBubbleSort**);

  // Call the system under test.
  **numberSorter**.sortNumbers(newList(3, 1, 2));

  // Validate that numberSorter.sortNumbers() used quicksort. The test
  // will fail if mockQuicksort.sort() is never called (e.g., if
  // mockBubbleSort is used) or if it’s called with the wrong arguments.
  verify(**mockQuicksort**).sort(newList(3, 1, 2));
}
```

At Google, we’ve found that emphasizing state testing is more scalable; it reduces test brittleness, making it easier to change and maintain code over time.

The primary  issue with interaction testing is that it can’t tell you that the system under test is working properly; it can only validate that certain functions are called as expected. It requires you to make an assumption about the behavior of the code; for example, “_If `database.save(item)` is called, we assume the item will be saved to the database._” State testing is preferred because it actually validates this assumption (such as by saving an item to a database and then querying the database to validate that the item exists).

Another downside of interaction testing is that it utilizes implementation details of the system under test—to validate that a function was called, you are exposing to the test that the system under test calls this function. Similar to stubbing, this extra code makes tests brittle because it leaks implementation details of your production code into tests. Some people at Google jokingly refer to tests that overuse interaction testing as _change-detector tests_ <https://oreil.ly/zkMDu> because they fail in response to any change to the production code, even if the behavior of the system under test remains unchanged.
