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
        'http://quotes.toscrape.com/page/1/'
    ]

    # 或者如下方法也是可以的
    # def start_requests(self):
    #     urls = [
    #         'http://quotes.toscrape.com/page/1/',
    #         'http://quotes.toscrape.com/page/2/',
    #     ]
    #     for url in urls:
    #         yield scrapy.Request(url=url, callback=self.parse)

    # 输出所需要的body内容
    # def parse(self, response):
    #     page = response.url.split("/")[-2]
    #     filename = os.path.dirname(__file__) + '/quotes-%s.html' % page
    #     with open(filename, 'wb') as f:
    #         f.write(response.body)
    #     self.log('Saved file %s' % filename)

    # 返回json列表
    # def parse(self, response):
    #     for quote in response.css('div.quote'):
    #         yield {
    #             'text': quote.css('span.text::text').extract_first(),
    #             'author': quote.css('small.author::text').extract_first(),
    #             'tags': quote.css('div.tags a.tag::text').extract(),
    #         }


    # 这里使用的是url的绝对路径的方式
    #In [16]: a = response.urljoin(next_page)
    # In [17]: a
    # Out[17]: 'http://quotes.toscrape.com/page/2/'
    # def parse(self, response):
    #     for quote in response.css('div.quote'):
    #         yield {
    #             'text':quote.css('span.text::text').extract_first(),
    #             'author':quote.css('small.author::text').extract_first(),
    #             'tags':quote.css('div.tags a.tag::text').extract_first()
    #         }
    #     next_page = response.css('li.next a::attr(href)').extract_first()
    #     if next_page is not None:
    #         next_page = response.urljoin(next_page)
    #         yield scrapy.Request(next_page,callback=self.parse)

    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                'text':quote.css('span.text::text').extract_first(),
                'author':quote.css('small.author::text').extract_first(),
                'tags':quote.css('div.tags a.tag::text').extract_first()
            }
        next_page = response.css('li.next a::attr(href)').extract_first()
        if next_page is not None:
            yield response.follow(next_page,callback=self.parse)