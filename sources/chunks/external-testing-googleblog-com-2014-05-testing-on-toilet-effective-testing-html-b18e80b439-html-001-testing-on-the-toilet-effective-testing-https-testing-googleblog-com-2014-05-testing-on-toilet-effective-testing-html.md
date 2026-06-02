---
source_name: "External Linked Documentation"
source_url: "https://testing.googleblog.com/2014/05/testing-on-toilet-effective-testing.html"
source_path: "sources/raw/external/testing-googleblog-com-2014-05-testing-on-toilet-effective-testing-html-b18e80b439.html"
license_ref: ""
---

Google Testing Blog: Testing on the Toilet: Effective Testing
##   Testing on the Toilet: Effective Testing  <https://testing.googleblog.com/2014/05/testing-on-toilet-effective-testing.html>
      _by Rich Martin, Zurich _
 _
_ _This article was adapted from a Google Testing on the Toilet <http://googletesting.blogspot.com/2007/01/introducing-testing-on-toilet.html> (TotT) episode. You can download a printer-friendly version <https://docs.google.com/document/d/1pb8AvYvshNRAP4x2skdd4fc0U2reCBxsMlccwEdFlFs/edit?usp=sharing> of this TotT episode and post it in your office. _

 Whether we are writing an individual unit test or designing a product’s entire testing process, it is important to take a step back and think about **how effective are our tests at detecting and reporting bugs in our code**. To be effective, there are **three important qualities** that every test should try to maximize:

 **Fidelity **

 When the code under test is broken, the test fails. **A high­-fidelity test is one which is very sensitive to defects in the code under test**, helping to prevent bugs from creeping into the code.

 Maximize fidelity by ensuring that your tests cover all the paths through your code and include all relevant assertions on the expected state.

 **Resilience **

 A test shouldn’t fail if the code under test isn’t defective. **A resilient test is one that only fails when a breaking change is made to the code under test.** Refactorings and other non-­breaking changes to the code under test can be made without needing to modify the test, reducing the cost of maintaining the tests.

 Maximize resilience by only testing the exposed API of the code under test; avoid reaching into internals. Favor stubs and fakes over mocks; don't verify interactions with dependencies unless it is that interaction that you are explicitly validating. A flaky test obviously has very low resilience.

 **Precision **

 When a test fails, **a high­-precision test tells you exactly where the defect lies**. A well­-written unit test can tell you exactly which line of code is at fault. Poorly written tests (especially large end-to-end tests) often exhibit very low precision, telling you that something is broken but not where.

 Maximize precision by keeping your tests small and tightly ­focused. Choose descriptive method names that convey exactly what the test is validating. For system integration tests, validate state at every boundary.

 These three qualities are often in tension with each other. It's easy to write a highly resilient test (the empty test, for example), but writing a test that is both highly resilient and high­-fidelity is hard. **As you design and write tests, use these qualities as a framework to guide your implementation**.

####  5 comments :

-

Point taken. Thnx
ReplyDelete <https://www.blogger.com/comment/delete/15045980/7644103653750730900>
Replies
Reply

-

FRP mantra
ReplyDelete <https://www.blogger.com/comment/delete/15045980/5263395241200956116>
Replies
Reply

-

Thanks! Very to the point.
ReplyDelete <https://www.blogger.com/comment/delete/15045980/7688154491095530072>
Replies
Reply

-

Can you expound on your statement "prefer stubs and fakes over mocks"?
ReplyDelete <https://www.blogger.com/comment/delete/15045980/631109350308963447>
Replies
-

You can read more about this here: http://googletesting.blogspot.com/2013/03/testing-on-toilet-testing-state-vs.html
Delete <https://www.blogger.com/comment/delete/15045980/5037257870070416267>
Replies
Reply

Reply

Add comment

Load more...

   _  _  <https://testing.googleblog.com/>   _  _  <https://testing.googleblog.com/2014/05/testing-on-toilet-risk-driven-testing.html>    _  _  <https://testing.googleblog.com/2014/04/testing-on-toilet-test-behaviors-not.html>

    _  _

## Feed
  <http://googletesting.blogspot.com/atom.xml>
