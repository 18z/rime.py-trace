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
