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
