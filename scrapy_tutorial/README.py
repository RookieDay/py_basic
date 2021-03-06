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

# For <a> elements there is a shortcut: response.follow uses their href attribute automatically.
# So the code can be shortened further:
# response.follow 会默认使用a标签的herf属性，所以代码继续精简
# for a in response.css('li.next a'):
#     yield response.follow(a, callback=self.parse)

# response.follow(response.css('li.next a')) is not valid because response.css returns a
# list-like object with selectors for all results, not a single selector. A for loop like
# in the example above, or response.follow(response.css('li.next a')[0]) is fine.

# Using spider arguments
# You can provide command line arguments to your spiders by using the -a option when running them:
# scrapy crawl quotes -o quotes-humor.json -a tag=humor
# These arguments are passed to the Spider’s __init__ method and become spider attributes by default.


# Command line tool
# Global commands:
# startproject/genspider/settings/runspider/shell/fetch/view/version

# Project-only commands:crawl/check/list/edit/parse/bench

# scrapy startproject <project_name> [project_dir]  If project_dir wasn’t specified, project_dir will be the same as project_name.
# scrapy genspider [-t template] <name> <domain>

# scrapy crawl <spider>  Start crawling using a spider.
# scrapy check [-l] <spider> Run contract checks.
# scrapy list List all available spiders in the current project. The output is one spider per line.
# scrapy edit <spider> Edit the given spider using the editor defined in the EDITOR environment variable or (if unset) the EDITOR setting.

# scrapy fetch <url> Downloads the given URL using the Scrapy downloader and writes the contents to standard output.
# Supported options:
# --spider=SPIDER: bypass spider autodetection and force use of specific spider
# --headers: print the response’s HTTP headers instead of the response’s body
# --no-redirect: do not follow HTTP 3xx redirects (default is to follow them)
# >scrapy fetch --nolog --headers http://quotes.toscrape.com/page/1/

# scrapy view <url>
# Opens the given URL in a browser, as your Scrapy spider would “see” it. Sometimes spiders see pages differently from regular users, so this can be used to check what the spider “sees” and confirm it’s what you expect.
# Supported options:
# --spider=SPIDER: bypass spider autodetection and force use of specific spider
# --no-redirect: do not follow HTTP 3xx redirects (default is to follow them)

# scrapy shell [url] Starts the Scrapy shell for the given URL (if given) or empty if no URL is given. Also supports UNIX-style local file paths, either relative with ./ or ../ prefixes or absolute file paths. See Scrapy shell for more info.
# Supported options:
# --spider=SPIDER: bypass spider autodetection and force use of specific spider
# -c code: evaluate the code in the shell, print the result and exit
# --no-redirect: do not follow HTTP 3xx redirects (default is to follow them); this only affects the URL you may pass as argument on the command line; once you are inside the shell, fetch(url) will still follow HTTP redirects by default.
# scrapy shell --nolog http://www.example.com/ -c "(response.status, response.url)"

# scrapy parse <url> [options] Fetches the given URL and parses it with the spider that handles it, using the method passed with the --callback option, or parse if not given.
# Supported options:
# --spider=SPIDER: bypass spider autodetection and force use of specific spider
# --a NAME=VALUE: set spider argument (may be repeated)
# --callback or -c: spider method to use as callback for parsing the response
# --pipelines: process items through pipelines
# --rules or -r: use CrawlSpider rules to discover the callback (i.e. spider method) to use for parsing the response
# --noitems: don’t show scraped items
# --nolinks: don’t show extracted links
# --nocolour: avoid using pygments to colorize the output
# --depth or -d: depth level for which the requests should be followed recursively (default: 1)
# --verbose or -v: display information for each depth level


# scrapy settings [options] Get the value of a Scrapy setting.
# $ scrapy settings --get BOT_NAME
# scrapybot
# $ scrapy settings --get DOWNLOAD_DELAY
# 0


# scrapy runspider <spider_file.py> Run a spider self-contained in a Python file, without having to create a project.
# scrapy version [-v] Prints the Scrapy version. If used with -v it also prints Python, Twisted and Platform info, which is useful for bug reports.
# scrapy bench ---> Run a quick benchmark test. Benchmarking.

# Custom project commands
# You can also add your custom project commands by using the COMMANDS_MODULE setting. See the Scrapy commands in
# scrapy/commands for examples on how to implement your commands.


# scrapy selector
# >>> from scrapy.selector import Selector
# >>> from scrapy.http import HtmlResponse

# scrapy shell http://doc.scrapy.org/en/latest/_static/selectors-sample1.html
# response.selector.xpath('//title/text()')
# Querying responses using XPath and CSS is so common that responses include two convenience shortcuts: response.xpath() and response.css():
# response.xpath('//title/text()') / response.css('title::text')
# response.css('img').xpath('@src').extract()

# response.xpath('//div[@id="not-exists"]/text()').extract_first() is None
# response.xpath('//div[@id="not-exists"]/text()').extract_first(default='not-found')


# itemloader by http://blog.csdn.net/ahri_j/article/details/72466231
# 通过之前的学习，已经知道网页的基本解析流程就是先通过 css/xpath 方法进行解析，然后再把值封装到 Item 中，如果有特殊需要的话还要对解析到的数据进行转换处理，这样当解析代码或者数据转换要求过多的时候，会导致代码量变得极为庞大，从而降低了可维护性。同时在 sipider 中编写过多的数据处理代码某种程度上也违背了单一职责的代码设计原则。我们需要使用一种更加简洁的方式来获取与处理网页数据，ItemLoader 就是用来完成这件事情的。
#
# ItemLoader 类位于 scrapy.loader ，它可以接收一个 Item 实例来指定要加载的 Item, 然后指定 response 或者 selector 来确定要解析的内容，最后提供了 add_css()、 add_xpath() 方法来对通过 css 、 xpath 解析赋值，还有 add_value() 方法来单独进行赋值。
# 在 ItemLoader 类中，提供了 default_output_processor 和 default_input_processor 来对数据的输入与输出进行解析，
# 如果我们需要只获取解析后的第一个值，可以指定 default_output_processor 为 TakeFirst() 即可，这是 Scrapy 提供的一个解析处理类，
# scrapy 提供 的 MapCompose 方法允许我们指定一系列的处理方法，Scrapy 会将 解析到的 list 中的值依次传递到每个方法中对值进行处理
#
# 首先定义一个 ItemLoader 类同时指定通用的 input/output 处理方法，然后在 parse 方法中声明 ItemLoader ，传递 Item 实例 和 response/selector。 通过 ItemLoader 的 add_css/add_xpath/add_value 来进行赋值。
# 如果对数据有特殊的处理，就在 Item 类的 Field 中传递 input_processor 和 output_processor 来指定处理函数，来完成整个数据的解析和处理。
#
