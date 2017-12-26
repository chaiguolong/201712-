#!/usr/bin/env python
# -*- coding:utf8 -*-

import re

pattern = re.compile(r'\d+')

result = pattern.findall('hello 123456 789')
result1 = pattern.findall('one1two2three3four4', 0, 10)

print result
print result1
