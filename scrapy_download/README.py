#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/11/23
# @Author  : RookieDay
# @Site    : 
# @File    : README
# @Github  : https://github.com/rookieday
# @Software: PyCharm Community Edition
#
# 下载器中间件(Downloader middlewares)
# 下载器中间件是在引擎及下载器之间的特定钩子(specific hook)，处理Downloader传递给引擎的response。 其提供了一个简便的机制，通过插入自定义代码来扩展Scrapy功能。
#
# Spider中间件(Spider middlewares)
# Spider中间件是在引擎及Spider之间的特定钩子(specific hook)，处理spider的输入(response)和输出(items及requests)。 其提供了一个简便的机制，通过插入自定义代码来扩展Scrapy功能。
#
# Scrapy中的数据流由执行引擎控制，其过程如下:
#
# 引擎打开一个网站(open a domain)，找到处理该网站的Spider并向该spider请求第一个要爬取的URL(s)。
# 引擎从Spider中获取到第一个要爬取的URL并在调度器(Scheduler)以Request调度。
# 引擎向调度器请求下一个要爬取的URL。
# 调度器返回下一个要爬取的URL给引擎，引擎将URL通过下载中间件(请求(request)方向)转发给下载器(Downloader)。
# 一旦页面下载完毕，下载器生成一个该页面的Response，并将其通过下载中间件(返回(response)方向)发送给引擎。
# 引擎从下载器中接收到Response并通过Spider中间件(输入方向)发送给Spider处理。
# Spider处理Response并返回爬取到的Item及(跟进的)新的Request给引擎。
# 引擎将(Spider返回的)爬取到的Item给Item Pipeline，将(Spider返回的)Request给调度器。
# (从第二步)重复直到调度器中没有更多地request，引擎关闭该网站。


# Scrapy中的数据流由执行引擎控制，其过程如下:
#
# 1，引擎从Spiders中获取到最初的要爬取的请求（Requests）。
# 2，引擎安排请求（Requests）到调度器中，并向调度器请求下一个要爬取的请求（Requests）。
# 3，调度器返回下一个要爬取的请求（Requests）给引擎。
# 4，引擎将上步中得到的请求（Requests）通过下载器中间件（Downloader Middlewares）发送给下载器（Downloader ），这个过程中下载器中间件（Downloader Middlewares）中的process_request()函数会被调用到。
# 5，一旦页面下载完毕，下载器生成一个该页面的Response，并将其通过下载中间件（Downloader Middlewares）发送给引擎，这个过程中下载器中间件（Downloader Middlewares）中的process_response()函数会被调用到。
# 6，引擎从下载器中得到上步中的Response并通过Spider中间件(Spider Middlewares)发送给Spider处理，这个过程中Spider中间件(Spider Middlewares)中的process_spider_input()函数会被调用到。
# 7，Spider处理Response并通过Spider中间件(Spider Middlewares)返回爬取到的Item及(跟进的)新的Request给引擎，这个过程中Spider中间件(Spider Middlewares)的process_spider_output()函数会被调用到。
# 8，引擎将上步中Spider处理的其爬取到的Item给Item 管道（Pipeline），将Spider处理的Request发送给调度器，并向调度器请求可能存在的下一个要爬取的请求（Requests）。
# 9，(从第二步)重复直到调度器中没有更多的请求（Requests）。