###
### USNParser README
###

■概要

  USN番号を指定し、バッチファイルを実行することで
  指定したUSN番号の詳細情報をCSVファイルに保存できます。
  また、Ubuntu版数やパッケージリストから該当するかどうかの判定もします。


■ファイル一覧

  ・merge.py              ：フォルダ内のファイルを1つのcsvファイルに結合する
  ・package_list_test.txt ：テスト用のパッケージ一覧
  ・README.txt            ：本テキスト
  ・usn.bat               ：指定した(複数の)USN番号の詳細を1つのcsvファイルに保存する
                              (内部でusnparser.pyとmerge.pyを呼び出している)
  ・usnparser.py         ：指定したUSN番号の詳細を取得する


■事前準備

以下が必要です。
・python 3.6.0
・beautifulsoup4 4.5.3
・urllib3 1.19.1

①python for windowsのインストール

    以下からダウンロードし、インストールする
        https://www.python.org/downloads/

    インストールしたフォルダとその下のScriptsをPathに追加
    ex)
        C:\Users\[user]\AppData\Local\Programs\Python\Python36-32
        C:\Users\[user]\AppData\Local\Programs\Python\Python36-32\Scripts

②beautifulsoup4、urllib3のインストール

    pipコマンドでインストールができる。
        pip install urllib3

    ただし、pipコマンドはネットワークを使うので、Proxy設定が必要。
    以下のサイトなどを参考に。
        http://lightson.dip.jp/blog/seko/3641

    ex)
        set HTTP_PROXY=http://[user]:[pw]@[proxy_server]:[port]
        set HTTPS_PROXY=http://[user]:[pw]@[proxy_server]:[port]

        pip install urllib3 --proxy=http://[user]:[pw]@[proxy_server]:[port]
        pip install beautifulsoup4 --proxy=http://[user]:[pw]@[proxy_server]:[port]


■使い方

①搭載パッケージ一覧のリストを用意する
    詳細はpackage_list_test.txt参照

②usnparser.pyの以下の部分を環境に合わせて変更する

usnparser.py
・・・
##### 環境に合わせて設定 #####

ubuntu_version = "Ubuntu 14.04 LTS"     # 対象Ubuntuバージョン
package_list = "package_list_test.txt"  # パッケージリストファイルを指定

##############################
・・・

③USN番号を指定しusn.batを実行する

    usn.bat <usn_no ...>
    ex) usn.bat USN-3170-2 USN-3171-1 USN-3172-1


■実行結果

    実行した日付のフォルダにファイルが生成される。
    以下は「usn.bat USN-3170-2 USN-3171-1 USN-3172-1」実行結果

    2017-01-26
    │  2017-01-26.csv      ←指定したUSN番号の情報をまとめたcsv
    │
    └─tmp                 ←作業フォルダ。各USN番号毎にテキストになっている。
            USN-3170-2.txt
            USN-3171-1.txt
            USN-3172-1.txt


    2017-01-26.csvについて
    USN番号毎に、左から順に以下のように並んでいる

        USN番号
        リリース日
        Ubuntu対象版数
        対象パッケージ
        判定※
        アップデート後の版数
        CVE番号
        重要度
        脆弱性内容（原文）
        （空欄）
        リリース詳細URL 

        ※ Ubuntu版数やパッケージリストから該当するかどうかの判定


■その他

□.pyファイルについて

・usnparser.py ：指定したUSN番号の詳細を取得する

    指定したUSN番号の詳細を取得し、カンマ区切りのテキストに保存する。
    「日付\tmp」フォルダの中に「USN番号.txt」の形で保存される。

    実行方法：
        usnparser.py <usn_no>
        ex)
            usnparser.py USN-3170-2.txt

    保存先：
        2017-01-26
        └─tmp
                USN-3170-2.txt


・merge.py      ：フォルダ内のファイルを1つのcsvファイルに結合する

    指定フォルダの中にtmpフォルダがあり、かつその中にファイルがある場合、
	tmpフォルダ内のファイルを1つのcsvファイルに結合する。
    指定フォルダの中に「日付.csv」の形で保存される。
	フォルダを指定しなかった場合は実行時の日付のフォルダが指定される。

    実行方法：
        merge.py <dir>
        ex)
            merge.py D:\testdir

    保存先：
        D:\testdir
　　    └  2017-01-26.csv


以上
