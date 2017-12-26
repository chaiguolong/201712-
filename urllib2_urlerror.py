# coding=utf-8

import urllib2

request = urllib2.Request('http://www.lskdfll.com')

try:
    urllib2.urlopen(request, timeout=5)
except urllib2.URLError, err:
    print err
