#!/usr/bin/env python
# -*- coding:utf8 -*-

import json


strList = '[1, 2, 3, 4]'

strDict = '{"city": "北京", "name": "大猫"}'

print json.loads(strList)

print json.loads(strDict)
