#!/usr/bin/env python
# -*- coding:utf8 -*-

from lxml import etree


html = etree.parse('hello.html')
result = html.xpath('//*[@class="bold"]')

print result[0].tag
