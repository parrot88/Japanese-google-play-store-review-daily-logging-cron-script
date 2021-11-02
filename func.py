# coding: utf-8
import urllib.request
import re
import pprint
from pprint import pprint
import os
import time
import urllib.error
import datetime

class Functions:
    first_url = ""      #ページのURL
    headers = {"User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:47.0) Gecko/20100101 Firefox/47.0"}
    html = ""

    def __init__(self,url):
        self.first_url = url #ページのURLを保管す
        #print(self.first_url)

    #全処理を行う
    def get_all(self):
        self.get_page_html(self.first_url)  #取得したurlからhtmlコードを取得
        num = self.get_review_num()         #レビュー数を取得
        average = self.get_review_average() #平均を取得する
        dt_now = datetime.datetime.now()    #現在時刻を取得
        print(dt_now.strftime('%Y/%m/%d %H:%M:%S')+" ,"+num+" 件, 星平均: "+average)
        #print(self.html)

    #取得したページからhtmlコードを取得
    def get_page_html(self,url):
        request = urllib.request.Request(url, headers=self.headers) 
        self.html = urllib.request.urlopen(request).read().decode('utf-8')
        #print(self.html)
        pass

    #レビュー件数を取得
    def get_review_num(self):
        pattern = "aria-label=\"[0-9]+ 件の評価"
        res = re.findall(pattern,self.html)
        string1 = res[0].replace("aria-label=\"","")
        #pprint(string1)
        pattern2 = "[0-9]+"
        res2 = re.findall(pattern2,string1)
        string2 = res2[0]
        #pprint(string2)
        return string2

    #星平均数を取得する
    def get_review_average(self):
        pattern = "平均評価: 星[^個]+個"
        res = re.findall(pattern,self.html)
        #pprint(res[0])
        pattern2 = "[0-9]+[^/]+"
        res2 = re.findall(pattern2,res[0])
        string2 = res2[0]
        #pprint(string2)
        return string2