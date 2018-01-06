#!/usr/bin/env python
# -*- coding:utf8 -*-

import json
import chardet

listStr = [1, 2, 3, 4]

tupleStr = (1, 2, 3, 4)

dictStr = {"city": "北京", "name": "大猫"}

print json.dumps(listStr)

print json.dumps(tupleStr)

print json.dumps(dictStr)

chardet.detect(json.dumps(dictStr))

print json.dumps(dictStr, ensure_ascii=False)

chardet.detect(json.dumps(dictStr, ensure_ascii=False))
