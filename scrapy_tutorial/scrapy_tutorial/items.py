# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import TakeFirst, MapCompose, Join


# 对应generic_spider.py
# class ScrapyTutorialItem(scrapy.Item):
#     # define the fields for your item here like:
#     name = scrapy.Field()
#     birthdate = scrapy.Field()
#     bio = scrapy.Field()


# itemloader测试使用部分
# 对应generic_itemloader.py
def add_prefix(value):
    return "ana_" + value

class ScrapyTutorialItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field(
        input_processor=MapCompose(add_prefix),
        output_processor=Join(),
    )
    birthdate = scrapy.Field()
    bio = scrapy.Field()
    arrtest = scrapy.Field(
        input_processor=MapCompose(add_prefix),
        output_processor=TakeFirst(),
    )
    url = scrapy.Field(
        input_processor=MapCompose(add_prefix),
        output_processor=Join(),
    )
