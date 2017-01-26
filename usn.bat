@echo off

REM 
REM usn.bat
REM 
REM  usage: usn.bat usn_no ...
REM      ex) usn.bat USN-3170-2 USN-3171-1 USN-3172-1
REM

setlocal

REM 引数チェック

if "%1" == "" (
    echo USN番号を一つ以上設定してください
    echo;

    echo Press any key...
    pause > nul
    goto END
)


REM 必要ならプロキシ設定
REM set HTTP_PROXY=http://[user]:[pw]@[proxy_server]:[port]
REM set HTTPS_PROXY=http://[user]:[pw]@[proxy_server]:[port]


REM 指定したUSNの情報をとってくる

for %%f in (%*) do (
    echo %%f
    python usnparser2.py %%f
)


REM 複数のUSN情報をcsvにまとめる
python merge.py


:END
echo end

endlocal
