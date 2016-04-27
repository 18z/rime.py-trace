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
