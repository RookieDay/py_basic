#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/11/22
# @Author  : RookieDay
# @Site    : 
# @File    : download_img
# @Github  : https://github.com/rookieday
# @Software: PyCharm Community Edition

from scrapy.spiders import CrawlSpider, Rule
from scrapy import Request
from scrapy.linkextractors import LinkExtractor
from scrapy_download.items import ScrapyDownloadItem

class Download_Img(CrawlSpider):
    name = 'down_img'
    allowed_domains = ['699pic.com']
    image_urls = []
    start_urls = [
        'http://699pic.com/best.html'
    ]
    rules = (
        Rule(LinkExtractor(allow=('http://699pic.com/tupian-\d+.html$',)),callback='parse_item',follow=True),
    )
    def parse_item(self, response):
        item = ScrapyDownloadItem()
        item['url'] = response.url
        item['name'] = response.xpath('//div[@class="crumbs"]/span/a[last()]/text()').extract_first(default="N/A")
        print('*'*11,item)
        yield Request(response.url, callback=self.img_url,dont_filter=True)
        item['image_urls'] = self.image_urls
        yield item

    def img_url(self, response,):
        img_urls = response.xpath('//div[@class="photo-img"]/a/img/@src').extract()
        for img_url in img_urls:
            self.image_urls.append(img_url)
