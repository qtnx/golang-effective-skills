---
source_name: "External Linked Documentation"
source_url: "https://abseil.io/resources/swe-book/html/ch12.html"
source_path: "sources/raw/external/abseil-io-resources-swe-book-html-ch12-html-f0fc7050d3.html"
license_ref: ""
---

# Unit Testing

## Make Your Tests Complete and Concise

Two high-level properties that  help tests achieve  clarity are completeness and conciseness <https://oreil.ly/lqwyG>. A  test is _complete_ when its body contains all of the information a reader needs in order to understand how it arrives at its result. A test is _concise_ when it contains no other distracting or irrelevant information. An incomplete and cluttered test shows a test that is neither complete nor concise:
  Example 12-6. An incomplete and cluttered test
```go

@Test
public void shouldPerformAddition() {
  Calculator calculator = new Calculator(new RoundingStrategy(),
      "unused", ENABLE_COSINE_FEATURE, 0.01, calculusEngine, false);
  int result = calculator.calculate(newTestCalculation());
  assertThat(result).isEqualTo(5); // Where did this number come from?
}
```

The test is passing a lot of irrelevant information into the constructor, and the actual important parts of the test are hidden inside of a helper method. The test can be made more complete by clarifying the inputs of the helper method, and more concise by using another helper to hide the irrelevant details of constructing the calculator, as illustrated in A complete, concise test.
  Example 12-7. A complete, concise test
```go

@Test
public void shouldPerformAddition() {
  Calculator calculator = newCalculator();
  int result = calculator.calculate(newCalculation(2, Operation.PLUS, 3));
  assertThat(result).isEqualTo(5);
}
```

Ideas we discuss later, especially around code sharing, will tie back to completeness and conciseness.  In particular, it can often be worth violating the DRY (Don’t Repeat Yourself) principle if it leads to clearer tests. Remember: a _test’s body should contain all of the information needed to understand it without containing any irrelevant or distracting information_.
