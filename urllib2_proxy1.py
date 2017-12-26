# coding=utf-8
import urllib2

# 构建两个代理Handler,一个有代理IP，一个没有代理IP
httpproxy_handler = urllib2.ProxyHandler({"http": "180.137.232.76:53281"})
nullproxy_handler = urllib2.ProxyHandler({})

proxySwitch = True

# 通过urllib2.build_opener()方法使用这些代理Handler对象，创建自定义opener对象
# 根据代理开关是否打开，使用不同的代理模式
if proxySwitch:
    opener = urllib2.build_opener(httpproxy_handler)
else:
    opener = urllib2.build_opener(nullproxy_handler)

request = urllib2.Request("http://www.baidu.com")

# 1.如果这么写，只有使用opener.open()方法发送请求才能使用自定义代理，
# 而urlopen()则不适用自定义代理
response = opener.open(request)

# 2.如果这么写，及时将opener应用到全局，之后所有的，不管是opener.open()还是
# urlopen()发送请求，都将使用自定义代理
# urllib2.install_opener(openner)
# response = urlopen(request)

print response.read()
