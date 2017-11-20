#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/11/16
# @Author  : RookieDay
# @Site    : 
# @File    : begin
# @Github  : https://github.com/rookieday
# @Software: PyCharm Community Edition

# by http://blog.csdn.net/wangsidadehao/article/details/52911746

from scrapy import cmdline
cmdline.execute('scrapy crawl genericLoader '.split())
# cmdline.execute('scrapy crawl generic '.split())
# cmdline.execute('scrapy crawl generic -o quptes-generic.jl'.split())
# cmdline.execute('scrapy crawl quotes-xpath -o quptes-xpath.jl'.split())
# cmdline.execute('scrapy crawl tag -o quptes-humor.jl -a tag=humor'.split())
# cmdline.execute('scrapy crawl author'.split())
#  cmdline.execute('scrapy crawl quotes'.split())