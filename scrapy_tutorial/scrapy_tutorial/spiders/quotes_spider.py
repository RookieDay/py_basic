#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/11/16
# @Author  : RookieDay
# @Site    : 
# @File    : quotes_spider
# @Github  : https://github.com/rookieday
# @Software: PyCharm Community Edition

import scrapy
import os

out_dir = os.path.join(os.path.dirname(__file__))

class QuotesSpider(scrapy.Spider):
    name = "quotes"

    start_urls = [
        'http://quotes.toscrape.com/page/1/',
        'http://quotes.toscrape.com/page/2/',
    ]

    # 或者如下方法也是可以的
    # def start_requests(self):
    #     urls = [
    #         'http://quotes.toscrape.com/page/1/',
    #         'http://quotes.toscrape.com/page/2/',
    #     ]
    #     for url in urls:
    #         yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = os.path.dirname(__file__) + '/quotes-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)