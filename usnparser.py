#coding: UTF-8

import sys
import urllib.request
from bs4 import BeautifulSoup

usn_url = "https://www.ubuntu.com/usn/"
usn_default_no = 'usn-3172-1'  # USN番号を指定
usn_sample_html = 'ubuntu.html'

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
    return soup.find_all("div", "medium-value")[0].text

# 一番高いレベルのPriorityを返す
def get_hieghest_priority(priorities):
    if 'High' in priorities:
        return 'High'
    elif 'Medium' in priorities:
        return 'Medium'
    elif 'Low' in priorities:
        return 'Low'
    else:
        return 'None'

# main
if __name__ == '__main__':
    args = sys.argv
    usn_no = usn_default_no
    if len(args) > 1:
        usn_no = args[1]
    soup = get_soup(usn_url + usn_no)
    #soup = get_soup(usn_sample_html)

    # 各項目の取得
    for h3 in soup.find_all('h3'):
        # Details
        title = h3.text
        if title == 'Details':
            print('Details:')
            print(h3.find_next_sibling('p').text)
            # next_siblingだと改行(\n)がヒットしてしまうので次の<p>を探す

        elif title == 'References':
            print('References:')
            p = h3.find_next_sibling('p')
            # <p>の中にCVEへのリンクがリストになっている
            priorities = []
            for a in p.find_all('a'):
                print(a.text)
                #print(a.get('href'))  # URL取得
                priorities.append(get_cve_priority(a.get('href')))  # CVE優先度
            print(get_hieghest_priority(priorities))
