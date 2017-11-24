#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/11/24
# @Author  : RookieDay
# @Site    : 
# @File    : selenium_test
# @Github  : https://github.com/rookieday
# @Software: PyCharm Community Edition

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get('http://www.python.org')
assert 'Python' in driver.title
ele = driver.find_element_by_name('q')
ele.send_keys('pycon')
ele.send_keys(Keys.RETURN)
print(driver.page_source)
