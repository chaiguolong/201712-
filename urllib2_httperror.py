import urllib2

requset = urllib2.Request('http://blog.baidu.com/itcast')

try:
    urllib2.urlopen(requset)
except urllib2.HTTPError, err:
    print err.code
    print err
