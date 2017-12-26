#!/usr/bin/env python
# -*- coding:utf8 -*-

import re

p = re.compile(r'[\s\,\;]+')
print p.split('a,b;; c   d')
