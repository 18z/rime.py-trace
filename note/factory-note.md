## factory.py

1. 用到 ibus 模組

2. 用到 ibus/factory.py

3. EngineFactory 類別是繼承自 factory.py 中的 EngineFactoryBase 類別。

4. 在 EngineFactoryBase 類別中，可看到 create_engine 函式。中州韻改寫了該函式。

5. 自創 __config_reloaded_cb() 及 __config_value_change_cb() 兩函式，用途尚未深入理解。

在此猜測 create_engine 函式定義好後，系統會知道在何時、何處執行 create_engine 函式，以製造引擎。

製造引擎則會呼叫到下一個程式，zime.py 中的 ZimeEngine 類別。