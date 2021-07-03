#!/usr/bin/env python3
# 一个简单的爬虫程序 抓取页面上的英雄联盟英雄信息并存到数据库中去

import pymysql
import requests
from bs4 import BeautifulSoup


def get_html_text():
    """获取html"""
    url = "https://lol.qq.com/data/info-heros.shtml"
    html = requests.get(url).text
    soup = BeautifulSoup(html, "html.parser")
    data = soup.find(id='jSearchHeroDiv').findAll('li')
    return data


def open_mysql():
    """打开数据库"""
    return pymysql.connect(user='root', password='', database='semye', charset='utf8')


def get(data, conn):
    cursor = conn.cursor()
    try:
        for li in data:
            hero_name = li.find('h2').getText()
            hero_nick_name = li.find('h3').getText()
            print(hero_name)
            print(hero_nick_name)
            sql = 'insert into semye_characters (name,nick_name,sex) values (%s,%s,%s)'
            cursor.execute(sql, (hero_name, hero_nick_name, '男'))
            conn.commit()

    except:
        conn.rollback()
    cursor.close()
    conn.close()


def get_hero():
    data = get_html_text()
    conn = open_mysql()
    get(data, conn)


if __name__ == '__main__':
    get_hero()
