Google Testing Blog: Code Health: Reduce Nesting, Reduce Complexity

##   Code Health: Reduce Nesting, Reduce Complexity  <https://testing.googleblog.com/2017/06/code-health-reduce-nesting-reduce.html>
      _This is another post in our Code Health <https://testing.googleblog.com/2017/04/code-health-googles-internal-code.html> series. A version of this post originally appeared in Google bathrooms worldwide as a Google Testing on the Toilet <https://testing.googleblog.com/2007/01/introducing-testing-on-toilet.html> episode. You can download a printer-friendly version <https://docs.google.com/document/d/12VE8zEDSp5s0WZSFY7eGn91WGbUE67ASvxZmmc-yFOM/edit?usp=sharing> to display in your office. _

 By Elliott Karpilovsky

 Deeply nested code hurts readability and is error-prone.** Try spotting the bug** in the two versions of this code:

     _Code with too much nesting_ _Code with less nesting_
```go
response = server.Call(request)

if response.GetStatus() == RPC.OK:
  if response.GetAuthorizedUser():
    if response.GetEnc() == 'utf-8':
      if response.GetRows():
        vals = [ParseRow(r) for r in
                response.GetRows()]
        avg = sum(vals) / len(vals)
        return avg, vals
      else:
        raise EmptyError()
    else:
      raise AuthError('unauthorized')
  else:
    raise ValueError('wrong encoding')
else:
  raise RpcError(response.GetStatus())
```

```go
response = server.Call(request)

if response.GetStatus() != RPC.OK:
  raise RpcError(response.GetStatus())

if not response.GetAuthorizedUser():
  raise ValueError('wrong encoding')

if response.GetEnc() != 'utf-8':
  raise AuthError('unauthorized')

if not response.GetRows():
  raise EmptyError()

vals = [ParseRow(r) for r in
        response.GetRows()]
avg = sum(vals) / len(vals)
return avg, vals
```

 Answer: the "_wrong encoding"_ and "_unauthorized"_ errors are swapped. **This bug is easier to see in the refactored version, since the checks occur right as the errors are handled.**

 The refactoring technique shown above is known as **_guard clauses_**. A guard clause checks a criterion and fails fast if it is not met. It decouples the computational logic from the error logic. By removing the cognitive gap between error checking and handling, it frees up mental processing power. As a result, **the refactored version is much easier to read and maintain**.
 **
** **Here are some rules of thumb for reducing nesting in your code**:

- Keep conditional blocks short. It increases readability by keeping things local.
- Consider refactoring when your loops and branches are more than 2 levels deep.
- Think about moving nested logic into separate functions. For example, if you need to loop through a list of objects that each contain a list (such as a protocol buffer with repeated fields), you can define a function to process each object instead of using a double nested loop.
 Reducing nesting results in more readable code, which leads to discoverable bugs, faster developer iteration, and increased stability. When you can, simplify!

####  5 comments :

-

Thanks for the article. I like the example. As a rule of thumb I'd add replace conditional with polymorphism if possible.
ReplyDelete <https://www.blogger.com/comment/delete/15045980/2070069235183990629>
Replies
Reply

-

Aren't the following 2 logical checks flipped on the exceptions they should raise?

if not response.GetAuthorizedUser():
•• raise ValueError('wrong encoding')

if response.GetEnc() != 'utf-8':
•• raise AuthError('unauthorized')
ReplyDelete <https://www.blogger.com/comment/delete/15045980/3422601211037969758>
Replies
Reply

-

Regarding my logic flip comment lol. Disregard since I clearly see it was intentional after continuing with the artcile
ReplyDelete <https://www.blogger.com/comment/delete/15045980/6015931823685605036>
Replies
Reply

-

I recently refactored a too much nested logic check because I had the very impression it wasn't redeable. Glad to see that kind of article, I will keep this tip in mind.
ReplyDelete <https://www.blogger.com/comment/delete/15045980/3346426588462160196>
Replies
Reply

-

The one difference I would have is if error0 else if errorN else { success }.
Slightly easier to immediately go, ah huh, error(s) then success paths. Thanks to less whitespace + usage of else keyword.
ReplyDelete <https://www.blogger.com/comment/delete/15045980/47338031013709936>
Replies
Reply

Add comment

Load more...

   _  _  <https://testing.googleblog.com/>   _  _  <https://testing.googleblog.com/2017/06/code-health-too-many-comments-on-your.html>    _  _  <https://testing.googleblog.com/2017/05/gtac-diversity-scholarship.html>

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

-    ►     Oct  <https://testing.googleblog.com/2017/10/> (1)

-    ►     Sep  <https://testing.googleblog.com/2017/09/> (1)

-    ►     Aug  <https://testing.googleblog.com/2017/08/> (1)

-    ►     Jul  <https://testing.googleblog.com/2017/07/> (2)

-    ▼     Jun  <https://testing.googleblog.com/2017/06/> (2)
-   Code Health: Too Many Comments on Your Code Reviews?  <https://testing.googleblog.com/2017/06/code-health-too-many-comments-on-your.html>
-   Code Health: Reduce Nesting, Reduce Complexity  <https://testing.googleblog.com/2017/06/code-health-reduce-nesting-reduce.html>

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
