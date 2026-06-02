---
source_name: "External Linked Documentation"
source_url: "https://abseil.io/resources/swe-book/html/ch13.html"
source_path: "sources/raw/external/abseil-io-resources-swe-book-html-ch13-html-8b9cefb288.html"
license_ref: ""
---

# Test Doubles

## Fakes Should Be Tested

A fake must have its _own_ tests to ensure that it conforms to the API of its corresponding real implementation.   A fake without tests might initially provide realistic behavior, but without tests, this behavior can diverge over time as the real implementation evolves.

One approach to writing tests for fakes involves writing tests against the API’s public  interface and running those tests against both the real implementation and the fake (these are known as _contract tests_ <https://oreil.ly/yuVlX>). The tests that run against the real implementation will likely be slower, but their downside is minimized because they need to be run only by the owners of the fake.

# Test Doubles

## What to Do If a Fake Is Not Available

If a fake is not available, first ask the owners of the API to create one.  The owners might not be familiar with the concept of fakes, or they might not realize the benefit they provide to users of an API.

If the owners of an API are unwilling or unable to create a fake, you might be able to write your own. One way to do this is to wrap all calls to the API in a single class and then create a fake version of the class that doesn’t talk to the API. Doing this can also be much simpler than creating a fake for the entire API because often you’ll need to use only a subset of the API’s behavior anyway. At Google, some teams have even contributed their fake to the owners of the API, which has allowed other teams to benefit from the fake.

Finally, you could decide to settle on using a real implementation (and deal with the trade-offs of real implementations that are mentioned earlier in this chapter), or resort to other test double techniques (and deal with the trade-offs that we will mention later in this chapter).

In some cases, you can think of a fake as an optimization: if tests are too slow using a real implementation, you can create a fake to make them run faster. But if the speedup from a fake doesn’t outweigh the work it would take to create and maintain the fake, it would be better  to stick with  using the real implementation.

# Stubbing

As discussed earlier in this chapter, stubbing  is a way  for a test to hardcode behavior for a function that otherwise has no behavior on its own. It is often a quick and easy way to replace a real implementation in a test. For example, the code in Using stubbing to simulate responses uses stubbing to simulate the response from a credit card server.
  Example 13-12. Using stubbing to simulate responses
```go

@Test public void getTransactionCount() {
  transactionCounter = new TransactionCounter(**mockCreditCardServer**);
  // Use stubbing to return three transactions.
  when(**mockCreditCardServer**.getTransactions()).thenReturn(
      newList(TRANSACTION_1, TRANSACTION_2, TRANSACTION_3));
  assertThat(transactionCounter.getTransactionCount()).isEqualTo(3);
}
```
