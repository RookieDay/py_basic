#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/11/20
# @Author  : RookieDay
# @Site    : 
# @File    : generic_itemloader
# @Github  : https://github.com/rookieday
# @Software: PyCharm Community Edition


import scrapy
from scrapy_tutorial.items import ScrapyTutorialItem
from scrapy.loader import ItemLoader

class GenericSpider(scrapy.Spider):
    name = 'genericLoader'
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
        item = ItemLoader(item = ScrapyTutorialItem(),response=response)
        item.add_css('name','h3.author-title::text')
        item.add_css('birthdate','.author-born-date::text')
        item.add_css('bio','.author-description::text')
        item.add_value('arrtest',['a','b','c'])
        item.add_value('url',response.url)
        yield item.load_item()