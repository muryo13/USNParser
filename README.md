# USNParser

## 必要なもの
* python 3.6.0
* beautifulsoup4 4.5.3
* urllib3 1.19.1

## インストール
まずpython for windowsを以下からインストール
https://www.python.org/downloads/

インストールしたフォルダとその下のScriptsをPathに追加
```
Path=C:\Users\murakami.ryo\AppData\Local\Programs\Python\Python36-32;C:\Users\murakami.ryo\AppData\Local\Programs\Python\Python36-32\Scripts
```

## Proxyの設定
下の2つは、`pip install urllib3`とかでインストールできる。

ただし、pipコマンドはネットワークを使うので、Proxy設定が必要。以下のサイトなどを参考に。

http://lightson.dip.jp/blog/seko/3641


## 使い方
USN-3164-1とか、USNページのタイトルを引数で指定してね。
```
usnparser.py <usn_no>
```

### 出力結果
```
d:\USNParser>usnparser.py usn-3172-1
Details:
It was discovered that Bind incorrectly handled certain malformed responsesto an
 ANY query. A remote attacker could possibly use this issue to causeBind to cras
h, resulting in a denial of service. (CVE-2016-9131)
References:
CVE-2016-9131
CVE-2016-9147
CVE-2016-9444
Medium

```
