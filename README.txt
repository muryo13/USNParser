###
### USNParser README
###

���T�v

  USN�ԍ����w�肵�A�o�b�`�t�@�C�������s���邱�Ƃ�
  �w�肵��USN�ԍ��̏ڍ׏���CSV�t�@�C���ɕۑ��ł��܂��B
  �܂��AUbuntu�Ő���p�b�P�[�W���X�g����Y�����邩�ǂ����̔�������܂��B


���t�@�C���ꗗ

  �Emerge.py              �F�t�H���_���̃t�@�C����1��csv�t�@�C���Ɍ�������
  �Epackage_list_test.txt �F�e�X�g�p�̃p�b�P�[�W�ꗗ
  �EREADME.txt            �F�{�e�L�X�g
  �Eusn.bat               �F�w�肵��(������)USN�ԍ��̏ڍׂ�1��csv�t�@�C���ɕۑ�����
                              (������usnparser.py��merge.py���Ăяo���Ă���)
  �Eusnparser.py         �F�w�肵��USN�ԍ��̏ڍׂ��擾����


�����O����

�ȉ����K�v�ł��B
�Epython 3.6.0
�Ebeautifulsoup4 4.5.3
�Eurllib3 1.19.1

�@python for windows�̃C���X�g�[��

    �ȉ�����_�E�����[�h���A�C���X�g�[������
        https://www.python.org/downloads/

    �C���X�g�[�������t�H���_�Ƃ��̉���Scripts��Path�ɒǉ�
    ex)
        C:\Users\[user]\AppData\Local\Programs\Python\Python36-32
        C:\Users\[user]\AppData\Local\Programs\Python\Python36-32\Scripts

�Abeautifulsoup4�Aurllib3�̃C���X�g�[��

    pip�R�}���h�ŃC���X�g�[�����ł���B
        pip install urllib3

    �������Apip�R�}���h�̓l�b�g���[�N���g���̂ŁAProxy�ݒ肪�K�v�B
    �ȉ��̃T�C�g�Ȃǂ��Q�l�ɁB
        http://lightson.dip.jp/blog/seko/3641

    ex)
        set HTTP_PROXY=http://[user]:[pw]@[proxy_server]:[port]
        set HTTPS_PROXY=http://[user]:[pw]@[proxy_server]:[port]

        pip install urllib3 --proxy=http://[user]:[pw]@[proxy_server]:[port]
        pip install beautifulsoup4 --proxy=http://[user]:[pw]@[proxy_server]:[port]


���g����

�@���ڃp�b�P�[�W�ꗗ�̃��X�g��p�ӂ���
    �ڍׂ�package_list_test.txt�Q��

�Ausnparser.py�̈ȉ��̕��������ɍ��킹�ĕύX����

usnparser.py
�E�E�E
##### ���ɍ��킹�Đݒ� #####

ubuntu_version = "Ubuntu 14.04 LTS"     # �Ώ�Ubuntu�o�[�W����
package_list = "package_list_test.txt"  # �p�b�P�[�W���X�g�t�@�C�����w��

##############################
�E�E�E

�BUSN�ԍ����w�肵usn.bat�����s����

    usn.bat <usn_no ...>
    ex) usn.bat USN-3170-2 USN-3171-1 USN-3172-1


�����s����

    ���s�������t�̃t�H���_�Ƀt�@�C�������������B
    �ȉ��́uusn.bat USN-3170-2 USN-3171-1 USN-3172-1�v���s����

    2017-01-26
    ��  2017-01-26.csv      ���w�肵��USN�ԍ��̏����܂Ƃ߂�csv
    ��
    ����tmp                 ����ƃt�H���_�B�eUSN�ԍ����Ƀe�L�X�g�ɂȂ��Ă���B
            USN-3170-2.txt
            USN-3171-1.txt
            USN-3172-1.txt


    2017-01-26.csv�ɂ���
    USN�ԍ����ɁA�����珇�Ɉȉ��̂悤�ɕ���ł���

        USN�ԍ�
        �����[�X��
        Ubuntu�Ώ۔Ő�
        �Ώۃp�b�P�[�W
        ���聦
        �A�b�v�f�[�g��̔Ő�
        CVE�ԍ�
        �d�v�x
        �Ǝ㐫���e�i�����j
        �i�󗓁j
        �����[�X�ڍ�URL 

        �� Ubuntu�Ő���p�b�P�[�W���X�g����Y�����邩�ǂ����̔���


�����̑�

��.py�t�@�C���ɂ���

�Eusnparser.py �F�w�肵��USN�ԍ��̏ڍׂ��擾����

    �w�肵��USN�ԍ��̏ڍׂ��擾���A�J���}��؂�̃e�L�X�g�ɕۑ�����B
    �u���t\tmp�v�t�H���_�̒��ɁuUSN�ԍ�.txt�v�̌`�ŕۑ������B

    ���s���@�F
        usnparser.py <usn_no>
        ex)
            usnparser.py USN-3170-2.txt

    �ۑ���F
        2017-01-26
        ����tmp
                USN-3170-2.txt


�Emerge.py      �F�t�H���_���̃t�@�C����1��csv�t�@�C���Ɍ�������

    �w��t�H���_�̒���tmp�t�H���_������A�����̒��Ƀt�@�C��������ꍇ�A
	tmp�t�H���_���̃t�@�C����1��csv�t�@�C���Ɍ�������B
    �w��t�H���_�̒��Ɂu���t.csv�v�̌`�ŕۑ������B
	�t�H���_���w�肵�Ȃ������ꍇ�͎��s���̓��t�̃t�H���_���w�肳���B

    ���s���@�F
        merge.py <dir>
        ex)
            merge.py D:\testdir

    �ۑ���F
        D:\testdir
�@�@    ��  2017-01-26.csv


�ȏ�
