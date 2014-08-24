#encoding:UTF-8

import urllib.request

def getHtml(url):
    page = urllib.request.urlopen(url)
    html = page.read()
    page.close()
    return html.decode('utf-8')


def getdata(url):
    data=urllib.request.urlopen(url).read().decode('utf-8')
    print(data)


if __name__ == '__main__' :
    html = getHtml('http://www.weather.com.cn/forecast/') 
    getdata(html)