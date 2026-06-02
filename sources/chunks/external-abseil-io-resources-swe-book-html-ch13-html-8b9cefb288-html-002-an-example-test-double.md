---
source_name: "External Linked Documentation"
source_url: "https://abseil.io/resources/swe-book/html/ch13.html"
source_path: "sources/raw/external/abseil-io-resources-swe-book-html-ch13-html-8b9cefb288.html"
license_ref: ""
---

# Test Doubles

## An Example Test Double

Imagine an ecommerce site that needs to process credit card payments. At its core, it might have something like the code shown in A credit card service.
  Example 13-1. A credit card service
```go

class PaymentProcessor {
  private **CreditCardService creditCardService**;
  ...
  boolean **makePayment**(CreditCard creditCard, Money amount) {
    if (creditCard.isExpired()) { return false; }
    boolean success =**
        creditCardService**.chargeCreditCard(creditCard, amount);
    return success;
  }
}
```

It would be infeasible to use a real credit card service in a test (imagine all the transaction fees from running the test!), but a test double could be used in its place to _simulate_ the behavior of the real system. The code in A trivial test double shows an extremely simple test double.
  Example 13-2. A trivial test double
```go

class TestDoubleCreditCardService implements CreditCardService {
 @Override
 public boolean chargeCreditCard(CreditCard creditCard, Money amount) {
   return true;
 }
}
```

Although this test double doesn’t look very useful, using it in a test still allows us to test some of the logic in the `makePayment()` method. For example, in Using the test double, we can validate that the method behaves properly when the credit card is expired because the code path that the test exercises doesn’t rely on the behavior of the credit card service.
  Example 13-3. Using the test double
```go

@Test public void cardIsExpired_returnFalse() {
  boolean success = **paymentProcessor**.makePayment(EXPIRED_CARD, AMOUNT);
  assertThat(success).isFalse();
}
```

The following sections in this chapter will discuss how to make use of test doubles in more complex situations than this one.
