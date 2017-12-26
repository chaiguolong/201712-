# coding=utf-8
import re

pattern = re.compile('\d+\.+\d*')

result = pattern.findall("123.141414, 'bigcat', 232423423, 3.15")

for item in result:
    print item
