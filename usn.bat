@echo off

REM 
REM usn.bat
REM 
REM  usage: usn.bat usn_no ...
REM      ex) usn.bat USN-3170-2 USN-3171-1 USN-3172-1
REM

setlocal

REM �����`�F�b�N

if "%1" == "" (
    echo USN�ԍ�����ȏ�ݒ肵�Ă�������
    echo;

    echo Press any key...
    pause > nul
    goto END
)


REM �K�v�Ȃ�v���L�V�ݒ�
REM set HTTP_PROXY=http://[user]:[pw]@[proxy_server]:[port]
REM set HTTPS_PROXY=http://[user]:[pw]@[proxy_server]:[port]


REM �w�肵��USN�̏����Ƃ��Ă���

for %%f in (%*) do (
    echo %%f
    python usnparser2.py %%f
)


REM ������USN����csv�ɂ܂Ƃ߂�
python merge.py


:END
echo end

endlocal
