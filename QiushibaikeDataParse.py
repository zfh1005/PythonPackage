# -*- coding:utf-8 -*-
 
import re
import threading
import urllib.request
import time
import os
number = 0
sqlku = []
 
 
def getDoc():
    global number, sqlku
    page = 1
    print ("正在获取页面...")
    while True:
        while number <= 10:
            number += 1
            myUrl = "http://m.qiushibaike.com/hot/page/"
            myPage = urllib.request.urlopen(myUrl).read()
            unicodePage = myPage.decode("utf-8")
            print(unicodePage)
            myItems = re.findall('<div.*?class="content".*?title="(.*?)">(.*?)</div>', unicodePage, re.S)
            #返回当前页面所有的匹配结果的列表到myItems列表
            for item in myItems:
               sqlku.append([item[0].replace('\n', ''), item[1].replace('\n', '')])
               #把内容处理之后加入到数据库
            page += 1
            myPage.close()
 
def showDoc():
    global number, sqlku
    i = 1
    for item in sqlku:
        key = raw_input('请输入回车来看段子(输入quit结束本程序)：')
        if key == "quit":
            os._exit(0)
        i += 1
        print ('时间：',item[0])
        print ('内容：',item[1])
        if i == 20:
            number -= 1
            i = 1
 
threading.Thread(target=getDoc).start()
time.sleep(2)
threading.Thread(target=showDoc).start()