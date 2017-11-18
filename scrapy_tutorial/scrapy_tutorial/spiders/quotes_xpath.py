#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/11/18
# @Author  : RookieDay
# @Site    : 
# @File    : quotes_xpath
# @Github  : https://github.com/rookieday
# @Software: PyCharm Community Edition

import scrapy

class QutesXpath(scrapy.Spider):
    name = 'quotes-xpath'
    start_urls = [
        'http://quotes.toscrape.com/',
    ]
    def parse(self, response):
        for quote in response.xpath('//div[@class="quote"]'):
            yield {
                'text': quote.xpath('./span[@class="text"]/text()').extract_first(),
                'author': quote.xpath('.//small[@class="author"]/text()').extract_first(),
                'tags': quote.xpath('.//div[@class="tags"]/a[@class="tag"]/text()').extract()
            }
        next_page_url = response.xpath('//li[@class="next"]/a/@href').extract_first()
        if next_page_url is not None:
            yield response.follow(next_page_url,self.parse)