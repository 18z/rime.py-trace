## zimedb.py

1. 在 ```__init__```時，先將 db 裡的資料以 SQL 語法寫好並放進變數中，以利後續使用。這些定義好的 SQL 語法都會給此檔中其他函式使用。例：store 函式會用到 UPDATE_PHRASE_SQL。

2. 有些 SQL 語法，例：CREATE_SETTING_TABLE_SQL 就不在 ```__init__```中，此點原因尚待調查。

3. open 函式，以 sqlite3 模組連接資料庫，並用到 CREATE_SETTING_TABLE_SQL 及 CREATE_SETTING_INDEX_SQL 兩語法。

4. delete 函式會用到 UPDATE_PHRASE_SQL，最後再呼叫 @classmethod flush。

5. list_keyword 函式用到 LIST_KEYWORDS_SQL。

6. lookup 函式用到 QUERY_PHRASE_SQL。

7. store 函式用到 PHRASE_EXIST_SQL 及 UPDATE_PHRASE_SQL, ADD_PHRASE_SQL。

8. read_config_list, read_config_value

9. read_setting_items, read_setting_list

10. UPDATE_SETTING 用到 ADD_SETTING_SQL 及 UPDATE_SETTING_SQL。

11. 可從 zimeengine.py 學如何使用 zimedb.py 中的函式，例：line 238 ```s = DB.reading_setting_items(u'Schema/')```   