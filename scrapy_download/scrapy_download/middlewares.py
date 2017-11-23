# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
import random,base64
from .settings import PROXIES

class ScrapyDownloadSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


# by https://www.cnblogs.com/wzjbg/p/6507581.html
class RandomUserAgent(object):
    def __init__(self,agents=''):
        self.agents = agents

    @classmethod
    def from_crawler(cls,crawler):
        return cls(
            crawler.settings.getlist('USER_AGENT')
        )
    def process_request(self,request,spider):
        request.headers.setdefault('USER_AGENT',random.choice(self.agents))

class ProxyMiddleware(object):
    def process_request(self,request,spider):
        proxy = random.choice(PROXIES)
        # if proxy['user_pass'] is not None:
        #     request.meta['proxy'] = "http://%s" % proxy['ip_port']
        #     # 对代理数据进行base64编码
        #     encoded_user_pass = base64.encodebytes(proxy['user_pass'])
        #     # 添加到HTTP代理格式里
        #     request.headers['Proxy-Authorization'] = 'Basic ' + encoded_user_pass
        # else:
        print("****代理****" + proxy['ip_port'])
        request.meta['proxy'] = "http://%s" % proxy['ip_port']

class ImageMiddleware(object):
    def process_request(self,request,spider):
        refer = request.meta.get('referer',None)
        if refer:
            request.headers['referer'] = refer