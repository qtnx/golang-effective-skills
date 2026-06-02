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
##  Archive
 _  _

-    ►     2026  <https://testing.googleblog.com/2026/> (5)
-    ►     May  <https://testing.googleblog.com/2026/05/> (2)

-    ►     Apr  <https://testing.googleblog.com/2026/04/> (1)

-    ►     Mar  <https://testing.googleblog.com/2026/03/> (2)

-    ►     2025  <https://testing.googleblog.com/2025/> (3)
-    ►     Oct  <https://testing.googleblog.com/2025/10/> (1)

-    ►     Sep  <https://testing.googleblog.com/2025/09/> (1)

-    ►     Jan  <https://testing.googleblog.com/2025/01/> (1)

-    ►     2024  <https://testing.googleblog.com/2024/> (13)
-    ►     Dec  <https://testing.googleblog.com/2024/12/> (1)

-    ►     Oct  <https://testing.googleblog.com/2024/10/> (1)

-    ►     Sep  <https://testing.googleblog.com/2024/09/> (1)

-    ►     Aug  <https://testing.googleblog.com/2024/08/> (1)

-    ►     Jul  <https://testing.googleblog.com/2024/07/> (1)

-    ►     May  <https://testing.googleblog.com/2024/05/> (3)

-    ►     Apr  <https://testing.googleblog.com/2024/04/> (3)

-    ►     Mar  <https://testing.googleblog.com/2024/03/> (1)

-    ►     Feb  <https://testing.googleblog.com/2024/02/> (1)

-    ►     2023  <https://testing.googleblog.com/2023/> (14)
-    ►     Dec  <https://testing.googleblog.com/2023/12/> (2)

-    ►     Nov  <https://testing.googleblog.com/2023/11/> (2)

-    ►     Oct  <https://testing.googleblog.com/2023/10/> (5)

-    ►     Sep  <https://testing.googleblog.com/2023/09/> (3)

-    ►     Aug  <https://testing.googleblog.com/2023/08/> (1)

-    ►     Apr  <https://testing.googleblog.com/2023/04/> (1)

-    ►     2022  <https://testing.googleblog.com/2022/> (2)
-    ►     Feb  <https://testing.googleblog.com/2022/02/> (2)

-    ►     2021  <https://testing.googleblog.com/2021/> (3)
-    ►     Jun  <https://testing.googleblog.com/2021/06/> (1)

-    ►     Apr  <https://testing.googleblog.com/2021/04/> (1)

-    ►     Mar  <https://testing.googleblog.com/2021/03/> (1)

-    ►     2020  <https://testing.googleblog.com/2020/> (8)
-    ►     Dec  <https://testing.googleblog.com/2020/12/> (2)

-    ►     Nov  <https://testing.googleblog.com/2020/11/> (1)

-    ►     Oct  <https://testing.googleblog.com/2020/10/> (1)

-    ►     Aug  <https://testing.googleblog.com/2020/08/> (2)

-    ►     Jul  <https://testing.googleblog.com/2020/07/> (1)

-    ►     May  <https://testing.googleblog.com/2020/05/> (1)

-    ►     2019  <https://testing.googleblog.com/2019/> (4)
-    ►     Dec  <https://testing.googleblog.com/2019/12/> (1)

-    ►     Nov  <https://testing.googleblog.com/2019/11/> (1)

-    ►     Jul  <https://testing.googleblog.com/2019/07/> (1)

-    ►     Jan  <https://testing.googleblog.com/2019/01/> (1)

-    ►     2018  <https://testing.googleblog.com/2018/> (7)
-    ►     Nov  <https://testing.googleblog.com/2018/11/> (1)

-    ►     Sep  <https://testing.googleblog.com/2018/09/> (1)

-    ►     Jul  <https://testing.googleblog.com/2018/07/> (1)

-    ►     Jun  <https://testing.googleblog.com/2018/06/> (2)

-    ►     May  <https://testing.googleblog.com/2018/05/> (1)

-    ►     Feb  <https://testing.googleblog.com/2018/02/> (1)

-    ▼     2017  <https://testing.googleblog.com/2017/> (17)
-    ►     Dec  <https://testing.googleblog.com/2017/12/> (1)

-    ►     Nov  <https://testing.googleblog.com/2017/11/> (1)

-    ▼     Oct  <https://testing.googleblog.com/2017/10/> (1)
-   Code Health: IdentifierNamingPostForWorldWideWebBlog  <https://testing.googleblog.com/2017/10/code-health-identifiernamingpostforworl.html>

-    ►     Sep  <https://testing.googleblog.com/2017/09/> (1)

-    ►     Aug  <https://testing.googleblog.com/2017/08/> (1)

-    ►     Jul  <https://testing.googleblog.com/2017/07/> (2)

-    ►     Jun  <https://testing.googleblog.com/2017/06/> (2)

-    ►     May  <https://testing.googleblog.com/2017/05/> (3)

-    ►     Apr  <https://testing.googleblog.com/2017/04/> (2)

-    ►     Feb  <https://testing.googleblog.com/2017/02/> (1)

-    ►     Jan  <https://testing.googleblog.com/2017/01/> (2)

-    ►     2016  <https://testing.googleblog.com/2016/> (15)
-    ►     Dec  <https://testing.googleblog.com/2016/12/> (1)

-    ►     Nov  <https://testing.googleblog.com/2016/11/> (2)

-    ►     Oct  <https://testing.googleblog.com/2016/10/> (1)

-    ►     Sep  <https://testing.googleblog.com/2016/09/> (2)

-    ►     Aug  <https://testing.googleblog.com/2016/08/> (1)

-    ►     Jun  <https://testing.googleblog.com/2016/06/> (2)

-    ►     May  <https://testing.googleblog.com/2016/05/> (3)

-    ►     Apr  <https://testing.googleblog.com/2016/04/> (1)

-    ►     Mar  <https://testing.googleblog.com/2016/03/> (1)

-    ►     Feb  <https://testing.googleblog.com/2016/02/> (1)

-    ►     2015  <https://testing.googleblog.com/2015/> (14)
-    ►     Dec  <https://testing.googleblog.com/2015/12/> (1)

-    ►     Nov  <https://testing.googleblog.com/2015/11/> (1)

-    ►     Oct  <https://testing.googleblog.com/2015/10/> (2)

-    ►     Aug  <https://testing.googleblog.com/2015/08/> (1)

-    ►     Jun  <https://testing.googleblog.com/2015/06/> (1)

-    ►     May  <https://testing.googleblog.com/2015/05/> (2)

-    ►     Apr  <https://testing.googleblog.com/2015/04/> (2)

-    ►     Mar  <https://testing.googleblog.com/2015/03/> (1)

-    ►     Feb  <https://testing.googleblog.com/2015/02/> (1)

-    ►     Jan  <https://testing.googleblog.com/2015/01/> (2)

-    ►     2014  <https://testing.googleblog.com/2014/> (24)
-    ►     Dec  <https://testing.googleblog.com/2014/12/> (2)

-    ►     Nov  <https://testing.googleblog.com/2014/11/> (1)

-    ►     Oct  <https://testing.googleblog.com/2014/10/> (2)

-    ►     Sep  <https://testing.googleblog.com/2014/09/> (2)

-    ►     Aug  <https://testing.googleblog.com/2014/08/> (2)

-    ►     Jul  <https://testing.googleblog.com/2014/07/> (3)

-    ►     Jun  <https://testing.googleblog.com/2014/06/> (3)

-    ►     May  <https://testing.googleblog.com/2014/05/> (2)

-    ►     Apr  <https://testing.googleblog.com/2014/04/> (2)

-    ►     Mar  <https://testing.googleblog.com/2014/03/> (2)

-    ►     Feb  <https://testing.googleblog.com/2014/02/> (1)

-    ►     Jan  <https://testing.googleblog.com/2014/01/> (2)

-    ►     2013  <https://testing.googleblog.com/2013/> (16)
-    ►     Dec  <https://testing.googleblog.com/2013/12/> (1)

-    ►     Nov  <https://testing.googleblog.com/2013/11/> (1)

-    ►     Oct  <https://testing.googleblog.com/2013/10/> (1)

-    ►     Aug  <https://testing.googleblog.com/2013/08/> (2)

-    ►     Jul  <https://testing.googleblog.com/2013/07/> (1)

-    ►     Jun  <https://testing.googleblog.com/2013/06/> (2)

-    ►     May  <https://testing.googleblog.com/2013/05/> (2)

-    ►     Apr  <https://testing.googleblog.com/2013/04/> (2)

-    ►     Mar  <https://testing.googleblog.com/2013/03/> (2)

-    ►     Jan  <https://testing.googleblog.com/2013/01/> (2)

-    ►     2012  <https://testing.googleblog.com/2012/> (11)
-    ►     Dec  <https://testing.googleblog.com/2012/12/> (1)

-    ►     Nov  <https://testing.googleblog.com/2012/11/> (2)

-    ►     Oct  <https://testing.googleblog.com/2012/10/> (3)

-    ►     Sep  <https://testing.googleblog.com/2012/09/> (1)

-    ►     Aug  <https://testing.googleblog.com/2012/08/> (4)

-    ►     2011  <https://testing.googleblog.com/2011/> (39)
-    ►     Nov  <https://testing.googleblog.com/2011/11/> (2)

-    ►     Oct  <https://testing.googleblog.com/2011/10/> (5)

-    ►     Sep  <https://testing.googleblog.com/2011/09/> (2)

-    ►     Aug  <https://testing.googleblog.com/2011/08/> (4)

-    ►     Jul  <https://testing.googleblog.com/2011/07/> (2)

-    ►     Jun  <https://testing.googleblog.com/2011/06/> (5)

-    ►     May  <https://testing.googleblog.com/2011/05/> (4)

-    ►     Apr  <https://testing.googleblog.com/2011/04/> (3)

-    ►     Mar  <https://testing.googleblog.com/2011/03/> (4)

-    ►     Feb  <https://testing.googleblog.com/2011/02/> (5)

-    ►     Jan  <https://testing.googleblog.com/2011/01/> (3)

-    ►     2010  <https://testing.googleblog.com/2010/> (37)
-    ►     Dec  <https://testing.googleblog.com/2010/12/> (3)

-    ►     Nov  <https://testing.googleblog.com/2010/11/> (3)

-    ►     Oct  <https://testing.googleblog.com/2010/10/> (4)

-    ►     Sep  <https://testing.googleblog.com/2010/09/> (8)

-    ►     Aug  <https://testing.googleblog.com/2010/08/> (3)

-    ►     Jul  <https://testing.googleblog.com/2010/07/> (3)

-    ►     Jun  <https://testing.googleblog.com/2010/06/> (2)

-    ►     May  <https://testing.googleblog.com/2010/05/> (2)

-    ►     Apr  <https://testing.googleblog.com/2010/04/> (3)

-    ►     Mar  <https://testing.googleblog.com/2010/03/> (3)

-    ►     Feb  <https://testing.googleblog.com/2010/02/> (2)

-    ►     Jan  <https://testing.googleblog.com/2010/01/> (1)

-    ►     2009  <https://testing.googleblog.com/2009/> (54)
-    ►     Dec  <https://testing.googleblog.com/2009/12/> (3)

-    ►     Nov  <https://testing.googleblog.com/2009/11/> (2)

-    ►     Oct  <https://testing.googleblog.com/2009/10/> (3)

-    ►     Sep  <https://testing.googleblog.com/2009/09/> (5)

-    ►     Aug  <https://testing.googleblog.com/2009/08/> (4)

-    ►     Jul  <https://testing.googleblog.com/2009/07/> (15)

-    ►     Jun  <https://testing.googleblog.com/2009/06/> (8)

-    ►     May  <https://testing.googleblog.com/2009/05/> (3)

-    ►     Apr  <https://testing.googleblog.com/2009/04/> (2)

-    ►     Feb  <https://testing.googleblog.com/2009/02/> (5)

-    ►     Jan  <https://testing.googleblog.com/2009/01/> (4)

-    ►     2008  <https://testing.googleblog.com/2008/> (75)
-    ►     Dec  <https://testing.googleblog.com/2008/12/> (6)

-    ►     Nov  <https://testing.googleblog.com/2008/11/> (8)

-    ►     Oct  <https://testing.googleblog.com/2008/10/> (9)

-    ►     Sep  <https://testing.googleblog.com/2008/09/> (8)

-    ►     Aug  <https://testing.googleblog.com/2008/08/> (9)

-    ►     Jul  <https://testing.googleblog.com/2008/07/> (9)

-    ►     Jun  <https://testing.googleblog.com/2008/06/> (6)

-    ►     May  <https://testing.googleblog.com/2008/05/> (6)

-    ►     Apr  <https://testing.googleblog.com/2008/04/> (4)

-    ►     Mar  <https://testing.googleblog.com/2008/03/> (4)

-    ►     Feb  <https://testing.googleblog.com/2008/02/> (4)

-    ►     Jan  <https://testing.googleblog.com/2008/01/> (2)

-    ►     2007  <https://testing.googleblog.com/2007/> (41)
-    ►     Oct  <https://testing.googleblog.com/2007/10/> (6)

-    ►     Sep  <https://testing.googleblog.com/2007/09/> (5)

-    ►     Aug  <https://testing.googleblog.com/2007/08/> (3)

-    ►     Jul  <https://testing.googleblog.com/2007/07/> (2)

-    ►     Jun  <https://testing.googleblog.com/2007/06/> (2)

-    ►     May  <https://testing.googleblog.com/2007/05/> (2)

-    ►     Apr  <https://testing.googleblog.com/2007/04/> (7)

-    ►     Mar  <https://testing.googleblog.com/2007/03/> (5)

-    ►     Feb  <https://testing.googleblog.com/2007/02/> (5)

-    ►     Jan  <https://testing.googleblog.com/2007/01/> (4)

## Feed
  <http://googletesting.blogspot.com/atom.xml>
