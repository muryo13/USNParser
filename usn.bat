@echo off

# �K�v�Ȃ�v���L�V�ݒ�
#set HTTP_PROXY=http://[user]:[pw]@[proxy_server]:[port]
#set HTTPS_PROXY=http://[user]:[pw]@[proxy_server]:[port]

# �Ƃ肠�����A����1�̂ݎw��B�w�肵��USN�̏����Ƃ��Ă���
python usnparser2.py %1

python merge.py

