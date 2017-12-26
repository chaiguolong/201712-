#!/usr/bin/env python
# -*- coding:utf8 -*-

import re
# 讲正则表达式编译成pattern对象
pattern = re.compile(r'\d+')
# 使用search()查找匹配的子串，不存在匹配的子串将返回None
# 这里使用match（）无法完成匹配
m = pattern.search('hello 123456 789')
if m:
    # 使用Match获得分组信息
    print 'matching string:', m.group()
    # 起始位置和结束位置
    print 'position:', m.span()
