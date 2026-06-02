---
source_name: "External Linked Documentation"
source_url: "https://abseil.io/resources/swe-book/html/ch13.html"
source_path: "sources/raw/external/abseil-io-resources-swe-book-html-ch13-html-8b9cefb288.html"
license_ref: ""
---

# Test Doubles

## The Dangers of Overusing Stubbing

Because stubbing is so easy to apply in tests, it can be tempting to use this technique anytime it’s not trivial to use a real implementation.  However, overuse of stubbing can result in major losses in productivity for engineers who need to maintain these tests.

### Tests become unclear

Stubbing involves writing extra code to define the behavior of the functions being stubbed.  Having this extra code detracts from the intent of the test, and this code can be difficult to understand if you’re not familiar with the implementation of the system under test.

A key sign that stubbing isn’t appropriate for a test is if you find yourself mentally stepping through the system under test in order to understand why certain functions in the test are stubbed.

### Tests become brittle

Stubbing leaks  implementation details of your code into your test.  When implementation details in your production code change, you’ll need to update your tests to reflect these changes. Ideally, a good test should need to change only if user-facing behavior of an API changes; it should remain unaffected by changes to the API’s implementation.

### Tests become less effective

With stubbing, there is no way to  ensure the function being stubbed behaves like the real implementation, such as in a statement like that shown in the following snippet that hardcodes part of the contract of the `add()` method (_“If 1 and 2 are passed in, 3 will be returned”_):

```go

when(stubCalculator.add(1, 2)).thenReturn(3);
```

Stubbing is a poor choice if the system under test depends on the real implementation’s contract because you will be forced to duplicate the details of the contract, and there is no way to guarantee that the contract is correct (i.e., that the stubbed function has fidelity to the real implementation).

Additionally, with stubbing there is no way to store state, which can make it difficult to test certain aspects of your code. For example, if you call `database.save(item)` on either a real implementation or a fake, you might be able to retrieve the item by calling `database.get(item.id())` given that both of these calls are accessing internal state, but with stubbing, there is no way to do this.

### An example of overusing stubbing

Overuse of stubbing illustrates a test that  overuses stubbing.
  Example 13-13. Overuse of stubbing
```go

@Test public void creditCardIsCharged() {
  // Pass in test doubles that were created by a mocking framework.
  **paymentProcessor** =
      new PaymentProcessor(**mockCreditCardServer**, **mockTransactionProcessor**);
  // Set up stubbing for these test doubles.
  when(**mockCreditCardServer**.isServerAvailable()).thenReturn(true);
  when(**mockTransactionProcessor**.beginTransaction()).thenReturn(transaction);
  when(**mockCreditCardServer**.initTransaction(transaction)).thenReturn(true);
  when(**mockCreditCardServer**.pay(transaction, creditCard, 500))
      .thenReturn(false);
  when(**mockTransactionProcessor**.endTransaction()).thenReturn(true);
  // Call the system under test.
  **paymentProcessor**.processPayment(creditCard, Money.dollars(500));
  // There is no way to tell if the pay() method actually carried out the
  // transaction, so the only thing the test can do is verify that the
  // pay() method was called.
  verify(**mockCreditCardServer**).pay(transaction, creditCard, 500);
}
```

Refactoring a test to avoid stubbing rewrites the same test but avoids using stubbing. Notice how the test is shorter and that implementation details (such as how the transaction processor is used) are not exposed in the test.  No special setup is needed because the credit card server knows how to behave.
  Example 13-14. Refactoring a test to avoid stubbing
```go

@Test public void creditCardIsCharged() {
  **paymentProcessor** =
      new PaymentProcessor(**creditCardServer**, **transactionProcessor**);
  // Call the system under test.
  **paymentProcessor**.processPayment(creditCard, Money.dollars(500));
  // Query the credit card server state to see if the payment went through.
  assertThat(**creditCardServer**.getMostRecentCharge(creditCard))
      .isEqualTo(500);
}
```

We obviously don’t want such a test to talk to an external credit card server, so a fake credit card server would be more suitable. If a fake isn’t available, another option is to use a real implementation that talks to a hermetic credit card server, although this will increase the execution time of the tests. (We explore hermetic servers in the next chapter.)
