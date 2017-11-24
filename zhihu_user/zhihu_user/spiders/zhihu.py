# -*- coding: utf-8 -*-
import scrapy
import json
from zhihu_user.items import ZhihuUserItem

class ZhihuSpider(scrapy.Spider):
    name = 'zhihu'
    allowed_domains = ['www.zhihu.com']
    start_urls = ['http://www.zhihu.com/']
    image_urls = []
    # 获取用户详细信息 user是该用户的url_token，include是查询参数
    user_url = 'https://www.zhihu.com/api/v4/members/{user}?include={include}'
    # 获取用户列表
    follows_url = 'https://www.zhihu.com/api/v4/members/{user}/followees?include={include}&amp;offset={offset}&amp;limit={limit}'
    # 获取粉丝列表
    followers_url = 'https://www.zhihu.com/api/v4/members/{user}/followers?include={include}&offset={offset}&limit={limit}'

    start_user = 'excited-vczh'
    # 用户详细信息参数
    user_query = 'allow_message,is_followed,is_following,is_org,is_blocking,employments,answer_count,follower_count,articles_count,gender,badge[?(type=best_answerer)].topics'
    # 用户列表参数
    follows_query = 'data[*].answer_count,articles_count,gender,follower_count,is_followed,is_following,badge[?(type=best_answerer)].topics'
    # 粉丝列表参数
    followers_query = 'data[*].answer_count,articles_count,gender,follower_count,is_followed,is_following,badge[?(type=best_answerer)].topics'

    def start_requests(self):

        # 用户信息
        yield scrapy.Request(self.user_url.format(user=self.start_user,include=self.user_query),self.parse_user)
        # 用户列表
        yield scrapy.Request(self.follows_url.format(user=self.start_user,include=self.follows_query,limit=20,offset=0),self.parse_follows)
        # 粉丝列表
        yield scrapy.Request(self.followers_url.format(user=self.start_user, include=self.followers_query, limit=20, offset=0),self.parse_followers)

    def parse_user(self,response):
        result = json.loads(response.text)
        item = ZhihuUserItem()
        for field in item.fields:
            if field in result.keys():
                item[field] = result.get(field)
                if field == 'avatar_url':
                    self.image_urls.append(item['avatar_url'])
        item['image_urls'] = self.image_urls
        yield item
        # 获取该用户关注列表的请求
        yield scrapy.Request(self.follows_url.format(user=result.get('url_token'),include=self.follows_query,limit=20,offset=0),self.parse_follows)
        yield scrapy.Request(self.followers_url.format(user=result.get('url_token'),include=self.followers_query,limit=20,offset=0),self.parse_followers)

    def parse_follows(self,response):
        result = json.loads(response.text)
        # print(result.get('data'))
        if 'data' in result.keys():
            for result in result.get('data'):
                yield scrapy.Request(self.user_url.format(user=result.get('url_token'),include=self.user_query),self.parse_user)
        if 'paging' in result.keys() and result.get('paging').get('is_end') == False:
            next_page = result.get('paging').get('next')
            yield scrapy.Request(next_page,self.parse_follows)

    def parse_followers(self, response):
        results = json.loads(response.text)

        if 'data' in results.keys():
            for result in results.get('data'):
                yield scrapy.Request(self.user_url.format(user=result.get('url_token'), include=self.user_query), self.parse_user)

        if 'paging' in results.keys() and results.get('paging').get('is_end') == False:
            next_page = results.get('paging').get('next')
            yield scrapy.Request(next_page,self.parse_followers)