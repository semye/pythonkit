import keyword
import os
import requests
from src import semye_support
from bs4 import BeautifulSoup


def fuck():
    """一个自定义的函数"""
    strrr = input("请输入:\n")
    print("你输入的内容是: ", strrr)


# 获取html
def get_html(url):
    """获取指定网址的html"""
    return requests.get(url).text


def print_keywords():
    """打印python的keyword"""
    print(keyword.kwlist)


def print_files():
    """显示所有文件夹名"""
    print("hello,world")
    path = "/Users/yesheng"
    dirlist = os.listdir(path)
    for i in dirlist:
        print(i.title())


def download_image():
    url = "http://h5.eqxiu.com/s//5F7wmiq0"
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2)+\
         AppleWebKit/537.36 (KHTML, like Gecko)+\
          Chrome/63.0.3239.84 Safari/537.36",
        "Host": "h5.eqxiu.com",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "zh-cn,zh;q=0.8,en-us;q=0.5,en;q=0.3",
        "Accept-Encoding": "gzip, deflate",
        "Connection": "keep-alive",
        "Refer": "http://store.eqxiu.com/scene-467272.html",
        "Cookie": "gr_user_id=22c19384-907b-44fd-9124-cbbaed48b481; +\
        gr_session_id_a17a66c1107ba80b=e8416813-b99f-4672-8d98-a9385a8bd9b0; +\
        _tracker_distinct_id_=c89039c7-06fe-4b98-909d-71892d5200e5; +\
        _tracker_launch_=1;+\
         _tracker_session_id_=f8d9adf2-36fe-4163-a55c-57ed3d38e5f3; +\
         _tracker_user_id_=; +\
         _tracker_share_level_=0;+\
          _tracker_from_user_=;+\
           _tracker_from_id_="
    }
    down_html = requests.get(url=url, headers=headers)
    bs = BeautifulSoup(down_html.text, "html.parser")
    print(bs)


if __name__ == '__main__':
    __version__ = '1.0'
    print("当前版本号为:" + __version__)
    html = get_html("http://www.douyu.com/directory/all")
    print(html)
    semye_support.helloworld()
