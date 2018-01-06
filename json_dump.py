#!/usr/bin/env python
# -*- coding:utf8 -*-

import json

listStr = [{"city": "北京"}, {"name": "大刘"}]

json.dump(listStr, open("listStr.json", "w"), ensure_ascii=False)

dictStr = {"city": "北京", "name": "大刘"}
json.dump(dictStr, open("dictStr.json", "w"), ensure_ascii=False)
