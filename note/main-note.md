## main.py

1. 有 import ibus 模組。

2. 用了 main 函式。

函式內功能有：

1. 用 getopt 來接收參數，並做出相對動作。

2. 最後執行 IMApp.run()，IMApp() 為 main.py 中自定義的 class。該 class 無繼承 ibus 中的類別。

IMApp 類別中，初始化時就會先做：

1. 用 ibus component 填入輸入法相關資訊。

2. 用 ibus component.add_engine 填入 engine 相關資訊。

3. 用 gobject 模組。

4. 用 enginefactory 製造輸入法引擎。

5. 定義類別函式，讓 gobject.mainloop 跑起來。

6. 定義類別函式，讓 gobject.mainloop 停止。

初始化時 ```__init__``` 內的 code 就會被執行。

猜測因而在類別被使用時， engine 就會被 factory 製造了 ```factory.EngineFactory(ibus.Bus())```

查看 ibus github 中的 ibus/bus.py 就可看到 Bus 類別。類別內容之後再深入探討。