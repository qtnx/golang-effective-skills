---
source_name: "External Linked Documentation"
source_url: "https://testing.googleblog.com/2013/03/testing-on-toilet-testing-state-vs.html"
source_path: "sources/raw/external/testing-googleblog-com-2013-03-testing-on-toilet-testing-state-vs-html-d3cdd73eda.html"
license_ref: ""
---

Google Testing Blog: Testing on the Toilet: Testing State vs. Testing Interactions
##   Testing on the Toilet: Testing State vs. Testing Interactions  <https://testing.googleblog.com/2013/03/testing-on-toilet-testing-state-vs.html>
      _By Andrew Trenk_
 _This article was adapted from a Google Testing on the Toilet <http://googletesting.blogspot.com/2007/01/introducing-testing-on-toilet.html> (TotT) episode. You can download a printer-friendly version of this TotT episode and post it in your office._

 There are typically two ways a unit test can verify that the code under test is working properly: by testing state or by testing interactions. What’s the difference between these?

 **Testing state means you're verifying that the code under test returns the right results.**

```go
public void testSortNumbers() {
  NumberSorter **numberSorter** = new NumberSorter(**quicksort, bubbleSort**);
  // Verify that the returned list is sorted. It doesn't matter which sorting
  // algorithm is used, as long as the right result is returned.
  assertEquals(
      new ArrayList(1, 2, 3),
      **numberSorter**.sortNumbers(new ArrayList(3, 1, 2)));
}
```
 **Testing interactions means you're verifying that the code under test calls certain methods properly.**

```go
public void **testSortNumbers_quicksortIsUsed**() {
  // Pass in mocks to the class and call the method under test.
  NumberSorter **numberSorter** = new NumberSorter(**mockQuicksort, mockBubbleSort**);
  **numberSorter**.sortNumbers(new ArrayList(3, 1, 2));
  // Verify that numberSorter.sortNumbers() used quicksort. The test should
  // fail if mockQuicksort.sort() is never called or if it's called with the
  // wrong arguments (e.g. if mockBubbleSort is used to sort the numbers).
  verify(**mockQuicksort**).sort(new ArrayList(3, 1, 2));
}
```
 The second test may result in good code coverage, but it doesn't tell you whether sorting works properly, only that quicksort.sort() was called. **Just because a test that uses interactions is passing doesn't mean the code is working properly**. This is why **in most cases, you want to test state, not interactions.**
 In general, **interactions should be tested when correctness doesn't just depend on what the code's output is, but also how the output is determined**. In the above example, you would only want to test interactions in addition to testing state if it's important that quicksort is used (e.g. the method would run too slowly with a different sorting algorithm), otherwise the test using interactions is unnecessary.

 **What are some other examples of cases where you want to test interactions?**
 - **The code under test calls a method where differences in the number or order of calls would cause undesired behavior**, such as side effects (e.g. you only want one email to be sent), latency (e.g. you only want a certain number of disk reads to occur) or multithreading issues (e.g. your code will deadlock if it calls some methods in the wrong order). Testing interactions ensures that your tests will fail if these methods aren't called properly.
 - **You're testing a UI where the rendering details of the UI are abstracted away from the UI logic** (e.g. using MVC or MVP). In tests for your controller/presenter, you only care that a certain method of the view was called, not what was actually rendered, so you can test interactions with the view. Similarly, when testing the view, you can test interactions with the controller/presenter.

####  6 comments :

-

Always good to see more TotT!

Maybe it's too obvious to be mentioned, but you also want to test interactions when the targets of those interactions are not suitable for access during a test. That is, if they would be too slow, return inconsistent results, or perhaps are simply inaccessible from your test environment (this last comes up less with unit tests). Oh, and of course when you need to simulate failure cases during the interactions.

Regardless, I think your point is well taken that you should be verifying state regardless. Even when you are mocking out all interactions, you need to ensure that the code under test properly handles the results of those interactions.
ReplyDelete <https://www.blogger.com/comment/delete/15045980/7092765062252452238>
Replies
Reply

-

State testing, as you stated, is good for validating the results, often of some function or calculation. State testing is also good for validating edge cases and exceptions (divide by 0).

Interaction testing is good to validate business logic and usage requirements. For example, if a user is added to the system, was a welcoming email sent. Sure, I could mock an SMTP server and test the state of the queue... I could just as easily shim/stub the method for sending email, and validate that it was called.

see more: http://www.sbrickey.com/Tech/Blog/Post/Why_We_Test
ReplyDelete <https://www.blogger.com/comment/delete/15045980/5670810965506464480>
Replies
Reply

-

Hi, Andrew

Thanks for the article. The one thing I personally cannot agree with is the statement that in most cases we need to test state, not interactions.

Where I work, we do a lot of message processing, where there's very little state (the state is transient an held in a message itself that passes through system and is processed in the meantime). As a result, at most of our objects don't hold state directly. Their only "state" are references to their collaborators with whom they exchange messages with. Their responsibilities is to receive messages (i.e. methods are called on them) and send messages (i.e. invoke methods on other objects). This makes 90% of our tests to be "interaction tests" while having ca. 70% of our methods not even returning any values to assert on.

Anyway, about your example - I'd probably write a test for a rule saying when bubble sort is chosen and when quick sort, but I'd still write a test for each sorting algorithm the same way you wrote the first one (state based). So, the two examples shown are not really alternatives in my mind - the first one specifies what the output of sorting should be, and the second one I'd write earlier to specify when which method should be chosen. Note that if you tested a logic where two sorting algorithms can be chosen and wrote only tests such as the first one, you could actually remove the choice between bubble sort and quick sort and leave just one algorithm - the tests would pass anyway, because each algorithm gives the same end result and this result is the only thing you're asserting.
ReplyDelete <https://www.blogger.com/comment/delete/15045980/56522396319639056>
Replies
Reply

-

Great post! And the example is also subtly great.

"Interaction testing" is also the only way when you want to test a framework whose components (real workers) are pluggable. Because you want to test the framework but not the components, so the state is meaningless, only the execution process of the framework is meaningful.
ReplyDelete <https://www.blogger.com/comment/delete/15045980/8686162138634325451>
Replies
Reply

-

Love this post. This topic of discussion seems to fall in with the Classical TDD vs Behavioral TDD debate, and I've thought that that argument usually just boiled down to what your post is about, testing state vs testing interactions.

When testing layers that don't make direct calls to the database, but perform them through data access objects, I usually mock them out to gain all the benefits of speed, reliability, and nimbleness (in terms of what branch statements I can hit) of unit tests. However, sometimes I wonder if it's better to just let those hit the database.
ReplyDelete <https://www.blogger.com/comment/delete/15045980/8329270615202180451>
Replies
Reply

-

" Testing state means you're verifying that the code under test returns the right results. "

This is misleading as objects communicates with other objects by sending objects (states). A unit test should also check those sent objects in order for the unit test to be correct and complete.
ReplyDelete <https://www.blogger.com/comment/delete/15045980/195564871463616511>
Replies
Reply

Add comment

Load more...

   _  _  <https://testing.googleblog.com/>   _  _  <https://testing.googleblog.com/2013/04/two-new-videos-about-testing-at-google.html>    _  _  <https://testing.googleblog.com/2013/03/announcing-gtac-2013-agenda.html>

    _  _

## Feed
  <http://googletesting.blogspot.com/atom.xml>
