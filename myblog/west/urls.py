#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/10/22 15:48
# @Author  : RookieDay
# @Site    : 
# @File    : urls.py
# @Software: PyCharm Community Edition

from django.conf.urls import url,include
from django.contrib import admin
from myblog import views

urlpatterns = [
    url(r'^$',views.first_page_1),
 ]
