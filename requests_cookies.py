#!/usr/bin/env python
# -*- coding:utf8 -*-

import requests

response = requests.get("http://www.baidu.com/")

# 7.返回CookieJar对象
cookiejar = response.cookies

# 8.讲CookieJar转为字典:
cookiedict = requests.utils.dict_from_cookiejar(cookiejar)

print cookiejar

print cookiedict
