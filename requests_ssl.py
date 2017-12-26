#!/usr/bin/env python
# -*- coding:utf8 -*-

import requests
response = requests.get("https://www.baidu.com/", verify=True)

print response.text
