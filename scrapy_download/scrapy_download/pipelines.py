# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.pipelines.images import ImagesPipeline
from scrapy.exceptions import DropItem
from scrapy import Request

class ScrapyDownloadPipeline(object):
    def process_item(self, item, spider):
        return item

class ImageDownloadPipeline(ImagesPipeline):

    def get_media_requests(self, item, info):
        for img_url in item['image_urls']:
            referer = item['url']
            yield Request(img_url, meta={'item': item,
                                         'referer': referer})

    def item_completed(self, results, item, info):
        image_paths = [x['path'] for ok, x in results if ok]
        print(results)
        if not image_paths:
            raise DropItem("Item contains no images")
        return item
