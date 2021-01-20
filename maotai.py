import json
from bs4 import BeautifulSoup

import requests

target_url = "https://item.jd.com/100012043978.html"

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2)+\
         AppleWebKit/537.36 (KHTML, like Gecko)+\
          Chrome/63.0.3239.84 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "zh-cn,zh;q=0.8,en-us;q=0.5,en;q=0.3",
    "Accept-Encoding": "gzip, deflate",
    "Connection": "keep-alive"
}
response = requests.get(url=target_url, headers=headers)
cookies = response.cookies
print(cookies.values())
# print(response.text)

# todo 登录
