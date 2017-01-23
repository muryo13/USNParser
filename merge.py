#coding: UTF-8

import sys

import os
import csv
import datetime

# main
if __name__ == '__main__':
    args = sys.argv
    if len(args) < 1:
        print("引数を確認してください:" + args[0])
        sys.exit(1)        

    # ディレクトリの確認
    topdir = os.getcwd()
    date = str(datetime.date.today())

    if len(args) == 2:
        savedir = args[1] + '\\'
    else:
        savedir = topdir + '\\' + date +'\\'

    tmpdir = savedir + 'tmp\\'
    if not os.path.exists(savedir):
        print("対象ディレクトリがありません:" + savedir)
        sys.exit(1)

    if not os.path.exists(tmpdir):
        print("作業ディレクトリがありません:" + tmpdir)
        sys.exit(1)        


    ##### ファイル結合

    files = os.listdir(tmpdir)
    if len(files) == 0:
        print("作業ファイルがありません")
        sys.exit(1)

    fm = open(tmpdir + 'merge.txt', 'w')

    for file in files:
        f = open(tmpdir + file, 'r')
        fm.write(f.read())
        fm.write('\n')
        f.close()
    fm.close()
        
    os.rename(tmpdir + 'merge.txt', savedir + date + '.csv')
    
