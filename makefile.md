## makefile 解讀

從中觀察到兩個關鍵點

* 安裝時會先將檔案進行搬移

    ```bash
    1. 把 data, icon, engin 搬到 /usr/share/ibus-rime 底下
    2. 把 ibus-engin-rime bash 執行檔搬到 /usr/lib/ibus-rime/ 底下
    3. 把 rime.xml 搬到 /usr/share/ibus/component/ 底下

    其中 ibus-engin-rime 是搬到 makefile 中定義 libexecdir 資料夾底下。
    且查看 ibus-engin-rime 內容，為執行 main.py。
    因此推測，engin 中的 main.py 為中州韻運作時切入點(也就是追 code 切入點)。
    ```

* 匯入資料庫

    ```bash
    若輸入 make schema_zhuyin
    則會執行 cd data; python zimedb-admin.py -vi Zhuyin.txt
    推測是將 Zhuyin.txt 裡面所建立的文字資料匯入 ~/.ibus/zime/zime.db 中
    用 sqlite3 即可查看資料庫內容
    ```
