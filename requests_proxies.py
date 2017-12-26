#!/usr/bin/env python
# -*- coding:utf8 -*-

import requests

# 根据协议类型，选择不同的代理
proxies = {
    "http": "119.129.99.177:9797",
    "https": " 119.123.176.79:9000",
}

response = requests.get("http://www.baidu.com/", proxies=proxies)

print response.text
