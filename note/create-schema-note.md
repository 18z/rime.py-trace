## create-schema.py

```
▶ imports

 -__split : function

 +add_phrase : function

 +debug : function

 +join_phrase : function

 +process_phrase : function

 +query_keyword : function

 +split_phrase : function

▼ variables
    conn
    db_file
    delim
    delim
    delim
    equal_sign
    f
    f
    f
    freq
    keyword_file
    keyword_map
    m
    parser
    phrase_counter
    phrase_file
    prefix
    prefix
    prefix_args
    schema
    schema
    schema_file
    usage
    word
    x
    x
    x
```

1.  在 split_phrase 函式中用到 __split 函式 (相互使用)

2.  add_phrase 函式中用到

    ```
    QUERY_PHRASE_SQL
    UPDATE_PHRASE_SQL
    ADD_PHRASE_SQL
    ```

3.  debug 感覺是做字元除錯的。

4.  query_keyword 函式中用到

    ```
    QUERY_KEYWORD_SQL
    ```

5.  在 option 程式碼後，連線至 db，並執行 CREATE_SETTING_TABLE_SQL, CREATE_SETTING_INDEX_SQL。

6.  if schema_file 用到

    ```
    CLEAR_SCHEMA_SETTING_SQL
    ADD_SETTING_SQL
    ```

7.  if not options.keep 用到

    ```
    DROP_KEYWORD_INDEX_SQL
    DROP_PHRASE_INDEX_SQL
    DROP_KEYWORD_TABLE_SQL
    DROP_PHRASE_TABLE_SQL
    ```

8.  程式直接執行

   ```
    CREATE_KEYWORD_TABLE_SQL
    CREATE_PHRASES_TABLE_SQL
    CREATE_KEYWORD_INDEX_SQL
    CREATE_PHRASE_INDEX_SQL
   ```

9.  line 190 ~ 194

    ```
    SQL %= prefix_args
    ```

10. if keyword.file 用到

    ```
    ADD_KEYWORD_SQL
    ```
