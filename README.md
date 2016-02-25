## 中州韻輸入法研究

依照 [rime.py](https://github.com/lotem/rime.py) 安裝完成後。
/usr/share/ibus-rime 目錄檔案結構如下。

```bash
$ tree -L 2 /usr/share/ibus-rime
/usr/share/ibus-rime
├── data
│   ├── ComboPinyin.txt
│   ├── DoublePinyin.txt
│   ├── jyutping-keywords.txt
│   ├── Jyutping.txt
│   ├── make-phrases.py
│   ├── phrases.txt
│   ├── pinyin-keywords.txt
│   ├── pinyin-phrases.txt
│   ├── Pinyin.txt
│   ├── quick-keywords.txt
│   ├── Quick.txt
│   ├── schema_jyutping.bat
│   ├── schema_pinyin.bat
│   ├── schema_quick.bat
│   ├── schema_tonal_pinyin.bat
│   ├── schema_wu.bat
│   ├── schema_zhuyin.bat
│   ├── tonal-pinyin-keywords.txt
│   ├── tonal-pinyin-phrases.txt
│   ├── TonalPinyin.txt
│   ├── translate-keywords.py
│   ├── wu-extra-phrases.txt
│   ├── wu-keywords.txt
│   ├── Wu.txt
│   ├── zhuyin-keywords.txt
│   ├── zhuyin-phrases.txt
│   ├── Zhuyin.txt
│   └── zimedb-admin.py
├── engine
│   ├── algebra.py
│   ├── builder.py
│   ├── composer.py
│   ├── context.py
│   ├── core.py
│   ├── engine.py
│   ├── factory.py
│   ├── __init__.py
│   ├── main.py
│   ├── processor.py
│   ├── rime.py
│   ├── segmentation.py
│   └── storage.py
└── icons
    ├── zhung.png
    └── zhung.xcf
```

### data

假設是使用注音輸入法，則重點應該在於幾個檔案。

```
zhuyin-keywords.txt
zhuyin-phraces.txt
Zhuyin-txt
zimedb-admin.py
make-phraces.py
```

### engine

中州韻的引擎。
使用中州韻輸入法時，輸入

```bash
$ ps aux|grep ibus
deanboo+  2218  0.3  0.1 436220  5292 ?        Ssl  09:26   0:07 /usr/bin/ibus-daemon --daemonize --xim
deanboo+  2275  0.0  0.0 280880  3460 ?        Sl   09:26   0:00 /usr/lib/ibus/ibus-dconf
deanboo+  2288  0.1  0.4 489040 17876 ?        Sl   09:26   0:02 /usr/lib/ibus/ibus-ui-gtk3
deanboo+  2290  0.0  0.2 386816  9484 ?        Sl   09:26   0:00 /usr/lib/ibus/ibus-x11 --kill-daemon
deanboo+  2311  0.0  0.0 205156  3544 ?        Sl   09:26   0:00 /usr/lib/ibus/ibus-engine-simple
deanboo+  2397  0.1  0.9 114712 38952 ?        S    09:26   0:02 python /usr/share/ibus-rime/engine/main.py --ibus
deanboo+  2806  0.0  0.3 472604 13476 ?        Sl   09:29   0:00 /usr/lib/ibus/ibus-engine-chewing --ibus
deanboo+  3747  0.0  0.0  15948   920 pts/23   S+   10:01   0:00 grep ibus

推測引擎的進入點是 main.py。
```

### icon

輸入法顯示圖檔
