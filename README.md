## 中州韻奇幻旅程 - 中州韻輸入法研究

注意：以下筆記根據 rime.py 中 0c3be 版本所作。

依照 [rime.py](https://github.com/lotem/rime.py/tree/0c3be786d9d73de0956e884d7616b477df559015) 安裝完成後。
/usr/share/ibus-zime 目錄檔案結構如下。

```bash
$ tree -L 2 /usr/share/ibus-zime/
/usr/share/ibus-zime/
├── data
│   ├── combo-pinyin-schema.txt
│   ├── create-schema.py
│   ├── jyutping-keywords.txt
│   ├── jyutping-schema.txt
│   ├── make-phrases.py
│   ├── phrases.txt
│   ├── pinyin-keywords.txt
│   ├── pinyin-phrases.txt
│   ├── pinyin-schema.txt
│   ├── test-keywords.txt
│   ├── test-schema.txt
│   ├── zhung-keywords.txt
│   ├── zhung-schema.txt
│   ├── zhuyin-keywords.txt
│   ├── zhuyin-phrases.txt
│   ├── zhuyin-schema.txt
│   └── zhuyin-to-pinyin.py
├── engine
│   ├── factory.py
│   ├── main.py
│   ├── stylo
│   ├── test.py
│   └── zime.py
└── icons
    ├── chinese.svg
    ├── english.svg
    ├── full-letter.svg
    ├── full-punct.svg
    ├── half-letter.svg
    ├── half-punct.svg
    └── zhung.png
```

### data

假設是使用注音輸入法，則重點應該在於幾個檔案。

```
create-schema.py
zhuyin-schema.txt
zhuyin-keywords.txt
zhuyin-phrases.txt
```

### engine

中州韻的引擎。
使用中州韻輸入法時，輸入

```bash
$ ps aux|grep ibus
amtb      1636  0.8  0.4 303676  9380 ?        Ssl  13:51   0:03 /usr/bin/ibus-daemon --daemonize --xim
amtb      1672  0.0  0.3 296040  7968 ?        Sl   13:51   0:00 /usr/lib/ibus/ibus-dconf
amtb      1675  0.3  1.5 493484 30852 ?        Sl   13:51   0:01 /usr/lib/ibus/ibus-ui-gtk3
amtb      1680  0.0  0.7 397020 15380 ?        Sl   13:51   0:00 /usr/lib/ibus/ibus-x11 --kill-daemon
amtb      1818  0.1  0.4 220184  9872 ?        Sl   13:51   0:00 /usr/lib/ibus/ibus-engine-simple
amtb      1878  0.1  1.2 482424 26424 ?        Sl   13:51   0:00 /usr/lib/ibus/ibus-engine-chewing --ibus
amtb      2949  0.1  0.8  89432 16876 ?        S    13:56   0:00 python /usr/share/ibus-zime/engine/main.py --ibus
amtb      3039  0.0  0.1  15976  2172 pts/23   S+   13:59   0:00 grep ibus

推測引擎的進入點是 main.py。
```

### icon

輸入法顯示圖檔
