import os
import time
import urllib

import ssl

from bs4 import BeautifulSoup

import requests
from selenium import webdriver

# 漫画id
comicId = "543584"
# 漫画url
comicUrl = "http://ac.qq.com/Comic/comicInfo/id/543584" + comicId
print(comicUrl)
html = requests.get(comicUrl).text
soup = BeautifulSoup(html, "html.parser")
# a标签集合
data = soup.find(attrs={'class': 'works-chapter-list-wr ui-left'}).findAll('a', href=True)

# 章节url集合
chapter_urls = []

for label in data:
    if 'http://ac.qq.com' + label['href'] not in chapter_urls:
        chapter_urls.append('http://ac.qq.com' + label['href'])

for chapter_url in chapter_urls:
    browser = webdriver.Chrome()
    browser.get(chapter_url)
    time.sleep(5)

    # 模拟浏览器滑动  将浏览器慢慢滑到底部
    for a in range(1, 120):
        script = "document.documentElement.scrollHeight*" + str(a)
        print(script)
        browser.execute_script('window.scrollTo(0, %s);' % script)
        print(a)
        # 这里设置5秒是为了保证图片能加载出来
        time.sleep(5)

    html = BeautifulSoup(browser.page_source, "lxml")
    data = html.find(attrs={'class': 'main'}).findAll('img')

    # 打印所有src地址
    print("图片链接地址")
    urls = []
    for aaa in data:
        print(aaa['src'])
        urls.append(aaa['src'])

    print("筛选图片地址")
    imgUrls = []
    for bbbbb in urls:
        print(bbbbb)
        if bbbbb.__contains__("manhua_detail"):
            imgUrls.append(bbbbb)
            print(bbbbb)

    filePath = os.path.realpath(__file__)
    dirPath = os.path.dirname(filePath)

    print("批量下载图片")
    for a in imgUrls:
        print("===>" + a[39:-2])
        ssl._create_default_https_context = ssl._create_unverified_context
        urllib.request.urlretrieve(a, dirPath + "/" + a[39:-2])
    browser.close()
