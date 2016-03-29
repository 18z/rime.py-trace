1. 找 source code，比對[iBus Reference Manual](http://ibus.github.io/docs/ibus-1.5/IBusLookupTable.html) 裡的變數與函式。

2. 發現 [iBus Reference Manual](http://ibus.github.io/docs/ibus-1.5/IBusLookupTable.html) 與 [Python 實際程式碼](https://github.com/ibus/ibus/blob/master/ibus/lookuptable.py)中定義的函式命名有落差。例：Reference Manual 中的 ibus_lookup_table_clear () 與實際程式碼的 def clean(self):。
