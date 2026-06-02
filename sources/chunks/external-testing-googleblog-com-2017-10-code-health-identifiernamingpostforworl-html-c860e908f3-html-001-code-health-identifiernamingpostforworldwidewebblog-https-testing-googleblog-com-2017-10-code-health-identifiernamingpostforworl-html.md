---
source_name: "External Linked Documentation"
source_url: "https://testing.googleblog.com/2017/10/code-health-identifiernamingpostforworl.html"
source_path: "sources/raw/external/testing-googleblog-com-2017-10-code-health-identifiernamingpostforworl-html-c860e908f3.html"
license_ref: ""
---

Google Testing Blog: Code Health: IdentifierNamingPostForWorldWideWebBlog
##   Code Health: IdentifierNamingPostForWorldWideWebBlog  <https://testing.googleblog.com/2017/10/code-health-identifiernamingpostforworl.html>

  This is another post in our Code Health <https://testing.googleblog.com/2017/04/code-health-googles-internal-code.html> series. A version of this post originally appeared in Google bathrooms worldwide as a Google Testing on the Toilet <https://testing.googleblog.com/2007/01/introducing-testing-on-toilet.html> episode. You can download a printer-friendly version <https://docs.google.com/document/d/1pwxIjkmwwGjpCF9CjeWxMoNtqAs0aXLkwfen5MTTPAs/edit?usp=sharing> to display in your office.

  By Chris Lewis and Bob Nystrom

  It's easy to get carried away creating long identifiers. Longer names often make things more readable. But names that are too long can decrease readability. There are many examples of variable names longer than 60 characters on GitHub and elsewhere. In 58 characters, we managed this haiku for you to consider:

   Name variables
   Using these simple guidelines
   Beautiful source code

  Names should be two things: clear (know what it refers to) and precise (know what it does not refer to). Here are some guidelines to help:

  • Omit words that are obvious given a variable's type declaration.

```go
// Bad, the type tells us what these variables are:
String nameString; List<datetime> holidayDateList;
// Better:
String name; List<datetime> holidays;

```

  • Omit irrelevant details.

```go
// Overly specific names are hard to read:
Monster finalBattleMostDangerousBossMonster; Payments nonTypicalMonthlyPayments;
// Better, if there's no other monsters or payments that need disambiguation:
Monster boss; Payments payments;

```

  • Omit words that are clear from the surrounding context.

```go
// Bad, repeating the context:
class AnnualHolidaySale {int annualSaleRebate; boolean promoteHolidaySale() {...}}
// Better:
class AnnualHolidaySale {int rebate; boolean promote() {...}}

```

 • Omit words that could apply to any identifier.
 You know the usual suspects: data, state, amount, number, value, manager, engine, object, entity, instance, helper, util, broker, metadata, process, handle, context. Cut them out.

 There are some exceptions to these rules; use your judgment. Names that are too long are still better than names that are too short. However, following these guidelines, your code will remain unambiguous and be much easier to read. Readers, including "future you,” will appreciate how clear your code is!

####  6 comments :

-

Hi,

I'm curious if there is/are tool/s that check (at least with warning) for too long variables names. What could be even better is another check (simple regex on variables would be sufficient) for "clue" words that author pointed in article. So did any one found tool that is able to do that?

Bests,
Alex
ReplyDelete <https://www.blogger.com/comment/delete/15045980/7684249877093158366>
Replies
-

For Java, PMD or Checkstyle will help:
 - http://pmd.sourceforge.net/pmd-4.3.0/rules/naming.html
 - http://checkstyle.sourceforge.net/config_naming.html#Content

The former has a rule that reports long names, the latter might require to specify your rule as a regular expression.
Delete <https://www.blogger.com/comment/delete/15045980/2784976123798041472>
Replies
Reply

Reply

-

It's a good approach to omit types in variable names, but don't you think that the example with Date and generally Date suffix is a special case ?

Date is a natural part of English and as an example when we talk about a book we say "publish date". Would be strange to have a class Book with getPublish method instead of getPublishDate. And it seems the case is the same for holiday dates.
ReplyDelete <https://www.blogger.com/comment/delete/15045980/1817847045410780532>
Replies
Reply

-

I would expand the first rule to "avoid duplicating information from type/access declaration". E.g. `abstract class AbstractSomething {}` is better to be just named `class Something{}` and there is o need to rename it once you realize it cannot be abstract anymore.
ReplyDelete <https://www.blogger.com/comment/delete/15045980/3706992262093664843>
Replies
Reply

-

An example of making names longer to make better code: the video game League of Legends has an internal API method named GetElapsedFrameTimeSecs(). It replaced GetTime(), which wasn't precise, because there is no information scent on:
- whether the unit is seconds, or milliseconds;
- whether the time flows during simulation, or is quantized to simulation ticks;
- and whether the time is relative to last simulation tick, or some epoch like process start.

https://engineering.riotgames.com/news/determinism-league-legends-unified-clock
ReplyDelete <https://www.blogger.com/comment/delete/15045980/1913028702075298808>
Replies
-

See also https://testing.googleblog.com/2017/11/obsessed-with-primitives.html

Using wrapping types like Duration/TimeDelta/TimeTicks can represent this information, and make correct usage statically checkable.

https://codesearch.chromium.org/chromium/src/base/time/time.h
https://github.com/abseil/abseil-cpp/blob/master/absl/time/time.h
Delete <https://www.blogger.com/comment/delete/15045980/1877435570612971649>
Replies
Reply

Reply

Add comment

Load more...

   _  _  <https://testing.googleblog.com/>   _  _  <https://testing.googleblog.com/2017/11/obsessed-with-primitives.html>    _  _  <https://testing.googleblog.com/2017/09/code-health-providing-context-with.html>

    _  _

## Feed
  <http://googletesting.blogspot.com/atom.xml>
