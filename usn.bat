@echo off

# 必要ならプロキシ設定
#set HTTP_PROXY=http://[user]:[pw]@[proxy_server]:[port]
#set HTTPS_PROXY=http://[user]:[pw]@[proxy_server]:[port]

# とりあえず、引数1つのみ指定。指定したUSNの情報をとってくる
python usnparser2.py %1

python merge.py

