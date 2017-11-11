#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/11/11
# @Author  : RookieDay
# @Site    : 
# @File    : douban
# @Github  : https://github.com/rookieday
# @Software: PyCharm Community Edition

# https://zhuanlan.zhihu.com/p/20423182


import requests
from bs4 import BeautifulSoup
URL = 'https://movie.douban.com/top250'

def download_html(URL):
    # 产生403的原因，一般可能是因为需要登录的网站没有登录或者被服务器认为是爬虫而拒绝访问，这里很显然属于第二种情况。
    # 一般，浏览器在向服务器发送请求的时候，会有一个请求头——User - Agent，它用来标识浏览器的类型.当我们使用requests
    # 来发送请求的时候，默认的User - Agent是python - requests / 2.8.1（后面的数字可能不同，表示版本号）。
    # 我们通过手动指定User - Agent为Chrome浏览器，再此访问就得到了真实的网页源码。服务器通过校验请求的U - A来识别爬虫，
    # 这算是最简单的一种反爬虫机制了，通过模拟浏览器的U - A，能够很轻松地绕过这个问题。
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
    }
    data = requests.get(URL,headers=headers)
    # data.encoding = 'utf-8'
    return data.content
def parse_html(html):
    soup = BeautifulSoup(html, "lxml")
    movie_list = soup.find('ol', attrs={'class':'grid_view'})
    for movie_li in movie_list.find_all('li'):
        detail = movie_li.find('div',attrs={'class':'hd'})
        movie_name = movie_li.find('span',attrs={'class':'title'}).getText()
        print(movie_name)

if __name__ == '__main__':
    html = download_html(URL)
    parse_html(html)