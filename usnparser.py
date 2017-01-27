#coding: UTF-8

#
#  usnparser2.py
#
#   usage: usnparser2.py usn_no
#       ex) usnparser2.py USN-3172-1
#

import sys
import urllib.request
from bs4 import BeautifulSoup

import os
import shutil
import datetime


##### 環境に合わせて設定 #####

ubuntu_version = "Ubuntu 14.04 LTS"     # 対象Ubuntuバージョン
package_list = "package_list_test.txt"  # パッケージリストファイルを指定

##############################

usn_url = "https://www.ubuntu.com/usn/"
usn_default_no = 'USN-3172-1'  # USN番号を指定
usn_sample_html = 'ubuntu.html'

topdir = os.getcwd()

detail_text=' The problem can be corrected by updating your system to the following\npackage version:'

# soupを取得
def get_soup(target):
    soup = 0
    if 'http' in target:
        # USNサイトからhtmlを取得
        html = urllib.request.urlopen(target).read()
        # HTML解析
        soup = BeautifulSoup(html, "html.parser")
    else:
        html = open(target, 'r').read()
        soup = BeautifulSoup(html, "html.parser")
    return soup

# RefernecesのCVE優先度を取得する
def get_cve_priority(href):
    soup = get_soup(href)
    # 最初のfieldクラスがPriority
#    return soup.find_all("div", "medium-value")[0].text

    for div in soup.find_all('div'):
        title = div.text
        if title == 'Priority':
            priority=div.find_next_sibling('div').text
            #print(priority)  #for debug
    return priority

# 一番高いレベルのPriorityを返す
def get_hieghest_priority(priorities):
    if 'High' in priorities:
        return '高'
    elif 'Medium' in priorities:
        return '中'
    elif 'Low' in priorities:
        return '低'
    else:
        return 'None'

# 日付変換
def convert_date_format(datestr):

    # 序数表記削除    
    if '1st' in datestr:
        datestr = datestr.replace("1st","1")
    elif 'nd' in datestr:
        datestr = datestr.replace("nd","")
    elif 'rd' in datestr:
        datestr = datestr.replace("rd","")
    elif 'th' in datestr:
        datestr = datestr.replace("th","")

    # 文字列→日付
    tmpdate = datetime.datetime.strptime(datestr, '%d %B, %Y')
    # 日付→文字列
    datestr = tmpdate.strftime("%Y/%m/%d")   

    return datestr

# アップデート対象かどうかを判定
def is_supported(usndir):

    ret = False
    f = open(usndir + "Ubuntu_version.txt",'r')
    u_ver = f.readlines()
    f.close()

    # Ubuntuバージョンチェック
    if ubuntu_version + '\n' in u_ver:
        ret = True
    else:
        return ret    # False

    # 搭載パッケージチェック
    f = open(topdir + '\\' + package_list ,'r')
    p_list = f.readlines()     # 搭載パッケージリスト取得
    f.close()
  
    f = open(usndir + "Package.txt",'r')
    u_list = f.readlines()    # アップデートパッケージリスト取得
    f.close()

    for update_package in u_list:
        if update_package in p_list:
            ret = True
            break
        else:
            ret = False

    return ret


# ファイルリストの順にファイルをカンマ区切りで内容をstrに結合
def marge_files(usn_no, dirname, filelist):

    csvstr = usn_no+ ","
    for filename in filelist:
        csvstr = csvstr + '"'

        if filename != "":
            f = open(dirname + filename,'r')
            lines2 = f.readlines()
            f.close()
            for line in lines2:
                 csvstr = csvstr +line

        csvstr = csvstr[:-1]
        csvstr = csvstr + '"' + ','

    return csvstr


# main
if __name__ == '__main__':
    args = sys.argv
    usn_no = usn_default_no
    if len(args) > 1:
        usn_no = args[1]
    soup = get_soup(usn_url + usn_no)
    #soup = get_soup(usn_sample_html)


    # 作業ディレクトリの作成
    usndir = topdir + '\\' + usn_no + '\\'
    if os.path.exists(usndir):
        print("既に存在します :" + usn_no)
        sys.exit(1)        
    os.mkdir(usndir)

    # 各項目の取得

    # 通知日
    h2 = soup.find('h2')
    datestr = h2.find_next_sibling('p').text
    datestr = convert_date_format(datestr)
    f = open(usndir + "Date.txt",'w')
    f.write(datestr + '\n')
    f.close()

    # 対象Ubuntu版数
    h3 = soup.find('h3')    
    ul = h3.find_next_sibling('ul')
    lis = ul.find_all('li')
    f = open(usndir + "Ubuntu_version.txt",'w')
    for li in lis:
        f.write(li.text + '\n')
    f.close()

    for h3 in soup.find_all('h3'):
        # Details
        title = h3.text
        if title == 'Details':
            f = open(usndir + "Details.txt",'w')
            # next_siblingだと改行(\n)がヒットしてしまうので次の<p>を探す
            p = h3
            while  True:
                p = p.find_next_sibling('p')
                if p is None:
                    # 見つからなかったら抜ける
                    break
                if p.text == detail_text:
                    # Detailsが終わったら抜ける
                    break
                f.write(p.text + '\n\n')
            f.close()

        # Update instructions
        elif title == 'Update instructions':
            fp = open(usndir + "Package.txt",'w')
            fpv = open(usndir + "Package_version.txt",'w')

            # <dl>の中に<dt>でUbuntuバージョン、さらに<dd>のなかに対象パッケージとバージョンがリストになっている
            # <dl>
            #     <dt>Ubuntuバージョン</dt>
            #     <dd>
            #         <a>パッケージ名
            #         <a>パッケージバージョン</a>
            #     </dd>
            # ・・・
            # </dl>            
            dls = h3.find_next_sibling('dl')
            lists = dls.find_all([ 'dt' , 'a' ])
            num = 1
            for a in lists:
                if  'Ubuntu ' in a.text:
                    fp.write(a.text + '\n')
                    fpv.write(a.text + '\n')
                    num = 1
                else:
                    if num %2 == 1:
                        #パッケージだけをファイルにまとめる
                        fp.write(a.text + '\n')
                        num += 1
                    else:
                        #パッケージバージョンだけをファイルにまとめる
                        fpv.write(a.text + '\n')
                        num += 1
            fp.close()
            fpv.close()
            

        # CVE_number (References)
        elif title == 'References':
            f = open(usndir + "CVE_number.txt",'w')
            p = h3.find_next_sibling('p')
            # <p>の中にCVEへのリンクがリストになっている
            priorities = []
            for a in p.find_all('a'):
                f.write(a.text + '\n')
                #print(a.get('href'))  # URL取得
                priorities.append(get_cve_priority(a.get('href')))  # CVE優先度
            f.close()

        # Priority
            f = open(usndir + "Priority.txt",'w')
            f.write(get_hieghest_priority(priorities) + '\n')
            f.close()

        # Link
            f = open(usndir + "Link.txt",'w')
            f.write(usn_url + usn_no + '\n')
            f.close()

        # Details和訳
            f = open(usndir + "Details_jp.txt",'w')
            f.write('\n')
            f.close()

    # USNがサポート対象か判定

    support = is_supported(usndir)
    if support:
        support = "○"
    else:
        support = "×"

    f = open(usndir + "support.txt",'w')
    f.write(support + '\n')
    f.close()
    

    ##### ファイル編集

    filelist = ['Date.txt', 'Ubuntu_version.txt', 'Package.txt', 'support.txt', 'Package_version.txt', 'CVE_number.txt', 'Priority.txt', 'Details.txt', 'Details_jp.txt', 'Link.txt']
    csvstr = marge_files(usn_no, usndir, filelist)

    # 保存ディレクトリの作成
    date = str(datetime.date.today())
    savedir = topdir + '\\' + date +'\\' + 'tmp\\'
    if not os.path.exists(savedir):
        os.makedirs(savedir)

    f = open(savedir + usn_no + '.txt', 'w')
    f.write(csvstr)
    f.close()


    # 作業ディレクトリの削除
    shutil.rmtree(usndir)
