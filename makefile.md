## makefile 解讀

從中觀察到兩個關鍵點

* 安裝時會先將檔案進行搬移

    ```bash
    1. 把 data, icon, engin 搬到 /usr/share/ibus-zime 底下
    2. 把 ibus-engin-zime bash 執行檔搬到 /usr/lib/ibus/ibus-engine-zime 底下
    3. 把 rime.xml 搬到 /usr/share/ibus/component/ 底下

    其中 ibus-engin-zime 是搬到 makefile 中定義 libexecdir 資料夾底下。
    且查看 ibus-engin-zime 內容，為執行 main.py。
    因此推測，engin 中的 main.py 為中州韻運作時切入點(也就是追 code 切入點)。
    ```

* 匯入資料庫

    ```bash
    cd data; ./create-schema.py zhuyin-schema.txt zhuyin-keywords.txt zhuyin-phrases.txt
    推測是將 *.txt 裡面所建立的文字資料匯入 ~/.ibus/zime/zime.db 中
    用 sqlite3 即可查看資料庫內容
    ```
