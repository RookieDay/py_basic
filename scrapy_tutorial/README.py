#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/11/16
# @Author  : RookieDay
# @Site    : 
# @File    : README
# @Github  : https://github.com/rookieday
# @Software: PyCharm Community Edition

# 遇到的pywin32问题问题解决办法
# ttp://blog.csdn.net/chennudt/article/details/76726580


# Scrapy主要包括了以下组件：
#
# 引擎(Scrapy)
#   用来处理整个系统的数据流处理, 触发事务(框架核心)

# 调度器(Scheduler)
#   用来接受引擎发过来的请求, 压入队列中, 并在引擎再次请求的时候返回. 可以想像成一个URL（抓取网页的网址或者说是链接）的优先队列, 由它来决定下一个要抓取的网址是什么, 同时去除重复的网址

# 下载器(Downloader)
#   用于下载网页内容, 并将网页内容返回给蜘蛛(Scrapy下载器是建立在twisted这个高效的异步模型上的)

# 爬虫(Spiders)
#   爬虫是主要干活的, 用于从特定的网页中提取自己需要的信息, 即所谓的实体(Item)。用户也可以从中提取出链接,让Scrapy继续抓取下一个页面

# 项目管道(Pipeline)
#   负责处理爬虫从网页中抽取的实体，主要的功能是持久化实体、验证实体的有效性、清除不需要的信息。当页面被爬虫解析后，将被发送到项目管道，并经过几个特定的次序处理数据。

# 下载器中间件(Downloader Middlewares)
#   位于Scrapy引擎和下载器之间的框架，主要是处理Scrapy引擎与下载器之间的请求及响应。

# 爬虫中间件(Spider Middlewares)
#   介于Scrapy引擎和爬虫之间的框架，主要工作是处理蜘蛛的响应输入和请求输出。

# 调度中间件(Scheduler Middewares)
#   介于Scrapy引擎和调度之间的中间件，从Scrapy引擎发送到调度的请求和响应。

# Scrapy运行流程大概如下：
#
#     引擎从调度器中取出一个链接(URL)用于接下来的抓取
#     引擎把URL封装成一个请求(Request)传给下载器
#     下载器把资源下载下来，并封装成应答包(Response)
#     爬虫解析Response
#     解析出实体（Item）,则交给实体管道进行进一步的处理
#     解析出的是链接（URL）,则把URL交给调度器等待抓取

# tutorial/
#     scrapy.cfg            # deploy configuration file
#     项目的配置信息，主要为Scrapy命令行工具提供一个基础的配置信息。（真正爬虫相关的配置信息在settings.py文件中）
#     tutorial/             # project's Python module, you'll import your code from here
#         __init__.py
#
#         items.py          # project items definition file
#         设置数据存储模板，用于结构化数据，如：Django的Model
#         pipelines.py      # project pipelines file
#         数据处理行为，如：一般结构化的数据持久化
#         settings.py       # project settings file
#         配置文件，如：递归的层数、并发数，延迟下载等
#         spiders/          # a directory where you'll later put your spiders
#          爬虫目录，如：创建文件，编写爬虫规则
#             __init__.py

import os
print(os.path.dirname(__file__) + '/1.html')

# scrapy shell

# scrapy shell <url>
# scrapy shell 'http://quotes.toscrape.com/page/1/'
# windows下面必须使用双引号
# scrapy shell "http://quotes.toscrape.com/page/1/"
# >>> response.css('title') 返回的是一个选择器列表
# [<Selector xpath='descendant-or-self::title' data='<title>Quotes to Scrape</title>'>]

# >>> response.css('title::text').extract()  ::text代表可以选择title元素的text文本
# ['Quotes to Scrape']

# >>> response.css('title').extract()  如果没有::text 我们获得是 full title element, including its tags
# ['<title>Quotes to Scrape</title>']

# >>> response.css('title::text').extract_first()   .extract() is a list,返回的是一个list  .extract_first() 只会返回第一个结果
# 'Quotes to Scrape'
# 类似下面这样的情况
# >>> response.css('title::text')[0].extract()
# 'Quotes to Scrape'
# Remark: .extract_first() avoids an IndexError and returns None when it doesn’t find any element matching the selection.

# 也支持re() method
# >>> response.css('title::text').re(r'Quotes.*')
# ['Quotes to Scrape']
# >>> response.css('title::text').re(r'Q\w+')
# ['Quotes']
# >>> response.css('title::text').re(r'(\w+) to (\w+)')
# ['Quotes', 'Scrape']


# xpath
# 表达式	    描述
# nodename	选取此节点的所有子节点。
# /	        从根节点选取。
# //	        从匹配选择的当前节点选择文档中的节点，而不考虑它们的位置。
# .	        选取当前节点。
# ..	        选取当前节点的父节点。
# @	        选取属性。


# 路径表达式	                                结果
# /bookstore/book[1]	                    选取属于 bookstore 子元素的第一个 book 元素。
# /bookstore/book[last()]	                选取属于 bookstore 子元素的最后一个 book 元素。
# /bookstore/book[last()-1]	            选取属于 bookstore 子元素的倒数第二个 book 元素。
# /bookstore/book[position()<3]	        选取最前面的两个属于 bookstore 元素的子元素的 book 元素。
# //title[@lang]	                        选取所有拥有名为 lang 的属性的 title 元素。
# //title[@lang='eng']	                选取所有 title 元素，且这些元素拥有值为 eng 的 lang 属性。
# /bookstore/book[price>35.00]	        选取 bookstore 元素的所有 book 元素，且其中的 price 元素的值须大于 35.00。
# /bookstore/book[price>35.00]/title	    选取 bookstore 元素中的 book 元素的所有 title 元素，且其中的 price 元素的值须大于 35.00。

#
# 通配符	    描述
# *	        匹配任何元素节点。
# @*	        匹配任何属性节点。
# node()	    匹配任何类型的节点。
#
# 路径表达式	                              结果
# //book/title | //book/price	        选取 book 元素的所有 title 和 price 元素。
# //title | //price	                    选取文档中的所有 title 和 price 元素。
# /bookstore/book/title | //price	    选取属于 bookstore 元素的 book 元素的所有 title 元素，以及文档中所有的 price 元素。

# >>> response.xpath('//title')
# [<Selector xpath='//title' data='<title>Quotes to Scrape</title>'>]
# >>> response.xpath('//title/text()').extract_first()
# 'Quotes to Scrape'


# cmd下输入  by http://jsonlines.org/
# 1. That will generate an quotes.json file containing all scraped items, serialized in JSON.
# scrapy crawl quotes -o quotes.json
# 2. You can also used other formats, like JSON Lines:
# scrapy crawl quotes -o quotes.jl

# urljoin 使用请求的绝对路径
# next_page = response.css('li.next a::attr(href)').extract_first()
#         if next_page is not None:
#             next_page = response.urljoin(next_page)
#             yield scrapy.Request(next_page, callback=self.parse)


# response.follow 可以使用请求的相对路径
# response.follow just returns a Request instance; you still have to yield this Request.
# next_page = response.css('li.next a::attr(href)').extract_first()
# if next_page is not None:
#     yield response.follow(next_page, callback=self.parse)

# 你也可以给response.follow传递一个选择器而不是字符串
# You can also pass a selector to response.follow instead of a string; this selector should extract necessary attributes:
#
# for href in response.css('li.next a::attr(href)'):
#     yield response.follow(href, callback=self.parse)

# For <a> elements there is a shortcut: response.follow uses their href attribute automatically. So the code can be shortened further:
# response.follow 会默认使用a标签的herf属性，所以代码继续精简
# for a in response.css('li.next a'):
#     yield response.follow(a, callback=self.parse)