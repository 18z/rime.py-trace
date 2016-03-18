## zimemodel.py

```
" Press <F1>, ? for help

▼ Model : class
   -__add_candidate : function
  ▼-__calculate : function
     +update_sugg : function
   -__concatenated : function
   +__init__ : function
   -__invalidate_selections : function
   -__memorize : function
   +delete_phrase : function
  ▼+learn : function
     +check_new_word : function
   +select : function
   +update : function

▼ variables
    join_phrase
    split_phrase
```

定義了 Model 類別，無繼承自其他類別。

1. 初始化時沒做事。

2. 有十一個類別中函式，詳參閱上圖。

3. 在 update 函式中用到

    ```
    __invalidate_selections()
    splite_phrase (lambdb
    __concatenated()
    __add_candidate()
    ```
4. 在 select 函式中用到

    ```
    __invalidate_selections()
    __calculate()
    ```

5. 在 learn 函式中用到

    ```
    __memorize()
    ```

6. 在 delete_phrase 函式中用到

    ```
    join_phrase (lambda
    ```

7. 推測：函式前有雙底線者，為供函式使用之函式。

8. 函式幾乎都會用到 db。

9. splite_phrase 及 join_phrase 兩變數值都是經過 lambda 處理過的。

