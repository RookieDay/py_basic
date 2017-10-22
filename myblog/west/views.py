#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/10/22 15:24
# @Author  : RookieDay
# @Site    : 
# @File    : views.py
# @Software: PyCharm Community Edition

from django.http import HttpResponse

def first_page_1(request):
    return HttpResponse('<p>good</p>')