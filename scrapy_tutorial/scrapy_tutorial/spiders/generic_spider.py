#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/11/19
# @Author  : RookieDay
# @Site    : 
# @File    : generic_spider
# @Github  : https://github.com/rookieday
# @Software: PyCharm Community Edition

import scrapy
from scrapy_tutorial.items import ScrapyTutorialItem

class AuthorSpider(scrapy.Spider):
    name = 'generic'
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        # follow links to author pages 紧接在author后面的a标签
        for href in response.css('.author + a::attr(href)'):
            yield response.follow(href,self.parse_author)
        # follow pagination links
        for href in response.css('li.next a::attr(href)'):
            yield response.follow(href, self.parse)

    def parse_author(self,response):
        self.logger.info('Hi, this is an item page! %s', response.url)
        item = ScrapyTutorialItem()

        def extract_with_css(query):
            return response.css(query).extract()

        item['name'] = extract_with_css('h3.author-title::text')
        item['birthdate'] = extract_with_css('.author-born-date::text')
        item['bio'] = extract_with_css('.author-description::text')
        return item