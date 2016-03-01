## zime.py

1. 用到 ibus 模組。

2. 用 gobject 模組。

3. 建立 ZimeEngine 類別，此類別繼承 ibus/engine.py 中的 EngineBase 類別。

4. EngineBase 類別中有許多定義好的函式，例：page_up, page_down。這兩函式，作者都做了改寫。

5. 在 backend 的地方，呼叫了 zimeengine.py 中的 Schema_Chooser 類別。是在 process_key_event 函式中用到了 zimeengine.Schema_Choose.process_key_event <- 函式。

6. 有出現  __lookup_table。猜測應是針對使用者介面做客製化調整。

7. 對於檯面下的運作，則交給 backend 去處理，例如：計算哪個字要先出現等方法。