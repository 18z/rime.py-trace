## 合抱之木生於毫末

1. 找 source code，比對[iBus Reference Manual](http://ibus.github.io/docs/ibus-1.5/IBusLookupTable.html) 裡的變數與函式。

2. 發現 [iBus Reference Manual](http://ibus.github.io/docs/ibus-1.5/IBusLookupTable.html) 與 [Python 實際程式碼](https://github.com/ibus/ibus/blob/master/ibus/lookuptable.py)中定義的函式命名有落差。例：Reference Manual 中的 ibus_lookup_table_clear () 與實際程式碼的 def clean(self):。

3. 閱讀 [iBus Reference Manual](http://ibus.github.io/docs/ibus-1.5/index.html) 中的 Overview。

4. 一般來說，輸入法開發者只需要讀前三個模組就好。

    ```
    According to the puroposes of modules, we categorized them into following parts:
    
    Panel: 
    A IBus-panel is an UI which provides UI components such as language bar, property buttons and so on.
    
    Input method engine (IME): 
    An Input method engine is an implementation of certain input method. Here lists essential classes and functions for input method engine building, such as engine specification, and class abstracts.
    
    Configuration:
    This part lists functions for configuring IBus and engines. Since most configuration files are in XML format, XML handling functions are also listed here.
    
    Communication:
    Here lists the service communication functions.
    
    Internal:
    Definition and functions for IBus internal use.
    ```
5. A IBus-panel is an UI which provides UI components such as language bar, property buttons and so on.
    
    ```
    IBus-panel 提供使用者介面，components 有 language bar, property buttons 等。
    ```

6. An Input method engine is an implementation of certain input method. Here lists essential classes and functions for input method engine building, such as engine specification, and class abstracts.

    ```
    Input method engine 就是實作特定 input method。
    此部分列出必要的 classes and functions for input method engine building。
    例如引擎規格及 class abstracts。
    ```

7. 觀察 [rime.py](https://github.com/deanboole/rime.py-trace/blob/master/ibus-rime/engine/rime.py) 與 [engine.py](https://github.com/ibus/ibus/blob/master/ibus/engine.py) 中的函式。例：update_preedit, update_preedit_text

8. 發現 [rime.py](https://github.com/deanboole/rime.py-trace/blob/a801e253353baca0fbce06b99f1aedebdd93a7c2/ibus-rime/engine/rime.py) 中的 page_up 是繼承自 [ibus/engine.py](https://github.com/ibus/ibus/blob/master/ibus/engine.py)，並利用 [ibus/lookuptable.py](https://github.com/ibus/ibus/blob/master/ibus/lookuptable.py) 進行改寫。

9. 感覺研究初期可以先關注 [rime.py](https://github.com/deanboole/rime.py-trace/blob/a801e253353baca0fbce06b99f1aedebdd93a7c2/ibus-rime/engine/rime.py) 中的函式是怎麼 implement 而非關注 [ibus/lookuptable.py](https://github.com/ibus/ibus/blob/master/ibus/lookuptable.py) 中的。

10. 試試將將 rime.py 中的 page_up, page_down 內容調換？

11. This part lists functions for configuring IBus and engines. Since most configuration files are in XML format, XML handling functions are also listed here.

    ```
    此部分列出的 functions是用來 configuring IBus 跟 engines。絕大多數的 configuration 檔案都是 XML 格式，XML handling functions 也都會被列在這裡。 
    ```

12. rime.py 中 page_up, page_down function 互換後，按鍵盤上的 page up, page down 鍵可看到更改後結果。 ```/usr/share/ibus-rime/engine/rime.py```

13. 調試 rime.py 中其他函式看看。 

14. rime.py 中 cursor_up, cursor_down function 互換後，選字時按方向鍵下 cursor 會往上，按上則往下。

15. rime.py 中，將 ```self.__page_size = storage.DB.read_setting(u'Option/PageSize') or 5``` 5 改為 10，候選字從五個改成十個。

16. rime.py 中 ```__all__ ``` 似乎與 [python 手冊 6.4.1. 小節](https://docs.python.org/2/tutorial/modules.html)中講述的不同？

17. rime.py 中，```import storage``` 是 import engine/storage.py。 

18. rime.py 中，觀察到 core, engine 都是用 ```from ... import * ```，但 storage 卻直接用 ```import```。兩種用法差別是？

19. import module，在使用 module function 時，前綴須帶 module name。例如要用到 storage.py 中的 read_setting 時，就要寫 ```storage.DB.read_setting(u'Option/PageSize')```。

20. ```from module import *``` 則是在使用 module function 時，不需要 module name 為前綴。以上例來說，可直接用 read_setting。

21. rime.py 中，class RimeSession 繼承自 [ibus.EngineBase](https://github.com/ibus/ibus/blob/0432aa66b8728bc266da3c2cca84587bc44b3557/ibus/engine.py) 與在 core.py 中定義的 class [Frontend](https://github.com/deanboole/rime.py-trace/blob/366ee52b59f796d8f42dbdc27feb19bf37eb7030/ibus-rime/engine/core.py)。

22. 下一步看的是 Class RimeSession 中的 ```def __init__(self, conn, object_path):``` 

23. 看 [python 手冊](https://docs.python.org/2/tutorial/classes.html) 逐步探索 Class 的各種問題。 

24. class variable 與 instance variable 的差別。

    ```python
    class Dog:

    kind = 'canine'         # class variable shared by all instances

    def __init__(self, name):
        self.name = name    # instance variable unique to each instance

    >>> d = Dog('Fido')
    >>> e = Dog('Buddy')
    >>> d.kind                  # shared by all dogs
    'canine'
    >>> e.kind                  # shared by all dogs
    'canine'
    >>> d.name                  # unique to d
    'Fido'
    >>> e.name                  # unique to e
    'Buddy'
    ```

25. 目標 class 中的 super，試圖理解其原理。

26. Return a proxy object that delegates method calls to a parent or sibling class of type. This is useful for accessing inherited methods that have been overridden in a class.  節錄自 [Python 手冊](https://docs.python.org/2/library/functions.html?highlight=super#super)

27. [rime.py](https://github.com/18z/rime.py-trace/blob/a801e253353baca0fbce06b99f1aedebdd93a7c2/ibus-rime/engine/rime.py) 中 ```super(RimeSession, self).__init__(conn, object_path)```，呼叫的是 ibus.EngineBase 還是 Frontend 的 ```__init__``` ?

28. 是 ibus.EngineBase 的。因為 Frontend 沒有 ```__init__```。 

29. 若有一個以上繼承，使用 super 時會呼叫哪個 class 的 ```__init__```？ 

30. 簡單實驗：結果呼叫的是 class B 的 __init__, class A 沒出現。若 class C(B, A): A, B 順序調換，則呼叫 class A 的 __init__。 

    ```python
    class A(object):
        def __init__(self):
            print "entering A"
            print "leaving A"
 
    class B(object):
        def __init__(self):
            print "entering B"
         #super(B, self).__init__()
            print "leaving B"
 
    class C(B,A):
        def __init__(self):
            print "entering c"
            super(C, self).__init__()
            print "leaving c"
 
    a = C() 
    ```

31. 看一下 [super considered super](https://rhettinger.wordpress.com/2011/05/26/super-considered-super/)。

32. If you aren’t wowed by Python’s super() builtin, chances are you don’t really know what it is capable of doing or how to use it effectively.

    ```
    若沒對 Python 的內建 super() 函式發出驚嘆，你可能還沒真正理解它的威。
    ```

33. Much has been written about super() and much of that writing has been a failure.

    ```
    針對 super() 有許多文章專門介紹，但這些文章都沒寫得很好。
    ```

34. This article seeks to improve on the situation by:

    ```
    providing practical use cases
    提供實用範例
    
    giving a clear mental model of how it works
    提供一清楚模型，解釋運作原理
    
    showing the tradecraft for getting it to work every time
    展示相關技巧，有效使用方法
    
    concrete advice for building classes that use super()
    當在 classes 中使用 super()，給予具體建議
    
    favoring real examples over abstract ABCD diamond diagrams.
    https://zh.wikipedia.org/zh-tw/%E5%A4%9A%E9%87%8D%E7%BB%A7%E6%89%BF
    多重繼承問題
    ```

35. The examples for this post are available in both Python 2 syntax and Python 3 syntax.

    ```
    文中範例皆適用於 Python 2 及 Python 3 syntax
    ```

36. Using Python 3 syntax, let’s start with a basic use case, a subclass for extending a method from one of the builtin classes:

    ```python
    class LoggingDict(dict):
        def __setitem__(self, key, value):
            logging.info('Settingto %r' % (key, value))
            super().__setitem__(key, value)
    ```
    ```
    上面是 Python 3 語法，從一個基礎的範例開始，一個 subclass 從一個 builtin class 中 extending 一個方法。
    ```

37. This class has all the same capabilities as its parent, dict, but it extends the __setitem__ method to make log entries whenever a key is updated.

    ```
    此 class 繼承自 dict，它擁有所有 dict 的 capabilities，但它延伸了 __setitem__ method，to make log entries whenever a key is updated.
    ```

38. After making a log entry, the method uses super() to delegate the work for actually updating the dictionary with the key/value pair.

    ```
    __setitem__ method 用了 super() 來 delegate 更新字典中 key/value 的工作。
    ```

39. Before super() was introduced, we would have hardwired the call with dict.__setitem__(self, key, value). 

    ```
    在 super() 出場前，我們先用 hardwired 方式呼叫 dict.__setitem__(self, key, value)。
    ```

40. However, super() is better because it is a computed indirect reference. [super ref](https://rhettinger.wordpress.com/2011/05/26/super-considered-super/)

    ```
    super() 是個間接的 reference。
    ```

41. One benefit of indirection is that we don’t have to specify the delegate class by name.

    ```
    優點就是，我們不用寫出 delegate class 的名字。
    ```

42. If you edit the source code to switch the base class to some other mapping, the super() reference will automatically follow. [super ref](https://rhettinger.wordpress.com/2011/05/26/super-considered-super/)

    ```
    如果我們使用其他的 base class，則 super() 會自動幫我們 follow。
    ```

43. You have a single source of truth: 正確代表 SomeOtherMapping

    ```python
    class LoggingDict(SomeOtherMapping):            # new base class
        def __setitem__(self, key, value):
            logging.info('Settingto %r' % (key, value))
            super().__setitem__(key, value)         # no change needed
    ```

44. In addition to isolating changes, there is another major benefit to computed indirection, one that may not be familiar to people coming from static languages. [super ref](https://rhettinger.wordpress.com/2011/05/26/super-considered-super/)

    ```
    此外，對於 computed indirection，還有一個優點是寫 static language 的人較不熟系的。
    ```

45. Since the indirection is computed at runtime, we have the freedom to influence the calculation so that the indirection will point to some other class.

    ```
    indirection 都是在 runtime 時被 computed，因此，我們可以在 runtime 時影響它，使它指向其他的 class。
    ```

46. The calculation depends on both the class where super is called and on the instance’s tree of ancestors. [super ref](https://rhettinger.wordpress.com/2011/05/26/super-considered-super/)

    ```
    此計算依據 super 是在哪被呼叫及 class 的族譜。
    ```

47. The first component, the class where super is called, is determined by the source code for that class.

    ```
    第一個 component，有呼叫 super 的 class，is determined by the source code for that class.
    說實在看不懂。
    ```
    
48. In our example, super() is called in the LoggingDict.__setitem__ method. 

    ```
    範例中，super() 在 LoggingDict.__setitem__method 中被呼叫。
    ```

49. That component is fixed. 

    ```
    該 component 是 fixed 的。
    ```

50. The second and more interesting component is variable (we can create new subclasses with a rich tree of ancestors). [super ref](https://rhettinger.wordpress.com/2011/05/26/super-considered-super/)

    ```
    第二個，更有趣的 component 就是變數 (有 rich tree of ancestors，可以 create 新的 subclasses。)
    ```

51. Let’s use this to our advantage to construct a logging ordered dictionary without modifying our existing classes:

    ```python
    class LoggingOD(LoggingDict, collections.OrderedDict):
        pass
    
    """ 我們就用這樣的優點，再不修改既有的 classes 的情況下，來建構一個 logging ordered dictionary。
    ```

52. The ancestor tree for our new class is: LoggingOD, LoggingDict, OrderedDict, dict, object. [super ref](https://rhettinger.wordpress.com/2011/05/26/super-considered-super/)

    ```
    現在新 class 的 ancestor tree 就是 LoggingOD, LoggingDict, OrderedDict, dict, object。
    ```

53. For our purposes, the important result is that OrderedDict was inserted after LoggingDict and before dict!

    ```
    我們的目的是讓 OrderedDict 在 LoggingDict 之後、dict 之前被 insert。(塞入 ancestor tree。)[super ref](https://rhettinger.wordpress.com/2011/05/26/super-considered-super/)
    ```

54. This means that the super() call in LoggingDict.__setitem__ now dispatches the key/value update to OrderedDict instead of dict. [super ref](https://rhettinger.wordpress.com/2011/05/26/super-considered-super/)

    ```
    這表示 LoggingDict.__setitem__ 現在動到的是 OrderedDict 的值而非 dict 的值。
    ```
    
55. Think about that for a moment.

    ```
    請稍微想一下。
    ```
    
56. We did not alter the source code for LoggingDict.

    ```
    我們並無修改 LoggingDict 的原始碼。
    ```

57. Instead we built a subclass whose only logic is to compose two existing classes and control their search order.[super ref](https://rhettinger.wordpress.com/2011/05/26/super-considered-super/)

    ```
    我們做的就是建立一個 subclass，目的在修改兩個既有 classes 並控制他們的搜尋 order。
    ```

58. What I’ve been calling the search order or ancestor tree is officially known as the Method Resolution Order or MRO. 

    ```
    這種呼叫 search order 的方法或者是 ancestor tree，官方稱為 Method Resolution Order (MRO)。
    ```

59. It’s easy to view the MRO by printing the __mro__ attribute

    ```python
    可藉由 printing __mro__ 來看順序。
    >>> pprint(LoggingOD.__mro__)
    (<class '__main__.LoggingOD'>,
    <class '__main__.LoggingDict'>,
    <class 'collections.OrderedDict'>,
    <class 'dict'>,
    <class 'object'>)
    ```

60. If our goal is to create a subclass with an MRO to our liking, we need to know how it is calculated. [super ref](https://rhettinger.wordpress.com/2011/05/26/super-considered-super/)

    ```
    若我們想用 MRO，就必須了解它是如何被計算的。
    ```

61. The basics are simple.

    ```
    其實很簡單。
    ```
    
62. The sequence includes the class, its base classes, and the base classes of those bases and so on until reaching object which is the root class of all classes.

    ```
    順序就是 class，其 base classes，base classes 的 bases，直到 object (root class)。
    ```

63. The sequence is ordered so that a class always appears before its parents, and if there are multiple parents, they keep the same order as the tuple of base classes.

    ```
    這樣就讓 class 總是在其 parents class 之前，且若有多個 parents，they keep the same order as the tuple of base clasees。
    ```

64. The MRO shown above is the one order that follows from those constraints: [super ref](https://rhettinger.wordpress.com/2011/05/26/super-considered-super/)

    ```
    MRO order 有下列限制：
    LoggingOD precedes its parents, LoggingDict and OrderedDict
    LoggingDict precedes OrderedDict because LoggingOD.__bases__ is (LoggingDict, OrderedDict)
    LoggingDict precedes its parent which is dict
    OrderedDict precedes its parent which is dict
    dict precedes its parent which is object
    ```

65. The process of solving those constraints is known as linearization.

    ```
    處理 contraints 的方法就是線性化。
    ```
