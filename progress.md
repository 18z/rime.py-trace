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