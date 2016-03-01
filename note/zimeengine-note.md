## zimeengine.py

1. 用了 ibus 模組中 keysyms, modifier, ascii。

2. 建立了 Engine 類別，但無繼承自其他類別。

3. 建立了 Schema_Chooser 類別，無 inherit 其他類別，但在 Schema_Chooser 中會呼叫到 Engine 類別。

4. 一旦 zimeengine.py 被使用，則會執行其中 __initialize()，該函式就是建立跟 DB 連線的 instance，```DB.open(user_db)```

5. Engine 與 Schema_Chooser 都有 process_key_event 函式。疑：zime.py 中有定義 page_up, page_down 但不曉得是何時，被何事觸發。

6. Schema_Chooser 中的 process_key_event 就是用 keycode, mask 來判斷鍵盤事件（專處理跟 Schema_Chooser 有關的 keyevent。）。

7. Engine 類別中 process_key_event 就是專門處理跟 Engine 運作有關的 keyevent。

8. 在 __initialize() 中用到 zimedb.py 進入點。

9. Engine class 中 ```__init__``` 會用到 zimecore.py 中的 Context class。

10. Engine class 中 process_key_event 用到 zimecore.py 中的 KeyEvent class。

11. Engine class 中 ```__init__``` 用到 zimecore.py 中的 Parser class。

12. Engine class 中 ```__init__``` 用到 zimecore.py 中的 Schema class。

13. Engine class 中 ```__init__``` 用到 zimemodel.py 中的 Model class。

14. zimeparser.py 中的 class 找不到進入點。猜測作者在此版中尚在測試，未正式使用，此版還是用 zimecore.py 中的 Parser class 處理。